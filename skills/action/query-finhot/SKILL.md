---
name: query-finhot
description: 当任务需要读取最新金融动态、Finhot 已沉淀的产品/案例/模式/政策/观察/打法，或需要把 Fincap 与 Finhot 内容库联动时使用。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: retrieve
  display_name_zh: 查询 Finhot 内容库
  audience: [finance-learner, bank-practitioner, manager]
  related_skills:
    - skill.action.interpret-financial-signal
    - skill.action.distill-and-curate
    - skill.action.market-corporate-client
    - skill.action.product-matching-boundary
  related_prompts:
    - prompt.skill.action.query-finhot
---

# 查询 Finhot 内容库 Skill

## 范围

Finhot 是 Fincap 的内容库、动态库和知识沉淀前台。Fincap 仍保留稳定的方法框架、任务流程和边界规则；涉及最新动态、外部来源、产品拆解、案例/模式、政策观察和人工整理内容时，优先查询 Finhot。

## 默认端点

生产站：

```text
https://finhot.boluomi.ren
```

本地开发：

```text
http://localhost:3801
```

如环境变量存在，优先使用：

```text
FINHOT_PUBLIC_BASE_URL
```

## 查询方式

最新精选：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?mode=selected&take=10"
```

按关键词：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?q=现金管理&take=10"
```

最近 2 天某关键词：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?q=现金管理&days=2&take=10"
```

按内容分类：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?content_type=dynamic&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?category=product&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?category=case-model&take=10"
```

按来源分类：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?source_category=regulator&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?source_category=bank&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?source_category=media&take=10"
```

信源列表：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/sources"
```

Agent 读取上下文：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/context?q=供应链金融&days=2&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items/{slug}"
```

`/api/public/context` 会返回每条内容的使用规则：动态线索保留来源链接，人工整理内容可继续读取详情 API。`/api/public/items/{slug}` 会返回 `agent_context`，其中 `content_markdown`、`use_rule`、`answer_boundary` 是给 Agent 读取的稳定字段。

## 使用规则

1. 如果用户问“最新”“动态”“近期”“同业”“政策变化”“新产品”“案例”，先查 Finhot，再结合 Fincap skill 解读。
2. `content_type=dynamic` 是发现层，点击或引用时应保留 `source_url`，不要把它当成站内知识定稿。
3. 人工整理内容的 `link_mode=detail`，可以作为站内沉淀内容读取和复用；优先读取详情 API 的 `agent_context.content_markdown`，再结合 `use_rule` 和 `answer_boundary` 回答。
4. 回答时区分：
   - Finhot 原始动态：来源线索，适合进一步核验
   - Finhot 人工整理：可作为 Fincap 的内容依据
   - Fincap skill：负责判断框架、执行流程和表达结构
5. 如果 Finhot 无结果，写明“Finhot 当前未覆盖”，再回到 Fincap 仓库稳定知识或提示需要外部检索。

## 输出建议

默认不要展示 API 细节。面向用户时直接输出：

- 一句话结论
- 命中的 Finhot 动态/内容
- 可落地解读
- 需要继续核验或人工整理的方向

## 边界

- 不把 Finhot 动态视作监管结论。
- 不复制外部来源全文。
- 不输出内部审批、授信、定价、时效承诺。
- 涉及客户敏感信息时，回到 private-first 处理。
