---
id: prompt.skill.action.market-corporate-client
kind: skill
display_name_zh: 对公客户首访推进 Prompt
target_skill: skill.action.market-corporate-client
summary: 帮助完成首访前诊断、切入口设计和首次会谈目标设定。
relations:
  - knowledge.banks.ceb.corporate-settlement.basic-settlement
  - knowledge.banks.ceb.transaction-banking.e-fu-tong
  - knowledge.banks.ceb.trade-finance.dian-fei-tong
---

请把我接下来提供的信息整理成一版可直接拿去做客户首访或首次触达的推进方案。

请输出：

- 客户场景初判
- 推荐切入口
- 首次会谈目标
- 不宜过早触达的话题
- 会后推进动作

要求：

1. 先判断场景，再给产品或方案方向。
2. 优先做最小推进动作，不要把所有内容一次讲满。
3. 如涉及公开产品，只基于仓库中的 knowledge 给出稳妥口径。
4. 不输出审批、授信、定价、时效承诺。
