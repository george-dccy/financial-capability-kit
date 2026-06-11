<h1 align="center">Financial Capability Kit</h1>

<p align="center">
  面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力，可以不断成长为金融人面对客户时的分身
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

这是一个**银行从业者的工作诊断与行动工具箱**。

你可以把客户、产品、政策、同业动态、经营推进、汇报表达或能力成长问题交给支持读取仓库的 Agent。Fincap 会先帮 Agent 判断问题处境，再路由到合适的金融工作能力，而不是直接堆知识或泛泛回答。

```text
用户问题
  -> Fincap 主路由
  -> 前提检查
  -> reference/action/knowledge/Finhot/workspace
  -> Agent 自主分析
  -> 工作交付物
```

Fincap 不把每个银行工作写成僵硬流程。它提供能力闭环、判断重点和边界，让 Agent 用自己的知识储备做专业分析，但始终沿着正确方向工作。

## 工具箱能做什么

| 场景 | 你可以这样问 | Fincap 会引导 Agent 做什么 |
|---|---|---|
| 客户经营 | “我明天要见一个客户，资料很散，先从哪入手？” | 判断客户场景、切入口、会谈目标和下一步 |
| 客户资料研判 | “我手里有报表和经营数据，帮我看看能发现什么。” | 结合财报、现金流、行业和交易链条做经营初判 |
| 动态信号解读 | “这个政策/同业产品/案例对我有什么用？” | 先查 Finhot，再转成客户经营、产品或汇报启发 |
| 产品与方案边界 | “这个产品适不适合客户？” | 判断可能适配、待核验项和不能承诺的边界 |
| 汇报与拍板 | “领导让我说清楚这个客户值不值得继续跟进。” | 输出一句话结论、关键事实、建议动作和拍板项 |
| 跟进与复盘 | “这个客户跟了几轮没进展，问题在哪？” | 复盘卡点、事项状态和下一步推进动作 |
| 能力成长与沉淀 | “以后类似问题也按这个方式处理。” | 沉淀到 workspace private，稳定后再考虑 public 候选 |

完整能力图见 [Fincap Capability Map](./docs/capability-map.md)。

## 仓库怎么组织

Fincap 由几类资产共同组成：

- 把公开金融知识、公开产品资料、FAQ 和来源整理成可稳定复用的 `knowledge`
- 把专业视角、判断框架、表达结构沉淀成 `skills/reference`
- 把首访推进、持续跟进、汇报拍板、提炼整理等任务沉淀成 `skills/action`
- 支持每个用户在 clone 后，把自己的经验、偏好、案例和复盘继续沉淀到 `workspace/private/`

你可以把它理解成：

> **公开层提供专业骨架，私有层负责长期成长。**

当前系统分成三块：

- `financial-capability-kit / fincap`：主功能和公开能力底座，放稳定知识、产品地图、从业者能力、reference/action skill。
- `fincap-workspace`：个人沉淀层，放个人资讯、参考材料、案例复盘、偏好、不便公开内容和未成熟草稿。
- `finhot`：动态雷达，发现新政策、新产品、新项目案例、新同业动作和客户经营线索。

推荐流转方式：

`Finhot 发现信号 -> Fincap 解读和沉淀方法 -> workspace 记录个人经验和私有案例`

它摒弃不精准的临时搜索结果，也不透露银行内部资料。
它是一个会持续增长的金融能力集合，帮助你越来越像专业人士那样看问题、说问题、推进问题。
甚至支持你直接发给客户，成为你面对客户时的分身。

---

## 你现在就可以这样用

### 0) 一句话接入

给支持读取仓库的 Agent：

```text
请读取并遵循 Financial Capability Kit 安装说明：
https://gitee.com/georgedccy/financial-capability-kit/raw/main/INSTALL_FOR_AGENTS.md

如果能读取仓库，请简单确认已接入，然后等我提出具体问题；如果不能读取，请直接说“当前无法访问仓库”。
```

如果是在本地 Agent 中，希望新会话也能自动触发，可安装 resolver skill：

```powershell
git clone https://gitee.com/georgedccy/financial-capability-kit.git fincap
python .\fincap\install\fincap_agent_skill.py --target all
```

给支持读取仓库的聊天模型：

```text
请读取 Financial Capability Kit：
https://gitee.com/georgedccy/financial-capability-kit.git

请先按仓库中的 INSTALL_FOR_CHAT_MODELS.md 工作。如果能读取仓库，请简单确认已接入，然后等我提出具体问题；如果不能读取，请直接说“当前无法访问仓库”。
```

详细见：

- [Agent 安装说明](./INSTALL_FOR_AGENTS.md)
- [聊天模型接入说明](./INSTALL_FOR_CHAT_MODELS.md)
- [个人代理发布说明](./docs/agent-publishing.md)
- [三仓操作模型](./docs/operating-model.md)

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
- Finhot 联动入口 → [点这里](prompts/entrypoints/agent/finhot-aware.md)

它会让你的 Agent：

- 遇到类似问题时优先复用仓库里的专业视角、行动 skill 和公开知识
- 遇到最新公开动态、同业动作、产品案例和经营线索时，先查询 Finhot 雷达
- 默认先解当前问题，再判断是否值得沉淀
- 把你确认过的经验、偏好、案例和复盘优先写进 `workspace/private/`

### 3) 先沉淀到 private growth layer

如果你提供的是经验、偏好、失败教训、案例、公开材料或专题资料，推荐优先使用：

- [点这里](skills/action/distill-and-curate/SKILL.md)

---

## 试试这些问题

演示或试用时，建议先复制上面的“一句话接入”，确认模型能读取仓库后，再直接追问下面这类真实工作问题。

- 明天要去见一个客户，资料有点散，你先帮我看看怎么准备。
- 这个客户报表看起来还行，但我总觉得哪里不太踏实，你帮我看看。
- 最近供应链金融、交易银行这块有什么值得关注的吗？我想找点对客户有用的东西。
- 这个客户跟了几轮还是没进展，我有点不知道卡在哪里。
- 领导明天问这个客户还要不要继续跟，我怎么说比较稳？
- 我最近感觉自己看财报、看现金流还是抓不住重点，能不能带着我练一下？
- 这次拜访复盘里有些经验我不想丢，帮我整理一下。

---

## 仓库地图

- `skills/reference/`：专业视角、判断框架、表达结构
- `skills/action/`：首访推进、持续跟进、汇报拍板、提炼整理等任务型 skill
- `knowledge/`：公开知识、公开产品资料、FAQ、来源
- `inbox/`：公共素材摄入层，接收文件/链接/文本，经解读后提炼为 knowledge 或 skill
- `prompts/`：给支持读取仓库的聊天模型 / Agent 直接复制使用
- `workspace/private/`：你的私有增长层，包含 private skills、knowledge、memories、case-notes、registry
- `registry/`：让 Agent 知道该读什么、何时触发、怎么关联
- `docs/`：架构、贡献与使用说明

---

## 这个仓库和临时搜索有什么不同

擅长把公开资料组织成稳定的能力底座。
不会拿泛金融资料或不贴题产品来拼答案。
涉及最新公开动态、同业动作、政策变化、产品案例和经营线索时，优先使用 Finhot 作为公开信号雷达；Fincap 负责把这些信号解读成判断框架、客户经营动作、产品设计启发、汇报材料或沉淀建议。稳定知识和产品地图继续沉淀在 Fincap，个人材料继续沉淀在 workspace。
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
- [三仓操作模型](./docs/operating-model.md)

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
- inbox 素材摄入与提炼流水线

## License

[MIT](./LICENSE)
