#!/usr/bin/env python3
"""Independently verify Round114 manifests, inventory, modes, links, and canonical identity."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json

CHUNK = 8 << 20
CANONICAL_SHA256 = "25d39fbd9add4f5c0d9b7fea76ab2ede1f0c5c3711cd7a152ca98bbde351a834"


def scan(path):
    digest = hashlib.sha256()
    size = lines = 0
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(CHUNK), b""):
            digest.update(block)
            size += len(block)
            lines += block.count(b"\n")
    return digest.hexdigest(), size, lines


def manifest(root, name):
    rows = []
    for number, line in enumerate((root / name).read_text().splitlines(), 1):
        digest, separator, relative = line.partition("  ")
        assert separator and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
        posix = PurePosixPath(relative)
        assert relative == posix.as_posix() and not posix.is_absolute() and ".." not in posix.parts
        path = root / relative
        assert path.is_file() and not path.is_symlink() and scan(path)[0] == digest, (name, number, relative)
        rows.append(relative)
    assert rows == sorted(rows) and len(rows) == len(set(rows))
    return rows


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
assert not [p for p in root.rglob("*") if p.is_symlink()]
payload = manifest(root, "PAYLOAD_SHA256SUMS.txt")
root_rows = manifest(root, "SHA256SUMS.txt")
actual = sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())
assert set(root_rows) == set(actual) - {"SHA256SUMS.txt"} and len(root_rows) == len(actual) - 1
inventory = []
for number, line in enumerate((root / "FILE_INVENTORY.jsonl").read_text().splitlines(), 1):
    row = json.loads(line)
    digest, size, lines = scan(root / row["path"])
    assert (digest, size, lines) == (row["sha256"], row["bytes"], row["lines"]), (number, row["path"])
    inventory.append(row)
assert [row["path"] for row in inventory] == sorted(row["path"] for row in inventory)
assert len(inventory) == len({row["path"] for row in inventory})
assert set(row["path"] for row in inventory) == set(actual) - {"FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}
files = [root / relative for relative in actual]
directories = [root, *[p for p in root.rglob("*") if p.is_dir()]]
assert all(not (p.stat().st_mode & 0o222) for p in files + directories)
assert all(p.stat().st_nlink == 1 for p in files)
assert scan(root / "PROPOSED_CIRCDIST.gross.yaml")[0] == scan(root / "bindings/CIRCDIST.gross.yaml")[0] == CANONICAL_SHA256
result = {
    "schema": "circdist-gross-round114-independent-sealed-root-verification-v1",
    "status": "PASS",
    "root_manifest_sha256": scan(root / "SHA256SUMS.txt")[0],
    "root_manifest_bytes": scan(root / "SHA256SUMS.txt")[1],
    "root_manifest_lf": scan(root / "SHA256SUMS.txt")[2],
    "root_rows": len(root_rows),
    "payload_manifest_sha256": scan(root / "PAYLOAD_SHA256SUMS.txt")[0],
    "payload_manifest_bytes": scan(root / "PAYLOAD_SHA256SUMS.txt")[1],
    "payload_manifest_lf": scan(root / "PAYLOAD_SHA256SUMS.txt")[2],
    "payload_rows": len(payload),
    "inventory_rows": len(inventory),
    "physical_files": len(actual),
    "substantive_bytes": sum(row["bytes"] for row in inventory),
    "substantive_lf": sum(row["lines"] for row in inventory),
    "symlinks": 0,
    "files_with_nlink_not_one": 0,
    "writable_files": 0,
    "writable_directories": 0,
    "canonical_yaml_unchanged": True,
    "ctime_provenance_claimed": False,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
