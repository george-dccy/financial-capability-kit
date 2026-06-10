# Fincap Operating Model

本文件定义 `financial-capability-kit`、`fincap-workspace` 和 `finhot` 的长期分工。

## 一句话

Fincap 是能力，workspace 是个人沉淀，Finhot 是雷达。

## 三仓职责

### financial-capability-kit / fincap

主功能和公开能力底座。

放：

- `skills/reference`：专业视角、判断框架、表达结构
- `skills/action`：任务推进、客户经营、汇报、复盘、方案草拟
- `knowledge`：公开、稳定、可引用的产品知识、基础概念、FAQ 和来源
- `registry`：让 Agent 知道什么时候读什么
- `prompts`：给聊天模型和 Agent 的稳定入口

不放：

- 真实客户数据
- 用户个人不便公开的案例
- 未核验的外部动态
- 临时素材堆积

### fincap-workspace

个人沉淀层。

放：

- 个人资讯和参考材料
- 客户拜访、推进、失败案例和复盘
- 用户偏好、表达习惯、常用话术
- 不便公开的材料和未成熟草稿
- 每周 queue、run report 和试用反馈

默认 private-first。只有去敏感、补来源、补边界后，才整理为 public candidate。

### finhot

公开信号雷达。

放：

- 新政策
- 新产品
- 新项目案例
- 新同业动作
- 企业经营线索
- 同业交易银行产品集合、新产品和特色产品公开入口
- 公开来源、摘要、标签、推荐理由、业务领域、价值标签

不放：

- Fincap 稳定 knowledge 的副本
- 完整产品百科
- 同业产品静态知识库副本
- 个人私有资料
- 重型 CMS
- 长期方法论沉淀

## 流转规则

```text
Finhot 发现动态或公开产品入口
-> Fincap 主路由判断场景
-> Fincap 解读和组织行动
-> workspace 记录个人经验
-> 稳定后再回流 Fincap public candidate
```

## 判断表

| 内容 | 放哪里 | 说明 |
|---|---|---|
| 新监管政策链接 | Finhot | 先作为动态线索，保留来源 |
| 对政策的解读框架 | Fincap skill | 稳定方法进入 `skills/action` 或 `skills/reference` |
| 某客户受政策影响的复盘 | workspace | 含个人和客户上下文，默认 private |
| 银行基础产品说明 | Fincap knowledge | 需要公开来源和边界 |
| 同业产品集合或新产品公开入口 | Finhot | 保留来源链接，供人点击、Agent 继续读取 |
| 同业产品比较、解读方法和客户经营启发 | Fincap skill | 不复制产品库，只沉淀可复用判断框架、边界和表达模板 |
| 个人常用汇报话术 | workspace | 稳定后可去敏感转 public candidate |

## 开发约束

- Finhot 新功能默认只服务发现、筛选、审核、分发信号。
- Fincap 新能力默认服务用户能不能更专业地判断、表达、推进。
- Workspace 新内容默认服务用户长期个性化和隐私。
- 如果一个功能同时想服务三件事，先拆开，不要做成一个巨型模块。

## 本周试用优先级

1. 让同事能问金融工作问题，并得到可直接用的答案。
2. 让最新动态先走 Finhot，再由 Fincap 解读。
3. 让个人经验和反馈有 workspace 承接位置。
4. 不扩 Finhot 大功能，只修雷达质量和 API 稳定性。
