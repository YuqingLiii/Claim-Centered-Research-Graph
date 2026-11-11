#!/usr/bin/env python3
"""Certified rational-log endpoint checks for the interior SU(3) mixture entropy proof."""

from __future__ import annotations

from fractions import Fraction


TERMS = 80


def reduced_log_bounds(y: Fraction) -> tuple[Fraction, Fraction]:
    """Bounds ln(y) for 1<=y<2 by the atanh series."""
    z = (y - 1) / (y + 1)
    total = Fraction(0)
    for n in range(TERMS):
        total += 2 * z ** (2 * n + 1) / (2 * n + 1)
    remainder = 2 * z ** (2 * TERMS + 1) / (
        (2 * TERMS + 1) * (1 - z * z)
    )
    return total, total + remainder


LN2_LOWER, LN2_UPPER = reduced_log_bounds(Fraction(2))


def log_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    if x <= 0:
        raise ValueError("log input must be positive")
    exponent = 0
    reduced = x
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    low, high = reduced_log_bounds(reduced)
    if exponent >= 0:
        return low + exponent * LN2_LOWER, high + exponent * LN2_UPPER
    return low + exponent * LN2_UPPER, high + exponent * LN2_LOWER


def entropy_bounds(probabilities: list[Fraction]) -> tuple[Fraction, Fraction]:
    low = Fraction(0)
    high = Fraction(0)
    for probability in probabilities:
        if not probability:
            continue
        log_low, log_high = log_bounds(probability)
        low -= probability * log_high
        high -= probability * log_low
    return low, high


def divergence_bounds(probabilities: list[Fraction]) -> tuple[Fraction, Fraction]:
    outcomes = len(probabilities)
    low = Fraction(0)
    high = Fraction(0)
    for probability in probabilities:
        if not probability:
            continue
        log_low, log_high = log_bounds(outcomes * probability)
        low += probability * log_low
        high += probability * log_high
    return low, high


def isotropic_probabilities(t: Fraction) -> list[Fraction]:
    return [(1 + 8 * t) / 9] + [(1 - t) / 9] * 8


def main() -> None:
    ln3_lower, _ = log_bounds(Fraction(3))
    boundary_kl_margin = (
        ln3_lower + Fraction(7, 12) - Fraction(7, 3) * LN2_UPPER
    )
    if boundary_kl_margin <= 0:
        raise AssertionError("boundary qutrit KL/collision inequality failed")
    print(
        "boundary KL/collision certified natural-log margin > "
        f"{float(boundary_kl_margin):.12e}"
    )

    low_t = Fraction(2, 3)
    _, divergence_upper = divergence_bounds(isotropic_probabilities(low_t))
    low_t_margin = Fraction(64, 45) * LN2_LOWER - divergence_upper
    if low_t_margin <= 0:
        raise AssertionError("low-t divergence endpoint inequality failed")
    print(f"low-t certified natural-log margin > {float(low_t_margin):.12e}")

    intervals = [
        (Fraction(2, 3), Fraction(3, 4), Fraction(22, 25)),
        (Fraction(3, 4), Fraction(4, 5), Fraction(93, 100)),
        (Fraction(4, 5), Fraction(5, 6), Fraction(24, 25)),
        (Fraction(5, 6), Fraction(6, 7), Fraction(39, 40)),
        (Fraction(6, 7), Fraction(7, 8), Fraction(99, 100)),
    ]
    for lower_t, upper_t, lower_a in intervals:
        square_margin = 6 * lower_t - Fraction(5, 4) - (3 * lower_a - 1) ** 2
        if square_margin <= 0:
            raise AssertionError("highest-weight lower bound failed")
        bell_lower, _ = entropy_bounds(isotropic_probabilities(upper_t))
        _, side_upper = entropy_bounds(
            [lower_a, (1 - lower_a) / 2, (1 - lower_a) / 2]
        )
        entropy_margin = bell_lower - 2 * side_upper
        if entropy_margin <= 0:
            raise AssertionError("high-t entropy endpoint inequality failed")
        print(
            f"[{lower_t},{upper_t}] certified natural-log margin > "
            f"{float(entropy_margin):.12e}; square margin {square_margin}"
        )

    print("all certified SU(3) interior-mixture endpoint inequalities passed")


if __name__ == "__main__":
    main()
