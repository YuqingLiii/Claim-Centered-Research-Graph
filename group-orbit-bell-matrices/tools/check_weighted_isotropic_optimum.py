#!/usr/bin/env python3
"""Rational examples for GROTHORB.weighted-isotropic-optimum."""

from fractions import Fraction as F


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def exact_psd_pivots(matrix):
    """Congruence elimination: positive pivots, or an identically zero column."""
    work = [list(row) for row in matrix]
    size = len(work)
    assert all(work[i][j] == work[j][i] for i in range(size) for j in range(size))
    pivots = []
    for k in range(size):
        pivot = work[k][k]
        assert pivot >= 0
        pivots.append(pivot)
        if pivot == 0:
            assert all(work[i][k] == work[k][i] == 0 for i in range(k, size))
            continue
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                work[i][j] -= work[i][k] * work[k][j] / pivot
        for i in range(k + 1, size):
            work[i][k] = work[k][i] = F(0)
    return pivots


def check_case(label, a, u, b, v, expected):
    a = tuple(tuple(map(F, row)) for row in a)
    b = tuple(tuple(map(F, row)) for row in b)
    u, v = tuple(map(F, u)), tuple(map(F, v))
    r, m, n = len(a[0]), len(a), len(b)
    assert len(u) == m and len(v) == n
    assert all(len(row) == r and dot(row, row) == 1 for row in a + b)
    assert all(weight > 0 for weight in u + v)
    s_total, t_total = sum(u), sum(v)
    for frame, weights, total in ((a, u, s_total), (b, v, t_total)):
        for k in range(r):
            for ell in range(r):
                moment = sum(weight * row[k] * row[ell] for weight, row in zip(weights, frame))
                assert moment == (total / r if k == ell else 0)
    bell = [[u[i] * v[j] * dot(a[i], b[j]) for j in range(n)] for i in range(m)]
    value = sum(bell[i][j] * dot(a[i], b[j]) for i in range(m) for j in range(n))
    assert value == s_total * t_total / r == expected
    certificate = [[F(0) for _ in range(m + n)] for _ in range(m + n)]
    for i in range(m):
        certificate[i][i] = t_total * u[i] / r
    for j in range(n):
        certificate[m + j][m + j] = s_total * v[j] / r
        for i in range(m):
            certificate[i][m + j] = certificate[m + j][i] = -bell[i][j]
    pivots = exact_psd_pivots(certificate)
    assert sum(certificate[k][k] for k in range(m + n)) / 2 == expected
    print(f"{label}: r={r}, m={m}, n={n}, S={s_total}, T={t_total}; "
          f"unit frames, positive weights and isotropy exact; PASS")
    print(f"{label}: matching value=diagonal upper certificate={value}; PASS")
    print(f"{label}: exact PSD elimination pivots=" + ",".join(map(str, pivots)) + "; PASS")


def main():
    check_case("scalar", ((1,), (-1,)), (2, 1),
               ((-1,), (1,), (-1,)), (F(1, 2), F(3, 2), 4), F(18))
    check_case("rectangular", ((1, 0), (F(3, 5), F(4, 5)), (F(3, 5), -F(4, 5))),
               (F(7, 8), F(25, 16), F(25, 16)),
               ((1, 0), (0, 1), (F(3, 5), F(4, 5)), (-F(4, 5), F(3, 5))),
               (1, 1, 2, 2), F(12))
    print("Scope: two exact finite examples; the all-frame theorem is proved in WI-2--WI-3.")


if __name__ == "__main__":
    main()
