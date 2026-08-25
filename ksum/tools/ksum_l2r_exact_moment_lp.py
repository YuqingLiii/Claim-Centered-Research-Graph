"""Corrected-threshold exact LPs for KSUM.B4b.L2.

The LP is unchanged from phase 1: it maximizes correlation of a unit-l1
signed orbit measure subject to exact falling-factorial moments below degree d.
Only the direct quantum interpretation is corrected.  With F in {-1,+1}, a
T-query error-1/3 algorithm gives a degree-2T expected-sign polynomial with
uniform error 2/3, so direct Q_(1/3) >= d/2 requires correlation strictly
greater than 2/3.

All LP arithmetic is rational through SymPy's exact simplex solver.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.solvers.simplex import lpmax


DIRECT_Q13_THRESHOLD = sp.Rational(2, 3)
POINTS = ((3, 3, 0), (4, 3, 0), (5, 4, 1))


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def centralizer_of_sigma(q: int, target: int):
    sigma = tuple((target - a) % q for a in range(q))
    return [
        perm
        for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    ]


def act_counts(counts, perm):
    moved = [0] * len(counts)
    for old, new in enumerate(perm):
        moved[new] = counts[old]
    return tuple(moved)


def orbit_key(counts, centralizer, mode: str):
    if mode == "joint":
        return min(act_counts(counts, perm) for perm in centralizer)
    if mode == "single":
        return tuple(sorted(counts, reverse=True))
    raise ValueError(f"unknown mode: {mode}")


def build_classes(n: int, q: int, target: int, mode: str):
    centralizer = centralizer_of_sigma(q, target)
    grouped = {}
    for counts in compositions(n, q):
        grouped.setdefault(orbit_key(counts, centralizer, mode), []).append(counts)
    return [grouped[key] for key in sorted(grouped)], centralizer


def two_sum_sign(counts, q: int, target: int) -> int:
    sigma = tuple((target - a) % q for a in range(q))
    for a, b in enumerate(sigma):
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def falling(value: int, order: int) -> int:
    return math.prod(value - offset for offset in range(order))


def average(values) -> Fraction:
    values = list(values)
    return Fraction(sum(values), len(values))


def class_data(classes, q: int, target: int, degree: int):
    correlation = [
        average(two_sum_sign(counts, q, target) for counts in cls)
        for cls in classes
    ]
    rows = []
    raw_count = 0
    for total in range(degree):
        for alpha in compositions(total, q):
            raw_count += 1
            rows.append(
                tuple(
                    average(
                        math.prod(falling(counts[a], alpha[a]) for a in range(q))
                        for counts in cls
                    )
                    for cls in classes
                )
            )
    return correlation, list(dict.fromkeys(rows)), raw_count


def rational(value: Fraction):
    return sp.Rational(value.numerator, value.denominator)


def solve_band(n: int, q: int, target: int, mode: str, degree: int):
    classes, centralizer = build_classes(n, q, target, mode)
    correlation, rows, raw_rows = class_data(classes, q, target, degree)
    class_count = len(classes)
    pos = sp.symbols(f"p0:{class_count}")
    neg = sp.symbols(f"m0:{class_count}")
    signed = [pos[j] - neg[j] for j in range(class_count)]
    objective = sum(rational(correlation[j]) * signed[j] for j in range(class_count))
    constraints = [
        sp.Eq(
            sum(rational(row[j]) * signed[j] for j in range(class_count)),
            0,
        )
        for row in rows
    ]
    constraints.append(sum(pos) + sum(neg) <= 1)
    constraints.extend(variable >= 0 for variable in (*pos, *neg))
    optimum, solution = lpmax(objective, constraints)

    weights = [
        sp.simplify(solution.get(pos[j], 0) - solution.get(neg[j], 0))
        for j in range(class_count)
    ]
    l1 = sp.simplify(sum(abs(weight) for weight in weights))
    exact_correlation = sp.simplify(
        sum(rational(correlation[j]) * weights[j] for j in range(class_count))
    )
    residuals = [
        sp.simplify(
            sum(rational(row[j]) * weights[j] for j in range(class_count))
        )
        for row in rows
    ]
    if exact_correlation != optimum or any(residuals):
        raise ArithmeticError("exact witness verification failed")

    return {
        "degree": degree,
        "mode": mode,
        "class_count": class_count,
        "centralizer_order": len(centralizer),
        "raw_moment_rows": raw_rows,
        "unique_moment_rows": len(rows),
        "moment_rank": int(
            sp.Matrix([[rational(entry) for entry in row] for row in rows]).rank()
        ),
        "optimum_exact": str(optimum),
        "optimum_float": float(optimum),
        "witness_l1_exact": str(l1),
        "certifies_direct_q13": bool(optimum > DIRECT_Q13_THRESHOLD),
        "nonzero_weights": [
            {"class_index": j, "weight": str(weight)}
            for j, weight in enumerate(weights)
            if weight != 0
        ],
    }


def solve_point(n: int, q: int, target: int):
    modes = {}
    for mode in ("single", "joint"):
        bands = [solve_band(n, q, target, mode, degree) for degree in range(1, n + 1)]
        modes[mode] = {
            "bands": bands,
            "max_certified_degree_direct_q13": max(
                (row["degree"] for row in bands if row["certifies_direct_q13"]),
                default=0,
            ),
        }
    single_degree = modes["single"]["max_certified_degree_direct_q13"]
    joint_degree = modes["joint"]["max_certified_degree_direct_q13"]
    return {
        "case": [n, q, target],
        "modes": modes,
        "corrected_degree_gain_joint_minus_single": joint_degree - single_degree,
        "corrected_degree_gain_survives": joint_degree > single_degree,
        "joint_dominates_every_objective_band": all(
            modes["joint"]["bands"][d - 1]["optimum_exact"]
            == modes["single"]["bands"][d - 1]["optimum_exact"]
            or sp.Rational(modes["joint"]["bands"][d - 1]["optimum_exact"])
            > sp.Rational(modes["single"]["bands"][d - 1]["optimum_exact"])
            for d in range(1, n + 1)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = [solve_point(*point) for point in POINTS]
    all_vanish = all(
        not result["corrected_degree_gain_survives"] for result in results
    )
    payload = {
        "arithmetic": "exact rational (SymPy simplex)",
        "function_encoding": "-1 on NO, +1 on YES",
        "direct_quantum_error": "1/3",
        "expected_sign_uniform_error": "2/3",
        "correlation_threshold": "strictly greater than 2/3",
        "degree_to_query_conversion": "Q_(1/3) >= d/2",
        "moment_basis": "falling-factorial occupancy monomials of total degree < d",
        "single_symmetry": "S_N x S_q",
        "joint_symmetry": "S_N x C(sigma)",
        "results": results,
        "all_corrected_degree_gains_vanish": all_vanish,
        "kill_criterion_triggered": all_vanish,
        "decision": "KILL" if all_vanish else "SURVIVE",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
