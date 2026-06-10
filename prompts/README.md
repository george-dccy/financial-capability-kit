# Prompts Usage

## 主入口

这些入口共同服务于同一个仓库定位：

`面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力，甚至可以不断成长为金融人面对客户时的分身`

## 使用前提

不是所有聊天类大模型应用都能真正读取仓库内容。

基于 2026-06-10 的当前实测：

- `MiniMax 全能模式`：当前优先推荐，可克隆仓库并读取内容
- `豆包电脑版超能模式`：可读取仓库；普通聊天模式不保证生效
- `DeepSeek`：建议 `深度思考 + 关闭智能搜索`
- `千问等普通聊天模式`：容易绕开仓库自由回答，不建议作为主入口
- `本地 Agent / 可读本地仓库的 Agent`：通常最稳定

详细见：

- [模型与模式兼容性说明](../docs/prompts/model-compatibility.md)

当前仓库优先推荐这些入口：

- `prompts/entrypoints/chat/financial-capability.md`
- `prompts/entrypoints/chat/public-consulting.md`
- `prompts/entrypoints/chat/bank-staff.md`
- `prompts/entrypoints/chat/frontline-manager.md`
- `prompts/entrypoints/chat/head-office-leadership.md`
- `prompts/entrypoints/chat/auto.md`
- `prompts/entrypoints/agent/general.md`

这些聊天模型入口统一使用当前仓库地址：

`https://gitee.com/georgedccy/financial-capability-kit.git`

共同约定：

1. 先读取 `README.md`、`docs/capability-map.md`、`skills/action/fincap-router/SKILL.md`
2. 再读取 `registry/skills.json`、`registry/knowledge.json`、`registry/prompts.json`
3. 先判断问题属于客户经营、客户资料研判、动态信号、产品与方案边界、汇报与拍板、跟进复盘，还是能力成长与沉淀
4. 再判断更需要 `skills/reference`、`skills/action`、`skills/action/query-finhot` 还是 `knowledge`
5. 这套仓库约束适用于整个对话，不只第一轮
6. 默认优先使用仓库和 Finhot，不要拿外部搜索替代仓库
7. 对用户呈现时，优先直接给结论、判断或可执行结果
8. 每个入口末尾都保留问题占位，方便直接复制使用
9. 覆盖不足时明确写出“当前仓库未覆盖”

Finhot 是 Fincap 的公开信号雷达：

- 生产地址：`https://finhot.boluomi.ren`
- 最新动态、同业动作、政策变化、同业产品集合、新产品、产品案例和经营线索，优先使用 `skills/action/query-finhot`
- Fincap 仓库继续负责稳定知识、产品地图、判断框架、执行流程、边界规则和 prompt
- Finhot 的 `dynamic` 是来源线索，`product/detail` 是公开同业产品入口或特色产品信号，人工校准信号只是解读上下文；稳定框架留在 Fincap，个性化产品笔记进 workspace

推荐读取顺序：

`README -> capability-map -> fincap-router -> registry -> Finhot if latest signal needed -> reference/action/knowledge -> answer -> private distill if valuable`

其中：

- 支持仓库读取的聊天模型入口，重点是“多轮持续用仓库，外部自然表达”
- Agent 入口，重点是“整场会话持续以仓库为底座，先解题，再沉淀资产”

## 专项 Prompt

当你明确只做某一类任务时，再使用更短的专项 prompt：

- `prompts/skills/reference/*`
- `prompts/skills/action/*`
- `prompts/knowledge/*`
