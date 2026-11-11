#!/usr/bin/env python3
"""Losslessly retain large checked quotient CNFs as deterministic gzip files."""
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


def digest(handle):
    sha = hashlib.sha256()
    size = lf = 0
    for chunk in iter(lambda: handle.read(1 << 20), b""):
        sha.update(chunk)
        size += len(chunk)
        lf += chunk.count(b"\n")
    return sha.hexdigest(), size, lf


rows = []
for relative in args.paths:
    source = args.root / relative
    assert source.is_file() and source.suffix == ".cnf"
    with source.open("rb") as handle:
        raw_sha, raw_bytes, raw_lf = digest(handle)
    output = source.with_suffix(source.suffix + ".gz")
    temporary = output.with_suffix(output.suffix + ".tmp")
    with source.open("rb") as inp, temporary.open("wb") as raw_out:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out,
                           compresslevel=9, mtime=0) as encoded:
            shutil.copyfileobj(inp, encoded, 1 << 20)
    os.replace(temporary, output)
    with gzip.open(output, "rb") as handle:
        check = digest(handle)
    assert check == (raw_sha, raw_bytes, raw_lf)
    gzip_sha = hashlib.sha256(output.read_bytes()).hexdigest()
    descriptor = {
        "schema": "circdist-gross-round102-compressed-bound-formula-v1",
        "status": "PASS",
        "raw_path": relative,
        "raw_sha256": raw_sha,
        "raw_bytes": raw_bytes,
        "raw_lf_count": raw_lf,
        "gzip_path": str(output.relative_to(args.root)),
        "gzip_sha256": gzip_sha,
        "gzip_bytes": output.stat().st_size,
        "lossless_roundtrip_verified": True,
    }
    source.with_suffix(source.suffix + ".compression.json").write_text(
        json.dumps(descriptor, indent=2, sort_keys=True) + "\n")
    source.unlink()
    rows.append(descriptor)

print(json.dumps({
    "status": "PASS",
    "formulas": len(rows),
    "raw_bytes": sum(row["raw_bytes"] for row in rows),
    "gzip_bytes": sum(row["gzip_bytes"] for row in rows),
}, sort_keys=True))
