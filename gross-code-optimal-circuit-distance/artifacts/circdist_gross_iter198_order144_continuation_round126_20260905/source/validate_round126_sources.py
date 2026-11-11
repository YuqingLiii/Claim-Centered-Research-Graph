#!/usr/bin/env python3
"""AST-parse and scope-check all Round126-authored executable Python sources."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

S = Path("/private/tmp/circdist-round126-proposer-20260905/source")
files = sorted(p for p in S.glob("*round126*.py") if p.is_file())
assert files
rows = []
for path in files:
    raw = path.read_bytes()
    ast.parse(raw.decode(), filename=str(path))
    rows.append({"path": "source/" + path.name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})

replay = (S / "replay_round126.py").read_text()
required = [
    'I = R / "input/iter198"', 'E = R / "output/iter198"', 'F = R / "frontier/iter199"',
    '"--source-selector-count", "51840"', '"--iteration", "199"',
    '"--selectors", "52128"', '"--assertions", "870918"',
    'bindings/round125_exact_review.md', 'bindings/round124_parent/SHA256SUMS.txt',
    'bindings/round126_proofpilot_rank.json', 'check_sat_trace_streams_round126.py',
]
assert all(x in replay for x in required)
forbidden = [
    'input/iter197', 'output/iter197', 'frontier/iter198"',
    'bindings/round123_exact_review.md', 'bindings/round122_parent/SHA256SUMS.txt',
    'solve-iter197-', 'audit_css_duality_iter197',
]
assert not [x for x in forbidden if x in replay]
seal = (S / "seal_package_round126.py").read_text()
assert 'circdist_gross_iter198_order144_continuation_round126_20260905' in seal
assert seal.count('solve-iter198-') == 3 and 'solve-iter197-' not in seal

out = {
    "schema": "circdist-gross-round126-source-validation-v1", "status": "PASS",
    "ast_parsed_files": len(rows), "files": rows,
    "replay_exact_input_iteration": 198, "replay_fresh_iteration": 199,
    "replay_solver_invocations": 0, "sealer_expected_solver_starts": 3,
    "stale_scope_tokens_rejected": True,
}
target = Path("/private/tmp/circdist-round126-proposer-20260905/work/recovery/ROUND126_SOURCE_VALIDATION.json")
target.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "ast_parsed_files": len(rows)}, sort_keys=True))
