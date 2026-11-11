#!/usr/bin/env python3
"""Create deterministic corrupt and final-record-truncated proof controls."""
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--drat", type=Path, required=True)
parser.add_argument("--lrat", type=Path, required=True)
parser.add_argument("--output-dir", type=Path, required=True)
args = parser.parse_args()
args.output_dir.mkdir(parents=True, exist_ok=True)

drat_lines = args.drat.read_bytes().splitlines(keepends=True)
lrat_lines = args.lrat.read_bytes().splitlines(keepends=True)
assert len(drat_lines) > 1 and drat_lines[-1].strip() == b"0"
assert len(lrat_lines) > 1 and b" 0 " in lrat_lines[-1]

drat_raw = args.drat.read_bytes()
(args.output_dir / "php6_5.truncated.drat").write_bytes(
    drat_raw[:max(1, len(drat_raw) // 2)])
(args.output_dir / "php6_5.corrupt.drat").write_bytes(b"not-a-valid-proof\n")
(args.output_dir / "php6_5.truncated.lrat").write_bytes(b"".join(lrat_lines[:-1]))
(args.output_dir / "php6_5.corrupt.lrat").write_bytes(b"not-a-valid-lrat\n")

print(json.dumps({
    "status": "PASS",
    "drat_records": len(drat_lines),
    "lrat_records": len(lrat_lines),
    "drat_truncation": "retained the first half of the byte stream",
    "lrat_truncation": "removed the final proof record",
}, sort_keys=True))
