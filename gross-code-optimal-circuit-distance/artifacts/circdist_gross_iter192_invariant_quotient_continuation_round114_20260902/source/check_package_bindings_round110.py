#!/usr/bin/env python3
"""Check embedded governance, predecessor, input, and fresh-frontier bindings."""
from pathlib import Path
import argparse
import hashlib
import json


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    bindings = json.loads((root / "INPUT_BINDINGS.json").read_text())
    assert bindings["status"] == "PASS" and bindings["bound_before_science"] is True
    local = {
        "operations/circdist/SCHEDULER.yaml": root / "bindings/SCHEDULER.yaml",
        "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": root / "bindings/CIRCDIST.gross.yaml",
        "circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md": root / "bindings/round109_review.md",
    }
    for name, path in local.items():
        expected = bindings["canonical"][name]
        assert sha(path) == expected["sha256"] and path.stat().st_size == expected["bytes"]
    assert (root / "PROPOSED_CIRCDIST.gross.yaml").read_bytes() == (root / "bindings/CIRCDIST.gross.yaml").read_bytes()

    for rel, expected in bindings["embedded_input_files"].items():
        path = root / rel
        assert path.is_file() and sha(path) == expected["sha256"] and path.stat().st_size == expected["bytes"]
    actual_inputs = {p.relative_to(root).as_posix() for p in (root / "inputs/round108").rglob("*") if p.is_file()}
    assert actual_inputs == set(bindings["embedded_input_files"])

    old_manifest = {}
    for line in (root / "bindings/round108_SHA256SUMS.txt").read_text().splitlines():
        digest, rel = line.split("  ", 1)
        old_manifest[rel] = digest
    predecessor_mapped = 0
    for rel in sorted(actual_inputs):
        suffix = rel.removeprefix("inputs/round108/")
        if suffix.startswith("iter189_adjudication/"):
            leaf = suffix.split("/", 1)[1]
            old_rel = ("solver/iter189/candidate.json" if leaf == "candidate.json" else
                       "solver/iter189/direct/direct_verification.json")
        else:
            old_rel = suffix
        assert old_rel in old_manifest and old_manifest[old_rel] == sha(root / rel)
        predecessor_mapped += 1

    fresh = json.loads((root / "FRESH_FRONTIER.json").read_text())
    state = json.loads((root / "frontier/iter191_full_invariant/state.json").read_text())
    assert fresh["status"] == "PASS" and fresh["iteration"] == 191
    assert fresh["fresh_unstarted"] and not fresh["iter191_solved"]
    assert state["started"] is False and state["stop"] is None and state["next_iteration"] == 191
    base_set = sorted(p.name for p in (root / "frontier/iter191_full_invariant/formula").iterdir() if p.is_file())
    quotient_set = sorted(p.name for p in (root / "frontier/iter191_full_invariant_quotient").iterdir() if p.is_file())
    assert base_set == fresh["base_formula_exact_file_set"]
    assert quotient_set == fresh["quotient_exact_file_set"]
    forbidden = ("assignment", "solver", "drat", "lrat", "proof", "model")
    assert not any(any(token in p.name.lower() for token in forbidden)
                   for p in (root / "frontier").rglob("*") if p.is_file())
    symlinks = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
    assert not symlinks
    result = {"schema": "circdist-gross-round110-package-bindings-check-v1", "status": "PASS",
              "canonical_bindings": len(local), "embedded_input_files": len(actual_inputs),
              "predecessor_manifest_mapped_files": predecessor_mapped,
              "fresh_iteration": 191, "reviewed_iteration": 190,
              "base_exact_file_set": base_set, "quotient_exact_file_set": quotient_set,
              "symlinks": 0, "proposed_canonical_identical": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
