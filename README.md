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
| 汇报与拍板 | “领导让我说清楚这个客户值不值得继续跟。” | 输出一句话结论、关键事实、建议动作和拍板项 |
| 跟进与复盘 | “这个客户跟了几轮没推进，问题在哪？” | 复盘卡点、事项状态和下一步推进动作 |
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
请读取并遵循 Financial Capability Kit 安装说明：https://gitee.com/georgedccy/financial-capability-kit/raw/main/INSTALL_FOR_AGENTS.md

然后先读取 README.md、docs/capability-map.md、skills/action/fincap-router/SKILL.md 和 registry/*.json，把这个仓库作为银行从业者的工作诊断与行动工具箱使用。每次回答前先判断我的问题属于客户经营、客户资料研判、动态信号、产品与方案边界、汇报与拍板、跟进复盘，还是能力成长与沉淀。

如果你不能读取仓库正文，请直接说“当前无法访问仓库”，不要按通用金融常识补全。
```

如果是在本地 Agent 中，希望新会话也能自动触发，可安装 resolver skill：

```powershell
git clone https://gitee.com/georgedccy/financial-capability-kit.git fincap
python .\fincap\install\fincap_agent_skill.py --target all
```

给支持读取仓库的聊天模型：

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

演示或试用时，建议先复制上面的“一句话接入”，确认模型能读取仓库后，再直接追问下面这类真实工作问题。不要另写一套脱离 README 的系统提示。

- 我是对公客户经理，明天要见一家做跨境贸易和供应链配套的客户，但资料比较散。你先帮我判断该从哪里入手，哪些信息必须补，首访应该问什么，最后要形成什么推进动作。
- 我手里有客户的财务报表、进销存摘要和几条公开新闻，但暂时不确定这个客户值不值得继续深挖。你帮我做一个经营初判，并告诉我哪些结论能说、哪些还不能说。
- 最近有没有值得关注的交易银行、供应链金融、现金管理或跨境金融同业产品和案例？请先查 Finhot，再帮我判断对客户经营、产品设计或汇报选题有什么启发。
- 领导让我明天汇报一个重点客户推进卡住的问题。你帮我整理成一分钟能讲清楚的版本：一句话判断、关键事实、风险、建议动作和需要领导拍板的事项。
- 我是基层管理者，团队里两个重点客户推进了几轮但没有实质进展。你帮我拆解卡点、安排检查点、明确谁下一步该做什么，以及哪些问题需要上提。
- 我想系统提升自己的财报分析、现金流分析、经营分析和行业理解能力。请先诊断我现在该从哪条能力链路开始，并给我一套可以边做客户边提升的练习方式。
- 我有几次客户经营失败案例和一些个人常用话术。请先帮我判断哪些适合进入 workspace private，哪些未来可以去敏感后整理成 public candidate。

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
