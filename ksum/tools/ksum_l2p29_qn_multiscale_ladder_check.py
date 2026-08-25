"""Bounded scalar checks for the Phase-29 q=N multiscale ladder.

No support optimization or LP is performed.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


def log_cosh(x: float) -> float:
    return x - math.log(2.0) + math.log1p(math.exp(-2.0 * x))


def case(N: int) -> dict[str, float | int | bool]:
    D = math.floor(N ** (2.0 / 3.0))
    s_min = math.ceil(math.sqrt(N))
    s_max = D
    A = s_min * s_min
    B = s_max * s_max
    y0 = (B + A) / (B - A)
    alpha0 = math.acosh(y0)
    separator_degree = math.ceil(math.acosh(4.0) / alpha0)
    query_degree = 2 * separator_degree

    full_degree = (D - 1) // 2
    log_q0 = log_cosh(full_degree * alpha0)
    log_corr_upper = math.log(2.0) - log_q0

    return {
        "N": N,
        "D": D,
        "s_min": s_min,
        "s_max": s_max,
        "ct_min": A,
        "ct_max": B,
        "largest_core_filler": N - 2 * s_max,
        "legal": N - 2 * s_max > 0,
        "number_of_local_rungs": s_max - s_min,
        "chebyshev_alpha": alpha0,
        "one_quarter_separator_degree": separator_degree,
        "separator_query_degree": query_degree,
        "separator_query_degree_over_D": query_degree / D,
        "full_cutoff_log_correlation_upper": log_corr_upper,
        "full_cutoff_log10_correlation_upper": log_corr_upper / math.log(10.0),
    }


def main() -> None:
    path = Path(__file__)
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "cases": [case(n) for n in (1001, 8001, 64001, 512001)],
        "scope": "Formula ladder legality and scalar C_t Chebyshev bounds only; no support optimization or LP.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
