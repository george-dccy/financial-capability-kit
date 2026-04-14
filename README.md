# Awesome Banker Skills / 银行人.skill

面向银行人、聊天大模型和 Agent 的能力基础，也同步支持公开咨询类问答。

它把银行人的共识技能、可公开知识和可复用方法沉淀下来，直接给豆包或 Agent 使用。

## 项目背景

银行工作的很多技能是跨岗位、跨流程复用的。
银行人需要不断学习、积累、总结，才能在业务中游刃有余。
但银行人往往没有时间、精力、动力去整理这些知识。
这些知识往往分散在各个人的大脑中，难以共享和复用。

### 这个项目希望能够

- 沉淀银行岗位共识技能、优秀人员可复用的方法、产品经营路径和可公开知识
- 支持每个用户在本地继续长出自己的 private skills / knowledge packs / methods / memories / case notes
- 不管是银行人还是银行客户，直接给豆包 / Agent 发送一段提示词，就能开始工作
- 为未来银行内部落地预留结构，支持添加行内知识源、连接客户数据，进行更复杂的判断和决策
- 让银行人少踩坑、少重复劳动、少加班，让业务推动更丝滑、业绩节节高，有更多时间陪伴家人、享受生活、提升消费，从而让我们的社会变得更好

## 主入口

项目适配了豆包/千问等大模型聊天应用。推荐直接复制以下入口 prompt 文件内容，再附上 Gitee 仓库地址及问题：

- `prompts/entrypoints/doubao/public-consulting.md`
  面向公开咨询用户，优先读取公开 knowledge packs
- `prompts/entrypoints/doubao/bank-staff.md`
  面向银行员工，先识别岗位；如有对应 role skill 就一并读取，再由 workflow 调用 methods 和 knowledge packs
- `prompts/entrypoints/doubao/frontline-manager.md`
  面向基层管理者，先叠加管理者角色视角，再进入管理或汇报 workflow
- `prompts/entrypoints/doubao/head-office-leadership.md`
  面向总行/分行领导层，先叠加领导层角色视角，再进入决策支持 workflow
- `prompts/entrypoints/doubao/auto.md`
  不确定身份或场景时使用

这些入口要求模型：

- 先读取 `registry/*.json`
- 先识别身份或岗位，如有对应 `role skill` 就一并读取
- 回答前先列出准备读取的文件路径
- 先识别 `scene`，再选择 `workflow`
- 显式写出调用了哪些 `role skill / workflow skill / method / pack`
- 把“方法/判断依据”和“公开知识依据”分层表达
- 覆盖不足时明确写出“当前仓库未覆盖”

补充说明见 [豆包入口说明](./docs/prompts/doubao.md)。

## Agent 使用方式

如果你有自己的 Agent，不必先手动讲解仓库结构。可以直接把下面这段提示词发给它：

```text
请把 `https://gitee.com/georgedccy/awesome-banker-skills.git` 作为我的银行业务 skill 仓库，并按下面方式工作：

1. 先拉取或更新这个仓库到本地工作目录。
2. 读取 `registry/skills.json`、`registry/methods.json`、`registry/knowledge-packs.json`、`registry/prompts.json`。
3. 如果你的运行环境支持 skill 安装，就把本轮需要的 skill 安装到本地；如果不支持，就直接按仓库里的 `SKILL.md`、`README.md`、`frameworks.md` 使用。
4. 如果存在 `workspace/private/registry/*.json`，一并作为 private overlay 读取。
5. 先识别我的身份或岗位；如果仓库里有对应 role skill，请一并读取。
6. 再识别我的问题属于哪个 scene，并选择对应 workflow。
7. 再根据问题需要补充 methods 和 knowledge packs。
8. 回答前先列出准备读取的文件路径。
9. 回答时明确写出：调用的 role skill / workflow skill / method / pack、方法判断依据、公开知识依据、下一步建议、边界提示。
10. 如果仓库没有覆盖，直接写“当前仓库未覆盖”。

现在开始，先告诉我你准备读取哪些文件。
```

这段提示词兼容两种方式：

- 支持安装 skill 的 Agent，可以把本轮需要的 skill 装到本地再使用
- 不支持安装 skill 的 Agent，也可以直接按 repo-first 方式读取仓库并开始问答

适合直接发给 Agent 的示例问题：

- 我是对公客户经理，明天首访一家做新能源零部件的客户，应该怎么开场、问什么、先推进什么？
- 客户问“光大 e 付通适合什么场景、前期要准备什么”，请按公开口径回答。
- 我是基层管理者，团队里两个重点客户推进卡住了，帮我拆任务、定检查点、整理上提事项。
- 把这周某个交易银行项目的进展，整理成一版 30 秒口头汇报和一版书面简版。
- 我有一份公开材料和几次失败案例，帮我先沉淀到 private，再整理成可提交 Gitee PR 的公开候选。

## 项目结构

```text
.
├─ skills/
│  ├─ roles/
│  └─ workflows/
├─ knowledge-packs/
│  ├─ banks/
│  └─ common/
├─ methods/
│  ├─ business-operations/
│  ├─ management/
│  ├─ communication-reporting/
│  └─ reusable/
├─ prompts/
│  ├─ entrypoints/
│  ├─ roles/
│  ├─ workflows/
│  ├─ knowledge-packs/
│  └─ methods/
├─ registry/
│  ├─ skills.json
│  ├─ knowledge-packs.json
│  ├─ methods.json
│  └─ prompts.json
├─ docs/
└─ templates/
```

结构解释：

- `skills/roles`：岗位 skill，沉淀这个岗位常见的判断方式、关注重点和沟通习惯
- `skills/workflows`：workflow skills，沉淀具体场景下的输入、动作、输出和推进顺序
- `knowledge-packs`：公开、稳定、可引用的知识事实
- `methods`：可复用判断与推进框架

推荐路由层级：

`scene -> workflow -> method -> knowledge pack`

如果身份明确，也可以同时读取对应 `role skill`。

## 支持公开和私有内容

公开仓库使用 `public base + private overlay` 模型。

公开层是仓库本体，面向分享、贡献和模型直接读取。  
私有层默认放在本地：

```text
workspace/private/
├─ skills/
├─ knowledge-packs/
├─ methods/
├─ memories/
├─ case-notes/
└─ registry/
```

这样可保证：

- 公共仓库更新时，private 层不会被覆盖
- Agent 可以同时读取 public 和 private
- 用户可以把 private 中的内容整理为 public contribution candidate
- 自进化先写 private memory / patch proposal，经确认后再更新正文

详细见：

- [架构说明](./docs/architecture/README.md)
- [Overlay 规则](./docs/architecture/overlay.md)
- [Methods 层说明](./docs/architecture/methods.md)

## 提交方式

推荐走 `private-first -> public-candidate -> merge to public`：

1. 先用私有层沉淀草稿
2. 用 `distill-and-contribute` 整理资产类型、目标路径和变更摘要
3. 去敏感化、补来源、补边界
4. 再整理成公开提交候选

### 如何用仓库内置 skill 沉淀内容

推荐优先使用 `workflow.distill-and-contribute`。它适合做四类事：

- 把公开文档、公开网页、说明材料整理成 knowledge pack / method / role skill / workflow skill
- 帮你判断内容应该落在 `skills`、`knowledge-packs` 还是 `methods`
- 先生成到 `workspace/private/*`，再决定是否公开
- 基于已有内容做增量补全，而不是整包重写

你可以直接对 Agent 这样下指令：

- “请使用 `workflow.distill-and-contribute`，把这份公开材料整理成 knowledge pack 草稿，先写到 `workspace/private/knowledge-packs/`。”
- “请使用 `workflow.distill-and-contribute`，把我这几次客户推进的失败复盘整理成 private method，先不要公开。”
- “请使用 `workflow.distill-and-contribute`，把 `workspace/private` 里的这几个草稿整理成公开贡献候选，并补 sources、registry 变更建议和 PR 摘要。”

推荐动作顺序：

1. 准备原料：公开文档、公开链接、公开网页、个人经验、失败教训、案例笔记。
2. 让 Agent 调用 `workflow.distill-and-contribute`，先判断资产类型和推荐落点。
3. 默认先写入 `workspace/private/skills`、`workspace/private/knowledge-packs`、`workspace/private/methods`、`workspace/private/memories`、`workspace/private/case-notes`。
4. 让 Agent 做增量补全，补 README、sources、faq、modules、registry 建议，而不是每次整包重写。
5. 你自己检查公开边界，确认没有敏感信息、内部制度、审批口径和无法公开传播的内容。
6. 再让 Agent 生成 public candidate、变更摘要和 PR 草稿。
7. 提交到 Gitee，并优先向 Gitee 发起 PR。

### 公开仓库协作入口

- Gitee 主仓库：`https://gitee.com/georgedccy/awesome-banker-skills.git`
- GitHub 镜像仓库：`https://github.com/george-dccy/awesome-banker-skills.git`

协作约定：

- 优先向 Gitee 提交 PR
- GitHub 主要用于展示、同步和备份
- 以 Gitee 上的 PR 讨论和合并为准

相关入口：

- [CONTRIBUTING](./CONTRIBUTING.md)
- [公开提炼流程](./docs/contribution/distillation-workflow.md)
- `templates/distill-skill/intake.md`

## 内容边界

仓库不会收录：

- 真实客户数据
- 内部制度原文
- 内部审批、授信、定价结论
- 额度、费率、时效承诺
- 真实敏感参数、账号、证件、合同、流水

仓库中的所有内容都只用于：

- 前期理解与准备
- 沟通、汇报、推进辅助
- 公开知识和可复用方法沉淀

如果仓库没有依据，应明确写出：`当前仓库未覆盖`

## License

[MIT](./LICENSE)
