# 豆包入口说明

## 为什么单独做豆包入口

这个仓库重点适配豆包的使用方式。  
目标不是给出一个很长的万能 prompt，而是提供几张“可直接复制、角色清楚、约束明确”的入口卡片。

## 入口列表

### 1. 公开咨询入口

- 文件：`prompts/entrypoints/doubao/public-consulting.md`
- 适合：客户、公开咨询用户、非专业用户
- 特点：优先读公开 knowledge packs，回答简单、保守、可理解

### 2. 银行员工入口

- 文件：`prompts/entrypoints/doubao/bank-staff.md`
- 适合：客户经理、产品协同、业务支持人员
- 特点：先识别岗位，如有对应 role skill 就一并读取，再进入 workflow，并补 methods 与 packs

### 3. 基层管理者入口

- 文件：`prompts/entrypoints/doubao/frontline-manager.md`
- 适合：团队负责人、支行长、基层管理者
- 特点：先叠加管理者角色视角，再强调拆任务、盯进度、做闭环、形成汇报口径

### 4. 总行领导层入口

- 文件：`prompts/entrypoints/doubao/head-office-leadership.md`
- 适合：总行或分行中高层
- 特点：先叠加领导层角色视角，再强调判断、关键事实、风险、取舍、拍板项

### 5. 自动路由入口

- 文件：`prompts/entrypoints/doubao/auto.md`
- 适合：不确定该用哪个入口时
- 特点：先识别使用者身份，再切到对应逻辑

## 统一要求

所有豆包入口都要求模型：

- 先读取 `registry/*.json`
- 先识别身份或岗位，如有对应 role skill 就一并读取
- 回答前先列出准备读取的文件路径
- 显式写出调用了哪些 `role skill / workflow skill / method / pack`
- 把“方法/判断依据”和“公开知识依据”分开
- 覆盖不足时明确写出“当前仓库未覆盖”

## 使用建议

- 如果你已经知道自己的身份，优先用对应入口
- 如果你只想先试一试，用 `auto.md`
- 如果你需要把 private overlay 也算进去，建议在本地 Agent 环境中再叠加 `workspace/private/registry/*`
