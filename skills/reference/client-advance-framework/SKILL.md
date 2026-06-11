---
name: skill.reference.client-advance-framework
description: 当你需要把一次沟通推进成明确动作时触发。提供推进四问和最小推进卡片，确保每一步有目标、责任人、时间点和回看信号。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: execute
  display_name_zh: 客户推进框架
  audience: [finance-learner, bank-practitioner]
  task_patterns: ["下一步怎么推进", "客户跟进", "闭环", "谁做什么", "时间点"]
  when_to_use: "需要把一次沟通或一次判断推进成可执行的下一步动作时。"
  not_for: "需要直接输出事实查询结果或替代场景编排时。"
  inputs: ["当前关系阶段", "关键卡点", "协同对象"]
  outputs: ["推进目标", "动作清单", "责任人", "时间点"]
  boundary:
    - "本 skill 提供推进框架，不替代 action skill 的场景编排"
    - "在 market-corporate-client 中负责首次接触变成可执行下一步"
    - "在 accompany-corporate-client 中负责持续陪伴变成明确推进节奏"
  source_frameworks: ["推进四问", "最小推进卡片"]
---

# 客户推进框架

## Scope

这是一个 reference skill。
它负责把"聊过了"变成"下一步谁做什么、什么时候做、怎样算往前走"。

## When To Use

- 需要把一次沟通推进成明确动作
- 害怕事情停在"保持联系"
- 需要设计责任人、时间点和检查点

## Core Output Rule

每次至少明确：

1. 这一步的目标
2. 谁负责
3. 何时推进
4. 如何判断是否真的往前走

## Not For

- 替代 action skill 的场景编排
- 只做概念解释不做推进设计

## 判断框架

### 推进四问

1. 本轮最小目标是什么
2. 谁是本轮关键对象
3. 下一步动作由谁完成
4. 什么信号算真正往前推进

### 最小推进卡片

每次沟通后至少形成：

- 目标
- 对象
- 动作
- 时间点
- 风险点
- 回看信号

### 复用提醒

- 在 `skill.action.market-corporate-client` 中，它负责把首次接触变成可执行的下一步动作
- 在 `skill.action.accompany-corporate-client` 中，它负责把持续陪伴变成明确的推进节奏和闭环信号

## 示例

### 首次会谈后的跟进

会后不要只写"持续跟进"，而要写成：

- 目标：确认客户是否愿意进一步梳理对账场景
- 对象：财务负责人
- 动作：发送公开资料并预约二次电话
- 时间点：本周四前
- 风险点：对方没有内部协同意愿
- 回看信号：是否愿意补充现有流程信息

## 常见误区

- 会后只写"保持联系"
- 没写责任人和时间点
- 没定义什么叫推进成功

## Quality Gate

- 每个推进卡片是否包含目标、对象、动作、时间、风险、回看信号六个要素
- 是否避免了"保持联系"式的空泛跟进
- 时间点是否具体到可执行
