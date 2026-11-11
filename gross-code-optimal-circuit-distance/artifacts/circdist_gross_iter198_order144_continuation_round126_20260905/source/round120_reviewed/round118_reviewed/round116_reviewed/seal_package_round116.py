#!/usr/bin/env python3
"""Create two-level manifests, complete inventory, and a read-only package seal."""
import argparse,hashlib,json,os,stat
from pathlib import Path

def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8<<20),b""):h.update(b)
 return h.hexdigest()

def files(root):return sorted((p for p in root.rglob("*") if p.is_file()),key=lambda p:p.relative_to(root).as_posix())
ap=argparse.ArgumentParser();ap.add_argument("--root",type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
reserved={"PAYLOAD_SHA256SUMS.txt","SHA256SUMS.txt","FILE_INVENTORY.jsonl","SEAL.json","COPY_AUDIT.json"}
assert not any((R/x).exists() for x in reserved)
assert not [p for p in R.rglob("*") if p.is_symlink()]
seen={};aliases=[]
for p in files(R):
 key=(p.stat().st_dev,p.stat().st_ino)
 if key in seen:aliases.append([seen[key],p.relative_to(R).as_posix()])
 else:seen[key]=p.relative_to(R).as_posix()
assert not aliases and all(p.stat().st_nlink==1 for p in files(R))
copy_audit={"schema":"circdist-gross-round116-preseal-copy-audit-v1","status":"PASS","files":len(files(R)),
 "symlinks":0,"hardlink_aliases":0,"files_with_nlink_not_one":0,"ordinary_file_tree":True,
 "ctime_immutability_claimed":False,"note":"Final repository installation is separately verified as an ordinary copy with distinct inode for every file."}
(R/"COPY_AUDIT.json").write_text(json.dumps(copy_audit,indent=2,sort_keys=True)+"\n")
payload=files(R)
(R/"PAYLOAD_SHA256SUMS.txt").write_text("".join(f"{sha(p)}  {p.relative_to(R).as_posix()}\n" for p in payload))
seal={"schema":"circdist-gross-round116-two-level-seal-v1","status":"SEALED","date":"2026-09-02",
 "payload_manifest_sha256":sha(R/"PAYLOAD_SHA256SUMS.txt"),"payload_files":len(payload),
 "root_manifest_excludes_only":"SHA256SUMS.txt itself","postseal_mutation_permitted":False,
 "ordinary_copy_required":True,"symlinks_permitted":False,"hardlink_aliases_permitted":False,"ctime_immutability_claimed":False}
(R/"SEAL.json").write_text(json.dumps(seal,indent=2,sort_keys=True)+"\n")
# Complete pathname inventory. Self-referential inventory/root hashes are null; the root manifest binds the inventory bytes.
paths=[p.relative_to(R).as_posix() for p in files(R)]+["FILE_INVENTORY.jsonl","SHA256SUMS.txt"]
paths=sorted(set(paths))
with (R/"FILE_INVENTORY.jsonl").open("w") as f:
 for rel in paths:
  p=R/rel
  if p.exists():row={"path":rel,"bytes":p.stat().st_size,"mode":oct(stat.S_IMODE(p.stat().st_mode)),"sha256":sha(p),"self_reference":False}
  else:row={"path":rel,"bytes":None,"mode":None,"sha256":None,"self_reference":True,"binding":"bound externally by SHA256SUMS.txt or is SHA256SUMS.txt itself"}
  f.write(json.dumps(row,sort_keys=True,separators=(",",":"))+"\n")
root_files=files(R)
(R/"SHA256SUMS.txt").write_text("".join(f"{sha(p)}  {p.relative_to(R).as_posix()}\n" for p in root_files))
root_sha=sha(R/"SHA256SUMS.txt")
for p in files(R):os.chmod(p,0o555 if (p.stat().st_mode&0o111) else 0o444)
for p in sorted((p for p in R.rglob("*") if p.is_dir()),key=lambda p:len(p.parts),reverse=True):os.chmod(p,0o555)
os.chmod(R,0o555)
print(json.dumps({"status":"SEALED","root_manifest_sha256":root_sha,"payload_manifest_sha256":seal["payload_manifest_sha256"],
 "root_rows":len(root_files),"payload_rows":len(payload),"inventory_paths":len(paths)},sort_keys=True))
