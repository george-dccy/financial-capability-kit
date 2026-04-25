# Public / Private Overlay

## 目标

让公开仓库持续更新，同时不破坏本地私有资产。

## 读取顺序

Agent 统一按以下顺序读取：

1. `registry/skills.json`
2. `registry/knowledge.json`
3. `registry/prompts.json`
4. 如果存在，再读取：
   - `workspace/private/registry/skills.json`
   - `workspace/private/registry/knowledge.json`
   - `workspace/private/registry/prompts.json`
5. 合并索引后，再按路由读取具体正文

## 合并规则

- 新 id：直接追加
- 同 id：private 元数据优先
- 正文路径：如果 private 覆盖存在，优先读取 private path
- 增量扩展：可使用 `extends` 或 `base_id` 指向 public base

目标是补丁式增强，不是整包重写。

## 自进化规则

任何”学到的新偏好、新案例、新经验”都要先走 private：

1. 先写入 `workspace/private/memories/` 或 patch proposal
2. 给用户看候选变更摘要
3. 经用户确认后，再更新 private 资产
4. 如用户愿意公开，再整理成 public contribution candidate

公共素材的摄入可通过 `inbox/` 进入：

1. 用户将文件/链接/文本放入 `inbox/raw/{category}/`
2. 运行 `python inbox/tools/scan-inbox.py` 生成初步分类元数据
3. 使用 `prompts/skills/action/inbox-intake.md` 引导 agent 逐条解读
4. 经用户确认后，蒸馏为 public knowledge pack 或 skill
5. 私有 inbox（`workspace/private/inbox/`）中的去敏感化内容可转入 public inbox

如果内容已经不只是提醒，而是可稳定复用的专业视角、行动套路或知识专题，应优先整理成：

- `workspace/private/skills/reference`
- `workspace/private/skills/action`
- `workspace/private/knowledge`

不要长期只停留在零散 memory 中。

严禁无审查自动覆写 public 资产。

## public contribution 流程

推荐走三段式：

1. `private draft`
2. `public candidate`
3. `merge to public`

整理为公开候选时，至少要完成：

- 去敏感化
- 明确边界
- 补齐来源
- 生成变更摘要

## 对未来行内落地的意义

这个 overlay 结构为后续更强的私有化落地预留了清晰扩展点：

- public registry 可替换为机构内部 registry
- private growth layer 可映射为个人或部门工作区
- repo-first prompt 逻辑可以延续到更封闭的 Agent 环境
- 当前版本先保留结构，不实现具体内网接口
