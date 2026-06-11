---
name: corporate-client-coverage-lens
description: Use when handling a corporate-client or banking task and you need a professional lens for prioritization, stakeholder differences, and safe next-step guidance.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 对公客户覆盖视角
  audience: [finance-learner, bank-practitioner]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.client-advance-framework
    - skill.action.market-corporate-client
    - skill.action.accompany-corporate-client
    - skill.action.report-decision-brief
  related_knowledge:
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.e-fu-tong
    - knowledge.banks.ceb.trade-finance.dian-fei-tong
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.economics.business-basics
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.reference.corporate-client-coverage-lens
  references_dir: references
  scripts_dir: scripts
---

# 对公客户覆盖视角 Skill

## Scope

这是一个 reference skill。
它不替你完成整套任务，而是先把问题拉回成熟对公客户覆盖视角，帮助你判断先看什么、先找谁、先推进什么、哪些话不能说满。

## When To Use

- 需要快速进入对公客户覆盖视角
- 需要识别老板、财务、业务负责人、内部协同方的关注点差异
- 需要先给稳健判断，再决定补读哪一个 action skill 或 knowledge 资产
- 需要避免把公开知识说成承诺、把模糊感觉说成结论

## Required Reads

1. `references/coverage-lens.md`
2. `references/stakeholder-map.md`
3. `references/invocation-rules.md`
4. `references/output-contract.md`
5. 按问题类型补读相关 skill 或 knowledge 正文

## Default Lens

- 先看客户当前正在发生什么经营或交易动作
- 先看真实卡点、决策链和协同链
- 先争取最小可推进动作，而不是一次讲满所有产品
- 先说清能判断什么、还缺什么、哪些内容不能承诺

## Priority Rules

1. 先判断真实问题是否成立。
2. 先判断关键对象是谁。
3. 先判断有没有最小推进动作。
4. 先守住边界和口径。

## Stakeholder Hints

- 老板：更关注结果、节奏、关键风险和是否值得继续推进
- 财务：更关注流程、对账、资金安排、控制性和落地细节
- 业务负责人：更关注执行摩擦、效率、客户体验和配合成本
- 内部协同方：更关注信息是否完整、动作是否清楚、边界是否明确

## Pairing Rules

- 首访或首次触达，优先补 `skill.action.market-corporate-client`
- 会后跟进、闭环和持续推进，优先补 `skill.action.accompany-corporate-client`
- 需要口头或书面汇报，优先补 `skill.action.report-decision-brief`
- 需要先判断问题与机会，再补 `skill.reference.problem-opportunity-framework`
- 需要把沟通推进成明确动作，再补 `skill.reference.client-advance-framework`
- 涉及公开产品、FAQ 或机构信息时，再补相关 `knowledge.*`

## Quality Gate

- 是否识别了关键对象及其关注点差异
- 是否明确区分了专业判断与公开依据
- 是否指出了还缺哪些关键事实
- 是否避免审批、授信、定价、时效承诺

## Script Hooks

- `scripts/build-context.py`：根据问题生成建议读取顺序和推荐资产
- `scripts/validate-output.py`：校验输出是否符合专业视角结构
