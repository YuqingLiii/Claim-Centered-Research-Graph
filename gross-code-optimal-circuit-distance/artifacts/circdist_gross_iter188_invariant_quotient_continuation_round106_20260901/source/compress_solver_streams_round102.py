#!/usr/bin/env python3
"""Losslessly retain solver streams with deterministic, streaming gzip.

The caller supplies the actual solver disposition.  In particular, an UNKNOWN
prefix is never relabeled as a proof.  Raw bytes are deleted only after a full
decompression/hash/length/LF round trip succeeds.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import shutil


CHUNK = 8 << 20


def scan_handle(handle):
    digest = hashlib.sha256()
    size = 0
    lf = 0
    empty_clause_lines = 0
    pending = b""
    for block in iter(lambda: handle.read(CHUNK), b""):
        digest.update(block)
        size += len(block)
        lf += block.count(b"\n")
        data = pending + block
        lines = data.split(b"\n")
        pending = lines.pop()
        empty_clause_lines += sum(line.strip() == b"0" for line in lines)
    if pending:
        empty_clause_lines += pending.strip() == b"0"
    return digest.hexdigest(), size, lf, int(empty_clause_lines)


def scan_path(path, compressed=False):
    opener = gzip.open if compressed else open
    with opener(path, "rb") as handle:
        return scan_handle(handle)


def digest_only(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--solver-status", required=True,
                        choices=("SATISFIABLE", "UNSATISFIABLE", "UNKNOWN"))
    parser.add_argument("--certificate-disposition", required=True)
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()
    root = args.root.resolve()
    rows = []
    for relative in args.paths:
        source = root / relative
        assert source.is_file(), source
        raw = scan_path(source)
        output = source.with_name(source.name + ".gz")
        temporary = output.with_name(output.name + ".tmp")
        with source.open("rb") as inp, temporary.open("wb") as raw_out:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_out,
                               compresslevel=9, mtime=0) as encoded:
                shutil.copyfileobj(inp, encoded, CHUNK)
        os.replace(temporary, output)
        restored = scan_path(output, compressed=True)
        assert restored == raw, (relative, raw, restored)
        descriptor = {
            "schema": "circdist-gross-round102-solver-output-stream-v1",
            "status": "PASS",
            "query": relative,
            "solver_status": args.solver_status,
            "proof_output_enabled_from_start": True,
            "certificate_disposition": args.certificate_disposition,
            "raw_sha256": raw[0],
            "raw_bytes": raw[1],
            "raw_lf_count": raw[2],
            "raw_empty_clause_lines": raw[3],
            "gzip_path": output.relative_to(root).as_posix(),
            "gzip_sha256": digest_only(output),
            "gzip_bytes": output.stat().st_size,
            "lossless_roundtrip_verified": True,
            "streaming_memory_bound_bytes": CHUNK,
        }
        source.with_name(source.name + ".stream.json").write_text(
            json.dumps(descriptor, indent=2, sort_keys=True) + "\n")
        source.unlink()
        rows.append(descriptor)
    print(json.dumps({
        "status": "PASS",
        "solver_status": args.solver_status,
        "streams": len(rows),
        "raw_bytes": sum(row["raw_bytes"] for row in rows),
        "gzip_bytes": sum(row["gzip_bytes"] for row in rows),
        "empty_clause_lines": sum(row["raw_empty_clause_lines"] for row in rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
