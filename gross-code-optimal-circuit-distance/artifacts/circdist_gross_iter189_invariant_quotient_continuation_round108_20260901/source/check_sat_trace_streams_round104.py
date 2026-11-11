#!/usr/bin/env python3
"""Stream-check the three compressed SAT side-output descriptors."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json

CHUNK = 8 << 20


def scan(handle):
    digest = hashlib.sha256()
    size = lf = empty = 0
    pending = b""
    for chunk in iter(lambda: handle.read(CHUNK), b""):
        digest.update(chunk)
        size += len(chunk)
        lf += chunk.count(b"\n")
        rows = (pending + chunk).split(b"\n")
        pending = rows.pop()
        empty += sum(row.strip() == b"0" for row in rows)
    if pending:
        empty += pending.strip() == b"0"
    return digest.hexdigest(), size, lf, int(empty)


def fsha(path):
    with Path(path).open("rb") as f:
        return scan(f)[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    descriptors = [
        "solver/iter187/outer.drat.stream.json",
        "solver/iter187/direct/solver/Xerr.drat.stream.json",
        "solver/iter187/direct/solver/Zerr.drat.stream.json",
    ]
    rows = []
    for rel in descriptors:
        descriptor = json.loads((root / rel).read_text())
        gz = root / descriptor["gzip_path"]
        assert descriptor["status"] == "PASS"
        assert descriptor["solver_status"] == "SATISFIABLE"
        assert "not a DRAT/LRAT certificate" in descriptor["certificate_disposition"]
        assert descriptor["raw_empty_clause_lines"] == 0
        assert descriptor["lossless_roundtrip_verified"] is True
        assert fsha(gz) == descriptor["gzip_sha256"]
        assert gz.stat().st_size == descriptor["gzip_bytes"]
        with gzip.open(gz, "rb") as f:
            observed = scan(f)
        expected = (descriptor["raw_sha256"], descriptor["raw_bytes"],
                    descriptor["raw_lf_count"], descriptor["raw_empty_clause_lines"])
        assert observed == expected
        rows.append({"descriptor": rel, "gzip_path": descriptor["gzip_path"],
                     "gzip_sha256": descriptor["gzip_sha256"],
                     "raw_sha256": descriptor["raw_sha256"],
                     "raw_bytes": descriptor["raw_bytes"],
                     "raw_lf_count": descriptor["raw_lf_count"],
                     "raw_empty_clause_lines": 0,
                     "classification": "SAT trace, not an UNSAT certificate"})
    result = {"schema": "circdist-gross-round104-sat-trace-stream-check-v1",
              "status": "PASS", "streams": rows,
              "stream_count": 3,
              "raw_bytes": sum(row["raw_bytes"] for row in rows),
              "gzip_bytes": sum((root / json.loads((root / rel).read_text())["gzip_path"]).stat().st_size
                                for rel in descriptors),
              "empty_clause_lines": 0,
              "all_lossless_roundtrips_verified": True,
              "certificate_claim": None}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "stream_count", "raw_bytes",
                                             "gzip_bytes", "empty_clause_lines")}, sort_keys=True))


if __name__ == "__main__":
    main()
