#!/usr/bin/env python3
"""Exact small-rank checks for the explicit Clifford generator convention.

All entries are Gaussian integers represented by Python complex numbers with
integer real and imaginary parts.  The tested identities therefore use exact
equality; no tolerance or floating-point approximation is involved.
"""

from __future__ import annotations


Matrix = tuple[tuple[complex, ...], ...]


I2: Matrix = ((1, 0), (0, 1))
X: Matrix = ((0, 1), (1, 0))
Y: Matrix = ((0, -1j), (1j, 0))
Z: Matrix = ((1, 0), (0, -1))


def eye(n: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def zero(n: int) -> Matrix:
    return tuple(tuple(0 for _ in range(n)) for _ in range(n))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * x for x in row) for row in a)


def mul(a: Matrix, b: Matrix) -> Matrix:
    bt = tuple(zip(*b))
    return tuple(tuple(sum(x * y for x, y in zip(row, col)) for col in bt) for row in a)


def dagger(a: Matrix) -> Matrix:
    return tuple(tuple(x.conjugate() for x in col) for col in zip(*a))


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(col) for col in zip(*a))


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def kron(a: Matrix, b: Matrix) -> Matrix:
    rows = []
    for ar in a:
        for br in b:
            rows.append(tuple(x * y for x in ar for y in br))
    return tuple(rows)


def tensor_string(factors: list[Matrix]) -> Matrix:
    out: Matrix = ((1,),)
    for factor in factors:
        out = kron(out, factor)
    return out


def generators(s: int) -> list[Matrix]:
    if s < 1:
        raise ValueError("s must be positive")
    q = s // 2
    out: list[Matrix] = []
    for j in range(q):
        prefix = [Z] * j
        suffix = [I2] * (q - j - 1)
        out.append(tensor_string(prefix + [X] + suffix))
        out.append(tensor_string(prefix + [Y] + suffix))
    if s % 2:
        out.append(tensor_string([Z] * q))
    return out


def linear_combination(coeffs: list[int], mats: list[Matrix]) -> Matrix:
    out = zero(len(mats[0]))
    for coeff, mat in zip(coeffs, mats):
        out = add(out, scale(coeff, mat))
    return out


def check_rank(s: int) -> tuple[int, int]:
    gs = generators(s)
    d = len(gs[0])
    ident = eye(d)
    nil = zero(d)
    assert len(gs) == s
    for a, ga in enumerate(gs):
        assert dagger(ga) == ga
        assert dagger(transpose(ga)) == transpose(ga)
        assert mul(ga, ga) == ident
        for b, gb in enumerate(gs):
            anti = add(mul(ga, gb), mul(gb, ga))
            assert anti == (scale(2, ident) if a == b else nil)
            assert trace(mul(ga, gb)) == (d if a == b else 0)

    coeffs = list(range(1, s + 1))
    gv = linear_combination(coeffs, gs)
    norm_sq = sum(c * c for c in coeffs)
    assert mul(gv, gv) == scale(norm_sq, ident)
    return d, norm_sq


def main() -> None:
    for s in range(1, 10):
        d, norm_sq = check_rank(s)
        print(f"s={s} D={d} all_exact_identities=PASS test_norm_sq={norm_sq}")


if __name__ == "__main__":
    main()

