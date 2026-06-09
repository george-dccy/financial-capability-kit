---
name: operating-recommendation-brief
description: Use when a branch, team, outlet, or business line has an operating diagnosis and needs prioritized actions, owner hints, checkpoints, and a short management-facing recommendation.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 经营建议简报
  audience: [bank-practitioner, manager]
  related_skills:
    - skill.action.branch-operating-diagnosis
    - skill.reference.branch-operating-diagnosis-lens
    - skill.action.report-decision-brief
  boundary:
    - "不替代正式经营考核"
    - "不编造缺失数据"
    - "不输出内部制度、定价、授信或考核承诺"
---

# 经营建议简报 Skill

## 适用场景

- 已经完成经营分析，需要把短板转成下一步动作
- 领导问“接下来怎么抓”
- 团队需要把经营目标拆成一周内能推进的事项
- 分支行、网点、条线想做简短经营复盘和行动建议

## 最低输入

至少需要：

1. 当前经营目标或考核关注点
2. 已知亮点和短板
3. 1-3 个关键数据或现场信号

如果缺少关键数据，先输出稳妥建议，并明确待补数项。

## 推进顺序

1. 先复述经营目标，不扩大口径。
2. 把问题分成结果问题、结构问题、动作问题和协同问题。
3. 每类问题只保留最关键的 1-2 个信号。
4. 把建议分成：
   - 本周能做
   - 需要协同
   - 需要上提
   - 需要补数再判断
5. 给出检查点，而不是只给口号。

## 输出契约

```text
一句话判断：

经营抓手：
1. ...
2. ...
3. ...

本周动作：
- 动作：
  负责人：
  检查点：
  风险：

需要协同：

需要上提：

待补数项：

边界：
```

## 检查点

- 是否把建议和已知事实连上了
- 是否避免“加强营销、提高重视”这类空话
- 是否给出责任人类型和检查时间
- 是否标注缺数和边界
- 是否能被领导或团队当天拿去推进
