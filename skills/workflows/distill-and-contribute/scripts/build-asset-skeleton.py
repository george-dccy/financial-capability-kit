#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATES = {
    "role": ["SKILL.md", "references/", "scripts/"],
    "workflow": ["SKILL.md", "references/", "scripts/"],
    "knowledge-pack": ["README.md", "pack.json", "faq.md", "sources.md", "modules/"],
    "method": ["README.md", "method.json", "frameworks.md", "examples.md"],
}


def build_path(kind: str, slug: str, mode: str, category: str, institution: str) -> str:
    if mode == "private-first":
        prefix = Path("workspace/private")
    else:
        prefix = Path(".")

    if kind == "role":
        return str(prefix / "skills" / "roles" / slug)
    if kind == "workflow":
        return str(prefix / "skills" / "workflows" / slug)
    if kind == "knowledge-pack":
        base = prefix / "knowledge-packs"
        if institution:
            return str(base / "banks" / institution / category / slug)
        return str(base / "common" / category / slug)
    if kind == "method":
        return str(prefix / "methods" / category / slug)
    raise ValueError(f"Unsupported kind: {kind}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a recommended asset skeleton.")
    parser.add_argument("--kind", required=True, choices=["role", "workflow", "knowledge-pack", "method"])
    parser.add_argument("--slug", required=True)
    parser.add_argument("--mode", default="private-first", choices=["private-first", "public-candidate"])
    parser.add_argument("--category", default="reusable")
    parser.add_argument("--institution", default="")
    parser.add_argument("--create", action="store_true")
    args = parser.parse_args()

    path = Path(build_path(args.kind, args.slug, args.mode, args.category, args.institution))
    files = TEMPLATES[args.kind]

    if args.create:
        path.mkdir(parents=True, exist_ok=True)
        for entry in files:
            target = path / entry
            if entry.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch(exist_ok=True)

    print(
        json.dumps(
            {
                "kind": args.kind,
                "mode": args.mode,
                "path": path.as_posix(),
                "files": files,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
