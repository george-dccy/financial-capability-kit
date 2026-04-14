---
name: distill-and-contribute
description: Use when maintainers or contributors need to distill skills, knowledge packs, or methods from public materials, update repository assets incrementally, or prepare private-first drafts for public contribution.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  banker_kind: workflow
  display_name_zh: 蒸馏与贡献协作
  related_packs:
    - pack.common.banker-thinking.top-performer
    - pack.common.sales.consultative-b2b
    - pack.common.psychology.business-communication
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 蒸馏与贡献协作 Skill

## Scope

这个 workflow 用来帮助维护者和贡献者，把公开材料、仓库已有资产和用户经验，增量提炼成：

- role skill
- workflow skill
- knowledge pack
- method

默认先走 `private-first`，不做无审查自动覆写。

## 适用场景

- 想从文档、链接、说明材料中提炼新资产
- 想补全已有 knowledge pack / method / skill
- 想把 private 内容整理成 public contribution candidate
- 想先写 patch proposal，再由用户确认更新

## Required Reads

1. `references/asset-classification.md`
2. `references/private-public-flow.md`
3. `references/output-templates.md`
4. `references/contribution-checklist.md`
5. 如果目标资产已存在，先读该资产当前正文与对应 registry

## Input Contract

至少明确以下信息：

- 输入材料来源
- 目标内容更像角色 skill / workflow / knowledge pack / method 哪一类
- 目标是 `private-first` 还是 `public-candidate`
- 是新建、补全、修订，还是 private 转 public

信息不足时，先补关键缺口，不要直接重写整个资产。

## Classification Rule

- 岗位使命、默认视角、优先级规则、关键对象沟通差异、常见误区、调用规则 -> `skills/roles`
- 输入、动作、输出、检查点、失败场景 -> `skills/workflows`
- 公开事实、公开产品、公开来源 -> `knowledge-packs/banks` 或 `knowledge-packs/common`
- 跨岗位复用的判断与推进框架 -> `methods`

## Default Flow

1. 读取输入材料与目标资产现状
2. 判断应落哪一层
3. 先决定是 `create`、`extend`、`revise` 还是 `promote-private-to-public`
4. 默认生成 `private-first` 草稿
5. 输出 patch proposal 和 change summary
6. 用户确认后再真正更新正文与 registry

## Output Contract

输出至少包含：

1. 资产归类判断
2. 建议目标路径
3. 建议生成或修改的文件
4. 增量变更摘要
5. private-first 还是 public-candidate 的建议
6. 公开贡献时的风险与边界提示

## Quality Gate

- 是否误把岗位视角写成 workflow 编排
- 是否误把跨岗位复用框架写进 role skill
- 是否误把方法论写进 knowledge pack
- 是否误把公开事实写进 skill
- 是否优先做增量更新，而不是整包重写
- 是否默认先写 private
- 是否明确哪些内容需要用户确认后才能公开

## Script Hooks

- `scripts/detect-target.py`：根据输入内容给出资产类型和推荐落点
- `scripts/build-asset-skeleton.py`：生成建议目录结构与文件清单
- `scripts/build-change-summary.py`：生成变更摘要或贡献摘要
