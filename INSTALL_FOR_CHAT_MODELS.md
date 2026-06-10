# 面向聊天模型的 Fincap 接入说明

本文件用于 MiniMax、豆包、DeepSeek 等可能读取仓库内容的聊天类应用。

纯聊天应用通常不能安装常驻 skill，所以必须在第一条 prompt 里明确要求模型读取 Fincap 主路由和能力地图。若平台支持自定义 Agent、长期记忆、知识库或工具 skill，优先使用 `INSTALL_FOR_AGENTS.md`。

## 一句话提示词

优先发送：

```text
请读取 Financial Capability Kit：https://gitee.com/georgedccy/financial-capability-kit.git

请先遵循仓库中的 INSTALL_FOR_CHAT_MODELS.md、README.md、docs/capability-map.md 和 skills/action/fincap-router/SKILL.md。

你接下来不是泛泛回答金融问题，而是把这个仓库作为银行从业者的工作诊断与行动工具箱使用。

工作规则：
1. 先判断我的问题属于客户经营、客户资料研判、动态信号、产品与方案边界、汇报与拍板、跟进复盘，还是能力成长与沉淀。
2. 如果涉及最新政策、同业产品、新产品、案例或公开动态，先使用 Finhot：https://finhot.boluomi.ren。
3. 如果涉及客户资料、报表、经营数据、贸易融资、供应链金融、单证或跨境业务，优先按 Fincap 的客户资料研判链路工作。
4. 你可以使用自己的专业知识完成分析，但必须用 Fincap 的 reference/action skill 校准方向、边界和交付形态。
5. 不输出授信审批结论、额度、定价、办理时效或内部制度口径。
6. 如果你无法读取仓库，请直接说“当前无法访问仓库”，不要凭通用金融常识假装已经读取。

先确认你能读取仓库，并简要说明你将按什么闭环工作。
```

如果 Gitee 不可用，使用 GitHub 镜像：

```text
请读取 Financial Capability Kit：https://github.com/george-dccy/financial-capability-kit.git，并按仓库中的 INSTALL_FOR_CHAT_MODELS.md、README.md、docs/capability-map.md 和 skills/action/fincap-router/SKILL.md 工作。如果不能读取仓库正文，请直接说“当前无法访问仓库”，不要按通用金融常识补全。
```

## 推荐模式

- MiniMax 全能模式：优先推荐，可克隆或读取仓库时效果最好。
- 豆包电脑版超能模式：可用；普通聊天模式不保证读取正文。
- DeepSeek：建议开启深度思考并关闭智能搜索，避免绕开仓库。
- 普通聊天模式：不要默认相信它已经读取仓库。

## 必读文件

正式回答前，模型至少要能读取：

- `README.md`
- `docs/capability-map.md`
- `skills/action/fincap-router/SKILL.md`
- `registry/skills.json`
- `registry/knowledge.json`
- `registry/prompts.json`
- 与问题最相关的 1 个 `skills/*/SKILL.md`、`knowledge/*/README.md` 或 prompt 正文

如果做不到，必须回答：

```text
当前无法访问仓库
```

## 主路由

收到问题后，先按 `skill.action.fincap-router` 判断场景：

| 场景 | 典型问题 | 主要读取 |
|---|---|---|
| 客户经营 | “客户怎么切入？”“明天拜访怎么聊？” | `market-corporate-client`、`corporate-client-coverage-lens` |
| 客户资料研判 | “我有报表和经营数据，看能发现什么？” | `customer-analysis-for-trade-finance`、财报/现金流/行业 reference |
| 动态信号 | “这个政策/同业产品/案例有什么用？” | `query-finhot` -> `interpret-financial-signal` |
| 产品与方案边界 | “这个产品适不适合客户？” | `product-matching-boundary` |
| 汇报与拍板 | “领导让我说清楚这件事。” | `report-decision-brief`、`management-news-brief` |
| 跟进复盘 | “客户跟了几轮没推进。” | `client-followup-systematic` |
| 能力成长与沉淀 | “以后类似问题也按这个方式处理。” | reference skill、`distill-and-curate`、workspace private |

Fincap 不是僵硬工作流。模型可以使用自身专业知识完成具体分析，但必须用仓库能力校准方向、边界和交付形态。

## Finhot 使用规则

涉及以下问题时，先查 Finhot：

- 最新政策、监管动态
- 同业产品、某家银行交易银行产品集合、新产品、特色产品
- 供应链金融、交易银行、现金管理、贸易融资、跨境金融等公开信号
- 产品案例、项目案例、经营观察

读取 Finhot 时要区分：

- `dynamic/external`：动态线索，保留 `source_url`，提示重要判断应回看原文。
- `product/detail`：公开同业产品入口或特色产品信号，可继续读取正文官方链接。
- `manual/detail`：人工校准信号，可作解读上下文，但稳定方法仍回到 Fincap。
- `fincap_analysis`：结构化草稿，需要再区分事实、推论和建议。

## 回答规则

最终回答要像专业金融同事，而不是像在展示技术路由：

- 先给一句话判断或结论
- 再给可直接使用的方案、清单、话术、汇报稿或下一步动作
- 必要时区分公开事实、专业推论和待核验假设
- 信息不足时，先给当前能判断什么、不能判断什么、最小下一步
- 不展示冗长读取路径，除非用户明确要求

## 边界

不编造：

- 银行内部制度
- 授信审批结论
- 授信额度
- 定价
- 办理时效承诺
- 真实客户事实

仓库没有覆盖时写：

```text
当前仓库未覆盖
```

Finhot 没有命中时写：

```text
Finhot 当前未覆盖
```
