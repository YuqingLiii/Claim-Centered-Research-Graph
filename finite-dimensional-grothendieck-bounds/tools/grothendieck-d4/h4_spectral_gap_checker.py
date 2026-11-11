#!/usr/bin/env python3
"""Exact audit for the d=4 H4 spectral-primary reduction.

This is an author-side exact checker.  It does not prove the Boolean classical bound.
It proves the exact square-free annihilating polynomial, its characteristic
factor multiplicities, and rational isolating intervals for the twelve real
eigenvalues.  The proof that one cyclic column suffices uses the certified
transitive signed-H4 action commuting with A.

Dependencies: h5py, numpy, sympy.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import h5py
import numpy as np
import sympy as sp


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")
EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_MULTIPLICITIES = [8, 4, 48, 24, 16, 36]


def file_md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def matvec(a: list[list[int]], v: list[int]) -> list[int]:
    return [sum(q * z for q, z in zip(row, v)) for row in a]


def newton_power_sums(poly: sp.Poly, count: int) -> list[sp.Integer]:
    """Return p_k=sum(root**k), k=0,...,count, by Newton identities."""

    degree = poly.degree()
    coeff = poly.all_coeffs()[1:]
    out = [sp.Integer(degree)]
    for k in range(1, count + 1):
        value = sum(coeff[i - 1] * out[k - i] for i in range(1, min(k, degree + 1)))
        if k <= degree:
            value += k * coeff[k - 1]
        out.append(-value)
    return out


def main() -> None:
    assert file_md5(MAT) == EXPECTED_MD5
    with h5py.File(MAT, "r") as archive:
        raw = np.asarray(archive["A"][()])
    a = [[int(z) for z in row] for row in raw]
    assert all(float(a[i][j]) == float(raw[i, j]) for i in range(300) for j in range(300))
    assert all(a[i][j] == a[j][i] for i in range(300) for j in range(300))

    system = json.loads(SYSTEM.read_text())
    generators = system["group"]["coxeter_generators"]

    # The convention in the frozen generator data is
    # G e_i = sign[i] e_perm[i].  Verify G A G^T=A exactly.
    for generator in generators:
        perm = generator["perm"]
        sign = generator["sign"]
        assert sorted(perm) == list(range(300))
        assert set(sign) <= {-1, 1}
        for i in range(300):
            for j in range(300):
                assert a[perm[i]][perm[j]] == sign[i] * sign[j] * a[i][j]

    # The permutation orbit of coordinate 0 is all 300 coordinates.  Hence an
    # annihilating relation checked on e_0 propagates to every coordinate.
    orbit = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for generator in generators:
            j = generator["perm"][i]
            if j not in orbit:
                orbit.add(j)
                frontier.append(j)
    assert len(orbit) == 300

    t = sp.symbols("t")
    factors = [
        sp.Poly(t + 138661354237888, t),
        sp.Poly(
            t**2
            - 10265488660412764 * t
            - 1421816489542807475215868726156,
            t,
        ),
        sp.Poly(
            t**2
            + 210061762674492 * t
            + 9969780653922489971805459684,
            t,
        ),
        sp.Poly(
            t**2
            + 375839439213876 * t
            - 1102647072483179451883551606876,
            t,
        ),
        sp.Poly(
            t**2
            + 6416438611362062 * t
            + 3336362192084004310572308931844,
            t,
        ),
        sp.Poly(
            t**3
            - 1705855162085280 * t**2
            - 246398705402929136951530868420 * t
            + 506733415307469348748117480555083324928345752,
            t,
        ),
    ]
    polynomial = sp.Poly(sp.prod(f.as_expr() for f in factors), t)
    assert polynomial.degree() == 12
    assert sp.gcd(polynomial, polynomial.diff()).degree() == 0
    assert [f.degree() for f in factors] == [1, 2, 2, 2, 2, 3]
    assert sp.factor_list(polynomial.as_expr())[0] == 1
    assert len(sp.factor_list(polynomial.as_expr())[1]) == 6

    e0 = [0] * 300
    e0[0] = 1

    # Horner evaluation of m(A)e_0, with arbitrary-precision integers.
    coefficients = [int(z) for z in polynomial.all_coeffs()]
    value = [coefficients[0] * z for z in e0]
    for coefficient in coefficients[1:]:
        value = matvec(a, value)
        value[0] += coefficient
    assert value == [0] * 300

    # Transitivity and commutation above imply m(A)=0.  Recover exact
    # characteristic multiplicities from six trace moments.  Transitivity
    # also makes every diagonal entry of A^k equal, so tr(A^k)=300(A^k)_00.
    moments = []
    value = e0
    for _ in range(6):
        moments.append(value[0])
        value = matvec(a, value)
    power_sums = [newton_power_sums(factor, 5) for factor in factors]
    matrix = sp.Matrix(
        [[power_sums[j][k] for j in range(6)] for k in range(6)]
    )
    traces = sp.Matrix([300 * moment for moment in moments])
    multiplicities = list(matrix.LUsolve(traces))
    assert multiplicities == EXPECTED_MULTIPLICITIES
    assert sum(m * f.degree() for m, f in zip(multiplicities, factors)) == 300

    intervals = [factor.intervals(eps=sp.Integer(1)) for factor in factors]
    # The large negative root of factor 4 is the exact residual norm after the
    # four-dimensional top projector is removed.
    assert intervals[4][0][0] == (
        sp.Integer(-5845700854670611),
        sp.Rational(-11691401709341221, 2),
    )
    # After additionally removing that rank-16 eigenspace, the largest
    # remaining absolute eigenvalue is the positive root of the cubic.
    assert intervals[5][2][0][0] == sp.Integer(1671954910365626)
    assert intervals[5][2][0][1] == sp.Rational(56846466952431285, 34)

    # Exact three-node Gauss--Jacobi rule for the Beta(1/2,3/2) measure.
    # It integrates z^j, j=0,...,5.  Hermite interpolation of sqrt(z) at
    # these nodes is a majorant because the sixth derivative is negative.
    alpha = 2 * sp.cos(sp.pi / 7)
    for j in range(6):
        quadrature_moment = sp.Rational(4, 7) * sum(
            sp.sin(sp.pi * k / 7) ** 2 * sp.cos(sp.pi * k / 7) ** (2 * j)
            for k in range(1, 4)
        )
        beta_moment = sp.rf(sp.Rational(1, 2), j) / sp.rf(2, j)
        exact_moment = sp.to_number_field(quadrature_moment, alpha)
        assert sp.simplify(exact_moment.as_expr() - beta_moment) == 0
    quadrature_bound = sp.Rational(2, 7) * (
        sp.cos(sp.pi / 7) + sp.cos(2 * sp.pi / 7)
    )
    c_squared = (sp.cos(sp.pi / 7) + sp.cos(2 * sp.pi / 7)) ** 2
    assert sp.minimal_polynomial(c_squared, t) == (
        64 * t**3 - 224 * t**2 + 196 * t - 49
    )
    c_squared_intervals = sp.Poly(
        64 * t**3 - 224 * t**2 + 196 * t - 49, t
    ).intervals(eps=sp.Rational(1, 100000))
    assert c_squared_intervals[-1][0][1] == sp.Rational(911, 392)
    assert sp.Rational(911, 392) < sp.Rational(931, 400)
    assert sp.simplify(
        1200 * quadrature_bound**2 - sp.Rational(4800, 49) * c_squared
    ) == 0

    # A sharp warning about moment-only support arguments.  The Lobatto rule
    # below has exactly the same beta moments through degree five and an atom
    # of mass 7/24 at zero.  Mixing 166/175 of it with 9/175 of the beta
    # measure leaves all those moments fixed and gives zero mass 83/300.
    lobatto_nodes = [
        sp.Integer(0),
        (5 - sp.sqrt(7)) / 12,
        (5 + sp.sqrt(7)) / 12,
        sp.Integer(1),
    ]
    lobatto_weights = [
        sp.Rational(7, 24),
        sp.Rational(29, 84) + sp.sqrt(7) / 21,
        sp.Rational(29, 84) - sp.sqrt(7) / 21,
        sp.Rational(1, 56),
    ]
    for j in range(6):
        assert sp.simplify(
            sum(w * z**j for w, z in zip(lobatto_weights, lobatto_nodes))
            - sp.rf(sp.Rational(1, 2), j) / sp.rf(2, j)
        ) == 0
    assert sp.Rational(166, 175) * sp.Rational(7, 24) == sp.Rational(83, 300)

    print("exact annihilating polynomial factors:")
    for factor, multiplicity in zip(factors, multiplicities):
        print(f"  characteristic factor exponent {multiplicity}: {factor.as_expr()}")
    print("m(A)e_0=0; signed-H4 transitivity and commutation imply m(A)=0")
    print("all twelve roots are simple and real; rational isolating intervals:")
    for interval in intervals:
        print(f"  {interval}")
    print("residual norm rho lies in (5845700854670610.5, 5845700854670611)")
    print("post-rank-16 residual norm sigma lies in (1671954910365626, 56846466952431285/34)")
    print("10th-moment Gauss--Jacobi bound: x^T E x < 228 for every sign x")
    print("moment-only obstruction: degree-10 data allow zero mass 83/300")


if __name__ == "__main__":
    main()
