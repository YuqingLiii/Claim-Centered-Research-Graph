#!/usr/bin/env python3
"""Hash-bound adaptations of reviewed Round124 packaging/replay utilities."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

PARENT = Path("<repo>/circdist/artifacts/circdist_gross_iter197_order144_continuation_round124_20260905/source")
OUT = Path("/private/tmp/circdist-round126-proposer-20260905/source")
HASHES = {
    "check_sat_trace_streams_round124.py": "1a0fbade687084c2dd09b459fdb6560f1514354a418193d62499c420f03596ec",
    "check_sealed_package_round124.py": "ecfe4351b9d63012b2a9986c0512e60f841af5b1455cb624a71644599fcd881a",
    "install_sealed_copy_round124.py": "bfaa8cb39a51bcc89c7ece13b4e3ec76ca70c7b62ab1469e64a1c7d9cb7e3b58",
    "seal_package_round124.py": "4a0bfc520e1d1316f85f1b1afef2f9e0d60c4f2636fa24ad3dd72c954b47fe5e",
    "replay_round124.py": "c5ddd9bd0ae8eb8ab4fc24d94eb86210592e507ade207553c53bb5df901e988f",
    "run_repository_gates_round124.py": "fd69cbc0603ee6013bad3bcd2336d35cefab16ccca6fc2a343624fa4fe58dfca",
    "check_evidence_closure_round124.py": "455354dbdb6286ca129be627dc41850ff6ea2afa80cf379322945c3742de03a1",
    "sync_stage_round124.py": "08297f12e1b5054641b7b44253eb2eb5671bcf6ed233620326b51d53832f7a58",
}
NAMES = {name: name.replace("round124", "round126") for name in HASHES}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


written = []
for old_name, expected in HASHES.items():
    raw = (PARENT / old_name).read_bytes()
    assert digest(raw) == expected, old_name
    text = raw.decode().replace("Round124", "Round126").replace("round124", "round126")
    if old_name == "check_sat_trace_streams_round124.py":
        text = text.replace("iteration-197", "iteration-198")
    elif old_name == "seal_package_round124.py":
        text = text.replace(
            "circdist_gross_iter197_order144_continuation_round126_20260905",
            "circdist_gross_iter198_order144_continuation_round126_20260905",
        ).replace("solve-iter197-", "solve-iter198-")
    elif old_name in {"check_sealed_package_round124.py", "install_sealed_copy_round124.py"}:
        text = text.replace(
            "circdist_gross_iter197_order144_continuation_round126_20260905",
            "circdist_gross_iter198_order144_continuation_round126_20260905",
        )
    elif old_name == "replay_round124.py":
        text = text.replace("iteration-197", "iteration-198").replace("iter197", "iter198")
        text = text.replace('F = R / "frontier/iter198"', 'F = R / "frontier/iter199"')
        text = text.replace('"--source-selector-count", "51552"', '"--source-selector-count", "51840"')
        text = text.replace(
            'S / "audit_css_duality_iter198_round122.py"',
            'S / "audit_css_duality_iter198_candidate_round126.py"',
        )
        text = text.replace('"css.iter198.json"', '"css.iter198_candidate.json"')
        text = text.replace('"regenerate_iter198_source"', '"regenerate_iter199_source"')
        text = text.replace('"iter198 source regeneration"', '"iter199 source regeneration"')
        text = text.replace('"iter198 state regeneration"', '"iter199 state regeneration"')
        text = text.replace('"iter198 advance audit"', '"iter199 advance audit"')
        text = text.replace('"round123_exact_review.md"', '"round125_exact_review.md"')
        text = text.replace('"round122_parent/SHA256SUMS.txt"', '"round124_parent/SHA256SUMS.txt"')
        text = text.replace('"iter198_translation"', '"iter199_translation"')
        text = text.replace('"iter198.translation.json"', '"iter199.translation.json"')
        text = text.replace('"--iteration", "198"', '"--iteration", "199"')
        text = text.replace('"--selectors", "51840"', '"--selectors", "52128"')
        text = text.replace('"--assertions", "870630"', '"--assertions", "870918"')
        text = text.replace('"iter198 translation closure"', '"iter199 translation closure"')
        text = text.replace('"verification/iter198_registry_invariance.json"', '"verification/iter199_registry_invariance.json"')
        text = text.replace('"iter198_css"', '"iter199_css"')
        text = text.replace('S / "audit_css_duality_iter198_round126.py"', 'S / "audit_css_duality_iter199_round126.py"')
        text = text.replace('"iter198.css.json"', '"iter199.css.json"')
        text = text.replace('"iter198 CSS closure"', '"iter199 CSS closure"')
        text = text.replace('"verification/css_duality_registry_audit_iter198.json"', '"verification/css_duality_registry_audit_iter199.json"')
        text = text.replace('"iter198_base_encoding"', '"iter199_base_encoding"')
        text = text.replace('"iter198.base_check.json"', '"iter199.base_check.json"')
        text = text.replace('"iter198 base encoding"', '"iter199 base encoding"')
        text = text.replace('"iter198_order144"', '"iter199_order144"')
        text = text.replace('S / "check_order144_quotient_iter198_round126.py"', 'S / "check_order144_quotient_iter199_round126.py"')
        text = text.replace('"iter198.order144.json"', '"iter199.order144.json"')
        text = text.replace('"iter198 order144 check"', '"iter199 order144 check"')
        text = text.replace('"iter198_unstarted"', '"iter199_unstarted"')
        text = text.replace('"iter198.unstarted.json"', '"iter199.unstarted.json"')
        text = text.replace('"fresh_iter198_remained_unstarted"', '"fresh_iter199_remained_unstarted"')
        text = text.replace(
            'R / "logs/session_and_process/process/session_process.jsonl"',
            '(R / "FINAL_PRESEAL_PROCESS_LEDGER.jsonl" if (R / "FINAL_PRESEAL_PROCESS_LEDGER.jsonl").is_file() else R / "logs/session_and_process/PROCESS_LEDGER.jsonl")',
        )
    new_name = NAMES[old_name]
    target = OUT / new_name
    target.write_text(text)
    ast.parse(text, filename=str(target))
    written.append({
        "parent": old_name,
        "parent_sha256": expected,
        "output": new_name,
        "output_sha256": digest(text.encode()),
    })

report = {
    "schema": "circdist-gross-round126-finalizer-adaptation-v1",
    "status": "PASS",
    "method": "hash-bound literal adaptation followed by Python AST parse; Round126-specific assertions are independently inspected and executed before seal",
    "files": written,
}
(Path("/private/tmp/circdist-round126-proposer-20260905/work/recovery/FINALIZER_ADAPTATION.json")).write_text(
    json.dumps(report, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({"status": "PASS", "files": len(written)}, sort_keys=True))
