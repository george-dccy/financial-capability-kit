# Inbox 素材摄入与蒸馏 Prompt

> 将此 prompt 粘贴到对话中，引导 agent 处理 inbox 中的待处理素材。

---

请帮我处理 inbox 中的待处理素材。

## 执行步骤

### 1. 扫描 inbox 并检查状态

**先运行扫描器**，处理 `inbox/raw/` 下所有新增素材：

```bash
python inbox/tools/scan-inbox.py --all
```

扫描器会自动跳过已生成过 meta 的文件，只为新增素材生成 `inbox/processed/*.meta.json`。

然后读取 `inbox/processed/` 下所有 `.meta.json` 文件，找出 `status` 为 `scanned` 的条目。

如果没有任何 scanned 状态的条目，告知用户"inbox 中没有待处理的素材"并结束。

### 2. 逐条解读

对每条 scanned 状态的素材：

1. 读取其 `.meta.json` 获取元数据（类别、信号类型、文本预览）
2. 读取 `skills/action/interpret-financial-signal/SKILL.md` 及其 4 个 references
3. 运行 `python inbox/tools/scan-inbox.py --text "{text_preview}"` 确认信号分类
4. 按 interpret-financial-signal 的执行规则进行解读，产出：
   - 一句话结论
   - 信号类型与相关性判断
   - 对银行/金融工作的影响路径
   - 可落地参考方向

### 3. 蒸馏建议（关键步骤 — 需要用户确认）

解读完成后，对每条素材给出蒸馏建议：

```
## 蒸馏建议

素材：{filename}
类别：{category}
信号类型：{signal_type}

**建议蒸馏为：**
- [ ] Knowledge pack — 事实性内容（产品参数、政策条文、行业数据）
- [ ] Reference skill — 判断框架（如何识别/评估某类信号）
- [ ] Action skill — 执行方法（如何应对此类信号）
- [ ] 不蒸馏 — 信息已过时 / 仓库已覆盖 / 价值不足以沉淀

**建议归属：**
- [ ] Public（可公开共享的行业通用知识）
- [ ] Private（个人专属经验/案例）

**理由：**{简述为什么建议这个分类}

请确认或调整。
```

### 4. 等待用户确认

**必须等待用户明确回复后才能继续。** 用户可能：
- 确认建议 → 执行蒸馏
- 调整分类/归属 → 按用户选择执行
- 跳过某条 → 标记为 archived
- 全部跳过 → 结束

### 5. 执行蒸馏

用户确认后，根据选择执行：

**Knowledge pack 蒸馏：**
1. 创建 `knowledge/{category}/{pack-name}/` 目录结构
2. 生成 `README.md`、`pack.json`、`modules/` 下的内容模块
3. 按 inbox 素材内容填充，遵循 knowledge pack 格式规范
4. 更新 `registry/knowledge.json` 添加新条目

**Reference skill 蒸馏：**
1. 创建 `skills/reference/{skill-name}/` 目录结构
2. 生成 `SKILL.md`（参考 `templates/` 中的模板）
3. 填充框架、反模式、示例
4. 更新 `registry/skills.json`

**Action skill 蒸馏：**
1. 创建 `skills/action/{skill-name}/` 目录结构
2. 生成 `SKILL.md` 及 references/
3. 定义输入输出契约、执行步骤、质量门槛
4. 更新 `registry/skills.json`

**Private 蒸馏：**
1. 写入 `workspace/private/knowledge/` 或 `workspace/private/skills/`
2. 更新 `workspace/private/registry/`（如存在）

### 6. 更新 inbox 状态

蒸馏完成后：
- 将素材的 `.meta.json` 中 `status` 更新为 `distilled`
- 填写 `distill_target`、`distill_visibility`、`distill_output_path`
- 重建 `inbox/processed/index.json`

### 7. 汇报结果

输出处理摘要：

```
## Inbox 处理完成

已处理：{N} 条
已蒸馏：{N} 条
已跳过：{N} 条

### 蒸馏产出
- {产出路径1}: {简述}
- {产出路径2}: {简述}

### 待跟进
- {如有需要进一步完善的条目，列出}
```

## 边界规则

- 不自动执行蒸馏——每一步都需要用户确认
- 不编造素材来源——无法核实的内容标记 `source_verified: false`
- 不在 public 层存放客户敏感信息
- 蒸馏产出遵循仓库现有的格式规范（knowledge pack 格式、SKILL.md 格式）
- 单次处理建议不超过 5 条素材，避免信息过载
