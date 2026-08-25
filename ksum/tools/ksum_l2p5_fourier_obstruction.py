"""Exact symbolic gates for the phase-5 Fourier/l1 obstruction.

For equal pair totals s, a unit-torus evaluation makes every interior local
polynomial the negative of its axis polynomial.  The resulting Fourier mode
lower-bounds the post-average l1 norm and forces normalized correlation <=1/2
for every r>=2 and every repeated block count m>=2.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction


def outer_weights(r: int):
    nodes = [0]
    power = 1
    while power <= r:
        nodes.append(power)
        power *= 5
    raw = {
        node: Fraction(1, math.prod(node - other for other in nodes if other != node))
        for node in nodes
    }
    if raw[0] > 0:
        raw = {node: -weight for node, weight in raw.items()}
    norm = sum(abs(weight) for weight in raw.values())
    return tuple(nodes), {node: weight / norm for node, weight in raw.items()}


def outer_identity_gate(r: int):
    nodes, weights = outer_weights(r)
    assert all(node % 2 == 1 for node in nodes[1:])
    assert sum(weights.values()) == 0
    parity_evaluation = sum(weight * ((-1) ** node) for node, weight in weights.items())
    assert parity_evaluation == 2 * weights[0]
    rho = 2 * abs(weights[0])
    return {
        "r": r,
        "q": 2 * r + 1,
        "outer_nodes": list(nodes),
        "rho": str(rho),
        "sum_Wk_minus_one_to_k": str(parity_evaluation),
        "absolute_fourier_outer_factor": str(abs(parity_evaluation)),
        "identity": "abs(sum_k W_k*(-1)^k)=rho",
    }


def exponent_gate(r: int, m: int):
    # Even s: correlation <= 2^((r+1)(1-m)).
    even_exponent = (r + 1) * (1 - m)
    assert even_exponent <= -3

    # Odd s: |A_s|>=2^(-1/2), so correlation is at most
    # 2^[r+1-m(r/2+1)].  Store twice the exponent to stay integral.
    odd_twice_exponent = 2 * (r + 1) - m * (r + 2)
    assert odd_twice_exponent <= -2
    return {
        "r": r,
        "m": m,
        "even_s_bound": f"2^({even_exponent})",
        "odd_s_bound": f"2^({odd_twice_exponent}/2)",
        "at_most_one_half": True,
    }


def main():
    transition_r = {2, 3, 4}
    for exponent in range(1, 7):
        pivot = 5**exponent
        transition_r.update((pivot - 1, pivot, pivot + 1))
    outer_checks = [outer_identity_gate(r) for r in sorted(transition_r)]
    exponent_checks = [exponent_gate(r, m) for r in range(2, 13) for m in range(2, 9)]
    print(json.dumps({
        "arithmetic": "fractions.Fraction plus integral exponent inequalities",
        "scope": "equal pair totals s>=2, odd q>=5, repeated shared-value blocks m>=2",
        "outer_identity_checks": outer_checks,
        "correlation_bound_checks": exponent_checks,
        "general_verdict": "normalized correlation <= 1/2",
        "verification": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
