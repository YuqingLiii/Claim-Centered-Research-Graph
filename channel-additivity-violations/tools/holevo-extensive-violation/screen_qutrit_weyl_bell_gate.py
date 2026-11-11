#!/usr/bin/env python3
"""Seeded numerical screen for the qutrit Weyl classical Bell gate.

This script is route-selection evidence only.  It does not certify the global
entropy inequality recorded in QUTRIT_WEYL_RANDOM_UNITARY_BELL_GATE_20260830.md.
"""

import argparse
import math
import random


Q = 3
LINES = ((1, 0), (0, 1), (1, 1), (1, 2))


def entropy(probabilities):
    return -sum(value * math.log2(value) for value in probabilities if value > 0.0)


def projection(probabilities, direction):
    u, v = direction
    result = [0.0] * Q
    for i in range(Q):
        for j in range(Q):
            result[(u * i + v * j) % Q] += probabilities[Q * i + j]
    return result


def autocorrelation(probabilities):
    result = [0.0] * (Q * Q)
    for a in range(Q):
        for b in range(Q):
            result[Q * a + b] = sum(
                probabilities[Q * i + j]
                * probabilities[Q * ((i - a) % Q) + ((j - b) % Q)]
                for i in range(Q)
                for j in range(Q)
            )
    return result


def gate_value(probabilities):
    side = min(entropy(projection(probabilities, line)) for line in LINES)
    return 2.0 * side - entropy(autocorrelation(probabilities))


def renyi2_collision_slack(probabilities):
    quotient_collisions = [
        sum(value * value for value in projection(probabilities, line))
        for line in LINES
    ]
    correlation = autocorrelation(probabilities)
    correlation_collision = sum(value * value for value in correlation)
    return max(quotient_collisions) ** 2 - correlation_collision


def selected_majorization_margin(probabilities):
    quotients = [projection(probabilities, line) for line in LINES]
    selected = max(quotients, key=max)
    correlation = sorted(autocorrelation(probabilities), reverse=True)
    product = sorted(
        (left * right for left in selected for right in selected),
        reverse=True,
    )
    correlation_partial = 0.0
    product_partial = 0.0
    margin = math.inf
    for index in range(Q * Q - 1):
        correlation_partial += correlation[index]
        product_partial += product[index]
        margin = min(margin, product_partial - correlation_partial)
    return margin


def dirichlet_sample(rng, alpha):
    values = [rng.gammavariate(alpha, 1.0) for _ in range(Q * Q)]
    total = sum(values)
    return [value / total for value in values]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=200_000)
    parser.add_argument("--seed", type=int, default=20260830)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    best_value = -math.inf
    best_probabilities = None
    smallest_renyi2_slack = math.inf
    smallest_majorization_margin = math.inf
    for _ in range(args.samples):
        alpha = 10.0 ** rng.uniform(-2.0, 2.0)
        probabilities = dirichlet_sample(rng, alpha)
        value = gate_value(probabilities)
        if value > best_value:
            best_value = value
            best_probabilities = probabilities
        smallest_renyi2_slack = min(
            smallest_renyi2_slack,
            renyi2_collision_slack(probabilities),
        )
        smallest_majorization_margin = min(
            smallest_majorization_margin,
            selected_majorization_margin(probabilities),
        )

    point_mass = [1.0] + [0.0] * (Q * Q - 1)
    uniform = [1.0 / (Q * Q)] * (Q * Q)
    assert abs(gate_value(point_mass)) < 1e-14
    assert abs(gate_value(uniform)) < 1e-14

    print(f"samples={args.samples}; seed={args.seed}")
    print(f"largest strictly sampled classical gate value={best_value:.12e}")
    print(f"smallest sampled Renyi-2 collision slack={smallest_renyi2_slack:.12e}")
    print(f"smallest sampled selected-line majorization margin={smallest_majorization_margin:.12e}")
    print("exact point-mass and uniform anchors have gate value 0")
    print("best sampled distribution=" + ",".join(f"{x:.12e}" for x in best_probabilities))
    print("NUMERICAL ONLY: no global inequality is certified")


if __name__ == "__main__":
    main()
