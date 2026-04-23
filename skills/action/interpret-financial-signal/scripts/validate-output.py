#!/usr/bin/env python3
"""Validate output structure for interpret-financial-signal."""

from __future__ import annotations

import argparse
import sys


REQUIRED_SECTIONS = [
    "一句话结论",
    "信息类型",
    "影响路径",
    "落地",
    "待确认",
    "边界",
]

RISKY_TERMS = [
    "保证通过",
    "肯定能批",
    "承诺额度",
    "固定费率",
    "内部规定是",
    "一定可以",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Output text to validate")
    args = parser.parse_args()

    missing = [section for section in REQUIRED_SECTIONS if section not in args.text]
    risky = [term for term in RISKY_TERMS if term in args.text]

    if missing:
        print("FAIL: missing sections -> " + ", ".join(missing))
        sys.exit(1)
    if risky:
        print("FAIL: found risky terms -> " + ", ".join(risky))
        sys.exit(1)
    print("PASS: output structure is complete")


if __name__ == "__main__":
    main()
