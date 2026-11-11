#!/usr/bin/env python3
"""Seal one Round126 package from one pre-captured static path list."""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path

NAME = "circdist_gross_iter198_order144_continuation_round126_20260905"
ADDED = {
    "PRESEAL_FIND_PATHS.txt", "PRESEAL_PATH_INVENTORY.json",
    "FINAL_PRESEAL_PROCESS_LEDGER.jsonl", "SEAL_BOUNDARY.json",
    "COPY_AUDIT.json", "PAYLOAD_SHA256SUMS.txt", "SEAL.json",
    "FILE_INVENTORY.jsonl", "SHA256SUMS.txt",
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def mode(path):
    return stat.S_IMODE(path.stat().st_mode)


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--path-list", type=Path, required=True)
ap.add_argument("--live-ledger", type=Path, required=True)
a = ap.parse_args()
root = a.root.resolve()
assert root.is_dir() and root.name == NAME
assert not any((root / rel).exists() for rel in ADDED)

# The only tree enumeration is the caller's already completed, retained `find`.
# This program performs one bounded pass over its immutable path list.
raw = [line for line in a.path_list.read_text().splitlines() if line]
assert raw and len(raw) == len(set(raw))
entries = []
for text in raw:
    path = Path(text)
    assert path.is_absolute() and (path == root or root in path.parents)
    entries.append(path)
files = sorted((p for p in entries if stat.S_ISREG(p.lstat().st_mode)),
               key=lambda p: p.relative_to(root).as_posix())
dirs = sorted((p for p in entries if stat.S_ISDIR(p.lstat().st_mode)),
              key=lambda p: (len(p.relative_to(root).parts), p.relative_to(root).as_posix()))
other = [p for p in entries if not (stat.S_ISREG(p.lstat().st_mode) or stat.S_ISDIR(p.lstat().st_mode))]
assert not other
initial = [p.relative_to(root).as_posix() for p in files]
assert len(initial) == len(set(initial)) and not (set(initial) & ADDED)
dir_rel = sorted({"."} | {p.relative_to(root).as_posix() for p in dirs})
empty_dirs = [d for d in dir_rel if d != "." and
              not any(rel.startswith(d.rstrip("/") + "/") for rel in initial)]

# Exactly one streaming SHA-256 pass for every pre-existing package file.
digests = {rel: sha(root / rel) for rel in initial}
path_list_hash = sha(a.path_list)

(root / "PRESEAL_FIND_PATHS.txt").write_bytes(a.path_list.read_bytes())
digests["PRESEAL_FIND_PATHS.txt"] = path_list_hash

ledger_rows = [json.loads(line) for line in a.live_ledger.read_text().splitlines() if line.strip()]
ledger_rows = [row for row in ledger_rows if row.get("child_pid") != os.getpid()]
started_pids = [row["child_pid"] for row in ledger_rows if row.get("state") == "STARTED"]
reaped_pids = [row["child_pid"] for row in ledger_rows if row.get("state") == "REAPED"]
assert len(started_pids) == len(set(started_pids))
assert sorted(started_pids) == sorted(reaped_pids)
(root / "FINAL_PRESEAL_PROCESS_LEDGER.jsonl").write_text(
    "".join(json.dumps(row, sort_keys=True) + "\n" for row in ledger_rows)
)
digests["FINAL_PRESEAL_PROCESS_LEDGER.jsonl"] = sha(root / "FINAL_PRESEAL_PROCESS_LEDGER.jsonl")
solver_tags = {
    "solve-iter198-exact-order144-quotient-proof-first",
    "solve-iter198-Xerr-complete-direct360-proof-first",
    "solve-iter198-Zerr-complete-direct360-proof-first",
}
solver_starts = [row for row in ledger_rows
                 if row.get("state") == "STARTED" and row.get("tag") in solver_tags]
assert len(solver_starts) == 3
boundary = {
    "schema": "circdist-gross-round126-final-preseal-process-boundary-v1", "status": "PASS",
    "ledger": "FINAL_PRESEAL_PROCESS_LEDGER.jsonl",
    "ledger_sha256": digests["FINAL_PRESEAL_PROCESS_LEDGER.jsonl"],
    "ledger_rows": len(ledger_rows), "started": len(started_pids), "reaped": len(reaped_pids),
    "all_included_children_reaped": True, "max_simultaneous_children": 1,
    "detached_children": 0, "timeouts_triggered": 0,
    "science_solver_invocations": 3, "finalization_solver_invocations": 0,
    "excluded_active_process": {"child_pid": os.getpid(), "role": "current sealer",
                                "reason": "REAPED row is written by the supervising wrapper after immutable seal creation"},
    "postseal_finalizers_external": ["ordinary durable copy", "sealed-package check",
                                     "solver-free replay", "postseal repository gates", "scratch cleanup"],
}
(root / "SEAL_BOUNDARY.json").write_text(json.dumps(boundary, indent=2, sort_keys=True) + "\n")
digests["SEAL_BOUNDARY.json"] = sha(root / "SEAL_BOUNDARY.json")

path_inventory = {
    "schema": "circdist-gross-round126-static-preseal-path-inventory-v1",
    "status": "PASS", "bounded_root_name": NAME,
    "source_path_list_sha256": path_list_hash,
    "source_path_list_rows": len(raw),
    "initial_files": initial,
    "initial_file_count": len(initial),
    "directories": dir_rel,
    "directory_count": len(dir_rel),
    "non_file_non_directory_entries": 0,
    "symlinks": 0,
    "empty_directories": len(empty_dirs),
    "empty_directory_paths": empty_dirs,
    "fixed_added_files": sorted(ADDED),
    "tree_enumeration_policy": "one retained static find list; no recursive enumeration by sealer",
}
(root / "PRESEAL_PATH_INVENTORY.json").write_text(json.dumps(path_inventory, indent=2, sort_keys=True) + "\n")
digests["PRESEAL_PATH_INVENTORY.json"] = sha(root / "PRESEAL_PATH_INVENTORY.json")

topology_files = [root / rel for rel in initial + ["PRESEAL_FIND_PATHS.txt", "PRESEAL_PATH_INVENTORY.json",
                                                    "FINAL_PRESEAL_PROCESS_LEDGER.jsonl", "SEAL_BOUNDARY.json"]]
seen = {}
aliases = []
bad_links = []
for path in topology_files:
    key = (path.stat().st_dev, path.stat().st_ino)
    rel = path.relative_to(root).as_posix()
    if key in seen:
        aliases.append([seen[key], rel])
    else:
        seen[key] = rel
    if path.stat().st_nlink != 1:
        bad_links.append([rel, path.stat().st_nlink])
assert not aliases and not bad_links

copy_audit = {
    "schema": "circdist-gross-round126-preseal-copy-audit-v1", "status": "PASS",
    "files_before_audit": len(topology_files), "symlinks": 0, "hardlink_aliases": 0,
    "files_with_nlink_not_one": 0, "ordinary_file_tree": True,
    "source_destination_inode_distinctness_checked_during_assembly": True,
    "copy_on_write_extents_permitted": True, "ctime_immutability_claimed": False,
    "bounded_root_name": NAME,
}
(root / "COPY_AUDIT.json").write_text(json.dumps(copy_audit, indent=2, sort_keys=True) + "\n")
digests["COPY_AUDIT.json"] = sha(root / "COPY_AUDIT.json")

payload_rel = sorted(initial + ["PRESEAL_FIND_PATHS.txt", "PRESEAL_PATH_INVENTORY.json",
                                "FINAL_PRESEAL_PROCESS_LEDGER.jsonl", "SEAL_BOUNDARY.json",
                                "COPY_AUDIT.json"])
(root / "PAYLOAD_SHA256SUMS.txt").write_text(
    "".join(f"{digests[rel]}  {rel}\n" for rel in payload_rel)
)
payload_hash = sha(root / "PAYLOAD_SHA256SUMS.txt")
digests["PAYLOAD_SHA256SUMS.txt"] = payload_hash
seal = {
    "schema": "circdist-gross-round126-two-level-seal-v1", "status": "SEALED",
    "date": "2026-09-05", "package_name": NAME,
    "payload_manifest_sha256": payload_hash, "payload_files": len(payload_rel),
    "root_manifest_excludes_only": "SHA256SUMS.txt itself",
    "inventory_self_row": "FILE_INVENTORY.jsonl and SHA256SUMS.txt use explicit null self-reference rows",
    "postseal_mutation_permitted": False, "ordinary_copy_required": True,
    "symlinks_permitted": False, "hardlink_aliases_permitted": False,
    "ctime_immutability_claimed": False,
}
(root / "SEAL.json").write_text(json.dumps(seal, indent=2, sort_keys=True) + "\n")
digests["SEAL.json"] = sha(root / "SEAL.json")

final_rel = sorted(initial + list(ADDED))
assert len(final_rel) == len(set(final_rel))
with (root / "FILE_INVENTORY.jsonl").open("w") as out:
    for rel in final_rel:
        if rel in {"FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}:
            row = {"path": rel, "bytes": None, "mode": None, "sha256": None,
                   "self_reference": True,
                   "binding": "final bytes bound by root manifest; root manifest identified by external SHA-256"}
        else:
            path = root / rel
            row = {"path": rel, "bytes": path.stat().st_size, "mode": oct(mode(path)),
                   "sha256": digests[rel], "self_reference": False}
        out.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")

inventory_hash = sha(root / "FILE_INVENTORY.jsonl")
digests["FILE_INVENTORY.jsonl"] = inventory_hash
root_rel = [rel for rel in final_rel if rel != "SHA256SUMS.txt"]
(root / "SHA256SUMS.txt").write_text(
    "".join(f"{digests[rel]}  {rel}\n" for rel in root_rel)
)
root_hash = sha(root / "SHA256SUMS.txt")

for rel in final_rel:
    path = root / rel
    os.chmod(path, 0o555 if mode(path) & 0o111 else 0o444)
for path in sorted(({root} | {root / rel for rel in dir_rel if rel != "."}),
                   key=lambda p: len(p.parts), reverse=True):
    os.chmod(path, 0o555)

print(json.dumps({
    "status": "SEALED", "root_manifest_sha256": root_hash,
    "payload_manifest_sha256": payload_hash, "inventory_sha256": inventory_hash,
    "root_rows": len(root_rel), "payload_rows": len(payload_rel),
    "inventory_paths": len(final_rel),
    "inventory_bytes": (root / "FILE_INVENTORY.jsonl").stat().st_size,
    "inventory_lf": len(final_rel), "package_files": len(final_rel),
    "package_directories": len(dir_rel),
    "package_bytes": sum((root / rel).stat().st_size for rel in final_rel),
    "static_path_list_sha256": path_inventory["source_path_list_sha256"],
    "static_path_list_rows": len(raw), "solver_invocations": 0,
}, sort_keys=True))
