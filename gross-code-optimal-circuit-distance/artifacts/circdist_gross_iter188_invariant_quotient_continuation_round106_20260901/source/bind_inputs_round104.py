#!/usr/bin/env python3
"""Verify and bind the immutable Round104 dispatch inputs."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import platform
import subprocess


EXPECTED = {
    "bindings/SCHEDULER.yaml": "d9bcb7affe40ed12a479785f5a102673108b4322fe0d20a1cf6da4483069c31f",
    "bindings/CIRCDIST.gross.yaml": "dd367bf93e59e10588a824d4f530a0b07c3707d43886004bb3ddb754f0ff7d91",
    "bindings/round103_review.md": "a7e027b228d785fae5280b33ab95f7999bb4e9b3e001cd30a5816444637db48e",
    "inputs/round102/SHA256SUMS.txt": "80e70f62075a852355029b765cbe7ebfa4f8156d25b6d9fa2ea1ddbb9e19b4f4",
    "inputs/round102/frontier/iter187_full_invariant/formula/outer.cnf": "7f66b46643b6b10cce57358e4e66f7e95cdc1bfe52ee14f77884c56ddd5d5eab",
    "inputs/round102/frontier/iter187_full_invariant_quotient/outer.cnf": "e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234",
}


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def metrics(path):
    digest = hashlib.sha256()
    size = lines = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
            size += len(block)
            lines += block.count(b"\n")
    return {"sha256": digest.hexdigest(), "bytes": size, "lf": lines}


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
args = ap.parse_args()
root = args.root.resolve()
rows = {}
for rel, expected in EXPECTED.items():
    path = root / rel
    assert path.is_file(), rel
    row = metrics(path)
    assert row["sha256"] == expected, (rel, row["sha256"], expected)
    rows[rel] = row

state_path = root / "inputs/round102/frontier/iter187_full_invariant/state.json"
state = json.loads(state_path.read_text())
assert state["status"] == "PASS" and state["started"] is False
assert state["next_iteration"] == 187
assert state["block_count"] == 517140 and state["selector_count"] == 24012

quotient_dir = root / "inputs/round102/frontier/iter187_full_invariant_quotient"
expected_names = {
    "independent_check.json", "metadata.json", "outer.cnf",
    "translation_roots.jsonl", "translation_trace.json.gz",
}
observed_names = {p.name for p in quotient_dir.iterdir()}
assert observed_names == expected_names, (observed_names - expected_names, expected_names - observed_names)
for forbidden in ("solver.log", "solver.stderr.log", "outer.drat", "outer.drat.gz",
                  "assignment.dimacs", "candidate.json", "replay.json"):
    assert not (quotient_dir / forbidden).exists(), forbidden

with (quotient_dir / "outer.cnf").open() as handle:
    header = handle.readline().split()
assert header == ["p", "cnf", "2452334", "11789630"], header
qmeta = json.loads((quotient_dir / "metadata.json").read_text())
qcheck = json.loads((quotient_dir / "independent_check.json").read_text())
assert qcheck["status"] == "PASS"
assert qcheck["base_cnf_sha256"] == EXPECTED[
    "inputs/round102/frontier/iter187_full_invariant/formula/outer.cnf"]
assert qcheck["quotient_cnf_sha256"] == EXPECTED[
    "inputs/round102/frontier/iter187_full_invariant_quotient/outer.cnf"]
assert qcheck["group"] == {"name": "Z_12 x Z_6", "nonidentity": 71, "order": 72}
assert qmeta["variables"] == 2452334 and qmeta["clauses"] == 11789630

tool_rows = {}
for name in ("cadical-1.9.5-arm64-macos", "drat-trim-arm64-macos", "lrat-check-arm64-macos"):
    path = root / "tooling" / name
    assert path.is_file() and os.access(path, os.X_OK)
    tool_rows[name] = metrics(path)

out = {
    "schema": "circdist-gross-round104-input-bindings-v1",
    "status": "PASS",
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "package": str(root),
    "expected_and_observed": rows,
    "round102_root_sha256sums_digest": rows["inputs/round102/SHA256SUMS.txt"]["sha256"],
    "frontier": {
        "iteration": 187,
        "fresh_unstarted": True,
        "quotient_directory_exact_unstarted_file_set": sorted(observed_names),
        "blocks": state["block_count"],
        "selectors": state["selector_count"],
        "state_sha256": sha(state_path),
        "source_sha256": sha(root / "inputs/round102/frontier/iter187_full_invariant/source.json.gz"),
        "base_variables": 1838894,
        "base_clauses": 6882039,
        "quotient_variables": 2452334,
        "quotient_clauses": 11789630,
    },
    "tooling": tool_rows,
    "environment": {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "cwd": os.getcwd(),
    },
}
args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "iteration": 187, "fresh_unstarted": True,
                  "variables": 2452334, "clauses": 11789630}, sort_keys=True))
