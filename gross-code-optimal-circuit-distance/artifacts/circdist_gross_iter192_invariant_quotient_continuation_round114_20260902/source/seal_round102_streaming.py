#!/usr/bin/env python3
"""Create the Round102 two-level seal without loading multi-gigabyte files.

Level 0 is FILE_INVENTORY.jsonl over the substantive payload.  Level 1 is
PAYLOAD_SHA256SUMS.txt over that payload plus the inventory.  The root
SHA256SUMS.txt covers Level 1 as well.  The root-manifest digest is the package
identity reported to reviewers.
"""
from pathlib import Path
import argparse
import hashlib
import json


CHUNK = 8 << 20
GENERATED = {"FILE_INVENTORY.jsonl", "PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"}


def scan(path):
    digest = hashlib.sha256()
    size = 0
    lf = 0
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
            size += len(block)
            lf += block.count(b"\n")
    return digest.hexdigest(), size, lf


def files(root):
    return sorted((p.relative_to(root).as_posix(), p)
                  for p in root.rglob("*") if p.is_file())


def write_hashes(path, rows):
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for rel, source in rows:
            handle.write(f"{scan(source)[0]}  {rel}\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    for name in GENERATED:
        target = root / name
        if target.exists():
            target.unlink()

    substantive = [(rel, path) for rel, path in files(root) if rel not in GENERATED]
    total_bytes = 0
    total_lf = 0
    with (root / "FILE_INVENTORY.jsonl").open("w", encoding="utf-8", newline="\n") as out:
        for rel, path in substantive:
            digest, size, lf = scan(path)
            total_bytes += size
            total_lf += lf
            out.write(json.dumps({"bytes": size, "lines": lf, "path": rel,
                                  "sha256": digest},
                                 sort_keys=True, separators=(",", ":")) + "\n")

    payload_rows = [(rel, path) for rel, path in files(root)
                    if rel not in {"PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"}]
    write_hashes(root / "PAYLOAD_SHA256SUMS.txt", payload_rows)
    root_rows = [(rel, path) for rel, path in files(root) if rel != "SHA256SUMS.txt"]
    write_hashes(root / "SHA256SUMS.txt", root_rows)

    root_sha, root_bytes, root_lf = scan(root / "SHA256SUMS.txt")
    payload_sha, payload_bytes, payload_lf = scan(root / "PAYLOAD_SHA256SUMS.txt")
    print(json.dumps({
        "schema": "circdist-round102-streaming-two-level-seal-v1",
        "status": "PASS",
        "substantive_files": len(substantive),
        "substantive_bytes": total_bytes,
        "substantive_lf": total_lf,
        "inventory_rows": len(substantive),
        "payload_rows": len(payload_rows),
        "root_rows": len(root_rows),
        "payload_manifest_sha256": payload_sha,
        "payload_manifest_bytes": payload_bytes,
        "payload_manifest_lf": payload_lf,
        "root_manifest_sha256": root_sha,
        "root_manifest_bytes": root_bytes,
        "root_manifest_lf": root_lf,
        "memory_safety": "all payload files scanned in fixed 8 MiB chunks",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
