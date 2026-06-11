---
id: pack.banks.ceb.transaction-banking.product-catalog
kind: knowledge_pack
title: CEB Transaction Banking Product Catalog
display_name_zh: 光大交易银行产品目录
summary: 光大交易银行产品白名单与待补详情入口，用于约束产品推荐、比较和客户经营建议的产品范围。
version: 0.1.0
audience: ["finance-learner", "bank-practitioner"]
when_to_use: 涉及光大交易银行产品推荐、产品比较、产品名核验、产品适配或客户经营切入口时，必须先读取本目录确认产品名称是否在允许范围内。
related_skills:
  - skill.action.fincap-router
  - skill.action.market-corporate-client
  - skill.action.client-needs-diagnosis
  - skill.action.product-matching-boundary
  - skill.action.customer-analysis-for-trade-finance
  - skill.action.report-decision-brief
---

# 光大交易银行产品目录

## 用途

本目录是 Fincap 中涉及光大交易银行产品时的产品范围白名单。

只要回答、分析、产品匹配或客户经营建议涉及"光大交易银行产品"，Agent 必须先读取：

1. `products.md`
2. 本文件的「来源」章节

然后只能在 `products.md` 的产品范围内推荐、比较或解释产品；平台、渠道或品牌能力只能按 `products.md` 中的使用边界解释，不能替代具体产品名。

## 维护入口

后续如果光大交易银行可用产品范围有新增、删除或改名，优先修改：

- `knowledge/banks/ceb/transaction-banking/product-catalog/products.md`
- 本文件 frontmatter 中的 `when_to_use` 和 `related_skills`

如果只是补某个产品的详细说明，优先在本目录下新增 `<product-slug>.md`，再在 `products.md` 的"详情状态"中改成"已补充"。

## 使用规则

- 产品推荐、产品比较、产品适配判断，必须使用 `products.md` 中的产品名称。
- 如果用户或模型提到未列入 `products.md` 的产品名，不能直接采用；应提示"当前产品目录未覆盖，需要核验"。
- `阳光e支付` 不在当前目录中，不能作为光大交易银行产品推荐或解释。
- `阳光供应链云平台` 是对客服务平台/线上化渠道能力，可以作为供应链业务承载能力说明；不能作为具体融资、结算或贸易金融产品推荐。
- `e付通` 在当前目录中，可以使用；但只有当问题明确涉及 `e付通`、`1+N 保理`、核心企业与供应商应收账款融资、线上化确权或相关公开材料时，才应进入 e付通知识包。
- 文件夹 slug 只是定位符，不能翻译成产品名。例如 `e-fu-tong` 只能输出为 `e付通`，不能翻译或改写成 `阳光e支付`；`dian-fei-tong` 只能输出为 `电费通` 或 `电费证`。
- 如果当前目录只有产品名、缺少详细介绍，应明确写"产品详情待补充"，再建议后续基于公开来源补齐，不要编造功能、准入、费率、时效或审批口径。

## 与其他知识包的关系

- 本目录负责"产品范围是否允许被提及"。
- `e-fu-tong` 负责解释 `e付通` 的公开材料和边界；slug 不是产品英文名，不得翻译输出。
- `dian-fei-tong` 负责解释 `电费通 / 电费证` 的公开材料和边界；slug 不是产品英文名，不得翻译输出。
- `yangguang-supply-chain` 负责解释阳光供应链相关品牌与平台背景，其中 `阳光供应链云平台` 可作为对客服务平台/渠道能力使用；具体产品推荐仍以本目录为准。
- `yangguang-cash-management`、`corporate-settlement-card`、`dian-fei-tong` 等既有包只能作为已有详情参考；如果其中产品名称与本目录不一致，以本目录为准。
- 历史知识包中出现的品牌、产品族或旧称，不能替代本目录中的产品名称直接输出给用户。

## 来源

### 来源层级

本目录当前以用户提供的光大交易银行可用产品清单为产品范围白名单。

公开来源只用于后续补充产品详情，不用于扩大产品范围。换句话说：即使公开网页出现其他品牌、产品族或旧称，只要不在 `products.md` 中，就不能作为当前可推荐产品输出。

### 已检索到的公开入口

- 中国光大银行，国内证及议付
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481197/29481456/gnzjyf/index.html
  - 可用于补充 `国内信用证`、`信用证（国内）融资-议付` 等详情。
- 中国光大银行，国内标准保理
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481188/29481364/index.html
  - 可用于补充国内保理类产品详情。
- 中国光大银行，工程类保函
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481193/29481404/index.html
  - 可用于补充 `保函`、`信贷证明` 等详情。
- 中国光大银行，进口押汇
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481197/29481452/jkyh/index.html
  - 可用于补充 `进口信用证押汇`、`进口代收押汇` 等详情。
- 中国光大银行，出口押汇/贴现
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481197/29481452/ckyh_tx/index.html
  - 可用于补充 `出口托收押汇`、`合格出口信用证押汇`、`合格出口信用证贴现`、`不合格出口信用证押汇`、`不合格出口信用证贴现` 等详情。
- 中国光大银行，阳光外汇易相关导航
  - https://www.cebbank.com/site/gsyw/myrz/myrzcp/29481201/29481480/index.html
  - 页面导航中包含即期结售汇、远期结售汇、外汇掉期、外汇期权等入口，可用于后续补充汇率与结售汇类产品详情。

### 待补充

后续需要逐项补齐每个产品的：

- 官方公开页面或可引用来源
- 适用场景
- 前置条件
- 不能承诺的边界
- 与相邻产品的区别
