# 架构说明

`Financial Capability Kit` 是一个面向银行/金融场景的专业知识与方法集合，致力于为金融人的职场助力，甚至可以不断成长为金融人面对客户时的分身。

它采用 `public base + private growth layer` 架构。

## 公开层

公开层是可分享、可贡献、可直接给支持读取仓库的聊天模型和通用 Agent 使用的仓库底座，包含：

- `skills/reference`
- `skills/action`
- `knowledge`
- `prompts`
- `registry`
- `docs`
- `templates`

公开层只沉淀三类内容：

- 专业视角与判断框架
- 任务型行动 skill
- 可公开知识与来源

## 私有层

私有层位于 `workspace/private/*`，默认本地自用，不进 Git。

推荐结构：

```text
workspace/private/
├─ skills/
│  ├─ reference/
│  └─ action/
├─ knowledge/
├─ memories/
├─ case-notes/
└─ registry/
```

私有层用于沉淀：

- 个人经验
- 偏好与输出习惯
- 案例复盘
- 失败教训
- 暂不公开的半成品资产

## 三层资产边界

- `skills/reference`：专业视角、判断框架、表达结构
- `skills/action`：具体任务的输入、步骤、输出、检查点
- `knowledge`：公开、稳定、可引用的知识事实、FAQ、来源

推荐读取顺序：

`question -> reference/action/knowledge -> answer`

如果任务同时需要专业视角和行动方案，可以先读 reference，再读 action。

## 设计原则

- 公开的是专业骨架，不是私人绝活
- private 默认本地生长，不自动公开
- 公共更新不能覆盖 private
- 用户可把 private 内容整理后转成 public contribution
- 仓库优先服务 repo-first 使用方式，而不是页面展示

## 读取约定

Agent 应先读 `registry/*.json`，再按路由读取对应资产正文。  
如果存在 `workspace/private/registry/*.json`，则在 public registry 基础上合并 private 后再路由。
