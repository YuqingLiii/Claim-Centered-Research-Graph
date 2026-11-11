#!/usr/bin/env python3
"""Verify the Round116 root/payload manifests and filesystem seal."""
import argparse, hashlib, json, os, stat
from pathlib import Path


def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(8<<20),b""): h.update(chunk)
    return h.hexdigest()


def parse(path):
    rows=[]
    for line in path.read_text().splitlines():
        digest, rel=line.split("  ",1); rows.append((digest,rel))
    assert len(rows)==len({r for _,r in rows})
    return rows


ap=argparse.ArgumentParser(); ap.add_argument("--root",type=Path,required=True)
ap.add_argument("--output",type=Path); a=ap.parse_args(); root=a.root.resolve()
root_rows=parse(root/"SHA256SUMS.txt"); payload_rows=parse(root/"PAYLOAD_SHA256SUMS.txt")
actual=sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())
assert sorted(r for _,r in root_rows)==sorted(r for r in actual if r!="SHA256SUMS.txt")
for digest,rel in root_rows: assert sha(root/rel)==digest
for digest,rel in payload_rows: assert sha(root/rel)==digest
assert sha(root/"PAYLOAD_SHA256SUMS.txt")==json.loads((root/"SEAL.json").read_text())["payload_manifest_sha256"]
links=[p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
aliases=[]
seen={}
for p in root.rglob("*"):
    if p.is_file():
        key=(p.stat().st_dev,p.stat().st_ino)
        if key in seen: aliases.append([seen[key],p.relative_to(root).as_posix()])
        else: seen[key]=p.relative_to(root).as_posix()
assert not links and not aliases
readonly=all(not (p.stat().st_mode & 0o222) for p in [root,*root.rglob("*")])
assert readonly
out={"schema":"circdist-gross-round116-sealed-package-check-v1","status":"PASS",
     "root_manifest_sha256":sha(root/"SHA256SUMS.txt"),
     "payload_manifest_sha256":sha(root/"PAYLOAD_SHA256SUMS.txt"),
     "root_files":len(root_rows),"payload_files":len(payload_rows),"symlinks":0,
     "hardlink_aliases":0,"all_paths_read_only":True,"ctime_immutability_claimed":False}
if a.output: a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,sort_keys=True))
