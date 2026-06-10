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

Finhot 是 Fincap 的公开信号雷达。Fincap 保留稳定的方法框架、任务流程、边界规则和可公开基础知识；涉及最新动态、外部来源、政策变化、产品案例、同业动作、同业产品集合和经营线索时，优先查询 Finhot。

同业产品信息不再沉淀到 Fincap public knowledge。公开同业产品集合、某家银行交易银行产品入口、特色产品解读、新产品发布等内容，统一进入 Finhot 的 `content_type=product`。用户自己的比较表、客户化解读和不便公开的产品笔记，应进入 workspace。

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
- `content_type=product` 是同业产品集合、特色产品和新产品信号的主入口；`product_domain` 是信号归属字段，不是产品百科路径。打标不足时，主路径仍然是 `/api/public/items` + `q` + `content_type=product` + `take`。
- 一条银行产品集合通常代表“一家银行公开交易银行/公司金融产品入口表”。正文里的官方链接是给人和 Agent 继续读取更细产品页面的入口。
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

按产品内容、产品信号归属或价值标签：

```bash
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "content_type=product" \
  --data-urlencode "take=10"
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "q=招商银行 交易银行" \
  --data-urlencode "content_type=product" \
  --data-urlencode "take=10"
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "product_domain=供应链金融" \
  --data-urlencode "take=10"
curl --get "$FINHOT_PUBLIC_BASE_URL/api/public/items" \
  --data-urlencode "value_tag=客户经营线索" \
  --data-urlencode "take=10"
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
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?content_type=product&take=10"
curl "$FINHOT_PUBLIC_BASE_URL/api/public/items?content_type=case-model&take=10"
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
2. 如果用户问某家银行产品、某类交易银行产品、同业产品比较，先查 `content_type=product`，优先命中银行产品集合页；再读取 `/api/public/items/{slug}` 的 `agent_context.content_markdown`，沿正文官方链接继续核验。
3. `content_type=dynamic` 是发现层，点击或引用时应保留 `source_url`，不要把它当成完整事实或 Fincap 知识定稿。
4. 人工校准信号的 `link_mode=detail`，可以作为解读上下文读取；优先读取详情 API 的 `agent_context.content_markdown`，再结合 `use_rule` 和 `answer_boundary` 回答。稳定知识仍以 Fincap `knowledge/*` 为准；同业产品集合除外，它们应从 Finhot 读取。
5. 回答时区分：
   - Finhot 原始动态：来源线索，适合进一步核验
   - Finhot 产品集合/特色产品：可作为公开同业产品入口和比较素材，正文链接需要继续核验
   - Finhot 人工校准信号：可作为解读上下文，不是基础知识库
   - Finhot 产品领域 `product_domain`：表示信号业务归属，如供应链金融、现金管理、跨境金融
   - Finhot 价值标签 `value_tags`：表示这条内容可用于客户经营、产品设计、风险识别、政策跟踪、汇报材料等用途
   - Fincap skill：负责判断框架、执行流程和表达结构
6. 如果返回 `fincap_analysis`，先把它当作结构化解读草稿，再用 `interpret-financial-signal` 校正事实、推论、建议和边界。
7. 如果 Finhot 无结果，写明“Finhot 当前未覆盖”，再回到 Fincap 仓库稳定框架或提示需要外部检索。
8. 如果用户需要沉淀个性化产品比较、客户化判断或内部口径，继续用 `distill-and-curate` 按 private-first 进入 workspace。

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
