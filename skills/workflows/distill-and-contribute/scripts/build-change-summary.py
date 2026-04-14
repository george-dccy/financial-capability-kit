#!/usr/bin/env python3
from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a short change summary for distillation work.")
    parser.add_argument("--action", required=True, choices=["create", "extend", "revise", "promote-private-to-public"])
    parser.add_argument("--target", required=True)
    parser.add_argument("--mode", default="private-first", choices=["private-first", "public-candidate"])
    parser.add_argument("--file", action="append", default=[])
    parser.add_argument("--note", action="append", default=[])
    args = parser.parse_args()

    print(f"# Change Summary\n")
    print(f"- Action: `{args.action}`")
    print(f"- Target: `{args.target}`")
    print(f"- Mode: `{args.mode}`")
    if args.file:
        print(f"- Files:")
        for item in args.file:
            print(f"  - `{item}`")
    if args.note:
        print(f"- Notes:")
        for item in args.note:
            print(f"  - {item}")


if __name__ == "__main__":
    main()
