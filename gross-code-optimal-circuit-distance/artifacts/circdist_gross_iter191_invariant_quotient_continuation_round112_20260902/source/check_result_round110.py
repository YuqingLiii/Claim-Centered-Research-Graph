#!/usr/bin/env python3
"""Assert the honest Round110 result and exact residual."""
from pathlib import Path
import argparse
import hashlib
import json


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args(); root = args.root.resolve()
    result = json.loads((root / "RESULT.json").read_text())
    assert result["status"] == "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED"
    assert result["root_closed"] is False
    assert result["root_branch_A_closed"] is False and result["root_branch_B_closed"] is False
    assert result["distance_status"] == {"CIRCDIST.gross": "CONJECTURED", "gap-via-lift": "CONJECTURED", "D_star_Gross": [11, 12]}
    assert result["iteration190"]["quotient"]["status"] == "SATISFIABLE"
    assert result["iteration190"]["quotient"]["all_clauses_satisfied"] is True
    assert result["iteration190"]["candidate_excluded"] is True
    assert result["iteration190"]["repair_entered"] is False
    assert all(result["iteration190"]["direct"][s]["status"] == "SATISFIABLE" for s in ("Xerr", "Zerr"))
    assert all(result["iteration190"]["direct"][s]["fault_count"] == 10 for s in ("Xerr", "Zerr"))
    assert result["orbit_continuation"]["old_selectors"] == 24444
    assert result["orbit_continuation"]["added_selectors"] == 144
    assert result["orbit_continuation"]["new_selectors"] == 24588
    assert result["orbit_continuation"]["collisions"] == 0
    assert result["fresh_frontier"]["iteration"] == 191 and result["fresh_frontier"]["fresh_unstarted"]
    assert result["proof_disposition"]["actual_Gross_UNSAT"] is False
    assert result["proof_disposition"]["sat_streams_are_search_traces_not_certificates"] is True
    assert result["proposed_canonical_yaml"]["identical_to_bound_canonical"] is True
    assert sha(root / "PROPOSED_CIRCDIST.gross.yaml") == "7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b"
    checked = {"schema": "circdist-gross-round110-result-check-v1", "status": "PASS",
               "root_closed": False, "branches_closed": [], "canonical_level": "CONJECTURED",
               "interval": [11, 12], "iteration190_solver_outcomes": ["SAT", "SAT", "SAT"],
               "fresh_iteration": 191, "fresh_unstarted": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(checked, indent=2, sort_keys=True) + "\n")
    print(json.dumps(checked, sort_keys=True))


if __name__ == "__main__":
    main()
