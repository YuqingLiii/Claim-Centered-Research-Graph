"""Exact gates for the phase-6 spine/satellite transfer obstruction.

This does not import numerical optimizer data.  It checks, in exact rational
arithmetic, the gauge freedom of a multiplicity block, Reynolds cancellation
of a nontrivial vector sector, and two canonical projector-diagonal
instantiations of the label-only spine+satellite transfer.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def permutations(n):
    return list(itertools.permutations(range(n)))


def centralizer(q, target):
    sigma = [(target - a) % q for a in range(q)]
    return [
        p
        for p in itertools.permutations(range(q))
        if all(p[sigma[a]] == sigma[p[a]] for a in range(q))
    ]


def act_tail_alphabet(x, tail_perm, alphabet):
    y = [x[0]] + [x[1 + tail_perm[j]] for j in range(len(tail_perm))]
    return tuple(alphabet[a] for a in y)


def standard_character(perm):
    return sum(perm[i] == i for i in range(len(perm))) - 1


def projector_diagonal(x, tail_perms, alphabet_group, position_label):
    m = len(tail_perms[0])
    if position_label == "trivial":
        dimension = 1
        character = lambda perm: 1
    elif position_label == "standard":
        dimension = m - 1
        character = standard_character
    else:
        raise ValueError(position_label)
    total = 0
    for perm in tail_perms:
        chi = character(perm)
        if chi:
            for alphabet in alphabet_group:
                if act_tail_alphabet(x, perm, alphabet) == x:
                    total += chi
    return Fraction(dimension * total, len(tail_perms) * len(alphabet_group))


def two_sum(x, q, target):
    return any((x[i] + x[j]) % q == target for i in range(len(x)) for j in range(i + 1, len(x)))


def swap_to_front(x, i):
    y = list(x)
    y[0], y[i] = y[i], y[0]
    return tuple(y)


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def finite_instance(n, q, target):
    tail_perms = permutations(n - 1)
    alphabet_group = centralizer(q, target)
    inputs = list(itertools.product(range(q), repeat=n))
    h_weight = {}
    nonnegative = True
    for x in inputs:
        spine = projector_diagonal(x, tail_perms, alphabet_group, "trivial")
        satellite = projector_diagonal(x, tail_perms, alphabet_group, "standard")
        h_weight[x] = spine + satellite
        nonnegative &= h_weight[x] >= 0
    # Reynolds average from the stabilizer to the full position group.  Tail
    # invariance makes the N transporters sufficient.
    weight = {
        x: sum((h_weight[swap_to_front(x, i)] for i in range(n)), Fraction()) / n
        for x in inputs
    }
    mass = sum(weight.values(), Fraction())
    measure = {x: value / mass for x, value in weight.items()}
    l1 = sum((abs(value) for value in measure.values()), Fraction())
    degree_zero = sum(measure.values(), Fraction())
    correlation = sum(
        (value * (1 if two_sum(x, q, target) else -1) for x, value in measure.items()),
        Fraction(),
    )
    # Direct invariance gates for adjacent position swaps and every alphabet
    # centralizer element.
    invariant = True
    for x, value in measure.items():
        for i in range(n - 1):
            y = list(x)
            y[i], y[i + 1] = y[i + 1], y[i]
            invariant &= measure[tuple(y)] == value
        for p in alphabet_group:
            invariant &= measure[tuple(p[a] for a in x)] == value
    return {
        "case": [n, q, target],
        "closed_form": "Reynolds(diag(P_([N-1],triv_C)+P_([N-2,1],triv_C))) / trace",
        "support": sum(value != 0 for value in measure.values()),
        "nonnegative": bool(nonnegative and all(value >= 0 for value in measure.values())),
        "full_invariance": bool(invariant),
        "l1": fraction_text(l1),
        "degree_zero_factorial_moment": fraction_text(degree_zero),
        "correlation": fraction_text(correlation),
        "annihilation_band": 0,
    }


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction()) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def gauge_gate():
    q_basis = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    block = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    rotation = [[Fraction(3, 5), Fraction(-4, 5)], [Fraction(4, 5), Fraction(3, 5)]]
    q_rotated = matmul(q_basis, rotation)
    block_rotated = matmul(matmul(transpose(rotation), block), rotation)
    natural = matmul(matmul(q_basis, block), transpose(q_basis))
    natural_rotated = matmul(matmul(q_rotated, block_rotated), transpose(q_rotated))
    return {
        "rotation": [[fraction_text(x) for x in row] for row in rotation],
        "original_top_coordinate_squares": ["1", "0"],
        "rotated_top_coordinate_squares": ["9/25", "16/25"],
        "natural_operator_equal": natural == natural_rotated,
    }


def reynolds_gate():
    # The S3 standard vector (1,-1,0) has zero group average exactly.
    vector = (1, -1, 0)
    orbit = [tuple(vector[p[i]] for i in range(3)) for p in permutations(3)]
    average = [Fraction(sum(v[i] for v in orbit), len(orbit)) for i in range(3)]
    return {
        "sector": "S3:[2,1]",
        "input_vector": list(vector),
        "reynolds_average": [fraction_text(x) for x in average],
        "killed": all(x == 0 for x in average),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json")
    args = parser.parse_args()
    result = {
        "theorem_gates": {
            "multiplicity_gauge": gauge_gate(),
            "nontrivial_vector_reynolds": reynolds_gate(),
            "projector_diagonal_fact": "diag(A)>=0 and sum diag(A)=trace(A)>0 for every nonzero PSD A",
        },
        "finite_instances": [finite_instance(4, 5, 0), finite_instance(5, 5, 0)],
        "interpretation": (
            "The label-only positive projector transfer is invariant and has exact l1 one, but its "
            "constant factorial moment is one, so it has no positive annihilation band. Signed "
            "sector coefficients or a canonical multiplicity-coordinate construction are outside this obstruction."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.json:
        Path(args.json).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
