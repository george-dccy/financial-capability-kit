# Inbox 素材摄入与蒸馏 — 无人值守模式

> 此 prompt 供无人值守 agent loop 自动调用，全流程无需用户确认。

---

请自动处理 inbox 中的待处理素材。

## 与半自动模式的区别

| | 半自动模式 (`inbox-intake.md`) | 无人值守模式（本文件） |
|---|---|---|
| 类别判断 | 用户确认 | agent 自主判断 |
| 蒸馏建议 | 用户确认 | agent 按规则自动执行 |
| 蒸馏执行 | 用户确认后执行 | 自动执行 |
| 适用场景 | 用户交互时 | `fincap loop` / 无人值守循环 |

## 执行步骤

### 1. 扫描 inbox

```bash
python inbox/tools/scan-inbox.py --all
```

如无 scanned 条目，直接结束，不阻塞循环。

### 2. 逐条解读

对每条 scanned 状态的素材：

1. 读取 `.meta.json` 获取元数据
2. 读取 `skills/action/interpret-financial-signal/SKILL.md` 及 references
3. 按 interpret-financial-signal 的执行规则进行解读

### 3. 自主蒸馏判断

解读完成后，按以下规则自动判断（无需用户确认）：

**蒸馏为 knowledge pack 的条件：**
- 内容以事实为主（产品参数、政策条文、行业数据、统计指标）
- 信息相对稳定，不会频繁变化
- 有明确的公开来源可引用
- 仓库中尚无同类 knowledge pack 覆盖

**蒸馏为 reference skill 的条件：**
- 内容以判断框架或方法论为主（如何识别、如何评估、如何应对）
- 可复用于多个场景
- 仓库中尚无同类 reference skill 覆盖

**蒸馏为 action skill 的条件：**
- 内容以执行步骤为主（具体怎么做、先做什么后做什么）
- 有明确的输入输出契约
- 仓库中尚无同类 action skill 覆盖

**不蒸馏的条件（跳过并标记为 archived）：**
- 仓库已有同类内容覆盖
- 信息已过时或价值不足以沉淀
- 来源不可核实（`source_verified: false`）
- 内容涉及客户敏感信息、内部审批、定价细节

**归属判断：**
- 默认 public（可公开共享的行业通用知识）
- 仅当内容涉及个人经验、内部案例、特定机构内部操作时，才归入 private

### 4. 执行蒸馏

按判断结果自动执行：

**Knowledge pack：**
1. 创建 `knowledge/{category}/{pack-name}/` 目录结构
2. 生成 `README.md`、`pack.json`、`modules/`
3. 从 inbox 素材中提取事实内容填充模块
4. 更新 `registry/knowledge.json`

**Reference skill：**
1. 创建 `skills/reference/{skill-name}/` 目录结构
2. 生成 `SKILL.md` 及 references/
3. 更新 `registry/skills.json`

**Action skill：**
1. 创建 `skills/action/{skill-name}/` 目录结构
2. 生成 `SKILL.md` 及 references/
3. 更新 `registry/skills.json`

**Private 蒸馏：**
1. 写入 `workspace/private/knowledge/` 或 `workspace/private/skills/`
2. 更新 `workspace/private/registry/`（如存在）

### 5. 更新 inbox 状态

- 将 `.meta.json` 中 `status` 更新为 `distilled`
- 填写 `distill_target`、`distill_visibility`、`distill_output_path`
- 重建 `inbox/processed/index.json`

### 6. 记录到 run report

将 inbox 处理结果写入本轮 run report：

```markdown
## Inbox 处理记录

- 处理素材数：{N}
- 蒸馏为 knowledge：{列表}
- 蒸馏为 skill：{列表}
- 跳过（原因）：{列表}
- 来源验证：{通过/未通过}
```

## Agent 主动写入 Inbox

在无人值守循环中，agent 在联网搜索或执行任务时发现有价值的公开资料，应主动写入 inbox：

1. 将内容保存为文件，放入 `inbox/raw/{category}/` 对应类别
2. 创建 `.url.txt` 文件记录原始 URL
3. 在本轮后续步骤中通过 scan-inbox.py 扫描并处理

写入规则：
- 只写入与当前任务相关的公开资料
- 只写入有明确来源的内容
- 文件命名：`{来源}-{主题}-{日期}.{ext}`
- 不写入付费墙内容的全文（只保存 URL 和摘要）
- 不写入客户敏感信息

## 边界规则

- 不编造来源——无法核实的内容标记 `source_verified: false` 并跳过蒸馏
- 不在 public 层存放客户敏感信息
- 蒸馏产出遵循仓库现有格式规范
- 单轮最多处理 5 条 inbox 素材，避免单轮改动过大
- 如蒸馏判断不确定，标记为 `needs-review` 而非强行蒸馏
