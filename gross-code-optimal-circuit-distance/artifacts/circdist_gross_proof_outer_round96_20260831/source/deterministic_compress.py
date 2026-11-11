#!/usr/bin/env python3
"""Deterministically gzip bulky retained SAT evidence without changing payload bytes."""
from pathlib import Path
import argparse, gzip, hashlib, json, time

ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()

targets = []
for i in range(148, 161):
    F = R / "formulas" / f"iter{i}"
    targets += [F / "outer.cnf", F / "assertion_map.jsonl"]
for name in ("fresh.outer.cnf", "stored.outer.cnf", "fresh.assertion_map.jsonl", "stored.assertion_map.jsonl"):
    targets.append(R / "reconstruction" / name)
for i in range(148, 160):
    I = R / "iterations" / f"iter{i}"
    targets += [I / "outer/solver.log", I / "outer/assignment.dimacs", I / "outer/assignment.independent.dimacs"]
    D = I / "direct/direct360"
    for sector in ("Xerr", "Zerr"):
        for suffix in ("cnf", "variables.json", "columns.json", "clauses.jsonl"):
            targets.append(D / f"{sector}.{suffix}")

rows = []
for path in targets:
    if not path.exists():
        # Iter148 outer/map were inherited already gzip-compressed.
        assert path.with_name(path.name + ".gz").is_file(), path
        continue
    assert path.is_file() and path.suffix != ".gz"
    raw = path.read_bytes()
    encoded = gzip.compress(raw, compresslevel=9, mtime=0)
    out = path.with_name(path.name + ".gz")
    assert not out.exists(), out
    out.write_bytes(encoded)
    assert gzip.decompress(encoded) == raw
    rows.append({
        "source_path": path.relative_to(R).as_posix(),
        "stored_path": out.relative_to(R).as_posix(),
        "content_bytes": len(raw), "stored_bytes": len(encoded),
        "content_sha256": hashlib.sha256(raw).hexdigest(),
        "stored_sha256": hashlib.sha256(encoded).hexdigest(),
        "content_lf": raw.count(b"\n"), "mtime": 0, "compresslevel": 9,
    })
    path.unlink()

record = {
    "schema": "circdist-round96-deterministic-compression-v1", "status": "PASS",
    "created_unix": time.time(), "files_compressed": len(rows),
    "content_bytes": sum(x["content_bytes"] for x in rows),
    "stored_bytes": sum(x["stored_bytes"] for x in rows),
    "all_roundtrips_byte_identical": True, "rows": rows,
}
(R / "verification").mkdir(exist_ok=True)
(R / "verification/compression.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({k:record[k] for k in ("status","files_compressed","content_bytes","stored_bytes")}, sort_keys=True))
