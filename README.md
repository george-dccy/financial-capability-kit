<h1 align="center">Financial Capability Kit</h1>

<p align="center">
  面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力，甚至可以不断成长为金融人面对客户时的分身
</p>
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/MiniMax-Preferred-1677ff?style=flat-square" alt="MiniMax Preferred" />
  <img src="https://img.shields.io/badge/Agent-Ready-7c3aed?style=flat-square" alt="Agent Ready" />
  <img src="https://img.shields.io/badge/Public%20%2B%20Private-Growth-f59e0b?style=flat-square" alt="Public + Private Growth" />
  <img src="https://img.shields.io/badge/Finance-Capability-0f766e?style=flat-square" alt="Finance Capability" />
</p>

<p align="center">
  帮助个人逐步形成更像专业人士的观察视角、表达方式、分析能力和推进能力
</p>

---

## 这是什么

这是一个**面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力**：

- 把公开金融知识、公开产品资料、FAQ 和来源整理成可稳定复用的 `knowledge`
- 把专业视角、判断框架、表达结构沉淀成 `skills/reference`
- 把首访推进、持续跟进、汇报拍板、蒸馏整理等任务沉淀成 `skills/action`
- 支持每个用户在 clone 后，把自己的经验、偏好、案例和复盘继续沉淀到 `workspace/private/`

你可以把它理解成：

> **公开层提供专业骨架，私有层负责长期成长。**

它摒弃不精准的临时搜索结果，也不透露银行内部资料。
它是一个会持续增长的金融能力集合，帮助你越来越像专业人士那样看问题、说问题、推进问题。
甚至支持你直接发给客户，成为你面对客户时的分身。

---

## 你现在就可以这样用

### 1) 面向支持读取仓库的聊天应用

不是所有聊天类大模型应用都能真的读取仓库内容。推荐顺序是：

- `MiniMax 全能模式`：当前优先推荐，可克隆仓库后读取内容并回答，整体效果最好。
- `豆包电脑版超能模式`：可以读取仓库内容；普通聊天模式不保证能读取正文。
- `DeepSeek`：建议开启 `深度思考`，并关闭 `智能搜索`，否则容易绕开仓库直接泛化回答。
- `千问等普通聊天模式`：容易不受仓库约束而自由发挥，不建议作为主入口。
- `本地 Agent / 可读本地仓库的 Agent`：如果能直接 clone 或读取本地文件，通常最稳定。

详细见：

- [模型与模式兼容性说明](./docs/prompts/model-compatibility.md)

复制 [prompts/entrypoints/chat/](prompts/entrypoints/chat/) 下的入口提示词，再附上仓库地址和你的问题即可。

使用前先确认你当前应用真的支持仓库读取，尤其不要默认把普通聊天模式当成“可按仓库回答”的模式。

- 想系统提升金融能力 → [点这里](prompts/entrypoints/chat/financial-capability.md)
- 公开咨询用户 → [点这里](prompts/entrypoints/chat/public-consulting.md)
- 银行员工 → [点这里](prompts/entrypoints/chat/bank-staff.md)
- 基层管理者 → [点这里](prompts/entrypoints/chat/frontline-manager.md)
- 领导层 / 决策层 → [点这里](prompts/entrypoints/chat/head-office-leadership.md)
- 不确定用哪个 → [点这里](prompts/entrypoints/chat/auto.md)

### 2) 面向 Hermes / OpenClaw / Workbuddy 等 Agent

如果你有自己的 Agent，建议直接使用这个独立入口文件：

- 通用 Agent 入口 → [点这里](prompts/entrypoints/agent/general.md)

它会让你的 Agent：

- 遇到类似问题时优先复用仓库里的专业视角、行动 skill 和公开知识
- 默认先解当前问题，再判断是否值得沉淀
- 把你确认过的经验、偏好、案例和复盘优先写进 `workspace/private/`

### 3) 先沉淀到 private growth layer

如果你提供的是经验、偏好、失败教训、案例、公开材料或专题资料，推荐优先使用：

- [点这里](skills/action/distill-and-curate/SKILL.md)

---

## 试试这些问题

- 我想系统提升自己的金融分析能力，看到一家银行新产品时，应该先看哪些关键内容？
- 我需要把一个复杂事项整理成一分钟能讲清楚的版本，怎么说才更像专业人士？
- 我是对公客户经理，明天要拜访一家新能源零部件企业，应该怎么开场、问什么、先推进什么？
- 我是基层管理者，团队里两个重点客户推进卡住了，帮我拆任务、定检查点、整理上提事项。
- 我有几次失败案例和几篇公开材料，帮我先沉淀到 private，再整理成可公开贡献的候选资产。

---

## 仓库地图

- `skills/reference/`：专业视角、判断框架、表达结构
- `skills/action/`：首访推进、持续跟进、汇报拍板、蒸馏整理等任务型 skill
- `knowledge/`：公开知识、公开产品资料、FAQ、来源
- `prompts/`：给支持读取仓库的聊天模型 / Agent 直接复制使用
- `workspace/private/`：你的私有增长层，包含 private skills、knowledge、memories、case-notes、registry
- `registry/`：让 Agent 知道该读什么、何时触发、怎么关联
- `docs/`：架构、贡献与使用说明

---

## 这个仓库和临时搜索有什么不同

擅长把公开资料组织成稳定的能力底座。
不会拿泛金融资料或不贴题产品来拼答案。
它除了给答案，还能帮助你慢慢长出更像专业人士的看法、说法和分析方式。
public 提供公共骨架，private 负责个人长期增长。
你确认过的经验、偏好、表达方式和案例，不需要每次重新讲一遍。

---

## public 与 private

仓库采用 `public base + private growth layer` 结构。

```text
workspace/private/
├─ skills/
│  ├─ reference/
│  └─ action/
├─ knowledge/
├─ memories/
├─ case-notes/
└─ registry/
```

这样可以保证：

- 公共仓库更新时，private 层不会被覆盖
- Agent 可以同时读取 public 和 private
- 个人经验可以先 private-first，再决定是否公开
- private 可以逐步长成个人金融 LLM Wiki

详细见：

- [架构说明](./docs/architecture/README.md)
- [Overlay 规则](./docs/architecture/overlay.md)
- [Skill 分类说明](./docs/architecture/skill-taxonomy.md)

---

## 提交方式

推荐走：

`private-first -> public-candidate -> merge to public`

推荐顺序：

1. 先解决眼前问题
2. 再判断哪些内容值得长期保留
3. 先沉淀到 `workspace/private/*`
4. 等内容稳定后，再整理成公开候选

相关入口：

- [CONTRIBUTING](./CONTRIBUTING.md)
- [公开提炼流程](./docs/contribution/distillation-workflow.md)

---

## 当前方向

当前仓库重点围绕以下方向建设：

- 金融专业能力成长
- 银行/金融业务推进 skill
- 公开金融知识与产品资料整理
- private growth layer
- repo-first 的 Agent / 仓库可读模式使用体验

后续会继续增强：

- 官网与公开报道的持续提炼
- private 的长期记忆与偏好沉淀
- 触发条件更明确的 registry
- 更贴近个人 LLM Wiki 的增长体验

## License

[MIT](./LICENSE)
