---
id: prompt.skill.action.online-credit-approval-solution-drafting
kind: skill
display_name_zh: 线上授信自动化审批业务方案辅助撰写 Prompt
target_skill: skill.action.online-credit-approval-solution-drafting
summary: 通过问答收集信息，输出缺口清单、追问问题和”授信方案”章节草稿。
relations:
  - skill.reference.online-credit-solution-lens
  - skill.reference.executive-briefing-decision-support
---

请按“线上授信自动化审批业务方案辅助撰写”方式处理我接下来提供的信息。

目标不是直接给审批结论，而是：

- 先问答补数
- 识别缺口
- 起草“授信方案”章节
- 对准入策略给结构化建议
- 明确待人工确认项

请按以下顺序工作：

1. 先判断当前已掌握信息和关键缺口
2. 只追问最影响“授信方案”章节的内容
3. 优先输出：
   - 当前已掌握信息
   - 缺口清单
   - 需追问问题
   - 授信方案章节草稿
   - 准入策略建议草稿
   - 待人工确认项

授信方案章节至少覆盖：

- 审批模式
- 准入策略
- 贷款额度
- 授信期限
- 贷款期限
- 贷款用途
- 还款方式
- 风险缓释
- 场景价值评估

要求：

1. 区分事实、建议、待确认。
2. 没有公开依据或用户补数不足时，写明“当前仓库未覆盖”或“待人工确认”。
3. 不编造内部制度，不输出审批、授信、定价、时效承诺。
4. 如果用户提供了模板、历史方案或修改意见，优先提醒适合沉淀到 private-first 的路径。
5. 如果用户还没有明确场景，优先判断是否属于“核心企业上下游场景”或“平台交易场景”，并从这两个方向先追问。
6. 如果属于平台交易场景，优先追问平台控制力、交易真实性、结算链条、数据可核验能力、反欺诈和贷后监测安排。
