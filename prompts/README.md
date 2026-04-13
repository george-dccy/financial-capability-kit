# Prompts Usage

## 推荐入口（给豆包/千问/通用模型）

优先使用：

- `prompts/entrypoints/auto.md`

这个入口会让模型自动：

1. 读取 `registry/*.json`
2. 选择最匹配的 `skills/*`
3. 关联并读取对应 `knowledge-packs/*`
4. 输出路由决策 + 结论 + 依据 + 下一步 + 边界

## 专项 Prompt

当你明确只做某一类任务时，再使用：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
