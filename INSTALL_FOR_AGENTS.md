# 面向 Agent 的 Fincap 安装说明

请先完整读取本文件，然后把本仓库作为用户的银行/金融专业能力底座使用。

## 一句话安装

让 Agent 先执行这条指令：

```text
请读取并遵循 Financial Capability Kit 安装说明：https://gitee.com/georgedccy/financial-capability-kit/raw/main/INSTALL_FOR_AGENTS.md
```

如果 Gitee 原始文件访问不可用，使用 GitHub 镜像：

```text
请读取并遵循 Financial Capability Kit 安装说明：https://raw.githubusercontent.com/george-dccy/financial-capability-kit/main/INSTALL_FOR_AGENTS.md
```

## 第 1 步：克隆或读取仓库

优先使用 Gitee 主仓库：

```powershell
git clone https://gitee.com/georgedccy/financial-capability-kit.git fincap
cd fincap
```

如果 Gitee 不可用，使用 GitHub 镜像：

```powershell
git clone https://github.com/george-dccy/financial-capability-kit.git fincap
cd fincap
```

如果平台不能克隆仓库，至少需要读取这些文件：

- `README.md`
- `registry/skills.json`
- `registry/knowledge.json`
- `registry/prompts.json`
- `skills/action/fincap-router/SKILL.md`
- `docs/capability-map.md`
- `prompts/entrypoints/agent/general.md`

## 第 2 步：安装常驻 resolver skill

最佳安装方式是把 Fincap 安装成一个“路由型 skill”。

这样即使新开对话 session，只要用户问题进入银行、金融、客户推进、产品理解、政策新闻解读、竞品分析、汇报表达等上下文，Agent 也能自动触发 Fincap，并按仓库 registry 找到合适的正文内容。

跨平台推荐使用 Python 安装器：

```powershell
python install/fincap_agent_skill.py --target all
```

Windows 用户也可以使用 PowerShell 包装脚本：

```powershell
powershell -ExecutionPolicy Bypass -File .\install\fincap-agent-skill.ps1 -Target all
```

安装器会复制：

```text
agent-skills/financial-capability-kit/SKILL.md
```

到常见本地 skill 目录：

- `~/.claude/skills/financial-capability-kit`
- `~/.codex/skills/financial-capability-kit`
- `~/.agents/skills/financial-capability-kit`

安装器还会写入 `repository-path.txt`，让已安装的 skill 知道本仓库位于哪里。

安装后，请重启或新开一个 Agent session，让 skill 索引重新加载。

如果平台有自己的 skill 市场、自定义 skill、长期记忆、知识库或持久系统指令机制，请把 `agent-skills/financial-capability-kit/SKILL.md` 安装或上传到对应位置。

如果平台不能安装 skill，则把 `prompts/entrypoints/agent/general.md` 放入系统指令或开发者指令中。这种方式弱于真正的 skill，因为它不一定能在每个新 session 中自动触发。

## 第 3 步：加载仓库 resolver

把三个 registry 文件当作仓库路由器：

- `registry/skills.json`：判断要读取哪个 reference skill 或 action skill
- `registry/knowledge.json`：判断要读取哪个公开知识包
- `registry/prompts.json`：判断是否可复用某个入口 prompt 或轻量 prompt

如果仓库中已有相关 skill 或 knowledge，不要绕开仓库直接用泛化金融常识回答。

## 第 4 步：加载默认 Agent 入口

读取：

```text
prompts/entrypoints/agent/general.md
```

并优先读取 Fincap 主路由：

```text
skills/action/fincap-router/SKILL.md
```

后续整个会话都应遵守该入口约束，而不是只在第一轮生效。

## 第 5 步：自检仓库访问

正式回答用户第一个真实问题前，先确认：

- 能读取全部三个 `registry/*.json`
- 能列出至少一个相关的 `skills/*/SKILL.md` 或 `knowledge/*/README.md`
- 能说明本轮将使用哪个文件，但最终回答不要展示冗长技术路由过程

如果做不到，直接说：

```text
当前无法访问仓库，不能保证按 Financial Capability Kit 回答。
```

## 第 6 步：工作规则

- 专业视角、判断框架、表达结构：读取 `skills/reference/*`
- 任务推进、客户拜访、汇报、清单、复盘：读取 `skills/action/*`
- 公开产品事实、FAQ、来源：读取 `knowledge/*`
- 新政策、新闻、产品、竞品、客户变化或其他新信息：读取 `skills/action/interpret-financial-signal`
- 用户经验、偏好、案例、失败教训和个人方法：如果平台支持，优先进入私有 workspace

## 第 7 步：边界

不要编造：

- 银行内部制度
- 审批结论
- 授信额度
- 定价
- 办理时效承诺
- 真实客户信息

如果仓库未覆盖用户问题，写：

```text
当前仓库未覆盖
```

然后说明缺少什么来源、材料或决策。

## 第 8 步：更新

如果本仓库已在本地克隆：

```powershell
git pull origin main
```

公共仓库更新不能覆盖用户的私有 workspace。
