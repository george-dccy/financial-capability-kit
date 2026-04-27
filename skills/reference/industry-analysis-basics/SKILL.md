---
name: industry-analysis-basics
description: Use when you need a banker's professional lens to assess an industry — building credit-relevant perspective on industry lifecycle, competitive structure, regulatory impact, and cycle position before corporate client engagement or loan post-management.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 行业分析基础
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 行业分析基础 Skill

## Scope

这是一个 reference skill。
它帮助你从银行对公业务视角，快速建立接触企业客户前或贷后管理中的行业分析判断框架。
重心不是教会你做行业研究，而是让你知道"先看什么行业维度、看什么信号、避免什么误判"。

## When To Use

- 客户拜访前需要快速建立对客户所处行业的信用风险判断
- 信审报告中的行业分析段落
- 贷后管理中需要判断行业周期变化对企业的影响
- 判断一家企业所在行业是否值得深入合作
- 在没有专业行业研究团队支持下需要独立判断行业信用特征

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Banker vs. Analyst Perspective

银行视角与行业研究视角的核心差异：

| 维度 | 行业研究视角 | 银行视角 |
|------|-------------|----------|
| 关注焦点 | 增长潜力、竞争格局 | 信用风险、还款来源、周期敏感性 |
| 时间 horizon | 3–10年 | 12–36个月 |
| 关键问题 | 行业天花板在哪 | 行业下行时企业能不能还贷 |
| 核心框架 | 波特五力、产业链、生命周期 | 生命周期位置、周期敏感度、监管影响 |
| 判断目的 | 投资机会 | 信用风险和偿债能力 |

银行不关心这个行业"有没有投资机会"，只关心"这个行业的企业贷款能不能收回来"。

## Required Inputs

以下至少需要一项才能启动判断：

- 客户所处行业名称（可精确到二级分类）
- 客户主营业务描述
- 近期公开的行业政策或监管动态（可选）

数据越完整，判断越准确。行业名称本身已可给出初步框架判断。

## Quality Gate

- 是否从银行信用风险视角而非投资视角切入
- 是否有判断优先级（首次接触看什么、行业分化看什么、贷后管理看什么）
- 是否避免了具体行业知识堆砌
- 是否标注了"缺少什么关键信息"
- 是否避免了授信、定价、审批承诺
