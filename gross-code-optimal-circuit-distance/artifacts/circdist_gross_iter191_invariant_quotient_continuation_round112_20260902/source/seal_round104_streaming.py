#!/usr/bin/env python3
"""Create and verify the idempotent Round104 two-level package seal."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json

CHUNK = 8 << 20
GENERATED = {"FILE_INVENTORY.jsonl", "PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"}


def scan(path):
    h = hashlib.sha256()
    size = lf = 0
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(CHUNK), b""):
            h.update(chunk)
            size += len(chunk)
            lf += chunk.count(b"\n")
    return h.hexdigest(), size, lf


def files(root):
    return sorted((p.relative_to(root).as_posix(), p) for p in root.rglob("*") if p.is_file())


def write_hashes(path, rows):
    with path.open("w", encoding="utf-8", newline="\n") as out:
        for rel, source in rows:
            out.write(f"{scan(source)[0]}  {rel}\n")


def parse_and_verify(root, name):
    rows = []
    for number, line in enumerate((root / name).read_text().splitlines(), 1):
        digest, sep, rel = line.partition("  ")
        assert sep and len(digest) == 64 and all(c in "0123456789abcdef" for c in digest)
        posix = PurePosixPath(rel)
        assert not posix.is_absolute() and rel == posix.as_posix() and ".." not in posix.parts
        path = root / rel
        assert path.is_file() and not path.is_symlink() and scan(path)[0] == digest, (name, number, rel)
        rows.append(rel)
    assert rows == sorted(rows) and len(rows) == len(set(rows))
    return set(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    symlinks = [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_symlink()]
    assert not symlinks, symlinks
    for name in GENERATED:
        path = root / name
        if path.exists():
            path.unlink()
    substantive = [(rel, path) for rel, path in files(root) if rel not in GENERATED]
    total_bytes = total_lf = 0
    with (root / "FILE_INVENTORY.jsonl").open("w", encoding="utf-8", newline="\n") as out:
        for rel, path in substantive:
            digest, size, lf = scan(path)
            total_bytes += size
            total_lf += lf
            out.write(json.dumps({"bytes": size, "lines": lf, "path": rel,
                                  "sha256": digest}, sort_keys=True,
                                 separators=(",", ":")) + "\n")
    payload_rows = [(rel, path) for rel, path in files(root)
                    if rel not in {"PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"}]
    write_hashes(root / "PAYLOAD_SHA256SUMS.txt", payload_rows)
    root_rows = [(rel, path) for rel, path in files(root) if rel != "SHA256SUMS.txt"]
    write_hashes(root / "SHA256SUMS.txt", root_rows)
    root_set = parse_and_verify(root, "SHA256SUMS.txt")
    payload_set = parse_and_verify(root, "PAYLOAD_SHA256SUMS.txt")
    actual = {rel for rel, _ in files(root)}
    assert root_set == actual - {"SHA256SUMS.txt"}
    assert payload_set == actual - {"SHA256SUMS.txt", "PAYLOAD_SHA256SUMS.txt"}
    assert root_set == payload_set | {"PAYLOAD_SHA256SUMS.txt"}
    root_sha, root_bytes, root_lf = scan(root / "SHA256SUMS.txt")
    payload_sha, payload_bytes, payload_lf = scan(root / "PAYLOAD_SHA256SUMS.txt")
    print(json.dumps({"schema": "circdist-gross-round104-two-level-seal-v1",
                      "status": "PASS", "substantive_files": len(substantive),
                      "substantive_bytes": total_bytes, "substantive_lf": total_lf,
                      "inventory_rows": len(substantive), "payload_rows": len(payload_rows),
                      "root_rows": len(root_rows), "physical_files": len(actual),
                      "payload_manifest_sha256": payload_sha,
                      "payload_manifest_bytes": payload_bytes,
                      "payload_manifest_lf": payload_lf,
                      "root_manifest_sha256": root_sha,
                      "root_manifest_bytes": root_bytes, "root_manifest_lf": root_lf,
                      "symlinks": 0, "verified_after_write": True,
                      "memory_safety": "all files scanned in fixed 8 MiB chunks"}, sort_keys=True))


if __name__ == "__main__":
    main()
