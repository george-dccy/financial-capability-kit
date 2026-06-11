---
id: prompt.skill.action.accompany-corporate-client
kind: skill
display_name_zh: 对公客户持续推进 Prompt
target_skill: skill.action.accompany-corporate-client
summary: 帮助持续跟进客户、组织问题闭环并安排后续推进。
relations:
  - knowledge.banks.ceb.corporate-settlement.basic-settlement
  - knowledge.banks.ceb.transaction-banking.e-fu-tong
  - knowledge.banks.ceb.trade-finance.dian-fei-tong
---

请把我接下来提供的信息整理成一版客户持续推进方案。

请输出：

- 当前关系阶段判断
- 待回应问题清单
- 本次跟进动作
- 内部协同清单
- 下一次触达计划

要求：

1. 同时覆盖客户动作和内部动作。
2. 下一次触达目标必须明确。
3. 如果涉及公开产品或制度口径，只能基于仓库中的 knowledge 表达。
4. 不输出审批、授信、定价、时效承诺。
