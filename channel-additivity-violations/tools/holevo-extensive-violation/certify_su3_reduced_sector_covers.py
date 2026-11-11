#!/usr/bin/env python3
"""Exact reduced-sector SU(3) three-face Bernstein checkers.

The default mode performs exact reconstruction, compactification, initial-sector
verification, and a bounded number of smoke-test subdivisions.  A full adaptive
certificate is available only behind the explicit ``--certificate`` flag.  This
file is independent of the older long-running input scripts.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from math import comb

import certify_su3_highest_edge_adjacent_faces as polynomial_core
from certify_su3_adjacent_elementary_faces import component_entropy_upper
from certify_su3_all_elementary_cycles import (
    entropy_bounds,
    isotropic_probabilities,
    log_bounds,
)
from certify_su3_triangular_three_face_clusters import (
    Configuration,
    add_dense_controls,
    binary_interval_entropy_upper,
    build_union,
    compact_q_tail_parameter_upper,
    endpoint_patterns,
    gram_denominator,
    gram_t,
    retained_coordinate_count,
    retained_side_distributions,
    shifted_offsets,
    side_denominator,
)
from su3_common_den_controls import (
    CommonDenControls,
    common_den_controls,
    rational_range_common,
    split_common_controls,
)


F = Fraction
Poly = dict[tuple[int, ...], F]


INPUT_TRIANGLE = ((-2, 1), (-1, -1), (0, 0))
WEAKEST_BENT = ((-3, 0), (-2, 1), (0, 0))


@dataclass(frozen=True)
class SectorSpec:
    name: str
    config: Configuration
    free_labels: tuple[str, ...]
    fixed_labels: tuple[tuple[str, F], ...]
    initial_sector: str

    @property
    def coordinate_count(self) -> int:
        return retained_coordinate_count(self.config)

    @property
    def nvar(self) -> int:
        return len(self.free_labels) + self.coordinate_count


SPECS = {
    "input-low": SectorSpec(
        "input-centered-low-P",
        Configuration(
            "input-centered-low-P",
            INPUT_TRIANGLE,
            (((-1, 1), "binary"), ((1, 0), "binary"), ((2, -2), "binary")),
            24,
        ),
        ("P", "Q"),
        (),
        "a-low-63-over-64",
    ),
    "input-high": SectorSpec(
        "input-centered-high-P",
        Configuration(
            "input-centered-high-P",
            INPUT_TRIANGLE,
            (((-2, 0), "binary"), ((1, -3), "binary"), ((1, 0), "binary")),
            24,
        ),
        ("P", "Q"),
        (),
        "a-high-63-over-64",
    ),
    "bent-main": SectorSpec(
        "weakest-bent-P-at-least-one",
        Configuration(
            "weakest-bent-fixed-two",
            WEAKEST_BENT,
            (((-1, 1), "binary"), ((1, 0), "binary")),
            72,
        ),
        ("P", "Q"),
        (),
        "a-right-half",
    ),
    "bent-q-face": SectorSpec(
        "weakest-bent-P-zero-Q-at-least-one",
        Configuration(
            "weakest-bent-fixed-two",
            WEAKEST_BENT,
            (((-1, 1), "binary"), ((1, 0), "binary")),
            72,
        ),
        ("Q",),
        (("P", F(0)),),
        "q-right-half",
    ),
    "bent-origin": SectorSpec(
        "weakest-bent-origin-fixed-three",
        Configuration(
            "weakest-bent-origin-fixed-three",
            WEAKEST_BENT,
            (
                ((-1, -2), "binary"),
                ((-1, 1), "binary"),
                ((1, 0), "binary"),
            ),
            36,
        ),
        (),
        (("P", F(0)), ("Q", F(0))),
        "full",
    ),
}


def set_polynomial_dimension(nvar: int) -> None:
    polynomial_core.NVAR = nvar


def poly_evaluate(poly: Poly, values: tuple[F, ...]) -> F:
    return polynomial_core.poly_evaluate(poly, values)


def polynomial_degrees(poly: Poly) -> tuple[int, ...]:
    return polynomial_core.polynomial_degrees(poly)


def tensor_interpolate(values, degrees):
    return polynomial_core.tensor_interpolate(values, degrees)


def bernstein_coefficients(poly, degrees):
    return polynomial_core.bernstein_coefficients(poly, degrees)


def specialize_polynomial(
    poly: Poly, fixed_axes: dict[int, F], original_nvar: int
) -> Poly:
    retained_axes = [axis for axis in range(original_nvar) if axis not in fixed_axes]
    result: Poly = {}
    for monomial, coefficient in poly.items():
        value = coefficient
        for axis, fixed in fixed_axes.items():
            value *= fixed ** monomial[axis]
        if not value:
            continue
        target = tuple(monomial[axis] for axis in retained_axes)
        result[target] = result.get(target, F(0)) + value
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def base_denominator_polynomials(spec: SectorSpec, union):
    """Build public P,Q denominators, then exactly specialize fixed label axes."""
    full_nvar = 2 + spec.coordinate_count
    set_polynomial_dimension(full_nvar)
    gram = gram_denominator(spec.config, union)
    side = side_denominator(spec.config, union)
    fixed = dict(spec.fixed_labels)
    fixed_axes = {}
    if "P" in fixed:
        fixed_axes[0] = fixed["P"]
    if "Q" in fixed:
        fixed_axes[1] = fixed["Q"]
    if fixed_axes:
        gram = specialize_polynomial(gram, fixed_axes, full_nvar)
        side = specialize_polynomial(side, fixed_axes, full_nvar)
    set_polynomial_dimension(spec.nvar)
    return gram, side


def decode_point(spec: SectorSpec, point: tuple[F, ...]):
    labels = dict(spec.fixed_labels)
    for axis, name in enumerate(spec.free_labels):
        labels[name] = point[axis]
    coordinates = point[len(spec.free_labels):]
    return labels.get("P", F(0)), labels.get("Q", F(0)), coordinates


def interpolation_test_points(spec: SectorSpec) -> tuple[tuple[F, ...], ...]:
    values = (
        F(1, 3), F(2, 5), F(3, 7), F(4, 9), F(5, 11), F(6, 13)
    )
    first = tuple(values[index] for index in range(spec.nvar))
    second = tuple(
        (F(7, 4), F(8, 3), F(2, 3), F(5, 8), F(7, 10), F(9, 11))[index]
        for index in range(spec.nvar)
    )
    return first, second


def reconstruct_gram_numerator(
    spec: SectorSpec, union, pattern, denominator: Poly, degrees
) -> Poly:
    values = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        point = tuple(map(F, index))
        P, Q, coordinates = decode_point(spec, point)
        values[index] = (
            gram_t(spec.config, union, pattern, P, Q, coordinates)
            * poly_evaluate(denominator, point)
        )
    numerator = tensor_interpolate(values, degrees)
    for test in interpolation_test_points(spec):
        P, Q, coordinates = decode_point(spec, test)
        direct = gram_t(spec.config, union, pattern, P, Q, coordinates)
        reconstructed = poly_evaluate(numerator, test) / poly_evaluate(denominator, test)
        if direct != reconstructed:
            raise AssertionError(("Gram reconstruction mismatch", spec.name, pattern, test))
    return numerator


def reconstruct_side_numerators(
    spec: SectorSpec, union, denominator: Poly, degrees
):
    tables = [[{} for _ in range(3)] for _ in spec.config.retained]
    for index in product(*(range(degree + 1) for degree in degrees)):
        point = tuple(map(F, index))
        P, Q, coordinates = decode_point(spec, point)
        distributions = retained_side_distributions(
            spec.config, union, P, Q, coordinates
        )
        denominator_value = poly_evaluate(denominator, point)
        for side_index, distribution in enumerate(distributions):
            for component, probability in enumerate(distribution):
                tables[side_index][component][index] = probability * denominator_value
    numerators = tuple(
        tuple(tensor_interpolate(table, degrees) for table in group)
        for group in tables
    )
    test = interpolation_test_points(spec)[0]
    P, Q, coordinates = decode_point(spec, test)
    direct = retained_side_distributions(spec.config, union, P, Q, coordinates)
    denominator_value = poly_evaluate(denominator, test)
    reconstructed = tuple(
        tuple(poly_evaluate(value, test) / denominator_value for value in group)
        for group in numerators
    )
    if direct != reconstructed:
        raise AssertionError(("side reconstruction mismatch", spec.name, test))
    return numerators


def compactify_free_labels(poly: Poly, degrees, label_count: int) -> Poly:
    """Substitute X=a/(1-a) and homogenize each remaining free label axis."""
    result: Poly = {}
    for monomial, coefficient in poly.items():
        options = []
        for axis in range(label_count):
            power = monomial[axis]
            options.append(tuple(
                (tail, F(comb(degrees[axis] - power, tail)) * (-1) ** tail)
                for tail in range(degrees[axis] - power + 1)
            ))
        for choices in product(*options) if options else ((),):
            target = list(monomial)
            value = coefficient
            for axis, (tail, factor) in enumerate(choices):
                target[axis] += tail
                value *= factor
            target_tuple = tuple(target)
            result[target_tuple] = result.get(target_tuple, F(0)) + value
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


@dataclass(frozen=True)
class ExactData:
    spec: SectorSpec
    union: tuple
    patterns: tuple
    gram_degrees: tuple[int, ...]
    side_degrees: tuple[int, ...]
    gram_numerators: tuple[CommonDenControls, ...]
    gram_denominator: CommonDenControls
    side_groups: tuple[tuple[CommonDenControls, ...], ...]
    side_denominator: CommonDenControls
    branch_sets: tuple[tuple[str, ...], ...]
    q_constants: tuple[int, ...]


@dataclass(frozen=True)
class Box:
    gram_numerators: tuple[CommonDenControls, ...]
    side_groups: tuple[tuple[CommonDenControls, ...], ...]
    gram_denominator: CommonDenControls
    side_denominator: CommonDenControls
    bounds: tuple[tuple[F, F], ...]
    depths: tuple[int, ...]


@dataclass(frozen=True)
class Assessment:
    t_lower: F
    t_upper: F
    side_upper: F | None
    margin: F | None
    active_count: int
    active_numerators: tuple[CommonDenControls, ...]


def reconstruct_exact_data(spec: SectorSpec) -> ExactData:
    set_polynomial_dimension(spec.nvar)
    union = build_union(spec.config.cluster)
    _, patterns = endpoint_patterns(union[1], union[2], dict(spec.config.retained))
    if len(patterns) != spec.config.expected_patterns:
        raise AssertionError((spec.name, len(patterns), spec.config.expected_patterns))

    gram_den, side_den = base_denominator_polynomials(spec, union)
    gram_base_degrees = polynomial_degrees(gram_den)
    side_base_degrees = polynomial_degrees(side_den)
    gram_degrees = tuple(
        gram_base_degrees[axis] if axis < len(spec.free_labels) else 2
        for axis in range(spec.nvar)
    )
    side_degrees = tuple(
        side_base_degrees[axis] if axis < len(spec.free_labels) else 1
        for axis in range(spec.nvar)
    )

    gram_nums = tuple(
        reconstruct_gram_numerator(spec, union, pattern, gram_den, gram_degrees)
        for pattern in patterns
    )
    side_nums = reconstruct_side_numerators(
        spec, union, side_den, side_degrees
    )

    compact_gram_numerators = tuple(
        common_den_controls(bernstein_coefficients(
            compactify_free_labels(value, gram_degrees, len(spec.free_labels)),
            gram_degrees,
        ))
        for value in gram_nums
    )
    compact_gram_denominator = common_den_controls(bernstein_coefficients(
        compactify_free_labels(gram_den, gram_degrees, len(spec.free_labels)),
        gram_degrees,
    ))
    compact_side_groups = tuple(
        tuple(common_den_controls(bernstein_coefficients(
            compactify_free_labels(value, side_degrees, len(spec.free_labels)),
            side_degrees,
        )) for value in group)
        for group in side_nums
    )
    compact_side_denominator = common_den_controls(bernstein_coefficients(
        compactify_free_labels(side_den, side_degrees, len(spec.free_labels)),
        side_degrees,
    ))

    retained = dict(spec.config.retained)
    shifted_inputs = dict(zip(union[1], shifted_offsets(spec.config, union)[1]))
    branch_sets = tuple(
        tuple(branch for _, branch in incidence)
        for offset, incidence in zip(union[1], union[2])
        if offset in retained
    )
    q_constants = tuple(
        shifted_inputs[offset][1] for offset in union[1] if offset in retained
    )
    return ExactData(
        spec,
        union,
        patterns,
        gram_degrees,
        side_degrees,
        compact_gram_numerators,
        compact_gram_denominator,
        compact_side_groups,
        compact_side_denominator,
        branch_sets,
        q_constants,
    )


def root_box(data: ExactData) -> Box:
    return Box(
        data.gram_numerators,
        data.side_groups,
        data.gram_denominator,
        data.side_denominator,
        tuple((F(0), F(1)) for _ in range(data.spec.nvar)),
        (0,) * data.spec.nvar,
    )


def split_box(data: ExactData, box: Box, axis: int) -> tuple[Box, Box]:
    gram_splits = tuple(
        split_common_controls(value, data.gram_degrees, axis)
        for value in box.gram_numerators
    )
    gram_den_splits = split_common_controls(
        box.gram_denominator, data.gram_degrees, axis
    )
    side_splits = tuple(
        tuple(split_common_controls(value, data.side_degrees, axis) for value in group)
        for group in box.side_groups
    )
    side_den_splits = split_common_controls(
        box.side_denominator, data.side_degrees, axis
    )
    low, high = box.bounds[axis]
    midpoint = (low + high) / 2
    output = []
    for side in (0, 1):
        bounds = list(box.bounds)
        bounds[axis] = (low, midpoint) if side == 0 else (midpoint, high)
        depths = list(box.depths)
        depths[axis] += 1
        output.append(Box(
            tuple(pair[side] for pair in gram_splits),
            tuple(tuple(pair[side] for pair in group) for group in side_splits),
            gram_den_splits[side],
            side_den_splits[side],
            tuple(bounds),
            tuple(depths),
        ))
    return output[0], output[1]


def reset_depths(box: Box) -> Box:
    return replace(box, depths=(0,) * len(box.depths))


def initial_boxes(data: ExactData) -> tuple[Box, ...]:
    sector = data.spec.initial_sector
    root = root_box(data)
    if sector == "full":
        return (root,)
    if sector in ("a-right-half", "q-right-half"):
        _, right = split_box(data, root, 0)
        return (reset_depths(right),)
    if sector in ("a-low-63-over-64", "a-high-63-over-64"):
        low_slabs = []
        right = root
        for _ in range(6):
            left, right = split_box(data, right, 0)
            low_slabs.append(reset_depths(left))
        if sector == "a-low-63-over-64":
            return tuple(low_slabs)
        return (reset_depths(right),)
    raise AssertionError(sector)


def q_conditional_entropy_upper(
    data: ExactData, box: Box, q_constant: int
) -> F:
    spec = data.spec
    if "Q" in spec.free_labels:
        q_axis = spec.free_labels.index("Q")
        conditional = compact_q_tail_parameter_upper(
            box.bounds[q_axis][0], q_constant
        )
    else:
        fixed_q = dict(spec.fixed_labels).get("Q", F(0))
        conditional = F(1, 1) / (fixed_q + q_constant + 2)
    return entropy_bounds((conditional, 1 - conditional))[1]


def retained_side_entropy_upper(data: ExactData, box: Box) -> F:
    candidates = []
    for group, branches, q_constant in zip(
        box.side_groups, data.branch_sets, data.q_constants
    ):
        branch_set = set(branches)
        if branch_set == {"h", "m"}:
            low, high = rational_range_common(
                group[0], box.side_denominator, box.bounds
            )
            candidates.append(binary_interval_entropy_upper(low, high))
            continue
        if branch_set == {"h", "c"}:
            low, high = rational_range_common(
                group[0], box.side_denominator, box.bounds
            )
            binary_part = binary_interval_entropy_upper(low, high)
            tail = add_dense_controls(group[1], group[2], box.side_denominator)
            _, tail_high = rational_range_common(
                tail, box.side_denominator, box.bounds
            )
            candidates.append(
                binary_part
                + tail_high * q_conditional_entropy_upper(data, box, q_constant)
            )
            continue
        intervals = tuple(
            rational_range_common(value, box.side_denominator, box.bounds)
            for value in group
        )
        candidates.append(min(
            sum(component_entropy_upper(low, high) for low, high in intervals),
            log_bounds(F(3))[1],
        ))
    return min(candidates)


def assess_box(data: ExactData, box: Box) -> Assessment:
    ranges = tuple(
        rational_range_common(value, box.gram_denominator, box.bounds)
        for value in box.gram_numerators
    )
    floor = max(low for low, _ in ranges)
    active_indices = tuple(
        index for index, (_, high) in enumerate(ranges) if high >= floor
    )
    active = tuple(box.gram_numerators[index] for index in active_indices)
    t_upper = max(ranges[index][1] for index in active_indices)
    side_upper = None
    margin = None
    if F(0) <= t_upper < F(1):
        side_upper = retained_side_entropy_upper(data, box)
        margin = entropy_bounds(isotropic_probabilities(t_upper))[0] - 2 * side_upper
    return Assessment(floor, t_upper, side_upper, margin, len(active), active)


def pruned_box(box: Box, assessment: Assessment) -> Box:
    return replace(box, gram_numerators=assessment.active_numerators)


def validate_initial_coverage(data: ExactData, boxes: tuple[Box, ...]) -> None:
    sector = data.spec.initial_sector
    first_axis = sorted((box.bounds[0] for box in boxes)) if boxes else []
    if sector == "a-low-63-over-64":
        if first_axis[0][0] != 0 or first_axis[-1][1] != F(63, 64):
            raise AssertionError((sector, first_axis))
        for left, right in zip(first_axis, first_axis[1:]):
            if left[1] != right[0]:
                raise AssertionError(("sector gap", left, right))
    elif sector == "a-high-63-over-64":
        if first_axis != [(F(63, 64), F(1))]:
            raise AssertionError((sector, first_axis))
    elif sector in ("a-right-half", "q-right-half"):
        if first_axis != [(F(1, 2), F(1))]:
            raise AssertionError((sector, first_axis))
    elif sector == "full":
        if data.spec.nvar and first_axis != [(F(0), F(1))]:
            raise AssertionError((sector, first_axis))


def print_assessment(prefix: str, box: Box, assessment: Assessment) -> None:
    margin = "none" if assessment.margin is None else f"{float(assessment.margin):.6e}"
    print(
        f"{prefix}: bounds={box.bounds}; active={assessment.active_count}/"
        f"{len(box.gram_numerators)}; t=[{float(assessment.t_lower):.6f},"
        f"{float(assessment.t_upper):.6f}]; margin={margin}",
        flush=True,
    )


def smoke_test(data: ExactData, split_count: int) -> None:
    boxes = initial_boxes(data)
    validate_initial_coverage(data, boxes)
    print(
        f"{data.spec.name}: exact reconstruction complete; nvar={data.spec.nvar}; "
        f"patterns={len(data.patterns)}; gram_degrees={data.gram_degrees}; "
        f"side_degrees={data.side_degrees}; initial_boxes={len(boxes)}",
        flush=True,
    )
    queue = []
    for index, box in enumerate(boxes):
        assessment = assess_box(data, box)
        print_assessment(f"initial[{index}]", box, assessment)
        queue.append(pruned_box(box, assessment))
    for step in range(split_count):
        if not queue:
            break
        box = queue.pop(0)
        axis = step % data.spec.nvar
        left, right = split_box(data, box, axis)
        for side, child in enumerate((left, right)):
            assessment = assess_box(data, child)
            print_assessment(f"smoke[{step}].child[{side}]", child, assessment)
            queue.append(pruned_box(child, assessment))


def run_certificate(data: ExactData, max_boxes: int, max_depth: int) -> None:
    """Full exact loop; callers must opt in explicitly."""
    stack = list(initial_boxes(data))
    processed = 0
    certified = 0
    smallest_margin = None
    while stack:
        if max_boxes and processed >= max_boxes:
            raise RuntimeError(("box budget exhausted", data.spec.name, processed, len(stack)))
        box = stack.pop()
        processed += 1
        assessment = assess_box(data, box)
        if assessment.margin is not None and assessment.margin > 0:
            certified += 1
            if smallest_margin is None or assessment.margin < smallest_margin:
                smallest_margin = assessment.margin
            continue
        box = pruned_box(box, assessment)
        available = [
            axis for axis, depth in enumerate(box.depths) if depth < max_depth
        ]
        if not available:
            raise AssertionError((
                "uncertified maximum-depth box", data.spec.name, box.bounds,
                float(assessment.t_upper),
                None if assessment.margin is None else float(assessment.margin),
            ))
        # Exact trial splits; score first by immediately certified children and
        # then by the larger child margin.  The heuristic affects speed only.
        choices = []
        for axis in available:
            children = split_box(data, box, axis)
            child_assessments = tuple(assess_box(data, child) for child in children)
            certified_children = sum(
                item.margin is not None and item.margin > 0
                for item in child_assessments
            )
            worst_margin = min(
                item.margin if item.margin is not None else F(-10**6)
                for item in child_assessments
            )
            choices.append((certified_children, worst_margin, -axis, children, child_assessments))
        _, _, _, children, child_assessments = max(choices, key=lambda item: item[:3])
        for child, child_assessment in zip(children, child_assessments):
            if child_assessment.margin is not None and child_assessment.margin > 0:
                certified += 1
                if smallest_margin is None or child_assessment.margin < smallest_margin:
                    smallest_margin = child_assessment.margin
            else:
                stack.append(pruned_box(child, child_assessment))
        if processed % 1000 == 0:
            print(
                f"{data.spec.name}: processed={processed}; certified={certified}; "
                f"pending={len(stack)}",
                flush=True,
            )
    print(
        f"{data.spec.name}: certificate complete; processed={processed}; "
        f"certified={certified}; smallest_margin={float(smallest_margin):.12e}",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sector", choices=tuple(SPECS) + ("all-smoke",))
    parser.add_argument("--smoke-splits", type=int, default=0)
    parser.add_argument("--certificate", action="store_true")
    parser.add_argument("--max-boxes", type=int, default=0)
    parser.add_argument("--max-depth", type=int, default=8)
    arguments = parser.parse_args()
    if arguments.certificate and arguments.sector == "all-smoke":
        parser.error("--certificate requires one explicit sector")
    names = tuple(SPECS) if arguments.sector == "all-smoke" else (arguments.sector,)
    for name in names:
        data = reconstruct_exact_data(SPECS[name])
        if arguments.certificate:
            run_certificate(data, arguments.max_boxes, arguments.max_depth)
        else:
            smoke_test(data, arguments.smoke_splits)


if __name__ == "__main__":
    main()
