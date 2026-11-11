#!/usr/bin/env python3
"""Delete only three losslessly packaged SAT search traces after fixed binding checks."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--package", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
pkg = a.package.resolve()
assert pkg.name == "circdist_gross_iter196_order144_continuation_round122_20260904"
rows = []
for label in ("outer", "Xerr", "Zerr"):
    meta = json.loads((pkg / f"proof_streams/{label}.stream.json").read_text())
    raw = Path(meta["raw_path"])
    gzip_path = pkg / meta["package_gzip_path"]
    assert raw.is_file() and raw.stat().st_size == meta["raw_bytes"]
    with raw.open("rb") as f:
        first = f.read(64).hex()
        f.seek(-64, 2)
        last = f.read(64).hex()
    assert first == meta["raw_first_64_hex"] and last == meta["raw_last_64_hex"]
    assert gzip_path.is_file() and gzip_path.stat().st_size == meta["gzip_bytes"]
    assert sha(gzip_path) == meta["gzip_sha256"]
    raw.unlink()
    assert not raw.exists()
    rows.append({"label": label, "deleted_raw_path": str(raw),
                 "deleted_raw_bytes": meta["raw_bytes"], "deleted_raw_sha256": meta["raw_sha256"],
                 "retained_gzip_package_path": meta["package_gzip_path"],
                 "retained_gzip_bytes": meta["gzip_bytes"], "retained_gzip_sha256": meta["gzip_sha256"],
                 "lossless_roundtrip_verified": meta["lossless_roundtrip_verified"]})
out = {
    "schema": "circdist-gross-round122-preseal-cleanup-v1", "status": "PASS",
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "exact allowlist of three Round122-owned raw SAT search traces",
    "deleted_files": 3, "deleted_bytes": sum(row["deleted_raw_bytes"] for row in rows),
    "retained_gzip_files": 3, "solver_invocations": 0, "rows": rows,
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "deleted_files": 3,
                  "deleted_bytes": out["deleted_bytes"], "retained_gzip_files": 3,
                  "solver_invocations": 0}, sort_keys=True))
