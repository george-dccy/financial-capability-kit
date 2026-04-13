# DEVELOPMENT

## 项目北极星

这个项目要帮助银行人少踩坑、少重复劳动、少加班，让优秀经验可以被安装、传承和复用。

第一阶段不是做“大而全”的银行 AI 产品，而是先证明一件事：

`岗位方法论 + 流程打法 + 公开知识包` 可以组成一条真实可用的对公业务推进链路。

## 资产分层原则

### 1. roles 只写岗位方法论

- 写判断框架、沟通方式、推进节奏、常见失误
- 不写机构事实库
- 不复制 knowledge pack 内容

### 2. workflows 只写工作动作

- 写输入、动作、输出、检查点、失败场景
- 不写成岗位人格故事
- 不沉淀机构知识细节

### 3. knowledge-packs 只写公开知识

- 只收录公开、稳定、可引用、适合外部传播的内容
- 必须带 `sources.md`
- 优先官方来源，必要时补充公开二手来源

### 4. prompts 只是轻量入口

- 不新增独立知识
- 只是把 role、workflow 或 knowledge pack 变成可直接复制的 prompt
- prompt 必须指向目标 skill 或 pack

### 5. registry 是唯一机器索引

- 新增任何资产都要更新对应 registry
- registry 中的 path 必须是仓库内真实存在的路径
- 所有 id 使用英文 slug，不使用中文 id

### 6. workspace 是长期协作上下文

- 给未来切换模型或切换 Agent 的开发者用
- 记录“为什么这样设计”，而不是重复 README 文案

## 命名规则

- 目录名：英文 slug，小写，单词用 `-` 连接
- display name：中文
- skill `name`：必须等于父目录名
- pack id 建议格式：`pack.banks.<institution>.<pack-slug>`
- role id 建议格式：`role.<slug>`
- workflow id 建议格式：`workflow.<slug>`
- prompt id 建议格式：`prompt.<kind>.<slug>`

## 目录契约

```text
skills/<roles|workflows>/<slug>/SKILL.md
prompts/<roles|workflows|knowledge-packs>/<slug>.md
knowledge-packs/banks/<institution>/<pack-slug>/
registry/<skills|prompts|knowledge-packs>.json
workspace/<DEVELOPMENT|PROGRESS|AGENT_PROMPT>.md
```

## 内容红线

严禁写入以下内容：

- 真实客户数据
- 内部制度原文
- 内部审批口径
- 授信、定价、审批或受理结论
- 敏感参数、账号、证件号、合同号、发票号、流水

所有技能和知识包都要明确：

- 这是前期理解与准备辅助
- 不是正式业务受理入口
- 不是审批或授信结论输出器

## 第一阶段边界

第一阶段只做以下 5 类资产：

- `corp-relationship-manager`
- `report-to-leader`
- `market-corporate-client`
- `accompany-corporate-client`
- `banks/ceb/public-basics`

第一阶段不做：

- 前端 demo
- 安装脚本
- 包管理器
- 多银行并行扩张
- `branch-manager`

## 第二阶段优先 backlog

- `branch-manager`
- 更多银行或金融机构的公开知识包
- contribution guide 与模板
- registry 校验脚本
- 轻量安装辅助脚本
- README 英文版

## 开发质量要求

- 先读 `README.md` 与 `workspace/*`
- 新增内容时保持“方法论”和“公开知识”分离
- 每次改动同步更新 `registry/`、`README.md`、`workspace/PROGRESS.md`
- 如果引用公开知识，必须把来源放进对应 pack 的 `sources.md`