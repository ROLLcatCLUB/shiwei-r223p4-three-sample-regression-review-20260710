import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[2]

REQUIRED_FILES = [
    "R223P_4_regression_plan.md",
    "R223P_4_sample_M_stationery_regression.md",
    "R223P_4_sample_N_paper_print_regression.md",
    "R223P_4_sample_O_color_collision_regression.md",
    "R223P_4_three_sample_regression_matrix.json",
    "R223P_4_teacher_default_view_check.md",
    "R223P_4_review_ledger_check.md",
    "R223P_4_component_trigger_status_check.md",
    "R223P_4_unit_intensity_router_effectiveness_check.md",
    "R223P_4_field_overload_check.md",
    "R223P_4_decision_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]

SAMPLES = ["sample_M_stationery", "sample_N_paper_print", "sample_O_color_collision"]
FORBIDDEN_TEACHER_TERMS = [
    "practice_pattern_type",
    "demonstration_type",
    "micro_practice_type",
    "appreciation_scaffold_type",
    "component_trigger",
    "component_trigger_status",
    "screen_trigger",
    "learning_sheet_fields",
]
PATTERNS = [
    "observation_discovery",
    "comparison_judgment",
    "artwork_appreciation",
    "teacher_demonstration",
    "micro_practice",
    "material_experiment",
    "idea_generation",
    "creation_progression",
    "showcase_evaluation",
    "closure_transfer",
]
STATUS_VALUES = [
    "already_registered",
    "candidate_from_R222D_pool",
    "new_surface_candidate",
    "unregistered_do_not_execute",
]
FORBIDDEN_TRUE_FLAGS = [
    "schema_v0_2_published",
    "r223m_p5_schema_modified",
    "existing_teacher_drafts_modified",
    "r222d_component_library_modified",
    "formal_ui",
    "r97b_modified",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "formal_apply",
]
TEACHER_SOURCE_MAP = {
    "sample_M_stationery": WORKSPACE / "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223M_P5_GOLDEN_STANDARD_LOCK_PACKAGE/R223M_P5_teacher_default_reading_sample_v0_1.md",
    "sample_N_paper_print": WORKSPACE / "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223N_P3_P1_LIGHT_SAMPLE_FLAVOR_AND_LAYOUT_POLISH/R223N_P3_P1_teacher_manuscript_draft_v5.md",
    "sample_O_color_collision": WORKSPACE / "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R223O_P1_COLOR_MANUSCRIPT_STRUCTURE_RECOVERY/R223O_P1_teacher_manuscript_draft_v2.md",
}


def add(checks, name, passed, detail=None):
    item = {"check": name, "passed": bool(passed)}
    if detail is not None:
        item["detail"] = detail
    checks.append(item)


def load_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def main():
    checks = []
    for name in REQUIRED_FILES:
        add(checks, f"required_file:{name}", (ROOT / name).exists())

    manifest = load_json("PACKAGE_MANIFEST.json")
    matrix = load_json("R223P_4_three_sample_regression_matrix.json")

    add(checks, "manifest_stage", manifest.get("stage_id") == "1013R_R223P_4_THREE_SAMPLE_REGRESSION")
    add(checks, "decision", matrix.get("decision") == "PASS_CONTINUE_TO_R223P_5_V0_2_LOCK_CANDIDATE")

    for flag in FORBIDDEN_TRUE_FLAGS:
        add(checks, f"boundary_false:{flag}", manifest.get(flag) is False and matrix.get(flag, False) is False)

    sample_map = {sample.get("sample_id"): sample for sample in matrix.get("samples", [])}
    for sample_id in SAMPLES:
        sample = sample_map.get(sample_id)
        add(checks, f"sample_exists:{sample_id}", sample is not None)
        if not sample:
            continue
        add(checks, f"sample_pass:{sample_id}", sample.get("regression_result") == "PASS")
        profile = sample.get("lesson_profile", {})
        for key in ["unit_phase_role", "practice_intensity", "student_work_time_ratio", "teacher_support_density"]:
            add(checks, f"profile:{sample_id}:{key}", bool(profile.get(key)))
        events = sample.get("events", [])
        add(checks, f"events_min_7:{sample_id}", len(events) >= 7)
        for event in events:
            eid = event.get("event_id", "unknown")
            primary = event.get("primary_practice_pattern_type")
            add(checks, f"primary_pattern:{sample_id}:{eid}", primary in PATTERNS)
            add(checks, f"evidence_outputs:{sample_id}:{eid}", bool(event.get("evidence_outputs")))
            for trigger in event.get("component_triggers", []):
                add(checks, f"component_status:{sample_id}:{eid}:{trigger.get('component_id')}", trigger.get("status") in STATUS_VALUES)

    distinct_profiles = {
        (
            sample.get("lesson_profile", {}).get("unit_phase_role"),
            sample.get("lesson_profile", {}).get("practice_intensity"),
            sample.get("lesson_profile", {}).get("teacher_support_density"),
        )
        for sample in matrix.get("samples", [])
    }
    add(checks, "unit_intensity_distinct_profiles_at_least_2", len(distinct_profiles) >= 2, sorted(map(str, distinct_profiles)))

    for sample_id, path in TEACHER_SOURCE_MAP.items():
        exists = path.exists()
        add(checks, f"teacher_source_exists:{sample_id}", exists, str(path))
        if exists:
            text = path.read_text(encoding="utf-8")
            for term in FORBIDDEN_TEACHER_TERMS:
                add(checks, f"teacher_no_forbidden:{sample_id}:{term}", term not in text)

    contamination_terms = {
        "sample_M_stationery": ["纸印", "红黄蓝", "间色"],
        "sample_N_paper_print": ["赠笔", "智造", "红黄蓝"],
        "sample_O_color_collision": ["赠笔", "纸印", "版画车间坊"],
    }
    for sample_id, terms in contamination_terms.items():
        path = TEACHER_SOURCE_MAP[sample_id]
        if path.exists():
            text = path.read_text(encoding="utf-8")
            for term in terms:
                add(checks, f"no_content_contamination:{sample_id}:{term}", term not in text)

    for name in [
        "R223P_4_teacher_default_view_check.md",
        "R223P_4_review_ledger_check.md",
        "R223P_4_component_trigger_status_check.md",
        "R223P_4_unit_intensity_router_effectiveness_check.md",
        "R223P_4_field_overload_check.md",
    ]:
        text = read(name)
        add(checks, f"doc_mentions_PASS:{name}", "PASS" in text or "pass" in text or "effective" in text)

    result_summary = matrix.get("cross_sample_result", {})
    for key in [
        "all_samples_pass",
        "teacher_default_view_clean",
        "review_ledger_has_primary_patterns",
        "unregistered_components_hidden_from_teacher_default",
    ]:
        add(checks, f"cross_sample_true:{key}", result_summary.get(key) is True)
    add(checks, "content_contamination_false", result_summary.get("content_contamination_detected") is False)
    add(checks, "field_overload_false", result_summary.get("field_overload_detected") is False)
    add(checks, "unit_intensity_effective_2_of_3", result_summary.get("unit_intensity_router_effective_samples", 0) >= 2)

    failures = [check for check in checks if not check["passed"]]
    result = {
        "passed": not failures,
        "check_count": len(checks),
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223P_5_V0_2_LOCK_CANDIDATE" if not failures else "HOLD_FOR_DELTA_REDUCTION",
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223P_4_three_sample_regression_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["passed", "check_count", "failed", "decision"]}, ensure_ascii=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
