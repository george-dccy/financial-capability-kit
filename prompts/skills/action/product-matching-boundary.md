---
id: prompt.skill.action.product-matching-boundary
kind: skill
display_name_zh: 产品匹配与边界提示 Prompt
target_skill: skill.action.product-matching-boundary
summary: 根据客户需求定型结论，输出产品候选、边界提示、协同需求和下一步动作。
relations:
  - skill.action.client-needs-diagnosis
  - skill.action.market-corporate-client
---

```text
请使用 `skill.action.product-matching-boundary`。

先确认：
- 客户需求是否已经定型
- 客户行业、规模、经营状态
- 客户归属和协同条线
- 已知边界或不可承诺事项

输出：
1. 产品候选列表，按适配度排序
2. 适配依据
3. 不能承诺或必须核验的边界
4. 需要协同的条线或角色
5. 下一轮客户沟通建议

不要输出授信、审批、定价或办理时效承诺。
```
