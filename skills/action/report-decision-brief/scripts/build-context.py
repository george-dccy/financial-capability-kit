#!/usr/bin/env python3
"""Build routing context for report-decision-brief."""

import argparse
import json
import re


KNOWLEDGE_RULES = [
    (r"结算|账户|收付|回单|对账", "knowledge.banks.ceb.corporate-settlement.basic-settlement"),
    (r"e付通|订单|账单|开票|协同", "knowledge.banks.ceb.transaction-banking.e-fu-tong"),
    (r"电费证|国内证|福费廷|电网", "knowledge.banks.ceb.trade-finance.dian-fei-tong"),
    (r"复盘|优先级|执行节奏|管理", "knowledge.common.banker-thinking.top-performer"),
    (r"利率|通胀|周期|宏观|现金流", "knowledge.common.economics.business-basics"),
    (r"心理|信任|偏差|沟通", "knowledge.common.psychology.business-communication"),
]


def route_knowledge(topic: str) -> list[str]:
    hits: list[str] = []
    for pattern, knowledge_id in KNOWLEDGE_RULES:
        if re.search(pattern, topic):
            hits.append(knowledge_id)
    return hits or ["knowledge.banks.ceb.corporate-settlement.basic-settlement"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True, help="Topic for leader report")
    args = parser.parse_args()
    payload = {
        "skill": "report-decision-brief",
        "recommended_knowledge": route_knowledge(args.topic),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
