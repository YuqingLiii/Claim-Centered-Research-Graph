#!/usr/bin/env python3
"""Copy immutable reviewed dependencies into the Round110 scratch package.

This is packaging only.  Existing Round110 source files are never overwritten.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def copy_tree_missing(src: Path, dst: Path) -> None:
    for path in sorted(src.rglob("*")):
        rel = path.relative_to(src)
        out = dst / rel
        if path.is_symlink():
            raise RuntimeError(f"symlink forbidden: {path}")
        if path.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        elif not out.exists():
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--round108", type=Path, required=True)
    args = ap.parse_args()
    root, repo, old = args.root.resolve(), args.repo.resolve(), args.round108.resolve()

    copied = {}
    for name in ("source", "vendor", "python", "tooling", "controls"):
        copy_tree_missing(old / name, root / name)
        copied[name] = sum(p.is_file() for p in (root / name).rglob("*"))

    adjudication = root / "inputs/round108/iter189_adjudication"
    adjudication.mkdir(parents=True, exist_ok=True)
    for src, name in (
        (old / "solver/iter189/candidate.json", "candidate.json"),
        (old / "solver/iter189/direct/direct_verification.json", "direct_verification.json"),
    ):
        shutil.copyfile(src, adjudication / name)

    bindings = root / "bindings"
    bindings.mkdir(parents=True, exist_ok=True)
    review = repo / "circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md"
    binding_sources = {
        "SCHEDULER.yaml": repo / "operations/circdist/SCHEDULER.yaml",
        "CIRCDIST.gross.yaml": repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml",
        "round109_review.md": review,
        "round108_SHA256SUMS.txt": old / "SHA256SUMS.txt",
        "round108_PAYLOAD_SHA256SUMS.txt": old / "PAYLOAD_SHA256SUMS.txt",
        "round108_FILE_INVENTORY.jsonl": old / "FILE_INVENTORY.jsonl",
        "round108_RESULT.json": old / "RESULT.json",
        "round108_REPORT.md": old / "REPORT.md",
    }
    for name, src in binding_sources.items():
        shutil.copyfile(src, bindings / name)

    proposed = root / "PROPOSED_CIRCDIST.gross.yaml"
    shutil.copyfile(binding_sources["CIRCDIST.gross.yaml"], proposed)

    for cache in sorted(root.rglob("__pycache__"), reverse=True):
        if cache.is_dir():
            shutil.rmtree(cache)
    for path in root.rglob("*"):
        if path.is_dir():
            os.chmod(path, 0o755)
        elif path.is_file():
            os.chmod(path, 0o755 if path.suffix == ".py" or path.name == "replay.sh" or "tooling" in path.parts else 0o644)

    output = {
        "status": "PASS",
        "copied_file_counts": copied,
        "bindings": {name: {"sha256": sha256(bindings / name), "bytes": (bindings / name).stat().st_size}
                     for name in sorted(binding_sources)},
        "proposed_canonical_sha256": sha256(proposed),
        "symlinks": sum(p.is_symlink() for p in root.rglob("*")),
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
