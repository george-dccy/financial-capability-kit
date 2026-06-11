# Knowledge Routing

根据诊断结论的二级细分，路由到对应 knowledge 包补充背景知识。

涉及光大交易银行具体产品名、产品推荐或产品比较时，优先读取：

`knowledge.banks.ceb.transaction-banking.product-catalog`

该目录是当前产品名称白名单。未列入目录的名称不能作为光大交易银行产品输出。

## 路由表

| 诊断结论 | 优先读取 | 补充读取 |
|---------|---------|---------|
| 基础结算 / 现金管理 | `knowledge.banks.ceb.transaction-banking.product-catalog` | `knowledge.banks.ceb.corporate-settlement.basic-settlement` |
| 企业收单 / 工资代发 | `knowledge.banks.ceb.corporate-settlement.corporate-settlement-card` | - |
| 信用证 / 托收 / 保函 | `knowledge.banks.ceb.trade-finance.dian-fei-tong` | - |
| 供应链融资 / 确权 | `knowledge.banks.ceb.transaction-banking.product-catalog` | `knowledge.banks.ceb.transaction-banking.e-fu-tong` 仅在明确命中 e付通/1+N 时读取 |
| 普惠 / 场景贷款 | `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map` | - |
| 流动资金 / 固定资产贷款 | `knowledge.common.economics.business-basics` | 产品目录中仅保留交易银行相关产品；贷款类需另行核验 |
| 外汇避险 / 跨境结算 | `knowledge.banks.ceb.transaction-banking.product-catalog` | 对应结售汇、掉期、期权、跨境汇款产品详情待补 |
| 数字化转型 / 银企直连 | `knowledge.banks.ceb.transaction-banking.product-catalog` | 不能默认进入 e付通；需明确产品名或场景 |

## 路由执行顺序

1. 先读 knowledge 的 `README.md` 获取概览
2. 再按需读 `modules/*` 下的子模块
3. 如有 `faq.md` 优先读，常见问题最密集
4. 如有 `sources.md` 读来源，验证公开性

## 诊断时补充背景的方法

- 知道行业但不确定需求方向：先读 `knowledge.common.economics.business-basics/modules/macro-signals.md`
- 知道客户规模但不确定需求层次：先读 `knowledge.common.banker-thinking.top-performer/modules/decision-framework.md`
- 想判断客户沟通风格：读 `knowledge.common.sales.consultative-b2b/modules/discovery-questions.md`
