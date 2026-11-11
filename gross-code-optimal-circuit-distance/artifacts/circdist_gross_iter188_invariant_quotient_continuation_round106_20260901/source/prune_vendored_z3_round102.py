#!/usr/bin/env python3
"""Remove non-macOS and duplicate libraries from the bound local Z3 wheel."""
from pathlib import Path
import argparse
import hashlib
import json


parser = argparse.ArgumentParser()
parser.add_argument("--site-packages", type=Path, required=True)
args = parser.parse_args()
library = args.site_packages / "z3" / "lib"
keep = library / "libz3.dylib"
assert keep.is_file()
keep_sha = hashlib.sha256(keep.read_bytes()).hexdigest()
removed = []
for path in sorted(library.iterdir()):
    if path == keep:
        continue
    removed.append({"name": path.name, "bytes": path.stat().st_size})
    path.unlink()
print(json.dumps({
    "status": "PASS",
    "kept": str(keep),
    "kept_sha256": keep_sha,
    "removed": removed,
    "removed_bytes": sum(row["bytes"] for row in removed),
}, sort_keys=True))
