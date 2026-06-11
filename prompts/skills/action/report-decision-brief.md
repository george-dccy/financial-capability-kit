---
id: prompt.skill.action.report-decision-brief
kind: skill
display_name_zh: 向领导汇报与拍板 Prompt
target_skill: skill.action.report-decision-brief
summary: 帮助快速形成可拍板的口头和书面汇报。
relations:
  - knowledge.banks.ceb.corporate-settlement.basic-settlement
  - knowledge.banks.ceb.transaction-banking.e-fu-tong
  - knowledge.banks.ceb.trade-finance.dian-fei-tong
---

请把我接下来提供的信息整理成一版适合向领导汇报的内容。

请输出两个版本：

- `30 秒口头汇报版`
- `书面简版`

要求：

1. 先给一句话结论。
2. 只保留影响判断和拍板的信息。
3. 明确写出：关键事实、当前卡点、建议动作、需要拍板的点。
4. 语气要像成熟汇报，不要写成流水账，也不要解释你怎么组织信息。
5. 如果信息还不够形成汇报，请先给可成立的初版，再直接指出缺口。
