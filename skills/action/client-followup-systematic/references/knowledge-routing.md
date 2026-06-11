# 知识路由

本文件指导在跟进场景中，根据事项类型补充对应的公开知识。

## 按事项类型的知识路由

### 结算与支付类

路由到：

- `knowledge/banks/ceb/corporate-settlement/basic-settlement`
- `knowledge/banks/ceb/transaction-banking/e-fu-tong`

适用场景：

- 客户询问账户服务
- 支付结算流程问题
- 电子银行产品需求

### 贸易金融类

路由到：

- `knowledge/banks/ceb/trade-finance/dian-fei-tong`
- 相关信用证、保函知识包

适用场景：

- 进出口结算需求
- 信用证开立或修改
- 保函办理

### 信贷与授信类

路由到：

- `knowledge/common/sales/consultative-b2b/modules/objection-handling`
- `knowledge/common/banker-thinking/top-performer`

适用场景：

- 客户对额度或利率有顾虑
- 需要用专业口径回应异议
- 提升说服力的案例参考

### 客户沟通与异议处理

路由到：

- `knowledge/common/psychology/business-communication`
- `knowledge/common/sales/consultative-b2b/modules/discovery-questions`

适用场景：

- 需要问出客户真实顾虑
- 对方表示"考虑一下"需要推进
- 需要给出合理回答但避免过度承诺

### 市场与行业分析

路由到：

- `knowledge/common/economics/business-basics`

适用场景：

- 客户提出市场相关问题
- 需要提供宏观经济或行业背景信息
- 帮助客户理解产品价值

## 知识使用原则

1. **先用后补**：先完成事项状态评估和推动策略，知识补充是锦上添花
2. **公开口径**：只使用公开可查的知识，不引用内部数据
3. **边界清晰**：如果知识无法回答客户具体问题，说明需要进一步核实
4. **避免承诺**：知识补充不等于承诺，具体结果仍需走审批流程

## 路由决策流程

```
事项涉及的产品或话题是？
│
├─ 结算/支付 → corporate-settlement / product-catalog / e-fu-tong（仅明确命中 e付通时）
├─ 贸易金融 → product-catalog / dian-fei-tong（仅明确命中电费通或电费证时）
├─ 信贷/授信 → consultative-b2b objection-handling, top-performer
├─ 沟通技巧 → business-communication, discovery-questions
├─ 市场背景 → business-basics
└─ 其他 → 根据具体话题判断，无匹配则不强制路由
```
