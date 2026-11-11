#!/usr/bin/env python3
"""Exact rational outer-product replay for GROTHORB.minimum-settings-isotropic."""

from fractions import Fraction as F


def rank(matrix):
    work = [list(row) for row in matrix]
    row_count, col_count = len(work), len(work[0])
    pivot_row = 0
    for col in range(col_count):
        found = next((i for i in range(pivot_row, row_count) if work[i][col]), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row][col]
        for j in range(col, col_count):
            work[pivot_row][j] /= pivot
        for i in range(pivot_row + 1, row_count):
            factor = work[i][col]
            if factor:
                for j in range(col, col_count):
                    work[i][j] -= factor * work[pivot_row][j]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def outer(vector, denominator):
    return tuple(tuple(F(x * y, denominator) for y in vector) for x in vector)


def measurement_row(projector):
    r = len(projector)
    return tuple(projector[i][i] for i in range(r)) + tuple(
        2 * projector[i][j] for i in range(r) for j in range(i + 1, r)
    )


def check_frame(projectors, weights, r):
    assert len(projectors) == len(weights)
    assert all(w > 0 for w in weights)
    for p in projectors:
        assert sum(p[i][i] for i in range(r)) == 1
        assert all(p[i][j] == p[j][i] for i in range(r) for j in range(r))
        # A symmetric idempotent with trace one is a unit rank-one projector.
        assert all(sum(p[i][k] * p[k][j] for k in range(r)) == p[i][j]
                   for i in range(r) for j in range(r))
    total = sum(weights, F(0))
    assert all(sum(w * p[i][j] for w, p in zip(weights, projectors))
               == (total / r if i == j else 0)
               for i in range(r) for j in range(r))
    return total


def check_dimension(r):
    alice = []
    for i in range(r):
        vector = [0] * r
        vector[i] = 1
        alice.append(outer(vector, 1))
    bob = []
    for i in range(r):
        for j in range(i + 1, r):
            vector = [0] * r
            vector[i], vector[j] = 1, -1
            bob.append(outer(vector, 2))
    bob.append(outer([1] * r, r))
    u = [F(1)] * r
    v = [F(2, r)] * (len(bob) - 1) + [F(1)]
    s_total = check_frame(alice, u, r)
    t_total = check_frame(bob, v, r)
    assert s_total == t_total == r
    alice_rows = [measurement_row(p) for p in alice]
    bob_rows = [measurement_row(p) for p in bob]
    d = r * (r + 1) // 2
    assert len(alice) == r
    assert len(bob) == r * (r - 1) // 2 + 1
    assert len(alice_rows) + len(bob_rows) == d + 1
    # Exact coefficient vector of the nonzero weighted trace relation.
    relation = tuple(w / s_total for w in u) + tuple(-w / t_total for w in v)
    rows = alice_rows + bob_rows
    assert any(relation)
    assert all(sum(c * row[k] for c, row in zip(relation, rows)) == 0
               for k in range(d))
    actual_rank = rank(rows)
    assert actual_rank == d
    print(f"r={r}: m={len(alice)}, n={len(bob)}, total={d + 1}, "
          f"rank(Sym_r map)={actual_rank}, S=T={s_total}; "
          "unit projectors, positivity, isotropy and trace relation exact; PASS")


def main():
    for r in range(1, 11):
        check_dimension(r)
    print("Arithmetic: rational outer products and elimination only; no floating-point square roots.")
    print("Scope: finite construction replay; the universal minimum is proved in MS-2--MS-4.")


if __name__ == "__main__":
    main()
