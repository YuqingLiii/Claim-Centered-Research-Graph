#!/usr/bin/env python3
"""Local exact diagnostics for the straight-reduced-coordinate depth-10 blocker.

This is an analysis-only companion.  It imports the registered certificate code
read-only, reconstructs the same exact rational Bernstein tensors, restricts
them to the one recorded dyadic box, and itemizes the enclosure slack.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import log

import certify_su3_input_centered_triangle_sixdim as core
from certify_su3_chain_three_face_sixdim_covers import CONFIGURATIONS
from certify_su3_all_elementary_cycles import isotropic_probabilities
from certify_su3_triangular_three_face_clusters import (
    add_dense_controls,
    binary_interval_entropy_upper,
    build_union,
    compact_q_tail_parameter_upper,
    endpoint_patterns,
    retained_side_distributions,
    shifted_offsets,
)
from su3_common_den_controls import common_den_controls, rational_range_common


CONFIG = CONFIGURATIONS["straight-reduced-coordinate"]
DEGREES_GRAM = None
DEGREES_SIDE = None
TARGET_INDICES = (1023, 640, 520, 769, 917, 777)
TARGET_DEPTH = 10


def entropy_float(probabilities):
    return -sum(float(p) * log(float(p)) for p in probabilities if p)


def restrict_axis(controls, degrees, axis, index, depth):
    current = controls
    for shift in range(depth - 1, -1, -1):
        children = core.split_controls(current, degrees, axis)
        current = children[(index >> shift) & 1]
    return current


def restrict_to_target(controls, degrees):
    current = controls
    for axis, index in enumerate(TARGET_INDICES):
        current = restrict_axis(current, degrees, axis, index, TARGET_DEPTH)
    return current


def detailed_side(groups, denominator, bounds, branch_sets, q_constants):
    rows = []
    for side_index, (group, branches, q_constant) in enumerate(
        zip(groups, branch_sets, q_constants)
    ):
        if set(branches) == {"h", "m"}:
            interval = rational_range_common(group[0], denominator, bounds)
            exact_envelope = max(
                entropy_float((interval[0], 1 - interval[0])),
                entropy_float((interval[1], 1 - interval[1])),
            )
            if interval[0] <= F(1, 2) <= interval[1]:
                exact_envelope = log(2)
            rigorous = binary_interval_entropy_upper(*interval)
            rows.append((side_index, branches, "binary-hm", (interval,), rigorous, exact_envelope))
            continue
        if set(branches) == {"h", "c"}:
            interval = rational_range_common(group[0], denominator, bounds)
            binary_rigorous = binary_interval_entropy_upper(*interval)
            binary_exact = max(
                entropy_float((interval[0], 1 - interval[0])),
                entropy_float((interval[1], 1 - interval[1])),
            )
            if interval[0] <= F(1, 2) <= interval[1]:
                binary_exact = log(2)
            tail = add_dense_controls(group[1], group[2], denominator)
            tail_interval = rational_range_common(tail, denominator, bounds)
            conditional = compact_q_tail_parameter_upper(bounds[1][0], q_constant)
            conditional_entropy_exact = entropy_float((conditional, 1 - conditional))
            conditional_entropy_rigorous = core.entropy_bounds((conditional, 1 - conditional))[1]
            rigorous = binary_rigorous + tail_interval[1] * conditional_entropy_rigorous
            exact_envelope = binary_exact + float(tail_interval[1]) * conditional_entropy_exact
            rows.append((side_index, branches, "binary-hc-tail", (interval, tail_interval), rigorous, exact_envelope))
            continue
        intervals = tuple(rational_range_common(value, denominator, bounds) for value in group)
        rigorous = min(
            sum(core.component_entropy_upper(low, high) for low, high in intervals),
            core.log_bounds(F(3))[1],
        )
        exact_component_envelope = 0.0
        for low, high in intervals:
            lo = float(low)
            hi = float(high)
            optimum = min(max(1 / 2.718281828459045, lo), hi)
            exact_component_envelope += -optimum * log(optimum) if optimum else 0.0
        exact_envelope = min(exact_component_envelope, log(3))
        rows.append((side_index, branches, "ternary-component", intervals, rigorous, exact_envelope))
    return rows


def margin_parts(box, branch_sets, q_constants):
    gram_ranges = [
        rational_range_common(value, box.gram_denominator, box.bounds)
        for value in box.gram_numerators
    ]
    active = max(range(len(gram_ranges)), key=lambda index: gram_ranges[index][1])
    t_upper = gram_ranges[active][1]
    bell_rigorous = core.entropy_bounds(isotropic_probabilities(t_upper))[0]
    bell_exact_at_t_upper = entropy_float(isotropic_probabilities(t_upper))
    side_rows = detailed_side(
        box.side_groups, box.side_denominator, box.bounds, branch_sets, q_constants
    )
    side_active = min(range(len(side_rows)), key=lambda index: side_rows[index][4])
    row = side_rows[side_active]
    return {
        "gram_ranges": gram_ranges,
        "gram_active": active,
        "t_upper": t_upper,
        "bell_rigorous": bell_rigorous,
        "bell_exact_at_t_upper": bell_exact_at_t_upper,
        "side_rows": side_rows,
        "side_active": side_active,
        "side_rigorous": row[4],
        "side_exact_same_intervals": row[5],
        "margin_rigorous": float(bell_rigorous - 2 * row[4]),
        "margin_exact_logs_same_intervals": bell_exact_at_t_upper - 2 * row[5],
    }


def split_box(box, axis):
    gram_num_splits = [
        core.split_controls(value, DEGREES_GRAM, axis) for value in box.gram_numerators
    ]
    gram_den_splits = core.split_controls(box.gram_denominator, DEGREES_GRAM, axis)
    side_group_splits = [
        [core.split_controls(value, DEGREES_SIDE, axis) for value in group]
        for group in box.side_groups
    ]
    side_den_splits = core.split_controls(box.side_denominator, DEGREES_SIDE, axis)
    low, high = box.bounds[axis]
    midpoint = (low + high) / 2
    children = []
    for side in (0, 1):
        bounds = list(box.bounds)
        bounds[axis] = (low, midpoint) if side == 0 else (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        children.append(core.Box(
            tuple(pair[side] for pair in gram_num_splits), gram_den_splits[side],
            tuple(tuple(pair[side] for pair in group) for group in side_group_splits),
            side_den_splits[side], tuple(bounds), tuple(depths),
        ))
    return children


def main():
    global DEGREES_GRAM, DEGREES_SIDE
    core.CONFIG = CONFIG
    union = build_union(CONFIG.cluster)
    eliminated, patterns = endpoint_patterns(union[1], union[2], dict(CONFIG.retained))
    assert len(patterns) == CONFIG.expected_patterns

    gram_den = core.gram_denominator(union)
    base_degrees = core.polynomial_degrees(gram_den)
    DEGREES_GRAM = (base_degrees[0], base_degrees[1], 2, 2, 2, 2)
    gram_nums = tuple(
        core.reconstruct_gram_numerator(union, pattern, gram_den, DEGREES_GRAM)
        for pattern in patterns
    )
    print(f"reconstructed gram branches={len(gram_nums)} degrees={DEGREES_GRAM}", flush=True)

    side_den = core.side_denominator(union)
    base_side_degrees = core.polynomial_degrees(side_den)
    DEGREES_SIDE = (base_side_degrees[0], base_side_degrees[1], 1, 1, 1, 1)
    side_nums = core.reconstruct_side_numerators(union, side_den, DEGREES_SIDE)
    print(f"reconstructed side groups={len(side_nums)} degrees={DEGREES_SIDE}", flush=True)

    retained_offsets = dict(CONFIG.retained)
    shifted_inputs = dict(zip(union[1], shifted_offsets(CONFIG, union)[1]))
    branch_sets = tuple(
        tuple(branch for _, branch in incidence)
        for offset, incidence in zip(union[1], union[2])
        if offset in retained_offsets
    )
    q_constants = tuple(
        shifted_inputs[offset][1]
        for offset in union[1]
        if offset in retained_offsets
    )

    compact_gram_nums = tuple(
        common_den_controls(core.bernstein_coefficients(
            core.compactify(value, DEGREES_GRAM[0], DEGREES_GRAM[1]), DEGREES_GRAM
        )) for value in gram_nums
    )
    compact_gram_den = common_den_controls(core.bernstein_coefficients(
        core.compactify(gram_den, DEGREES_GRAM[0], DEGREES_GRAM[1]), DEGREES_GRAM
    ))
    compact_side_groups = tuple(tuple(
        common_den_controls(core.bernstein_coefficients(
            core.compactify(value, DEGREES_SIDE[0], DEGREES_SIDE[1]), DEGREES_SIDE
        )) for value in group
    ) for group in side_nums)
    compact_side_den = common_den_controls(core.bernstein_coefficients(
        core.compactify(side_den, DEGREES_SIDE[0], DEGREES_SIDE[1]), DEGREES_SIDE
    ))

    box = core.Box(
        tuple(restrict_to_target(value, DEGREES_GRAM) for value in compact_gram_nums),
        restrict_to_target(compact_gram_den, DEGREES_GRAM),
        tuple(tuple(restrict_to_target(value, DEGREES_SIDE) for value in group)
              for group in compact_side_groups),
        restrict_to_target(compact_side_den, DEGREES_SIDE),
        tuple((F(index, 1 << TARGET_DEPTH), F(index + 1, 1 << TARGET_DEPTH))
              for index in TARGET_INDICES),
        (TARGET_DEPTH,) * core.NVAR,
    )
    parts = margin_parts(box, branch_sets, q_constants)
    print("TARGET")
    for key in ("gram_active", "t_upper", "bell_rigorous", "bell_exact_at_t_upper",
                "side_active", "side_rigorous", "side_exact_same_intervals",
                "margin_rigorous", "margin_exact_logs_same_intervals"):
        print(f"{key}={parts[key]}")
    for row in parts["side_rows"]:
        print(f"side_row={row}")

    midpoint = tuple((low + high) / 2 for low, high in box.bounds)
    midpoint_gram = [core.gram_t(CONFIG, union, pattern, midpoint[0], midpoint[1], midpoint[2:])
                     for pattern in patterns]
    midpoint_t = max(midpoint_gram)
    midpoint_sides = retained_side_distributions(
        CONFIG, union, midpoint[0], midpoint[1], midpoint[2:]
    )
    midpoint_side_entropies = [entropy_float(distribution) for distribution in midpoint_sides]
    midpoint_bell = entropy_float(isotropic_probabilities(midpoint_t))
    print(f"midpoint_active_gram={max(range(len(midpoint_gram)), key=midpoint_gram.__getitem__)}")
    print(f"midpoint_t={midpoint_t}")
    print(f"midpoint_bell={midpoint_bell}")
    print(f"midpoint_side_entropies={midpoint_side_entropies}")
    print(f"midpoint_margin={midpoint_bell - 2 * min(midpoint_side_entropies)}")
    print(f"gram_t_slack={float(parts['t_upper'] - midpoint_t)}")

    print("ONE_EXTRA_SPLIT_PER_AXIS")
    split_summaries = []
    for axis in range(core.NVAR):
        child_parts = [margin_parts(child, branch_sets, q_constants) for child in split_box(box, axis)]
        margins = [child["margin_rigorous"] for child in child_parts]
        exact_log_margins = [child["margin_exact_logs_same_intervals"] for child in child_parts]
        summary = (axis, margins, exact_log_margins,
                   [float(child["t_upper"]) for child in child_parts],
                   [float(child["side_rigorous"]) for child in child_parts])
        split_summaries.append(summary)
        print(f"axis_split={summary}")

    # Follow the locally best bisection tree for three additional cuts.  This is
    # a diagnostic, not a complete cover unless every leaf becomes positive.
    frontier = [box]
    for generation in range(1, 4):
        next_frontier = []
        certified = 0
        for current in frontier:
            trials = []
            for axis in range(core.NVAR):
                children = split_box(current, axis)
                infos = [margin_parts(child, branch_sets, q_constants) for child in children]
                trials.append((min(info["margin_rigorous"] for info in infos), axis, children, infos))
            _, axis, children, infos = max(trials, key=lambda item: item[0])
            for child, info in zip(children, infos):
                if info["margin_rigorous"] > 0:
                    certified += 1
                else:
                    next_frontier.append(child)
        worst = min((margin_parts(item, branch_sets, q_constants)["margin_rigorous"]
                     for item in next_frontier), default=float("inf"))
        print(f"greedy_generation={generation} certified_leaves={certified} "
              f"uncertified_leaves={len(next_frontier)} worst_margin={worst}")
        frontier = next_frontier
        if not frontier:
            break


if __name__ == "__main__":
    main()
