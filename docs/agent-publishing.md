# 个人金融工作 Agent 发布说明

本文件说明如何把本仓库形成的能力发布为个人金融工作 Agent。

## 1. 发布目标

发布 Fincap 时，应把它作为能力底座，而不是固定人格。

这个 Agent 应该像：

- 银行/金融工作助手
- repo-first 的专业知识使用者
- private-first 的个人经验整理者
- 能直接生成简报、话术、清单和跟进计划的执行者

它不应该像：

- 银行客服机器人
- 会编造内部制度的模型
- 某个人的人格克隆
- 泛化搜索助手

## 2. 最小 Agent 能力包

如果平台支持自定义 Agent，优先上传或连接：

- `agent-skills/financial-capability-kit/SKILL.md`
- `INSTALL_FOR_AGENTS.md`
- `README.md`
- `docs/capability-map.md`
- `skills/action/fincap-router/SKILL.md`
- `registry/*.json`
- `prompts/entrypoints/agent/general.md`
- 需要使用的 `skills/*` 和 `knowledge/*`

如果平台限制文件数量，优先保留 `agent-skills/financial-capability-kit/SKILL.md`、`docs/capability-map.md`、`skills/action/fincap-router/SKILL.md`、registry 文件和 Agent 入口 prompt。

`agent-skills/financial-capability-kit/SKILL.md` 是让新 session 能按上下文自动触发 Fincap 的关键，不只是让用户每次复制一大段 prompt。

## 3. 平台接入方式

对可以克隆仓库的平台，给 Agent 这段指令：

```text
Read https://gitee.com/georgedccy/financial-capability-kit.git and follow INSTALL_FOR_AGENTS.md, README.md, docs/capability-map.md, and skills/action/fincap-router/SKILL.md.

Use the repository as my banking and financial capability base. Before answering, route my question as customer coverage, customer material analysis, dynamic signal, product boundary, decision brief, follow-up review, or capability growth. If you cannot read repository files, say so directly.
```

对本地 skill 型 Agent，安装 resolver skill：

```powershell
python install/fincap_agent_skill.py --target all
```

Windows 用户也可以使用包装脚本：

```powershell
powershell -ExecutionPolicy Bypass -File .\install\fincap-agent-skill.ps1 -Target all
```

对只支持上传文档的平台：

1. 上传 `agent-skills/financial-capability-kit/SKILL.md`
2. 上传 `INSTALL_FOR_AGENTS.md`
3. 上传 `README.md`
4. 上传 `docs/capability-map.md`
5. 上传 `skills/action/fincap-router/SKILL.md`
6. 上传 `registry/*.json`
7. 上传目标 skill 或 knowledge 文件夹
8. 将 `prompts/entrypoints/agent/general.md` 设置为系统指令或开发者指令

对纯聊天工具，使用：

```text
Read INSTALL_FOR_CHAT_MODELS.md, README.md, docs/capability-map.md, and skills/action/fincap-router/SKILL.md first. If you cannot access repository content, do not answer as if you had read it.
```

## 4. Kimi、MiniMax、OpenClaw、Hermes 等平台

模型和平台能力变化很快。
只有当平台确实支持读取文件、保留指令或调用工具时，才使用其专属 Agent 能力。

推荐打包方式：

- MiniMax：使用能克隆或读取仓库内容的模式
- Kimi Agent 或类似平台：上传 resolver skill、能力地图、主路由、安装说明、registry 文件和选定 skill，作为能力包使用
- OpenClaw 或 Hermes 风格 Agent：克隆仓库，并把 resolver 文件绑定到 Agent 启动流程
- CLI Agent：将本仓库作为工作目录，并读取 `INSTALL_FOR_AGENTS.md`

本仓库应保持模型无关。
不要把任何一个厂商的工作流写成唯一支持路径。

## 5. 多 Agent 协作

多 Agent 系统中，按任务边界拆分角色：

- 信息解读 Agent：使用 `skill.action.interpret-financial-signal`
- 产品地图 Agent：基于官方来源扩充公开产品知识
- Skill 整理 Agent：把高频任务整理成 reference skill 或 action skill
- 汇报简报 Agent：把复杂事项整理成领导可判断、可拍板的版本
- Review Agent：检查来源、边界、registry 一致性和风险措辞

Agent 之间应通过明确产物交接：

- 输入材料
- 选用资产
- 输出草稿
- 来源列表
- 未解决问题
- 建议仓库更新

避免只用含糊聊天记录交接。

## 6. 私有层

个人案例、偏好、失败经验、客户笔记和工作记忆，默认不能发布。

优先使用 private-first 存储：

- `workspace/private/skills`
- `workspace/private/memories`
- `workspace/private/case-notes`
- `workspace/private/knowledge`

只有完成去敏感化并补齐公开来源后，才考虑进入 public candidate。
