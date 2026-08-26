"""Exact certificates for the within-tower agreement operator ``M_phi``.

The target class is ``((n-1,1),(n))`` and its scalar cells are

    A_j = (2n-j,j),       B_j = (2n-j-1,j,1),   1 <= j < n.

``BlockEngine(..., variant="zprop")`` is sufficient here because both
multiplicities are one.  It is much cheaper than the fully reconstructed
matrix coefficient and differs from it by one common scalar on this class.

The raw engine gauge is converted to the intrinsic projection gauge
``v_lambda = E_lambda v_0`` by comparing multiplication by ``x=a(n-a)`` with
the independently proved closed matrix in ``mdh_closed_tower``.  The script
then checks the diagonal similarity on every entry before applying it to
``M_phi``.  No interpolation is performed.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from mdh_blocks import BlockEngine
from mdh_closed_tower import cells, closed_x_projection, norm, shape
from mdh_engine import CosetSpace, rref


F = Fraction


def parse_fraction(value):
    return F(value)


def target_vectors(n):
    """Build exact orbit functions in the light scalar-block gauge."""
    cs = CosetSpace(n)
    orbits = cs.orbits()
    orbit_list, _ = orbits
    mu = (n - 1, 1)
    nu = (n,)
    labels = cells(n)
    vectors = []
    for branch, j in labels:
        lam = shape(n, branch, j)
        block, m_y, m_n, _ = BlockEngine(n, lam, cs).orbit_blocks(
            mu, nu, orbits, variant="zprop")
        assert block is not None and (m_y, m_n) == (1, 1)
        vectors.append([entry[0][0] for entry in block])
    orbit_sizes = [len(orbit) for orbit in orbit_list]
    phi_values = [F(cs.phi(sorted(orbit)[0])) for orbit in orbit_list]
    x_values = []
    for orbit in orbit_list:
        representative = sorted(orbit)[0]
        overlap = sum(value < n for value in representative)
        x_values.append(F(overlap * (n - overlap)))
    return labels, vectors, orbit_sizes, x_values, phi_values


def multiplication_matrix(vectors, orbit_sizes, values):
    """Return target-row/source-column multiplication coefficients."""
    norms = [sum(value * value / F(size)
                 for value, size in zip(vector, orbit_sizes))
             for vector in vectors]
    matrix = []
    for target, target_vector in enumerate(vectors):
        row = []
        for source_vector in vectors:
            numerator = sum(
                multiplier * left * right / F(size)
                for multiplier, left, right, size in
                zip(values, target_vector, source_vector, orbit_sizes))
            row.append(numerator / norms[target])
        matrix.append(row)
    return matrix, norms


def projection_scales(n, raw_x):
    """Solve ``raw = diag(s)^-1 projection diag(s)`` exactly."""
    labels, projection_x = closed_x_projection(n)
    count = len(labels)
    scales = [None] * count
    scales[0] = F(1)

    changed = True
    while changed:
        changed = False
        for target in range(count):
            for source in range(count):
                raw = raw_x[target][source]
                closed = projection_x[target][source]
                if not raw or not closed:
                    continue
                if scales[source] is not None and scales[target] is None:
                    scales[target] = scales[source] * closed / raw
                    changed = True
                elif scales[target] is not None and scales[source] is None:
                    scales[source] = scales[target] * raw / closed
                    changed = True
    if any(scale is None for scale in scales):
        missing = [labels[index] for index, scale in enumerate(scales)
                   if scale is None]
        raise AssertionError(f"x graph did not determine scales: {missing}")

    reconstructed = [
        [scales[source] * projection_x[target][source] / scales[target]
         for source in range(count)]
        for target in range(count)
    ]
    assert reconstructed == raw_x
    return scales


def change_to_projection(matrix, scales):
    """Convert a raw multiplication matrix to the projection gauge."""
    return [
        [scales[target] * matrix[target][source] / scales[source]
         for source in range(len(scales))]
        for target in range(len(scales))
    ]


def boundary_values(n):
    """The five low-level reduced elements determining ``M_phi`` for n>=4.

    Matrix entries use target rows and source columns.  These are kept in one
    function because they are the only representation-theoretic input not
    supplied by commutation with ``M_x`` and weighted self-adjointness.
    """
    return {
        (("A", 1), ("A", 1)): F(2 * n - 3, n - 1),
        (("B", 1), ("B", 1)): F(3 * n - 5, 2 * n - 3),
        (("A", 2), ("A", 1)): F(
            2 * n - 1, n * (n - 1) * (2 * n - 3)),
        (("A", 2), ("B", 1)): F((n - 1) ** 2, n * (2 * n - 3)),
        (("B", 1), ("B", 2)): F(
            2 * (n - 1), (2 * n - 3) * (2 * n - 1)),
    }


def closed_phi_projection(n):
    """Reconstruct the full projection-gauge ``M_phi`` recurrence exactly.

    For n>=4 there is a unique matrix which

    * is supported on total-level moves at most one;
    * commutes with the proved closed ``M_x`` matrix;
    * is self-adjoint for the hook weights; and
    * has the five low-level reduced elements in :func:`boundary_values`.

    This is a closed finite recurrence certificate.  It does not use an
    engine table or fitted coefficients.
    """
    if n < 4:
        raise ValueError("the five-boundary reconstruction is unique for n>=4")
    labels, x_matrix = closed_x_projection(n)
    count = len(labels)
    levels = [j + (branch == "B") for branch, j in labels]
    support = [
        (target, source)
        for target in range(count)
        for source in range(count)
        if abs(levels[target] - levels[source]) <= 1
    ]
    variable = {entry: index for index, entry in enumerate(support)}
    equations = []

    def add_equation(terms, right=F(0)):
        row = [F(0)] * (len(support) + 1)
        for entry, coefficient in terms:
            row[variable[entry]] += coefficient
        row[-1] = right
        equations.append(row)

    # X Phi - Phi X = 0.
    for row in range(count):
        for column in range(count):
            terms = []
            for middle in range(count):
                if (middle, column) in variable and x_matrix[row][middle]:
                    terms.append(((middle, column), x_matrix[row][middle]))
                if (row, middle) in variable and x_matrix[middle][column]:
                    terms.append(((row, middle), -x_matrix[middle][column]))
            if terms:
                add_equation(terms)

    # h_target Phi[target,source] = h_source Phi[source,target].
    weights = [norm(n, *label) for label in labels]
    for target in range(count):
        for source in range(target):
            if (target, source) in variable:
                add_equation([
                    ((target, source), weights[target]),
                    ((source, target), -weights[source]),
                ])

    position = {label: index for index, label in enumerate(labels)}
    for (target_label, source_label), value in boundary_values(n).items():
        add_equation([
            ((position[target_label], position[source_label]), F(1))
        ], value)

    reduced, pivots = rref(equations, len(support) + 1)
    if len(support) in pivots:
        raise AssertionError("closed M_phi equations are inconsistent")
    if len(pivots) != len(support):
        raise AssertionError(
            f"closed M_phi equations leave {len(support) - len(pivots)} "
            "free parameters")
    solution = [F(0)] * len(support)
    for row, pivot in enumerate(pivots):
        solution[pivot] = reduced[row][-1]

    matrix = [[F(0)] * count for _ in range(count)]
    for entry, index in variable.items():
        matrix[entry[0]][entry[1]] = solution[index]
    return labels, matrix


def build_certificate(n):
    labels, vectors, sizes, x_values, phi_values = target_vectors(n)
    raw_x, raw_norms = multiplication_matrix(vectors, sizes, x_values)
    raw_phi, _ = multiplication_matrix(vectors, sizes, phi_values)
    scales = projection_scales(n, raw_x)
    projection_phi = change_to_projection(raw_phi, scales)
    return {
        "n": n,
        "labels": [f"{branch}{j}" for branch, j in labels],
        "orbit_sizes": sizes,
        "x_values": [str(value) for value in x_values],
        "phi_values": [str(value) for value in phi_values],
        "vectors": [[str(value) for value in vector] for vector in vectors],
        "raw_norms": [str(value) for value in raw_norms],
        "projection_scales": [str(value) for value in scales],
        "projection_phi": [
            [str(value) for value in row] for row in projection_phi
        ],
    }


def load_certificate(path):
    with path.open(encoding="utf-8") as stream:
        payload = json.load(stream)
    payload["projection_phi"] = [
        [parse_fraction(value) for value in row]
        for row in payload["projection_phi"]
    ]
    payload["projection_scales"] = [
        parse_fraction(value) for value in payload["projection_scales"]
    ]
    return payload


def print_recurrence(payload):
    labels = payload["labels"]
    matrix = payload["projection_phi"]
    if matrix and isinstance(matrix[0][0], str):
        matrix = [[parse_fraction(value) for value in row] for row in matrix]
    print(f"n={payload['n']} projection-gauge M_phi")
    for source, label in enumerate(labels):
        terms = [f"{matrix[target][source]} {labels[target]}"
                 for target in range(len(labels))
                 if matrix[target][source]]
        print(f"  {label} -> " + " + ".join(terms))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?")
    parser.add_argument("--load", type=Path)
    parser.add_argument("--save", type=Path)
    args = parser.parse_args()
    if args.load and args.save:
        parser.error("--load and --save cannot be combined")
    if args.save and args.save.exists():
        parser.error(f"refusing to overwrite {args.save}")
    if args.load:
        payload = load_certificate(args.load)
    else:
        if args.n is None:
            parser.error("provide n or --load")
        payload = build_certificate(args.n)
        if args.save:
            args.save.parent.mkdir(parents=True, exist_ok=True)
            with args.save.open("x", encoding="utf-8") as stream:
                json.dump(payload, stream, indent=2)
                stream.write("\n")
    print_recurrence(payload)


if __name__ == "__main__":
    main()
