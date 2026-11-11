#!/usr/bin/env python3
"""Verify a Round122 seal solely from its fixed manifests and static inventory."""
import argparse
import hashlib
import json
import stat
from pathlib import Path

NAME = "circdist_gross_iter196_order144_continuation_round122_20260904"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def parse_manifest(path):
    rows = []
    for line in path.read_text().splitlines():
        digest, rel = line.split("  ", 1)
        assert len(digest) == 64 and rel and not rel.startswith("/") and ".." not in Path(rel).parts
        rows.append((digest, rel))
    assert len(rows) == len({rel for _, rel in rows})
    return rows


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path)
a = ap.parse_args()
root = a.root.resolve()
assert root.is_dir() and root.name == NAME
root_rows = parse_manifest(root / "SHA256SUMS.txt")
payload_rows = parse_manifest(root / "PAYLOAD_SHA256SUMS.txt")
inventory = [json.loads(line) for line in (root / "FILE_INVENTORY.jsonl").read_text().splitlines()]
assert len(inventory) == len({row["path"] for row in inventory})
inventory_paths = sorted(row["path"] for row in inventory)
assert sorted(rel for _, rel in root_rows) == sorted(set(inventory_paths) - {"SHA256SUMS.txt"})
static = json.loads((root / "PRESEAL_PATH_INVENTORY.json").read_text())
expected_paths = sorted(static["initial_files"] + static["fixed_added_files"])
assert inventory_paths == expected_paths
for digest, rel in root_rows:
    assert sha(root / rel) == digest, rel
for digest, rel in payload_rows:
    assert sha(root / rel) == digest, rel
assert sorted(rel for _, rel in payload_rows) == sorted(
    set(inventory_paths) - {"PAYLOAD_SHA256SUMS.txt", "SEAL.json", "FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}
)
seal = json.loads((root / "SEAL.json").read_text())
assert seal["schema"] == "circdist-gross-round122-two-level-seal-v1"
assert seal["status"] == "SEALED" and seal["package_name"] == NAME
assert sha(root / "PAYLOAD_SHA256SUMS.txt") == seal["payload_manifest_sha256"]
seen = {}
aliases = []
bad_links = []
for row in inventory:
    path = root / row["path"]
    assert path.is_file() and not path.is_symlink()
    key = (path.stat().st_dev, path.stat().st_ino)
    if key in seen:
        aliases.append([seen[key], row["path"]])
    else:
        seen[key] = row["path"]
    if path.stat().st_nlink != 1:
        bad_links.append([row["path"], path.stat().st_nlink])
    if row["path"] in {"FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}:
        assert row["self_reference"] and row["bytes"] is row["mode"] is row["sha256"] is None
    else:
        assert not row["self_reference"] and row["bytes"] == path.stat().st_size
        final_mode = stat.S_IMODE(path.stat().st_mode)
        assert final_mode == (0o555 if int(row["mode"], 8) & 0o111 else 0o444)
        assert row["sha256"] == sha(path)
assert not aliases and not bad_links
dirs = [root if rel == "." else root / rel for rel in static["directories"]]
assert all(path.is_dir() and not path.is_symlink() and not (path.stat().st_mode & 0o222) for path in dirs)
out = {
    "schema": "circdist-gross-round122-sealed-package-check-v1", "status": "PASS",
    "root_manifest_sha256": sha(root / "SHA256SUMS.txt"),
    "payload_manifest_sha256": sha(root / "PAYLOAD_SHA256SUMS.txt"),
    "inventory_sha256": sha(root / "FILE_INVENTORY.jsonl"),
    "root_files": len(root_rows), "payload_files": len(payload_rows),
    "package_files": len(inventory), "package_directories": len(dirs),
    "package_bytes": sum((root / rel).stat().st_size for rel in inventory_paths),
    "inventory_paths": len(inventory),
    "inventory_bytes": (root / "FILE_INVENTORY.jsonl").stat().st_size,
    "inventory_lf": len(inventory), "inventory_explicit_self_rows": 2,
    "symlinks": 0, "hardlink_aliases": 0, "files_with_nlink_not_one": 0,
    "all_manifest_paths_read_only": True, "static_inventory_only": True,
    "solver_invocations": 0, "ctime_immutability_claimed": False,
}
if a.output:
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
