#!/usr/bin/env python3
"""Deterministically gzip one complete ASCII SAT search trace and verify round trip."""

import argparse
import gzip
import hashlib
import json
import os
import time
from pathlib import Path


p = argparse.ArgumentParser()
p.add_argument("--input", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
p.add_argument("--metadata", type=Path, required=True)
p.add_argument("--label", required=True)
p.add_argument("--solver-return-code", type=int, required=True)
a = p.parse_args()

assert a.solver_return_code == 10
a.output.parent.mkdir(parents=True, exist_ok=True)
a.metadata.parent.mkdir(parents=True, exist_ok=True)
before = a.input.stat()
t0 = time.monotonic()
raw_hash = hashlib.sha256()
raw_bytes = 0
newlines = 0
first = b""
last = b""
with a.input.open("rb") as src, a.output.open("wb") as raw_out:
    with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out, compresslevel=6, mtime=0) as dst:
        while True:
            chunk = src.read(8 << 20)
            if not chunk:
                break
            if not first:
                first = chunk[:64]
            last = (last + chunk)[-64:]
            raw_hash.update(chunk)
            raw_bytes += len(chunk)
            newlines += chunk.count(b"\n")
            dst.write(chunk)
    raw_out.flush()
    os.fsync(raw_out.fileno())
after = a.input.stat()
assert (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) == (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns)
assert raw_bytes == before.st_size and raw_bytes > 0

compressed_hash = hashlib.sha256()
with a.output.open("rb") as fh:
    for chunk in iter(lambda: fh.read(8 << 20), b""):
        compressed_hash.update(chunk)

roundtrip_hash = hashlib.sha256()
roundtrip_bytes = 0
roundtrip_newlines = 0
with gzip.open(a.output, "rb") as fh:
    for chunk in iter(lambda: fh.read(8 << 20), b""):
        roundtrip_hash.update(chunk)
        roundtrip_bytes += len(chunk)
        roundtrip_newlines += chunk.count(b"\n")
assert roundtrip_hash.hexdigest() == raw_hash.hexdigest()
assert roundtrip_bytes == raw_bytes
assert roundtrip_newlines == newlines

result = {
    "schema": "circdist-gross-round126-complete-sat-search-trace-v1",
    "status": "PASS",
    "label": a.label,
    "classification": "SAT_SEARCH_TRACE",
    "unsat_certificate_credit": 0,
    "proof_output_enabled_from_byte_zero": True,
    "solver_return_code": a.solver_return_code,
    "raw_path": str(a.input),
    "raw_bytes": raw_bytes,
    "raw_sha256": raw_hash.hexdigest(),
    "raw_newline_count": newlines,
    "raw_first_64_hex": first.hex(),
    "raw_last_64_hex": last.hex(),
    "gzip_path": str(a.output),
    "gzip_bytes": a.output.stat().st_size,
    "gzip_sha256": compressed_hash.hexdigest(),
    "deterministic_gzip_mtime": 0,
    "gzip_compresslevel": 6,
    "roundtrip_bytes": roundtrip_bytes,
    "roundtrip_sha256": roundtrip_hash.hexdigest(),
    "roundtrip_newline_count": roundtrip_newlines,
    "input_identity_stable_during_compression": True,
    "elapsed_seconds": time.monotonic() - t0,
}
a.metadata.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({k: result[k] for k in ("status", "label", "raw_bytes", "raw_sha256", "gzip_bytes", "gzip_sha256", "roundtrip_sha256", "unsat_certificate_credit", "elapsed_seconds")}, sort_keys=True))
