---
name: market-corporate-client
description: Use when preparing or simulating a first-touch corporate client conversation and you need a structured opening, diagnosis path, and next-step design.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 对公客户首访推进
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.client-advance-framework
    - skill.reference.corporate-client-coverage-lens
  related_knowledge:
    - knowledge.banks.ceb.transaction-banking.product-catalog
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.e-fu-tong
    - knowledge.banks.ceb.trade-finance.dian-fei-tong
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.economics.business-basics
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.action.market-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户首访推进 Skill

## Scope

这是一个 action skill。
它聚焦“营销前”和“首次接触”，负责组织输入、调用参考框架、补充公开知识，并直接产出可拿去用的首访推进方案。

## When To Use

- 计划首次拜访客户，想明确开场与切入口
- 客户意向模糊，需要先把场景和痛点说清楚
- 需要为业务会议或首次电话准备一版结构化打法

## Required Reads

1. `references/pre-call-diagnosis.md`
2. `references/opening-playbook.md`
3. `references/knowledge-routing.md`
4. `skill.reference.problem-opportunity-framework`
5. `skill.reference.client-advance-framework`
6. 涉及光大交易银行产品名时，先读 `knowledge/banks/ceb/transaction-banking/product-catalog/products.md`
7. 命中 knowledge 后，读取对应 `README.md`、`modules/*`、`faq.md`、`sources.md`

## Execution Rule

1. 先用 `skill.reference.problem-opportunity-framework` 判断客户卡点与机会
2. 再用 `skill.reference.client-advance-framework` 明确首次会谈目标和最小推进动作
3. 如涉及光大交易银行产品，先用产品目录核验产品名称；未在目录内的名称不得输出
4. 最后按 `references/knowledge-routing.md` 补相应公开知识

## Input Contract

最低输入：

- 行业
- 当前卡点
- 会谈对象
- 希望达成的最小结果

## Output Contract

输出至少包含：

1. 客户场景初判
2. 推荐切入口（1-3 个）
3. 首次会谈目标
4. 不宜过早触达的话题
5. 会后推进动作
6. 客户常见追问与建议回答（公开口径）

## Quality Gate

- 是否先输出场景判断，再输出产品建议
- 是否先调用 reference skill，再落到具体 knowledge
- 是否包含明确下一步时间点与责任人
- 是否避免审批、额度、费率、时效承诺

## Script Hooks

- `scripts/build-context.py`：根据问题路由 knowledge 并返回建议读取顺序
- `scripts/validate-output.py`：校验结构完整性与承诺风险
