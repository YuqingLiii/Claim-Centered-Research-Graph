#!/usr/bin/env python3
"""Verify that Round106 did not alter the protected scheduler/proof-DAG inputs."""
from pathlib import Path
import argparse
import hashlib
import json

EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "89767aecd57e32608cc75010c26a5d415af3330964c42e572aefed86796c259b",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae",
    "circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md": "01d14be78fc75362c16340b4ba32df783a645084a819fc18a96f432d9a45e932",
    "circdist/artifacts/circdist_gross_iter187_invariant_continuation_round104_20260901/SHA256SUMS.txt": "410807a787005a0fb5ebb1753f8b75712c798d9a15e9101f1265d0be25206ebb",
}
STORED = {
    "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md": "bindings/round105_review.md",
    "circdist/artifacts/circdist_gross_iter187_invariant_continuation_round104_20260901/SHA256SUMS.txt": "bindings/round104_SHA256SUMS.txt",
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repository", type=Path, required=True)
    ap.add_argument("--package", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    repo, package = args.repository.resolve(), args.package.resolve()
    rows = []
    for rel, expected in EXPECTED.items():
        live = (repo / rel).read_bytes()
        stored = (package / STORED[rel]).read_bytes()
        assert live == stored and sha(live) == expected
        rows.append({"path": rel, "stored_path": STORED[rel], "sha256": expected,
                     "bytes": len(live), "lf": live.count(b"\n")})
    scheduler = (repo / "operations/circdist/SCHEDULER.yaml").read_text()
    gross = (repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml").read_text()
    assert "round 106 authorized and pending" in scheduler
    assert "Budget remains 131/132 until settlement" in scheduler
    assert "level: CONJECTURED" in gross
    assert "D*_Gross in {11,12}" in gross
    result = {"schema": "circdist-gross-round106-live-governance-check-v1",
              "status": "PASS", "rows": rows, "files_checked": len(rows),
              "round106_dispatch_state": "pending, unspent, 131/132",
              "gross_status": "CONJECTURED", "gross_residual": [11, 12],
              "canonical_files_unchanged": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
