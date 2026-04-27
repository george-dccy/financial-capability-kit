# Related Assets

## 联动 Skills

- `skill.reference.enterprise-cash-flow-judgment`
  行业分析完成后，用现金流判断验证行业周期是否真的反映到企业财务数据上；行业下行期现金流恶化是关键的交叉验证信号

- `skill.reference.financial-statement-reading-lens`
  财报阅读提供银行视角的财务报表判断框架，行业分析是其重要的前置输入——先判断行业背景，再看企业财报是否符合行业特征

- `skill.action.client-needs-diagnosis`
  行业分析是客户需求诊断的前置：知道客户处于什么行业，才能判断这个行业的常见金融需求类型（制造业看结算和项目融资，贸易业看票据和供应链金融）

- `skill.reference.corporate-client-coverage-lens`
  客户覆盖视角提供全局优先级和关键对象判断，行业分析是其客户评估的重要维度之一

- `skill.reference.problem-opportunity-framework`
  问题-机会框架在行业分析完成后，帮助收束成"这个行业当前的机会和风险分别在哪里，下一步先判断什么"

- `skill.action.product-matching-boundary`
  行业分析结论是判断产品边界的重要输入：重资产制造业 vs. 轻资产服务业需要不同的产品匹配

## 联动 Knowledge

- `knowledge.common.economics.business-basics`
  商业基础常识中的行业结构、竞争策略部分，提供行业分析框架的经济学基础

- `knowledge.banks.ceb.corporate-settlement.basic-settlement`
  对公结算基础，光大银行视角的结算产品与行业现金流结构相关

## 待建立 Asset（不在当前仓库）

- 特定行业（制造业、房地产、贸易等）的信用风险特征 knowledge pack
- 银行视角的产业链分析框架
- 政策解读 action skill（未来可扩展，本 skill 提供行业分析基础后，政策解读负责具体政策落地）

## Trigger Word Mapping

使用 `build-context.py` 脚本时，遇到以下词应路由到本 skill：

- 行业分析、行业判断、行业风险
- 行业周期、生命周期、行业位置
- 波特五力、行业结构、竞争格局
- 行业信用风险、行业政策影响
- 贷后行业跟踪、行业预警信号
- 首次接触看行业、行业背景判断

配合使用：

- "企业现金流" → 联动 `skill.reference.enterprise-cash-flow-judgment`
- "财报数据" → 联动 `skill.reference.financial-statement-reading-lens`
- "客户需求" → 联动 `skill.action.client-needs-diagnosis`
- "能不能批/授信" → 不路由，直接拒绝，跳至合规边界提示
