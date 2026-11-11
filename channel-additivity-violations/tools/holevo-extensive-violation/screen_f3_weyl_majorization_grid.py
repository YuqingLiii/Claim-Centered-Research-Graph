#!/usr/bin/env python3
"""Exact rational-grid screen for the selected-line F_3^2 Weyl majorization.

This is route-selection evidence, not a continuum certificate.  A distribution
is represented by nine nonnegative integers summing to ``denominator``.  All
majorization comparisons are then performed with integer numerators over the
common denominator squared.  Every direction containing a maximum-mass affine
line is checked, including ties.
"""

import argparse
from itertools import combinations


Q = 3
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (1, 2))


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, parts - 1, prefix + (value,))


def projection(weights, direction):
    u, v = direction
    result = [0] * Q
    for i in range(Q):
        for j in range(Q):
            result[(u * i + v * j) % Q] += weights[Q * i + j]
    return tuple(result)


def autocorrelation_numerators(weights):
    result = []
    for a in range(Q):
        for b in range(Q):
            result.append(
                sum(
                    weights[Q * i + j]
                    * weights[Q * ((i - a) % Q) + ((j - b) % Q)]
                    for i in range(Q)
                    for j in range(Q)
                )
            )
    return tuple(result)


def cumulative_margins(weights):
    quotients = [projection(weights, direction) for direction in DIRECTIONS]
    maximum = max(max(quotient) for quotient in quotients)
    selected = [quotient for quotient in quotients if max(quotient) == maximum]
    correlation = sorted(autocorrelation_numerators(weights), reverse=True)
    correlation_cumulative = []
    running = 0
    for value in correlation[:-1]:
        running += value
        correlation_cumulative.append(running)

    direction_margins = []
    for quotient in selected:
        product = sorted((left * right for left in quotient for right in quotient), reverse=True)
        product_cumulative = []
        running = 0
        for value in product[:-1]:
            running += value
            product_cumulative.append(running)
        direction_margins.append(
            tuple(right - left for left, right in zip(correlation_cumulative, product_cumulative))
        )
    return tuple(direction_margins)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--denominator", type=int, default=12)
    parser.add_argument("--progress-every", type=int, default=100_000)
    parser.add_argument("--strictly-positive", action="store_true")
    args = parser.parse_args()

    minima = [None] * 8
    records = [None] * 8
    positive_minima = [None] * 8
    positive_records = [None] * 8
    zero_counts = [0] * 8
    pair_branch_minima = {
        (includes_selected, branch): None
        for includes_selected in (False, True)
        for branch in (1, 2)
    }
    pair_branch_records = dict(pair_branch_minima)
    distributions = 0
    selected_cases = 0
    residual = args.denominator - (Q * Q if args.strictly_positive else 0)
    if residual < 0:
        raise SystemExit("denominator is too small for strictly positive weights")
    for raw_weights in compositions(residual, Q * Q):
        weights = tuple(value + 1 for value in raw_weights) if args.strictly_positive else raw_weights
        distributions += 1
        margins_by_direction = cumulative_margins(weights)
        quotients = [projection(weights, direction) for direction in DIRECTIONS]
        maximum = max(max(quotient) for quotient in quotients)
        selected_direction_indices = [
            index for index, quotient in enumerate(quotients) if max(quotient) == maximum
        ]
        correlation = autocorrelation_numerators(weights)
        q_zero = correlation[0]
        collisions = [sum(value * value for value in quotient) for quotient in quotients]
        for direction_index, margins in enumerate(margins_by_direction):
            selected_cases += 1
            for index, margin in enumerate(margins):
                if minima[index] is None or margin < minima[index]:
                    minima[index] = margin
                    records[index] = (weights, direction_index)
                if margin == 0:
                    zero_counts[index] += 1
                elif margin > 0 and (positive_minima[index] is None or margin < positive_minima[index]):
                    positive_minima[index] = margin
                    positive_records[index] = (weights, direction_index)
            selected_global_index = selected_direction_indices[direction_index]
            a, b, c = sorted(quotients[selected_global_index], reverse=True)
            branch_values = {
                1: args.denominator * args.denominator - c * (args.denominator + b),
                2: args.denominator * args.denominator - (b + c) * (b + c),
            }
            for left, right in combinations(range(len(DIRECTIONS)), 2):
                q_top_five_candidate = collisions[left] + collisions[right] - q_zero
                includes_selected = selected_global_index in (left, right)
                for branch, target in branch_values.items():
                    key = (includes_selected, branch)
                    margin = target - q_top_five_candidate
                    if pair_branch_minima[key] is None or margin < pair_branch_minima[key]:
                        pair_branch_minima[key] = margin
                        pair_branch_records[key] = (
                            weights,
                            selected_global_index,
                            (left, right),
                            (a, b, c),
                        )
        if args.progress_every and distributions % args.progress_every == 0:
            print(f"distributions={distributions}; selected_direction_cases={selected_cases}", flush=True)

    print(f"denominator={args.denominator}")
    print(f"strictly_positive={args.strictly_positive}")
    print(f"distributions={distributions}")
    print(f"selected_direction_cases={selected_cases}")
    for index, (margin, record) in enumerate(zip(minima, records), start=1):
        print(
            f"k={index}: minimum integer margin={margin}; record={record}; "
            f"zero cases={zero_counts[index - 1]}; minimum positive margin={positive_minima[index - 1]}; "
            f"positive record={positive_records[index - 1]}"
        )
    for key in sorted(pair_branch_minima):
        print(
            f"k=5 pair branch {key}: minimum integer margin={pair_branch_minima[key]}; "
            f"record={pair_branch_records[key]}"
        )
    print("EXACT GRID SCREEN ONLY: continuum majorization is not certified")


if __name__ == "__main__":
    main()
