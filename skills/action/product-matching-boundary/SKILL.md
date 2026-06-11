---
name: skill.action.product-matching-boundary
description: Use when you have a diagnosed client need and need to systematically determine which products are suitable and which boundaries cannot be crossed.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: execute
  display_name_zh: 产品匹配与边界提示
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.corporate-client-coverage-lens
    - skill.action.market-corporate-client
    - skill.action.client-followup-systematic
  related_knowledge:
    - knowledge.banks.ceb.transaction-banking.product-catalog
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.e-fu-tong
    - knowledge.banks.ceb.trade-finance.dian-fei-tong
    - knowledge.banks.ceb.transaction-banking.yangguang-supply-chain
    - knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map
    - knowledge.common.sales.consultative-b2b
  related_prompts:
    - prompt.skill.action.product-matching-boundary
  references_dir: references
  scripts_dir: scripts
---

# 产品匹配与边界提示 Skill

## Scope

这是一个 action skill。
它聚焦"需求已诊断"之后的判断环节，负责系统判断哪类产品适合、哪些边界不能碰、是否需要跨条线协同。

与 `skill.action.market-corporate-client` 的边界：

- `market-corporate-client`：负责开场、提问、需求发现和首次切入口选择，输出是场景判断 + 切入口 + 会谈目标
- `product-matching-boundary`：负责需求定型后的产品适配判断和边界核查，输出是产品候选 + 合规边界 + 协同需求

简单说：`market-corporate-client` 告诉你"聊什么"，`product-matching-boundary` 告诉你"能推什么、不能碰什么"。

## When To Use

- 需求诊断已完成（来自 client-needs-diagnosis 或 market-corporate-client 输出），需要判断主推产品
- 客户提出明确需求，需要评估银行产品是否可能适配
- 已有初步产品想法，需要核查边界和合规风险
- 需要判断是否涉及跨条线（公司、零售、同业、风险）协同

## Required Reads

1. `knowledge/banks/ceb/transaction-banking/product-catalog/products.md`
2. `references/product-candidate-matrix.md`
3. `references/boundary-checklist.md`
4. `references/knowledge-routing.md`
5. `skill.reference.corporate-client-coverage-lens`
6. 命中 knowledge 后，读取对应 `README.md`、`modules/*`、`faq.md`、`sources.md`

## Execution Rule

1. 先用 `product-catalog/products.md` 核验产品范围；不在白名单内的名称不得作为候选产品输出。
2. 再用 `references/product-candidate-matrix.md` 根据需求类型生成产品候选列表。
3. 对每个候选产品做白名单二次核验，过滤掉未列入目录的名称；`阳光e支付` 不得输出。
4. `阳光供应链云平台` 只作为对客服务平台/线上化渠道能力说明，不作为候选产品排序。
5. 再用 `references/boundary-checklist.md` 对每个候选产品核查边界。
6. 然后按 `references/knowledge-routing.md` 调用对应产品知识包确认适配判断。
7. 如涉及跨条线产品，用 boundary-checklist 判断协同边界。
8. 最后汇总：产品方向 + 白名单内候选产品 + 平台/渠道能力（如适用）+ 边界提示 + 协同需求。

## Input Contract

最低输入：

- 客户需求定型结论（需求类型、资金用途、金额量级、时间窗口）
- 客户基本情况（行业、企业规模、经营状态至少有一项）
- 客户归属（公司/零售/普惠/同业/其他）

可选补充：

- 已有产品想法或偏好
- 监管敏感标识（如涉房、涉煤、涉平台）
- 历史合作情况摘要

## Output Contract

必须包含：

1. **产品候选列表**：按适配度排序的推荐产品，标注适配依据
2. **边界提示**：每个候选产品的监管红线、机构边界、客群限制
3. **协同需求**：是否需要其他条线支持，协同方向
4. **下一轮动作建议**：基于判断结果的下一步

禁止在输出中：

- 承诺具体费率、定价、审批结论
- 承诺产品可办理或放款
- 写入授信准入具体数值
- 写内部审批口径
- 超出"是否可能"层级的边界判断
- 输出不在 `product-catalog/products.md` 中的光大交易银行产品名
- 把 `阳光e支付` 写成光大交易银行产品
- 把 `阳光供应链云平台` 当作具体融资、结算或贸易金融产品排序推荐
- 在产品详情待补充时编造功能、准入、费率、时效或办理条件

## Quality Gate

- 是否区分"可能适配"和"明确不可"
- 是否对每个候选产品标注边界层级
- 是否判断协同条线和方向
- 是否避免堆砌产品功能和定价细节
- 是否在边界模糊时标注"需进一步确认"

## Boundary With Market Corporate Client

| 维度 | market-corporate-client | product-matching-boundary |
|------|------------------------|---------------------------|
| 核心逻辑 | 开场诊断，切入口选择 | 需求定型后，产品适配与边界判断 |
| 输入阶段 | 首访/首次触达 | 需求已诊断或客户已有明确想法 |
| 输出重心 | 场景判断 + 切入口 + 会谈目标 | 产品候选 + 合规边界 + 协同需求 |
| 适用场景 | 首次拜访、需求探索 | 需求确认后、方案设计前 |
| 协同视角 | 切入口优先 | 合规优先 |

## Script Hooks

- `scripts/validate-output.py`：校验结构完整性与承诺风险
