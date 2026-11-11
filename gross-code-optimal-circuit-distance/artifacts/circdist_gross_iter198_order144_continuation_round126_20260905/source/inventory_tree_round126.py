#!/usr/bin/env python3
"""Create a canonical SHA-256 inventory for one preserved failure tree."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--root", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
p.add_argument("--label", required=True)
a = p.parse_args(); root = a.root.resolve()
assert root.is_dir() and not root.is_symlink()
rows = []
for path in sorted(root.rglob("*")):
    assert not path.is_symlink(), path
    if path.is_file():
        rows.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)})
canonical = "".join(f"{r['sha256']}  {r['bytes']}  {r['path']}\n" for r in rows).encode()
out = {
    "schema": "circdist-gross-round126-preserved-tree-inventory-v1", "status": "PASS",
    "label": a.label, "root_at_inventory_time": str(root), "files": rows,
    "file_count": len(rows), "total_bytes": sum(r["bytes"] for r in rows),
    "canonical_inventory_sha256": hashlib.sha256(canonical).hexdigest(),
    "canonical_inventory_definition": "SHA-256 of UTF-8 rows '<sha256>  <bytes>  <relative_path>\\n' in bytewise relative-path order",
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: out[k] for k in ("status", "label", "file_count", "total_bytes", "canonical_inventory_sha256")}, sort_keys=True))
