#!/usr/bin/env python3
"""Build routing context for market-corporate-client."""

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class KnowledgeRule:
    pattern: str
    knowledge_id: str
    priority: int
    reason: str


KNOWLEDGE_RULES = [
    KnowledgeRule(
        pattern=r"结算|账户|收付|回单|对账|付款流程|授权管理",
        knowledge_id="knowledge.banks.ceb.corporate-settlement.basic-settlement",
        priority=95,
        reason="命中基础结算场景关键词",
    ),
    KnowledgeRule(
        pattern=r"e付通|订单|账单|开票|协同|供应链|融e链|1\+N|保理|应收账款|账期|交易链|线上化确认|线上化融资",
        knowledge_id="knowledge.banks.ceb.transaction-banking.yangguang-e-pay",
        priority=120,
        reason="命中交易协同场景关键词",
    ),
    KnowledgeRule(
        pattern=r"电费证|电费|电网|国内证|福费廷|电费缴纳|电费结算|月度缴费|缴费优化|电费支付",
        knowledge_id="knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate",
        priority=120,
        reason="命中电费场景融资关键词",
    ),
    KnowledgeRule(
        pattern=r"思维|复盘|优先级|执行节奏",
        knowledge_id="knowledge.common.banker-thinking.top-performer",
        priority=35,
        reason="命中推进方法关键词",
    ),
    KnowledgeRule(
        pattern=r"利率|通胀|周期|宏观|现金流",
        knowledge_id="knowledge.common.economics.business-basics",
        priority=30,
        reason="命中经营环境解释关键词",
    ),
    KnowledgeRule(
        pattern=r"销售|异议|洞察|推进|开场",
        knowledge_id="knowledge.common.sales.consultative-b2b",
        priority=45,
        reason="命中营销沟通关键词",
    ),
    KnowledgeRule(
        pattern=r"心理|信任|偏差|沟通摩擦",
        knowledge_id="knowledge.common.psychology.business-communication",
        priority=30,
        reason="命中信任与沟通关键词",
    ),
]

DEMO_PATTERN = re.compile(r"演示|会上|业务会|汇报|示例|问答")

INDUSTRY_SUPPLY_CHAIN = re.compile(
    r"制造|加工|分包|分销|贸易|批发|零部件|原材料|供应商|采购"
)
INDUSTRY_ENERGY = re.compile(
    r"化工|钢铁|有色金属|数据中心|园区|综合体|高耗能|能耗|用电"
)

DEFAULT_PRIMARY_KNOWLEDGE = "knowledge.banks.ceb.corporate-settlement.basic-settlement"


def route_knowledge(question: str) -> list[dict[str, object]]:
    scored: list[dict[str, object]] = []
    seen: set[str] = set()
    for rule in KNOWLEDGE_RULES:
        if re.search(rule.pattern, question) and rule.knowledge_id not in seen:
            seen.add(rule.knowledge_id)
            scored.append(
                {
                    "knowledge_id": rule.knowledge_id,
                    "priority": rule.priority,
                    "reason": rule.reason,
                }
            )
    if not scored:
        fallback = _infer_fallback(question)
        scored.append(
            {
                "knowledge_id": fallback["knowledge_id"],
                "priority": 90,
                "reason": fallback["reason"],
            }
        )
    scored.sort(key=lambda item: int(item["priority"]), reverse=True)
    return scored


def _infer_fallback(question: str) -> dict[str, str]:
    if INDUSTRY_SUPPLY_CHAIN.search(question):
        return {
            "knowledge_id": "knowledge.banks.ceb.transaction-banking.yangguang-e-pay",
            "reason": "行业特征匹配供应链场景，默认走 e付通",
        }
    if INDUSTRY_ENERGY.search(question):
        return {
            "knowledge_id": "knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate",
            "reason": "行业特征匹配能源缴费场景，默认走电费通",
        }
    return {
        "knowledge_id": DEFAULT_PRIMARY_KNOWLEDGE,
        "reason": "未命中特定关键词，默认先走基础结算场景",
    }


def infer_mode(question: str) -> str:
    if DEMO_PATTERN.search(question):
        return "meeting-demo"
    if re.search(r"首次|第一次|拜访|开场|触达", question):
        return "first-touch"
    return "routine-marketing"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="Question text")
    args = parser.parse_args()

    routed = route_knowledge(args.question)
    primary = routed[0]["knowledge_id"]
    payload = {
        "skill": "market-corporate-client",
        "mode": infer_mode(args.question),
        "recommended_knowledge": [item["knowledge_id"] for item in routed],
        "primary_knowledge": primary,
        "backup_knowledge": routed[1]["knowledge_id"] if len(routed) > 1 else None,
        "routing_reasons": routed,
        "reading_order": [
            "references/pre-call-diagnosis.md",
            "references/opening-playbook.md",
            "references/knowledge-routing.md",
            f"{primary} -> README.md / modules/* / faq.md / sources.md",
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
