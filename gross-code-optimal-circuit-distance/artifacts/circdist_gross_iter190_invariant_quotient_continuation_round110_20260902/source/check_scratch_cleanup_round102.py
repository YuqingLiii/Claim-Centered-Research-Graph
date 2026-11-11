#!/usr/bin/env python3
"""Assert that no Round102 scratch or uncompressed large solver stream survives."""
from pathlib import Path
import argparse
import json
import tempfile


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()

temporary_suffixes = (".tmp", ".partial", ".part")
package_temporary = sorted(
    path.relative_to(root).as_posix()
    for path in root.rglob("*")
    if (path.is_file() and path.name.endswith(temporary_suffixes))
    or (path.is_dir() and path.name in {"scratch", ".scratch", "tmp", ".tmp"})
)
system_temp = Path(tempfile.gettempdir())
system_survivors = sorted(
    path.as_posix()
    for pattern in ("circdist-round102-*", "circdist-r96-proof-control.*")
    for path in system_temp.glob(pattern)
)
corrected = root / "frontier/iter186_full_invariant_quotient"
raw_large_streams = sorted(
    path.relative_to(root).as_posix()
    for path in corrected.rglob("*.drat")
)
assert not package_temporary, package_temporary
assert not system_survivors, system_survivors
assert not raw_large_streams, raw_large_streams

result = {
    "schema": "circdist-gross-round102-scratch-cleanup-v1",
    "status": "PASS",
    "package_temporary_survivors": package_temporary,
    "system_round102_temporary_survivors": system_survivors,
    "corrected_raw_large_solver_streams": raw_large_streams,
    "scratch_survivor_count": 0,
    "raw_large_stream_survivor_count": 0,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
