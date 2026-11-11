#!/usr/bin/env python3
"""Build both complete unrestricted direct-360 sector CNFs from an audited outer candidate."""
from pathlib import Path
import argparse
import hashlib
import json
import sys


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--vendor", type=Path, required=True)
    parser.add_argument("--source-selector-count", type=int, required=True)
    args = parser.parse_args()

    vendor = args.vendor.resolve()
    sys.path[:0] = [str(vendor / "src" / "round63_src"), str(vendor / "src")]
    import model as model
    import round68_build as builder

    outer = json.loads(args.candidate.read_text())
    times = {str(k): int(v) for k, v in outer["compressed_times"].items()}
    assert canonical_sha256(times) == outer["compressed_schedule_sha256"]
    audit = model.audit_schedule(times, True)
    assert audit["ok"] and audit["global_interleaved"]
    assert audit == outer["frozen_audit"]

    args.output.mkdir(parents=True, exist_ok=True)
    direct_candidate = {
        "schema": "round90-proof-outer-direct-candidate-v1",
        "schedule_times": times,
        "schedule_sha256": canonical_sha256(times),
        "audit": audit,
        "source_outer_formula_sha256": outer["cnf_sha256"],
        "existing_blocks_avoided": 14484,
        "efssc_cuts_avoided": args.source_selector_count,
    }
    (args.output / "candidate.json").write_text(
        json.dumps(direct_candidate, indent=2, sort_keys=True) + "\n"
    )

    _, _, logical_x, logical_z = builder.load_context()
    sectors = builder.sectors(times, logical_x, logical_z)
    summaries = {}
    for label in ("Xerr", "Zerr"):
        summaries[label] = builder.build_direct_cnf(
            sectors[label],
            args.output / "direct360" / label,
            direct_candidate["schedule_sha256"],
            10,
        )
    result = {
        "schema": "round90-direct360-build-v1",
        "status": "PASS",
        "candidate_sha256": direct_candidate["schedule_sha256"],
        "source_selector_count": args.source_selector_count,
        "sectors": summaries,
    }
    (args.output / "build_summary.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
