---
name: market-corporate-client
description: 面向对公客户营销场景，帮助在接触客户前识别业务机会、设计切入口和安排下一步动作。适用于客户拜访前、电话沟通前、方案切题前。
license: MIT
metadata:
  banker_kind: workflow
  display_name_zh: 对公客户营销
  related_packs: pack.banks.ceb.public-basics
  related_prompts: prompt.workflow.market-corporate-client
---

# 对公客户营销 Skill

## 能力定位

这个 workflow 用于营销前准备，目标是把“找客户聊一聊”变成“带着切入口、有判断、有下一步地去推进”。

## 适用时机

- 拜访客户前
- 电话沟通前
- 准备营销话术时
- 不确定先从哪个产品或需求切入时

## 推荐输入

- 客户所属行业与企业类型
- 当前公开可见的经营特征
- 你掌握到的初步需求
- 是否已有合作基础
- 本次沟通的预期目标

## 输出框架

1. `客户场景初判`
2. `可切入的话题`
3. `为什么这个切入口合理`
4. `本次沟通目标`
5. `不该急着谈什么`
6. `沟通后下一步动作`

## 工作原则

- 先谈客户经营动作，不急着谈产品名词
- 先争取下一步，不追求一次讲完
- 先看交易、结算、资金流，再看更复杂的结构化方案
- 如需机构公开事实，单独读取相关 knowledge pack，不在 workflow 内硬编码

## 常见失误

- 一上来推产品
- 没搞清楚客户真实经营动作
- 没有为下一次沟通埋点
- 把公开产品信息说成审批承诺