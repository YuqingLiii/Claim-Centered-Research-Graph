#!/usr/bin/env python3
"""Deterministically adapt the reviewed Round124 frontier advance to Round126."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path("/private/tmp/circdist-round126-proposer-20260905")
TARGET = ROOT / "source/advance_css_closed_frontier_round126.py"
REPORT = ROOT / "work/recovery/FRONTIER_ADVANCE_ADAPTATION.json"
EXPECTED_INPUT_SHA256 = "539d612a479fea6eafa6dc7797fba0437f1c8db347f6ff6ecd2ee1f179fd2438"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


raw = TARGET.read_bytes()
assert sha256_bytes(raw) == EXPECTED_INPUT_SHA256
text = raw.decode("utf-8")


def replace_exact(old: str, new: str, expected_count: int = 1) -> None:
    global text
    count = text.count(old)
    assert count == expected_count, (old, count, expected_count)
    text = text.replace(old, new)


replace_exact("Build deterministic iteration 198", "Build deterministic iteration 199")
replace_exact("assert len(old_skeys) == len(old_sset) == 51552", "assert len(old_skeys) == len(old_sset) == 51840")
replace_exact("assert len(selectors) == 51840", "assert len(selectors) == 52128")
replace_exact('"source_iteration": 197', '"source_iteration": 198', 3)
replace_exact("r124", "r126", 9)
replace_exact("round124", "round126", 32)
replace_exact("iter197", "iter198", 4)
replace_exact("iteration198", "iteration199", 1)
replace_exact('"next_iteration": 198', '"next_iteration": 199')
replace_exact(
    '"scope": "fresh checked unstarted iteration-198 source after four sound iter198 mechanism/CSS orbits; no iteration-198 solver disposition"',
    '"scope": "fresh checked unstarted iteration-199 source after four sound iter198 mechanism/CSS orbits; no iteration-199 solver disposition"',
)
replace_exact('"fresh_frontier": {"iteration": 198', '"fresh_frontier": {"iteration": 199')

assert "round124" not in text
assert "r124" not in text
assert "iter197" not in text
assert "iteration198" not in text
assert "51552" not in text
assert text.count('"source_iteration": 198') == 3
assert text.count("51840") == 1
assert text.count("52128") == 1
ast.parse(text, filename=str(TARGET))
output = text.encode("utf-8")
TARGET.write_bytes(output)
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(
    json.dumps(
        {
            "schema": "circdist-round126-reviewed-source-adaptation-v1",
            "status": "PASS",
            "input_sha256": EXPECTED_INPUT_SHA256,
            "output_sha256": sha256_bytes(output),
            "target": str(TARGET),
            "syntax": "PASS via ast.parse with no bytecode write",
            "adaptation": "Round124 iteration-198 advance specialized to Round126 iteration-199; input selector count 51840 and output selector count 52128",
        },
        indent=2,
        sort_keys=True,
    )
    + "\n"
)
print(REPORT.read_text(), end="")
