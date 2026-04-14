# Prompts Usage

## 推荐入口

当前仓库优先推荐豆包专项入口：

- `prompts/entrypoints/doubao/public-consulting.md`
- `prompts/entrypoints/doubao/bank-staff.md`
- `prompts/entrypoints/doubao/frontline-manager.md`
- `prompts/entrypoints/doubao/head-office-leadership.md`
- `prompts/entrypoints/doubao/auto.md`

这些入口会要求模型：

1. 先读取 `registry/*.json`
2. 回答前先列出准备读取的文件路径
3. 显式说明调用了哪些 `skills / methods / knowledge packs`
4. 把“方法/判断依据”和“公开知识依据”分层表达
5. 在覆盖不足时明确写出“当前仓库未覆盖”

## 兼容入口

以下入口仍然保留，适合已有使用习惯：

- `prompts/entrypoints/ceb-customer-consulting.md`
- `prompts/entrypoints/auto.md`

## 专项 Prompt

当你明确只做某一类任务时，再使用：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
