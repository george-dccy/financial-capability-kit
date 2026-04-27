# Related Assets

## 联动 Skills

- `skill.reference.enterprise-cash-flow-judgment`
  现金流判断是财报阅读的核心子模块，本 skill 提供整体框架，现金流 skill 提供深度判断

- `skill.reference.corporate-client-coverage-lens`
  客户覆盖视角提供全局优先级判断，财报阅读是其财务评估的底层支撑

- `skill.reference.problem-opportunity-framework`
  财报阅读完成后，用问题-机会框架收束成"这家企业值不值得跟进"

- `skill.action.client-needs-diagnosis`
  财报阅读结果可作为客户需求诊断前的财务背景输入

- `skill.action.product-matching-boundary`
  财报财务判断是产品匹配的核心依据之一

- `skill.action.report-decision-brief`
  财报阅读结论可以结构化成拍板简报中的客户财务段落

## 联动 Knowledge

- `knowledge.common.economics.business-basics`
  商业基础逻辑模块，理解"钱从哪里来、在哪里沉淀、什么时候最紧张"的通用框架

- `knowledge.banks.ceb.corporate-settlement.yangguang-cash-management`
  光大银行现金管理产品家族，财务报表状态是匹配现金管理产品的依据

- `knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate`
  电费证等贸易融资产品与特定行业的现金流场景相关

- `knowledge.banks.ceb.transaction-banking.yangguang-e-pay`
  e付通与经营现金流的收款环节直接挂钩

## 待建立 Asset（不在当前仓库）

- `knowledge.industry.manufacturing.financial-characteristics`
  制造业财务特征知识包，与本 skill 的行业判断模块形成互补

- `knowledge.industry.trade.financial-characteristics`
  贸易业财务特征知识包

- `knowledge.industry.construction.financial-characteristics`
  建筑业财务特征知识包

- `skill.action.quick-financial-assessment`
  快速财务评估 action skill，提供5分钟速读模板

## Trigger Word Mapping

使用 `build-context.py` 脚本时，遇到以下词应路由到本 skill：

- 财报阅读、财务报表分析、财务判断
- 企业财务状况、客户财务质量
- 怎么看财报、先看什么
- 资产负债表、现金流量表、利润表
- 财务指标、偿债能力、盈利能力
- 客户财务评估、企业质量判断

配合使用：

- "现金流" → 联动 `skill.reference.enterprise-cash-flow-judgment`
- "客户要不要跟" → 联动 `skill.reference.problem-opportunity-framework`
- "能不能批贷款" → 不路由，直接拒绝，跳至合规边界提示
