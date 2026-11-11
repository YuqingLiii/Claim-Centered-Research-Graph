#!/usr/bin/env python3
"""Verify Round110 did not alter bound live governance or predecessor seal."""
from pathlib import Path
import argparse
import hashlib
import json

EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "beefafeee1608dda1eadfe0e82b920f7148bd2dfc12e93c52c6b48ff69e74aed",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b",
    "circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md": "0d31152bc03ca8066a7ffeaf885730b51ff2c55a3634819fc68d9fcbcd26dd82",
    "circdist/artifacts/circdist_gross_iter189_invariant_quotient_continuation_round108_20260901/SHA256SUMS.txt": "6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0",
}
STORED = {
    "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md": "bindings/round109_review.md",
    "circdist/artifacts/circdist_gross_iter189_invariant_quotient_continuation_round108_20260901/SHA256SUMS.txt": "bindings/round108_SHA256SUMS.txt",
}


def digest(raw): return hashlib.sha256(raw).hexdigest()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repository", type=Path, required=True)
    ap.add_argument("--package", type=Path, required=True); ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args(); repo, package = args.repository.resolve(), args.package.resolve()
    rows = []
    for rel, expected in EXPECTED.items():
        live, stored = (repo / rel).read_bytes(), (package / STORED[rel]).read_bytes()
        assert live == stored and digest(live) == expected
        rows.append({"path": rel, "stored_path": STORED[rel], "sha256": expected,
                     "bytes": len(live), "lf": live.count(b"\n")})
    scheduler = (repo / "operations/circdist/SCHEDULER.yaml").read_text()
    gross = (repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml").read_text()
    assert "round 110 resumes the cleared fresh iteration-190 invariant quotient" in scheduler
    assert "total_sessions: 136" in scheduler and "spent_sessions: 135.0" in scheduler
    assert "level: CONJECTURED" in gross and "D*_Gross in {11,12}" in gross
    result = {"schema": "circdist-gross-round110-live-governance-check-v1", "status": "PASS",
              "rows": rows, "files_checked": 4, "round110_dispatch_state": "pending, unspent, 135/136",
              "gross_status": "CONJECTURED", "gross_residual": [11, 12], "canonical_files_unchanged": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__": main()
