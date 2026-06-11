---
name: accompany-corporate-client
description: Use when managing follow-up, issue closure, and relationship progression after a corporate client conversation.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 对公客户持续推进
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.client-advance-framework
    - skill.reference.team-followup-framework
    - skill.reference.corporate-client-coverage-lens
  related_knowledge:
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.e-fu-tong
    - knowledge.banks.ceb.trade-finance.dian-fei-tong
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.action.accompany-corporate-client
  references_dir: references
  scripts_dir: scripts
---

# 对公客户持续推进 Skill

## Scope

这是一个 action skill。
它负责组织客户关系推进、问题闭环和下一次触达计划，不替代团队管理框架本体。

## When To Use

- 会后跟进，需要安排本次动作和下次触达
- 客户问题悬而未决，需要列清闭环路径
- 需要把关系经营、问题回应和内部协同放进一张推进表里

## Required Reads

1. `references/follow-up-cadence.md`
2. `references/issue-closure-model.md`
3. `references/knowledge-routing.md`
4. `skill.reference.client-advance-framework`
5. `skill.reference.team-followup-framework`

## Execution Rule

1. 先用 `skill.reference.client-advance-framework` 判断当前推进节奏和下一步动作
2. 再用 `skill.reference.team-followup-framework` 组织内部协同闭环
3. 需要补充公开事实时，再按 `references/knowledge-routing.md` 调用对应 knowledge

## Input Contract

最低输入：

- 当前客户关系阶段
- 待回应问题或未闭环事项
- 需要协同的内部角色
- 下一次触达希望达成的目标

## Output Contract

必须包含：

1. 客户关系温度
2. 待回应问题清单
3. 本次跟进动作
4. 内部协同清单
5. 下一次触达计划

## Quality Gate

- 是否同时覆盖客户动作和内部动作
- 是否把下一次触达目标写清楚
- 是否把待回应问题和已闭环事项区分开
- 是否避免承诺未核实的事实或口径

## Script Hooks

- `scripts/build-context.py`
- `scripts/validate-output.py`
