"""Exact phase-5 shared-value positional composition and S_N average.

Each labeled position block uses the phase-3 axis/interior divided-difference
kernel on the same full set of nonfixed sigma-pairs.  The fixed point is unused.
The raw block tensor is averaged over S_N.  At occupancy level this average is
the convolution of the block occupancy measures, followed by the uniform orbit
lift.  All arithmetic is exact ``fractions.Fraction``.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


CASES = ((10, 5, 2), (12, 5, 2), (14, 5, 2), (12, 7, 2))


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def falling(value: int, order: int) -> int:
    return math.prod(value - offset for offset in range(order))


def involution_data(q: int, target: int):
    if q % 2 != 1:
        raise ValueError("phase 5 is restricted to odd q")
    sigma = tuple((target - a) % q for a in range(q))
    fixed = [a for a in range(q) if sigma[a] == a]
    assert len(fixed) == 1
    seen = set(fixed)
    pairs = []
    for a in range(q):
        if a not in seen:
            b = sigma[a]
            pairs.append(tuple(sorted((a, b))))
            seen.update((a, b))
    return sigma, fixed[0], tuple(sorted(pairs))


def balanced_totals(block_size: int, pair_count: int):
    low, extra = divmod(block_size, pair_count)
    if low < 2:
        raise ValueError("each positional block needs at least two positions per sigma-pair")
    row = (low + 1,) * extra + (low,) * (pair_count - extra)
    return tuple(sorted(set(itertools.permutations(row))))


def axis_probability(size: int):
    return (((size, 0), Fraction(1, 2)), ((0, size), Fraction(1, 2)))


def interior_probability(size: int):
    lo, hi = size // 2, size - size // 2
    if lo == hi:
        return (((lo, hi), Fraction(1)),)
    return (((lo, hi), Fraction(1, 2)), ((hi, lo), Fraction(1, 2)))


def divided_difference_outer(pair_count: int):
    nodes = [0]
    power = 1
    while power <= pair_count:
        nodes.append(power)
        power *= 5
    raw = {}
    for node in nodes:
        raw[node] = Fraction(1, math.prod(node - other for other in nodes if other != node))
    if raw[0] > 0:
        raw = {node: -weight for node, weight in raw.items()}
    norm = sum(abs(weight) for weight in raw.values())
    outer = {node: weight / norm for node, weight in raw.items()}
    order = len(nodes) - 1
    assert outer[0] < 0
    assert sum(abs(weight) for weight in outer.values()) == 1
    for degree in range(order):
        assert sum(weight * falling(node, degree) for node, weight in outer.items()) == 0
    return order, outer


def block_measure(block_size: int, q: int, target: int):
    sigma, fixed, pairs = involution_data(q, target)
    totals = balanced_totals(block_size, len(pairs))
    order, outer = divided_difference_outer(len(pairs))
    answer = {}
    for row in totals:
        for active_count, layer_weight in outer.items():
            for active_tuple in itertools.combinations(range(len(pairs)), active_count):
                active = frozenset(active_tuple)
                pattern_weight = (
                    Fraction(1, len(totals))
                    * layer_weight
                    / math.comb(len(pairs), active_count)
                )
                local_tables = [
                    interior_probability(size) if index in active else axis_probability(size)
                    for index, size in enumerate(row)
                ]
                for choices in itertools.product(*local_tables):
                    counts = [0] * q
                    weight = pattern_weight
                    for (a, b), ((i, j), local_weight) in zip(pairs, choices):
                        counts[a], counts[b] = i, j
                        weight *= local_weight
                    key = tuple(counts)
                    answer[key] = answer.get(key, Fraction(0)) + weight
    answer = {counts: weight for counts, weight in answer.items() if weight}
    assert all(counts[fixed] == 0 and sum(counts) == block_size for counts in answer)
    assert sum(answer.values()) == 0
    assert sum(abs(weight) for weight in answer.values()) == 1
    return sigma, fixed, pairs, totals, 2 * order, outer, answer


def convolve(left, right):
    answer = {}
    for a, wa in left.items():
        for b, wb in right.items():
            key = tuple(x + y for x, y in zip(a, b))
            answer[key] = answer.get(key, Fraction(0)) + wa * wb
    return {counts: weight for counts, weight in answer.items() if weight}


def convolution_power(measure, exponent: int):
    q = len(next(iter(measure)))
    result = {(0,) * q: Fraction(1)}
    for _ in range(exponent):
        result = convolve(result, measure)
    return result


def function_label(counts, sigma):
    for a, b in enumerate(sigma):
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def move_counts(counts, permutation):
    answer = [0] * len(counts)
    for old, new in enumerate(permutation):
        answer[new] = counts[old]
    return tuple(answer)


def centralizer(q: int, sigma):
    return tuple(
        permutation
        for permutation in itertools.permutations(range(q))
        if all(permutation[sigma[a]] == sigma[permutation[a]] for a in range(q))
    )


def moment_rows(weights, q: int, band: int):
    rows = 0
    for degree in range(band):
        for alpha in weak_compositions(degree, q):
            rows += 1
            residual = sum(
                weight * math.prod(falling(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    return rows


def check_case(n: int, q: int, block_count: int, target: int):
    if n % block_count:
        raise ValueError("finite gates use equal integer position blocks")
    block_size = n // block_count
    sigma, fixed, pairs, totals, inner_band, outer, block = block_measure(
        block_size, q, target
    )
    averaged = convolution_power(block, block_count)
    assert all(sum(counts) == n and counts[fixed] == 0 for counts in averaged)
    assert sum(averaged.values()) == 0

    # Choose the harmless global orientation making the true global NO mass negative.
    no_mass = sum(
        weight for counts, weight in averaged.items() if function_label(counts, sigma) == -1
    )
    orientation = -1 if no_mass > 0 else 1
    averaged = {counts: orientation * weight for counts, weight in averaged.items()}
    no_mass *= orientation
    assert no_mass < 0

    post_average_l1 = sum(abs(weight) for weight in averaged.values())
    normalized = {counts: weight / post_average_l1 for counts, weight in averaged.items()}
    assert sum(abs(weight) for weight in normalized.values()) == 1

    band = block_count * inner_band
    rows = moment_rows(normalized, q, band)
    correlation_numerator = sum(
        weight * function_label(counts, sigma) for counts, weight in averaged.items()
    )
    normalized_correlation = correlation_numerator / post_average_l1
    assert correlation_numerator == -2 * no_mass

    r = len(pairs)
    expected_no_mass_abs = abs(outer[0]) ** block_count * Fraction(
        1, 2 ** (r * (block_count - 1))
    )
    blockwise_or_numerator = 2 * abs(outer[0]) ** block_count
    cross_block_factor = Fraction(1, 2 ** (r * (block_count - 1)))
    assert -no_mass == expected_no_mass_abs
    assert correlation_numerator == blockwise_or_numerator * cross_block_factor

    group = centralizer(q, sigma)
    for counts, weight in normalized.items():
        for permutation in group:
            assert normalized.get(move_counts(counts, permutation), Fraction(0)) == weight

    layer_masses = {}
    layer_signs = {}
    for counts, weight in normalized.items():
        layer = sum(bool(counts[a] and counts[b]) for a, b in pairs)
        layer_masses[layer] = layer_masses.get(layer, Fraction(0)) + weight
        layer_signs.setdefault(layer, set()).add(1 if weight > 0 else -1)

    return {
        "case": [n, q, target, block_count],
        "block_size": block_size,
        "fixed_point": fixed,
        "sigma_pairs": [list(pair) for pair in pairs],
        "all_blocks_share_all_sigma_pairs": True,
        "pair_total_assignments_per_block": [list(row) for row in totals],
        "outer_layer_weights": {str(k): str(v) for k, v in outer.items()},
        "inner_band": inner_band,
        "averaged_band": band,
        "factorial_rows_checked": rows,
        "block_support": len(block),
        "post_average_support": len(averaged),
        "raw_tensor_l1": "1",
        "post_average_l1_before_renormalization": str(post_average_l1),
        "post_renormalization_l1": "1",
        "true_no_mass_before_renormalization": str(no_mass),
        "blockwise_or_correlation_numerator": str(blockwise_or_numerator),
        "cross_block_no_consistency_factor": str(cross_block_factor),
        "true_2sum_correlation_numerator": str(correlation_numerator),
        "normalized_true_2sum_correlation": str(normalized_correlation),
        "strictly_above_two_thirds": normalized_correlation > Fraction(2, 3),
        "centralizer_order": len(group),
        "global_K_layer_signed_masses": {
            str(layer): str(mass) for layer, mass in sorted(layer_masses.items())
        },
        "global_K_layers_with_both_weight_signs": [
            layer for layer, signs in sorted(layer_signs.items()) if len(signs) == 2
        ],
        "m2_condition_5_escape_signature": (
            "global K=r layer has support but zero signed mass"
            if r in layer_masses and layer_masses[r] == 0
            else "mixed signs occur within a global K layer"
        ),
        "normalized_weights": [
            {"counts": list(counts), "weight": str(weight)}
            for counts, weight in sorted(normalized.items())
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    records = [
        check_case(n, q, block_count, target)
        for n, q, block_count in CASES
        for target in range(q)
    ]
    payload = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "construction": "shared-value positional block tensor, S_N average, exact l1 renormalization",
        "occupancy_average": "m-fold convolution followed by uniform S_N orbit lift",
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "arithmetic": payload["arithmetic"],
        "checks": [
            {key: record[key] for key in (
                "case", "inner_band", "averaged_band", "factorial_rows_checked",
                "post_average_l1_before_renormalization", "true_no_mass_before_renormalization",
                "cross_block_no_consistency_factor", "normalized_true_2sum_correlation",
                "strictly_above_two_thirds", "centralizer_order",
            )}
            for record in records
        ],
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
