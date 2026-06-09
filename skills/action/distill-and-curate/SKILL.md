---
name: distill-and-curate
description: Use when maintainers or contributors need to distill public materials, existing assets, or personal experience into reusable skills or knowledge, then package them for private-first or public contribution.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: distill
  display_name_zh: 蒸馏与整理
  audience: [maintainer, contributor, finance-learner, bank-practitioner]
  related_knowledge:
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.psychology.business-communication
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 蒸馏与整理 Skill

## Scope

这是一个 action skill。
它用来把公开材料、仓库已有资产和用户经验，增量整理成：

- reference skill
- action skill
- knowledge

默认先走 `private-first`，不做无审查自动覆写。

## When To Use

- 想从文档、链接、说明材料中提炼新资产
- 想从 Finhot 动态、人工校准信号或管理员提炼草稿中判断是否沉淀为 Fincap 资产
- 想补全已有 skill 或 knowledge
- 想把 private 内容整理成 public contribution candidate
- 想先给出 patch proposal，再由用户确认落库

## Required Reads

1. `references/asset-classification.md`
2. `references/private-public-flow.md`
3. `references/output-templates.md`
4. `references/contribution-checklist.md`
5. 如果目标资产已存在，先读该资产当前正文与对应 registry

## Input Contract

至少明确以下信息：

- 输入材料来源
- 如果来源是 Finhot，标明是 `dynamic/external`、`manual/detail` 还是管理员生成的 `fincap_analysis`
- 目标内容更像 reference skill、action skill 还是 knowledge
- 目标是 `private-first` 还是 `public-candidate`
- 是新建、补全、修订，还是 private 转 public

信息不足时，先补关键缺口，不要直接重写整个资产。

## Classification Rule

- 专业视角、判断框架、表达结构、复盘框架 -> `skills/reference`
- 面向具体任务的输入、步骤、输出、检查点 -> `skills/action`
- 公开事实、公开产品、公开来源、FAQ -> `knowledge/*`
- Finhot `dynamic/external` 默认只是线索，不能直接写入 public knowledge；先核验原文和来源日期
- Finhot `manual/detail` 可作为站内材料，但进入 public 仍要补来源、边界和 registry
- Finhot `fincap_analysis` 可作为结构化草稿，不等于最终结论

## Default Flow

1. 读取输入材料与目标资产现状
2. 判断更适合落到 `reference`、`action` 还是 `knowledge`
3. 先决定是 `create`、`extend`、`revise` 还是 `promote-private-to-public`
4. 默认生成 `private-first` 草稿
5. 如果来自 Finhot，输出建议目标路径、资产类型、增量摘要、公开边界和待核验事实
6. 输出 patch proposal 和 change summary
7. 用户确认后再真正更新正文与 registry

## Output Contract

输出至少包含：

1. 资产归类判断
2. 建议目标路径
3. 建议生成或修改的文件
4. 增量变更摘要
5. private-first 还是 public-candidate 的建议
6. 公开贡献时的风险与边界提示

## Quality Gate

- 是否误把 reference skill 写成 action 流程
- 是否误把 action skill 写成知识清单
- 是否误把公开事实写进 skill
- 是否优先做增量更新，而不是整包重写
- 是否默认先写 private
- 是否明确哪些内容需要用户确认后才能公开

## Script Hooks

- `scripts/detect-target.py`：根据输入内容给出资产类型和推荐落点
- `scripts/build-asset-skeleton.py`：生成建议目录结构与文件清单
- `scripts/build-change-summary.py`：生成变更摘要或贡献摘要
