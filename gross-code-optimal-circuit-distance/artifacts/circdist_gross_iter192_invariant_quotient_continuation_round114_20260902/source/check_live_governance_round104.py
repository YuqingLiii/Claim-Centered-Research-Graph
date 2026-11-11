#!/usr/bin/env python3
"""Verify that Round104 did not alter the protected scheduler/proof-DAG inputs."""
from pathlib import Path
import argparse
import hashlib
import json

EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "d9bcb7affe40ed12a479785f5a102673108b4322fe0d20a1cf6da4483069c31f",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "dd367bf93e59e10588a824d4f530a0b07c3707d43886004bb3ddb754f0ff7d91",
    "circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md": "a7e027b228d785fae5280b33ab95f7999bb4e9b3e001cd30a5816444637db48e",
    "circdist/artifacts/circdist_gross_global_closure_round102_20260901/SHA256SUMS.txt": "80e70f62075a852355029b765cbe7ebfa4f8156d25b6d9fa2ea1ddbb9e19b4f4",
}
STORED = {
    "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md": "bindings/round103_review.md",
    "circdist/artifacts/circdist_gross_global_closure_round102_20260901/SHA256SUMS.txt": "inputs/round102/SHA256SUMS.txt",
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
    assert "round 104 authorized and pending" in scheduler
    assert "Budget remains 129/130 until settlement" in scheduler
    assert "level: CONJECTURED" in gross
    assert "D*_Gross in {11,12}" in gross
    result = {"schema": "circdist-gross-round104-live-governance-check-v1",
              "status": "PASS", "rows": rows, "files_checked": len(rows),
              "round104_dispatch_state": "pending, unspent, 129/130",
              "gross_status": "CONJECTURED", "gross_residual": [11, 12],
              "canonical_files_unchanged": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
