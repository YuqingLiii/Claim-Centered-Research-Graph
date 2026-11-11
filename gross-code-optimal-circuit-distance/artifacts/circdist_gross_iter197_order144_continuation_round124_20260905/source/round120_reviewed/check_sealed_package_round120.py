#!/usr/bin/env python3
"""Verify Round120 manifests, exact inventory conventions, topology, and read-only seal."""
import argparse
import hashlib
import json
import stat
from pathlib import Path


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_manifest(path):
    rows = []
    for line in path.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        assert len(digest) == 64
        rows.append((digest, relative))
    assert len(rows) == len({relative for _, relative in rows})
    return rows


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path)
ap.add_argument("--allow-writable-root", action="store_true")
a = ap.parse_args()
R = a.root.resolve()
root_rows = parse_manifest(R / "SHA256SUMS.txt")
payload_rows = parse_manifest(R / "PAYLOAD_SHA256SUMS.txt")
actual = sorted(p.relative_to(R).as_posix() for p in R.rglob("*") if p.is_file())
assert sorted(relative for _, relative in root_rows) == sorted(relative for relative in actual if relative != "SHA256SUMS.txt")
for digest, relative in root_rows:
    assert sha(R / relative) == digest, relative
for digest, relative in payload_rows:
    assert sha(R / relative) == digest, relative
seal = json.loads((R / "SEAL.json").read_text())
assert seal["status"] == "SEALED"
assert sha(R / "PAYLOAD_SHA256SUMS.txt") == seal["payload_manifest_sha256"]

inventory = [json.loads(line) for line in (R / "FILE_INVENTORY.jsonl").read_text().splitlines()]
assert len(inventory) == len({row["path"] for row in inventory}) == len(actual)
assert sorted(row["path"] for row in inventory) == actual
for row in inventory:
    if row["path"] in ("FILE_INVENTORY.jsonl", "SHA256SUMS.txt"):
        assert row["self_reference"] and row["bytes"] is row["mode"] is row["sha256"] is None
    else:
        path = R / row["path"]
        assert not row["self_reference"]
        assert row["bytes"] == path.stat().st_size
        # Inventory records preseal modes. Files may only have lost write bits at seal.
        recorded = int(row["mode"], 8)
        final = stat.S_IMODE(path.stat().st_mode)
        assert final == (0o555 if recorded & 0o111 else 0o444)
        assert row["sha256"] == sha(path)

links = [p.relative_to(R).as_posix() for p in R.rglob("*") if p.is_symlink()]
aliases = []
bad_links = []
seen = {}
for path in R.rglob("*"):
    if path.is_file():
        key = (path.stat().st_dev, path.stat().st_ino)
        if key in seen:
            aliases.append([seen[key], path.relative_to(R).as_posix()])
        else:
            seen[key] = path.relative_to(R).as_posix()
        if path.stat().st_nlink != 1:
            bad_links.append([path.relative_to(R).as_posix(), path.stat().st_nlink])
assert not links and not aliases and not bad_links
readonly = all(not (p.stat().st_mode & 0o222) for p in [R, *R.rglob("*")])
if not a.allow_writable_root:
    assert readonly

out = {
    "schema": "circdist-gross-round120-sealed-package-check-v1",
    "status": "PASS",
    "root_manifest_sha256": sha(R / "SHA256SUMS.txt"),
    "payload_manifest_sha256": sha(R / "PAYLOAD_SHA256SUMS.txt"),
    "root_files": len(root_rows),
    "payload_files": len(payload_rows),
    "inventory_paths": len(inventory),
    "inventory_bytes": (R / "FILE_INVENTORY.jsonl").stat().st_size,
    "inventory_lf": (R / "FILE_INVENTORY.jsonl").read_bytes().count(b"\n"),
    "inventory_explicit_self_rows": 2,
    "symlinks": 0,
    "hardlink_aliases": 0,
    "files_with_nlink_not_one": 0,
    "all_paths_read_only": readonly,
    "writable_root_allowed": a.allow_writable_root,
    "ctime_immutability_claimed": False,
}
if a.output:
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
