---
name: skill.action.customer-analysis-for-trade-finance
description: Use when you need to analyze corporate client materials for trade finance, supply-chain finance, document business, or cross-border scenarios before drafting recommendations or report sections.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 贸易与供应链客户资料分析
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.corporate-client-coverage-lens
    - skill.reference.financial-statement-reading-lens
    - skill.reference.enterprise-cash-flow-judgment
    - skill.reference.industry-analysis-basics
    - skill.action.client-needs-diagnosis
    - skill.action.product-matching-boundary
    - skill.action.report-decision-brief
    - skill.action.client-followup-systematic
  related_knowledge:
    - knowledge.common.economics.business-basics
    - knowledge.common.sales.consultative-b2b
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 贸易与供应链客户资料分析 Skill

## Scope

这是一个 action skill。
它聚焦客户资料分析，不替代授信审查、审批意见、定价测算或内部尽调结论。

本周试用版只覆盖：

- 贸易融资
- 供应链金融
- 单证业务
- 跨境业务

它的任务不是穷尽所有分析步骤，而是给 Agent 一个银行工作方向：把分散资料转成经营判断、交易链条假设、现金流压力线索、可能切入口和报告章节草稿。

## When To Use

- 用户手里有客户财务报表、进销存、水电或生产经营数据，需要先判断能看出什么
- 用户有客户情况介绍、拜访记录或公开资料，需要组织成客户经营初判
- 用户想判断贸易融资、供应链、单证或跨境业务是否可能有切入口
- 用户需要撰写客户调查报告、客户经营分析或向上汇报中的某一段
- 主路由判断用户处于“资料整理 / 客户诊断 / 方案建议 / 汇报”阶段

## Required Reads

1. `skill.reference.problem-opportunity-framework`
2. `skill.reference.corporate-client-coverage-lens`
3. 有财报时，读取 `skill.reference.financial-statement-reading-lens`
4. 有现金流、回款、账期或偿债问题时，读取 `skill.reference.enterprise-cash-flow-judgment`
5. 需要理解行业位置时，读取 `skill.reference.industry-analysis-basics`
6. `skill.action.client-needs-diagnosis`
7. `skill.action.product-matching-boundary`
8. 需要汇报表达时，读取 `skill.action.report-decision-brief`
9. 需要持续推进时，读取 `skill.action.client-followup-systematic`
10. 涉及最新政策、同业产品、公开动态或案例时，先通过 `skill.action.query-finhot` 查 Finhot

## Input Contract

最低输入，满足其一即可启动：

- 客户基本情况：行业、主营业务、规模、区域或上下游角色
- 客户材料：财务报表、经营数据、进销存、水电/物流/订单数据、公司介绍、拜访记录
- 公开线索：官网、新闻、招投标、工商、行业动态或同业产品链接

建议补充：

- 用户当前目标：拜访准备、客户诊断、方案建议、领导汇报、报告章节、持续跟进
- 已知交易背景：买方、卖方、账期、结算方式、贸易单据、跨境收付、核心企业或平台
- 已有银行合作情况：账户、结算、授信、贸易融资、供应链或跨境业务摘要
- 材料日期和来源，避免把过期资料当作当前事实

## Execution Rule

Agent 可以使用自己的财报、现金流、行业和贸易金融知识完成具体分析，但必须遵守以下顺序感：

1. **材料先行**：先说明已经依据什么材料判断，哪些只是缺口。
2. **事实和假设分层**：不要把推断写成结论。
3. **回到交易链条**：围绕主营业务、上下游、账期、回款、单据、跨境要素组织判断。
4. **从经营信号到金融切入口**：先说经营和现金流变化，再说可能业务方向。
5. **交付当轮结果**：按用户目标输出经营初判、待核验清单、建议动作或报告章节草稿。
6. **接续下一步**：需要产品判断时接 `product-matching-boundary`，需要汇报时接 `report-decision-brief`，需要跟进时接 `client-followup-systematic`。

## Output Contract

通常包含：

1. **材料盘点**：已用材料、材料日期、可靠性和缺口
2. **客户经营初判**：主营业务、经营阶段、近期变化和关键不确定性
3. **交易链条梳理**：上下游、交易背景、结算方式、单据/跨境要素
4. **现金流与回款压力线索**：应收、应付、存货、账期、订单或产能信号
5. **可能业务切入口**：贸易融资、供应链、单证或跨境方向，标注适配依据和待核验项
6. **待核验清单**：下一次沟通或补材料时必须确认的问题
7. **下一步工具链**：建议继续使用哪个 action skill，例如 `product-matching-boundary`、`report-decision-brief` 或 `client-followup-systematic`

如果用户问题很轻，不必机械输出全部 7 项；但必须保留事实/假设/待核验边界。

可选输出：

- 客户调查报告某一章节草稿
- 领导汇报的一句话结论和要点
- 下一次拜访提问清单
- workspace session 保存摘要

## Quality Gate

- 是否先做材料盘点，再做判断
- 是否把事实、假设、待核验项分开
- 是否围绕贸易融资、供应链、单证、跨境试点范围
- 是否输出了能推动下一步的待核验清单
- 是否避免把产品适配写成办理承诺
- 是否避免授信结论、额度、定价、审批意见或办理时效承诺

## Boundary

禁止输出：

- 授信审批结论
- 授信额度、定价、期限、担保方式的承诺
- 内部审批口径或内部制度原文
- 未脱敏的真实客户敏感信息
- 对客户信用风险的最终结论

如材料不足，必须写：

```text
当前材料不足以形成结论，以下仅为工作假设。
```

如仓库或 Finhot 没有覆盖相关产品、政策、案例或同业信息，必须写：

```text
当前仓库未覆盖，需要补充公开来源或用户材料。
```
