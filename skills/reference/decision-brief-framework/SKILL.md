---
name: skill.reference.decision-brief-framework
description: 当你需要准备一句话结论、30秒口头汇报或一页式简报时触发。提供五段式简报结构，把复杂事项压缩成可拍板的表达骨架。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: communicate
  display_name_zh: 拍板简报框架
  audience: [finance-learner, bank-practitioner, manager]
  task_patterns: ["向领导汇报", "拍板简报", "口头汇报", "书面简报"]
  when_to_use: "需要把复杂事项压缩成可判断、可拍板、可转述的表达结构时。"
  not_for: "缺少基础事实且尚未完成事实收集时。"
  inputs: ["背景事实", "关键变化", "卡点", "建议动作"]
  outputs: ["一句话结论", "关键事实", "卡点", "建议动作", "拍板项"]
  boundary:
    - "本 skill 提供表达结构，不负责事实采集"
    - "事实采集由具体 action skill 先组织好再套入本框架"
    - "在 skill.action.report-decision-brief 中负责完整汇报编排"
  source_frameworks: ["五段式简报"]
---

# 拍板简报框架

## Scope

这是一个 reference skill。
它提供"怎么说成可拍板结构"的表达骨架，不负责先替你采集事实。

## When To Use

- 需要准备一句话结论
- 需要做 30 秒口头汇报
- 需要把复杂事项压缩成一页式简报

## Core Output Rule

优先使用五段式：

1. 一句话结论
2. 关键事实
3. 当前卡点
4. 建议动作
5. 需要拍板项

## Not For

- 在没有基础事实时硬写判断
- 把所有背景都堆进汇报

## 判断框架

### 五段式简报

1. 一句话结论
2. 关键事实
3. 当前卡点
4. 建议动作
5. 需要拍板项

### 写法要求

- 先讲判断，再讲材料
- 先讲变化，再讲细节
- 拍板项必须可选，不要空泛

### 复用提醒

- 它负责"怎么把事情说成可拍板结构"，不负责"该汇报哪些事实"
- 事实采集、knowledge 引用和场景边界，应由具体 action skill 先组织好再套入本框架

## 示例

### 支行项目汇报

一句话结论：

制造业客户的推进价值成立，但目前卡在客户内部财务与业务协同，建议先争取一次跨部门流程梳理会。

需要拍板项：

- 是否允许我方联动产品同事参与下一轮会谈
- 是否将该客户纳入本月重点推进清单

## 常见误区

- 汇报全是材料，没有结论
- 讲了问题，但没给建议动作
- 需要拍板项写成开放式讨论题

## Quality Gate

- 是否以一句话结论开头
- 拍板项是否具体可选（不是开放式问题）
- 是否避免了把所有背景堆进汇报
