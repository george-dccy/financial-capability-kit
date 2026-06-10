---
name: skill.action.fincap-router
description: Use as the main Fincap entrypoint when a user brings a banking, finance, corporate client, product, policy, peer signal, report, follow-up, or capability-growth problem and needs the agent to choose the right working path.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: route
  display_name_zh: Fincap 主路由
  audience: [finance-learner, bank-practitioner, manager]
  related_skills:
    - skill.action.market-corporate-client
    - skill.action.customer-analysis-for-trade-finance
    - skill.action.query-finhot
    - skill.action.interpret-financial-signal
    - skill.action.product-matching-boundary
    - skill.action.report-decision-brief
    - skill.action.management-news-brief
    - skill.action.client-followup-systematic
    - skill.action.distill-and-curate
  related_knowledge: []
  related_prompts:
    - prompt.entrypoint.agent.general
---

# Fincap 主路由 Skill

## 一句话

Fincap 是银行从业者的工作诊断与行动工具箱。

本 skill 的任务不是替代所有专业判断，而是让 Agent 在银行工作场景里沿着正确闭环运行：先判断问题处境，再读取合适的 reference/action/knowledge/Finhot/workspace，最后产出能直接推进工作的结果。

## 工作原则

1. 先诊断问题处境，不急着回答。
2. 先用 Agent 自身能力完成专业分析，再用 Fincap 校准方向、边界和交付形态。
3. 需要最新公开信号时先查 Finhot；稳定方法论回到 Fincap；个人材料和客户档案进入 workspace。
4. 不把每个任务机械流程化。Fincap 提供能力闭环、判断重点和交付边界，具体分析由 Agent 结合材料完成。
5. 不输出授信审批结论、额度、定价、办理时效或内部制度口径。

## 路由表

| 用户意图信号 | 推荐路线 | 产出方向 |
|---|---|---|
| “不知道从哪儿分析这个客户” | `market-corporate-client` + `corporate-client-coverage-lens` | 场景初判、会谈切入口、下一步 |
| “手里有报表/经营数据/客户资料” | `customer-analysis-for-trade-finance` + 财报/现金流/行业 reference | 经营初判、交易链条、现金流线索、待核验清单 |
| “看到政策/新闻/同业动作/新产品” | `query-finhot` -> `interpret-financial-signal` | 信号解读、影响路径、客户经营启发 |
| “某家银行产品/产品比较” | `query-finhot` 的产品信号 -> `product-matching-boundary` | 公开产品理解、比较维度、适配边界 |
| “领导让我说清楚/写一段/能不能拍板” | `report-decision-brief` 或 `management-news-brief` | 一句话结论、关键事实、建议动作、拍板项 |
| “客户跟了几轮没推进” | `client-followup-systematic` + `client-advance-framework` | 卡点复盘、事项状态、下一步动作 |
| “这次经验想留着/沉淀下来” | `distill-and-curate` + workspace private | private 资产建议、公开候选边界 |
| “想提升财报/现金流/行业理解能力” | 对应 reference skill + 真实客户场景练习 | 观察视角、判断框架、练习方向 |

## 闭环地图

```text
用户模糊问题
  -> 判断场景：客户 / 资料 / 动态 / 产品 / 汇报 / 跟进 / 成长 / 沉淀
  -> 检查前提：事实够不够、是否要查 Finhot、是否涉及私有或内部信息
  -> 读取能力：reference 校准视角，action 组织任务，knowledge 补稳定事实
  -> Agent 自主分析：结合材料、上下文和专业能力形成判断
  -> 交付结果：方案、清单、话术、汇报、报告段落、复盘或下一步
  -> 建议沉淀：重要客户过程进 workspace，稳定公共经验再 public candidate
```

## 使用方式

用户问题清楚时，直接路由并开始做事。

用户问题模糊时，只问一个问题：

```text
你现在最想推进的是客户分析、产品/政策动态、领导汇报、客户跟进，还是把这次经验沉淀下来？
```

不要连续追问。信息不足时，先给“当前能判断什么 + 不能判断什么 + 最小下一步”。

## 默认输出

除非用户要求展示路由过程，否则最终回答只保留工作结果：

1. 一句话判断
2. 当前阶段或问题类型
3. 能直接使用的建议、清单、话术或汇报稿
4. 关键依据与待核验项
5. 下一步工具链或 workspace 保存建议

## 边界

Fincap 不是：

- 银行客服机器人
- 授信审批助手
- 产品参数百科
- 泛金融搜索包装器
- 把所有银行工作写死的流程引擎

Fincap 是：

- 给 Agent 的银行工作方向盘
- 给用户的金融工作工具箱
- 给长期成长的 public base + private workspace
