# R223P-4 sample N regression: 有趣的纸印

source_stage: R223N-P3-P1  
sample_focus: 材料技法 / 印痕探究 / 材料实验  
regression_result: PASS

## unit intensity router

```text
unit_phase_role = technique_preparation
lesson_position_in_unit = middle
practice_intensity = medium
student_work_time_ratio = medium
teacher_support_density = normal
```

该样本不是高密度整课创作课，而是材料和印痕的探究课。实践密度适中：学生需要观察、改造、试印和完成小幅作品，但核心证据是纸材预测、试印记录、印法比较和作品说明。

## practice_pattern_type 回归

| event | primary pattern | 回归判断 |
| --- | --- | --- |
| 任务入场 | comparison_judgment | 画出来 / 印出来对比建立问题 |
| 纸材肌理观察 | material_experiment | 摸、看、预测纸材印痕 |
| 制造纸的新肌理 | teacher_demonstration | 示范刻剪撕揉折等方法 |
| 第一次转印 | micro_practice | 小块试印验证材料效果 |
| 印法比较 | comparison_judgment | 干印、湿印、油印效果判断 |
| 用印痕完成作品 | creation_progression | 从试验转入作品完成 |
| 印痕展评 | showcase_evaluation | 用证据介绍纸印作品 |

## 条件字段验证

- `material_experiment` 激活了材料观察、材料管理和实验结论。
- `teacher_demonstration` 后接 `micro_practice_type` 与 `transition_to_formal_creation`。
- `micro_practice` 带有 `student_practice_output`：试印记录和调整计划。

## 教师默认稿检查

R223N-P3-P1 默认稿是成熟教师文稿，没有暴露组件名和后端字段。组件仅被自然化为“两图对比”“摸猜材料”“步骤拆解”“圈画印痕”等课堂动作。

## 结论

P3 delta 能区分纸印课与文具课：这里不是高密度设计改造，而是材料技法准备和印痕探究。字段增量没有导致教师稿变重。

