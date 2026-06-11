---
name: report-decision-brief
description: Use when turning a complex banking or finance topic into a concise, decision-ready oral or written brief.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: communicate
  display_name_zh: 向领导汇报与拍板
  audience: [finance-learner, bank-practitioner, manager]
  related_skills:
    - skill.reference.decision-brief-framework
    - skill.reference.team-followup-framework
  related_knowledge:
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.e-fu-tong
    - knowledge.banks.ceb.trade-finance.dian-fei-tong
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.economics.business-basics
    - knowledge.common.psychology.business-communication
  related_prompts:
    - prompt.skill.action.report-decision-brief
  references_dir: references
  scripts_dir: scripts
---

# 向领导汇报与拍板 Skill

## Scope

这是一个 action skill。
它负责组织汇报所需事实、调用拍板简报框架，并输出可直接拿去讲或写的结果。

## When To Use

- 需要把复杂事项快速整理成领导可判断的版本
- 需要准备 30 秒口头汇报或一页式书面简报
- 需要明确哪些事情需要拍板，哪些只是同步

## Required Reads

1. `references/report-structure.md`
2. `references/decision-signals.md`
3. `references/knowledge-routing.md`
4. `skill.reference.decision-brief-framework`

## Execution Rule

1. 先采集本阶段最影响判断的事实和变化
2. 再用 `skill.reference.decision-brief-framework` 组织成可拍板结构
3. 涉及公开产品事实时，再补对应 knowledge 依据

## Input Contract

最低输入：

- 汇报类型
- 当前进展
- 当前卡点
- 期望领导拍板或支持的事项

## Output Contract

必须包含：

1. 一句话结论
2. 本周或本阶段关键事实
3. 当前卡点
4. 建议动作
5. 需要领导拍板项

## Quality Gate

- 是否先讲判断，再讲材料
- 是否只保留影响拍板的信息
- 是否把“建议动作”和“拍板项”区分清楚
- 是否避免空泛表态和无依据承诺

## Script Hooks

- `scripts/build-context.py`：按主题推荐需要引用的 knowledge
- `scripts/validate-output.py`：校验汇报结构与决策字段
