#!/usr/bin/env python3
"""Create two-level manifests, an exact inventory, and a read-only Round118 seal."""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def files(root):
    return sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix())


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
reserved = {"PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt", "FILE_INVENTORY.jsonl", "SEAL.json", "COPY_AUDIT.json"}
assert not any((R / name).exists() for name in reserved)
assert not [p for p in R.rglob("*") if p.is_symlink()]

seen = {}
aliases = []
bad_links = []
for path in files(R):
    key = (path.stat().st_dev, path.stat().st_ino)
    rel = path.relative_to(R).as_posix()
    if key in seen:
        aliases.append([seen[key], rel])
    else:
        seen[key] = rel
    if path.stat().st_nlink != 1:
        bad_links.append([rel, path.stat().st_nlink])
assert not aliases and not bad_links

copy_audit = {
    "schema": "circdist-gross-round118-preseal-copy-audit-v1",
    "status": "PASS",
    "files": len(files(R)),
    "symlinks": 0,
    "hardlink_aliases": 0,
    "files_with_nlink_not_one": 0,
    "ordinary_file_tree": True,
    "source_destination_inode_distinctness_checked_during_assembly": True,
    "copy_on_write_extents_permitted": True,
    "ctime_immutability_claimed": False,
}
(R / "COPY_AUDIT.json").write_text(json.dumps(copy_audit, indent=2, sort_keys=True) + "\n")

payload = files(R)
(R / "PAYLOAD_SHA256SUMS.txt").write_text(
    "".join(f"{sha(path)}  {path.relative_to(R).as_posix()}\n" for path in payload)
)
payload_hash = sha(R / "PAYLOAD_SHA256SUMS.txt")
seal = {
    "schema": "circdist-gross-round118-two-level-seal-v1",
    "status": "SEALED",
    "date": "2026-09-03",
    "payload_manifest_sha256": payload_hash,
    "payload_files": len(payload),
    "root_manifest_excludes_only": "SHA256SUMS.txt itself",
    "inventory_self_row": "explicit null self-reference; final inventory bytes are bound by SHA256SUMS.txt",
    "postseal_mutation_permitted": False,
    "ordinary_copy_required": True,
    "symlinks_permitted": False,
    "hardlink_aliases_permitted": False,
    "ctime_immutability_claimed": False,
}
(R / "SEAL.json").write_text(json.dumps(seal, indent=2, sort_keys=True) + "\n")

# The two self-referential paths are explicitly null. All ordinary rows bind final bytes.
ordinary_paths = [p.relative_to(R).as_posix() for p in files(R)]
paths = sorted(set(ordinary_paths + ["FILE_INVENTORY.jsonl", "SHA256SUMS.txt"]))
with (R / "FILE_INVENTORY.jsonl").open("w") as handle:
    for relative in paths:
        if relative in ("FILE_INVENTORY.jsonl", "SHA256SUMS.txt"):
            row = {
                "path": relative,
                "bytes": None,
                "mode": None,
                "sha256": None,
                "self_reference": True,
                "binding": "final bytes are bound by SHA256SUMS.txt, except SHA256SUMS.txt which is externally identified by its root hash",
            }
        else:
            path = R / relative
            row = {
                "path": relative,
                "bytes": path.stat().st_size,
                "mode": oct(stat.S_IMODE(path.stat().st_mode)),
                "sha256": sha(path),
                "self_reference": False,
            }
        handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

root_files = files(R)
(R / "SHA256SUMS.txt").write_text(
    "".join(f"{sha(path)}  {path.relative_to(R).as_posix()}\n" for path in root_files)
)
root_hash = sha(R / "SHA256SUMS.txt")

for path in files(R):
    os.chmod(path, 0o555 if (path.stat().st_mode & 0o111) else 0o444)
for path in sorted((p for p in R.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
    os.chmod(path, 0o555)
os.chmod(R, 0o555)

print(json.dumps({
    "status": "SEALED",
    "root_manifest_sha256": root_hash,
    "payload_manifest_sha256": payload_hash,
    "root_rows": len(root_files),
    "payload_rows": len(payload),
    "inventory_paths": len(paths),
    "inventory_bytes": (R / "FILE_INVENTORY.jsonl").stat().st_size,
    "inventory_lf": (R / "FILE_INVENTORY.jsonl").read_bytes().count(b"\n"),
}, sort_keys=True))
