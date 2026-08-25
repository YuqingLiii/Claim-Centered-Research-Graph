"""Bounded exact checks for the Phase-28 q=N two-reservoir construction.

No orbit-support optimization or LP is performed.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


def parity_moment(L: int, j: int) -> int:
    return sum((-1) ** z * math.comb(L, z) * z**j for z in range(L + 1))


def log_cosh(x: float) -> float:
    return x - math.log(2.0) + math.log1p(math.exp(-2.0 * x))


def log_cosh_difference(x: float, y: float) -> float:
    # x>y>=0; evaluate log(cosh(x)-cosh(y)) stably.
    lx, ly = log_cosh(x), log_cosh(y)
    return lx + math.log1p(-math.exp(ly - lx))


def case(N: int) -> dict[str, object]:
    D = math.floor(N ** (2.0 / 3.0))
    L = D + 1
    S = D
    filler = N - 2 * S - 2 * L
    occupied_pair_types = L + 2
    pair_budget = (N - 1) // 2
    bridge_ct = N // 4
    tail_min = S * S
    tail_max = S * S + L

    # W0=(3/4)B+(1/4)T, where corr(B)=1 and corr(T)=0.
    correlation = 0.75
    tail_mass = 0.25
    ct_moment_defect = 0.75 * bridge_ct / 2.0

    # Scalar TV lower bound for using a neutral tail supported in [H,2H]
    # to reproduce -(delta_M-delta_0)/2 through degree r.
    H = float(tail_min)
    eps = bridge_ct / H
    r = D // 2
    # Map [1,2] to [-1,1]: z(y)=2y-3.  At y=0 and eps, |z|=3 and 3-2eps.
    a0 = math.acosh(3.0)
    ae = math.acosh(3.0 - 2.0 * eps)
    log_tv_lower = log_cosh_difference(r * a0, r * ae) - math.log(2.0)

    return {
        "N": N,
        "D": D,
        "L": L,
        "S": S,
        "filler": filler,
        "occupied_pair_types": occupied_pair_types,
        "pair_budget": pair_budget,
        "legal": filler > 0 and occupied_pair_types <= pair_budget,
        "tail_ct_min": tail_min,
        "tail_ct_max": tail_max,
        "bridge_ct": bridge_ct,
        "raw_mixture_correlation": correlation,
        "raw_mixture_tail_mass": tail_mass,
        "ct_orbit_moment_defect": ct_moment_defect,
        "chebyshev_log_tv_lower_bound": log_tv_lower,
        "chebyshev_log10_tv_lower_bound": log_tv_lower / math.log(10.0),
        "parity_moments_0_to_6": [parity_moment(L, j) for j in range(7)],
    }


def main() -> None:
    path = Path(__file__)
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "cases": [case(n) for n in (1001, 8001, 64001)],
        "scope": "Exact parity identities, legality/scaling, raw mixture gates, and scalar Chebyshev TV bound only.",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
