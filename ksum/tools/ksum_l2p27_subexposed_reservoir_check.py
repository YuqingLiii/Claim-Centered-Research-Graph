"""Bounded checks for the Phase-27 formula-defined subexposed reservoir.

No support optimization or LP is performed.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


LAMBDAS = (Fraction(1, 50), Fraction(1, 5), Fraction(2, 5), Fraction(7, 10))


def lagrange_weights_at_zero(nodes: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    out = []
    for i, x in enumerate(nodes):
        w = Fraction(1)
        for k, y in enumerate(nodes):
            if k != i:
                w *= -y / (x - y)
        out.append(w)
    return tuple(out)


WEIGHTS = lagrange_weights_at_zero(LAMBDAS)


def log_falling(x: int, k: int) -> float:
    if k < 0 or k > x:
        return -math.inf
    return math.lgamma(x + 1) - math.lgamma(x - k + 1)


def fixed_index_defects(D: int) -> dict[str, float | int]:
    N = D * D
    n = N // 2
    h = round(0.75 * D)
    values: dict[str, float | int] = {"D": D, "h": h}
    for j in range(4):
        total = 0.0
        for lam, weight in zip(LAMBDAS, WEIGHTS):
            m = int(lam * D)
            factorial_ratio = 1.0 if j == 0 else math.exp(log_falling(m, j) - j * math.log(D))
            major_ratio = math.exp(log_falling(n - m, h) - log_falling(n, h))
            total += float(weight) * factorial_ratio * major_ratio
        if j == 0:
            total -= 1.0
        values[f"wkb_normalized_j{j}"] = total
        values[f"natural_scaled_j{j}"] = total / (D**j)
    return values


def positive_beta_gap(D: int) -> dict[str, float | int]:
    N = D * D
    alpha, beta = 0.50, 0.20
    h, b = round(alpha * D), round(beta * D)
    sigma, lam = 0.50, 0.70
    n, m = round(sigma * N), round(lam * D)
    log_reservoir = log_falling(m, b) + log_falling(n - m, h) - log_falling(N, h + b)
    v_star, q_star = beta / (alpha + beta), alpha / (alpha + beta)
    mv, mq = round(v_star * N), N - round(v_star * N)
    log_global = log_falling(mv, b) + log_falling(mq, h) - log_falling(N, h + b)
    gap = log_reservoir - log_global
    return {"D": D, "log_ratio_to_global_max": gap, "gap_over_D_log_D": gap / (D * math.log(D))}


def main() -> None:
    path = Path(__file__)
    weight_floats = [float(w) for w in WEIGHTS]
    reservoir_l1 = sum(abs(w) for w in weight_floats)
    payload = {
        "driver_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "lambdas": [float(x) for x in LAMBDAS],
        "weights_exact": [str(w) for w in WEIGHTS],
        "weights": weight_floats,
        "moment_checks_0_to_3": [
            sum(float(w) * float(x) ** j for w, x in zip(WEIGHTS, LAMBDAS)) for j in range(4)
        ],
        "reservoir_l1": reservoir_l1,
        "normalized_correlation": 2.0 / (1.0 + reservoir_l1),
        "normalized_high_tail_mass": reservoir_l1 / (1.0 + reservoir_l1),
        "fixed_index_defects": [fixed_index_defects(d) for d in (100, 200, 400, 800)],
        "positive_beta_subexposure": [positive_beta_gap(d) for d in (100, 200, 400, 800)],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
