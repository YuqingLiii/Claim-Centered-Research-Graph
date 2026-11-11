#!/usr/bin/env python3
"""Create the Round118 durable package with ordinary byte copies only."""
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
parent = repo / "circdist/artifacts/circdist_gross_iter193_invariant_quotient_continuation_round116_20260902"

assert parent.is_dir()
assert not dst.exists()
dst.mkdir(parents=True)


def copy_file(source, relative):
    source = Path(source)
    target = dst / relative
    assert source.is_file() and not source.is_symlink()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    os.chmod(target, source.stat().st_mode & 0o777)
    assert fsha(source) == fsha(target)
    assert (source.stat().st_dev, source.stat().st_ino) != (target.stat().st_dev, target.stat().st_ino)
    assert target.stat().st_nlink == 1


def copy_tree(source, relative):
    source = Path(source)
    target = dst / relative
    assert source.is_dir() and not source.is_symlink() and not target.exists()
    shutil.copytree(source, target, symlinks=False, copy_function=shutil.copy2)
    assert not [p for p in target.rglob("*") if p.is_symlink()]


# Exact reviewed iteration-194 input, complete result, and exact next frontier.
copy_tree(parent / "frontier/iter194", "input/iter194")
copy_tree(work / "output/iter194", "output/iter194")
copy_tree(work / "output/iter195", "frontier/iter195")

# Session evidence is a snapshot; a later preseal cutpoint refreshes the process ledger.
copy_tree(work / "logs", "logs/session")
copy_file(work / "logs/session_process.jsonl", "logs/process/session_process.initial.jsonl")

# Dispatch, governance, protocols, and complete reviewed-parent provenance.
bindings = {
    repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    repo / "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    repo / "circdist/reviews/circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md": "bindings/round117_exact_review.md",
    repo / "research/circdist/notes/HANDOFF_20260823.md": "bindings/HANDOFF_20260823.md",
    Path("/private/tmp/circdist-round118-proofpilot-rank.json"): "bindings/round118_proofpilot_rank.json",
    repo / "DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.root.md",
    repo / "FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.root.md",
    repo / "research/DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.research.md",
    repo / "research/FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.research.md",
    parent / "SHA256SUMS.txt": "bindings/round116_SHA256SUMS.txt",
    parent / "PAYLOAD_SHA256SUMS.txt": "bindings/round116_PAYLOAD_SHA256SUMS.txt",
    parent / "FILE_INVENTORY.jsonl": "bindings/round116_FILE_INVENTORY.jsonl",
    parent / "REPORT.md": "bindings/round116_REPORT.md",
    parent / "RESULT.json": "bindings/round116_RESULT.json",
    parent / "FRESH_FRONTIER.json": "bindings/round116_FRESH_FRONTIER.json",
    parent / "SEAL.json": "bindings/round116_SEAL.json",
    parent / "COPY_AUDIT.json": "bindings/round116_COPY_AUDIT.json",
}
for source, relative in bindings.items():
    copy_file(source, relative)

# Exact reviewed sources and every locally authored/adapted Python source.
copy_tree(parent / "source", "source/round116_reviewed")
for source in sorted(work.glob("*.py")):
    copy_file(source, "source/" + source.name)

# Pinned native tools and self-contained Python/vendor dependencies.
copy_tree(parent / "tooling", "tooling")
copy_tree(parent / "python", "python")
copy_tree(parent / "vendor", "vendor")

for path in (dst / "source").rglob("*.py"):
    os.chmod(path, 0o555)
for path in (dst / "tooling").glob("*"):
    if path.is_file():
        os.chmod(path, 0o555)

files = [p for p in dst.rglob("*") if p.is_file()]
seen = {}
for path in files:
    assert not path.is_symlink()
    assert path.stat().st_nlink == 1
    key = (path.stat().st_dev, path.stat().st_ino)
    assert key not in seen, (seen.get(key), path)
    seen[key] = path
print(f"PASS files={len(files)} bytes={sum(p.stat().st_size for p in files)}")
