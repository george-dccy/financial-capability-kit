---
id: prompt.skill.action.query-finhot
kind: skill
display_name_zh: 查询 Finhot 信号雷达 Prompt
target_skill: skill.action.query-finhot
summary: 查询 Finhot 最新动态、产品案例、政策变化、同业动作和经营线索，并结合 Fincap 输出解读。
relations:
  - skill.action.query-finhot
  - skill.action.interpret-financial-signal
  - skill.action.distill-and-curate
---

```text
你要把 Finhot 当作 Fincap 的公开信号雷达和同业产品公开入口使用。

默认 Finhot 地址：
- 生产： https://finhot.boluomi.ren
- 本地： http://localhost:3801
- 如果存在环境变量 FINHOT_PUBLIC_BASE_URL，优先用环境变量。

工作方式：
1. 用户问最新动态、政策变化、同业动作、产品、案例/模式、经营打法、供应链金融、交易银行、现金管理、支付结算、跨境金融时，先查 Finhot。
2. 用户问某家银行交易银行产品、某类产品、同业产品比较、新产品发布或特色产品解读时，优先查 `/api/public/items?content_type=product&...`。同业产品公开信息不放在 Fincap knowledge；Fincap 负责判断框架和解读，个性化产品笔记进入 workspace。
3. 查询入口：
   - /api/public/items?mode=selected&take=10
   - /api/public/items?q=关键词&take=10
   - /api/public/items?content_type=dynamic&take=10
   - /api/public/items?content_type=product&take=10
   - /api/public/items?q=招商银行 交易银行&content_type=product&take=10
   - /api/public/items?q=关键词&days=2&take=10
   - /api/public/items?content_type=case-model&take=10
   - /api/public/items?product_domain=供应链金融&take=10
   - /api/public/items?value_tag=客户经营线索&take=10
   - /api/public/context?q=关键词&days=2&take=10
   - /api/public/items/{slug}
   - /api/public/sources
4. 读取详情时，优先使用返回中的 agent_context.content_markdown、product_domain、value_tags、fincap_analysis、use_rule、answer_boundary。产品集合页正文中的官方链接，是继续读取具体银行产品页面的入口。
5. 读到 Finhot 内容后，再结合 Fincap 的 reference skill、action skill 和 knowledge 输出判断、方案、话术或汇报。
6. dynamic 是来源线索，必须保留 source_url，并提示需要看原文核验；product/manual/detail 可以作为公开同业产品入口或解读上下文，但不能替代银行官方页面和人工核验。
7. product_domain 只表示信号业务归属，value_tags 表示内容用途；不要把它们和 content_type/source_category 混淆。
8. 如果有 fincap_analysis，把它作为结构化草稿，再用 interpret-financial-signal 校正事实、推论、建议和边界。
9. 如果 Finhot 没有覆盖，明确写“Finhot 当前未覆盖”，再回到 Fincap 仓库内的稳定框架，或提示需要外部检索。
10. 不要把 API 路由过程展示给用户，除非用户要求；默认直接给结论、命中内容、解读和下一步。

现在请围绕这个问题查询并回答：
{{在这里粘贴问题}}
```
