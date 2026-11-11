#!/usr/bin/env python3
"""Verify Round108 did not alter scheduler, canonical Gross, review, or predecessor seal."""
from pathlib import Path
import argparse
import hashlib
import json

EXPECTED = {
    "operations/circdist/SCHEDULER.yaml": "13c74772427b20aaf8128633459ee995c62e60dd1b79090c458d00e9a0994343",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977",
    "circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md": "eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036",
    "circdist/artifacts/circdist_gross_iter188_invariant_quotient_continuation_round106_20260901/SHA256SUMS.txt": "0b9cc6d4074e8397062219ec8d079afbcf0388e14912ab925b5d66ac00c61c9d",
}
STORED = {
    "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md": "bindings/round107_review.md",
    "circdist/artifacts/circdist_gross_iter188_invariant_quotient_continuation_round106_20260901/SHA256SUMS.txt": "bindings/round106_SHA256SUMS.txt",
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
    assert "round 108 authorized and pending" in scheduler
    assert "Budget remains 133/134 until settlement" in scheduler
    assert "level: CONJECTURED" in gross
    assert "D*_Gross in {11,12}" in gross
    result = {"schema": "circdist-gross-round108-live-governance-check-v1",
              "status": "PASS", "rows": rows, "files_checked": len(rows),
              "round108_dispatch_state": "pending, unspent, 133/134",
              "gross_status": "CONJECTURED", "gross_residual": [11, 12],
              "canonical_files_unchanged": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
