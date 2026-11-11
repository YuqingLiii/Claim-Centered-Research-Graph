#!/usr/bin/env python3
"""Package-local exact binding, allowlist, state, and freshness checker."""
from pathlib import Path
import argparse
import hashlib
import json
import re

EXPECTED_BINDINGS = {
    "bindings/SCHEDULER.yaml": "89767aecd57e32608cc75010c26a5d415af3330964c42e572aefed86796c259b",
    "bindings/CIRCDIST.gross.yaml": "3fe41bc65891f94f65be55931c40f37cf3bbb3c5bdb7cca9cfa70a73489526ae",
    "bindings/round105_review.md": "01d14be78fc75362c16340b4ba32df783a645084a819fc18a96f432d9a45e932",
    "bindings/round104_SHA256SUMS.txt": "410807a787005a0fb5ebb1753f8b75712c798d9a15e9101f1265d0be25206ebb",
}
EXPECTED_INPUT = {
    "frontier/iter188_full_invariant/formula/outer.cnf": "051dbece97d9cd94a69de7bff644dbb31b35076d0c43558b5408d9f3cc86b257",
    "frontier/iter188_full_invariant_quotient/outer.cnf": "29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215",
    "frontier/iter188_full_invariant/source.json.gz": "bb6605e47b541fccd8c33a4b8f3ae56e1ac298ab4be591fbc4c388dc102e0647",
    "frontier/iter188_full_invariant/state.json": "ac4140e37f855fe37c1403c645e08d600d7ab70a6aee725f707b74a9721a30cd",
}
Q_ALLOW = {"independent_check.json", "metadata.json", "outer.cnf",
           "translation_roots.jsonl", "translation_trace.json.gz"}
B_ALLOW = {"assertion_map.jsonl", "definitions.json.gz", "encoding_check.json",
           "metadata.json", "outer.cnf"}
FORBIDDEN = re.compile(r"(?:^|[._-])(solver|model|assignment|proof|drat|lrat|stdout|stderr|log)(?:$|[._-])", re.I)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    bindings = {}
    for rel, expected in EXPECTED_BINDINGS.items():
        observed = sha(root / rel)
        assert observed == expected
        bindings[rel] = {"sha256": observed, "bytes": (root / rel).stat().st_size}
    manifest_rows = {}
    for line in (root / "bindings/round104_SHA256SUMS.txt").read_text().splitlines():
        digest, rel = line.split("  ", 1)
        assert rel not in manifest_rows
        manifest_rows[rel] = digest
    assert len(manifest_rows) == 383
    inputs = {}
    for rel, expected in EXPECTED_INPUT.items():
        copied = root / "inputs/round104" / rel
        observed = sha(copied)
        assert observed == expected == manifest_rows[rel]
        inputs[rel] = {"sha256": observed, "bytes": copied.stat().st_size}
    qdir = root / "inputs/round104/frontier/iter188_full_invariant_quotient"
    bdir = root / "inputs/round104/frontier/iter188_full_invariant/formula"
    assert {p.name for p in qdir.iterdir() if p.is_file()} == Q_ALLOW
    assert {p.name for p in bdir.iterdir() if p.is_file()} == B_ALLOW
    state = json.loads((root / "inputs/round104/frontier/iter188_full_invariant/state.json").read_text())
    assert state["next_iteration"] == 188 and state["started"] is False and state["stop"] is None
    assert state["block_count"] == 517140 and state["selector_count"] == 24156
    new_state = json.loads((root / "frontier/iter189_full_invariant/state.json").read_text())
    assert new_state["next_iteration"] == 189 and new_state["started"] is False and new_state["stop"] is None
    assert new_state["block_count"] == 517140 and new_state["selector_count"] == 24300
    expected_new_q = {"independent_check.json", "metadata.json", "outer.cnf",
                      "translation_roots.jsonl", "translation_trace.json.gz"}
    expected_new_b = {"assertion_map.jsonl", "definitions.json.gz", "encoding_check.json",
                      "metadata.json", "outer.cnf"}
    assert {p.name for p in (root / "frontier/iter189_full_invariant_quotient").iterdir() if p.is_file()} == expected_new_q
    assert {p.name for p in (root / "frontier/iter189_full_invariant/formula").iterdir() if p.is_file()} == expected_new_b
    frontier_files = [p for p in (root / "frontier").rglob("*") if p.is_file()]
    forbidden = [p.relative_to(root).as_posix() for p in frontier_files if FORBIDDEN.search(p.name)]
    assert forbidden == []
    symlinks = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
    assert symlinks == []
    result = {
        "schema": "circdist-gross-round106-package-binding-check-v1", "status": "PASS",
        "bindings": bindings, "round104_manifest_rows": len(manifest_rows),
        "mandatory_inputs": inputs,
        "reviewed_frontier": {"iteration": 188, "started": False, "stop": None,
                              "blocks": 517140, "selectors": 24156,
                              "quotient_allowlist": sorted(Q_ALLOW),
                              "base_formula_allowlist": sorted(B_ALLOW)},
        "fresh_frontier": {"iteration": 189, "started": False, "stop": None,
                           "blocks": 517140, "selectors": 24300,
                           "quotient_allowlist": sorted(expected_new_q),
                           "base_formula_allowlist": sorted(expected_new_b)},
        "forbidden_frontier_artifacts": forbidden, "symlinks": symlinks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "round104_manifest_rows": len(manifest_rows),
                      "reviewed_iteration": 188, "fresh_iteration": 189,
                      "symlinks": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
