#!/usr/bin/env python3
"""Build context routing for the corporate-client-coverage-lens skill."""

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class AssetRule:
    pattern: str
    asset_id: str
    path: str
    priority: int
    reason: str


ACTION_RULES = [
    AssetRule(
        pattern=r"汇报|领导|拍板|上提|口头汇报|书面汇报",
        asset_id="skill.action.report-decision-brief",
        path="skills/action/report-decision-brief/SKILL.md",
        priority=120,
        reason="命中汇报或拍板场景",
    ),
    AssetRule(
        pattern=r"跟进|复盘|闭环|陪伴|推进|协同",
        asset_id="skill.action.accompany-corporate-client",
        path="skills/action/accompany-corporate-client/SKILL.md",
        priority=110,
        reason="命中持续跟进与协同场景",
    ),
    AssetRule(
        pattern=r"首访|第一次|开场|拜访|触达|营销|切入口",
        asset_id="skill.action.market-corporate-client",
        path="skills/action/market-corporate-client/SKILL.md",
        priority=100,
        reason="命中首访和首次触达场景",
    ),
]

REFERENCE_RULES = [
    AssetRule(
        pattern=r"卡点|问题|机会|判断|优先级|切入",
        asset_id="skill.reference.problem-opportunity-framework",
        path="skills/reference/problem-opportunity-framework/SKILL.md",
        priority=100,
        reason="命中问题与机会判断场景",
    ),
    AssetRule(
        pattern=r"推进|下一步|动作|跟进|协同|闭环|时间点",
        asset_id="skill.reference.client-advance-framework",
        path="skills/reference/client-advance-framework/SKILL.md",
        priority=90,
        reason="命中推进动作与协同设计场景",
    ),
]

KNOWLEDGE_RULES = [
    AssetRule(
        pattern=r"结算|账户|收款|付款|回单|对账|权限",
        asset_id="knowledge.banks.ceb.corporate-settlement.basic-settlement",
        path="knowledge/banks/ceb/corporate-settlement/basic-settlement/README.md",
        priority=100,
        reason="命中对公基础结算关键词",
    ),
    AssetRule(
        pattern=r"e付通|订单|账单|开票|协同|供应链",
        asset_id="knowledge.banks.ceb.transaction-banking.e-fu-tong",
        path="knowledge/banks/ceb/transaction-banking/e-fu-tong/README.md",
        priority=110,
        reason="命中交易协同关键词",
    ),
    AssetRule(
        pattern=r"电费证|电费|电网|国内证|福费廷",
        asset_id="knowledge.banks.ceb.trade-finance.dian-fei-tong",
        path="knowledge/banks/ceb/trade-finance/dian-fei-tong/README.md",
        priority=110,
        reason="命中电费证和国内证关键词",
    ),
]

DEFAULT_REFERENCES = [
    {
        "asset_id": "skill.reference.problem-opportunity-framework",
        "path": "skills/reference/problem-opportunity-framework/SKILL.md",
        "priority": 80,
        "reason": "默认补充问题与机会判断框架",
    },
    {
        "asset_id": "skill.reference.client-advance-framework",
        "path": "skills/reference/client-advance-framework/SKILL.md",
        "priority": 70,
        "reason": "默认补充下一步推进框架",
    },
]

STAKEHOLDER_PATTERNS = [
    ("老板", r"老板|总经理|法人|一把手"),
    ("财务", r"财务|会计|资金主管"),
    ("业务负责人", r"业务负责人|销售负责人|运营负责人"),
    ("内部协同方", r"同事|协同|审批|产品经理|中后台"),
]


def collect_matches(question: str, rules: list[AssetRule]) -> list[dict[str, object]]:
    scored: list[dict[str, object]] = []
    seen: set[str] = set()
    for rule in rules:
        if re.search(rule.pattern, question) and rule.asset_id not in seen:
            seen.add(rule.asset_id)
            scored.append(
                {
                    "asset_id": rule.asset_id,
                    "path": rule.path,
                    "priority": rule.priority,
                    "reason": rule.reason,
                }
            )
    scored.sort(key=lambda item: int(item["priority"]), reverse=True)
    return scored


def infer_scene_hint(question: str) -> str:
    if re.search(r"汇报|领导|拍板|上提", question):
        return "reporting"
    if re.search(r"首访|首次|第一次|拜访|开场|触达", question):
        return "first-touch"
    if re.search(r"跟进|陪伴|复盘|闭环|协同|推进", question):
        return "follow-up"
    return "general-consulting"


def infer_stakeholders(question: str) -> list[str]:
    found: list[str] = []
    for label, pattern in STAKEHOLDER_PATTERNS:
        if re.search(pattern, question):
            found.append(label)
    return found or ["老板", "财务", "业务负责人"]


def default_actions(scene_hint: str) -> list[dict[str, object]]:
    mapping = {
        "reporting": {
            "asset_id": "skill.action.report-decision-brief",
            "path": "skills/action/report-decision-brief/SKILL.md",
            "priority": 100,
            "reason": "根据场景推断优先进入汇报与拍板 action skill",
        },
        "first-touch": {
            "asset_id": "skill.action.market-corporate-client",
            "path": "skills/action/market-corporate-client/SKILL.md",
            "priority": 100,
            "reason": "根据场景推断优先进入首访推进 action skill",
        },
        "follow-up": {
            "asset_id": "skill.action.accompany-corporate-client",
            "path": "skills/action/accompany-corporate-client/SKILL.md",
            "priority": 100,
            "reason": "根据场景推断优先进入持续推进 action skill",
        },
    }
    return [mapping[scene_hint]] if scene_hint in mapping else []


def build_reading_order(*groups: list[dict[str, object]]) -> list[str]:
    order = [
        "references/coverage-lens.md",
        "references/stakeholder-map.md",
        "references/invocation-rules.md",
        "references/output-contract.md",
    ]
    for group in groups:
        for item in group:
            path = str(item["path"])
            if path not in order:
                order.append(path)
    return order


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", required=True, help="User question or scenario text")
    args = parser.parse_args()

    scene_hint = infer_scene_hint(args.question)
    actions = collect_matches(args.question, ACTION_RULES) or default_actions(scene_hint)
    references = collect_matches(args.question, REFERENCE_RULES) or list(DEFAULT_REFERENCES)
    knowledge = collect_matches(args.question, KNOWLEDGE_RULES)

    payload = {
        "skill": "corporate-client-coverage-lens",
        "scene_hint": scene_hint,
        "stakeholder_hint": infer_stakeholders(args.question),
        "recommended_actions": [item["asset_id"] for item in actions],
        "recommended_references": [item["asset_id"] for item in references],
        "recommended_knowledge": [item["asset_id"] for item in knowledge],
        "routing_reasons": {
            "actions": actions,
            "references": references,
            "knowledge": knowledge,
        },
        "reading_order": build_reading_order(actions, references, knowledge),
        "references": [
            "references/coverage-lens.md",
            "references/stakeholder-map.md",
            "references/invocation-rules.md",
            "references/output-contract.md",
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
