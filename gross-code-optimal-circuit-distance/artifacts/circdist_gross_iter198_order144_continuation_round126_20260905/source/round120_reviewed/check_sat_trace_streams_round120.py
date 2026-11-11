#!/usr/bin/env python3
"""Independently check the three complete compressed iteration-195 SAT traces."""
import argparse, gzip, hashlib, json
from pathlib import Path

CHUNK = 8 << 20


def scan(handle):
    h = hashlib.sha256(); size = lf = empty = 0; pending = b""
    for chunk in iter(lambda: handle.read(CHUNK), b""):
        h.update(chunk); size += len(chunk); lf += chunk.count(b"\n")
        rows = (pending + chunk).split(b"\n"); pending = rows.pop()
        empty += sum(row.strip() == b"0" for row in rows)
    if pending: empty += int(pending.strip() == b"0")
    return h.hexdigest(), size, lf, empty


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args(); root = a.root.resolve()
descriptors = ["output/iter195/solver/outer.drat.stream.json",
               "output/iter195/direct/solver/Xerr.drat.stream.json",
               "output/iter195/direct/solver/Zerr.drat.stream.json"]
rows = []
for rel in descriptors:
    d = json.loads((root / rel).read_text()); gz = root / d["gzip_path"]
    assert d["status"] == "PASS" and d["solver_status"] == "SATISFIABLE"
    assert "not a DRAT/LRAT UNSAT certificate" in d["certificate_disposition"]
    assert d["raw_empty_clause_lines"] == 0 and d["lossless_roundtrip_verified"]
    with gz.open("rb") as f: compressed = scan(f)
    assert compressed[0] == d["gzip_sha256"] and compressed[1] == d["gzip_bytes"]
    with gzip.open(gz, "rb") as f: raw = scan(f)
    assert raw == (d["raw_sha256"], d["raw_bytes"], d["raw_lf_count"], 0)
    rows.append({"descriptor":rel, "gzip_sha256":compressed[0], "gzip_bytes":compressed[1],
                 "raw_sha256":raw[0], "raw_bytes":raw[1], "raw_lf_count":raw[2],
                 "raw_empty_clause_lines":0, "classification":"SAT search trace; no UNSAT credit"})
out = {"schema":"circdist-gross-round120-sat-trace-stream-check-v1", "status":"PASS",
       "streams":rows, "stream_count":3, "raw_bytes":sum(r["raw_bytes"] for r in rows),
       "gzip_bytes":sum(r["gzip_bytes"] for r in rows), "empty_clause_lines":0,
       "all_lossless_roundtrips_verified":True, "certificate_claim":None}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({k:out[k] for k in ("status","stream_count","raw_bytes","gzip_bytes","empty_clause_lines")},sort_keys=True))
