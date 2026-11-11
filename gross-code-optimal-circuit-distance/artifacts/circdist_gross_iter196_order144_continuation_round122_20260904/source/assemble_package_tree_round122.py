#!/usr/bin/env python3
"""Assemble the Round122 Gross proposer package with ordinary distinct-inode copies."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path

CHUNK = 8 << 20


def fsha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--repository", type=Path, required=True)
p.add_argument("--work", type=Path, required=True)
p.add_argument("--destination", type=Path, required=True)
a = p.parse_args()
repo, work, dst = a.repository.resolve(), a.work.resolve(), a.destination.resolve()
parent = repo / "circdist/artifacts/circdist_gross_iter195_order144_continuation_round120_20260904"
assert parent.is_dir() and not dst.exists()
dst.mkdir(parents=True)


def copy_file(src: Path, rel: str) -> None:
    src, target = Path(src), dst / rel
    assert src.is_file() and not src.is_symlink(), src
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, target)
    assert fsha(src) == fsha(target)
    assert (src.stat().st_dev, src.stat().st_ino) != (target.stat().st_dev, target.stat().st_ino)
    assert target.stat().st_nlink == 1


def copy_tree(src: Path, rel: str, skip_raw_drat: bool = False) -> None:
    src, target = Path(src), dst / rel
    assert src.is_dir() and not src.is_symlink() and not target.exists(), src
    if not skip_raw_drat:
        shutil.copytree(src, target, symlinks=False, copy_function=shutil.copy2)
    else:
        target.mkdir(parents=True)
        for item in sorted(src.rglob("*")):
            sub = item.relative_to(src)
            out = target / sub
            assert not item.is_symlink(), item
            if item.is_dir():
                out.mkdir(parents=True, exist_ok=True)
            elif item.suffix.lower() != ".drat":
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, out)
    assert not [x for x in target.rglob("*") if x.is_symlink()]


# Exact independently reviewed input, complete iter196 evidence except raw traces,
# and the fresh never-solved iter197 boundary.
copy_tree(parent / "frontier/iter196", "input/iter196")
copy_tree(work / "output/iter196", "output/iter196", skip_raw_drat=True)
copy_file(work / "logs/session/solve-iter196-exact-order144-quotient-proof-first.stdout", "output/iter196/solver/solver.log")
copy_file(work / "logs/session/solve-iter196-exact-order144-quotient-proof-first.stderr", "output/iter196/solver/solver.stderr")
copy_file(work / "verification/iter196_outer_orbit_controls.json", "output/iter196/solver/orbit_controls.json")
copy_tree(work / "frontier/iter197", "frontier/iter197")
copy_tree(work / "verification", "verification")
copy_tree(work / "logs", "logs/session_and_process")

# Lossless compressed forms of all three proof-output streams.
labels = {"outer": "outer.drat.gz", "Xerr": "Xerr.drat.gz", "Zerr": "Zerr.drat.gz"}
for label, filename in labels.items():
    copy_file(work / "proof_streams" / filename, "proof_streams/" + filename)
    copy_file(work / "proof_streams" / f"{label}.trace.json", f"proof_streams/provenance/{label}.trace.json")
    d = json.loads((work / "proof_streams" / f"{label}.trace.json").read_text())
    d["package_gzip_path"] = "proof_streams/" + filename
    d["solver_status"] = "SATISFIABLE"
    d["certificate_disposition"] = "complete SAT search trace retained; not a DRAT/LRAT UNSAT certificate; zero UNSAT-certificate credit"
    d["lossless_roundtrip_verified"] = True
    d["raw_lf_count"] = d["raw_newline_count"]
    target = dst / f"proof_streams/{label}.stream.json"
    target.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")

# Dispatch and protocol bindings.
bindings = {
    repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    repo / "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    repo / "circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md": "bindings/round121_exact_review.md",
    repo / "DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.md",
    repo / "FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.md",
    repo / "circdist/README.md": "bindings/circdist_README.md",
    Path("/private/tmp/circdist-round122-proofpilot-rank.json"): "bindings/round122_proofpilot_rank.json",
}
for src, rel in bindings.items():
    copy_file(src, rel)
for name in (
    "SHA256SUMS.txt", "PAYLOAD_SHA256SUMS.txt", "FILE_INVENTORY.jsonl", "REPORT.md",
    "RESULT.json", "FRESH_FRONTIER.json", "SEAL.json", "COPY_AUDIT.json",
    "INPUT_BINDINGS.json", "PROCESS_BOUNDARY.json", "PROCESS_LEDGER_CHECK.json",
    "THEOREM_NOTES.md", "ENVIRONMENT.json", "FAILURE_LEDGER.md",
):
    copy_file(parent / name, "bindings/round120_parent/" + name)

# Reviewed implementation ancestry, Round122 adaptations, pinned tools/deps.
copy_tree(parent / "source", "source/round120_reviewed")
for src in sorted(work.glob("*.py")):
    copy_file(src, "source/" + src.name)
copy_tree(parent / "tooling", "tooling")
copy_tree(parent / "python", "python")
copy_tree(parent / "vendor", "vendor")

for path in (dst / "source").rglob("*.py"):
    os.chmod(path, 0o555)
for path in (dst / "tooling").glob("*"):
    if path.is_file():
        os.chmod(path, 0o555)

files = [x for x in dst.rglob("*") if x.is_file()]
seen = {}
for path in files:
    assert not path.is_symlink() and path.stat().st_nlink == 1
    inode = (path.stat().st_dev, path.stat().st_ino)
    assert inode not in seen, (seen.get(inode), path)
    seen[inode] = path
print(json.dumps({"status": "PASS", "files": len(files), "bytes": sum(x.stat().st_size for x in files)}, sort_keys=True))
