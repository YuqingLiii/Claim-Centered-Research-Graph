#!/usr/bin/env python3
"""Exact tensor-spectral lower bound for the d=4 E-F Hadamard map.

This author-side checker constructs the rational/algebraic projectors E and F from
the frozen integer matrix.  It proves a polynomial identity for

    H = E o F

whose nonzero eigenvalues are the squared singular values of the linear map
E tensor F -> R^300, e tensor f |-> e o f.  The smallest eigenvalue gives a
uniform lower bound for the rank-one constant c_EF.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
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
A4 = 6_416_438_611_362_062
B4 = 3_336_362_192_084_004_310_572_308_931_844
DISC = 27_825_235_685_041_889_271_593_617_164_468


# Elements a+b*sqrt(5)+c*sqrt(DISC)+d*sqrt(5*DISC).
K4 = tuple[int, int, int, int]
Q4 = tuple[Fraction, Fraction, Fraction, Fraction]


def kadd(x: K4, y: K4) -> K4:
    return tuple(x[i] + y[i] for i in range(4))  # type: ignore[return-value]


def kmul(x: K4, y: K4) -> K4:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e + 5 * b * f + DISC * c * g + 5 * DISC * d * h,
        a * f + b * e + DISC * (c * h + d * g),
        a * g + c * e + 5 * (b * h + d * f),
        a * h + d * e + b * g + c * f,
    )


def qadd(x: Q4, y: Q4) -> Q4:
    return tuple(x[i] + y[i] for i in range(4))  # type: ignore[return-value]


def qneg(x: Q4) -> Q4:
    return tuple(-value for value in x)  # type: ignore[return-value]


def qmul(x: Q4, y: Q4) -> Q4:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e + 5 * b * f + DISC * c * g + 5 * DISC * d * h,
        a * f + b * e + DISC * (c * h + d * g),
        a * g + c * e + 5 * (b * h + d * f),
        a * h + d * e + b * g + c * f,
    )


def qinv(x: Q4) -> Q4:
    """Inverse in Q(sqrt(5),sqrt(DISC)), using two quadratic conjugations."""

    a, b, c, d = x
    # x=A+B*v, A=a+b*u, B=c+d*u, u^2=5, v^2=DISC.
    c0 = a * a + 5 * b * b - DISC * (c * c + 5 * d * d)
    c1 = 2 * a * b - 2 * DISC * c * d
    norm = c0 * c0 - 5 * c1 * c1
    assert norm
    inv_c = (c0 / norm, -c1 / norm)
    # (A-B*v) * inv(C).
    return (
        a * inv_c[0] + 5 * b * inv_c[1],
        a * inv_c[1] + b * inv_c[0],
        -(c * inv_c[0] + 5 * d * inv_c[1]),
        -(c * inv_c[1] + d * inv_c[0]),
    )


def qdiv(x: Q4, y: Q4) -> Q4:
    return qmul(x, qinv(y))


def qscale(x: K4 | Q4, scalar: int | Fraction) -> Q4:
    return tuple(Fraction(value) * scalar for value in x)  # type: ignore[return-value]


def q_from_k(x: K4) -> Q4:
    return tuple(Fraction(value) for value in x)  # type: ignore[return-value]


def qzero(x: Q4) -> bool:
    return all(value == 0 for value in x)


def integer_matvec(a: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(entry * value for entry, value in zip(row, vector)) for row in a]


def field_matvec(matrix: list[list[K4]], vector: list[K4]) -> list[K4]:
    output: list[K4] = []
    for row in matrix:
        total = (0, 0, 0, 0)
        for entry, value in zip(row, vector):
            total = kadd(total, kmul(entry, value))
        output.append(total)
    return output


def coset_permutations(generators: list[list[int]]) -> list[tuple[int, ...]]:
    """Return g_i with g_i(0)=i for every point i."""

    identity = tuple(range(N))
    representatives: list[tuple[int, ...] | None] = [None] * N
    representatives[0] = identity
    queue = deque([0])
    while queue:
        point = queue.popleft()
        current = representatives[point]
        assert current is not None
        for generator in generators:
            image_point = generator[point]
            if representatives[image_point] is None:
                representatives[image_point] = tuple(
                    generator[current[j]] for j in range(N)
                )
                queue.append(image_point)
    assert all(item is not None for item in representatives)
    return [item for item in representatives if item is not None]


def solve_three_by_three(matrix: list[list[Q4]], right: list[Q4]) -> list[Q4]:
    work = [[*row, right[i]] for i, row in enumerate(matrix)]
    for column in range(3):
        pivot = next(i for i in range(column, 3) if not qzero(work[i][column]))
        work[column], work[pivot] = work[pivot], work[column]
        inverse = qinv(work[column][column])
        work[column] = [qmul(entry, inverse) for entry in work[column]]
        for row in range(3):
            if row == column:
                continue
            factor = work[row][column]
            if qzero(factor):
                continue
            work[row] = [
                qadd(work[row][j], qneg(qmul(factor, work[column][j])))
                for j in range(4)
            ]
    return [work[i][3] for i in range(3)]


def main() -> None:
    with h5py.File(MAT, "r") as archive:
        a_np = exact.exact_int_matrix(archive["A"][()])
    x_gram, y_gram = exact.reconstruct_exact_gram(a_np)
    a = [[int(entry) for entry in row] for row in a_np]

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
    projector = other * sp.invert(other, factor4)
    denominator = math.lcm(
        *(int(sp.denom(projector.nth(k))) for k in range(12))
    )
    coefficients = [int(projector.nth(k) * denominator) for k in range(12)]

    # Exact first columns of Q and AQ, where Q is the two-root f4 projector.
    current = [1] + [0] * (N - 1)
    q_column = [0] * N
    for coefficient in coefficients:
        q_column = [
            q_column[i] + coefficient * current[i] for i in range(N)
        ]
        current = integer_matvec(a, current)
    aq_column = integer_matvec(a, q_column)

    # H=E o F has common denominator SCALE and integer K4 numerator.
    # E=(X+Y sqrt(5))/600 and
    # F=Q/2-(AQ+A4 Q/2)sqrt(DISC)/DISC.
    scale = 1200 * denominator * DISC
    row0: list[K4] = []
    for j in range(N):
        x = int(x_gram[0, j])
        y = int(y_gram[0, j])
        q = q_column[j]
        residual = 2 * aq_column[j] + A4 * q
        row0.append(
            (DISC * q * x, DISC * q * y, -residual * x, -residual * y)
        )

    system = json.loads(SYSTEM.read_text())
    generators = [item["perm"] for item in system["group"]["coxeter_generators"]]
    representatives = coset_permutations(generators)
    inverses = []
    for permutation in representatives:
        inverse = [0] * N
        for source, target in enumerate(permutation):
            inverse[target] = source
        inverses.append(inverse)
    matrix = [[row0[inverses[i][j]] for j in range(N)] for i in range(N)]
    assert all(matrix[i][j] == matrix[j][i] for i in range(N) for j in range(N))

    # Sanity check the exact diagonal H_ii=(1/75)(4/75)=4/5625.
    diagonal = row0[0]
    assert diagonal[1:] == (0, 0, 0)
    assert Fraction(diagonal[0], scale) == Fraction(4, 5625)

    # Exact trace moments of the scaled matrix K=SCALE*H.
    vectors: list[list[K4]] = [[(1, 0, 0, 0)] + [(0, 0, 0, 0)] * (N - 1)]
    moments: list[K4] = []
    for _ in range(6):
        vectors.append(field_matvec(matrix, vectors[-1]))
        moments.append(tuple(N * value for value in vectors[-1][0]))  # type: ignore[arg-type]

    # If the three nonzero eigenvalues of K are r1,r2,r3, their elementary
    # symmetric functions solve the trace recurrence
    # T_(k+3)=e1*T_(k+2)-e2*T_(k+1)+e3*T_k.
    qmom = [q_from_k(value) for value in moments]
    recurrence_matrix = [
        [qmom[k + 1], qneg(qmom[k]), qmom[k - 1]] for k in range(1, 4)
    ]
    recurrence_right = [qmom[k + 2] for k in range(1, 4)]
    e1, e2, e3 = solve_three_by_three(recurrence_matrix, recurrence_right)
    h1 = qscale(e1, Fraction(1, scale))
    h2 = qscale(e2, Fraction(1, scale * scale))
    h3 = qscale(e3, Fraction(1, scale * scale * scale))

    # Verify K(K^3-e1 K^2+e2 K-e3 I)e0=0 exactly.  Permutation
    # transitivity then propagates this relation to every coordinate vector.
    relation: list[Q4] = []
    for coordinate in range(N):
        value = q_from_k(vectors[4][coordinate])
        value = qadd(value, qneg(qmul(e1, q_from_k(vectors[3][coordinate]))))
        value = qadd(value, qmul(e2, q_from_k(vectors[2][coordinate])))
        value = qadd(value, qneg(qmul(e3, q_from_k(vectors[1][coordinate]))))
        relation.append(value)
    assert all(qzero(value) for value in relation)

    u = sp.sqrt(5)
    v = sp.sqrt(DISC)

    def expression(value: Q4) -> sp.Expr:
        return sum(
            sp.Rational(item.numerator, item.denominator) * basis
            for item, basis in zip(value, (1, u, v, u * v))
        )

    polynomial = sp.Poly(
        t**3 - expression(h1) * t**2 + expression(h2) * t - expression(h3),
        t,
        extension=[u, v],
    )
    factorization = sp.factor_list(polynomial, extension=[u, v])
    assert len(factorization[1]) == 3
    assert all(poly.degree() == 1 and exponent == 1 for poly, exponent in factorization[1])
    roots = sorted(
        [-poly.nth(0) / poly.nth(1) for poly, _ in factorization[1]],
        key=lambda root: float(sp.N(root, 30)),
    )

    # Exact algebraic comparisons give a simple publishable lower bound.
    lower = sp.Rational(1, 11000)
    assert all(sp.ask(sp.Q.positive(root - lower)) is True for root in roots)
    assert sp.ask(sp.Q.positive(sp.Rational(1, 10700) - roots[0])) is True

    multiplicities = [30, 25, 9]
    normalized_moments = [
        expression(qscale(moments[k], Fraction(1, scale ** (k + 1))))
        for k in range(3)
    ]
    for power in range(1, 4):
        assert sp.simplify(
            sum(multiplicities[i] * roots[i] ** power for i in range(3))
            - normalized_moments[power - 1]
        ) == 0
    assert sum(multiplicities) == 64

    # Quantitative consequence at the archived support split.  The improved
    # complementary-support inequality implies that either
    # u=s-alpha > 3s/2203 or v=t-beta > 3t/2203.  With sigma bounded above
    # as in the spectral-gap checker, this forces at least the following
    # primary spectral penalty.  It is still less than one fifteenth of the
    # exact ten-block correction target.
    lambda_lower = sp.Rational(5_132_744_330_206_382) + sp.Rational(
        2_356_560_241_063_596 * 559, 250
    )
    rho_lower = sp.Rational(11_691_401_709_341_221, 2)
    sigma_upper = sp.Rational(56_846_466_952_431_285, 34)
    p_penalty = (lambda_lower - sigma_upper) * sp.Rational(3 * 217, 2203)
    q_penalty = (rho_lower - sigma_upper) * sp.Rational(3 * 83, 2203)
    guaranteed_penalty = min(p_penalty, q_penalty)
    correction_target = sp.Integer(7_114_830_222_845_879)
    assert guaranteed_penalty == sp.Rational(
        17_667_466_582_242_999_264, 37_451
    )
    assert (correction_target + 1) / 16 < guaranteed_penalty < correction_target / 15

    print("rank(E tensor F Hadamard map) = 64")
    print("nonzero squared singular-value multiplicities: 30, 25, 9")
    for index, root in enumerate(roots):
        print(f"gamma_{index + 1} =", root)
        print(f"gamma_{index + 1} decimal =", sp.N(root, 18))
    print("exact lower bound: c_EF >= gamma_1 > 1/11000")
    print("and gamma_1 < 1/10700")
    print("archived 217+83 forced primary penalty >", math.floor(guaranteed_penalty))
    print("this certified penalty is between 1/16 and 1/15 of the ten-block target")


if __name__ == "__main__":
    main()
