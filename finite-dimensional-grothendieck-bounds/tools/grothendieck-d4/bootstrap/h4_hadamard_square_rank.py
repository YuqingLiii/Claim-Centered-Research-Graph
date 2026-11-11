#!/usr/bin/env python3

import sys

import h5py
import numpy as np
import sympy as sp

import h4_level2_sos as h4


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: python h4_hadamard_square_rank.py file.mat")

    with h5py.File(sys.argv[1], "r") as f:
        A = h4.exact_integer_matrix(f["A"][()], "A")
        Pfloat = np.asarray(f["P"][()], dtype=np.float64)

    rec = h4.reconstruct_P(A, Pfloat)
    X, Y = rec["X"], rec["Y"]

    Hfloat = Pfloat * Pfloat
    chosen = []
    for i in range(h4.N):
        trial = chosen + [i]
        principal = Hfloat[np.ix_(trial, trial)]
        if np.linalg.matrix_rank(principal, tol=1e-9) == len(trial):
            chosen = trial
        if len(chosen) == 10:
            break

    if len(chosen) != 10:
        raise SystemExit(f"failed to find 10 independent tensors: {chosen}")

    sqrt5 = sp.sqrt(5)
    exact_minor = sp.Matrix([
        [
            int(X[i, j]) ** 2
            + 5 * int(Y[i, j]) ** 2
            + 2 * int(X[i, j]) * int(Y[i, j]) * sqrt5
            for j in chosen
        ]
        for i in chosen
    ])
    determinant = sp.collect(
        sp.expand(sp.radsimp(exact_minor.det(method="domain-ge"))),
        sqrt5,
    )

    if determinant == 0:
        raise SystemExit("selected exact 10x10 minor vanishes")

    print("indices =", chosen)
    print("exact_scaled_minor_determinant =", determinant)
    print("rank_P_hadamard_square = 10")


if __name__ == "__main__":
    main()
