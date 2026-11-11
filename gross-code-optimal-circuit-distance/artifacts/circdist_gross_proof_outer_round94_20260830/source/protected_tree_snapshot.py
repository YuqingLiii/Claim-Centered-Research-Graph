#!/usr/bin/env python3
"""Hash all protected canonical/review/protocol/tool paths and prior seals."""
from pathlib import Path
import argparse
import hashlib
import json


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.repository.resolve()
package_name = "circdist_gross_proof_outer_round94_20260830"
files = set()
for rel in ("circdist/proof-dag/nodes", "circdist/reviews", "tools"):
    files.update(path for path in (R / rel).rglob("*") if path.is_file())
for rel in ("operations/circdist/SCHEDULER.yaml", "DAG_PROTOCOL.md", "FILE_PROTOCOL.md"):
    files.add(R / rel)
for path in (R / "circdist/artifacts").glob("*/SHA256SUMS.txt"):
    if package_name not in path.parts:
        files.add(path)
for path in (R / "circdist/artifacts").glob("*/PAYLOAD_SHA256SUMS.txt"):
    if package_name not in path.parts:
        files.add(path)
rows = []
for path in sorted(files):
    assert path.is_file(), path
    rows.append({"path": path.relative_to(R).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)})
out = {
    "schema": "circdist-round94-protected-tree-snapshot-v1", "status": "PASS",
    "file_count": len(rows), "rows": rows,
    "scope": "all canonical node files, all reviews, scheduler, protocols, tools, and every prior package root/payload seal file",
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "file_count": len(rows)}, sort_keys=True))
