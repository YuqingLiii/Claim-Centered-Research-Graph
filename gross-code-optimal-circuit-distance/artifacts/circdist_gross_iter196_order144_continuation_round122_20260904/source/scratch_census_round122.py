#!/usr/bin/env python3
"""Bounded census of the Round122-owned scratch tree."""
import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
root = a.root.resolve()
assert str(root) == "/private/tmp/circdist-round122-proposer"
files = [p for p in root.rglob("*") if p.is_file() and not p.is_symlink()]
dirs = [p for p in root.rglob("*") if p.is_dir() and not p.is_symlink()]
large = sorted(({"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size}
                for p in files if p.stat().st_size >= 100_000_000),
               key=lambda row: (-row["bytes"], row["path"]))
raw = sorted(p.relative_to(root).as_posix() for p in files
             if p.suffix in {".drat", ".proof"} and not p.name.endswith(".gz"))
out = {"schema": "circdist-round122-scratch-census-v1", "status": "PASS",
       "root": str(root), "files": len(files), "directories": len(dirs) + 1,
       "bytes": sum(p.stat().st_size for p in files), "large_files": large,
       "uncompressed_proof_streams": raw}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "files": len(files), "directories": len(dirs) + 1,
                  "bytes": out["bytes"], "large_files": len(large),
                  "uncompressed_proof_streams": len(raw)}, sort_keys=True))
