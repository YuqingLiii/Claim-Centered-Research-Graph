#!/usr/bin/env python3
"""Adapt the exact reviewed streaming SAT-trace compressor to Round126."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

root = Path("/private/tmp/circdist-round126-proposer-20260905")
source = Path("<repo>/circdist/artifacts/circdist_gross_iter197_order144_continuation_round124_20260905/source/compress_verify_sat_trace_round124.py")
target = root / "source/compress_verify_sat_trace_round126.py"
report = root / "work/recovery/TRACE_COMPRESSOR_ADAPTATION.json"
expected = "92423fddaf6e94fe34040477b3ca149f04b1c8b0d319a0927a7c0f0483fd0b20"
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
text = raw.decode()
assert text.count("round124") == 1
text = text.replace("round124", "round126")
ast.parse(text, filename=str(target))
assert not target.exists()
target.write_text(text)
result = {
    "schema": "circdist-round126-trace-compressor-adaptation-v1",
    "status": "PASS",
    "source": str(source),
    "source_sha256": expected,
    "target": str(target),
    "target_sha256": hashlib.sha256(text.encode()).hexdigest(),
    "replacement": {"old": "round124", "new": "round126", "count": 1},
    "syntax": "PASS via ast.parse with no bytecode write",
}
report.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, sort_keys=True))
