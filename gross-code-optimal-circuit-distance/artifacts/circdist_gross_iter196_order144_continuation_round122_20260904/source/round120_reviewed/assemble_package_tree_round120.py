#!/usr/bin/env python3
"""Assemble the Round120 Gross package using ordinary distinct-inode copies."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
from pathlib import Path


CHUNK = 8 << 20


def fsha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--work", type=Path, required=True)
ap.add_argument("--destination", type=Path, required=True)
a = ap.parse_args()
repo = a.repository.resolve()
work = a.work.resolve()
dst = a.destination.resolve()
parent = repo / "circdist/artifacts/circdist_gross_iter194_order144_continuation_round118_20260902"

assert parent.is_dir()
assert not dst.exists()
dst.mkdir(parents=True)


def copy_file(source: Path, relative: str) -> None:
    source = Path(source)
    target = dst / relative
    assert source.is_file() and not source.is_symlink(), source
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    assert fsha(source) == fsha(target)
    assert (source.stat().st_dev, source.stat().st_ino) != (target.stat().st_dev, target.stat().st_ino)
    assert target.stat().st_nlink == 1


def copy_tree(source: Path, relative: str) -> None:
    source = Path(source)
    target = dst / relative
    assert source.is_dir() and not source.is_symlink() and not target.exists(), source
    shutil.copytree(source, target, symlinks=False, copy_function=shutil.copy2)
    assert not [path for path in target.rglob("*") if path.is_symlink()]


# The exact independently reviewed input, the complete iteration-195 result,
# and the newly constructed iteration-196 review boundary.
copy_tree(parent / "frontier/iter195", "input/iter195")
copy_tree(work / "output/iter195", "output/iter195")
copy_tree(work / "frontier/iter196", "frontier/iter196")
copy_tree(work / "verification", "verification")

# Session/process logs are refreshed at the final preseal cutpoint.
copy_tree(work / "logs/session", "logs/session")
copy_tree(work / "logs/process", "logs/process")

bindings = {
    repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    repo / "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    repo / "circdist/reviews/circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md": "bindings/round119_exact_review.md",
    repo / "research/circdist/notes/HANDOFF_20260823.md": "bindings/HANDOFF_20260823.md",
    Path("/private/tmp/circdist-round120-proofpilot-rank.json"): "bindings/round120_proofpilot_rank.json",
    repo / "DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.root.md",
    repo / "FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.root.md",
    repo / "research/DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.research.md",
    repo / "research/FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.research.md",
}
for name in (
    "SHA256SUMS.txt", "PAYLOAD_SHA256SUMS.txt", "FILE_INVENTORY.jsonl",
    "REPORT.md", "RESULT.json", "FRESH_FRONTIER.json", "SEAL.json",
    "COPY_AUDIT.json", "INPUT_BINDINGS.json", "PROCESS_BOUNDARY.json",
    "THEOREM_NOTES.md", "ENVIRONMENT.json", "FAILURE_LEDGER.md",
):
    bindings[parent / name] = "bindings/round118_" + name
for source, relative in bindings.items():
    copy_file(source, relative)

# Complete reviewed implementation ancestry plus every Round120 adaptation.
copy_tree(parent / "source", "source/round118_reviewed")
for source in sorted((work / "source").glob("*.py")):
    copy_file(source, "source/" + source.name)

# Pinned solver/checking tools and locally vendored Python dependencies.
copy_tree(parent / "tooling", "tooling")
copy_tree(parent / "python", "python")
copy_tree(parent / "vendor", "vendor")

for path in (dst / "source").rglob("*.py"):
    os.chmod(path, 0o555)
for path in (dst / "tooling").glob("*"):
    if path.is_file():
        os.chmod(path, 0o555)

files = [path for path in dst.rglob("*") if path.is_file()]
seen = {}
for path in files:
    assert not path.is_symlink()
    assert path.stat().st_nlink == 1
    inode = (path.stat().st_dev, path.stat().st_ino)
    assert inode not in seen, (seen.get(inode), path)
    seen[inode] = path
print(f"PASS files={len(files)} bytes={sum(path.stat().st_size for path in files)}")
