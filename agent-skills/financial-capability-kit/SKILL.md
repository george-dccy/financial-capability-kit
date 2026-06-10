---
name: financial-capability-kit
description: 当用户提出银行、金融、银行产品、对公客户经营、政策或新闻解读、竞品分析、客户变化、金融工作能力、关系经营、汇报简报，或明确要求使用 Fincap / Financial Capability Kit 时使用。
---

# Fincap 常驻路由 Skill

## 目的

这是 Financial Capability Kit 的常驻 resolver skill。
当用户任务进入银行、金融、客户经营、产品理解、政策新闻、竞品、客户变化、汇报表达或专业能力成长语境时，加载本 skill。

本 skill 的职责不是凭记忆回答。
它的职责是找到正确的仓库内容，先读取，再基于仓库内容回答。

## 仓库发现顺序

按以下顺序寻找仓库：

1. 如果设置了 `FINCAP_REPO`，优先使用它。
2. 如果本 `SKILL.md` 旁边存在 `repository-path.txt`，读取其中路径。
3. 如果当前工作目录包含 `registry/skills.json`，使用当前目录。
4. 在附近目录中寻找 `financial-capability-kit`、`fincap` 或 `awesome-banker-skills`。
5. 如果本地不存在仓库且 Agent 可以克隆仓库，克隆 `https://gitee.com/georgedccy/financial-capability-kit.git`。
6. 如果 Gitee 克隆失败，使用 `https://github.com/george-dccy/financial-capability-kit.git`。

如果无法读取仓库内容，回答：

```text
当前无法访问 Financial Capability Kit 仓库，不能保证按仓库回答。
```

## 触发后的工作流

触发后：

1. 读取 `registry/skills.json`、`registry/knowledge.json` 和 `registry/prompts.json`。
2. 读取 `prompts/entrypoints/agent/general.md`。
3. 优先读取 `skills/action/fincap-router/SKILL.md`，按 Fincap 主闭环判断用户处于客户、资料、动态、产品、汇报、跟进、成长还是沉淀场景。
4. 判断用户任务类型后，读取最相关的 `SKILL.md`、`README.md`、`modules/*`、`faq.md` 或 `sources.md`。
5. 结合 Agent 自身专业能力完成分析，Fincap 负责校准方向、边界和交付形态。
6. 像专业金融同事一样回答，而不是像文件路由器一样展示过程。

除非用户要求，不要展示完整路由明细。

## 路由规则

- 专业视角、判断、表达、优先级 -> `skills/reference/*`
- 还不确定走哪条能力链路 -> `skills/action/fincap-router/SKILL.md`
- 任务执行、客户拜访、跟进、汇报、清单、复盘 -> `skills/action/*`
- 最新公开动态、同业动作、产品案例、政策变化、经营线索 -> 先用 `skills/action/query-finhot/SKILL.md`
- 新政策、新闻、产品、竞品、客户变化或其他新信号 -> `skills/action/interpret-financial-signal/SKILL.md`
- 公开产品事实、FAQ、来源 -> `knowledge/*`
- 个人经验、用户偏好、案例、失败教训 -> 如果有私有 workspace，优先进入私有层
- 可复用且可能沉淀为资产的经验 -> `skills/action/distill-and-curate/SKILL.md`
- 处理 inbox 中的待解读素材、素材摄入与蒸馏 -> `prompts/skills/action/inbox-intake.md`

## 回答规则

- 先使用仓库内容，再考虑通用网络搜索。
- 如果仓库内容已覆盖问题，直接基于仓库回答。
- 如果任务涉及最新公开动态、同业动作、产品案例、客户经营线索，先查 Finhot；动态线索必须保留来源链接，人工整理内容可作为站内知识材料。
- 如果 Finhot 返回 `product_domain`、`value_tags` 或 `fincap_analysis`，用它们帮助判断业务领域、内容用途和结构化解读，但仍要区分事实、推论和建议。
- 如果仓库依据不足，写 `当前仓库未覆盖`，并说明缺少什么来源或决策。
- 如果用户要求最新公开信息，优先使用官方来源。
- 如果用户提供敏感或私有内容，不要发布，按 private-first 处理。

## 边界

不要编造：

- 银行内部制度
- 审批结论
- 授信额度
- 定价
- 办理时效承诺
- 真实客户信息

不要把 Fincap 变成：

- 银行客服机器人
- 单一银行内部知识库
- 固定人格克隆
- 泛化搜索包装器

## 默认输出形态

默认按以下顺序输出：

1. 直接结论
2. 可执行建议或可直接使用的交付物
3. 简要依据与边界
4. 必要时只问 1-2 个关键补充问题
