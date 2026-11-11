#!/usr/bin/env python3
"""Install one ordinary copy using only the sealed fixed file inventory."""
import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--destination", type=Path, required=True)
ap.add_argument("--receipt", type=Path, required=True)
a = ap.parse_args()
src, dst = a.source.resolve(), a.destination
assert src.is_dir() and (src / "SHA256SUMS.txt").is_file() and not dst.exists()
assert dst.name == "circdist_gross_iter197_order144_continuation_round124_20260905"
inventory = [json.loads(line) for line in (src / "FILE_INVENTORY.jsonl").read_text().splitlines()]
rels = sorted(row["path"] for row in inventory)
assert len(rels) == len(set(rels))
static = json.loads((src / "PRESEAL_PATH_INVENTORY.json").read_text())
assert rels == sorted(static["initial_files"] + static["fixed_added_files"])
for rel in static["directories"]:
    (dst if rel == "." else dst / rel).mkdir(parents=True, exist_ok=True)
for rel in rels:
    target = dst / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src / rel, target)
inode_aliases = []
for rel in rels:
    sp, dp = src / rel, dst / rel
    assert sp.stat().st_size == dp.stat().st_size and sha(sp) == sha(dp), rel
    if (sp.stat().st_dev, sp.stat().st_ino) == (dp.stat().st_dev, dp.stat().st_ino):
        inode_aliases.append(rel)
    assert dp.stat().st_nlink == 1 and not dp.is_symlink()
assert not inode_aliases
dirs = {dst if rel == "." else dst / rel for rel in static["directories"]}
for path in sorted(dirs, key=lambda p: len(p.parts), reverse=True):
    os.chmod(path, 0o555)
out = {
    "schema": "circdist-gross-round124-durable-copy-v1", "status": "PASS",
    "source": str(src), "destination": str(dst.resolve()),
    "root_manifest_sha256": sha(dst / "SHA256SUMS.txt"),
    "payload_manifest_sha256": sha(dst / "PAYLOAD_SHA256SUMS.txt"),
    "inventory_sha256": sha(dst / "FILE_INVENTORY.jsonl"),
    "files": len(rels), "directories": len(dirs),
    "bytes": sum((dst / rel).stat().st_size for rel in rels),
    "ordinary_copy": True, "source_destination_inode_aliases": 0,
    "symlinks": 0, "solver_invocations": 0, "static_inventory_only": True,
}
a.receipt.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
