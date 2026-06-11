---
id: prompt.skill.reference.executive-briefing-decision-support
kind: skill
display_name_zh: 向上汇报与决策支持判断框架 Prompt
target_skill: skill.reference.executive-briefing-decision-support
summary: 帮助判断汇报类型、决策点、风险和表达结构。
relations:
  - skill.action.report-decision-brief
  - skill.reference.decision-brief-framework
---

```text
请使用 `skill.reference.executive-briefing-decision-support`。

先判断这次汇报属于哪一类：情况同步、问题上提、资源协调、拍板决策、风险提示。

输出：
1. 汇报类型
2. 领导需要判断什么
3. 哪些事实必须先讲
4. 哪些风险不能省
5. 建议使用的表达结构
6. 不应越界的内容

不要编造内部制度、审批结论、授信、定价或办理时效。
```
