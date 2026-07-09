# R223P-4 three sample regression plan

stage_id: 1013R_R223P_4_THREE_SAMPLE_REGRESSION  
status: regression_only  
decision: PASS_CONTINUE_TO_R223P_5_V0_2_LOCK_CANDIDATE  

## 目标

R223P-4 用三个已通过的样本验证 R223P-3 的 `classroom_event_schema v0.2 delta` 是否可用。P4 不改 R223M/N/O 既有教师稿，不发布 v0.2，不改组件库，不接 UI/runtime。

## 回归样本

| sample_id | 样本 | 课型侧重 | 来源 |
| --- | --- | --- | --- |
| sample_M_stationery | 《我为文具代言》第三阶段 | 设计应用 / 生活问题解决 / 高实践密度创作 | R223M-P5 |
| sample_N_paper_print | 《有趣的纸印》 | 材料技法 / 印痕探究 / 材料实验 | R223N-P3-P1 |
| sample_O_color_collision | 《色彩的碰撞》 | 视觉语言 / 色彩感知 / 表达 | R223O-P1 |

## 必测项

1. `unit_phase_role` 与 `practice_intensity` 是否能区分课时展开密度。
2. `practice_pattern_type` 是否能标注事件模式，而不替代教学设计。
3. `demonstration_type`、`micro_practice_type`、`appreciation_scaffold_type` 是否条件启用。
4. `component_trigger` 是否带状态，未注册组件不进入教师默认稿。
5. 教师默认稿是否仍是成熟教案文稿，不回到字段墙。
6. review ledger 是否保存模式、组件、大屏、学习单和证据链。
7. 三个样本之间是否无内容污染。
8. 至少 2/3 样本证明 `unit_phase_role + practice_intensity` 有实际区分度。

## 通过线

```text
每个样本 validator pass
每个样本教师默认稿不出现禁止字段名
每个样本 review ledger 含 primary practice_pattern_type
三样本无文具 / 纸印 / 色彩内容互相迁移污染
至少 2/3 样本证明 unit_phase_role + practice_intensity 有实际区分度
未注册组件不得进入教师默认稿
字段 delta 不导致教师稿变重
```

## 当前边界

```text
R223M_STANDARD_V0_2 = NOT_PUBLISHED
R223M/N/O_EXISTING_DRAFTS = UNMODIFIED
R222D_COMPONENT_LIBRARY = UNMODIFIED
FORMAL_UI = BLOCKED
R97B / runtime / prompt / model / db = UNTOUCHED
```

