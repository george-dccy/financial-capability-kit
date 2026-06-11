---
name: skill.action.branch-operating-diagnosis
description: 需要快速判断分支行、网点或团队当前经营状态时触发。通过对话收集目标、关键经营数据和自我评价，输出结构化经营分析初判（亮点、短板、初步归因和待补数项）。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 经营分析
  audience: [bank-practitioner, manager]
  related_skills:
    - skill.reference.branch-operating-diagnosis-lens
    - skill.action.operating-recommendation-brief
    - skill.action.report-decision-brief
    - skill.reference.executive-briefing-decision-support
  related_prompts:
    - prompt.skill.action.branch-operating-diagnosis
---

# 经营分析 Skill

## Scope

这是一个 action skill。
它负责通过对话收集目标、关键经营数据和自我评价，然后输出一版轻量、结构化、可继续补数的经营分析结论。

## When To Use

- 需要快速判断分支行、网点或团队当前经营状态
- 手上只有 3-8 个关键指标，需要先给出一版经营分析
- 需要在正式汇报前先形成初判
- 需要先找亮点、短板和待补数项，再进入经营建议阶段

## Input Contract

### 最低输入

- 当前阶段目标
- 3-8 个关键经营数据
- 至少一个对比维度（同比、环比、上期、目标、去年同期之一）
- 使用者自我评价或现场判断

### 推荐优先提供

- 存款
- 贷款
- 中收
- 利润或营收贡献
- AUM
- 客户数 / 活跃客户

### 可选补充

- 客群结构
- 产品结构
- 区域结构
- 新户 / 流失
- 近期政策、竞争或区域变化
- 已知资源约束

### 输入不足时怎么处理

如果缺目标、对比口径或关键经营数据，应先写明待补数，不直接下完整经营结论。

## Workflow

### Step 1：判断输入够不够

先确认：有没有目标、有没有关键指标、有没有对比口径。

### Step 2：先看结果

先回答：当前结果是亮点还是短板、离目标近还是远、是阶段波动还是持续趋势。

### Step 3：再拆结构

如果用户提供了结构信息，再拆：客群结构、产品结构、区域结构、过程动作。

### Step 4：再做初步归因

区分：结果问题、结构问题、过程问题、外部环境问题。

### Step 5：输出待补数项

至少列出：还缺什么数据、哪些结论暂时不宜下、后续是否适合进入经营建议阶段。

## Output Contract

### 必须包含

1. **当前初判** — 一句话结论
2. **做得好的地方** — 亮点
3. **做得不好的地方** — 短板
4. **主要判断依据** — 指标和对比口径
5. **初步归因** — 更像结果问题 / 结构问题 / 过程问题 / 外部环境问题
6. **还需补充的信息** — 待补数项
7. **边界提示** — 当前哪些结论只属于初判、哪些点需要人工复核

### 输出模板

```
## 当前初判
- 一句话结论：

## 做得好的地方
- 亮点 1：
- 亮点 2：

## 做得不好的地方
- 短板 1：
- 短板 2：

## 主要判断依据
- 指标和对比口径：

## 初步归因
- 更像结果问题 / 结构问题 / 过程问题 / 外部环境问题：

## 还需补充的信息
- 待补数 1：
- 待补数 2：

## 边界提示
- 当前哪些结论只属于初判：
- 哪些点需要人工复核：
```

### 禁止在输出中

- 冒充正式考核结论
- 编造口径不一致的数据解释
- 承诺内部经营动作已正确
- 写真实客户敏感信息

## Quality Gate

- 是否先看结果，再讲结构和原因
- 是否把亮点和短板拆开写
- 是否明确标出待补数项
- 是否避免把轻量经营分析写成内部经营例会纪要
- 是否可通过对话补数使用
- 是否写出了边界提示

## Related Assets

- `skill.reference.branch-operating-diagnosis-lens`
- `skill.action.operating-recommendation-brief`
- `skill.action.report-decision-brief`
- `skill.reference.executive-briefing-decision-support`
- `skill.action.interpret-financial-signal`

后续建议补：`knowledge.common.bank-operating-indicators-basics`
