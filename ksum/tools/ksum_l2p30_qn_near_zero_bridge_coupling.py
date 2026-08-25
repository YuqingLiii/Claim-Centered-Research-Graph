"""Bounded coupling arithmetic for the Phase-30 exact projection bridge.

Reads the archived Phase-22 full-orbit projection results.  No new support
optimization or LP is performed.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


EPSILON = 0.01


def main() -> None:
    path = Path(__file__)
    source = Path("ksum/artifacts/logs_ksum_L2p22_critical_dense_20260721/run.json")
    data = json.loads(source.read_text(encoding="utf-8"))
    rows = []
    threshold = (2.0 / 3.0) / (1.0 - EPSILON)
    for item in data["results"]:
        bridge_corr = item["normalized_correlation"]
        rows.append(
            {
                "N": item["N"],
                "L": item["L"],
                "D": item["D"],
                "bridge_correlation": bridge_corr,
                "coupled_correlation": (1.0 - EPSILON) * bridge_corr,
                "coupled_tail_lower_bound": EPSILON,
                "bridge_threshold_for_coupled_two_thirds": threshold,
                "coupled_correlation_pass": (1.0 - EPSILON) * bridge_corr > 2.0 / 3.0,
            }
        )
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "source_log": str(source).replace("\\", "/"),
        "source_driver_sha256": data["script_sha256"],
        "epsilon": EPSILON,
        "results": rows,
        "scope": "Arithmetic coupling of archived full-orbit bridge correlations with an independently annihilating parity tail; no new projection solve.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
