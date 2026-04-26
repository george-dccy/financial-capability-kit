# 相关资产

## 相关 Skills

### `skill.action.market-corporate-client`

- **关系**：同属对公客户拜访 Skill 体系
- **本 skill 定位**：开场判断框架（why/when/which）
- **market-corporate-client 定位**：完整场景编排，包含 opening-playbook
- **使用顺序**：先读本 skill 做判断，再按需调 market-corporate-client 做执行

### `skill.reference.problem-opportunity-framework`

- **关系**：开场找到客户痛点后，用 problem-opportunity-framework 进一步诊断
- **使用顺序**：开场判断 → 第一个问题 → 问题深化时调用

### `skill.reference.client-advance-framework`

- **关系**：开场和提问完成后，用 client-advance-framework 锁定下一步
- **使用顺序**：开场 → 问题探索 → client-advance 推进成明确动作

## 相关 Knowledge

### `knowledge.common.sales.consultative-b2b`

- **关系**：本 skill 的 SPIN 框架改编自顾问式销售公开方法论
- **本 skill 与其的边界**：consultative-b2b 是通用 2B 销售框架，本 skill 是银行对公场景改编版

### `knowledge.common.sales.consultative-b2b/modules/discovery-questions.md`

- **关系**：discovery-questions 中的"现状/困难/影响/目标"四问是本 skill 提问策略的知识基础
- **本 skill 与其的边界**：discovery-questions 写"问什么"，本 skill 写"何时问、问哪个、怎么判断"

## 与 opening-playbook 的边界（重点）

`skill.action.market-corporate-client/references/opening-playbook.md` 是本 skill 最需要明确区分的资产。

| 维度 | 本 skill | opening-playbook |
|------|---------|-----------------|
| 资产类型 | reference skill | action skill 的 reference 子文件 |
| 回答问题 | 开场用什么策略、为什么 | 开场具体说什么话 |
| 输出形式 | 策略选择、提问方向、状态评估标准 | 话术模板、会谈节奏示例 |
| 使用场景 | 拜访前准备、拜访后复盘 | 拜访现场执行 |
| 银行针对性 | 强（信任矩阵、SPIN改编） | 中（通用银行场景话术） |

**联动规则**：
1. 拜访准备阶段：先读本 skill 判断策略，再按需看 opening-playbook 的节奏参考
2. 拜访执行阶段：现场以 opening-playbook 的话术为主，本 skill 作为判断备用
3. 拜访复盘阶段：用本 skill 的框架评估开场是否正确，判断是否需要调整策略

## 来源说明

本 skill 的框架来源：

- **SPIN Selling**：Neil Rackham 的公开顾问式销售方法论（1988）
- **MEDDIC**：配电自动化行业的公开销售框架，用于理解客户决策链
- **银行对公实践**：银行公开培训材料中的提问技巧，经本 skill 改编
- **本仓库已有知识**：discovery-questions.md 的四问结构被本 skill 重构为银行场景版本
