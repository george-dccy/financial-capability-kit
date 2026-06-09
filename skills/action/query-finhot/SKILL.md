---
name: query-finhot
description: 当任务需要读取最新金融动态、政策变化、产品案例、同业动作或经营线索，或需要把 Fincap 与 Finhot 信号雷达联动时使用。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: retrieve
  display_name_zh: 查询 Finhot 信号雷达
  audience: [finance-learner, bank-practitioner, manager]
  related_skills:
    - skill.action.interpret-financial-signal
    - skill.action.distill-and-curate
    - skill.action.market-corporate-client
    - skill.action.product-matching-boundary
  related_prompts:
    - prompt.skill.action.query-finhot
---

# 查询 Finhot 信号雷达 Skill

## 范围

Finhot 是 Fincap 的公开信号雷达。Fincap 保留稳定的知识、产品地图、方法框架、任务流程和边界规则；涉及最新动态、外部来源、政策变化、产品案例、同业动作和经营线索时，优先查询 Finhot。

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

## 踩坑与正确调用姿势

- `/api/public/context` 已与 `/api/public/items` 对齐，支持 `q`、`category`、`content_type`、`source_category`、`product_domain`、`value_tag`、`days`、`take` 等同一组查询参数。
- 中文参数必须 URL encode。命令行调用时使用 `curl --get --data-urlencode`；不要把 `?q=供应链金融&days=2` 这类中文 query 直接拼进 URL。
- `product_domain` 是信号归属字段，不是产品百科路径。它只返回已经完成产品域打标的内容；打标不足时，主路径仍然是 `/api/public/items` + `q` + `category` + `days` + `take`。
- `dynamic/external` 是动态线索，必须保留 `source_url` 并提示核验原文；`manual/detail` 是人工校准信号，可继续读取详情 API，但不能替代 Fincap knowledge。

## 查询方式

最新精选：

```bash
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?mode=selected&take=10"
```

按关键词：

```bash
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "q=现金管理" \
  --data-urlencode "take=10"
```

按产品信号归属或价值标签：

```bash
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "product_domain=供应链金融" \
  --data-urlencode "take=10"
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "value_tag=客户经营线索" \
  --data-urlencode "take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/product-domains"
```

最近 2 天某关键词：

```bash
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "q=现金管理" \
  --data-urlencode "days=2" \
  --data-urlencode "take=10"
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
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/context" \
  --data-urlencode "q=供应链金融" \
  --data-urlencode "days=2" \
  --data-urlencode "take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items/{slug}"
```

`/api/public/context` 会返回每条内容的使用规则：动态线索保留来源链接，人工校准信号可继续读取详情 API。`/api/public/items/{slug}` 会返回 `agent_context`，其中 `content_markdown`、`product_domain`、`value_tags`、`fincap_analysis`、`use_rule`、`answer_boundary` 是给 Agent 读取的稳定字段。

## 使用规则

1. 如果用户问“最新”“动态”“近期”“同业”“政策变化”“新产品”“案例”，先查 Finhot，再结合 Fincap skill 解读。
2. `content_type=dynamic` 是发现层，点击或引用时应保留 `source_url`，不要把它当成完整事实或 Fincap 知识定稿。
3. 人工校准信号的 `link_mode=detail`，可以作为解读上下文读取；优先读取详情 API 的 `agent_context.content_markdown`，再结合 `use_rule` 和 `answer_boundary` 回答。稳定知识仍以 Fincap `knowledge/*` 为准。
4. 回答时区分：
   - Finhot 原始动态：来源线索，适合进一步核验
   - Finhot 人工校准信号：可作为解读上下文，不是基础知识库
   - Finhot 产品领域 `product_domain`：表示信号业务归属，如供应链金融、现金管理、跨境金融
   - Finhot 价值标签 `value_tags`：表示这条内容可用于客户经营、产品设计、风险识别、政策跟踪、汇报材料等用途
   - Fincap skill：负责判断框架、执行流程和表达结构
5. 如果返回 `fincap_analysis`，先把它当作结构化解读草稿，再用 `interpret-financial-signal` 校正事实、推论、建议和边界。
6. 如果 Finhot 无结果，写明“Finhot 当前未覆盖”，再回到 Fincap 仓库稳定知识或提示需要外部检索。
7. 如果命中内容有长期价值，继续用 `distill-and-curate` 判断是否进入 private-first 或 public candidate。

## 输出建议

默认不要展示 API 细节。面向用户时直接输出：

- 一句话结论
- 命中的 Finhot 动态/内容
- 可落地解读
- 需要继续核验、人工校准或转入 Fincap/workspace 的方向

## 边界

- 不把 Finhot 动态视作监管结论。
- 不复制外部来源全文。
- 不输出内部审批、授信、定价、时效承诺。
- 涉及客户敏感信息时，回到 private-first 处理。
