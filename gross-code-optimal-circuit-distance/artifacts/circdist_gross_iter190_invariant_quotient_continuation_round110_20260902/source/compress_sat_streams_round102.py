#!/usr/bin/env python3
"""Losslessly retain complete SAT-side proof-output streams as deterministic gzip."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import shutil


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("paths", nargs="+")
args = parser.parse_args()


def digest_stream(handle):
    sha = hashlib.sha256()
    size = 0
    lf = 0
    for chunk in iter(lambda: handle.read(1 << 20), b""):
        sha.update(chunk)
        size += len(chunk)
        lf += chunk.count(b"\n")
    return sha.hexdigest(), size, lf


rows = []
for relative in args.paths:
    source = args.root / relative
    assert source.is_file() and source.suffix == ".drat"
    with source.open("rb") as handle:
        raw_sha, raw_bytes, raw_lf = digest_stream(handle)
    output = source.with_suffix(source.suffix + ".gz")
    temporary = output.with_suffix(output.suffix + ".tmp")
    with source.open("rb") as inp, temporary.open("wb") as raw_out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out,
                           compresslevel=9, mtime=0) as encoded:
            shutil.copyfileobj(inp, encoded, 1 << 20)
    os.replace(temporary, output)
    with gzip.open(output, "rb") as handle:
        check_sha, check_bytes, check_lf = digest_stream(handle)
    assert (check_sha, check_bytes, check_lf) == (raw_sha, raw_bytes, raw_lf)
    gzip_sha = hashlib.sha256(output.read_bytes()).hexdigest()
    row = {
        "schema": "circdist-gross-round102-sat-proof-output-stream-v1",
        "status": "PASS",
        "query": relative,
        "solver_status": "SATISFIABLE",
        "proof_output_enabled_from_start": True,
        "certificate_disposition": "complete SAT-side proof output; not an UNSAT certificate",
        "raw_sha256": raw_sha,
        "raw_bytes": raw_bytes,
        "raw_lf_count": raw_lf,
        "gzip_path": str(output.relative_to(args.root)),
        "gzip_sha256": gzip_sha,
        "gzip_bytes": output.stat().st_size,
        "lossless_roundtrip_verified": True,
    }
    summary = source.with_suffix(source.suffix + ".stream.json")
    summary.write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    source.unlink()
    rows.append(row)

print(json.dumps({
    "status": "PASS",
    "streams": len(rows),
    "raw_bytes": sum(row["raw_bytes"] for row in rows),
    "gzip_bytes": sum(row["gzip_bytes"] for row in rows),
}, sort_keys=True))
