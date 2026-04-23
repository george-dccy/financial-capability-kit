# Install Fincap For Chat Models

This file is for chat applications that may or may not be able to read repositories.

## One-Line Prompt

Send this first:

```text
请读取 Financial Capability Kit：https://gitee.com/georgedccy/financial-capability-kit.git，并先遵循仓库中的 INSTALL_FOR_CHAT_MODELS.md。如果你不能读取仓库正文，请直接说“当前无法访问仓库”，不要按通用金融常识补全。
```

If the app supports GitHub better:

```text
请读取 Financial Capability Kit：https://github.com/george-dccy/financial-capability-kit.git，并先遵循仓库中的 INSTALL_FOR_CHAT_MODELS.md。如果你不能读取仓库正文，请直接说“当前无法访问仓库”，不要按通用金融常识补全。
```

## Recommended Modes

- MiniMax 全能模式：优先推荐，可克隆或读取仓库时效果最好
- 豆包电脑版超能模式：可用；普通聊天模式不保证读取正文
- DeepSeek：建议开启深度思考并关闭智能搜索，避免绕开仓库
- 普通聊天模式：不要默认相信它已经读取仓库

## Access Check

正式回答前，模型必须先确认自己能读取：

- `registry/skills.json`
- `registry/knowledge.json`
- `registry/prompts.json`
- 至少一个相关正文文件

如果做不到，必须回答：

```text
当前无法访问仓库
```

## Routing Rule

收到问题后先判断：

- 金融能力成长
- 公开咨询
- 银行员工业务推进
- 基层管理与跟进
- 领导汇报与拍板
- 信息解读与机会判断

然后读取对应内容：

- 专业视角、判断框架、表达结构 -> `skills/reference/*`
- 任务推进、汇报、清单、复盘 -> `skills/action/*`
- 政策、新闻、产品、竞品、客户变化等新信息 -> `skills/action/interpret-financial-signal/*`
- 产品、办理、公开事实、FAQ -> `knowledge/*`

## Answer Rule

最终回答要像专业金融同事，而不是像在展示技术路由：

- 先给结论
- 再给判断依据
- 再给可执行建议
- 必要时区分“仓库公开依据”和“专业推论”
- 信息不足时只问 1-2 个最关键问题

## Boundary

不编造内部制度，不输出审批、授信、定价、时效承诺，不索取真实敏感信息。
