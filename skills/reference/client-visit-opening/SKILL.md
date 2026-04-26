---
name: client-visit-opening
description: Use when preparing for or reflecting on a corporate client visit opening, and you need a professional judgment framework rather than a script.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 客户拜访开场框架
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
  related_skills:
    - skill.action.market-corporate-client
    - skill.reference.problem-opportunity-framework
    - skill.reference.client-advance-framework
  related_knowledge:
    - knowledge.common.sales.consultative-b2b
  boundary:
    - "本 skill 提供开场判断框架，不是话术模板"
    - "话术模板见 skill.action.market-corporate-client/references/opening-playbook.md"
    - "本 skill 与 opening-playbook 的边界：框架判断 vs. 执行脚本"
---

# 客户拜访开场框架 Skill

## Scope

这是一个 reference skill。
它不提供具体话术，而是提供开场时机的判断框架、信任建立策略选择、以及客户状态快速评估方法。

## When To Use

- 准备拜访客户，不知道先聊什么
- 需要判断用哪种开场策略
- 想快速评估客户当前状态和配合意愿
- 需要设计开场提问方向，而不是照读话术

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Core Output Rule

每次开场至少明确：

1. 选择哪种开场策略（冷淡/常规/高信任）
2. 第一个问题往哪个方向走（现状/困难/影响/目标）
3. 预判客户可能的配合度
4. 明确本 skill 与 opening-playbook 的使用边界

## Not For

- 提供具体话术文本
- 替代 action skill 的完整场景编排
- 首次拜访后的持续跟进设计

## Quality Gate

- 是否仍有专业判断框架而非话术堆砌
- 是否有银行/金融场景针对性
- 是否与 opening-playbook 边界清楚
- 是否有公开来源支撑
