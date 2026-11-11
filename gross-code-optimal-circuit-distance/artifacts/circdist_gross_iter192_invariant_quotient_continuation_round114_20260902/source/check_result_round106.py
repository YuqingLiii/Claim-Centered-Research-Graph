#!/usr/bin/env python3
"""Cross-check the Round106 machine verdict against retained primary evidence."""
from pathlib import Path
import argparse
import hashlib
import json
import os


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
args = ap.parse_args()
root = args.root.resolve()
result = json.loads((root / "RESULT.json").read_text())
assert result["verdict"] == "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED"
assert result["root_closed"] is False and result["canonical_state_modified"] is False
assert result["distance_status"] == {"CIRCDIST.gross": "CONJECTURED",
                                     "D_star_Gross": [11, 12],
                                     "gap-via-lift": "CONJECTURED"}
assert result["root_branches"] == {
    "A_explicit_legal_distance_12_circuit": False,
    "B_universal_frozen_family_distance_at_most_11": False}
for path in ("solver/iter188/assignment_check.json",
             "solver/iter188/direct/solver/Xerr.assignment_check.json",
             "solver/iter188/direct/solver/Zerr.assignment_check.json"):
    row = json.loads((root / path).read_text())
    assert row["status"] == "PASS" and row["solver_status"] == "SATISFIABLE"
    assert row["all_dimacs_clauses_satisfied"]
direct = json.loads((root / "verification/iter188_direct_independent_audit.json").read_text())
assert direct["status"] == "PASS"
assert all(direct["sectors"][sector]["status"] == "SATISFIABLE" for sector in ("Xerr", "Zerr"))
assert all(direct["sectors"][sector]["fault_count"] == 10 for sector in ("Xerr", "Zerr"))
assert all(direct["sectors"][sector]["physical_nonstabilizer"] for sector in ("Xerr", "Zerr"))
state = json.loads((root / "frontier/iter189_full_invariant/state.json").read_text())
assert state["started"] is False and state["next_iteration"] == 189 and state["stop"] is None
qdir = root / "frontier/iter189_full_invariant_quotient"
expected = {"independent_check.json", "metadata.json", "outer.cnf",
            "translation_roots.jsonl", "translation_trace.json.gz"}
assert {p.name for p in qdir.iterdir()} == expected
qmeta = json.loads((qdir / "metadata.json").read_text())
assert (qmeta["variables"], qmeta["clauses"], qmeta["cnf_sha256"]) == (
    2460741, 11816927, "3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7")
assert sha(qdir / "outer.cnf") == qmeta["cnf_sha256"]
assert json.loads((qdir / "independent_check.json").read_text())["status"] == "PASS"
assert json.loads((root / "verification/iter189_incremental_orbit_closure_independent.json").read_text())["status"] == "PASS"
assert json.loads((root / "controls/proof_toolchain_controls.json").read_text())["status"] == "PASS"
assert json.loads((root / "verification/preseal_replay.json").read_text())["status"] == "PASS"
assert json.loads((root / "verification/postseal_replay.json").read_text())["status"] == "PASS"
assert json.loads((root / "verification/repository_validators/summary.json").read_text())["status"] == "PASS"
assert json.loads((root / "PROCESS_FIX2_LEDGER.json").read_text())["status"] == "PASS"
assert sha(root / "PROPOSED_CIRCDIST.gross.yaml") == sha(root / "bindings/CIRCDIST.gross.yaml") == \
    "3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae"
assert os.access(root / "replay.sh", os.X_OK)
symlinks = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
assert not symlinks
for name in ("REPORT.md", "THEOREM_NOTES.md", "FAILURE_LEDGER.md",
             "INPUT_BINDINGS.json", "ENVIRONMENT.json", "FRESH_FRONTIER.json",
             "PROCESS_FIX2_LEDGER.json", "PROPOSED_CANONICAL_DELTA.md"):
    assert (root / name).is_file() and (root / name).stat().st_size > 0
out = {"schema": "circdist-gross-round106-result-consistency-check-v1",
       "status": "PASS", "verdict": result["verdict"], "root_closed": False,
       "solver_statuses": {"outer": "SATISFIABLE", "Xerr": "SATISFIABLE", "Zerr": "SATISFIABLE"},
       "fresh_iteration": 189, "fresh_quotient_sha256": qmeta["cnf_sha256"],
       "canonical_yaml_unchanged": True, "symlink_count": 0}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
