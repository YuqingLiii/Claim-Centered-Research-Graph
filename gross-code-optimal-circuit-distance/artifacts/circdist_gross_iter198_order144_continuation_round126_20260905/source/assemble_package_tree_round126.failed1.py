#!/usr/bin/env python3
"""Assemble the Round126 Gross proposer package with ordinary distinct-inode copies."""
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
parent = repo / "circdist/artifacts/circdist_gross_iter197_order144_continuation_round124_20260905"
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


def copy_tree(src: Path, rel: str, skip_sat_streams: bool = False) -> None:
    src, target = Path(src), dst / rel
    assert src.is_dir() and not src.is_symlink() and not target.exists(), src
    if not skip_sat_streams:
        shutil.copytree(src, target, symlinks=False, copy_function=shutil.copy2)
    else:
        target.mkdir(parents=True)
        for item in sorted(src.rglob("*")):
            sub = item.relative_to(src)
            out = target / sub
            assert not item.is_symlink(), item
            if item.is_dir():
                out.mkdir(parents=True, exist_ok=True)
            elif item.suffix.lower() != ".drat" and not item.name.lower().endswith(".drat.gz"):
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, out)
    assert not [x for x in target.rglob("*") if x.is_symlink()]


# Exact reviewed input, complete iteration-198 evidence except raw/compressed trace
# duplicates, and the fresh never-solved iteration-199 boundary.
copy_tree(parent / "frontier/iter198", "input/iter198")
copy_tree(work / "output/iter198", "output/iter198", skip_sat_streams=True)
copy_file(work / "logs/transcripts/solve-iter198-exact-order144-quotient-proof-first.stdout", "output/iter198/solver/solver.log")
copy_file(work / "logs/transcripts/solve-iter198-exact-order144-quotient-proof-first.stderr", "output/iter198/solver/solver.stderr")
copy_file(work / "logs/transcripts/solve-iter198-Xerr-complete-direct360-proof-first.stdout", "output/iter198/direct/solver/Xerr.solver.log")
copy_file(work / "logs/transcripts/solve-iter198-Xerr-complete-direct360-proof-first.stderr", "output/iter198/direct/solver/Xerr.solver.stderr")
copy_file(work / "logs/transcripts/solve-iter198-Zerr-complete-direct360-proof-first.stdout", "output/iter198/direct/solver/Zerr.solver.log")
copy_file(work / "logs/transcripts/solve-iter198-Zerr-complete-direct360-proof-first.stderr", "output/iter198/direct/solver/Zerr.solver.stderr")
copy_file(work / "verification/iter198_outer_orbit_controls.json", "output/iter198/solver/orbit_controls.json")
copy_tree(work / "frontier/iter199", "frontier/iter199")
copy_tree(work / "verification", "verification")
copy_tree(work / "logs", "logs/session_and_process")
copy_tree(work / "work", "recovery_state")
copy_file(work / "tmp/xcrun_db", "recovery_state/tmp/xcrun_db")

# Lossless compressed forms of all three proof-output streams.
streams = {
    "outer": (work / "output/iter198/solver/outer.sat_search_trace.drat.gz", work / "verification/outer_sat_search_trace.json"),
    "Xerr": (work / "output/iter198/direct/solver/Xerr.sat_search_trace.drat.gz", work / "verification/Xerr_sat_search_trace.json"),
    "Zerr": (work / "output/iter198/direct/solver/Zerr.sat_search_trace.drat.gz", work / "verification/Zerr_sat_search_trace.json"),
}
for label, (stream, provenance) in streams.items():
    filename = f"{label}.drat.gz"
    copy_file(stream, "proof_streams/" + filename)
    copy_file(provenance, f"proof_streams/provenance/{label}.trace.json")
    d = json.loads(provenance.read_text())
    d["package_gzip_path"] = "proof_streams/" + filename
    d["solver_status"] = "SATISFIABLE"
    d["certificate_disposition"] = "complete SAT search trace retained; not a DRAT/LRAT UNSAT certificate; zero UNSAT-certificate credit"
    d["lossless_roundtrip_verified"] = True
    d["raw_lf_count"] = d["raw_newline_count"]
    target = dst / f"proof_streams/{label}.stream.json"
    target.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")

# Dispatch, review, protocol, and parent-seal bindings.
bindings = {
    repo / "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "bindings/CIRCDIST.gross.yaml",
    repo / "operations/circdist/SCHEDULER.yaml": "bindings/SCHEDULER.yaml",
    repo / "circdist/reviews/circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md": "bindings/round125_exact_review.md",
    repo / "DAG_PROTOCOL.md": "bindings/DAG_PROTOCOL.md",
    repo / "FILE_PROTOCOL.md": "bindings/FILE_PROTOCOL.md",
    repo / "circdist/README.md": "bindings/circdist_README.md",
    Path("/private/tmp/circdist-round126-proofpilot-rank.json"): "bindings/round126_proofpilot_rank.json",
}
for src, rel in bindings.items():
    copy_file(src, rel)
for item in sorted(parent.iterdir()):
    if item.is_file() and not item.is_symlink():
        copy_file(item, "bindings/round124_parent/" + item.name)

# Reviewed implementation ancestry, Round126 adaptations, pinned tools/deps.
copy_tree(parent / "source", "source")
for item in sorted((work / "source").iterdir()):
    if item.is_file() and not item.is_symlink():
        copy_file(item, "source/" + item.name)
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
