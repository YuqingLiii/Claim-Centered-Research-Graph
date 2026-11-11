#!/usr/bin/env python3
"""Certified box proof for the smallest SU(3) reducible-input branching cycle."""

from __future__ import annotations

from fractions import Fraction

from certify_su3_interior_mixture_entropy import entropy_bounds


BOXES = 16


COEFFICIENTS = {
    "constant": Fraction(41, 128),
    "x": Fraction(-15, 64),
    "y": Fraction(-3, 16),
    "z": Fraction(9, 64),
    "xx": Fraction(105, 128),
    "yy": Fraction(9, 40),
    "zz": Fraction(9, 128),
    "xy": Fraction(-3, 16),
    "yz": Fraction(-3, 16),
    "zx": Fraction(-15, 64),
}


def side_distribution(kind: str, value: Fraction) -> list[Fraction]:
    if kind == "x":
        return [(1 + 2 * value) / 3, 2 * (1 - value) / 3]
    if kind == "y":
        return [1 - 4 * value / 5, 2 * value / 5, 2 * value / 5]
    if kind == "z":
        return [(1 + value) / 4, (1 + value) / 4, (1 - value) / 2]
    raise ValueError(kind)


def side_entropy_upper(kind: str, low: Fraction, high: Fraction) -> Fraction:
    critical = {"x": Fraction(1, 4), "y": Fraction(5, 6), "z": Fraction(1, 3)}[kind]
    candidates = [low, high]
    if low <= critical <= high:
        candidates.append(critical)
    return max(entropy_bounds(side_distribution(kind, value))[1] for value in candidates)


def gram_upper(
    x_low: Fraction,
    x_high: Fraction,
    y_low: Fraction,
    y_high: Fraction,
    z_low: Fraction,
    z_high: Fraction,
) -> Fraction:
    c = COEFFICIENTS
    return (
        c["constant"]
        + c["x"] * x_low
        + c["y"] * y_low
        + c["z"] * z_high
        + c["xx"] * x_high * x_high
        + c["yy"] * y_high * y_high
        + c["zz"] * z_high * z_high
        + c["xy"] * x_low * y_low
        + c["yz"] * y_low * z_low
        + c["zx"] * z_low * x_low
    )


def isotropic_distribution(t: Fraction) -> list[Fraction]:
    return [(1 + 8 * t) / 9] + [(1 - t) / 9] * 8


def main() -> None:
    side_bounds = {kind: [] for kind in "xyz"}
    for kind in "xyz":
        for index in range(BOXES):
            side_bounds[kind].append(
                side_entropy_upper(
                    kind, Fraction(index, BOXES), Fraction(index + 1, BOXES)
                )
            )

    smallest = None
    location = None
    checked = 0
    for i in range(BOXES):
        x_low, x_high = Fraction(i, BOXES), Fraction(i + 1, BOXES)
        for j in range(BOXES):
            y_low, y_high = Fraction(j, BOXES), Fraction(j + 1, BOXES)
            for k in range(BOXES):
                z_low, z_high = Fraction(k, BOXES), Fraction(k + 1, BOXES)
                t_upper = gram_upper(x_low, x_high, y_low, y_high, z_low, z_high)
                if not 0 <= t_upper < 1:
                    raise AssertionError(("invalid Gram upper bound", i, j, k, t_upper))
                bell_lower = entropy_bounds(isotropic_distribution(t_upper))[0]
                side_upper = min(
                    side_bounds["x"][i], side_bounds["y"][j], side_bounds["z"][k]
                )
                margin = bell_lower - 2 * side_upper
                if margin <= 0:
                    raise AssertionError(("uncertified box", i, j, k, float(margin)))
                if smallest is None or margin < smallest:
                    smallest = margin
                    location = (i, j, k, t_upper)
                checked += 1

    print(f"rational boxes certified: {checked}")
    print(f"smallest certified natural-log margin > {float(smallest):.12e} at {location}")
    print("minimal SU(3) covariant branching cycle certified Bell-no-go")


if __name__ == "__main__":
    main()
