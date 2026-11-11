#!/usr/bin/env python3
"""Exact fixed-cell reduction and radius-three orbit-shell audit.

This checker proves that the archived q vector is a global quadratic
minimizer over every sign choice on its fixed 83-point support.  It also
enumerates, exactly, the Hamming shells of radius one, two and three around
the archived complementary pair and certifies that they lie strictly below
the Bell target.

Dependencies: h5py, numpy, sympy and the frozen project-local H4 builders.
"""

from __future__ import annotations

from collections import Counter
import itertools
import sys
from pathlib import Path

import h5py
import numpy as np
import sympy as sp


HERE = Path(__file__).resolve()
PROJECT = HERE.parents[1]
TOOLS = PROJECT / "tools"
BOOTSTRAP = TOOLS / "bootstrap"
sys.path[:0] = [str(TOOLS), str(BOOTSTRAP)]

from h4_exact_instance_checker import (  # noqa: E402
    EXPECTED_CLASSICAL,
    exact_int_matrix,
    exact_signs,
)
import h4_nogap_irrep_cache as h4rep  # noqa: E402


MAT = PROJECT / "artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")
N = 300


def transformed(vector: np.ndarray, permutation, signs) -> np.ndarray:
    """Apply G e_i=sign_i e_perm_i to a coordinate vector."""

    result = np.empty(N, dtype=np.int8)
    result[np.asarray(permutation, dtype=np.int64)] = (
        np.asarray(signs, dtype=np.int8) * vector
    )
    return result


def main() -> None:
    with h5py.File(MAT, "r") as archive:
        matrix = exact_int_matrix(archive["A"][()])
        x = np.asarray(exact_signs(archive["ax"][()], "ax"), dtype=np.int64)
        y = np.asarray(exact_signs(archive["by"][()], "by"), dtype=np.int64)
    matrix_object = matrix.astype(object)
    p = (x + y) // 2
    q = (x - y) // 2
    p_support = list(map(int, np.flatnonzero(p)))
    q_support = list(map(int, np.flatnonzero(q)))
    assert len(p_support) == 217 and len(q_support) == 83
    assert set(p_support).isdisjoint(q_support)
    assert int(p.astype(object) @ (matrix_object @ p.astype(object))) - int(
        q.astype(object) @ (matrix_object @ q.astype(object))
    ) == EXPECTED_CLASSICAL

    # Gauge the q-support quadratic so that the archived q becomes all ones.
    q_signs = q[q_support]
    q_principal = matrix[np.ix_(q_support, q_support)].astype(object)
    q_gauged = q_principal * np.outer(q_signs, q_signs)
    q_laplacian = np.diag(np.asarray(q_gauged.sum(axis=1), dtype=object)) - q_gauged
    assert np.array_equal(q_laplacian, q_laplacian.T)
    assert all(sum(int(value) for value in row) == 0 for row in q_laplacian)

    # -L_q has kernel 1.  A grounded principal minor is positive definite,
    # proved by an exact rational LDL^T factorization.
    grounded = sp.Matrix((-q_laplacian)[:-1, :-1].tolist())
    lower, diagonal = grounded.LDLdecomposition(hermitian=True)
    assert lower * diagonal * lower.T == grounded
    assert all(diagonal[i, i] > 0 for i in range(82))

    # In contrast, the p-support Laplacian is not PSD.  The following sparse
    # integer direction is an exact certificate, not a floating eigenvalue.
    p_signs = p[p_support]
    p_principal = matrix[np.ix_(p_support, p_support)].astype(object)
    p_gauged = p_principal * np.outer(p_signs, p_signs)
    p_laplacian = np.diag(np.asarray(p_gauged.sum(axis=1), dtype=object)) - p_gauged
    p_position = {coordinate: index for index, coordinate in enumerate(p_support)}
    negative_direction_data = {
        20: -2, 26: -2, 43: -2, 46: 2, 53: -2, 56: 2, 85: 2,
        88: 1, 96: 1, 99: 2, 102: 1, 104: -2, 110: 1, 120: -2,
        131: 2, 148: 2, 154: 1, 199: 1, 239: 1,
    }
    negative_direction = [0] * 217
    for coordinate, value in negative_direction_data.items():
        negative_direction[p_position[coordinate]] = value
    negative_quadratic = sum(
        negative_direction[i] * int(p_laplacian[i, j]) * negative_direction[j]
        for i in range(217) for j in range(217)
    )
    assert negative_quadratic == -1_160_483_848_923_607

    # Recover the order-six stabilizer of the archived complementary pair.
    _quotient, _quotient_data, group, _hdata, _audit = h4rep.structural_construction()
    _system, elements, _generators, _action_sha = h4rep.load_and_match_certified_action(
        SYSTEM, group
    )
    stabilizer = []
    p8 = p.astype(np.int8)
    q8 = q.astype(np.int8)
    for permutation, signs in elements:
        if np.array_equal(transformed(p8, permutation, signs), p8) and np.array_equal(
            transformed(q8, permutation, signs), q8
        ):
            stabilizer.append(tuple(map(int, permutation)))
    assert len(stabilizer) == 6

    def canonical(subset: tuple[int, ...]) -> tuple[int, ...]:
        return min(tuple(sorted(permutation[i] for i in subset)) for permutation in stabilizer)

    # Exact QUBO coefficients for the Bell deficit from support-sign flips.
    ap = matrix_object @ p.astype(object)
    aq = matrix_object @ q.astype(object)
    p_single = {
        i: int(4 * p[i] * ap[i] - 4 * matrix[i, i]) for i in p_support
    }
    q_single = {
        i: int(-4 * q[i] * aq[i] + 4 * matrix[i, i]) for i in q_support
    }

    def interaction(i: int, j: int) -> int:
        if p[i] != 0 and p[j] != 0:
            return int(-8 * p[i] * p[j] * matrix[i, j])
        if q[i] != 0 and q[j] != 0:
            return int(8 * q[i] * q[j] * matrix[i, j])
        return 0

    def deficit(subset: tuple[int, ...]) -> int:
        value = sum(p_single.get(i, q_single.get(i)) for i in subset)
        value += sum(interaction(i, j) for i, j in itertools.combinations(subset, 2))
        return int(value)

    # Radius one: exact stabilizer-orbit tangent census.
    one_orbits: dict[tuple[int, ...], int] = {}
    one_sizes: Counter[tuple[int, ...]] = Counter()
    for subset in itertools.combinations(range(N), 1):
        representative = canonical(subset)
        value = deficit(subset)
        if representative in one_orbits:
            assert one_orbits[representative] == value
        else:
            one_orbits[representative] = value
        one_sizes[representative] += 1
    assert len(one_orbits) == 67
    assert Counter(one_sizes.values()) == Counter({6: 37, 3: 24, 1: 6})
    minimum_one = min(one_orbits.values())
    assert minimum_one == 2_353_967_343_413_440
    assert {
        i for i in range(N) if deficit((i,)) == minimum_one
    } == {46, 56, 85, 99, 131, 148}

    # Radius two: 44,850 pairs collapse to 7,765 exact stabilizer orbits.
    two_orbits: dict[tuple[int, ...], int] = {}
    two_sizes: Counter[tuple[int, ...]] = Counter()
    minimum_two = None
    minimum_two_subsets = []
    for subset in itertools.combinations(range(N), 2):
        representative = canonical(subset)
        value = deficit(subset)
        assert value > 0
        if representative in two_orbits:
            assert two_orbits[representative] == value
        else:
            two_orbits[representative] = value
        two_sizes[representative] += 1
        if minimum_two is None or value < minimum_two:
            minimum_two = value
            minimum_two_subsets = [subset]
        elif value == minimum_two:
            minimum_two_subsets.append(subset)
    assert len(two_orbits) == 7_765
    assert Counter(two_sizes.values()) == Counter({6: 7_195, 3: 555, 1: 15})
    assert minimum_two == 3_299_723_804_685_584
    assert minimum_two_subsets == [(46, 148), (56, 131), (85, 99)]

    # Radius three: close the complete 4,455,100-point shell exactly.  Orbit
    # storage is unnecessary; invariance was already certified above.
    minimum_three = None
    minimum_three_subsets = []
    triple_count = 0
    for subset in itertools.combinations(range(N), 3):
        value = deficit(subset)
        assert value > 0
        triple_count += 1
        if minimum_three is None or value < minimum_three:
            minimum_three = value
            minimum_three_subsets = [subset]
        elif value == minimum_three:
            minimum_three_subsets.append(subset)
    assert triple_count == 4_455_100
    assert minimum_three == 4_073_853_755_325_552
    assert minimum_three_subsets == [
        (46, 99, 131),
        (56, 85, 148),
    ]

    print("exact grounded LDL proves -L_q PSD with kernel span{1}")
    print("therefore q is a global minimizer on all 2^83 fixed-support signs")
    print("p-Laplacian sparse integer negative direction =", negative_quadratic)
    print("archived-pair stabilizer order =", len(stabilizer))
    print("radius-1 orbit count/minimum deficit =", len(one_orbits), minimum_one)
    print("radius-2 orbit count/minimum deficit =", len(two_orbits), minimum_two)
    print("all", triple_count, "radius-3 points are below C; minimum deficit =", minimum_three)


if __name__ == "__main__":
    main()
