# Awesome Banker Skills

让银行人的优秀经验可安装、可传承、可复用。  
Installable skills and public knowledge packs for bankers and banking clients.

`awesome-banker-skills` 是一个面向银行岗位、银行流程与公开业务知识的开源 Skill 平台。

它不追求做“银行官方统一入口”，而是把一线优秀从业者的做事方法、沟通框架、流程打法和公开知识，整理成可以被 Agent 直接读取、调用和复用的仓库资产。

## 3 个最核心卖点

### 1. 岗位方法论可安装

`roles` 目录沉淀岗位视角，例如对公客户经理的沟通方式、判断框架、推进节奏和风险边界。

### 2. 流程打法可复用

`workflows` 目录沉淀具体工作动作，例如营销客户、陪伴客户、向领导汇报，把重复劳动拆成稳定流程。

### 3. 公开知识可引用

`knowledge-packs` 目录只收录公开、稳定、可引用、适合外部传播的机构知识，帮助 Agent 在不碰内部材料的前提下回答更准确。

## 项目边界

这个项目不是：

- 银行官方统一服务入口
- 在线客服系统
- 业务受理系统
- 审批系统
- 内部知识原文公开库

这个项目强调：

- 岗位方法论与机构公开知识分层维护
- 既支持轻量 prompts，也支持安装型 skills
- repo 地址本身就可以被 Agent 直接消费
- 不放真实客户数据、不放内部制度原文、不放敏感参数、不放审批或授信结论

## 仓库结构

```text
.
├─ README.md
├─ LICENSE
├─ .gitignore
├─ registry/
├─ skills/
│  ├─ roles/
│  └─ workflows/
├─ prompts/
│  ├─ roles/
│  ├─ workflows/
│  └─ knowledge-packs/
├─ knowledge-packs/
│  └─ banks/
└─ workspace/
```

目录职责如下：

- `skills/`：安装型 Agent Skills，遵循 [Agent Skills Specification](https://agentskills.io/specification)
- `prompts/`：轻量入口，适合豆包、千问、Deep Research、通用聊天模型直接复制使用
- `knowledge-packs/`：面向机构公开知识的分包内容
- `registry/`：机器可读索引，方便 Agent 和贡献者发现资产
- `workspace/`：给后续 Agent 和协作者的持续上下文

## 第一阶段 MVP

当前首批资产聚焦“对公业务推进”主线：

- `roles/corp-relationship-manager`
- `workflows/report-to-leader`
- `workflows/market-corporate-client`
- `workflows/accompany-corporate-client`
- `knowledge-packs/banks/ceb/public-basics`

`branch-manager` 已进入 backlog，但不在第一阶段脚手架里。

## 典型使用方式

### 1. 发给豆包、千问、Deep Research 等模型

直接复制 `prompts/` 里的对应文件内容，或把仓库地址发给模型并明确指定要读的路径。

示例：

```text
请读取这个仓库并只使用其中的公开资产回答我：
https://github.com/george-dccy/awesome-banker-skills

优先读取：
1. prompts/workflows/report-to-leader.md
2. knowledge-packs/banks/ceb/public-basics/README.md
3. knowledge-packs/banks/ceb/public-basics/modules/

要求：
- 只基于仓库中的公开内容回答
- 不编造内部制度、审批口径、价格和额度
- 如果仓库中没有依据，就明确说“当前仓库未覆盖”
```

### 2. 给 Claude Code、Codex、OpenClaw 等 Agent 安装或挂载

当前版本不提供安装脚本，默认通过 `registry/` 让 Agent 自行发现技能目录。

示例：

```text
请帮我在本地使用 awesome-banker-skills 仓库中的公开 skills。

仓库地址：
https://github.com/george-dccy/awesome-banker-skills.git

执行要求：
1. 拉取仓库到本地；
2. 读取 registry/skills.json；
3. 启用其中全部 skills/<kind>/<slug>/SKILL.md；
4. 回答时优先路由到对应 role 或 workflow；
5. 如需机构公开知识，再读取 registry/knowledge-packs.json 对应 pack；
6. 不把 knowledge pack 内容写回 role/workflow；
7. 输出本地路径、已启用 skill 数量和可用 skill 列表。
```

### 3. 新增一个 skill 或 knowledge pack

新增资产时请遵循以下规范：

1. 先确定资产类型：`role`、`workflow`、`prompt`、`knowledge-pack`
2. 目录名使用英文 slug，展示名写在中文字段里
3. `skills` 只写方法论，`knowledge-packs` 只写公开事实
4. 每次新增资产都同步更新 `registry/` 和 `README.md`
5. 每个 knowledge pack 都必须带 `sources.md`

## 贡献入口结构

如果你想贡献内容，请优先沿这 4 条路径进入：

- 新增岗位 skill：`skills/roles/<slug>/SKILL.md`
- 新增流程 skill：`skills/workflows/<slug>/SKILL.md`
- 新增知识包：`knowledge-packs/banks/<institution>/<pack-slug>/`
- 新增轻量 prompt：`prompts/<kind>/<slug>.md`

提交前请至少确认：

- slug 是英文且稳定
- 展示名是中文且清晰
- registry 已同步
- README 首页资产目录已同步
- 不包含真实敏感数据与内部材料

## 首批资产目录

### Roles

- `corp-relationship-manager`：对公客户经理的机会判断、客户推进和沟通框架

### Workflows

- `report-to-leader`：把业务进展说清楚、说重点、说诉求
- `market-corporate-client`：客户营销前的场景理解、切入口设计和下一步动作
- `accompany-corporate-client`：客户陪伴、问题跟进和信任维护

### Knowledge Packs

- `banks/ceb/public-basics`：光大银行公开基础知识包，首期覆盖对公基础结算、阳光 e 付通、阳光电费证

## 合规与公开边界

- 仓库只收录公开、稳定、可引用、适合外部传播的内容
- 不收录真实客户信息、内部制度原文、内部审批口径、敏感参数
- 不输出审批结论、定价承诺、授信承诺、受理承诺
- 涉及具体办理安排、额度、费率、准入和时效，请以实际正式沟通结果为准

## 参考思路

本仓库的表达与结构参考以下项目，但会保持自己的分层边界：

- [Agent Skills Specification](https://agentskills.io/specification)
- [khazix-skills](https://github.com/KKKKhazix/khazix-skills)
- [colleague-skill](https://github.com/titanwings/colleague-skill)
- [awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills)
