# Fincap Capability Map

Fincap 是银行从业者的工作诊断与行动工具箱。

它不把银行工作拆成僵硬流程，而是给 Agent 一张能力地图：遇到不同问题时先判断场景，再调用合适的 reference skill、action skill、knowledge、Finhot 或 workspace。

## 主闭环

```text
用户问题
  -> Fincap 主路由
  -> 前提检查
  -> 能力链路
  -> Agent 自主分析
  -> 工作交付物
  -> workspace 沉淀
```

## 七类工作入口

| 入口 | 典型问题 | 主要能力 |
|---|---|---|
| 客户经营 | “这个客户怎么切入？”“明天拜访怎么聊？” | 客户场景判断、会谈切入口、下一步推进 |
| 客户资料研判 | “我手里有报表和经营数据，看能发现什么？” | 财报、现金流、行业、交易链条和待核验清单 |
| 动态信号解读 | “这个政策/同业产品/案例对我有什么用？” | Finhot 查询、信号解读、客户经营启发 |
| 产品与方案边界 | “这个产品适不适合客户？”“同业产品怎么比较？” | 产品匹配、边界提示、协同方向 |
| 汇报与拍板 | “领导让我说清楚这件事。” | 一句话结论、关键事实、建议动作、拍板项 |
| 跟进与复盘 | “客户跟了几轮没推进。” | 卡点复盘、事项状态、下一步动作 |
| 能力成长与沉淀 | “这类问题以后也按这个方式处理。” | reference skill、private-first、workspace 复盘 |

## 关键能力链路

### 客户问题

```text
fincap-router
  -> corporate-client-coverage-lens
  -> market-corporate-client / customer-analysis-for-trade-finance
  -> client-needs-diagnosis
  -> product-matching-boundary
  -> client-followup-systematic
  -> workspace session
```

### 外部信号

```text
fincap-router
  -> query-finhot
  -> interpret-financial-signal
  -> management-news-brief / report-decision-brief
  -> distill-and-curate
```

### 资料研判

```text
fincap-router
  -> customer-analysis-for-trade-finance
  -> financial-statement-reading-lens
  -> enterprise-cash-flow-judgment
  -> industry-analysis-basics
  -> report-decision-brief
```

## Reference Skill 的用法

Reference skill 不是流程脚本，而是方向校准：

- 财报分析：提醒 Agent 从银行视角先看现金流、资产负债结构和利润质量，不被净利润带偏。
- 现金流分析：提醒 Agent 区分真实现金、账面利润、融资依赖、三流平衡和回款节奏。
- 行业理解：提醒 Agent 从信用风险、周期位置、监管敏感度和上下游议价能力看行业。
- 客户覆盖：提醒 Agent 判断关键对象、推进节奏和关系经营优先级。

Agent 可以使用自身知识储备完成具体分析，但必须落在这些判断方向和边界内。

## Action Skill 的用法

Action skill 不负责穷尽所有场景，而是规定：

- 什么时候用
- 最低需要什么输入
- 应该产出什么工作结果
- 不能越过哪些边界
- 下一步应该接哪个能力

如果材料不足，Agent 仍应先输出当前能判断的内容、不能判断的内容和最小下一步，而不是停止工作。

## Finhot 与 Workspace

Finhot 是公开信号雷达：

- 新政策
- 同业产品
- 新产品
- 项目案例
- 经营观察

Workspace 是个人工作台：

- 客户档案
- 私有材料
- 会话状态
- 复盘和反馈
- 不便公开的经验

Fincap 负责把两者接入同一条工作闭环。
