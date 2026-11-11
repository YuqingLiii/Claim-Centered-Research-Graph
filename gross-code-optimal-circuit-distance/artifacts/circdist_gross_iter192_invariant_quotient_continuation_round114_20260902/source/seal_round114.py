#!/usr/bin/env python3
"""Create exact manifests and freeze the complete Round114 package."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, shutil

CHUNK = 8 << 20
GENERATED = {"FILE_INVENTORY.jsonl", "PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"}


def scan(path):
    digest = hashlib.sha256()
    size = lines = 0
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(CHUNK), b""):
            digest.update(block)
            size += len(block)
            lines += block.count(b"\n")
    return digest.hexdigest(), size, lines


def files(root):
    return sorted((p.relative_to(root).as_posix(), p) for p in root.rglob("*") if p.is_file())


def verify_manifest(root, name):
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
args = parser.parse_args()
root = args.root.resolve()

for cache in sorted(root.rglob("__pycache__"), reverse=True):
    if cache.is_dir():
        shutil.rmtree(cache)
assert not [p for p in root.rglob("*") if p.is_symlink()]
assert not [p for p in root.rglob("*") if p.is_file() and p.stat().st_nlink != 1]
assert not [p for p in root.rglob("*") if p.is_file() and p.name.endswith(".tmp")]
solver_raw_drat = [p for base in (root / "solver", root / "batch") if base.exists() for p in base.rglob("*.drat") if p.is_file()]
proof_control_raw_drat = [p for p in (root / "controls").rglob("*.drat") if p.is_file()]
assert not solver_raw_drat
for name in GENERATED:
    path = root / name
    if path.exists():
        path.chmod(path.stat().st_mode | 0o200)
        path.unlink()

payload = [(relative, path) for relative, path in files(root) if relative not in GENERATED]
(root / "PAYLOAD_SHA256SUMS.txt").write_text("".join(f"{scan(path)[0]}  {relative}\n" for relative, path in payload))
payload_rows = verify_manifest(root, "PAYLOAD_SHA256SUMS.txt")

substantive = [(relative, path) for relative, path in files(root) if relative not in {"FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}]
with (root / "FILE_INVENTORY.jsonl").open("w", encoding="utf-8", newline="\n") as output:
    for relative, path in substantive:
        digest, size, lines = scan(path)
        output.write(json.dumps({"bytes": size, "lines": lines, "path": relative, "sha256": digest}, sort_keys=True, separators=(",", ":")) + "\n")

root_entries = [(relative, path) for relative, path in files(root) if relative != "SHA256SUMS.txt"]
with (root / "SHA256SUMS.txt").open("w", encoding="utf-8", newline="\n") as output:
    for relative, path in root_entries:
        output.write(f"{scan(path)[0]}  {relative}\n")

root_rows = verify_manifest(root, "SHA256SUMS.txt")
actual = {relative for relative, _ in files(root)}
assert set(root_rows) == actual - {"SHA256SUMS.txt"} and len(root_rows) == len(actual) - 1
inventory = [json.loads(line) for line in (root / "FILE_INVENTORY.jsonl").read_text().splitlines()]
assert {row["path"] for row in inventory} == actual - {"FILE_INVENTORY.jsonl", "SHA256SUMS.txt"}
assert not [p for p in root.rglob("*") if p.is_file() and p.stat().st_nlink != 1]

result = {
    "schema": "circdist-gross-round114-full-root-seal-v1",
    "status": "PASS",
    "payload_rows": len(payload_rows),
    "payload_manifest_sha256": scan(root / "PAYLOAD_SHA256SUMS.txt")[0],
    "inventory_rows": len(inventory),
    "root_rows": len(root_rows),
    "physical_files": len(actual),
    "root_manifest_sha256": scan(root / "SHA256SUMS.txt")[0],
    "root_manifest_bytes": scan(root / "SHA256SUMS.txt")[1],
    "substantive_bytes": sum(row["bytes"] for row in inventory),
    "symlinks": 0,
    "files_with_nlink_not_one": 0,
    "raw_solver_or_batch_drat_files": 0,
    "raw_proof_control_drat_files": len(proof_control_raw_drat),
    "temporary_files": 0,
    "verified_after_write": True,
    "memory_safety": "fixed 8 MiB scans",
    "ctime_provenance_claimed": False,
}
package_files = [path for _, path in files(root)]
executable = 0
for path in package_files:
    is_executable = bool(path.stat().st_mode & 0o111)
    path.chmod(0o555 if is_executable else 0o444)
    executable += int(is_executable)
directories = sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True)
for path in directories:
    path.chmod(0o555)
root.chmod(0o555)
assert all(not (p.stat().st_mode & 0o222) for p in package_files + [root, *directories])
result.update({"content_frozen_read_only": True, "read_only_files": len(package_files), "read_only_directories": len(directories) + 1, "executable_files_preserved": executable})
print(json.dumps(result, sort_keys=True))
