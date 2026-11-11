#!/usr/bin/env python3
"""Create the Round116 staging tree using only ordinary byte copies."""
import argparse, hashlib, os, shutil
from pathlib import Path


def fsha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(8<<20),b""): h.update(b)
    return h.hexdigest()


ap=argparse.ArgumentParser(); ap.add_argument("--repository",type=Path,required=True)
ap.add_argument("--work",type=Path,required=True); ap.add_argument("--destination",type=Path,required=True)
a=ap.parse_args(); repo=a.repository.resolve(); work=a.work.resolve(); dst=a.destination.resolve()
assert not dst.exists(); dst.mkdir(parents=True)
r114=repo/"circdist/artifacts/circdist_gross_iter192_invariant_quotient_continuation_round114_20260902"


def copy_file(src,rel):
    src=Path(src); out=dst/rel; out.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,out); os.chmod(out,src.stat().st_mode & 0o777)
    assert fsha(src)==fsha(out) and (src.stat().st_dev,src.stat().st_ino)!=(out.stat().st_dev,out.stat().st_ino)


def copy_tree(src,rel):
    src=Path(src); out=dst/rel
    shutil.copytree(src,out,symlinks=False,copy_function=shutil.copy2)
    assert not [p for p in out.rglob("*") if p.is_symlink()]


# Exact reviewed iter193 inputs and all new result/frontier bytes.
copy_tree(r114/"frontier/iter193_full_invariant","input/iter193/base")
copy_tree(r114/"frontier/iter193_full_invariant_quotient","input/iter193/translation_quotient")
copy_tree(work/"output/iter193","output/iter193")
copy_tree(work/"output/iter194","frontier/iter194")
copy_tree(work/"logs","logs/session")
copy_file(work/"process.jsonl","logs/process/session_process.jsonl")

# Dispatch, governance, handoff, protocol, and reviewed-parent bindings.
bindings={
 repo/"circdist/proof-dag/nodes/CIRCDIST.gross.yaml":"bindings/CIRCDIST.gross.yaml",
 repo/"operations/circdist/SCHEDULER.yaml":"bindings/SCHEDULER.yaml",
 repo/"circdist/reviews/circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md":"bindings/round115_exact_review.md",
 repo/"research/circdist/notes/HANDOFF_20260823.md":"bindings/HANDOFF_20260823.md",
 Path("/private/tmp/circdist-round116-proofpilot-rank.json"):"bindings/round116_proofpilot_rank.json",
 repo/"DAG_PROTOCOL.md":"bindings/DAG_PROTOCOL.root.md",
 repo/"FILE_PROTOCOL.md":"bindings/FILE_PROTOCOL.root.md",
 repo/"research/DAG_PROTOCOL.md":"bindings/DAG_PROTOCOL.research.md",
 repo/"research/FILE_PROTOCOL.md":"bindings/FILE_PROTOCOL.research.md",
 r114/"SHA256SUMS.txt":"bindings/round114_SHA256SUMS.txt",
 r114/"PAYLOAD_SHA256SUMS.txt":"bindings/round114_PAYLOAD_SHA256SUMS.txt",
 r114/"REPORT.md":"bindings/round114_REPORT.md",
 r114/"RESULT.json":"bindings/round114_RESULT.json",
 r114/"FRESH_FRONTIER.json":"bindings/round114_FRESH_FRONTIER.json",
}
for src,rel in bindings.items(): copy_file(src,rel)

# Every executable or checker newly authored, adapted, or invoked scientifically.
custom=[p for p in (work/"scratch").glob("*.py") if p.name!="assemble_package_tree_round116.py"]
for src in custom: copy_file(src,"source/"+src.name)
copy_file(work/"serial_exec.py","source/serial_exec.py")
parent_tools=[
 "extract_and_check_assignment.py","verify_outer_sat_model.py",
 "check_sat_orbit_controls_round102.py","build_direct_from_candidate.py",
 "audit_batch_attempt_round112.py","audit_css_duality_round114.py",
 "check_registry_invariance_round110.py","compile_outer_cnf.py",
 "check_outer_encoding.py","duplicate_yaml_scan.py","check_process_ledger.py",
]
for name in parent_tools: copy_file(r114/"source"/name,"source/parent_"+name)
copy_tree(r114/"vendor","vendor")
copy_tree(r114/"python","python")
copy_tree(r114/"tooling","tooling")

for p in (dst/"source").glob("*.py"): os.chmod(p,0o555)
for p in (dst/"tooling").glob("*"):
    if p.is_file(): os.chmod(p,0o555)

files=[p for p in dst.rglob("*") if p.is_file()]
assert all(p.stat().st_nlink==1 for p in files)
seen={}
for p in files:
    key=(p.stat().st_dev,p.stat().st_ino); assert key not in seen; seen[key]=p
print(f"PASS files={len(files)} bytes={sum(p.stat().st_size for p in files)}")
