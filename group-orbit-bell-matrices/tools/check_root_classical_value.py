#!/usr/bin/env python3
"""Exact finite checks for GROTHORB.root-classical; no all-r inference."""

from fractions import Fraction
from itertools import product


def roots_with_witness(r):
    roots = []
    witness = []
    for i in range(r):
        for j in range(i + 1, r):
            for alpha, beta in product((-1, 1), repeat=2):
                w = [0] * r
                w[i], w[j] = alpha, beta
                roots.append(tuple(w))
                witness.append(alpha)
    return roots, tuple(witness)


def image(roots, signs):
    return tuple(sum(s * w[k] for s, w in zip(signs, roots))
                 for k in range(len(roots[0])))


def main():
    for r in range(3, 13):
        roots, witness = roots_with_witness(r)
        n = 2 * r * (r - 1)
        assert len(roots) == len(set(roots)) == n
        assert all(tuple(-x for x in w) in roots for w in roots)
        rho = tuple(range(r - 1, -1, -1))
        z = image(roots, witness)
        assert z == tuple(4 * x for x in rho)
        assert all(s * sum(a * b for a, b in zip(w, rho)) > 0
                   for s, w in zip(witness, roots))
        value = Fraction(sum(x * x for x in z), 4 * (r - 1))
        expected = Fraction(2 * r * (2 * r - 1), 3)
        assert value == expected
        print(f"r={r}: n={n}, exact witness value={value}; PASS")

    r = 3
    roots, _ = roots_with_witness(r)
    maximum_numerator = -1
    enumerated = 0
    for signs in product((-1, 1), repeat=len(roots)):
        z = image(roots, signs)
        # For fixed Bob signs, max_s s^T WW^T t = ||WW^T t||_1.
        numerator = sum(abs(sum(a * b for a, b in zip(w, z)))
                        for w in roots)
        maximum_numerator = max(maximum_numerator, numerator)
        enumerated += 1
    value = Fraction(maximum_numerator, 4 * (r - 1))
    assert enumerated == 4096
    assert value == 10
    print(f"r=3: enumerated all {enumerated} Bob signs; "
          f"exact bilinear maximum={value}; PASS")
    print("Scope: finite exact checks only; the all-r argument is in RC-2--RC-4.")


if __name__ == "__main__":
    main()
