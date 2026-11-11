#!/usr/bin/env python3
"""Package-local exact Round108 binding, allowlist, state, and freshness checker."""
from pathlib import Path
import argparse
import hashlib
import json
import re

EXPECTED_BINDINGS = {
    "bindings/SCHEDULER.yaml": "13c74772427b20aaf8128633459ee995c62e60dd1b79090c458d00e9a0994343",
    "bindings/CIRCDIST.gross.yaml": "8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977",
    "bindings/round107_review.md": "eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036",
    "bindings/round106_SHA256SUMS.txt": "0b9cc6d4074e8397062219ec8d079afbcf0388e14912ab925b5d66ac00c61c9d",
}
EXPECTED_INPUT = {
    "frontier/iter189_full_invariant/formula/outer.cnf": "f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178",
    "frontier/iter189_full_invariant_quotient/outer.cnf": "3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7",
    "frontier/iter189_full_invariant/source.json.gz": "b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b",
    "frontier/iter189_full_invariant/state.json": "8bb97ba8ff7590f178aaff29f51da8ab6953b1fae90bcf6952546d31f59c6f97",
}
Q_ALLOW = {"independent_check.json", "metadata.json", "outer.cnf",
           "translation_roots.jsonl", "translation_trace.json.gz"}
B_ALLOW = {"assertion_map.jsonl", "definitions.json.gz", "encoding_check.json",
           "metadata.json", "outer.cnf"}
FORBIDDEN = re.compile(r"(?:^|[._-])(solver|model|assignment|proof|drat|lrat|stdout|stderr|log)(?:$|[._-])", re.I)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
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
        path = root / rel
        observed = sha(path)
        assert observed == expected
        bindings[rel] = {"sha256": observed, "bytes": path.stat().st_size}
    manifest_rows = {}
    for line in (root / "bindings/round106_SHA256SUMS.txt").read_text().splitlines():
        digest, rel = line.split("  ", 1)
        assert rel not in manifest_rows
        manifest_rows[rel] = digest
    assert len(manifest_rows) == 432
    inputs = {}
    for rel, expected in EXPECTED_INPUT.items():
        copied = root / "inputs/round106" / rel
        observed = sha(copied)
        assert observed == expected == manifest_rows[rel]
        inputs[rel] = {"sha256": observed, "bytes": copied.stat().st_size}
    qdir = root / "inputs/round106/frontier/iter189_full_invariant_quotient"
    bdir = root / "inputs/round106/frontier/iter189_full_invariant/formula"
    assert {p.name for p in qdir.iterdir() if p.is_file()} == Q_ALLOW
    assert {p.name for p in bdir.iterdir() if p.is_file()} == B_ALLOW
    state = json.loads((root / "inputs/round106/frontier/iter189_full_invariant/state.json").read_text())
    assert state["next_iteration"] == 189 and state["started"] is False and state["stop"] is None
    assert state["block_count"] == 517140 and state["selector_count"] == 24300
    assert state["selector_state_sha256"] == "8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa"
    new_state = json.loads((root / "frontier/iter190_full_invariant/state.json").read_text())
    assert new_state["next_iteration"] == 190 and new_state["started"] is False and new_state["stop"] is None
    assert new_state["block_count"] == 517140 and new_state["selector_count"] == 24444
    new_qdir = root / "frontier/iter190_full_invariant_quotient"
    new_bdir = root / "frontier/iter190_full_invariant/formula"
    assert {p.name for p in new_qdir.iterdir() if p.is_file()} == Q_ALLOW
    assert {p.name for p in new_bdir.iterdir() if p.is_file()} == B_ALLOW
    frontier_files = [p for p in (root / "frontier").rglob("*") if p.is_file()]
    forbidden = [p.relative_to(root).as_posix() for p in frontier_files if FORBIDDEN.search(p.name)]
    assert forbidden == []
    symlinks = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
    assert symlinks == []
    result = {
        "schema": "circdist-gross-round108-package-binding-check-v1", "status": "PASS",
        "bindings": bindings, "round106_manifest_rows": len(manifest_rows),
        "mandatory_inputs": inputs,
        "reviewed_frontier": {"iteration": 189, "started": False, "stop": None,
                              "blocks": 517140, "selectors": 24300,
                              "quotient_allowlist": sorted(Q_ALLOW),
                              "base_formula_allowlist": sorted(B_ALLOW)},
        "fresh_frontier": {"iteration": 190, "started": False, "stop": None,
                           "blocks": 517140, "selectors": 24444,
                           "quotient_allowlist": sorted(Q_ALLOW),
                           "base_formula_allowlist": sorted(B_ALLOW)},
        "forbidden_frontier_artifacts": forbidden, "symlinks": symlinks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "round106_manifest_rows": len(manifest_rows),
                      "reviewed_iteration": 189, "fresh_iteration": 190,
                      "symlinks": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
