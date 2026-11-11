#!/usr/bin/env python3
"""Check every load-bearing Round126 result claim against packaged evidence."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--root", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args(); R = a.root.resolve()
r = json.loads((R / "RESULT.json").read_text())
b = json.loads((R / "INPUT_BINDINGS.json").read_text())
f = json.loads((R / "FRESH_FRONTIER.json").read_text())
assert r["status"] == b["status"] == "PASS" and f["status"] == "CHECKED_UNSTARTED"
assert "ITER198_CANDIDATE_KILLED_BY_BOTH_COMPLETE_DIRECT360_SECTORS" in r["verdict"]
for rel, digest in b["dispatch_hashes"].items():
    assert sha(R / rel) == digest, rel
assert b["mandatory_iter198_counts"] == {"blocks": 814392, "selectors": 51840, "assertions": 870630}
assert b["mandatory_iter198_base"] == {"sha256": "4dc712e335bd3d22c753aaa61e8603026c514a070522a94aa2e239714e185f8f", "variables": 3152127, "clauses": 11550293}
assert b["mandatory_iter198_order144_quotient"] == {"sha256": "ee72ce86b4191f6e2602d500e2dc157ea4aca9565028fa7c07073d8b8d19bd08", "variables": 4387647, "clauses": 21434596, "roots": 143}

assert r["outer"]["status"] == "SATISFIABLE" and r["outer"]["exact_mandatory_formula"]
outer = r["outer"]["semantic_replay"]
assert outer["complete_assignment_variables"] == 4387647 and outer["dimacs_clauses_checked"] == 21434596
assert outer["all_dimacs_clauses_satisfied"] and outer["reviewed_block_hits"] == 0
assert outer["efssc_named_frozen_valid_selectors"] == outer["efssc_symbolic_valid_selectors"] == 0
assert outer["frozen_schedule_audit"]["ok"] and outer["frozen_schedule_audit"]["edge_count"] == 864
orbit = r["outer"]["order144_orbit_controls"]
assert orbit["status"] == "PASS" and orbit["orbit"]["distinct_schedule_vectors"] == 144
assert orbit["orbit"]["stabilizer_size"] == 1 and orbit["orbit"]["strict_nonidentity_roots"] == 143

assert r["direct360"]["scope"].startswith("two complete unrestricted direct-360")
for label, expected in {"Xerr": (6130, 23100), "Zerr": (6151, 23184)}.items():
    s = r["direct360"]["sectors"][label]
    assert s["status"] == "SATISFIABLE" and (s["variables"], s["clauses"]) == expected
    assert s["fault_count"] == 10 and s["all_columns_reconstructed"] == 360
    assert s["all_clauses_checked"] == expected[1] and s["all_clauses_satisfied"]
    assert s["canonical_syndrome"] == s["physical_syndrome"] == []
    assert any(s["logical_parities"]) and s["canonical_nonstabilizer"] and s["physical_nonstabilizer"]
    assert len(s["selected_names"]) == 10
assert r["direct360"]["geometry"]["stabilizer_rank_per_sector"] == 66
assert r["direct360"]["geometry"]["logical_dimension"] == 12
assert r["direct360"]["geometry"]["cross_pairing_rank"] == 12

lineage = r["selector_lineage"]
assert lineage["all_physical_group_element_replays"] == 288
assert lineage["distinct_installed_selectors"] == 288
assert [lineage["original_orbits"][x]["size"] for x in ("Xerr", "Zerr")] == [72, 72]
assert [x["size"] for x in lineage["css_dual_orbits"]] == [72, 72]
assert all(x["stabilizer"] == [[0, 0]] for x in lineage["css_dual_orbits"])

assert f["iteration"] == 199 and not f["started"] and f["solver_invocations"] == 0
assert [f["blocks"], f["selectors"], f["assertions"]] == [814392, 52128, 870918]
assert f["base"] == {"sha256": "c08af6fc567c6d8554428eac5873c276ee4b89137d7c6bff192baca4608a1f9d", "variables": 3162788, "clauses": 11584428}
assert f["order144_quotient"] == {"sha256": "602f91c302883ec3ad6a1d9c4cc6b31b450d00feba059707fdc5c37a69aa71e1", "variables": 4398308, "clauses": 21468731, "roots": 143}
assert sha(R / "frontier/iter199/source.json.gz") == f["source_sha256"] == "ceb91b607e6434f9ef20c6177ba1ee5792b8688790f88f5ec89ee5b75d8f715f"
assert sha(R / "frontier/iter199/state.json") == f["state_sha256"] == "ba0795e0f82282193e6fe5c6566127fb69b680803cf50a216bcdb859933e39ab"
assert sha(R / "frontier/iter199/CHECKED_UNSTARTED.json") == f["checked_unstarted_sha256"] == "6b421a829cec5b07b63b8208443301f60d3e482735f6d20f722fe78563019f71"
for d in r["sat_search_traces"].values():
    assert d["classification"] == "SAT_SEARCH_TRACE" and d["unsat_certificate_credit"] == 0
    assert d["proof_output_enabled_from_byte_zero"]
    assert sha(R / d["package_gzip_path"]) == d["gzip_sha256"]
verification = r["verification"]
assert verification["solver_free_replay"]["status"] == "PASS"
assert [verification["solver_free_replay"]["runs"], verification["solver_free_replay"]["comparisons"]] == [20, 35]
assert verification["repository_gates"]["status"] == "PASS" and verification["repository_gates"]["checks"] == 9
assert sha(R / verification["preseal_summary_path"]) == verification["preseal_summary_sha256"]
sci = r["scientific_status"]
assert sci["CIRCDIST.gross"] == sci["gap-via-lift"] == "CONJECTURED"
assert sci["D*_Gross"] == [11, 12]
assert not sci["root_closed"] and not sci["search_exhausted"] and not sci["interval_narrowed"]
assert sci["distance_12_witness"] is None and sci["universal_distance_at_most_11_theorem"] is None

failed = json.loads((R / "recovery_state/recovery/FAILED_ASSEMBLY1_INVENTORY.json").read_text())
assert failed["status"] == "PRESERVED_AND_HASH_BOUND"
assert failed["failed_tree_file_count"] == 333 and failed["failed_tree_total_bytes"] == 7603830923
assert failed["canonical_inventory_sha256"] == "50a13b8da91274e78ad7ea623e1fb8239fcfefeb98f7a5c7b0a44542e8e2513c"
assert failed["original_stderr"]["sha256"] == "ec345e341ac6ab0b3af113891d834b3e63cb64f08dcf41b8b8521c96207a99be"
assert sha(R / "logs/session_and_process/transcripts/assemble-round126-package-tree.stderr") == failed["original_stderr"]["sha256"]
assert sha(R / "source/assemble_package_tree_round126.failed1.py") == "72e881bca05b15c35cb3ee2644377ef24d18fdeadd917b3f56e00225f9997182"

report = (R / "REPORT.md").read_text()
for phrase in ("Both mandatory complete unrestricted direct-360 sectors", "zero UNSAT-certificate credit", "CHECKED_UNSTARTED", "CONJECTURED", "{11,12}"):
    assert phrase in report, phrase
failures = (R / "FAILURE_LEDGER.md").read_text()
for event in ("F126-R001", "F126-R002", "F126-R003", "F126-R004", "F126-R005", "F126-R006", "F126-R007", "F126-R008"):
    assert event in failures

out = {
    "schema": "circdist-gross-round126-result-check-v1", "status": "PASS",
    "result_sha256": sha(R / "RESULT.json"), "input_bindings_sha256": sha(R / "INPUT_BINDINGS.json"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"), "report_sha256": sha(R / "REPORT.md"),
    "outer_complete_assignment_and_all_clauses": True, "both_complete_direct360_sat_and_kill": True,
    "selector_lineage_sound_and_closed": True, "fresh_iter199_checked_unstarted": True,
    "scientific_boundary_preserved": True, "sat_stream_unsat_credit": 0,
    "failed_assembly_preserved_and_hash_bound": True,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
