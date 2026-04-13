# Awesome Banker Skills

让银行人的优秀经验可安装、可传承、可复用。  
Installable skills and structured knowledge packs for bankers and banking clients.

`awesome-banker-skills` 是一个面向银行岗位与流程的 Skill 集合，支持两类核心资产：

- `skills`：岗位方法论与流程打法
- `knowledge-packs`：机构公开知识

## 核心定位

- 银行人的工作技能库
- 银行岗位与流程 Skill 平台
- 让优秀经验可安装、可传承、可复用

## 当前架构

```text
.
├─ skills/
│  ├─ roles/
│  │  └─ <skill>/SKILL.md + references/ + scripts/
│  └─ workflows/
│     └─ <skill>/SKILL.md + references/ + scripts/
├─ knowledge-packs/
│  └─ banks/ceb/
│     ├─ corporate-settlement/basic-settlement/
│     ├─ transaction-banking/yangguang-e-pay/
│     └─ trade-finance/yangguang-electricity-certificate/
├─ prompts/
├─ registry/
└─ workspace/
```

## 典型使用方式

### 1. 直接给模型使用

先用一个总prompt：

- `prompts/entrypoints/auto.md`

```text
你现在是一个“仓库驱动的银行业务助手”。请优先使用这个仓库作为能力来源，并自动判断该用哪些 skills 与 knowledge packs 来回答我的问题。

仓库地址：
https://github.com/george-dccy/awesome-banker-skills

执行规则（必须遵守）：
1. 先读取 registry/skills.json、registry/prompts.json、registry/knowledge-packs.json；
2. 根据我的问题自动路由，选出最相关的 1-2 个 skill（必要时可多选）；
3. 读取所选 skill 目录中的 SKILL.md + references/*；
4. 按 skill 的 knowledge routing 与 related_packs，读取对应 knowledge pack 的 README.md、modules/*、faq.md、sources.md；
5. 回答时必须把“岗位方法论”与“公开知识事实”分层表达，不要混在一起；
6. 不编造内部制度，不输出审批/授信/定价/受理承诺，不索取真实敏感信息；
7. 如果仓库覆盖不足，明确写“当前仓库未覆盖”，并告诉我还缺什么信息。

回答输出格式：
A. 路由决策（你用了哪些 skill / pack，为什么）
B. 结论（先给简明结论）
C. 依据（按“方法论依据 / 公开知识依据”分开）
D. 下一步建议（可执行）
E. 边界提示（合规与不确定项）

请现在开始，并先复述你准备读取的文件路径。
```

这段 prompt 会让模型自动读取 `registry/*.json`，自动选择 skill 和 knowledge pack 再回答。

如果你只想做某一个专项任务，再使用 `prompts/roles/*` 或 `prompts/workflows/*`。

### 2. 给 Agent 安装使用

可直接把下面这段发给 OpenClaw、Claude Code、Codex 等 Agent：

```text
请帮我安装并启用 awesome-banker-skills 仓库中的技能库。

仓库地址：
https://github.com/george-dccy/awesome-banker-skills.git

安装与调用要求：
1. 拉取仓库到本地工作目录；
2. 读取 registry/skills.json、registry/knowledge-packs.json、registry/prompts.json；
3. 启用 registry/skills.json 里全部 skill 的 SKILL.md；
4. 回答时先做路由：根据用户问题自动选择最相关的 1-2 个 skill；
5. 读取所选 skill 的 references/* 与 scripts/build-context.py；
6. 根据 build-context.py 和 SKILL.md 的 related_packs，读取对应 knowledge-pack 的 README.md、modules/*、faq.md、sources.md；
7. 生成答案后调用 scripts/validate-output.py 做结构检查；
8. 输出时包含：路由决策、结论、依据、下一步建议、边界提示；
9. 不输出内部制度、审批/授信/定价承诺，不要求真实敏感数据；
10. 若仓库未覆盖，明确说“当前仓库未覆盖”，并说明缺失信息。

安装完成后请回报：
- 本地路径
- 已启用 skills 列表
- 每个 skill 关联的 knowledge packs
- 推荐我如何提问以获得最佳效果
```

Agent 在执行时的核心调用链：

- `references/*`（方法论、路由、输出约定）
- `scripts/build-context.py`（知识包路由）
- `scripts/validate-output.py`（结构校验）

## 支持用户自蒸馏并贡献

项目把“个人经验蒸馏 -> 仓库规范化 -> PR 贡献”设计为标准路径：

1. 用模板采集你的真实工作样本与判断逻辑  
   `templates/distill-skill/intake.md`
2. 按模板生成一个 skill 包  
   `templates/distill-skill/SKILL.template.md`
3. 补齐 `references/` 与 `scripts/`
4. 在 `registry/` 注册并提交 PR

详细见 [CONTRIBUTING.md](./CONTRIBUTING.md) 与 [docs/distillation/WORKFLOW.md](./docs/distillation/WORKFLOW.md)。

## 边界与合规

- 不会放真实客户数据
- 不会放内部制度原文
- 不会放内部审批、授信、定价结论
- 不会承诺额度、费率、时效与办理结果

## LICENSE

[MIT](./LICENSE)
