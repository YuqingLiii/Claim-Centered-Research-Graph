#!/usr/bin/env python3
"""Cross-check RESULT.json against sealed Round96 evidence."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def actual(path):
    path = Path(path)
    if path.exists():
        return path, path.suffix == ".gz"
    gz = path.with_name(path.name + ".gz")
    assert gz.exists(), path
    return gz, True


def data_sha(path):
    path, compressed = actual(path)
    data = gzip.decompress(path.read_bytes()) if compressed else path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)


def object_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
x = load(R / "RESULT.json")
audit = load(R / "verification/independent_campaign_audit.json")
assert x["status"] == audit["status"] == "PASS"
assert x["verdict"] == audit["scientific_verdict"] == "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED"
assert x["root_status"] == x["route_status"] == "CONJECTURED" and x["D_star_Gross"] == [11, 12]
assert x["completed_candidate_count"] == 12 and x["strict_serial"]
assert x["all_outer_dispositions"] == x["all_direct_dispositions"] == "SATISFIABLE"
assert x["outer_sat_count"] == 12 and x["direct_sat_count"] == 24
assert x["unsat_count"] == x["unknown_count"] == x["timeout_count"] == 0
assert x["repair_entered"] is False and x["canonical_edits"] is False and x["commit"] is False and x["push"] is False
assert x["source_model"]["inherited_order_predicates"] == 14484
assert x["source_model"]["block_family_counts"] == {"unary": 1440, "round62": 20, "generalized": 12820, "dynamic": 204}

initial = x["initial_frontier"]
assert sha_file(R / "state/iter148_state.json") == initial["state_file_sha256"] == "1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81"
assert initial["selector_count"] == 256 and initial["selector_state_sha256"] == "9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f"
assert sha_file(R / "formulas/iter148/source.json.gz") == initial["source_file_sha256"]
assert data_sha(R / "formulas/iter148/outer.cnf") == initial["cnf_sha256"]

synthesis = load(R / "synthesis/order4_gf2_closure.json")
assert sha_file(R / x["synthesis"]["file"]) == x["synthesis"]["file_sha256"]
assert synthesis["finite_domain"]["unordered_distinct_quadruples_enumerated"] == x["synthesis"]["finite_domain_size"] == 15254626
eligible = sum(synthesis["sector_results"][s]["eligible_weight_1_to_10_with_multiplicity"] for s in ("Xerr", "Zerr"))
novel = sum(synthesis["sector_results"][s]["unique_novel_eligible_results"] for s in ("Xerr", "Zerr"))
assert eligible == x["synthesis"]["eligible_weight_1_to_10_with_multiplicity"] == 33760
assert novel == x["synthesis"]["unique_novel_eligible_results"] == 33654
assert len(synthesis["retained_terms"]) == x["synthesis"]["retained_terms"] == 0

assert len(x["iterations"]) == 12
for iteration, row in zip(range(148, 160), x["iterations"]):
    assert row["iteration"] == iteration and row == audit["iterations"][iteration - 148]
    F = R / "formulas" / f"iter{iteration}"
    I = R / "iterations" / f"iter{iteration}"
    metadata = load(F / "metadata.json")
    candidate = load(I / "outer/candidate.json")
    direct = load(I / "direct/direct_verification.json")
    record = load(I / "record.json")
    assert row["source_selector_count"] == 256 + 2 * (iteration - 148) == metadata["selector_count"]
    assert row["outer"]["status"] == "SATISFIABLE" and row["outer"]["complete_assignment"]
    assert row["outer"]["cnf_sha256"] == metadata["cnf_sha256"] == data_sha(F / "outer.cnf")
    assert row["outer"]["schedule_sha256"] == candidate["compressed_schedule_sha256"]
    assert record["new_selectors"] == [f"r96-i{iteration}-Xerr", f"r96-i{iteration}-Zerr"]
    assert record["state_mutated_atomically"] and record["repair_entered"] is False
    for sector in ("Xerr", "Zerr"):
        r = row["direct"][sector]
        d = direct["sectors"][sector]
        mechanism = d["mechanism"]
        assert r["status"] == d["status"] == "SATISFIABLE" and r["complete_assignment"] and r["physical_replay"]
        assert r["weight"] == mechanism["fault_count"]
        assert r["canonical_support_weight"] == mechanism["canonical_replay"]["net_weight"]
        assert r["physical_support_weight"] == mechanism["physical_net_weight"]
        assert r["physical_detector_syndrome"] == mechanism["physical_syndrome"] == []
        assert r["physical_logical_action"] == mechanism["physical_logical_parities"]
        assert r["canonical_physical_parities_equal"] is True
        assert r["mechanism_semantic_sha256"] == object_sha(mechanism)
        assert d["all_dimacs_clauses_satisfied"] and d["formula_summary"]["complete_query"]
        assert mechanism["physical_syndrome"] == [] and mechanism["physical_nontrivial"]
        assert mechanism["canonical_physical_parities_equal"]

assert x["weight_summary"]["Xerr"]["weight_9_iterations"] == []
assert x["weight_summary"]["Zerr"]["weight_9_iterations"] == [148, 152]
assert x["sat_proof_streams"]["count"] == 36 and x["sat_proof_streams"]["empty_clause_lines"] == 0
assert x["proof_objects"]["actual_unsat_count"] == 0
assert x["proof_objects"]["gross_unsat_drat"] is None and x["proof_objects"]["gross_unsat_lrat"] is None
assert x["proof_objects"]["direct_unsat_proofs"] == []
proof = load(R / "controls/proof_fixture_controls.json")
assert proof["status"] == "PASS" and proof["scope"] == "tool-chain controls only; no Gross UNSAT occurred"
for key in ("valid_drat_accepted", "generated_lrat_accepted", "corrupt_drat_rejected", "truncated_drat_rejected", "corrupt_lrat_rejected", "truncated_lrat_rejected"):
    assert proof[key] and x["proof_objects"]["fixture_controls"][key]

fresh = x["fresh_state"]
state = load(R / "state/iter160_state.json")
metadata = load(R / "formulas/iter160/metadata.json")
assert state["next_iteration"] == fresh["next_iteration"] == 160 and state["started"] is fresh["started"] is False
assert state["selector_count"] == fresh["selector_count"] == 280
assert state["selector_state_sha256"] == fresh["selector_state_sha256"] == "ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3"
assert sha_file(R / "state/iter160_state.json") == fresh["state_file_sha256"]
assert sha_file(R / "formulas/iter160/source.json.gz") == fresh["source_file_sha256"]
assert metadata["assertions"] == fresh["assertions"] == 19162
assert metadata["variables"] == fresh["variables"] == 411526
assert metadata["clauses"] == fresh["clauses"] == 1396722
assert metadata["cnf_sha256"] == fresh["cnf_sha256"] == data_sha(R / "formulas/iter160/outer.cnf")
assert not (R / "iterations/iter160").exists()
print("ROUND96_RESULT_CROSSCHECK_PASS", len(x["iterations"]), fresh["selector_count"])
