#!/usr/bin/env python3
"""Bind the preserved first failed Round126 assembly without copying it again."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CHUNK = 8 << 20


def fsha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--failed-tree", type=Path, required=True)
p.add_argument("--work", type=Path, required=True)
a = p.parse_args()
root = a.failed_tree.resolve()
work = a.work.resolve()
assert root.is_dir() and not root.is_symlink()

files = []
for path in sorted(root.rglob("*")):
    assert not path.is_symlink(), path
    if path.is_file():
        files.append({
            "path": path.relative_to(root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": fsha(path),
        })

canonical_rows = "".join(
    f"{row['sha256']}  {row['bytes']}  {row['path']}\n" for row in files
).encode()
stderr = work / "logs/transcripts/assemble-round126-package-tree.stderr"
current_assembler = work / "source/assemble_package_tree_round126.py"
current_text = current_assembler.read_text()
fix = 'os.chmod(dst / "source", 0o755)\n'
assert current_text.count(fix) == 1
failed_text = current_text.replace(fix, "")
failed_source = work / "source/assemble_package_tree_round126.failed1.py"
failed_source.write_text(failed_text)

report = {
    "schema": "circdist-gross-round126-failed-assembly-inventory-v1",
    "status": "PRESERVED_AND_HASH_BOUND",
    "failed_tree_absolute_path": str(root),
    "failed_tree_directory_count": sum(1 for x in root.rglob("*") if x.is_dir()),
    "failed_tree_file_count": len(files),
    "failed_tree_total_bytes": sum(row["bytes"] for row in files),
    "canonical_inventory_sha256": hashlib.sha256(canonical_rows).hexdigest(),
    "canonical_inventory_definition": "SHA-256 of UTF-8 rows '<sha256>  <bytes>  <relative_path>\\n' in bytewise relative-path order",
    "files": files,
    "original_stderr": {
        "path": "logs/transcripts/assemble-round126-package-tree.stderr",
        "bytes": stderr.stat().st_size,
        "sha256": fsha(stderr),
    },
    "failed_assembler_reconstruction": {
        "path": "source/assemble_package_tree_round126.failed1.py",
        "sha256": hashlib.sha256(failed_text.encode()).hexdigest(),
        "derivation": "current corrected assembler with exactly the single owner-write chmod line removed",
    },
    "corrected_assembler": {
        "path": "source/assemble_package_tree_round126.py",
        "sha256": fsha(current_assembler),
    },
    "correction_scope": "After copying the sealed parent source tree, change only the new destination source directory mode to 0755 before overlaying ordinary copied Round126 source files; payload bytes and scientific inputs are unchanged.",
}
out = work / "work/recovery/FAILED_ASSEMBLY1_INVENTORY.json"
out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: report[k] for k in ("status", "failed_tree_file_count", "failed_tree_total_bytes", "canonical_inventory_sha256")}, sort_keys=True))
