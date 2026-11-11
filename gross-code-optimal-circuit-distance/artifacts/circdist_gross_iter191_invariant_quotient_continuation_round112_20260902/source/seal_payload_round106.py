#!/usr/bin/env python3
"""Seal the immutable science payload before the retained postseal replay."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json

CHUNK = 8 << 20
EXCLUDED = {
    "FILE_INVENTORY.jsonl", "PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt",
    "ENVIRONMENT.json", "RESULT.json", "PROCESS_FIX2_LEDGER.json",
    "verification/final_process_census.json", "verification/postseal_replay.json",
    "verification/result_consistency.json", "verification/payload_seal.json",
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    assert not any(p.is_symlink() for p in root.rglob("*"))
    rows = []
    for p in sorted(x for x in root.rglob("*") if x.is_file()):
        rel = p.relative_to(root).as_posix()
        if rel in EXCLUDED or rel.startswith("logs/postseal") or \
                rel.startswith("logs/process/postseal") or \
                rel.startswith("logs/payload") or \
                rel.startswith("logs/process/payload") or \
                rel.startswith("logs/final_census_postseal") or \
                rel.startswith("logs/process/final_census_postseal") or \
                rel.startswith("logs/metadata_postseal") or \
                rel.startswith("logs/process/metadata_postseal") or \
                rel.startswith("logs/result_consistency") or \
                rel.startswith("logs/process/result_consistency"):
            continue
        rows.append((rel, p, sha(p)))
    manifest = root / "PAYLOAD_SHA256SUMS.txt"
    manifest.write_text("".join(f"{digest}  {rel}\n" for rel, _, digest in rows))
    seen = set()
    for line in manifest.read_text().splitlines():
        digest, rel = line.split("  ", 1)
        posix = PurePosixPath(rel)
        assert rel == posix.as_posix() and not posix.is_absolute() and ".." not in posix.parts
        assert rel not in seen and sha(root / rel) == digest
        seen.add(rel)
    result = {"schema": "circdist-gross-round106-immutable-payload-seal-v1",
              "status": "PASS", "manifest": "PAYLOAD_SHA256SUMS.txt",
              "manifest_sha256": sha(manifest), "manifest_bytes": manifest.stat().st_size,
              "rows": len(rows), "excluded_mutable_metadata": sorted(EXCLUDED),
              "scope": "immutable scientific payload sealed before retained postseal replay; final root manifest later covers every package file",
              "verified_after_write": True, "symlinks": 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
