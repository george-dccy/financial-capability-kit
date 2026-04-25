# Inbox — 公共素材摄入层

## 定位

Inbox 是 Financial Capability Kit 的素材入口。它负责接收外部信息（文件、链接、文本片段），经过半自动分类和解读后，蒸馏为仓库中的 knowledge pack 或 skill。

与 `workspace/private/inbox/`（个人私有素材）不同，这里的 inbox 承载**可公开共享的金融行业通用知识源**。

## 目录结构

```
inbox/
├── raw/                          # 待处理的原始素材
│   ├── regulatory/               # 监管政策：央行、金融监管总局、证监会、交易商协会等
│   ├── industry/                 # 行业研究：行业报告、白皮书、宏观经济分析、产业研究
│   ├── products/                 # 产品知识：本行及同业产品手册、方案说明、操作指南
│   ├── markets/                  # 市场动态：市场数据、经济指标、价格变动、行情分析
│   ├── cases/                    # 案例实务：业务案例、项目复盘、实务操作经验
│   ├── professional/             # 专业成长：管理方法、沟通技巧、职业发展、专业认证
│   └── tech-digital/             # 科技与数字化：金融科技、数字化转型、线上化场景
├── processed/                    # 已处理完成的素材（保留原始文件备查）
├── schema/                       # 元数据 schema
│   └── inbox-entry.schema.json   # 单条 inbox 记录的 JSON schema
└── tools/                        # 公共工具脚本
    ├── scan-inbox.py             # Inbox 扫描器：提取文本、初步分类、生成元数据
    └── README.md                 # 工具使用说明
```

## 使用流程

### 1. 投放素材

将素材放入 `raw/` 对应类别的文件夹中。支持三种形式：

| 形式 | 操作 | 示例 |
|------|------|------|
| 本地文件 | 直接复制到对应类别文件夹 | PDF 报告、Excel 数据表、Word 文档 |
| URL 链接 | 创建 `.url.txt` 文件，第一行写 URL | `raw/industry/cicc-report-2026.url.txt` |
| 文本片段 | 创建 `.md` 或 `.txt` 文件，直接写内容 | `raw/regulatory/pbc-notice-20260425.md` |

文件命名建议：`{来源}-{主题}-{日期}.{ext}`，例如 `pbc-利率政策调整-20260425.pdf`。

### 2. 扫描与初步分类

运行扫描器，为每个 raw 文件生成元数据：

```bash
python inbox/tools/scan-inbox.py --category regulatory
python inbox/tools/scan-inbox.py --all
```

扫描器会：
- 提取文件文本（PDF → text, URL → fetch, md/txt → read）
- 运行关键词分类，给出初步信号类型判断
- 在 `processed/` 下生成对应的 `.meta.json` 元数据文件
- 不移动原始文件——人工确认后再整理

### 3. 解读与蒸馏（两种模式）

**模式 A：半自动（用户交互时）**

使用 `prompts/skills/action/inbox-intake.md`：

```
请帮我处理 inbox 中的素材
```

Agent 会：
1. 自动运行扫描器
2. 对每条素材调用 `interpret-financial-signal` 进行解读
3. 给出蒸馏建议（类别、归属）
4. **等待用户确认**后再执行蒸馏

**模式 B：无人值守（agent loop 自动运行）**

使用 `prompts/skills/action/inbox-intake-unattended.md`：

- agent 在每轮循环开始前自动检查 inbox
- 自主判断类别和蒸馏目标，无需用户确认
- 蒸馏结果写入 run report
- agent 在联网搜索中发现有价值的资料时，主动写入 `inbox/raw/` 并在本轮处理

### 4. 蒸馏产出

确认后，素材会被蒸馏为仓库资产：

| 蒸馏目标 | 产出位置 | 示例 |
|----------|----------|------|
| 公共 knowledge pack | `knowledge/{category}/{pack-name}/` | `knowledge/common/regulatory/pbc-rate-policy/` |
| 公共 reference skill | `skills/reference/{skill-name}/` | `skills/reference/regulatory-change-lens/` |
| 公共 action skill | `skills/action/{skill-name}/` | `skills/action/respond-to-policy-change/` |
| 私有 knowledge | `workspace/private/knowledge/` | 个人案例、内部经验 |
| 私有 skill | `workspace/private/skills/` | 个人方法论、话术库 |

### 5. 归档

已蒸馏的素材从 `raw/` 移至 `processed/`，保留原始文件和 `.meta.json` 作为溯源记录。

## 类别说明

| 类别 | 英文 ID | 涵盖内容 | 典型来源 |
|------|---------|----------|----------|
| 监管政策 | regulatory | 央行政策、金融监管总局通知、证监会规则、交易商协会指引、法律法规 | 央行官网、银保监会、证监会、交易商协会 |
| 行业研究 | industry | 行业报告、白皮书、宏观经济分析、产业研究、券商研报 | 券商、咨询公司、行业协会、研究机构 |
| 产品知识 | products | 本行及同业产品手册、方案说明、操作指南、费率表 | 银行官网、产品部门、同业交流 |
| 市场动态 | markets | 利率汇率、经济指标、大宗商品、市场行情、统计数据 | 央行、统计局、Wind、Bloomberg |
| 案例实务 | cases | 业务案例、项目复盘、成功/失败经验、实务操作 | 内部复盘、行业交流、公开案例 |
| 专业成长 | professional | 管理方法、沟通技巧、职业发展、专业认证、读书笔记 | 书籍、课程、行业论坛 |
| 科技数字化 | tech-digital | 金融科技、数字化转型、线上化场景、AI 应用、数据治理 | 科技公司、银行科技部门、行业会议 |

## 与 Private Inbox 的关系

```
public inbox (本目录)              private inbox (workspace/private/inbox/)
├── 可公开共享的行业通用知识         ├── 个人工作文件、客户资料
├── 蒸馏后产出 public 资产          ├── 蒸馏后产出 private 资产
└── 受 contribution 流程约束        └── 遵循 private-first 原则
```

素材可以在两个 inbox 之间流转：
- Private inbox 中去敏感化后的内容，可转入 public inbox 作为贡献候选
- Public inbox 中的内容解读后，个人专属的落地经验可写回 private

## 边界红线

- 不在 inbox 中存放客户敏感信息、内部审批文件、定价细节
- 不自动蒸馏——所有产出需人工确认
- 不编造来源——无法核实的素材在元数据中标记 `source_verified: false`
- 公共素材的蒸馏需走 contribution 流程（去敏感化 → 明确边界 → 补齐来源）
