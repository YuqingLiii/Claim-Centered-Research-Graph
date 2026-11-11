#!/usr/bin/env python3
"""Check the Round118 machine verdict against retained evidence and reject overclaiming."""
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

assert d["status"] == "PASS_WITHOUT_ROOT_CLOSURE"
rv = d["root_verdict"]
assert rv["CIRCDIST.gross"] == rv["gap_via_lift"] == "CONJECTURED"
assert rv["Dstar_Gross"] == [11, 12]
assert not rv["branch_A_legal_distance12_schedule_established"]
assert not rv["branch_B_universal_distance_at_most11_established"]
assert rv["promotion_or_narrowing"] is None and rv["fresh_review_required"]

expected_bindings = {
    "scheduler": "9053f6d7de5acfccfed840381681991ad88f068b5f250f92b1e266ec2b936591",
    "proofpilot": "165edab1701c04e1ac79e3b5eb7d5634c5a8f20d99332d552878164565296525",
    "canonical_gross": "792c2db47abbb62fa1db07c1d3ebf780501fb1c8356d33e371c3c6ad80d19f5b",
    "round117_review": "26fd4c8c39910dae235348efc30e237c7f9ea3d93146076f3580b8c4459cf925",
    "round116_root_manifest": "2d214dc846b5cf8e7ef329e0baf9ed5204ad6340bcb9e93ac495e8e9e7a87143",
}
for name, expected in expected_bindings.items():
    row = d["dispatch"]["bindings"][name]
    assert row["sha256"] == expected == sha(R / row["path"])

i = d["iteration194"]
assert i["mandatory_quotient_solved_first"]
assert i["input"]["source"]["sha256"] == sha(R / "input/iter194/source.json.gz")
assert i["input"]["base"]["sha256"] == sha(R / "input/iter194/formula/outer.cnf")
assert i["input"]["quotient"]["sha256"] == sha(R / "input/iter194/order144_quotient/outer.cnf")
assert i["input"]["quotient"]["reviewed_equisatisfiable_without_orbit_freeness"]
outer = i["outer"]
assert outer["status"] == "SATISFIABLE" and outer["solver"]["returncode"] == 10
assert outer["solver"]["reaped"] and not outer["solver"]["detached"]
assert outer["proof_output_enabled_from_byte_zero"]
ca = outer["complete_assignment"]
assert ca["variables_assigned_exactly_once"] == 4353203
assert ca["clauses_checked"] == 21323127 and ca["all_clauses_satisfied"]
s = outer["schedule"]
assert s["edges"] == 864 and s["layers"] == 310 and s["min_time"] == 0 and s["max_time"] == 309
assert s["resource_conflicts"] == s["mc_violations"] == s["reviewed_block_hits"] == s["selector_hits"] == 0
assert s["mc_overlaps"] == 648 and s["global_interleaved"] and s["rank_compression_pairs_checked"] == 5616
oc = outer["order144_model_controls"]
assert oc["status"] == "PASS" and oc["orbit"]["distinct_schedule_vectors"] == 144
assert oc["orbit"]["stabilizer_size"] == 1 and oc["orbit"]["strict_nonidentity_roots"] == 143

for label, variables, clauses, orbit_size, stabilizer in (
    ("Xerr", 6154, 23196, 72, 1), ("Zerr", 6179, 23296, 36, 2)
):
    x = i["direct"][label]
    assert x["status"] == "SATISFIABLE" and x["query"] == "complete unrestricted direct-360"
    assert x["complete_query"] and x["physical_columns"] == 360 and x["W"] == 10
    assert x["formula"]["variables"] == variables and x["formula"]["clauses"] == clauses
    assert x["formula"]["sha256"] == sha(R / x["formula"]["path"])
    assert x["solver"]["returncode"] == 10 and x["solver"]["reaped"] and not x["solver"]["detached"]
    assignment = x["complete_assignment"]
    assert assignment["variables_assigned_exactly_once"] == variables
    assert assignment["clauses_checked"] == clauses and assignment["all_clauses_satisfied"]
    mechanism = x["mechanism"]
    assert mechanism["fault_count"] == 10 and len(mechanism["selected_names"]) == 10
    assert mechanism["canonical_syndrome"] == mechanism["physical_syndrome"] == []
    assert any(mechanism["logical_parities"])
    assert mechanism["canonical_nonstabilizer"] and mechanism["physical_nonstabilizer"]
    assert mechanism["all_360_columns_reconstructed"] and mechanism["all_clauses_satisfied"]
    orbit = x["translation_exclusion"]
    assert orbit["group_order"] == 72 and orbit["orbit_size"] == orbit_size
    assert orbit["stabilizer_size"] == stabilizer and orbit["orbit_stabilizer_product"] == 72
    assert orbit["collision_count"] == 0 and orbit["translated_physical_replays"] == 72
    assert orbit["all_translated_schedules_legal"] and orbit["all_translated_mechanisms_sound"]

assert not i["repair"]["entered"] and i["repair"]["status"] == "NOT_RUN_BY_PROTOCOL"
e = i["exclusions"]
assert e["four_translation_orbits"] == [72, 36, 72, 36]
assert e["new_selectors"] == 216 and e["final_selector_count"] == 51048
assert e["pairwise_disjoint"] and e["collision_free_against_existing"]
assert e["translation_closed"] and e["css_closed"] and e["physical_group_element_replays"] == 288
tr = i["sat_trace_retention"]
assert tr["streams"] == 3 and tr["raw_bytes"] == 33456766269 and tr["gzip_bytes"] == 6685262605
assert tr["empty_clause_lines"] == 0 and tr["lossless_roundtrip_verified"]
assert not tr["unsat_certificate_credit"]

f = d["iteration195_fresh_frontier"]
assert f["status"] == "CHECKED_UNSTARTED" and f["solver_invocations"] == 0
assert not f["started"] and f["sat_result"] is f["unsat_result"] is None
assert f["forbidden_solver_artifacts"] == []
assert f["source"]["blocks"] == 814392 and f["source"]["selectors"] == 51048 and f["source"]["assertions"] == 869838
assert f["source"]["sha256"] == sha(R / f["source"]["path"])
assert f["source"]["state_sha256"] == sha(R / "frontier/iter195/state.json")
assert f["base"]["variables"] == 3124223 and f["base"]["clauses"] == 11459291 and f["base"]["assertions"] == 869838
assert f["base"]["sha256"] == sha(R / f["base"]["path"])
assert f["quotient"]["variables"] == 4359743 and f["quotient"]["clauses"] == 21343594
assert f["quotient"]["roots"] == 143 and f["quotient"]["group_order"] == 144
assert f["quotient"]["equisatisfiable_with_full_iter195_base"]
assert f["quotient"]["sha256"] == sha(R / f["quotient"]["path"])
assert f["closure"]["order144"] and f["closure"]["nonfree_orbits_explicitly_handled"]
assert f["closure"]["orbit_sizes"] == [72, 36, 72, 36]

forbidden = []
for path in (R / "frontier/iter195").rglob("*"):
    if not path.is_file() or path.name == "CHECKED_UNSTARTED.json":
        continue
    lower = path.name.lower()
    if path.suffix.lower() in (".drat", ".lrat", ".proof", ".model", ".assignment") or any(
        token in lower for token in ("solver.log", "assignment.dimacs", "model.dimacs")
    ):
        forbidden.append(path.relative_to(R).as_posix())
assert not forbidden

defects = d["reviewed_parent_documentation_defects"]
assert defects["preserved_parent_package"] and not defects["parent_modified"]
assert not defects["material_to_round118_science"]

out = {
    "schema": "circdist-gross-round118-result-check-v1",
    "status": "PASS",
    "root_overclaim_rejected": True,
    "iteration194_disposition": ["SAT", "SAT", "SAT"],
    "repair_status": "NOT_RUN_BY_PROTOCOL",
    "iteration195_status": "CHECKED_UNSTARTED",
    "forbidden_iteration195_solver_artifacts": forbidden,
    "checked_hashes": {
        "source": f["source"]["sha256"],
        "base": f["base"]["sha256"],
        "quotient": f["quotient"]["sha256"],
    },
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
