# Prompts Usage

## 主入口

当前仓库优先推荐豆包专项入口：

- `prompts/entrypoints/doubao/public-consulting.md`
- `prompts/entrypoints/doubao/bank-staff.md`
- `prompts/entrypoints/doubao/frontline-manager.md`
- `prompts/entrypoints/doubao/head-office-leadership.md`
- `prompts/entrypoints/doubao/auto.md`

这些入口已经统一使用以下仓库地址：

`https://gitee.com/georgedccy/awesome-banker-skills.git`

共同约定：

1. 先读取 `registry/*.json`
2. 先识别身份或岗位，如有对应 `role skill` 就一并读取
3. 再识别场景，选择对应 workflow
4. 回答前先列出准备读取的文件路径
5. 显式写出调用了哪些 `role skill / workflow skill / method / pack`
6. 把“方法/判断依据”和“公开知识依据”分开
7. 覆盖不足时明确写出“当前仓库未覆盖”

推荐读取顺序：

`scene -> workflow -> method -> knowledge pack`

如果身份明确，也可以同时读取对应 `role skill`。

## 专项 Prompt

当你明确只做某一类任务时，再使用更短的专项 prompt：

- `prompts/roles/*`
- `prompts/workflows/*`
- `prompts/knowledge-packs/*`
