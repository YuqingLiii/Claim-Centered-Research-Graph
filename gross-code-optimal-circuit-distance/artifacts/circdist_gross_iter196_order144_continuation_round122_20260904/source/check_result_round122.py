#!/usr/bin/env python3
"""Check all load-bearing Round122 result claims against packaged evidence."""
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
assert "KILLED_BY_BOTH_COMPLETE_DIRECT360_SECTORS" in r["verdict"]
for rel, digest in b["dispatch_hashes"].items():
    assert sha(R / rel) == digest
assert r["outer"]["status"] == "SATISFIABLE" and r["outer"]["exact_mandatory_formula"]
outer = r["outer"]["semantic_replay"]
assert outer["complete_assignment_variables"] == 4365826 and outer["dimacs_clauses_checked"] == 21362300
assert outer["all_dimacs_clauses_satisfied"] and outer["reviewed_block_hits"] == 0
assert outer["efssc_named_frozen_valid_selectors"] == outer["efssc_symbolic_valid_selectors"] == 0
assert r["direct360"]["scope"].startswith("two complete unrestricted direct-360")
for label, expected in {"Xerr": (6124, 23076), "Zerr": (6126, 23084)}.items():
    s = r["direct360"]["sectors"][label]
    assert s["status"] == "SATISFIABLE" and s["variables"] == expected[0] and s["clauses"] == expected[1]
    assert s["fault_count"] == 10 and s["all_columns_reconstructed"] == 360
    assert s["all_clauses_checked"] == expected[1] and s["all_clauses_satisfied"]
    assert s["canonical_syndrome"] == s["physical_syndrome"] == []
    assert any(s["logical_parities"]) and s["canonical_nonstabilizer"] and s["physical_nonstabilizer"]
    assert len(s["selected_names"]) == 10
assert r["selector_lineage"]["all_physical_group_element_replays"] == 288
assert r["selector_lineage"]["distinct_installed_selectors"] == 216
assert [r["selector_lineage"]["original_orbits"][x]["size"] for x in ("Xerr", "Zerr")] == [36, 72]
assert [x["size"] for x in r["selector_lineage"]["css_dual_orbits"]] == [36, 72]
assert f["iteration"] == 197 and not f["started"] and f["solver_invocations"] == 0
assert [f["blocks"], f["selectors"], f["assertions"]] == [814392, 51552, 870342]
assert f["base"] == {"sha256": "f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3", "variables": 3140244, "clauses": 11511680}
assert f["order144_quotient"] == {"sha256": "fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334", "variables": 4375764, "clauses": 21395983, "roots": 143}
assert sha(R / "frontier/iter197/source.json.gz") == f["source_sha256"]
assert sha(R / "frontier/iter197/state.json") == f["state_sha256"]
assert sha(R / "frontier/iter197/CHECKED_UNSTARTED.json") == f["checked_unstarted_sha256"]
for label, d in r["sat_search_traces"].items():
    assert d["classification"] == "SAT_SEARCH_TRACE" and d["unsat_certificate_credit"] == 0
    assert d["proof_output_enabled_from_byte_zero"]
    assert sha(R / d["package_gzip_path"]) == d["gzip_sha256"]
sci = r["scientific_status"]
assert sci["CIRCDIST.gross"] == sci["gap-via-lift"] == "CONJECTURED"
assert sci["D*_Gross"] == [11, 12]
assert not sci["root_closed"] and not sci["search_exhausted"] and not sci["interval_narrowed"]
assert sci["distance_12_witness"] is None and sci["universal_distance_at_most_11_theorem"] is None
report = (R / "REPORT.md").read_text()
for phrase in ("Both mandatory complete unrestricted direct-360 sectors", "zero UNSAT-certificate credit", "CHECKED_UNSTARTED", "CONJECTURED", "{11,12}"):
    assert phrase in report, phrase
out = {
    "schema": "circdist-gross-round122-result-check-v1", "status": "PASS",
    "result_sha256": sha(R / "RESULT.json"), "input_bindings_sha256": sha(R / "INPUT_BINDINGS.json"),
    "fresh_frontier_sha256": sha(R / "FRESH_FRONTIER.json"), "report_sha256": sha(R / "REPORT.md"),
    "outer_complete_assignment_and_all_clauses": True, "both_complete_direct360_sat_and_kill": True,
    "selector_lineage_sound_and_closed": True, "fresh_iter197_checked_unstarted": True,
    "scientific_boundary_preserved": True, "sat_stream_unsat_credit": 0,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
