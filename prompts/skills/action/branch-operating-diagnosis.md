---
id: prompt.skill.action.branch-operating-diagnosis
kind: skill
display_name_zh: 经营分析 Prompt
target_skill: skill.action.branch-operating-diagnosis
summary: 通过对话补充经营目标、关键数据和自我评价，输出结构化经营分析初判。
relations:
  - skill.reference.branch-operating-diagnosis-lens
  - skill.action.report-decision-brief
  - skill.action.interpret-financial-signal
---

请按“经营分析”方式处理我接下来提供的信息。

目标不是生成正式经营考核结论，而是先形成一版轻量、结构化、可继续补数的经营分析初判。

请按以下顺序工作：

1. 先判断输入是否足够，缺关键数据时先列待补数
2. 先看结果，再看结构，再做初步归因
3. 输出时固定包含：
   - 当前初判
   - 做得好的地方
   - 做得不好的地方
   - 主要判断依据
   - 初步归因
   - 还需补充的信息
   - 边界提示

要求：

1. 区分事实、初步判断和待确认项。
2. 如果目标、对比口径或关键指标不足，写明待补数，不要硬下完整结论。
3. 不冒充内部经营系统或正式经营考核。
4. 如涉及最新政策、同业或区域变化，应提醒可继续联动信息解读能力。
