#!/usr/bin/env python3
"""Check the Round120 machine verdict and reject any root overclaim."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
d = json.loads((R / "RESULT.json").read_text())

assert d["schema"] == "circdist-gross-round120-proposer-result-v1"
assert d["status"] == "PASS_WITHOUT_ROOT_CLOSURE"
rv = d["root_verdict"]
assert rv["CIRCDIST.gross"] == rv["gap_via_lift"] == "CONJECTURED"
assert rv["Dstar_Gross"] == [11, 12]
assert not rv["branch_A_legal_distance12_schedule_established"]
assert not rv["branch_B_universal_distance_at_most11_established"]
assert rv["promotion_or_narrowing"] is None and rv["fresh_review_required"]

expected_bindings = {
    "scheduler": "0614734c7b1e4227935a0ec82e973d43e46be761baba6e3d5a706b01b0473177",
    "canonical_gross": "0b30330901d01b6eec2bb7dae69bf7aa9c4cc4530060cbed55382313ec9cbe96",
    "round119_exact_review": "d79e9ca01e43f646bf1fdd2bcfd7fa05c3845da4d7d4e8f7cd75b37d3bdbdd46",
    "round118_root_manifest": "c4e089e3daaebccca09a4ba12b338e751321b62054b997440837c8b6d905d329",
    "round120_proofpilot": "10b4cb531ff91bc13cbf926329a1a367baf71874f011d68b0132751f057bfcdd",
}
for name, expected in expected_bindings.items():
    row = d["dispatch"]["bindings"][name]
    assert row["sha256"] == expected == sha(R / row["path"])
assert d["dispatch"]["winner"] == "CIRCDIST.gross@dstar-residual"
assert d["dispatch"]["score"] == 0.0010998258664973192

i = d["iteration195"]
assert i["reviewed_frontier_genuinely_unstarted_before_science"]
assert i["mandatory_quotient_solved_first"]
assert i["input"]["source"]["sha256"] == sha(R / "input/iter195/source.json.gz")
assert i["input"]["source"]["semantic_sha256"] == "fa3a1b80b6b33a6ef14fa314aba2fd8acc394af588bb670a36d8bcffb44cb55b"
assert i["input"]["state"]["sha256"] == sha(R / "input/iter195/state.json")
assert i["input"]["base"]["sha256"] == sha(R / "input/iter195/formula/outer.cnf")
assert i["input"]["quotient"]["sha256"] == sha(R / "input/iter195/order144_quotient/outer.cnf")
assert i["input"]["quotient"]["reviewed_equisatisfiable_without_orbit_freeness"]

outer = i["outer"]
assert outer["status"] == "SATISFIABLE" and outer["solver"]["returncode"] == 10
assert outer["solver"]["reaped"] and not outer["solver"]["detached"]
assert not outer["solver"]["timeout_configured"] and not outer["solver"]["timeout_triggered"]
assert outer["proof_output_enabled_from_byte_zero"]
assert outer["complete_assignment"]["variables_assigned_exactly_once"] == 4359743
assert outer["complete_assignment"]["clauses_checked"] == 21343594
assert outer["complete_assignment"]["all_clauses_satisfied"]
s = outer["schedule"]
assert s["edges"] == 864 and s["layers"] == 325 and s["min_time"] == 0 and s["max_time"] == 324
assert s["resource_conflicts"] == s["mc_violations"] == s["reviewed_block_hits"] == s["selector_hits"] == 0
assert s["mc_overlaps_checked"] == 648 and s["global_interleaved"] and s["rank_compression_pairs_checked"] == 5616
orbit = outer["order144_action_audit"]["orbit"]
assert orbit["group_order"] == orbit["distinct_schedule_vectors"] == orbit["orbit_stabilizer_product"] == 144
assert orbit["stabilizer_size"] == 1 and orbit["strict_nonidentity_roots"] == 143

for label, variables, clauses in (("Xerr", 6142, 23148), ("Zerr", 6135, 23120)):
    sector = i["direct"][label]
    assert sector["status"] == "SATISFIABLE" and sector["query"] == "complete unrestricted direct-360"
    assert sector["complete_query"] and sector["physical_columns"] == 360 and sector["threshold_W"] == 10
    assert sector["formula"]["variables"] == variables and sector["formula"]["clauses"] == clauses
    assert sector["formula"]["sha256"] == sha(R / sector["formula"]["path"])
    assert sector["solver"]["returncode"] == 10 and sector["solver"]["reaped"] and not sector["solver"]["detached"]
    assignment = sector["complete_assignment"]
    assert assignment["variables_assigned_exactly_once"] == variables
    assert assignment["clauses_checked"] == clauses and assignment["all_clauses_satisfied"]
    mechanism = sector["mechanism"]
    assert mechanism["fault_count"] == len(mechanism["selected_names"]) == 10
    assert mechanism["canonical_syndrome"] == mechanism["physical_syndrome"] == []
    assert any(mechanism["logical_parities"])
    assert mechanism["canonical_nonstabilizer"] and mechanism["physical_nonstabilizer"]
    assert mechanism["all_360_columns_reconstructed"]
    translated = sector["translation_orbit"]
    assert translated["group_order"] == translated["orbit_size"] == translated["orbit_stabilizer_product"] == 72
    assert translated["stabilizer_size"] == 1 and translated["stabilizer_deltas"] == [[0, 0]]
    assert translated["collision_count"] == 0 and translated["translated_physical_replays"] == 72
    assert translated["all_schedules_legal"] and translated["all_mechanisms_sound"]

assert not i["repair"]["entered"] and i["repair"]["status"] == "NOT_RUN_BY_PROTOCOL"
e = i["exclusions"]
assert e["translation_orbit_sizes"] == [72, 72, 72, 72]
assert e["translation_stabilizer_sizes"] == [1, 1, 1, 1]
assert e["distinct_orbits"] == 4 and e["new_selectors"] == 288 and e["final_selector_count"] == 51336
assert e["new_selectors_by_sector"] == {"Xerr": 144, "Zerr": 144}
assert e["pairwise_disjoint"] and e["collision_free_against_existing"]
assert e["translation_closed"] and e["css_closed"] and e["physical_group_element_replays"] == 288
traces = i["sat_trace_retention"]
assert traces["stream_count"] == 3 and traces["raw_bytes"] == 20645231426
assert traces["gzip_bytes"] == 3924456936 and traces["empty_clause_lines"] == 0
assert traces["all_lossless_roundtrips_verified"] and not traces["unsat_certificate_credit"]

f = d["iteration196_fresh_frontier"]
assert f["status"] == "CHECKED_UNSTARTED" and f["solver_invocations"] == 0
assert not f["started"] and f["sat_result"] is f["unsat_result"] is None
assert f["forbidden_solver_artifacts"] == [] and f["files_before_unstarted_marker"] == 15
assert f["source"]["blocks"] == 814392 and f["source"]["selectors"] == 51336 and f["source"]["assertions"] == 870126
assert f["source"]["sha256"] == sha(R / f["source"]["path"])
assert f["source"]["state_sha256"] == sha(R / "frontier/iter196/state.json")
assert f["base"]["variables"] == 3130306 and f["base"]["clauses"] == 11477997 and f["base"]["assertions"] == 870126
assert f["base"]["sha256"] == sha(R / f["base"]["path"])
assert f["quotient"]["variables"] == 4365826 and f["quotient"]["clauses"] == 21362300
assert f["quotient"]["roots"] == 143 and f["quotient"]["group_order"] == 144
assert f["quotient"]["appended_clauses"] == 9884303 and f["quotient"]["equisatisfiable_with_full_iter196_base"]
assert f["quotient"]["sha256"] == sha(R / f["quotient"]["path"])
assert f["closure"]["translation"] == f["closure"]["css"] == f["closure"]["order144"] == "PASS"

forbidden = []
for path in (R / "frontier/iter196").rglob("*"):
    if not path.is_file() or path.name == "CHECKED_UNSTARTED.json":
        continue
    lower = path.name.lower()
    if path.suffix.lower() in (".drat", ".lrat", ".proof", ".model", ".assignment") or any(
        token in lower for token in ("solver.log", "assignment.dimacs", "model.dimacs")
    ):
        forbidden.append(path.relative_to(R).as_posix())
assert not forbidden

out = {
    "schema": "circdist-gross-round120-result-check-v1", "status": "PASS",
    "root_overclaim_rejected": True, "iteration195_disposition": ["SAT", "SAT", "SAT"],
    "repair_status": "NOT_RUN_BY_PROTOCOL", "iteration196_status": "CHECKED_UNSTARTED",
    "forbidden_iteration196_solver_artifacts": forbidden,
    "checked_hashes": {"source": f["source"]["sha256"], "base": f["base"]["sha256"],
                       "quotient": f["quotient"]["sha256"]},
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
