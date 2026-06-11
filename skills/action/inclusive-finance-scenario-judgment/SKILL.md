---
name: skill.action.inclusive-finance-scenario-judgment
description: Use when you need to quickly determine if a client or scenario qualifies for inclusive finance (普惠金融) products, identify the applicable policy category, and match to appropriate product candidates.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 普惠金融场景判断
  audience: [bank-practitioner]
  related_skills:
    - skill.action.client-needs-diagnosis
    - skill.action.product-matching-boundary
    - skill.reference.problem-opportunity-framework
    - skill.reference.corporate-client-coverage-lens
  related_knowledge:
    - knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map
    - knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map
    - knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map
    - knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 普惠金融场景判断 Skill

## Scope

这是一个 action skill。
它聚焦"场景识别"，负责在接触客户或接收业务线索时，快速判断该场景是否属于普惠金融适用范畴，并输出政策依据级别和产品候选方向。

与 `skill.action.client-needs-diagnosis` 的边界：

- `client-needs-diagnosis`：通用客户需求诊断，覆盖全行业全产品线
- `inclusive-finance-scenario-judgment`：专精普惠金融，判断是否适用、匹配哪类政策框架、建议哪类产品方向

简单说：`client-needs-diagnosis` 告诉你"他需要什么"，`inclusive-finance-scenario-judgment` 告诉你"他是不是普惠客户、属于哪类普惠"。

## When To Use

- 接触新客户时，判断其是否属于普惠金融适用客群
- 收到融资需求时，先判断是否应该走普惠条线
- 会后跟进时，需要明确客户的普惠分类和政策依据
- 需要给 `skill.action.product-matching-boundary` 提供"普惠场景判断结论"时

## Required Reads

1. `references/scenario-identification.md`
2. `references/policy-boundary.md`
3. `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`
4. `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`
5. `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`

## Execution Rule

1. 先用 `references/scenario-identification.md` 判断主体资格（规模、行业）
2. 再用 `references/policy-boundary.md` 核查政策匹配层级和监管红线
3. 结合光大普惠金融产品体系（阳光普惠 vs 阳光兴农），输出产品候选方向
4. 最后输出场景判断结论和政策依据

## Input Contract

最低输入（三选二）：

- 客户主营业务描述
- 企业规模信息（员工数/年营收/注册资本）
- 行业分类（制造业/科技/三农/服务等）

可选补充：

- 融资需求概述（金额/用途/期限）
- 企业注册地类型（城市/县城/农村）
- 客户归属判断（已接触/待开发/转介绍）

## Output Contract

必须包含：

1. **场景判断结论**：属于普惠 / 可能属于普惠 / 不属于普惠（附原因）
2. **适用客群分类**：小微企业 / 三农 / 重点行业 / 特定场景
3. **政策依据层级**：国家级政策 / 监管专项 / 行内战略
4. **产品候选方向**：阳光普惠通用 / 阳光普惠重点客群 / 阳光兴农 / 场景产品
5. **边界提示**：需要进一步核验的信息、不能承诺的事项
6. **联动建议**：是否需要衔接 `product-matching-boundary` 或继续深挖

禁止在输出中：

- 承诺具体产品可办理
- 承诺授信额度、贷款利率
- 承诺审批通过
- 写内部审批口径
- 超出公开政策范围做定性结论

## Quality Gate

- 是否输出了明确的场景判断结论（普惠 / 非普惠 / 待核实）
- 是否区分了"主体资格"和"产品匹配"两个判断层次
- 政策依据是否标注了来源层级
- 是否有明确的边界提示
- 是否避免定价和额度承诺

## Progress Sequence

```
主体识别 → 行业判断 → 规模判断 → 政策匹配 → 产品建议
```

| 步骤 | 内容 | 参考文件 |
|------|------|----------|
| 1. 主体识别 | 判断是企业还是个人/个体工商户 | scenario-identification.md |
| 2. 行业判断 | 制造业/科技/三农/服务/灵活用工等 | scenario-identification.md |
| 3. 规模判断 | 是否符合小微企业划型标准 | scenario-identification.md |
| 4. 政策匹配 | 对应哪类普惠政策支持框架 | policy-boundary.md |
| 5. 产品建议 | 阳光普惠 or 阳光兴农，产品系列方向 | key-products.md |

## Script Hooks

- `scripts/validate-scenario.py`：校验场景判断结论的完整性、承诺风险和边界合规

## 与光大普惠知识包的联动说明

本 skill 依赖以下知识包模块：

- `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`：阳光普惠/阳光兴农产品分类框架
- `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`：具体产品和场景分类（灵工通、安居通等）
- `knowledge.banks.ceb.inclusive-finance.inclusive-finance-scenario-map`："五篇大文章"、百链百户百亿等监管导向

本 skill 专注于"判断是否属于普惠场景"，产品细节和场景产品功能不在本 skill 范围内，由 `product-matching-boundary` 承接后续产品匹配。
