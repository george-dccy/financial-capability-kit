# Related Assets

## 联动 Skills

- `skill.reference.corporate-client-coverage-lens`
  客户覆盖视角提供全局优先级和关键对象判断，现金流判断常作为其客户评估的财务支撑

- `skill.reference.problem-opportunity-framework`
  现金流判断完成后，用问题-机会框架收束成"下一步先判断什么"

- `skill.action.market-corporate-client`
  首访前结合现金流判断做客户画像，准备切入话题

- `skill.action.product-matching-boundary`
  现金流状态是判断产品边界和还款来源的核心输入

- `skill.action.report-decision-brief`
  现金流判断结果可以结构化成拍板简报中的财务判断段落

## 联动 Knowledge

- `knowledge.common.economics.business-basics`
  现金流逻辑基础模块，提供"钱从哪里来、在哪个环节卡住、什么时候最紧张"的通用框架

- `knowledge.banks.ceb.corporate-settlement.yangguang-cash-management`
  光大银行现金管理产品家族，现金流状态是匹配现金管理产品的核心依据

- `knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate`
  电费证等贸易融资产品与特定行业的现金流场景相关

- `knowledge.banks.ceb.transaction-banking.yangguang-e-pay`
  e付通类产品与经营现金流的收款环节直接挂钩

## 待建立 Asset（不在当前仓库）

- 暂无（`skill.reference.financial-statement-reading-lens` 已建立，与本 skill 形成上下层联动关系）

## Trigger Word Mapping

使用 `build-context.py` 脚本时，遇到以下词应路由到本 skill：

- 现金流分析、现金质量、偿债能力、经营现金流
- 企业现金是否健康、还款能力评估
- 财报分析、企业财务信号

配合使用：

- "钱从哪来/资金链" → 联动 `knowledge.common.economics.business-basics`
- "客户财务" → 联动 `skill.reference.corporate-client-coverage-lens`
- "能不能批/授信" → 不路由，直接拒绝，跳至合规边界提示
