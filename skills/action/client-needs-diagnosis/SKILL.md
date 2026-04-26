---
name: skill.action.client-needs-diagnosis
description: Use when you need to systematically determine what type of financial solution a corporate client most likely needs, before proposing products or during client conversation.
license: MIT
compatibility:
  agents: [openclaw, claude-code, codex]
metadata:
  skill_type: action
  capability: analyze
  display_name_zh: 客户需求诊断
  audience: [bank-practitioner]
  related_skills:
    - skill.reference.problem-opportunity-framework
    - skill.reference.corporate-client-coverage-lens
    - skill.action.market-corporate-client
    - skill.action.product-matching-boundary
  related_knowledge:
    - knowledge.banks.ceb.corporate-settlement.basic-settlement
    - knowledge.banks.ceb.transaction-banking.yangguang-e-pay
    - knowledge.banks.ceb.trade-finance.yangguang-electricity-certificate
    - knowledge.banks.ceb.transaction-banking.yangguang-supply-chain
    - knowledge.banks.ceb.inclusive-finance.scenario-map
    - knowledge.common.sales.consultative-b2b
    - knowledge.common.economics.business-basics
  related_prompts: []
  references_dir: references
  scripts_dir: scripts
---

# 客户需求诊断 Skill

## Scope

这是一个 action skill。
它聚焦"需求诊断"，负责在营销前或沟通中系统判断客户当前更可能需要哪类金融方案。

与 `skill.action.market-corporate-client` 的边界：

- `market-corporate-client`：首访完整包，含开场、诊断、切入口选择和会后动作规划
- `client-needs-diagnosis`：纯诊断，专注判断客户需要什么类型的产品/服务，输出直接进 `product-matching-boundary`

简单说：`market-corporate-client` 告诉你"怎么开场聊"，`client-needs-diagnosis` 告诉你"他可能需要什么"。

## When To Use

- 拜访前，想先判断客户最可能的金融需求方向
- 沟通中，客户表达了不满或提到某个业务动作，想判断这背后对应哪类金融需求
- 会后，想把听到的信息归类到一个明确的需求类型
- 需要给 `product-matching-boundary` 提供明确的"需求定型结论"时

## Required Reads

1. `references/diagnosis-framework.md`
2. `references/need-type-matrix.md`
3. `references/knowledge-routing.md`
4. `skill.reference.problem-opportunity-framework`
5. `skill.reference.corporate-client-coverage-lens`

## Execution Rule

1. 先用 `references/diagnosis-framework.md` 梳理已知信号
2. 再用 `references/need-type-matrix.md` 对齐需求类型
3. 然后按 `references/knowledge-routing.md` 调用相关 knowledge 包补充背景
4. 最后输出需求类型结论和置信度

## Input Contract

最低输入：

- 客户基本情况（行业、企业规模、主营业务至少有一项）
- 已知信号（客户提及的业务动作、痛点、不满、变化至少一项）

可选补充：

- 企业经营状态（扩张/收缩/稳定）
- 历史合作情况摘要
- 客户归属（公司/零售/普惠/同业）

## Output Contract

必须包含：

1. **需求类型判断**：最可能的金融需求类型（一级分类 + 二级细分）
2. **信号依据**：支撑判断的关键信号
3. **置信度评估**：高 / 中 / 低，附原因
4. **待验证项**：还需要通过沟通或资料核验的信息
5. **建议下一步**：进入 `product-matching-boundary` 还是继续 `market-corporate-client`

禁止在输出中：

- 承诺具体产品可办理
- 承诺授信、定价、额度
- 写客户敏感信息
- 写内部审批口径

## Quality Gate

- 是否输出了明确的一级需求类型
- 是否区分了"主需求"和"次需求"
- 置信度是否有依据支撑
- 待验证项是否影响主判断
- 是否避免直接跳到产品结论

## Boundary With Market Corporate Client

| 维度 | market-corporate-client | client-needs-diagnosis |
|------|------------------------|------------------------|
| 核心逻辑 | 首访完整包：开场 + 诊断 + 切入口 + 规划 | 纯诊断：判断需要什么类型的产品/服务 |
| 输出阶段 | 场景判断 + 切入口 + 会谈目标 + 会后动作 | 需求类型 + 信号依据 + 置信度 + 待验证 |
| 适用场景 | 首次拜访准备 | 拜访前判断 / 沟通中归类 / 会后沉淀 |
| 协同视角 | 开场节奏优先 | 判断结论优先 |
| 后续衔接 | 衔接首次会谈 | 衔接 product-matching-boundary |

两者关系：`market-corporate-client` 的输出包含 `client-needs-diagnosis` 的结论，但 `client-needs-diagnosis` 可独立使用，专门用于需求归类。

## Script Hooks

- `scripts/validate-diagnosis.py`：校验诊断结论完整性、承诺风险和边界合规
