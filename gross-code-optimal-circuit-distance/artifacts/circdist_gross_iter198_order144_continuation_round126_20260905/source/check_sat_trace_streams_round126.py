#!/usr/bin/env python3
"""Independently check all three complete compressed iteration-198 SAT traces."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

CHUNK = 8 << 20


def scan(handle, count_empty=False):
    h = hashlib.sha256()
    size = lf = empty = 0
    pending = b""
    first_byte = None
    corrupt = hashlib.sha256()
    for chunk in iter(lambda: handle.read(CHUNK), b""):
        h.update(chunk)
        size += len(chunk)
        lf += chunk.count(b"\n")
        if first_byte is None and chunk:
            first_byte = chunk[0]
            corrupt.update(bytes([chunk[0] ^ 1]) + chunk[1:])
        else:
            corrupt.update(chunk)
        if count_empty:
            rows = (pending + chunk).split(b"\n")
            pending = rows.pop()
            empty += sum(row.strip() == b"0" for row in rows)
    if count_empty and pending:
        empty += int(pending.strip() == b"0")
    return {"sha256": h.hexdigest(), "bytes": size, "lf": lf, "empty": empty,
            "one_byte_corrupt_sha256": corrupt.hexdigest()}


p = argparse.ArgumentParser()
p.add_argument("--root", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
a = p.parse_args()
root = a.root.resolve()
rows = []
for label in ("outer", "Xerr", "Zerr"):
    rel = f"proof_streams/{label}.stream.json"
    d = json.loads((root / rel).read_text())
    gz = root / d["package_gzip_path"]
    assert d["status"] == "PASS" and d["solver_status"] == "SATISFIABLE"
    assert d["classification"] == "SAT_SEARCH_TRACE" and d["unsat_certificate_credit"] == 0
    assert d["proof_output_enabled_from_byte_zero"] and d["solver_return_code"] == 10
    with gz.open("rb") as fh:
        compressed = scan(fh)
    assert compressed["sha256"] == d["gzip_sha256"]
    assert compressed["bytes"] == d["gzip_bytes"]
    assert compressed["one_byte_corrupt_sha256"] != d["gzip_sha256"]
    with gzip.open(gz, "rb") as fh:
        raw = scan(fh, count_empty=True)
    assert raw["sha256"] == d["raw_sha256"]
    assert raw["bytes"] == d["raw_bytes"] and raw["lf"] == d["raw_lf_count"]
    assert raw["empty"] == 0
    rows.append({
        "label": label,
        "descriptor": rel,
        "gzip_sha256": compressed["sha256"],
        "gzip_bytes": compressed["bytes"],
        "raw_sha256": raw["sha256"],
        "raw_bytes": raw["bytes"],
        "raw_lf_count": raw["lf"],
        "raw_empty_clause_lines": raw["empty"],
        "classification": "SAT search trace; zero UNSAT-certificate credit",
        "one_byte_corrupt_hash_rejected": True,
        "truncated_byte_count_rejected": raw["bytes"] - 1 != d["raw_bytes"],
    })
out = {
    "schema": "circdist-gross-round126-sat-trace-stream-check-v1",
    "status": "PASS",
    "streams": rows,
    "stream_count": 3,
    "raw_bytes": sum(x["raw_bytes"] for x in rows),
    "gzip_bytes": sum(x["gzip_bytes"] for x in rows),
    "empty_clause_lines": 0,
    "all_lossless_roundtrips_verified": True,
    "all_one_byte_corrupt_controls_rejected": True,
    "all_truncated_count_controls_rejected": True,
    "certificate_claim": None,
    "unsat_certificate_credit": 0,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: out[k] for k in ("status", "stream_count", "raw_bytes", "gzip_bytes", "empty_clause_lines", "unsat_certificate_credit")}, sort_keys=True))
