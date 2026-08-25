"""Independent reconstruction check for corrected KSUM.B4b.L2 LP output."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


THRESHOLD = Q(2, 3)


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def centralizer(q, target):
    sigma = [(target - a) % q for a in range(q)]
    return [
        perm
        for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    ]


def move(counts, perm):
    result = [0] * len(counts)
    for old, new in enumerate(perm):
        result[new] = counts[old]
    return tuple(result)


def classes(n, q, target, mode):
    group = centralizer(q, target)
    buckets = {}
    for counts in compositions(n, q):
        key = (
            min(move(counts, perm) for perm in group)
            if mode == "joint"
            else tuple(sorted(counts, reverse=True))
        )
        buckets.setdefault(key, []).append(counts)
    return [buckets[key] for key in sorted(buckets)]


def sign(counts, q, target):
    for a in range(q):
        b = (target - a) % q
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def falling(value, order):
    return math.prod(value - offset for offset in range(order))


def average(values):
    values = list(values)
    return Q(sum(values), len(values))


def data(orbit_classes, q, target, degree):
    correlation = [average(sign(z, q, target) for z in cls) for cls in orbit_classes]
    raw = []
    for total in range(degree):
        for alpha in compositions(total, q):
            raw.append(
                tuple(
                    average(
                        math.prod(falling(z[a], alpha[a]) for a in range(q))
                        for z in cls
                    )
                    for cls in orbit_classes
                )
            )
    return correlation, list(dict.fromkeys(raw)), len(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    checks = []
    certified = {}
    for point in payload["results"]:
        n, q, target = point["case"]
        for mode, mode_data in point["modes"].items():
            max_degree = 0
            for record in mode_data["bands"]:
                degree = record["degree"]
                orbit_classes = classes(n, q, target, mode)
                correlation, rows, raw_count = data(orbit_classes, q, target, degree)
                weights = [Q(0)] * len(orbit_classes)
                for entry in record["nonzero_weights"]:
                    weights[entry["class_index"]] = Q(entry["weight"])
                exact_corr = sum(a * b for a, b in zip(correlation, weights))
                l1 = sum(abs(weight) for weight in weights)
                residuals = [sum(a * b for a, b in zip(row, weights)) for row in rows]
                optimum = Q(record["optimum_exact"])
                assert len(orbit_classes) == record["class_count"]
                assert raw_count == record["raw_moment_rows"]
                assert len(rows) == record["unique_moment_rows"]
                assert l1 == 1 and exact_corr == optimum and not any(residuals)
                assert record["certifies_direct_q13"] == (optimum > THRESHOLD)
                if optimum > THRESHOLD:
                    max_degree = degree

                matrix = np.array([[float(x) for x in row] for row in rows])
                vector = np.array([float(x) for x in correlation])
                width = len(orbit_classes)
                solution = linprog(
                    np.r_[-vector, vector],
                    A_ub=np.ones((1, 2 * width)),
                    b_ub=[1],
                    A_eq=np.hstack([matrix, -matrix]),
                    b_eq=np.zeros(len(rows)),
                    bounds=(0, None),
                    method="highs",
                )
                assert solution.success and abs(-solution.fun - float(optimum)) < 2e-9
                checks.append(
                    {
                        "case": [n, q, target],
                        "mode": mode,
                        "degree": degree,
                        "exact_correlation": str(exact_corr),
                        "exact_l1": str(l1),
                        "max_exact_moment_residual": "0",
                        "independent_highs_abs_error": abs(-solution.fun - float(optimum)),
                    }
                )
            assert max_degree == mode_data["max_certified_degree_direct_q13"]
            certified[(n, q, target, mode)] = max_degree

        gain = certified[(n, q, target, "joint")] - certified[(n, q, target, "single")]
        assert gain == point["corrected_degree_gain_joint_minus_single"]
        assert point["corrected_degree_gain_survives"] == (gain > 0)

    all_vanish = all(not point["corrected_degree_gain_survives"] for point in payload["results"])
    assert payload["all_corrected_degree_gains_vanish"] == all_vanish
    assert payload["kill_criterion_triggered"] == all_vanish
    assert payload["decision"] == ("KILL" if all_vanish else "SURVIVE")
    print(
        json.dumps(
            {
                "implementation": "independent orbit/moment reconstruction plus HiGHS optimum check",
                "threshold": "strictly greater than 2/3",
                "checks": checks,
                "decision_verified": payload["decision"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
