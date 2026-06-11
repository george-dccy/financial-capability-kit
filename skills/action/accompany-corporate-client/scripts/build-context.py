#!/usr/bin/env python3
"""Build routing context for accompany-corporate-client."""

import argparse
import json
import re


KNOWLEDGE_RULES = [
    (r"结算|账户|收付|回单|对账", "knowledge.banks.ceb.corporate-settlement.basic-settlement"),
    (r"e付通|订单|账单|开票|协同", "knowledge.banks.ceb.transaction-banking.e-fu-tong"),
    (r"电费证|电费|电网|国内证|福费廷", "knowledge.banks.ceb.trade-finance.dian-fei-tong"),
    (r"复盘|关系经营|优先级|执行节奏", "knowledge.common.banker-thinking.top-performer"),
    (r"销售|异议|推进|顾问式", "knowledge.common.sales.consultative-b2b"),
    (r"心理|信任|偏差|沟通摩擦|冲突", "knowledge.common.psychology.business-communication"),
]


def route_knowledge(question: str) -> list[str]:
    hits: list[str] = []
    for pattern, knowledge_id in KNOWLEDGE_RULES:
        if re.search(pattern, question):
            hits.append(knowledge_id)
    return hits or ["knowledge.banks.ceb.corporate-settlement.basic-settlement"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="Question text")
    args = parser.parse_args()
    payload = {
        "skill": "accompany-corporate-client",
        "recommended_knowledge": route_knowledge(args.question),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
