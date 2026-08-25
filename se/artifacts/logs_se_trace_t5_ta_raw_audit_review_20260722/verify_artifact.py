#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    data = json.loads((HERE / "independent_raw_audit.json").read_text(encoding="utf-8"))
    assert data["verdict"] == "CONFIRMED_REFUTATION"
    rows = data["tame_c2_exact_recomputations"]
    assert [row["n"] for row in rows] == [18, 19]
    assert all(row["T_a_verdict"] == "FAIL" and Q(row["T_a_ratio"]) > 1 for row in rows)
    assert all(row["T_b_verdict"] == "PASS_SINGLE_GATE" and Q(row["raw_T_b_rebuilt"]) < Q(row["T_b_cap"]) for row in rows)
    assert all(Q(row["raw_T_a_rebuilt_from_a_mass_times_r"]) ==
               Q(row["raw_T_a_rebuilt_from_d_squared_times_t_squared"]) for row in rows)
    assert all(abs(row["raw_over_normalized"] - 20) < 2e-12
               for row in data["non_tame_direct_raw_matrix_gate"]["branches"].values())
    manifest = HERE / "SHA256SUMS.txt"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            expected, name = line.split("  ", 1)
            assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == expected, name
    print("INDEPENDENT RAW AUDIT VERIFY PASS")


if __name__ == "__main__":
    main()
