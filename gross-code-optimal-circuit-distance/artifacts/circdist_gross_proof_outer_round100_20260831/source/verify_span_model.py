#!/usr/bin/env python3
"""Replay a complete SAT model for the exact full-span synthesis query."""
from pathlib import Path
import argparse
import hashlib
import json
import struct
import sys


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def object_sha256(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def from_words(words):
    return sum(int(word) << (64 * i) for i, word in enumerate(words))


def parse_rows(path):
    raw = Path(path).read_bytes()
    assert raw[:16] == b"CDR98O5V1\0\0\0\0\0\0\0"
    count = struct.unpack_from("<Q", raw, 16)[0]
    assert len(raw) == 24 + count * 19 * 8
    rows = []
    for index in range(count):
        values = struct.unpack_from("<19Q", raw, 24 + index * 19 * 8)
        rows.append((values[0], from_words(values[1:7]), from_words(values[7:10]),
                     from_words(values[10:13]), from_words(values[13:15]),
                     from_words(values[15:17]), values[17], values[18]))
    return rows


def bit_positions(value):
    return [i for i in range(value.bit_length()) if (value >> i) & 1]


def parity_mask(support, duals, popcount):
    result = 0
    for i, dual in enumerate(duals):
        result |= (popcount(support & dual) & 1) << i
    return result


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--sector", choices=("Xerr", "Zerr"), required=True)
parser.add_argument("--assignment", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
synthesis = root / "synthesis"
span = synthesis / "span"
metadata = json.loads((span / f"{args.sector}.metadata.json").read_text())
rows = parse_rows(synthesis / f"order5_input/{args.sector}.rows.bin")
ids = json.loads((synthesis / f"order5_input/{args.sector}.ids.json").read_text())
state = json.loads((synthesis / "inputs/iter137_state.json").read_text())
candidate = json.loads((synthesis / "inputs/iter136_candidate.json").read_text())
names = json.loads((synthesis / "order5_input/name_universe.json").read_text())
assert len(rows) == len(ids) == metadata["row_count"]
lines = args.assignment.read_text().splitlines()
assert lines[0] == "s SATISFIABLE"
signed = []
for line in lines[1:]:
    if line.startswith("v "):
        signed.extend(int(value) for value in line.split()[1:] if value != "0")
assert len(signed) == metadata["variables"]
assert {abs(value) for value in signed} == set(range(1, metadata["variables"] + 1))
truth = bytearray(metadata["variables"] + 1)
for value in signed:
    truth[abs(value)] = value > 0
selected_indices = [index for index, variable in enumerate(metadata["coefficient_variables"]) if truth[variable]]
effect = [0] * 7
for index in selected_indices:
    for component, value in enumerate(rows[index][1:]):
        effect[component] ^= value
named, canonical, physical, canonical_syndrome, physical_syndrome, canonical_logical, physical_logical = effect
assert all(bool(truth[variable]) == bool((named >> bit) & 1)
           for bit, variable in enumerate(metadata["name_variables"]))
assert 1 <= named.bit_count() <= 10
assert canonical_syndrome == physical_syndrome == 0
assert canonical_logical == physical_logical != 0
existing_masks = {row[1] for row in rows}
assert named not in existing_masks

vendor = root / "vendor/round80"
sys.path[:0] = [str(vendor / "src/round63_src"), str(vendor / "src")]
import model
import round68_build as builder

_, _, logical_x, logical_z = builder.load_context()
times = {key: int(value) for key, value in candidate["compressed_times"].items()}
assert object_sha256(times) == candidate["compressed_schedule_sha256"]
assert model.audit_schedule(times, True) == candidate["frozen_audit"] and candidate["frozen_audit"]["ok"]
sector = builder.sectors(times, logical_x, logical_z)[args.sector]
by_name = {column.name: column for column in sector.columns}
selected_names = [names[index] for index in bit_positions(named)]
canonical_replay = model.verify_named_selection(sector, selected_names, 10)
assert canonical_replay["ok"]
assert canonical_replay["net_support"] == bit_positions(canonical)
assert canonical_replay["syndrome"] == []
assert canonical_replay["logical_parities"] == [((canonical_logical >> i) & 1) for i in range(12)]
physical_replay = 0
for name in selected_names:
    physical_replay ^= by_name[name].physical_support
assert physical_replay == physical
assert sector.syndrome_of(physical_replay) == 0
assert parity_mask(physical_replay, sector.logical_duals, model.popcount) == physical_logical
result = {
    "schema": "circdist-round100-full-span-sat-witness-v1",
    "status": "PASS",
    "sector": args.sector,
    "formula_sha256": metadata["cnf_sha256"],
    "assignment_sha256": file_sha256(args.assignment),
    "complete_assignment": True,
    "selected_coefficient_count": len(selected_indices),
    "selected_coefficient_indices": selected_indices,
    "selected_coefficient_ids": [ids[index] for index in selected_indices],
    "selected_names": selected_names,
    "named_weight": len(selected_names),
    "named_mask_sha256": hashlib.sha256(named.to_bytes(45, "little")).hexdigest(),
    "canonical_support": bit_positions(canonical),
    "physical_support": bit_positions(physical),
    "canonical_syndrome": [],
    "physical_syndrome": [],
    "canonical_logical_parities": [((canonical_logical >> i) & 1) for i in range(12)],
    "physical_logical_parities": [((physical_logical >> i) & 1) for i in range(12)],
    "canonical_physical_parities_equal": True,
    "canonical_replay": canonical_replay,
    "physical_replay": True,
    "novel_vs_every_installed_sector_selector": True,
    "source_schedule_sha256": candidate["compressed_schedule_sha256"],
}
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "sector": args.sector,
                  "coefficient_count": len(selected_indices), "named_weight": len(selected_names)}, sort_keys=True))
