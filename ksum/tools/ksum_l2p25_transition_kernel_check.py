"""Bounded numerical checks for the Phase-25 mesoscopic transition formulas.

This checks gamma-ratio asymptotics only.  It performs no support or LP search.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


def log_falling(x: int, k: int) -> float:
    if k < 0 or k > x:
        return -math.inf
    return math.lgamma(x + 1) - math.lgamma(x - k + 1)


def entropy_phase(lam: float, beta: float) -> float:
    if lam <= beta:
        raise ValueError("interior transition formula requires lambda > beta")
    return lam * math.log(lam) - (lam - beta) * math.log(lam - beta) - beta


def transition_case(D: int) -> dict[str, float | int]:
    # N=D^2, so kappa=1 exactly.
    N = D * D
    sigma, lam, alpha, beta = 0.60, 0.80, 0.35, 0.20
    n, m, a, b = (round(N * sigma), round(D * lam), round(D * alpha), round(D * beta))
    q = (n - m) / N
    alpha_n, beta_n, lam_n = a / D, b / D, m / D

    exact = (
        b * math.log(N / D)
        + log_falling(m, b)
        + log_falling(n - m, a)
        - log_falling(N, a + b)
    )
    asym = (
        D * entropy_phase(lam_n, beta_n)
        + 0.5 * math.log(lam_n / (lam_n - beta_n))
        + a * math.log(q)
        + 0.5 * ((alpha_n + beta_n) ** 2 - alpha_n**2 / q)
    )
    return {"D": D, "log_error": abs(exact - asym), "D_times_error": D * abs(exact - asym)}


def bulk_overlap_case(D: int) -> dict[str, float | int]:
    N = D * D
    sigma, v, alpha, beta = 0.60, 0.10, 0.35, 0.20
    n, m, a, b = (round(N * sigma), round(N * v), round(D * alpha), round(D * beta))
    q = (n - m) / N
    alpha_n, beta_n = a / D, b / D
    exact = log_falling(m, b) + log_falling(n - m, a) - log_falling(N, a + b)
    asym = (
        b * math.log(v)
        + a * math.log(q)
        + 0.5
        * ((alpha_n + beta_n) ** 2 - beta_n**2 / v - alpha_n**2 / q)
    )
    return {"D": D, "log_error": abs(exact - asym), "D_times_error": D * abs(exact - asym)}


def birth_case(D: int, s: int = 2) -> dict[str, float | int]:
    N = D * D
    sigma, alpha, beta = 0.60, 0.35, 0.20
    n, a, b = round(N * sigma), round(D * alpha), round(D * beta)
    m = b + s
    q = (n - m) / N
    alpha_n, beta_n = a / D, b / D
    exact = (
        b * math.log(N / D)
        + log_falling(m, b)
        + log_falling(n - m, a)
        - log_falling(N, a + b)
    )
    asym = (
        D * (beta_n * math.log(beta_n) - beta_n)
        + (s + 0.5) * math.log(beta_n * D)
        + 0.5 * math.log(2 * math.pi)
        - math.lgamma(s + 1)
        + a * math.log(q)
        + 0.5 * ((alpha_n + beta_n) ** 2 - alpha_n**2 / q)
    )
    return {"D": D, "s": s, "log_error": abs(exact - asym), "D_times_error": D * abs(exact - asym)}


def fixed_j_overlap_case(D: int, j: int = 4) -> dict[str, float | int]:
    m = round(0.8 * D)
    exact = log_falling(m, j) - j * math.log(m)
    first_order = -j * (j - 1) / (2 * m)
    return {
        "D": D,
        "j": j,
        "log_error": abs(exact - first_order),
        "m_squared_times_error": m * m * abs(exact - first_order),
    }


def main() -> None:
    path = Path(__file__)
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "transition_interior": [transition_case(d) for d in (100, 200, 400, 800)],
        "bulk_overlap": [bulk_overlap_case(d) for d in (100, 200, 400, 800)],
        "activation_birth_s2": [birth_case(d) for d in (100, 200, 400, 800)],
        "fixed_j_overlap": [fixed_j_overlap_case(d) for d in (100, 200, 400, 800)],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
