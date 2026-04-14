# 架构说明

`awesome-banker-skills` 采用 `public base + private overlay` 架构。

## 公开层

公开层是可分享、可贡献、可直接给豆包和通用 Agent 使用的仓库底座，包含：

- `skills/roles`
- `skills/workflows`
- `knowledge-packs/banks`
- `knowledge-packs/common`
- `methods`
- `prompts`
- `registry`
- `docs`
- `templates`

公开层只沉淀三类内容：

- 共识技能
- 可公开知识
- 可复用方法论

## 私有层

私有层位于 `workspace/private/*`，默认本地自用，不进 Git。

推荐结构：

```text
workspace/private/
├─ skills/
├─ knowledge-packs/
├─ methods/
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

## 四层资产边界

- `skills/roles`：岗位 skill，沉淀岗位常见判断、关注重点和沟通方式
- `skills/workflows`：workflow skill，沉淀具体场景下的步骤、输出和推进方式
- `knowledge-packs`：公开、稳定、可引用的知识事实
- `methods`：跨岗位、跨流程复用的判断与推进框架

这三层必须保持分离，不互相混写。

推荐读取顺序：

`scene -> workflow -> method -> knowledge pack`

如果身份明确，也可以同时读取对应 `role skill`。

## 设计原则

- 公开的是共识，不是私人绝活
- 私有内容默认本地生长，不自动公开
- 公共更新不能覆盖 private
- 用户可把 private 内容整理后转成 public contribution
- 仓库优先服务 repo-first 使用方式，而不是前端

## 读取约定

Agent 应先读 `registry/*.json`，再按路由读取对应资产正文。  
如果存在 `workspace/private/registry/*.json`，则在 public registry 基础上合并 private overlay 后再路由。
