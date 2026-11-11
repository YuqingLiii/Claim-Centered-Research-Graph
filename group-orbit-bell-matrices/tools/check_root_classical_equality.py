#!/usr/bin/env python3
"""Exact finite replay of GROTHORB.root-classical-equality."""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial

from check_root_classical_value import image, roots_with_witness


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sign_nonzero(value):
    assert value != 0
    return 1 if value > 0 else -1


def check_orbit(r):
    roots, _ = roots_with_witness(r)
    rho = tuple(range(r - 1, -1, -1))
    directions = Counter(
        tuple(e * a for e, a in zip(epsilon, permuted))
        for permuted in permutations(rho)
        for epsilon in product((-1, 1), repeat=r)
    )
    expected_count = 2 ** (r - 1) * factorial(r)
    assert sum(directions.values()) == 2 ** r * factorial(r)
    assert len(directions) == expected_count
    assert set(directions.values()) == {2}

    pattern_to_direction = {}
    for y in directions:
        pattern = tuple(sign_nonzero(dot(w, y)) for w in roots)
        z = image(roots, pattern)
        assert z == tuple(4 * x for x in y)
        assert Fraction(dot(z, z), 4 * (r - 1)) == Fraction(2 * r * (2 * r - 1), 3)
        assert pattern not in pattern_to_direction
        pattern_to_direction[pattern] = y

    assert len(pattern_to_direction) == expected_count
    print(f"r={r}: {sum(directions.values())} signed permutations, "
          f"{expected_count} orbit vectors and distinct optimal patterns; "
          "multiplicity exactly 2, nonzero root products and W^T s=4y; PASS")
    return set(pattern_to_direction)


def check_all_bilinear_maximizers_r3(predicted):
    r = 3
    roots, _ = roots_with_witness(r)
    expected_numerator = 80
    maximizing_bob = set()
    seen = 0
    for bob in product((-1, 1), repeat=len(roots)):
        z = image(roots, bob)
        alice_coefficients = tuple(dot(w, z) for w in roots)
        numerator = sum(abs(value) for value in alice_coefficients)
        assert numerator <= expected_numerator
        if numerator == expected_numerator:
            # Nonzero coefficients certify that this maximizing Bob vector
            # has exactly one maximizing Alice choice, which must be Bob.
            alice = tuple(sign_nonzero(value) for value in alice_coefficients)
            assert alice == bob
            maximizing_bob.add(bob)
        seen += 1

    assert seen == 4096
    assert maximizing_bob == predicted
    assert len(maximizing_bob) == 24
    print("r=3: all 4096 Bob vectors enumerated; exactly 24 maximizing Bob "
          "vectors, each with unique Alice=Bob; predicted family exact; PASS")


def main():
    predicted_r3 = None
    for r in (3, 4, 5):
        patterns = check_orbit(r)
        if r == 3:
            predicted_r3 = patterns
    check_all_bilinear_maximizers_r3(predicted_r3)
    print("Scope: finite exact replay only; all-r equality proof is RE-2--RE-6.")


if __name__ == "__main__":
    main()
