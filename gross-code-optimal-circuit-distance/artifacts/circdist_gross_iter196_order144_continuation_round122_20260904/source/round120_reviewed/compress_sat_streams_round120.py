#!/usr/bin/env python3
"""Retain complete SAT-side proof-output streams as deterministic gzip."""
import argparse, gzip, hashlib, json, os, shutil
from pathlib import Path

CHUNK = 8 << 20


def scan(handle):
    digest = hashlib.sha256(); size = lf = empty = 0; pending = b""
    for chunk in iter(lambda: handle.read(CHUNK), b""):
        digest.update(chunk); size += len(chunk); lf += chunk.count(b"\n")
        rows = (pending + chunk).split(b"\n"); pending = rows.pop()
        empty += sum(row.strip() == b"0" for row in rows)
    if pending:
        empty += int(pending.strip() == b"0")
    return digest.hexdigest(), size, lf, empty


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("paths", nargs="+")
a = ap.parse_args()
rows = []
for relative in a.paths:
    source = a.root / relative
    assert source.is_file() and source.suffix == ".drat"
    with source.open("rb") as f:
        raw_sha, raw_bytes, raw_lf, raw_empty = scan(f)
    output = source.with_suffix(source.suffix + ".gz")
    temporary = output.with_suffix(output.suffix + ".tmp")
    with source.open("rb") as inp, temporary.open("wb") as raw_out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out,
                           compresslevel=9, mtime=0) as encoded:
            shutil.copyfileobj(inp, encoded, CHUNK)
    os.replace(temporary, output)
    with gzip.open(output, "rb") as f:
        check = scan(f)
    assert check == (raw_sha, raw_bytes, raw_lf, raw_empty)
    with output.open("rb") as f:
        gzip_sha, gzip_bytes, _, _ = scan(f)
    row = {
        "schema": "circdist-gross-round120-sat-proof-output-stream-v1",
        "status": "PASS", "query": relative,
        "solver_status": "SATISFIABLE", "proof_output_enabled_from_start": True,
        "certificate_disposition": "complete SAT-side proof output; search trace only; not a DRAT/LRAT UNSAT certificate",
        "raw_sha256": raw_sha, "raw_bytes": raw_bytes, "raw_lf_count": raw_lf,
        "raw_empty_clause_lines": raw_empty,
        "gzip_path": str(output.relative_to(a.root)), "gzip_sha256": gzip_sha,
        "gzip_bytes": gzip_bytes, "lossless_roundtrip_verified": True,
    }
    source.with_suffix(source.suffix + ".stream.json").write_text(
        json.dumps(row, indent=2, sort_keys=True) + "\n")
    source.unlink(); rows.append(row)
print(json.dumps({"status":"PASS", "streams":len(rows),
                  "raw_bytes":sum(r["raw_bytes"] for r in rows),
                  "gzip_bytes":sum(r["gzip_bytes"] for r in rows),
                  "empty_clause_lines":sum(r["raw_empty_clause_lines"] for r in rows)}, sort_keys=True))
