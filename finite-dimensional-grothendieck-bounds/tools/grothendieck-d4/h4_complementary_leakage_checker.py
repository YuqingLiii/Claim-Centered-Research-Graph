#!/usr/bin/env python3
"""Exact checks for the complementary-support d=4 leakage note.

The checker proves two kinds of statements.

1.  It evaluates the dominant and opposite-sign primary spectral terms of
    the archived equality witness exactly.
2.  It proves that pointwise multiplication E x F -> R^300 has no zero
    divisors.  All possible zero-coordinate flats of a nonzero E-vector are
    reduced to H4 orbits of one-, two-, and three-element spanning sets.  If
    an A-eigenvector were supported on such a flat Z, then
    A[Z^c,Z] would have a nontrivial kernel.  Full column rank modulo the
    prime 1,000,003 certifies that this never occurs.

This is a draft-side checker and does not prove the classical upper bound.
Dependencies: h5py, numpy, sympy and the canonical exact-instance checker.
"""

from __future__ import annotations

from collections import deque
import itertools
import json
import math
from pathlib import Path
import sys

import h5py
import numpy as np
import sympy as sp


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")
TOOLS = ROOT / "grothendieck-d4/tools"
sys.path.insert(0, str(TOOLS))
import h4_exact_instance_checker as exact  # noqa: E402


N = 300
PRIME = 1_000_003
C = 2_081_044_153_087_351_400
A4 = 6_416_438_611_362_062
B4 = 3_336_362_192_084_004_310_572_308_931_844
DISC = 27_825_235_685_041_889_271_593_617_164_468


def q5_mul(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    a, b = left
    c, d = right
    return a * c + 5 * b * d, a * d + b * c


PERMUTATIONS: dict[int, list[tuple[tuple[int, ...], int]]] = {}
for dimension in (2, 3, 4):
    terms = []
    for permutation in itertools.permutations(range(dimension)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(dimension)
            for j in range(i + 1, dimension)
        )
        terms.append((permutation, -1 if inversions % 2 else 1))
    PERMUTATIONS[dimension] = terms


def gram_determinant(
    x: np.ndarray, y: np.ndarray, indices: tuple[int, ...]
) -> tuple[int, int]:
    """Determinant numerator in Q(sqrt(5)); the common 8^-d is omitted."""

    dimension = len(indices)
    real = radical = 0
    for permutation, sign in PERMUTATIONS[dimension]:
        term = (sign, 0)
        for i in range(dimension):
            term = q5_mul(
                term,
                (
                    int(x[indices[i], indices[permutation[i]]]),
                    int(y[indices[i], indices[permutation[i]]]),
                ),
            )
        real += term[0]
        radical += term[1]
    return real, radical


def orbit_representatives_pairs(generators: list[list[int]]) -> list[tuple[int, int]]:
    seen: set[tuple[int, int]] = set()
    representatives = []
    for i in range(N):
        for j in range(i + 1, N):
            seed = (i, j)
            if seed in seen:
                continue
            representatives.append(seed)
            orbit = {seed}
            queue = deque([seed])
            while queue:
                pair = queue.popleft()
                for generator in generators:
                    image = tuple(sorted((generator[pair[0]], generator[pair[1]])))
                    if image not in orbit:
                        orbit.add(image)
                        queue.append(image)
            seen.update(orbit)
    assert len(seen) == math.comb(N, 2)
    return representatives


def orbit_representatives_triples(
    generators: list[list[int]],
) -> list[tuple[int, int, int]]:
    choose2 = [i * (i - 1) // 2 for i in range(N + 1)]
    choose3 = [i * (i - 1) * (i - 2) // 6 for i in range(N + 1)]

    def index(triple: tuple[int, int, int]) -> int:
        a, b, c = triple
        return a + choose2[b] + choose3[c]

    seen = bytearray(math.comb(N, 3))
    representatives = []
    covered = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                seed = (a, b, c)
                if seen[index(seed)]:
                    continue
                representatives.append(seed)
                orbit = {seed}
                queue = deque([seed])
                while queue:
                    triple = queue.popleft()
                    for generator in generators:
                        image = tuple(sorted(generator[i] for i in triple))
                        if image not in orbit:
                            orbit.add(image)
                            queue.append(image)
                for triple in orbit:
                    location = index(triple)
                    assert not seen[location]
                    seen[location] = 1
                covered += len(orbit)
    assert covered == math.comb(N, 3)
    return representatives


def rank_mod_prime(matrix: np.ndarray) -> int:
    assert sp.isprime(PRIME)
    work = np.remainder(matrix, PRIME).astype(np.int64, copy=True)
    row = 0
    for column in range(work.shape[1]):
        candidates = np.flatnonzero(work[row:, column])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        work[[row, pivot]] = work[[pivot, row]]
        inverse = pow(int(work[row, column]), PRIME - 2, PRIME)
        work[row] = work[row] * inverse % PRIME
        factors = work[:, column].copy()
        factors[row] = 0
        work = (work - factors[:, None] * work[row]) % PRIME
        row += 1
        if row == work.shape[1]:
            break
    return row


def matvec(a: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(entry * value for entry, value in zip(row, vector)) for row in a]


def quadratic_moments(a: list[list[int]], vector: list[int], degree: int) -> list[int]:
    current = vector[:]
    moments = []
    for _ in range(degree + 1):
        moments.append(sum(x * y for x, y in zip(vector, current)))
        current = matvec(a, current)
    return moments


def sqrt_interval(integer: int, scale: int) -> tuple[sp.Rational, sp.Rational]:
    lower_numerator = math.isqrt(integer * scale * scale)
    lower = sp.Rational(lower_numerator, scale)
    upper = sp.Rational(lower_numerator + 1, scale)
    assert lower * lower <= integer < upper * upper
    return lower, upper


def interval_three_term(
    rational: sp.Rational,
    coefficient5: sp.Rational,
    coefficient_disc: sp.Rational,
    scale: int = 10**25,
) -> tuple[sp.Rational, sp.Rational]:
    bounds5 = sqrt_interval(5, scale)
    bounds_disc = sqrt_interval(DISC, scale)
    lower = rational
    upper = rational
    for coefficient, bounds in (
        (coefficient5, bounds5),
        (coefficient_disc, bounds_disc),
    ):
        if coefficient >= 0:
            lower += coefficient * bounds[0]
            upper += coefficient * bounds[1]
        else:
            lower += coefficient * bounds[1]
            upper += coefficient * bounds[0]
    return lower, upper


def main() -> None:
    with h5py.File(MAT, "r") as archive:
        a_raw = archive["A"][()]
        ax = exact.exact_signs(archive["ax"][()], "ax")
        by = exact.exact_signs(archive["by"][()], "by")
    a_np = exact.exact_int_matrix(a_raw)
    x_gram, y_gram = exact.reconstruct_exact_gram(a_np)
    a = [[int(entry) for entry in row] for row in a_np]

    p = [(x + y) // 2 for x, y in zip(ax, by)]
    q = [(x - y) // 2 for x, y in zip(ax, by)]
    assert all(value in (-1, 0, 1) for value in p + q)
    assert all(p[i] * q[i] == 0 and p[i] * p[i] + q[i] * q[i] == 1 for i in range(N))
    assert sum(value != 0 for value in p) == 217
    assert sum(value != 0 for value in q) == 83

    def gram_quadratic(matrix: np.ndarray, vector: list[int]) -> int:
        return sum(
            vector[i] * int(matrix[i, j]) * vector[j]
            for i in range(N)
            for j in range(N)
        )

    assert gram_quadratic(x_gram, p) == 52_152
    assert gram_quadratic(y_gram, p) == 23_184
    assert gram_quadratic(x_gram, q) == 216
    assert gram_quadratic(y_gram, q) == -24
    p_e_rational, p_e_sqrt5 = sp.Rational(2173, 25), sp.Rational(966, 25)
    q_e_rational, q_e_sqrt5 = sp.Rational(9, 25), sp.Rational(-1, 25)

    t = sp.symbols("t")
    factors = [
        t + 138661354237888,
        t**2 - 10265488660412764 * t - 1421816489542807475215868726156,
        t**2 + 210061762674492 * t + 9969780653922489971805459684,
        t**2 + 375839439213876 * t - 1102647072483179451883551606876,
        t**2 + A4 * t + B4,
        t**3
        - 1705855162085280 * t**2
        - 246398705402929136951530868420 * t
        + 506733415307469348748117480555083324928345752,
    ]
    factor4 = sp.Poly(factors[4], t, domain=sp.QQ)
    other = sp.Poly(sp.prod(factors[:4] + factors[5:]), t, domain=sp.QQ)
    primary_projector = other * sp.invert(other, factor4)
    assert sp.rem(primary_projector, factor4) == sp.Poly(1, t, domain=sp.QQ)
    for index, factor in enumerate(factors):
        if index != 4:
            assert sp.rem(primary_projector, sp.Poly(factor, t, domain=sp.QQ)).is_zero

    primary_data = {}
    for name, vector in (("p", p), ("q", q)):
        moments = quadratic_moments(a, vector, 12)
        q0 = sp.factor(sum(primary_projector.nth(k) * moments[k] for k in range(12)))
        q1 = sp.factor(sum(primary_projector.nth(k) * moments[k + 1] for k in range(12)))
        primary_data[name] = (q0, q1)
    assert primary_data["p"] == (
        sp.Rational(308, 25),
        sp.Rational(-1544279284652142236, 25),
    )
    assert primary_data["q"] == (
        sp.Rational(4636, 75),
        sp.Rational(-26246003593099047412, 75),
    )
    assert DISC == A4 * A4 - 4 * B4

    # If (q0,q1)=(z^TQz,z^TAQz) for the two-root f4 primary projector Q,
    # then rho*z^TFz = -q1/2 -(2*B4*q0+A4*q1)*sqrt(DISC)/(2*DISC).
    def rho_f_terms(q0: sp.Rational, q1: sp.Rational) -> tuple[sp.Rational, sp.Rational]:
        return -q1 / 2, -(2 * B4 * q0 + A4 * q1) / (2 * DISC)

    p_rho_f = rho_f_terms(*primary_data["p"])
    q_rho_f = rho_f_terms(*primary_data["q"])

    lambda_rational = sp.Integer(5_132_744_330_206_382)
    lambda_sqrt5 = sp.Integer(2_356_560_241_063_596)

    def lambda_times_e(
        e_rational: sp.Rational, e_sqrt5: sp.Rational
    ) -> tuple[sp.Rational, sp.Rational]:
        return (
            lambda_rational * e_rational + 5 * lambda_sqrt5 * e_sqrt5,
            lambda_rational * e_sqrt5 + lambda_sqrt5 * e_rational,
        )

    p_lambda_e = lambda_times_e(p_e_rational, p_e_sqrt5)
    q_lambda_e = lambda_times_e(q_e_rational, q_e_sqrt5)

    dominant_excess = (
        p_lambda_e[0] + q_rho_f[0] - C,
        p_lambda_e[1],
        q_rho_f[1],
    )
    opposite_primary = (
        q_lambda_e[0] + p_rho_f[0],
        q_lambda_e[1],
        p_rho_f[1],
    )
    remaining_shortfall = tuple(
        dominant_excess[i] - opposite_primary[i] for i in range(3)
    )
    dominant_interval = interval_three_term(*dominant_excess)
    opposite_interval = interval_three_term(*opposite_primary)
    shortfall_interval = interval_three_term(*remaining_shortfall)
    assert sp.Integer(70_591_592_261_534_099) < dominant_interval[0]
    assert dominant_interval[1] < sp.Integer(70_591_592_261_534_100)
    assert sp.Integer(63_476_762_038_688_220) < opposite_interval[0]
    assert opposite_interval[1] < sp.Integer(63_476_762_038_688_221)
    assert sp.Integer(7_114_830_222_845_879) < shortfall_interval[0]
    assert shortfall_interval[1] < sp.Integer(7_114_830_222_845_880)

    # Enumerate every orbit of possible spans of zero coordinates of an
    # E-vector.  Signed coordinate factors do not affect spans or ranks, so
    # only the permutation part of the H4 action is needed.
    system = json.loads(SYSTEM.read_text())
    generators = [item["perm"] for item in system["group"]["coxeter_generators"]]
    pair_representatives = orbit_representatives_pairs(generators)
    triple_representatives = orbit_representatives_triples(generators)
    assert len(pair_representatives) == 18
    assert len(triple_representatives) == 714

    flats: list[tuple[tuple[int, ...], tuple[int, ...]]] = []

    def closure(base: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(
            i
            for i in range(N)
            if gram_determinant(x_gram, y_gram, (*base, i)) == (0, 0)
        )

    flats.append(((0,), closure((0,))))
    for pair in pair_representatives:
        if gram_determinant(x_gram, y_gram, pair) != (0, 0):
            flats.append((pair, closure(pair)))
    dependent_triples = 0
    for triple in triple_representatives:
        if gram_determinant(x_gram, y_gram, triple) == (0, 0):
            dependent_triples += 1
            continue
        flats.append((triple, closure(triple)))
    assert dependent_triples == 7
    assert len(flats) == 726

    size_counts: dict[int, int] = {}
    for base, flat in flats:
        size_counts[len(flat)] = size_counts.get(len(flat), 0) + 1
        assert set(base) <= set(flat)
        complement = [i for i in range(N) if i not in set(flat)]
        cross_block = a_np[np.ix_(complement, flat)]
        assert rank_mod_prime(cross_block) == len(flat)
    assert size_counts == {
        1: 1,
        2: 11,
        3: 83,
        4: 88,
        5: 37,
        6: 76,
        7: 52,
        9: 94,
        10: 34,
        12: 54,
        27: 122,
        30: 74,
    }
    assert max(size_counts) == 30

    print("archived support split: 217 + 83")
    print("dominant excess lies strictly between 70591592261534099 and 70591592261534100")
    print("opposite primary correction lies strictly between 63476762038688220 and 63476762038688221")
    print("remaining ten-block correction must exceed 7114830222845879")
    print("H4 pair orbits: 18; H4 triple orbits: 714; dependent triple orbits: 7")
    print("all 726 spanning-flat representatives have full-column-rank A[Z^c,Z]")
    print("therefore E x F -> R^300, (e,f) |-> e o f, has no zero divisors")


if __name__ == "__main__":
    main()
