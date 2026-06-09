---
name: management-news-brief
description: Use when a policy, news item, peer move, product case, or Finhot signal needs to become a concise management-facing brief with impact judgment, action options, and verification boundaries.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: communicate
  display_name_zh: 管理信息简报
  audience: [bank-practitioner, manager]
  related_skills:
    - skill.action.query-finhot
    - skill.action.interpret-financial-signal
    - skill.action.report-decision-brief
    - skill.reference.executive-briefing-decision-support
  boundary:
    - "动态摘要不能当作完整原文"
    - "重要判断必须提示核验来源"
    - "不编造内部政策、审批、授信、定价或办理时效"
---

# 管理信息简报 Skill

## 适用场景

- 看到新政策、新产品、新案例或同业动作，需要向领导讲清楚
- Finhot 命中一条动态，需要转成经营启发
- 用户问“这个对我们有什么影响”
- 需要把复杂外部信息压成一分钟汇报

## 最低输入

至少需要一项：

- Finhot 查询结果
- 原文链接
- 用户贴的新闻、政策、产品或案例摘要
- 用户描述的客户或管理场景

## 推进顺序

1. 先判断信号类型：政策、同业、产品、客户、行业、风险、能力素材。
2. 区分事实、推论和建议。
3. 给出对银行工作的影响路径。
4. 判断适合转成哪类动作：
   - 客户经营线索
   - 产品设计参考
   - 风险识别提示
   - 政策影响跟踪
   - 同业案例借鉴
   - 汇报材料素材
5. 给出可直接汇报的一分钟版本。

## 输出契约

```text
一句话结论：

这是什么信号：

为什么值得看：

可能影响：
1. 客户经营：
2. 产品或方案：
3. 风险或合规：
4. 管理动作：

建议动作：
- 今天能做：
- 本周能做：
- 需要核验：

一分钟汇报版：

来源与边界：
```

## 检查点

- 是否保留 `source_url` 或说明来源缺口
- 是否没有把动态摘要当作完整事实
- 是否能被领导快速听懂
- 是否给出下一步动作，而不是只复述新闻
- 是否判断是否值得转入 Fincap 或 workspace
