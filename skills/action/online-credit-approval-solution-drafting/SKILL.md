---
name: skill.action.online-credit-approval-solution-drafting
description: Use when you need to collect information through Q&A and draft an online credit automated approval business proposal, especially the credit-solution section.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 线上授信自动化审批业务方案辅助撰写
  audience: [bank-practitioner, manager]
  support_files:
    - README.md
    - checklist.md
    - examples.md
    - output-contract.md
    - related-assets.md
  related_skills:
    - skill.reference.online-credit-solution-lens
    - skill.reference.online-credit-admission-strategy-patterns
    - skill.reference.executive-briefing-decision-support
  related_prompts:
    - prompt.skill.action.online-credit-approval-solution-drafting
---

# 线上授信自动化审批业务方案辅助撰写 Skill

## Scope

这是一个 action skill。
它负责通过问答收集信息、识别缺口，并输出线上授信自动化审批业务方案的章节草稿，尤其聚焦“授信方案”部分。

## When To Use

- 分行需要起草线上授信自动化审批业务方案
- 已有部分材料，但不知道还缺什么
- 需要把“授信方案”章节先拉成可讨论草稿
- 需要把准入策略、额度、期限、用途、还款方式等内容先结构化

## Required Reads

1. `README.md`
2. `checklist.md`
3. `examples.md`
4. `output-contract.md`
5. `related-assets.md`
6. `skill.reference.online-credit-solution-lens`

## Execution Rule

1. 先按 `checklist.md` 收集最低输入
2. 信息不足时先输出缺口清单和追问问题，不强行写满
3. 重点先起草“授信方案”章节
4. 准入策略只能给结构化建议，不给最终政策口径
5. 结尾必须列出待人工确认项

## Input Contract

最低输入：

- 展业场景
- 目标客户群体
- 核心企业或合作平台基本情况
- 初步授信模式或还款来源

可选补充：

- 历史方案模板
- 核心企业或平台股权、经营和财务材料
- 数据来源和核验能力说明
- 风险缓释安排
- 反欺诈、反洗钱、消保、贷后管理要求

## Output Contract

必须包含：

1. **当前已掌握信息**
2. **缺口清单**
3. **需追问问题**
4. **授信方案章节草稿**
5. **准入策略建议草稿**
6. **待人工确认项**

禁止在输出中：

- 承诺审批通过
- 承诺额度、定价、期限最终口径
- 引用内部制度原文
- 编造核心企业、平台或客户数据

## Quality Gate

- 是否先问答补数，再起草
- 是否把“授信方案”作为中心输出
- 是否区分可草拟内容和待确认内容
- 是否明确边界和风险提示
