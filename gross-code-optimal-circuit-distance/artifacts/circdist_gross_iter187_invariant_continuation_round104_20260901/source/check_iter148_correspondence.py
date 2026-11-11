#!/usr/bin/env python3
from pathlib import Path
import argparse, gzip, hashlib, json

ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve(); F = R / "formulas/iter148"; X = R / "reconstruction"
def sha_bytes(data): return hashlib.sha256(data).hexdigest()
stored_cnf = gzip.decompress((F / "outer.cnf.gz").read_bytes())
stored_map = gzip.decompress((F / "assertion_map.jsonl.gz").read_bytes())
fresh_cnf = (X / "fresh.outer.cnf").read_bytes()
fresh_map = (X / "fresh.assertion_map.jsonl").read_bytes()
assert stored_cnf == fresh_cnf == (X / "stored.outer.cnf").read_bytes()
assert stored_map == fresh_map == (X / "stored.assertion_map.jsonl").read_bytes()
assert (F / "circuit_trace.json.gz").read_bytes() == (X / "fresh.circuit_trace.json.gz").read_bytes()
sm = json.loads((F / "metadata.json").read_text()); fm = json.loads((X / "fresh.metadata.json").read_text())
stored_compile_seconds = sm.pop("compile_seconds"); fresh_compile_seconds = fm.pop("compile_seconds"); assert sm == fm
se = json.loads((F / "encoding_check.json").read_text()); fe = json.loads((X / "fresh.encoding_check.json").read_text())
stored_check_seconds = se.pop("seconds"); fresh_check_seconds = fe.pop("seconds"); assert se == fe
out = {
  "schema": "circdist-round96-iter148-correspondence-v1", "status": "PASS",
  "source_file_sha256": sm["source_file_sha256"], "source_semantic_sha256": sm["source_semantic_payload_sha256"],
  "cnf_sha256": sha_bytes(fresh_cnf), "cnf_byte_identical": True,
  "assertion_map_sha256": sha_bytes(fresh_map), "assertion_map_byte_identical": True,
  "circuit_trace_sha256": hashlib.sha256((X / "fresh.circuit_trace.json.gz").read_bytes()).hexdigest(), "circuit_trace_byte_identical": True,
  "metadata_equal_excluding_compile_seconds": True, "encoding_check_equal_excluding_seconds": True,
  "stored_compile_seconds": stored_compile_seconds, "fresh_compile_seconds": fresh_compile_seconds,
  "stored_encoding_check_seconds": stored_check_seconds, "fresh_encoding_check_seconds": fresh_check_seconds,
  "assertions": sm["assertions"], "variables": sm["variables"], "clauses": sm["clauses"],
  "all_clause_ids_partitioned_once": fe["all_clause_ids_partitioned_once"],
  "all_source_roots_reconstructed": fe["all_source_roots_reconstructed"],
  "all_variables_primary_or_uniquely_defined": fe["all_variables_primary_or_uniquely_defined"],
  "negative_controls": fe["negative_controls"],
  "correspondence": "byte-identical deterministic source compilation plus independent complete clause/definition/root reconstruction",
}
(X / "correspondence.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
