#!/usr/bin/env python3
"""Vectorized formula scan for the two triangular three-face SU(3) clusters.

This is a candidate filter, not a proof.  It evaluates the complete union-incidence Gram formula
and every block-highest side output for random simplex weights.
"""

from __future__ import annotations

from itertools import combinations

import numpy as np

from certify_su3_all_elementary_cycles import (
    cross_numerator,
    cycle_t,
    dimension,
    environment_barycenter,
)
from scan_su3_adjacent_elementary_faces import adjacent_t


ENVIRONMENT_OFFSETS = ((0, 0), (2, -1), (1, -2))
INPUT_OFFSETS = ((1, 0), (2, -2), (0, -1))
FACE_EDGES = (
    (0, 0, "h"), (0, 2, "c"),
    (1, 0, "m"), (1, 1, "c"),
    (2, 1, "h"), (2, 2, "m"),
)
TRIANGLES = (
    ((-2, 1), (-1, -1), (0, 0)),
    ((-2, 1), (-1, 2), (0, 0)),
)
SAMPLES = 120_000
SEED = 20260830


def add(first, second):
    return first[0] + second[0], first[1] + second[1]


def build_union(cluster):
    environments = sorted(
        {add(base, offset) for base in cluster for offset in ENVIRONMENT_OFFSETS}
    )
    inputs = sorted({add(base, offset) for base in cluster for offset in INPUT_OFFSETS})
    environment_index = {label: index for index, label in enumerate(environments)}
    input_index = {label: index for index, label in enumerate(inputs)}
    edges = sorted(
        {
            (
                input_index[add(base, INPUT_OFFSETS[input_slot])],
                environment_index[add(base, ENVIRONMENT_OFFSETS[environment_slot])],
                branch,
            )
            for base in cluster
            for environment_slot, input_slot, branch in FACE_EDGES
        }
    )
    incidences = [[] for _ in inputs]
    attached = [[] for _ in environments]
    for input_index_value, environment_index_value, branch in edges:
        incidences[input_index_value].append((environment_index_value, branch))
        attached[environment_index_value].append((input_index_value, branch))
    return environments, inputs, incidences, attached


def minimum_base(environments, inputs):
    all_labels = environments + inputs
    return -min(label[0] for label in all_labels), -min(label[1] for label in all_labels)


def side_rows(r, s, branches):
    rows = {
        "h": np.array((1.0, 0.0, 0.0)),
        "m": np.array((1 / (r + 2), (r + 1) / (r + 2), 0.0)),
        "c": np.array(
            (
                1 / (r + s + 3),
                (r + s + 2) / ((s + 2) * (r + s + 3)),
                (s + 1) * (r + s + 2) / ((s + 2) * (r + s + 3)),
            )
        ),
    }
    return np.stack([rows[branch] for branch in branches])


def entropy(probabilities):
    safe = np.where(probabilities > 0, probabilities, 1.0)
    return -np.sum(np.where(probabilities > 0, probabilities * np.log2(safe), 0.0), axis=-1)


def random_weights(rng, incidences, samples):
    result = []
    for incidence in incidences:
        degree = len(incidence)
        first_count = samples // 2
        ordinary = rng.gamma(1.0, 1.0, size=(first_count, degree))
        corner = rng.gamma(0.15, 1.0, size=(samples - first_count, degree))
        values = np.concatenate((ordinary, corner), axis=0)
        values /= np.sum(values, axis=1, keepdims=True)
        result.append(values)
    return result


def weights_from_branch_maps(incidences, branch_maps):
    return [
        np.array([[branch_maps[input_index][branch] for _, branch in incidence]])
        for input_index, incidence in enumerate(incidences)
    ]


def evaluate(base_p, base_q, environments, inputs, incidences, attached, weights):
    sample_count = weights[0].shape[0]
    numerator = np.zeros(sample_count)
    side_entropies = []
    total_dimension = 0.0
    branch_positions = []
    for input_offset, incidence, block_weights in zip(inputs, incidences, weights):
        input_label = add((base_p, base_q), input_offset)
        input_dimension = float(dimension(*input_label))
        total_dimension += input_dimension
        center = environment_barycenter(*input_label)
        branches = [branch for _, branch in incidence]
        branch_positions.append({branch: index for index, branch in enumerate(branches)})
        local_t = -np.ones(sample_count)
        for index, branch in enumerate(branches):
            local_t += block_weights[:, index] ** 2 / float(center[branch])
        numerator += input_dimension * local_t / 8
        distribution = block_weights @ side_rows(*input_label, branches)
        side_entropies.append(entropy(distribution))
    for environment_offset, environment_attached in zip(environments, attached):
        environment_label = add((base_p, base_q), environment_offset)
        for first, second in combinations(environment_attached, 2):
            first_input, first_branch = first
            second_input, second_branch = second
            numerator += (
                weights[first_input][:, branch_positions[first_input][first_branch]]
                * weights[second_input][:, branch_positions[second_input][second_branch]]
                * float(cross_numerator(
                    *environment_label, first_branch, second_branch
                ))
            )
    gram_t = numerator / total_dimension
    if np.min(gram_t) < -1e-10 or np.max(gram_t) > 1 + 1e-10:
        raise AssertionError((base_p, base_q, float(np.min(gram_t)), float(np.max(gram_t))))
    gram_t = np.clip(gram_t, 0.0, 1.0)
    exceptional = (1 + 8 * gram_t) / 9
    repeated = (1 - gram_t) / 9
    bell = entropy(np.stack((exceptional, repeated, repeated, repeated, repeated,
                             repeated, repeated, repeated, repeated), axis=-1))
    side_matrix = np.stack(side_entropies)
    side = np.min(side_matrix, axis=0)
    return bell - 2 * side, gram_t, side, bell, side_matrix


def audit_against_existing_formulas():
    # One elementary face.
    environments, inputs, incidences, attached = build_union(((0, 0),))
    maps_by_offset = {
        (1, 0): {"h": 0.37, "m": 0.63},
        (2, -2): {"h": 0.59, "c": 0.41},
        (0, -1): {"m": 0.23, "c": 0.77},
    }
    weights = weights_from_branch_maps(
        incidences, [maps_by_offset[offset] for offset in inputs]
    )
    _, gram_t, _, _, _ = evaluate(3, 5, environments, inputs, incidences, attached, weights)
    expected = float(cycle_t(3, 5, 0.37, 0.41, 0.23))
    if abs(float(gram_t[0]) - expected) > 1e-12:
        raise AssertionError((float(gram_t[0]), expected))

    # The canonical middle-edge adjacent pair after its exact endpoint reduction.
    environments, inputs, incidences, attached = build_union(((0, 0), (1, 1)))
    pattern = ("m", 1, 0)
    retained_u, retained_v = 0.29, 0.71
    maps_by_offset = {
        (1, 0): {"h": 0.0, "m": 1.0, "c": 0.0},
        (2, -2): {"c": 1.0, "h": 0.0},
        (0, -1): {"m": 0.0, "c": 1.0},
        (2, 1): {"h": retained_u, "m": 1 - retained_u},
        (3, -1): {"c": retained_v, "h": 1 - retained_v},
    }
    weights = weights_from_branch_maps(
        incidences, [maps_by_offset[offset] for offset in inputs]
    )
    _, gram_t, _, _, _ = evaluate(4, 6, environments, inputs, incidences, attached, weights)
    expected = float(adjacent_t(4, 6, pattern, retained_u, retained_v))
    if abs(float(gram_t[0]) - expected) > 1e-12:
        raise AssertionError((float(gram_t[0]), expected))


def main():
    audit_against_existing_formulas()
    print("formula audit: single-face and canonical two-face matches", flush=True)
    rng = np.random.default_rng(SEED)
    offsets = (0, 1, 2, 4, 8, 16, 32)
    global_best = None
    for triangle in TRIANGLES:
        environments, inputs, incidences, attached = build_union(triangle)
        p_min, q_min = minimum_base(environments, inputs)
        weights = random_weights(rng, incidences, SAMPLES)
        triangle_best = None
        subset_worst = {
            subset: float("inf")
            for size in range(1, min(4, len(inputs)) + 1)
            for subset in combinations(range(len(inputs)), size)
        }
        for p_offset in offsets:
            for q_offset in offsets:
                base_p, base_q = p_min + p_offset, q_min + q_offset
                margin, gram_t, side, bell, side_matrix = evaluate(
                    base_p, base_q, environments, inputs, incidences, attached, weights
                )
                for subset in subset_worst:
                    subset_worst[subset] = min(
                        subset_worst[subset],
                        float(np.min(bell - 2 * np.min(side_matrix[list(subset)], axis=0))),
                    )
                index = int(np.argmin(margin))
                record = (
                    float(margin[index]), triangle, base_p, base_q,
                    float(gram_t[index]), float(side[index]),
                    tuple(tuple(float(value) for value in block[index]) for block in weights),
                )
                if triangle_best is None or record[0] < triangle_best[0]:
                    triangle_best = record
                if global_best is None or record[0] < global_best[0]:
                    global_best = record
        print(f"triangle {triangle}: I={len(inputs)}, E={len(environments)}, samples/base={SAMPLES}")
        print(f"  input offsets/degrees: {[(offset, len(incidence)) for offset, incidence in zip(inputs, incidences)]}")
        print(f"  smallest sampled Bell-minus-twice-side margin: {triangle_best}")
        for size in range(1, min(4, len(inputs)) + 1):
            candidates = [subset for subset in subset_worst if len(subset) == size]
            best_subset = max(candidates, key=subset_worst.get)
            print(
                f"  best fixed side {size}-cover: {tuple(inputs[index] for index in best_subset)} "
                f"with sampled worst margin {subset_worst[best_subset]:.12f} bit"
            )
    print(f"global smallest sampled margin: {global_best}")
    if global_best[0] < 0:
        print("candidate survives explicit block-highest side filter; global S_min still required")
    else:
        print("no triangular-cluster Bell candidate found by this formula scan")


if __name__ == "__main__":
    main()
