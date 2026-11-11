#!/usr/bin/env python3
"""Deterministically gzip bulky Round100 text evidence, preserving content bytes."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import time


def sha256(data):
    return hashlib.sha256(data).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()

targets = []
for iteration in range(172, 185):
    formula = R / "formulas" / f"iter{iteration}"
    targets.extend((formula / "outer.cnf", formula / "assertion_map.jsonl"))
for iteration in range(172, 184):
    item = R / "iterations" / f"iter{iteration}"
    targets.extend((
        item / "outer/solver.log",
        item / "outer/assignment.dimacs",
        item / "outer/assignment.independent.dimacs",
    ))
    for sector in ("Xerr", "Zerr"):
        direct = item / "direct/direct360"
        for suffix in ("cnf", "variables.json", "columns.json", "clauses.jsonl"):
            targets.append(direct / f"{sector}.{suffix}")
        targets.extend((
            item / "direct/solver" / f"{sector}.solver.log",
            item / "direct/solver" / f"{sector}.assignment.dimacs",
        ))
for sector in ("Xerr", "Zerr"):
    span = R / "synthesis/span"
    targets.extend((span / f"{sector}.cnf", span / f"{sector}.drat",
                    span / f"{sector}.solver.log"))
    certificate = span / f"{sector}.unsat_certificate"
    for name in ("accepted.lrat", "corrupt.drat", "truncated.drat",
                 "corrupt.lrat", "truncated.lrat"):
        targets.append(certificate / name)

assert len(targets) == len(set(targets)), "compression target duplicated"
rows = []
for path in targets:
    encoded_path = path.with_name(path.name + ".gz")
    if path.exists():
        raw = path.read_bytes()
        encoded = gzip.compress(raw, compresslevel=9, mtime=0)
        if encoded_path.exists():
            assert gzip.decompress(encoded_path.read_bytes()) == raw
            encoded = encoded_path.read_bytes()
        else:
            encoded_path.write_bytes(encoded)
        path.unlink()
    else:
        assert encoded_path.is_file(), path
        encoded = encoded_path.read_bytes()
        raw = gzip.decompress(encoded)
    assert gzip.decompress(encoded) == raw
    rows.append({
        "source_path": path.relative_to(R).as_posix(),
        "stored_path": encoded_path.relative_to(R).as_posix(),
        "content_bytes": len(raw),
        "stored_bytes": len(encoded),
        "content_sha256": sha256(raw),
        "stored_sha256": sha256(encoded),
        "content_lf": raw.count(b"\n"),
        "mtime": 0,
        "compresslevel": 9,
    })

record = {
    "schema": "circdist-round100-deterministic-compression-v1",
    "status": "PASS",
    "created_unix": time.time(),
    "files_compressed": len(rows),
    "content_bytes": sum(row["content_bytes"] for row in rows),
    "stored_bytes": sum(row["stored_bytes"] for row in rows),
    "all_roundtrips_byte_identical": True,
    "all_targets_present_exactly_once": True,
    "rows": rows,
}
(R / "verification").mkdir(exist_ok=True)
(R / "verification/compression.json").write_text(
    json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: record[key] for key in
                  ("status", "files_compressed", "content_bytes", "stored_bytes")},
                 sort_keys=True))
