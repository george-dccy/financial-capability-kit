---
name: financial-statement-reading-lens
description: Use when you need a banker's professional lens to read financial statements — focusing on what to look at first, how to judge quality, and how to express findings in professional contexts.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: reference
  capability: analyze
  display_name_zh: 财报阅读专业视角
  audience: [finance-learner, bank-practitioner]
  support_files:
    - README.md
    - frameworks.md
    - examples.md
    - anti-patterns.md
    - related-assets.md
---

# 财报阅读专业视角 Skill

## Scope

这是一个 reference skill。
它帮助你从银行对公业务视角，快速建立对一家企业财务状况的专业判断框架。
重心不是教会你做财务分析，而是让你知道"先看什么、看什么指标、避免什么误判"。

## When To Use

- 客户拜访前需要快速建立对企业财务状况的判断
- 撰写客户评估报告时需要财务判断段落
- 在会议中需要对企业财务状况发表专业意见
- 判断一家企业是否值得深入跟进
- 在没有专业财务团队支持下需要独立判断企业质量

## Required Reads

1. `README.md`
2. `frameworks.md`
3. `examples.md`
4. `anti-patterns.md`
5. `related-assets.md`

## Banker vs. Accountant Perspective

银行视角与财务视角的核心差异：

| 维度 | 财务视角 | 银行视角 |
|------|----------|----------|
| 关注焦点 | 利润表（EPS、ROE） | 资产负债表和现金流量表 |
| 时间 horizon | 全周期/年度 | 12–36个月 |
| 关键指标 | 净利润、增长率 | 现金流、偿债能力、资金周转 |
| 报表偏好 | 利润表先行 | 现金流量表优先，资产负债表交叉验证 |
| 判断目的 | 估值和投资决策 | 信用风险和偿还能力评估 |

银行不关心这家企业"值多少钱"，只关心"贷款能不能收回来"。

## Required Inputs

以下三项至少需要一项才能启动判断：

- 近三年简化资产负债表（资产、负债、所有者权益）
- 近三年现金流量表（经营/投资/融资三段）
- 近三年利润表 + 主要科目的变动说明

数据越完整，判断越准确。

## Quality Gate

- 是否先看了现金流而非利润
- 是否指出了"表面盈利但实际资金紧张"的风险
- 是否区分了行业特性对财务表现的影响
- 是否避免了授信、定价、审批承诺
- 是否标注了"缺少什么关键信息"
