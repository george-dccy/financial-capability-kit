---
name: interpret-financial-signal
description: 当用户提供新政策、新闻、产品、竞品动作、客户变化、市场信号，或任何需要解读并转成落地建议的金融/商业信息时使用。
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 金融信息解读与落地
  audience: [finance-learner, bank-practitioner, manager]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.corporate-client-coverage-lens
    - skill.reference.client-advance-framework
    - skill.reference.decision-brief-framework
    - skill.action.market-corporate-client
    - skill.action.accompany-corporate-client
    - skill.action.report-decision-brief
    - skill.action.distill-and-curate
    - skill.action.query-finhot
  related_knowledge:
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.yangguang-e-pay
    - knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate
    - knowledge.common.banker-thinking.top-performer
    - knowledge.common.economics.business-basics
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.psychology.business-communication
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 金融信息解读与落地 Skill

## 范围

这是一个 action skill。
它负责把用户新发现的信息，转成银行/金融工作中可理解、可判断、可追问、可落地的行动参考。

它不替代新闻事实核验，不输出内部审批结论，也不把一次性信息直接写成长期知识。

## 使用场景

- 用户贴出政策、监管动态、新闻报道或行业变化，希望判断含义
- 用户发现新产品、行外竞品、机构动作，希望知道对自身工作有什么启发
- 用户发现新客户、客户发生重大变化、客户业务出现新线索，需要形成拜访或跟进方向
- 用户提供 Finhot 动态线索、人工整理内容或后台生成的经营信号解读稿，需要进一步转成行动建议
- 用户给出任意他认为值得解读的材料，希望得到专业视角和落地建议
- 用户继续追问“这对我有什么用”“怎么跟客户讲”“怎么写汇报”“要沉淀到哪里”

## 必读内容

1. `references/signal-classification.md`
2. `references/interpretation-playbook.md`
3. `references/landing-directions.md`
4. `references/knowledge-routing.md`
5. 如果信息涉及最新动态、政策变化、同业动作、产品、案例/模式或外部来源，先用 `skill.action.query-finhot` 查询 Finhot
6. 按命中场景读取相关 reference skill、action skill、knowledge

## 输入契约

最低输入：

- 信息原文、链接、标题、截图转写或用户摘要
- 用户身份或使用场景，如果未提供，默认按“想提升金融能力的个人”处理
- 用户期望产出，如果未提供，默认输出“解读 + 落地参考 + 后续追问方向”

## 执行规则

1. 先判断信息类型：政策、新闻、产品、竞品、客户、行业、风险、能力素材或其他
2. 如果用户只给关键词或问最新情况，先查 Finhot；如果 Finhot 无命中，写明“Finhot 当前未覆盖”
3. 如果输入来自 Finhot，先区分：
   - `dynamic/external`：动态线索，必须保留 `source_url`，提示核验原文，不把摘要当作完整事实
   - `manual/detail`：人工整理内容，可作为站内知识材料，但仍要保留边界
   - `fincap_analysis`：结构化解读草稿，要再核对事实、推论、建议是否分层
4. 再判断工作相关性：能力成长、公开咨询、业务推进、管理跟进、领导汇报
5. 区分事实、推论和建议；事实不足时写明“待核验”或“当前仓库未覆盖”
6. 先给一句话结论，再给影响路径和落地动作
7. 如果用户继续追问，沿同一信息上下文深化，不要每轮重来
8. 如果信息涉及客户经营，建议后续调用 `market-corporate-client`、`accompany-corporate-client` 或 `client-needs-diagnosis`
9. 如果信息涉及管理汇报或材料整理，建议后续调用 `report-decision-brief`
10. 如果材料有长期价值，调用 `skill.action.distill-and-curate` 判断是否进入 private-first 沉淀

## 输出契约

输出至少包含：

1. 一句话结论
2. 信息类型与相关性判断
3. 对银行/金融工作的影响路径
4. 可落地参考方向
5. 需要补证或待确认的信息
6. 后续最值得追问的 1-3 个方向
7. 边界提示

## 质量门槛

- 是否先判断信息类型，而不是直接写观点
- 是否区分公开事实、专业推论和行动建议
- 是否把落地动作落到具体场景，而不是只写宏观意义
- 是否避免编造内部制度、审批、授信、定价、时效承诺
- 是否在证据不足时明确写“待核验”或“当前仓库未覆盖”
- 是否判断该信息是否值得沉淀为 private 资产或 public candidate

## 脚本钩子

- `scripts/build-context.py`：根据信息文本判断类型、推荐读取顺序和相关资产
- `scripts/validate-output.py`：校验解读结果是否包含必要结构和边界提示
