#!/usr/bin/env python3
"""Copy and hash the read-only governance inputs used by Round102."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("--repository", type=Path, required=True)
parser.add_argument("--package", type=Path, required=True)
args = parser.parse_args()
repository = args.repository.resolve()
package = args.package.resolve()
destination = package / "bindings" / "live_governance"

paths = [
    "operations/circdist/SCHEDULER.yaml",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml",
    "circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md",
    "DAG_PROTOCOL.md",
    "FILE_PROTOCOL.md",
    "tools/proof_dag_schema.py",
    "tools/proof_dag_check.py",
    "tools/evidence_closure_check.py",
    "tools/check_circdist_migration.py",
    "tools/test_release_contracts.py",
    "tools/test_dag_contracts.py",
    "tools/lean_dag_check.py",
]
expected = {
    "operations/circdist/SCHEDULER.yaml": "02cb4b7a02963451adf962dfc59fa3eb11ef8f71d7b2b2c49d89e6bc61e2c8f5",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "09290d2fb1d4f3c97e0ce503f9f5750a090df1b34b0114dcc9c6542733476dd4",
    "circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md": "8eb817e0af24df1d17af5cdd778cfa7180a1c6c60ca6c87d81ad3c5ad549ca88",
}

rows = []
for relative in paths:
    source = repository / relative
    assert source.is_file(), relative
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if relative in expected:
        assert digest == expected[relative], (relative, digest)
    stored = destination / relative
    stored.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, stored)
    assert stored.read_bytes() == raw
    rows.append({
        "original_path": relative,
        "stored_path": stored.relative_to(package).as_posix(),
        "sha256": digest,
        "bytes": len(raw),
        "lf": raw.count(b"\n"),
    })

result = {
    "schema": "circdist-gross-round102-live-governance-bindings-v1",
    "status": "PASS",
    "rows": rows,
    "file_count": len(rows),
    "scope": "scheduler, Gross canonical node, commissioned review, protocols, schema, and repository gate tools; all copied read-only",
}
(package / "bindings" / "LIVE_GOVERNANCE.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "file_count": len(rows)}, sort_keys=True))
