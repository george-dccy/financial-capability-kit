#!/usr/bin/env python3
"""Build routing context for interpret-financial-signal."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class RouteRule:
    pattern: str
    signal_type: str
    related_assets: list[str]
    reason: str


RULES = [
    RouteRule(
        pattern=r"政策|监管|通知|办法|意见|规则|条例|央行|金融监管|证监|交易商协会",
        signal_type="policy",
        related_assets=[
            "skill.reference.problem-opportunity-framework",
            "skill.action.report-decision-brief",
        ],
        reason="命中政策或监管信息",
    ),
    RouteRule(
        pattern=r"新闻|报道|发布|公告|采访|会议|论坛|发布会",
        signal_type="news",
        related_assets=[
            "skill.reference.problem-opportunity-framework",
            "skill.action.distill-and-curate",
        ],
        reason="命中新闻或公开动态",
    ),
    RouteRule(
        pattern=r"产品|方案|服务|功能|办理|申请|额度|融资|结算|账户|电费通|e付通|国内证|福费廷",
        signal_type="product",
        related_assets=[
            "skill.reference.corporate-client-coverage-lens",
            "skill.action.market-corporate-client",
            "knowledge.banks.ceb.transaction-banking.yangguang-e-pay",
            "knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate",
        ],
        reason="命中产品或服务方案",
    ),
    RouteRule(
        pattern=r"竞品|同业|他行|招行|工行|建行|农行|中行|平安|微众|网商|互联网平台",
        signal_type="competitor",
        related_assets=[
            "skill.reference.problem-opportunity-framework",
            "skill.action.distill-and-curate",
        ],
        reason="命中竞品或同业动作",
    ),
    RouteRule(
        pattern=r"客户|企业|公司|拜访|订单|项目|扩产|减产|股权|中标|诉讼|舆情|风险",
        signal_type="client",
        related_assets=[
            "skill.reference.corporate-client-coverage-lens",
            "skill.reference.client-advance-framework",
            "skill.action.accompany-corporate-client",
        ],
        reason="命中客户变化或客户线索",
    ),
    RouteRule(
        pattern=r"利率|汇率|通胀|经济|行业|周期|价格|大宗|出口|内需|现金流",
        signal_type="market",
        related_assets=[
            "knowledge.common.economics.business-basics",
            "skill.reference.problem-opportunity-framework",
        ],
        reason="命中市场或经营环境变化",
    ),
    RouteRule(
        pattern=r"方法|skill|技能|复盘|经验|话术|表达|框架|沉淀|学习",
        signal_type="capability",
        related_assets=[
            "skill.action.distill-and-curate",
            "knowledge.common.banker-thinking.top-performer",
        ],
        reason="命中能力素材或经验沉淀",
    ),
]


def infer_relevance(text: str) -> str:
    if re.search(r"领导|汇报|拍板|简报", text):
        return "领导汇报与拍板"
    if re.search(r"团队|跟进|管理|检查|复盘", text):
        return "基层管理与跟进"
    if re.search(r"客户经理|拜访|营销|客户|推进|方案", text):
        return "银行员工业务推进"
    if re.search(r"公开|咨询|客户问|用户问", text):
        return "公开咨询"
    return "金融能力成长"


def route(text: str) -> dict[str, object]:
    matches = [rule for rule in RULES if re.search(rule.pattern, text)]
    primary = matches[0] if matches else None
    assets: list[str] = []
    reasons: list[str] = []
    for rule in matches:
        reasons.append(rule.reason)
        for asset in rule.related_assets:
            if asset not in assets:
                assets.append(asset)

    if primary is None:
        signal_type = "other"
        reasons.append("未命中特定类型，按通用信息解读处理")
        assets = [
            "skill.reference.problem-opportunity-framework",
            "skill.action.distill-and-curate",
        ]
    else:
        signal_type = primary.signal_type

    return {
        "skill": "interpret-financial-signal",
        "signal_type": signal_type,
        "relevance": infer_relevance(text),
        "recommended_assets": assets[:8],
        "routing_reasons": reasons,
        "reading_order": [
            "references/signal-classification.md",
            "references/interpretation-playbook.md",
            "references/landing-directions.md",
            "references/knowledge-routing.md",
            "then read recommended_assets as needed",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Signal text")
    args = parser.parse_args()
    print(json.dumps(route(args.text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
