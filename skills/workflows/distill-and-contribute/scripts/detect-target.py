#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json


def classify(text: str) -> dict[str, str]:
    lowered = text.lower()
    if any(word in text for word in ["岗位", "客户经理", "理财经理", "产品经理", "领导层"]) or "role" in lowered:
        return {"asset_kind": "role", "recommended_root": "skills/roles"}
    if any(word in text for word in ["流程", "复盘", "汇报", "跟进", "workflow"]) or "input" in lowered:
        return {"asset_kind": "workflow", "recommended_root": "skills/workflows"}
    if any(word in text for word in ["知识包", "产品介绍", "公开知识", "faq", "sources"]) or "knowledge" in lowered:
        return {"asset_kind": "knowledge-pack", "recommended_root": "knowledge-packs/common"}
    if any(word in text for word in ["方法", "框架", "拆解", "推进", "汇报法", "管理法"]) or "method" in lowered:
        return {"asset_kind": "method", "recommended_root": "methods/reusable"}
    return {"asset_kind": "unknown", "recommended_root": "workspace/private"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend where a new asset should live.")
    parser.add_argument("--text", default="", help="Source text or task summary to classify.")
    parser.add_argument(
        "--mode",
        default="private-first",
        choices=["private-first", "public-candidate"],
        help="Preferred drafting mode.",
    )
    args = parser.parse_args()

    if not args.text:
        print(
            json.dumps(
                {
                    "default_mode": "private-first",
                    "private_root": "workspace/private",
                    "message": "Provide --text to classify the target asset.",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    result = classify(args.text)
    result["mode"] = args.mode
    if args.mode == "private-first":
        result["draft_root"] = "workspace/private"
    else:
        result["draft_root"] = result["recommended_root"]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
