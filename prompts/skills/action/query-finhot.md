---
id: prompt.skill.action.query-finhot
kind: skill
display_name_zh: 查询 Finhot 内容库 Prompt
target_skill: skill.action.query-finhot
summary: 查询 Finhot 最新动态、产品、案例/模式、政策、观察和打法，并结合 Fincap 输出解读。
---

```text
你要把 Finhot 当作 Fincap 的内容库和动态库使用。

默认 Finhot 地址：
- 生产： https://finhot.boluomi.ren
- 本地： http://localhost:3801
- 如果存在环境变量 FINHOT_PUBLIC_BASE_URL，优先用环境变量。

工作方式：
1. 用户问最新动态、政策变化、同业动作、产品、案例/模式、经营打法、供应链金融、交易银行、现金管理、支付结算、跨境金融时，先查 Finhot。
2. 查询入口：
   - /api/public/items?mode=selected&take=10
   - /api/public/items?q=关键词&take=10
   - /api/public/items?content_type=dynamic&take=10
   - /api/public/items?q=关键词&days=2&take=10
   - /api/public/items?category=product&take=10
   - /api/public/items?category=case-model&take=10
   - /api/public/context?q=关键词&days=2&take=10
   - /api/public/items/{slug}
   - /api/public/sources
3. 读取详情时，优先使用返回中的 agent_context.content_markdown、use_rule、answer_boundary。
4. 读到 Finhot 内容后，再结合 Fincap 的 reference skill、action skill 和 knowledge 输出判断、方案、话术或汇报。
5. dynamic 是来源线索，必须保留 source_url，并提示需要看原文核验；人工整理内容可以作为站内沉淀读取。
6. 如果 Finhot 没有覆盖，明确写“Finhot 当前未覆盖”，再回到 Fincap 仓库内的稳定框架和知识。
7. 不要把 API 路由过程展示给用户，除非用户要求；默认直接给结论、命中内容、解读和下一步。

现在请围绕这个问题查询并回答：
{{在这里粘贴问题}}
```
