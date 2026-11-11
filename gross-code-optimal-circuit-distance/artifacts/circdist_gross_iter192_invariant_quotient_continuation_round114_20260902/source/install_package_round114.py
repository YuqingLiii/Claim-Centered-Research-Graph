#!/usr/bin/env python3
"""Install the sealed package once using ordinary copies and verify isolation."""
from pathlib import Path
import argparse, hashlib, json, shutil

CHUNK = 8 << 20


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument("--source", type=Path, required=True)
parser.add_argument("--destination", type=Path, required=True)
args = parser.parse_args()
source, destination = args.source.resolve(), args.destination.resolve()
assert source.is_dir() and not destination.exists()
assert not [p for p in source.rglob("*") if p.is_symlink()]
shutil.copytree(source, destination, symlinks=False, copy_function=shutil.copy2)
source_files = sorted(p.relative_to(source).as_posix() for p in source.rglob("*") if p.is_file())
destination_files = sorted(p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file())
assert source_files == destination_files
for relative in source_files:
    left, right = source / relative, destination / relative
    assert sha(left) == sha(right)
    assert (left.stat().st_dev, left.stat().st_ino) != (right.stat().st_dev, right.stat().st_ino)
    assert left.stat().st_nlink == right.stat().st_nlink == 1
assert not [p for p in destination.rglob("*") if p.is_symlink()]
assert all(not (p.stat().st_mode & 0o222) for p in [destination, *destination.rglob("*")])
result = {
    "schema": "circdist-gross-round114-ordinary-copy-install-v1",
    "status": "PASS",
    "source": str(source),
    "destination": str(destination),
    "files": len(source_files),
    "byte_identical": True,
    "distinct_inode_every_file": True,
    "files_with_nlink_not_one": 0,
    "symlinks": 0,
    "destination_read_only": True,
    "copy_method": "Python shutil.copytree with shutil.copy2; no hardlinks",
    "ctime_provenance_claimed": False,
    "root_manifest_sha256": sha(destination / "SHA256SUMS.txt"),
}
print(json.dumps(result, sort_keys=True))
