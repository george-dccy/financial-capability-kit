"""Financial Capability Kit - Agent Loop Guards.

This module provides verification gates for the fincap无人值守循环.
Each guard returns (passed: bool, reason: str).
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from dataclasses import dataclass


# Prohibited keywords that indicate model drift or incorrect project framing.
# Matches against roadmap-governance.md "模型漂移防护" section.
DRIFT_KEYWORDS: list[str] = [
    "银行客服",          # bank customer service project framing
    "人格蒸馏",          # personality distillation
    "客服知识库",        # customer service knowledge base
    "角色设定",          # persona设定
    "doubao专属",        # doubao-specific naming (deprecated)
]

# Prohibited patterns for compliance - any of these in output means stop immediately.
COMPLIANCE_STOP_PATTERNS: list[str] = [
    r"授信",
    r"审批.*承诺",
    r"定价.*承诺",
    r"时效.*承诺",
    r"保证.*收益",
    r"内部口径",
]


@dataclass(frozen=True)
class GuardResult:
    """Result of a single guard check."""

    passed: bool
    guard_name: str
    reason: str = ""


def git_command(path: Path, *args: str, check: bool = False) -> subprocess.CompletedProcess[str]:
    """Run a git command with safe.directory configured."""
    cmd = ["git", "-c", f"safe.directory={path.as_posix()}", *args]
    return subprocess.run(
        cmd,
        cwd=str(path),
        text=True,
        capture_output=True,
        check=check,
    )


def git_status_short(path: Path) -> str:
    """Return short git status output, empty string if clean."""
    result = git_command(path, "status", "--short")
    return result.stdout.strip()


def public_repo_dirty_check(root: Path) -> GuardResult:
    """Check if public repo has unexpected changes before a run.

    Stop condition: public repo has uncommitted changes before agent run.
    """
    status = git_status_short(root)
    if status:
        return GuardResult(
            passed=False,
            guard_name="public_repo_dirty_check",
            reason=f"Public repo has unexpected changes before run:\n{status}",
        )
    return GuardResult(passed=True, guard_name="public_repo_dirty_check")


def workspace_dirty_check(workspace: Path) -> GuardResult:
    """Check if workspace has uncommitted changes.

    Unlike public repo, workspace dirtiness is informational - we still proceed
    but record it for the run report.
    """
    status = git_status_short(workspace)
    if status:
        return GuardResult(
            passed=True,  # informational, not a hard stop
            guard_name="workspace_dirty_check",
            reason=f"Workspace has uncommitted changes:\n{status}",
        )
    return GuardResult(passed=True, guard_name="workspace_dirty_check", reason="Workspace is clean")


def route_conflict_keyword_check(text: str) -> GuardResult:
    """Check text for route conflict keywords indicating model drift.

    Stop condition: prohibited keywords found that violate roadmap governance.
    """
    for keyword in DRIFT_KEYWORDS:
        pattern = re.compile(re.escape(keyword))
        if pattern.search(text):
            return GuardResult(
                passed=False,
                guard_name="route_conflict_keyword_check",
                reason=f"Prohibited drift keyword found: '{keyword}'",
            )
    return GuardResult(passed=True, guard_name="route_conflict_keyword_check")


def queue_status_check(status: str) -> GuardResult:
    """Verify queue item status is 'ready' before running.

    Stop condition: queue item status is not 'ready'.
    """
    valid_statuses = {"ready", "in-progress"}
    if status not in valid_statuses:
        return GuardResult(
            passed=False,
            guard_name="queue_status_check",
            reason=f"Queue item status is '{status}', expected 'ready' or 'in-progress'",
        )
    return GuardResult(passed=True, guard_name="queue_status_check")


def registry_json_parse_check(root: Path) -> GuardResult:
    """Legacy guard - registry JSON files have been removed.

    Skill metadata is now in SKILL.md frontmatter. This guard is a no-op.
    """
    return GuardResult(passed=True, guard_name="registry_json_parse_check")


def git_diff_check(root: Path) -> GuardResult:
    """Run git diff --check to detect problematic whitespace.

    Stop condition: git reports whitespace errors.
    """
    result = git_command(root, "diff", "--check")
    output = (result.stdout + result.stderr).strip()

    # Filter out CRLF conversion noise
    material_lines = [
        line
        for line in output.splitlines()
        if "LF will be replaced by CRLF" not in line
        and "CRLF will be replaced by LF" not in line
        and line.strip()
    ]

    if material_lines:
        return GuardResult(
            passed=False,
            guard_name="git_diff_check",
            reason="git diff --check failed:\n" + "\n".join(material_lines),
        )
    return GuardResult(passed=True, guard_name="git_diff_check")


def compliance_stop_check(text: str) -> GuardResult:
    """Check for compliance stop patterns that require immediate halt.

    Stop condition: compliance-relevant content that should not be generated
    without proper sourcing, internal data, or authority.
    """
    for pattern_str in COMPLIANCE_STOP_PATTERNS:
        pattern = re.compile(pattern_str)
        if pattern.search(text):
            return GuardResult(
                passed=False,
                guard_name="compliance_stop_check",
                reason=f"Compliance stop pattern matched: '{pattern_str}'",
            )
    return GuardResult(passed=True, guard_name="compliance_stop_check")


def run_all_pre_run_guards(
    root: Path,
    workspace: Path,
    queue_item_status: str,
) -> list[GuardResult]:
    """Run all guards that must pass before an agent run starts.

    Returns list of GuardResults. Any non-passed result indicates a stop condition.
    """
    results: list[GuardResult] = []

    # Critical guards - stop on failure
    results.append(public_repo_dirty_check(root))
    results.append(queue_status_check(queue_item_status))
    results.append(registry_json_parse_check(root))

    # Informational guards - always record but don't stop
    results.append(workspace_dirty_check(workspace))

    # Post-run guards (git_diff_check) should be called separately after agent run

    return results


def format_guard_results(results: list[GuardResult]) -> str:
    """Format guard results for run report."""
    lines = []
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        lines.append(f"- [{status}] {r.guard_name}: {r.reason}")
    return "\n".join(lines)
