---
name: skill.reference.team-followup-framework
description: 团队跟进框架。当需要把多人协同事项拆清楚、定责任、盯信号、做复盘时触发，帮助形成"安排了→有人跟→有人回→有人复盘"的稳定闭环。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: execute
  display_name_zh: 团队跟进框架
  audience: [finance-learner, bank-practitioner, manager]
  task_patterns:
    - 拆任务
    - 定责任
    - 做复盘
  when_to_use:
    - 需要多人协同推进事项
    - 需要避免"大家都知道但没人负责"
    - 需要形成固定检查点和复盘节奏
  not_for:
    - 替代客户场景 action skill
    - 只做口头表态，不形成可跟踪板
  inputs:
    - 重点事项清单
    - 参与人员及分工
  outputs:
    - 结构化跟进板（事项/负责人/截止时间/状态/卡点/检查点）
    - 复盘记录
  boundary:
    - 这是团队任务闭环框架，不是客户陪伴 workflow 的替代品
    - 当场景同时涉及客户推进和内部协同，scene 编排交给 workflow，闭环方法再调用本 skill
    - 在 skill.action.accompany-corporate-client 中，它负责内部协同闭环，不负责客户关系场景本身
    - 在管理型场景里，也可以单独复用这套闭环框架，而不绑定任何客户 workflow
  source_frameworks:
    - 管理闭环四步法
    - 最小管理板
---

# 团队跟进框架

## Scope

这是一个 reference skill。
它帮助你把多人协同事项拆清楚、盯住信号、形成复盘闭环。

## When To Use

- 需要多人协同推进事项
- 需要避免"大家都知道但没人负责"
- 需要形成固定检查点和复盘节奏

## Core Output Rule

每个重点事项至少应有：

- 事项名称
- 负责人
- 截止时间
- 当前状态
- 卡点
- 下次检查点

## Not For

- 替代客户场景 action skill
- 只做口头表态，不形成可跟踪板

## 判断框架

### 管理闭环四步

1. 拆任务
2. 定责任
3. 看信号
4. 做复盘

### 最小管理板

每个重点事项至少要有：

- 事项名称
- 负责人
- 截止时间
- 当前状态
- 卡点
- 下次检查点

## 示例

### 周例会后续

不要只说"大家跟一跟"，而要写成：

- 事项：完成客户二次电话预约
- 负责人：客户经理 A
- 截止：周三 18:00
- 当前状态：待联系
- 卡点：客户财务负责人时间未确认
- 下次检查点：周四晨会

## 常见误区

- **只有口头安排，没有书面责任**：任务只有口头安排，没有形成可跟踪的书面记录，导致"安排了"变成"没人跟"。
- **只看结果，不看中间信号**：只关注最终完成与否，忽略过程中的卡点信号和进度偏差，错失干预时机。
- **复盘只追责，不修方法**：复盘变成批斗会，不分析方法和流程问题，下次同样的问题继续发生。

## Quality Gate

- 每个重点事项是否都有明确负责人和截止时间
- 是否有固定的检查点节奏
- 复盘是否形成了可执行的改进项
