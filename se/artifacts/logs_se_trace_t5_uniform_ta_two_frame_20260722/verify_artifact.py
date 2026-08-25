#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


checked = 0
for line in (HERE / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    want, name = line.split(maxsplit=1)
    path = HERE / name.strip().lstrip("*")
    assert path.is_file() and digest(path) == want, name
    checked += 1
data = json.loads((HERE / "uniform_ta_two_frame.json").read_text(encoding="utf-8"))
assert data["verdict"] == "REFUTED"
assert len(data["tame_c2_gates"]) == 2
assert all(x["all_d_long_squared_le_B"] and x["normalized_below_two_frame_rank_bound"]
           and x["raw_registered_T_a_fails"]
           and x["raw_registered_T_b_finite_gate_passes"]
           for x in data["tame_c2_gates"])
assert len(data["j1_closed_form_rows"]) == 28
print(f"SHA256 {checked}/{checked} PASS")
print("INVARIANTS PASS")
