---
name: online-credit-solution-lens
description: Use when you need a judgment framework for drafting or reviewing an online credit automated approval business proposal, especially the credit-solution section and admission strategy.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 线上授信自动化审批方案视角
  audience: [bank-practitioner, manager]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
  related_skills:
    - skill.reference.online-credit-admission-strategy-patterns
    - skill.action.online-credit-approval-solution-drafting
    - skill.action.product-matching-boundary
    - skill.action.client-needs-diagnosis
  related_prompts: []
  boundary:
    - "本 skill 提供判断框架，不替代内部审批、授信政策、定价和最终结论"
    - "缺少用户补数或公开依据时，必须写明待人工确认"
    - "涉及内部制度原文、敏感参数或审批口径时，当前仓库未覆盖"
---

# 线上授信自动化审批方案视角 Skill

## Scope

这是一个 reference skill。
它聚焦“线上授信自动化审批业务方案”的判断框架，尤其是“授信方案”章节怎么拆、怎么补信息、怎么区分可先草拟内容和必须人工确认内容。

## When To Use

- 需要起草或审阅线上授信自动化审批业务方案
- 需要先判断这类方案还缺什么信息
- 需要识别“授信方案”章节的重点和边界
- 需要为后续 action skill 提供稳定的判断框架

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次进入这类方案时，至少先明确：

1. **场景与业务模式**：场景是什么，谁是核心企业或平台，交易闭环在哪里
2. **客群与还款来源**：借款主体是谁，还款能力靠什么支撑
3. **授信方案主干**：审批模式、准入策略、额度、期限、用途、还款方式、风险缓释、场景价值评估
4. **数据与核验能力**：哪些数据能拿到，哪些环节可验证，哪些只能假设
5. **管理与边界**：反欺诈、反洗钱、消保、贷后管理、人工复核点在哪里

## Not For

- 直接给出审批结论、授信政策、额度结论或定价承诺
- 替代内部授信制度
- 在没有基础事实时硬写“看起来完整”的方案

## Quality Gate

- 是否先判断场景、客群、还款来源，而不是直接堆章节
- 是否把“授信方案”章节作为主轴
- 是否区分了可草拟内容和待人工确认内容
- 是否明确写出了边界

## Boundary With Related Assets

| 资产 | 做什么 | 使用时机 |
|------|--------|----------|
| `skill.reference.online-credit-solution-lens`（本 skill） | 判断框架：先看什么、先补什么、先分什么边界 | 刚开始写方案或审方案 |
| `skill.reference.online-credit-admission-strategy-patterns` | 准入策略建议：从业务模式、场景、上下游、数据和风控角度给可参考建议 | 需要单独推敲准入策略 |
| `skill.action.online-credit-approval-solution-drafting` | 执行脚本：问答补数、拉缺口清单、生成章节草稿 | 需要直接开始起草 |
