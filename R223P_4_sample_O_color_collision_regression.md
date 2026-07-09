# R223P-4 sample O regression: 色彩的碰撞

source_stage: R223O-P1  
sample_focus: 视觉语言 / 色彩感知 / 表达  
regression_result: PASS

## unit intensity router

```text
unit_phase_role = intro_understanding
lesson_position_in_unit = early
practice_intensity = medium
student_work_time_ratio = medium
teacher_support_density = normal
```

该样本处于色彩单元早段，重点是从校园色彩和三原色实验建立视觉语言。它需要调色实验，但不是完整高密度创作课。因此 `practice_intensity=medium` 能控制展开：保留实验、小样、比较和展示，但不扩成大作业辅导。

## practice_pattern_type 回归

| event | primary pattern | 回归判断 |
| --- | --- | --- |
| 校园色彩入场 | observation_discovery | 从生活色彩建立问题 |
| 红黄蓝起点 | observation_discovery | 建立实验起点 |
| 两色调和 | material_experiment | 用两色实验发现间色 |
| 同色差异 | comparison_judgment | 比较偏向、明暗和冷暖 |
| 复色进阶 | micro_practice | 少量第三色小练和错误修补 |
| 色彩创想任务 | idea_generation | 选择代表色并命名表达 |
| 创想会分享 | showcase_evaluation | 用调色记录支持表达 |

## 条件字段验证

- `aesthetic_language_focus` 对色彩课有效：偏向、明暗、冷暖、画面感受。
- `material_experiment` 不迁移纸印材料逻辑，而是表达调色实验。
- `micro_practice_type` 用于复色小练，带 `student_practice_output` 和调色记录。

## 教师默认稿检查

R223O-P1 默认稿没有暴露 `practice_pattern_type`、`component_trigger` 或组件货架。结构是成熟教案文稿：课时定位、主线图、过程摘要、教学过程、评价设计和大屏结构。

## 结论

P3 delta 能迁移到视觉语言/色彩感知课型，并没有把文具课或纸印课内容迁移进来。

