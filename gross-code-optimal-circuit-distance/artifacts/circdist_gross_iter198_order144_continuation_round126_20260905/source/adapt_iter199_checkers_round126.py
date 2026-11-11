#!/usr/bin/env python3
"""Create Round126/iteration-199 checkers from exact reviewed Round124 sources."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path("/private/tmp/circdist-round126-proposer-20260905")
PARENT = Path("<repo>/circdist/artifacts/circdist_gross_iter197_order144_continuation_round124_20260905")
REPORT = ROOT / "work/recovery/ITER199_CHECKER_ADAPTATIONS.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


specs = [
    {
        "source": "source/audit_css_duality_iter198_round124.py",
        "expected": "4361ab5481bb461da3c59be3259f17e15049652ec1cfb02717b7fba41be74b5a",
        "target": "source/audit_css_duality_iter199_round126.py",
        "replacements": [
            ("iteration-198", "iteration-199", 2),
            ("51840", "52128", 1),
            ("round124", "round126", 1),
            ("iter198", "iter199", 1),
        ],
    },
    {
        "source": "source/check_order144_quotient_iter198_round124.py",
        "expected": "e7f4e81fa3520bee94ab8adc8357eb6b1d6373e349136c6e6ad3be76c45a226f",
        "target": "source/check_order144_quotient_iter199_round126.py",
        "replacements": [
            ("Round124", "Round126", 1),
            ("iteration-198", "iteration-199", 3),
            ("round124", "round126", 1),
            ("iter198", "iter199", 1),
        ],
    },
    {
        "source": "source/check_frontier_unstarted_round124.py",
        "expected": "6d402becfe306905984eb2aa06e4aa2d5a08dacf6f942ab542db95c8671a3b92",
        "target": "source/check_frontier_unstarted_round126.py",
        "replacements": [("round124", "round126", 1)],
    },
]

rows = []
for spec in specs:
    source = PARENT / spec["source"]
    target = ROOT / spec["target"]
    raw = source.read_bytes()
    assert digest(raw) == spec["expected"], source
    text = raw.decode("utf-8")
    applied = []
    for old, new, expected_count in spec["replacements"]:
        count = text.count(old)
        assert count == expected_count, (source, old, count, expected_count)
        text = text.replace(old, new)
        applied.append({"old": old, "new": new, "count": count})
    ast.parse(text, filename=str(target))
    if target.exists():
        assert target.read_text() == text
    else:
        target.write_text(text)
    rows.append(
        {
            "source": str(source),
            "source_sha256": spec["expected"],
            "target": str(target),
            "target_sha256": digest(text.encode()),
            "replacements": applied,
            "syntax": "PASS via ast.parse with no bytecode write",
        }
    )

REPORT.write_text(
    json.dumps(
        {
            "schema": "circdist-round126-iter199-checker-adaptations-v1",
            "status": "PASS",
            "files": rows,
        },
        indent=2,
        sort_keys=True,
    )
    + "\n"
)
print(REPORT.read_text(), end="")
