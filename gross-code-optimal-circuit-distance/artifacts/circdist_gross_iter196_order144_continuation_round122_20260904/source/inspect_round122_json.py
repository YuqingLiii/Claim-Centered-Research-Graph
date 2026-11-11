#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("kind", choices=["orbits", "translation", "css", "advance", "state", "metadata", "check", "direct", "replay"])
p.add_argument("path", type=Path)
a = p.parse_args()
d = json.loads(a.path.read_text(encoding="utf-8"))
if a.kind == "orbits":
    out = {
        "schema": d.get("schema"),
        "status": d.get("status"),
        "distinct_candidate_translation_orbits": d.get("distinct_candidate_translation_orbits"),
        "all_candidate_orbits_collision_free_against_css_closed_base": d.get("all_candidate_orbits_collision_free_against_css_closed_base"),
        "all_distinct_candidate_orbits_pairwise_disjoint": d.get("all_distinct_candidate_orbits_pairwise_disjoint"),
        "all_dual_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer": d.get("all_dual_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer"),
        "all_dual_schedules_legal": d.get("all_dual_schedules_legal"),
        "dual_results": [{k: x.get(k) for k in ("source_sector", "target_sector", "orbit_size", "stabilizer_size", "stabilizer_deltas", "translated_replay_count", "parent_support_is_exact_D_image")} for x in d.get("dual_results", [])],
        "source_results": [{k: x.get(k) for k in ("sector", "orbit_size", "stabilizer_size", "stabilizer_deltas", "translated_replay_count")} for x in d.get("source_results", [])],
        "bindings": d.get("bindings"),
    }
elif a.kind == "translation":
    out = {k: d.get(k) for k in ("schema", "status", "sector", "orbit_size", "stabilizer_size", "stabilizer_deltas", "translated_replay_count", "registry_collision_count", "prior_orbit_collision_count", "all_physical_replays_pass")}
elif a.kind == "css":
    out = {k: d.get(k) for k in ("schema", "status", "D_squared_identity", "D_T_delta_D_equals_T_neg_delta", "source_css_closed", "candidate_schedule_dual_legal")}
    out["keys"] = sorted(d)
elif a.kind == "advance":
    mech = d.get("iter196_mechanism_exclusions", {})
    out = {
        "schema": d.get("schema"),
        "status": d.get("status"),
        "input": d.get("input"),
        "output": d.get("output"),
        "fresh_frontier": d.get("fresh_frontier"),
        "closure": d.get("closure"),
        "mechanism_exclusions": {k: mech.get(k) for k in ("translation_orbits", "orbit_sizes", "selectors", "pairwise_disjoint", "collision_free_against_css_closed_input", "all_288_group_element_replays_covering_216_distinct_original_and_dual_selectors", "new_selectors_by_sector_including_inherited_closure")},
        "bindings": d.get("bindings"),
    }
elif a.kind == "metadata":
    keep = ("schema", "status", "variables", "clauses", "cnf_sha256", "source_file_sha256", "source_semantic_payload_sha256", "base_cnf_sha256", "base_variables", "base_clauses", "quotient_cnf_sha256", "quotient_variables", "quotient_clauses", "root_count", "roots", "stabilizer_safe_roots", "equivalence_kind", "assertions", "selector_count", "reviewed_blocks", "membership_expressions", "rank_expressions")
    out = {k: d.get(k) for k in keep if k in d}
    out["keys"] = sorted(d)
elif a.kind == "direct":
    out = {"keys": sorted(d), "schema": d.get("schema"), "status": d.get("status")}
    for key, value in d.items():
        if isinstance(value, dict):
            out[key + "_keys"] = sorted(value)
    out["sectors"] = d.get("sectors")
    out["geometry"] = d.get("geometry")
    out["schedule"] = d.get("schedule")
    out["scientific_conclusion"] = d.get("scientific_conclusion")
elif a.kind == "replay":
    out = {"keys": sorted(d), "schema": d.get("schema"), "status": d.get("status")}
    for key, value in d.items():
        if isinstance(value, (str, int, float, bool)) or value is None:
            out[key] = value
        elif isinstance(value, dict):
            out[key + "_keys"] = sorted(value)
elif a.kind in {"state", "check"}:
    out = d
print(json.dumps(out, sort_keys=True, indent=2))
