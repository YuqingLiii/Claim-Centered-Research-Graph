#!/usr/bin/env python3
"""Exact rank-one CG identity and a support-only no-go certificate."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
import importlib.util
import itertools
import json
import math
from pathlib import Path

import h5py
import sympy as sp


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]
MAT = ROOT / "grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat"
SYSTEM = Path(str(MAT) + ".H4_level2_exact_system.json")
TENSOR_CHECKER = HERE.with_name("h4_ef_tensor_bound_checker.py")

spec = importlib.util.spec_from_file_location("tensor_checker", TENSOR_CHECKER)
assert spec is not None and spec.loader is not None
tb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tb)

N = tb.N
DISC = tb.DISC
K4 = tb.K4
Q4 = tb.Q4


def signed_cosets(generators: list[dict[str, list[int]]]):
    identity = tuple(range(N))
    representatives: list[tuple[tuple[int, ...], tuple[int, ...]] | None] = [None] * N
    representatives[0] = (identity, (1,) * N)
    queue = deque([0])
    while queue:
        point = queue.popleft()
        current_perm, current_sign = representatives[point]  # type: ignore[misc]
        for generator in generators:
            perm = generator["perm"]
            sign = generator["sign"]
            image_point = perm[point]
            if representatives[image_point] is None:
                new_perm = tuple(perm[current_perm[j]] for j in range(N))
                new_sign = tuple(
                    current_sign[j] * sign[current_perm[j]] for j in range(N)
                )
                representatives[image_point] = (new_perm, new_sign)
                queue.append(image_point)
    assert all(item is not None for item in representatives)
    return [item for item in representatives if item is not None]


def qsum(values):
    total: Q4 = (Fraction(0),) * 4
    for value in values:
        total = tb.qadd(total, value)
    return total


def kdot(left: list[K4], right: list[K4]) -> K4:
    total: K4 = (0, 0, 0, 0)
    for x, y in zip(left, right):
        total = tb.kadd(total, tb.kmul(x, y))
    return total


def qdot(matrix: list[list[Q4]], vector: list[Q4]) -> list[Q4]:
    return [qsum(tb.qmul(entry, value) for entry, value in zip(row, vector)) for row in matrix]


def qquadratic(matrix: list[list[Q4]], vector: list[Q4]) -> Q4:
    return qsum(tb.qmul(vector[i], value) for i, value in enumerate(qdot(matrix, vector)))


def qexpr(value: Q4) -> sp.Expr:
    bases = (1, sp.sqrt(5), sp.sqrt(DISC), sp.sqrt(5 * DISC))
    return sum(
        sp.Rational(coefficient.numerator, coefficient.denominator) * basis
        for coefficient, basis in zip(value, bases)
    )


def main() -> None:
    with h5py.File(MAT, "r") as archive:
        a_np = tb.exact.exact_int_matrix(archive["A"][()])
        archived_x = tb.exact.exact_signs(archive["ax"][()], "ax")
        archived_y = tb.exact.exact_signs(archive["by"][()], "by")
    x_gram, y_gram = tb.exact.reconstruct_exact_gram(a_np)
    a = [[int(entry) for entry in row] for row in a_np]

    t = sp.symbols("t")
    factors = [
        t + 138661354237888,
        t**2 - 10265488660412764 * t - 1421816489542807475215868726156,
        t**2 + 210061762674492 * t + 9969780653922489971805459684,
        t**2 + 375839439213876 * t - 1102647072483179451883551606876,
        t**2 + tb.A4 * t + tb.B4,
        t**3
        - 1705855162085280 * t**2
        - 246398705402929136951530868420 * t
        + 506733415307469348748117480555083324928345752,
    ]
    factor4 = sp.Poly(factors[4], t, domain=sp.QQ)
    other = sp.Poly(sp.prod(factors[:4] + factors[5:]), t, domain=sp.QQ)
    projector = other * sp.invert(other, factor4)
    denominator = math.lcm(*(int(sp.denom(projector.nth(k))) for k in range(12)))
    coefficients = [int(projector.nth(k) * denominator) for k in range(12)]

    current = [1] + [0] * (N - 1)
    q_column = [0] * N
    for coefficient in coefficients:
        q_column = [q_column[i] + coefficient * current[i] for i in range(N)]
        current = tb.integer_matvec(a, current)
    aq_column = tb.integer_matvec(a, q_column)

    system = json.loads(SYSTEM.read_text())
    generators = system["group"]["coxeter_generators"]
    representatives = signed_cosets(generators)

    f_denominator = 2 * denominator * DISC
    f_row0: list[K4] = []
    for j in range(N):
        residual = 2 * aq_column[j] + tb.A4 * q_column[j]
        f_row0.append((DISC * q_column[j], 0, -residual, 0))

    f_num: list[list[K4]] = [[(0, 0, 0, 0)] * N for _ in range(N)]
    for i, item in enumerate(representatives):
        perm, sign = item
        assert perm[0] == i
        for j in range(N):
            f_num[i][perm[j]] = tuple(
                sign[0] * sign[j] * value for value in f_row0[j]
            )  # type: ignore[assignment]
    assert all(f_num[i][j] == f_num[j][i] for i in range(N) for j in range(N))

    scale = 600 * f_denominator
    h_num: list[list[K4]] = [[(0, 0, 0, 0)] * N for _ in range(N)]
    # H=E o F, reconstructed directly from the exact projectors.
    for i in range(N):
        for j in range(N):
            e_entry = (int(x_gram[i, j]), int(y_gram[i, j]), 0, 0)
            h_num[i][j] = tb.kmul(e_entry, f_num[i][j])
    assert Fraction(h_num[0][0][0], scale) == Fraction(4, 5625)

    roots: list[Q4] = [
        (
            Fraction(1, 375),
            Fraction(0),
            -Fraction(435142604279029, 6956308921260472317898404291117000),
            -Fraction(220524777030959, 1159384820210078719649734048519500),
        ),
        (
            Fraction(7, 1875),
            Fraction(0),
            Fraction(435142604279029, 11593848202100787196497340485195000),
            Fraction(661574331092877, 5796924101050393598248670242597500),
        ),
        (
            Fraction(1, 225),
            Fraction(0),
            Fraction(435142604279029, 4173785352756283390739042574670200),
            Fraction(220524777030959, 695630892126047231789840429111700),
        ),
    ]
    assert all(sp.ask(sp.Q.positive(qexpr(root))) is True for root in roots)

    interpolation = [
        [(Fraction(1), Fraction(0), Fraction(0), Fraction(0)), root, tb.qmul(root, root)]
        for root in roots
    ]
    pdiff = tb.solve_three_by_three(
        interpolation,
        [
            (Fraction(0),) * 4,
            (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
            (Fraction(-1), Fraction(0), Fraction(0), Fraction(0)),
        ],
    )
    p3 = tb.solve_three_by_three(
        interpolation,
        [
            (Fraction(0),) * 4,
            (Fraction(0),) * 4,
            (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        ],
    )

    # Exact bases: four E columns and sixteen F columns.
    e_indices = [210, 204, 24, 147]
    f_indices = [1, 253, 286, 267, 203, 41, 276, 80, 102, 65, 117, 207, 30, 221, 233, 108]
    e_basis = [
        [(int(x_gram[i, j]), int(y_gram[i, j]), 0, 0) for i in range(N)]
        for j in e_indices
    ]
    f_basis = [[f_num[i][j] for i in range(N)] for j in f_indices]
    product_basis = [
        [tb.kmul(e_basis[ea][i], f_basis[fb][i]) for i in range(N)]
        for ea in range(4)
        for fb in range(16)
    ]

    # G1=<h,h'> and G2=<h,Hh'> in the nonorthogonal product basis.
    g1_num = [[kdot(product_basis[i], product_basis[j]) for j in range(64)] for i in range(64)]
    h_times_basis: list[list[K4]] = []
    for column in product_basis:
        h_times_basis.append(
            [
                kdot(h_num[row], column)
                for row in range(N)
            ]
        )
    g2_num = [
        [kdot(product_basis[i], h_times_basis[j]) for j in range(64)]
        for i in range(64)
    ]

    g1 = [[tb.qscale(entry, Fraction(1, scale * scale)) for entry in row] for row in g1_num]
    g2 = [[tb.qscale(entry, Fraction(1, scale**3)) for entry in row] for row in g2_num]
    ge = [
        [
            tb.qscale(
                (int(x_gram[i, j]), int(y_gram[i, j]), 0, 0),
                Fraction(1, 600),
            )
            for j in e_indices
        ]
        for i in e_indices
    ]
    gf = [
        [tb.qscale(f_num[i][j], Fraction(1, f_denominator)) for j in f_indices]
        for i in f_indices
    ]

    e_tests = [[i] for i in range(4)] + [list(pair) for pair in itertools.combinations(range(4), 2)]
    f_tests = [[i] for i in range(16)] + [list(pair) for pair in itertools.combinations(range(16), 2)]
    zero = (Fraction(0),) * 4
    one_quarter = (Fraction(1, 4), Fraction(0), Fraction(0), Fraction(0))
    checked = 0
    for es in e_tests:
        ex = [(Fraction(int(i in es)), Fraction(0), Fraction(0), Fraction(0)) for i in range(4)]
        enorm = qquadratic(ge, ex)
        for fs in f_tests:
            fx = [(Fraction(int(i in fs)), Fraction(0), Fraction(0), Fraction(0)) for i in range(16)]
            fnorm = qquadratic(gf, fx)
            z = [
                (Fraction(int(ea in es and fb in fs)), Fraction(0), Fraction(0), Fraction(0))
                for ea in range(4)
                for fb in range(16)
            ]
            l0 = tb.qmul(enorm, fnorm)
            l1 = qquadratic(g1, z)
            l2 = qquadratic(g2, z)
            value = tb.qadd(tb.qmul(pdiff[0], l0), tb.qmul(pdiff[1], l1))
            value = tb.qadd(value, tb.qmul(pdiff[2], l2))
            value = tb.qadd(value, tb.qneg(tb.qmul(one_quarter, l0)))
            assert tb.qzero(value)
            checked += 1
    assert checked == 1360

    c_star = tb.qscale(tb.qadd(tb.qscale(roots[0], 3), roots[1]), Fraction(1, 4))
    assert sp.ask(sp.Q.positive(qexpr(c_star) - sp.Rational(1, 720))) is True

    # A fixed 217+83 complementary ternary pair gives a support-only no-go:
    # its high-block weight fraction is below 1/6000.
    p_string = "----+0-++--+0++0-+++00++++++-+0-++0-+0---++00+++0++0+0+--0+0+-0-+0-++-+0--00-+0-+-00-+--0---++-+-+-+--+-+00+00-+-+0++0-+--+-0+-++-000+0++++-+-+0---0-00++000++-0++00+0-+++0-+-0+-+---+-+-0++00+00++-++-+0-0+--+00++0--+0-0+++-0-0+++0+0+0-++-++---0----00--------+-0++-00++--00-+00++----+00-0-0000++-+0--++"
    q_string = "00000+000000+00+0000--00000000-000+00-00000--000+00+0-000+0-00-00-00000-00++00-000-+0000-0000000000000000++0+-0000+00+000000+00000-+-0-00000000+000+0+-00---000-00-+0-0000+000-0000000000+00+-0--0000000-0-0000-+00+000-0+0000-0+000-0+0-000000000+0000++0000000000+000-+0000-+00-+0000000-+0+0--+-0000-0000"
    decode = {"+": 1, "-": -1, "0": 0}
    p = [decode[char] for char in p_string]
    q = [decode[char] for char in q_string]
    assert len(p) == len(q) == N
    assert sum(value != 0 for value in p) == 217
    assert sum(value != 0 for value in q) == 83
    assert all(p[i] * q[i] == 0 and p[i] * p[i] + q[i] * q[i] == 1 for i in range(N))

    def block3_data(p_vector: list[int], q_vector: list[int]) -> tuple[Q4, Q4]:
        ep_num = [
            (
                sum(int(x_gram[i, j]) * p_vector[j] for j in range(N)),
                sum(int(y_gram[i, j]) * p_vector[j] for j in range(N)),
                0,
                0,
            )
            for i in range(N)
        ]
        current = q_vector[:]
        qq = [0] * N
        for coefficient in coefficients:
            qq = [qq[i] + coefficient * current[i] for i in range(N)]
            current = tb.integer_matvec(a, current)
        aqq = tb.integer_matvec(a, qq)
        fq_num = [
            (DISC * qq[i], 0, -(2 * aqq[i] + tb.A4 * qq[i]), 0)
            for i in range(N)
        ]
        mixed = [tb.kmul(ep_num[i], fq_num[i]) for i in range(N)]
        l1 = tb.qscale(kdot(mixed, mixed), Fraction(1, scale * scale))
        hmixed = [kdot(h_num[row], mixed) for row in range(N)]
        l2 = tb.qscale(kdot(mixed, hmixed), Fraction(1, scale**3))
        alpha = tb.qscale(
            (
                sum(p_vector[i] * ep_num[i][0] for i in range(N)),
                sum(p_vector[i] * ep_num[i][1] for i in range(N)),
                0,
                0,
            ),
            Fraction(1, 600),
        )
        beta = tb.qscale(
            (
                DISC * sum(q_vector[i] * qq[i] for i in range(N)),
                0,
                -sum(
                    q_vector[i] * (2 * aqq[i] + tb.A4 * qq[i])
                    for i in range(N)
                ),
                0,
            ),
            Fraction(1, f_denominator),
        )
        l0 = tb.qmul(alpha, beta)
        w3 = tb.qadd(tb.qmul(p3[0], l0), tb.qmul(p3[1], l1))
        w3 = tb.qadd(w3, tb.qmul(p3[2], l2))
        return l0, w3

    l0, w3 = block3_data(p, q)
    assert sp.ask(sp.Q.positive(qexpr(l0) / 6000 - qexpr(w3))) is True
    ratio = sp.N(qexpr(w3) / qexpr(l0), 18)

    archived_p = [(x + y) // 2 for x, y in zip(archived_x, archived_y)]
    archived_q = [(x - y) // 2 for x, y in zip(archived_x, archived_y)]
    archived_l0, archived_w3 = block3_data(archived_p, archived_q)
    archived_ratio_q = tb.qdiv(archived_w3, archived_l0)
    archived_ratio_expr = qexpr(archived_ratio_q)
    assert sp.ask(sp.Q.positive(archived_ratio_expr - sp.Rational(1, 1500))) is True
    assert sp.ask(sp.Q.positive(sp.Rational(1, 1480) - archived_ratio_expr)) is True
    archived_ratio = sp.N(archived_ratio_expr, 18)

    # The rank-one constant alone supplies more than 99% of the earlier
    # ten-block numerical benchmark at the 217+83 split, but remains below it.
    rho_lower = sp.Rational(11_691_401_709_341_221, 2)
    sigma_upper = sp.Rational(56_846_466_952_431_285, 34)
    rational_penalty = (rho_lower - sigma_upper) * sp.Rational(83, 49)
    correction_lower = sp.Integer(7_114_830_222_845_879)
    assert correction_lower * sp.Rational(99, 100) < rational_penalty < correction_lower

    # Near-extremizer audit.  Flip the sign of p at coordinate 85; this
    # preserves the complementary 217+83 support split.  This is one of six
    # H4-equivalent closest nontrivial one-coordinate support-sign flips.
    near_p = archived_p[:]
    assert near_p[85] != 0
    near_p[85] *= -1
    near_l0, near_w3 = block3_data(near_p, archived_q)
    near_ratio_q = tb.qdiv(near_w3, near_l0)
    near_ratio_expr = qexpr(near_ratio_q)

    def bell_objective(p_vector: list[int], q_vector: list[int]) -> int:
        ap = tb.integer_matvec(a, p_vector)
        aq = tb.integer_matvec(a, q_vector)
        return sum(p_vector[i] * ap[i] - q_vector[i] * aq[i] for i in range(N))

    classical_value = 2_081_044_153_087_351_400
    assert bell_objective(archived_p, archived_q) == classical_value
    near_value = bell_objective(near_p, archived_q)
    near_gap = classical_value - near_value
    assert near_gap == 2_353_967_343_413_440
    assert 884 * near_gap < classical_value < 885 * near_gap

    # The same gap is the smallest positive Bell loss among all 300
    # one-coordinate sign flips within the fixed support cells.
    one_flip_gaps: list[tuple[int, str, int]] = []
    for label, vector, other in (
        ("p", archived_p, archived_q),
        ("q", archived_q, archived_p),
    ):
        for index, value in enumerate(vector):
            if value == 0:
                continue
            changed = vector[:]
            changed[index] *= -1
            objective = (
                bell_objective(changed, other)
                if label == "p"
                else bell_objective(other, changed)
            )
            one_flip_gaps.append((classical_value - objective, label, index))
    minimum_gap = min(gap for gap, _label, _index in one_flip_gaps if gap > 0)
    assert minimum_gap == near_gap
    assert sorted(
        index for gap, label, index in one_flip_gaps
        if gap == minimum_gap and label == "p"
    ) == [46, 56, 85, 99, 131, 148]

    # The complete two-coordinate shell is also strictly below C.  Use the
    # exact quadratic update formulas, avoiding 44,850 dense reevaluations.
    ap0 = tb.integer_matvec(a, archived_p)
    aq0 = tb.integer_matvec(a, archived_q)
    p_delta = {
        i: -4 * archived_p[i] * ap0[i] + 4 * a[i][i]
        for i in range(N) if archived_p[i]
    }
    q_delta = {
        i: 4 * archived_q[i] * aq0[i] - 4 * a[i][i]
        for i in range(N) if archived_q[i]
    }
    two_flip_gaps: list[tuple[int, str, int, int]] = []
    for i, j in itertools.combinations(p_delta, 2):
        objective_delta = (
            p_delta[i] + p_delta[j]
            + 8 * archived_p[i] * archived_p[j] * a[i][j]
        )
        two_flip_gaps.append((-objective_delta, "pp", i, j))
    for i, j in itertools.combinations(q_delta, 2):
        objective_delta = (
            q_delta[i] + q_delta[j]
            - 8 * archived_q[i] * archived_q[j] * a[i][j]
        )
        two_flip_gaps.append((-objective_delta, "qq", i, j))
    for i in p_delta:
        for j in q_delta:
            two_flip_gaps.append((-(p_delta[i] + q_delta[j]), "pq", i, j))
    assert len(two_flip_gaps) == math.comb(N, 2)
    assert all(gap > 0 for gap, _label, _i, _j in two_flip_gaps)
    minimum_two_gap = min(gap for gap, _label, _i, _j in two_flip_gaps)
    assert minimum_two_gap == 3_299_723_804_685_584
    assert sorted(
        (i, j) for gap, label, i, j in two_flip_gaps
        if gap == minimum_two_gap and label == "pp"
    ) == [(46, 148), (56, 131), (85, 99)]

    # Translate the ten-block target into the exact W_9 ratio required by
    # the block-weighted penalty.  The archived ratio clears the target, but
    # the closest one-flip shell does not.  This is an exact no-go for a
    # coarse "within 1/884 of C" stability ansatz.
    kappa = tb.qadd(tb.qadd(roots[1], roots[2]), tb.qscale(roots[0], -2))
    one = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    gap_q = sp.Rational(11_691_401_709_341_221, 2) - sp.Rational(
        56_846_466_952_431_285, 34
    )

    def penalty_from_ratio(ratio_q: Q4) -> sp.Expr:
        effective = tb.qadd(c_star, tb.qmul(kappa, ratio_q))
        theta = tb.qscale(effective, 15)
        fraction = tb.qdiv(theta, tb.qadd(one, theta))
        return gap_q * 83 * qexpr(fraction)

    archived_penalty = penalty_from_ratio(archived_ratio_q)
    near_penalty = penalty_from_ratio(near_ratio_q)
    assert sp.ask(sp.Q.positive(archived_penalty - correction_lower)) is True
    assert sp.ask(sp.Q.positive(correction_lower - near_penalty)) is True

    # Exact isolating intervals make the separation independently readable.
    required_lower = sp.Rational(628, 1_000_000)
    required_upper = sp.Rational(629, 1_000_000)
    assert sp.ask(sp.Q.positive(near_ratio_expr - sp.Rational(561, 1_000_000))) is True
    assert sp.ask(sp.Q.positive(sp.Rational(562, 1_000_000) - near_ratio_expr)) is True
    # Directly solve the monotone penalty equality for the critical effective
    # constant and hence for the critical W_9 ratio.
    target_fraction = correction_lower / (gap_q * 83)
    critical_effective = target_fraction / (15 * (1 - target_fraction))
    critical_ratio_expr = (critical_effective - qexpr(c_star)) / qexpr(kappa)
    assert sp.ask(sp.Q.positive(critical_ratio_expr - required_lower)) is True
    assert sp.ask(sp.Q.positive(required_upper - critical_ratio_expr)) is True
    assert sp.ask(sp.Q.positive(critical_ratio_expr - near_ratio_expr)) is True
    assert sp.ask(sp.Q.positive(archived_ratio_expr - critical_ratio_expr)) is True

    print("verified 1360 polarized coefficients of w_25-w_9=(1/4)||e||^2||f||^2")
    print("rank-one lower bound c_EF >= (3 gamma_1+gamma_2)/4 > 1/720")
    print("archived witness w_9/(alpha beta) =", archived_ratio)
    print("critical w_9/(alpha beta) for ten-block target =", sp.N(critical_ratio_expr, 18))
    print("closest one-flip Bell gap =", near_gap, "at indices [46,56,85,99,131,148]")
    print("complete two-flip shell is below C; minimum gap =", minimum_two_gap)
    print("closest one-flip w_9/(alpha beta) =", sp.N(near_ratio_expr, 18))
    print("archived block penalty clears target; closest one-flip block penalty does not")
    print("rank-one penalty benchmark is >99% but <100% of the ten-block target")
    print("217+83 support-only counterexample has w_9/(alpha beta) =", ratio)
    print("therefore no support-size-only claim w_9/(alpha beta) >= 1/6000 can hold")


if __name__ == "__main__":
    main()
