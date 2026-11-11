#!/usr/bin/env python3
"""Check the retained quotient SAT model, its orbit minimum, and negative controls.

This checker is deliberately independent of the quotient builder. It checks every
DIMACS clause, links every primary time bit to the decoded schedule, recomputes all
1,235,520 lex-recurrence values, enumerates the complete 144-image translation/CSS
schedule orbit with stabilizers, and constructs corrupt/truncated controls.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json


L, M, G = 12, 6, 72


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def add(g, delta):
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def neg(g):
    i, j = divmod(int(g), M)
    return ((-i) % L) * M + ((-j) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def dq(q):
    q = int(q)
    return G + neg(q) if q < G else neg(q - G)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def de(edge):
    kind, check, qubit = edge.split(":")
    assert kind in ("X", "Z")
    return f"{'Z' if kind == 'X' else 'X'}:{neg(int(check))}:{dq(int(qubit))}"


def ge(edge, epsilon, delta):
    return te(de(edge), delta) if epsilon else te(edge, delta)


def recurrence(x, y, suffix):
    return ((not x) and y) or ((x == y) and suffix)


def parse_assignment(path, expected):
    literals = []
    for line in Path(path).read_text().splitlines():
        if not line.startswith("v "):
            continue
        literals.extend(value for value in map(int, line[2:].split()) if value)
    assert len(literals) == expected
    assert {abs(value) for value in literals} == set(range(1, expected + 1))
    values = bytearray(expected + 1)
    for value in literals:
        values[abs(value)] = value > 0
    return literals, values


def schedule_vector(times, edges):
    # Lex order in the CNF is edge-name order and then ten-bit MSB to LSB.
    return tuple(int(times[edge]) for edge in edges)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--assignment", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--trace", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    metadata = json.loads(args.metadata.read_text())
    source = load(args.source)
    candidate = json.loads(args.candidate.read_text())
    trace = load(args.trace)
    expected_variables = int(metadata["variables"])
    expected_clauses = int(metadata["clauses"])
    literals, values = parse_assignment(args.assignment, expected_variables)

    # Positive control: the complete retained model satisfies every clause.
    checked = 0
    first_failed_after_constant_flip = None
    with args.cnf.open() as handle:
        for line in handle:
            if not line.strip() or line.startswith("c"):
                continue
            if line.startswith("p "):
                fields = line.split()
                assert fields[:2] == ["p", "cnf"]
                assert tuple(map(int, fields[2:])) == (expected_variables, expected_clauses)
                continue
            clause = list(map(int, line.split()))
            assert clause and clause[-1] == 0 and all(clause[:-1])
            clause = clause[:-1]
            checked += 1
            assert any(bool(values[abs(lit)]) == (lit > 0) for lit in clause), checked
            if first_failed_after_constant_flip is None:
                def corrupt_value(variable):
                    observed = bool(values[variable])
                    return not observed if variable == int(metadata["constant_variable"]) else observed
                if not any(corrupt_value(abs(lit)) == (lit > 0) for lit in clause):
                    first_failed_after_constant_flip = checked
    assert checked == expected_clauses
    assert first_failed_after_constant_flip is not None

    # Truncation control is rejected before clause evaluation: exactly one variable
    # is absent and the completeness/domain invariant fails.
    truncated = literals[:-1]
    truncation_missing = sorted(set(range(1, expected_variables + 1)) -
                                {abs(value) for value in truncated})
    assert len(truncated) == expected_variables - 1
    assert truncation_missing == [abs(literals[-1])]

    edges = sorted(source["edges"])
    assert len(edges) == len(set(edges)) == 864
    # The quotient acts on the raw bounded primary words.  Rank compression is a
    # strictly increasing relabeling and is checked elsewhere for schedule replay.
    times = {str(edge): int(value) for edge, value in candidate["raw_times"].items()}
    assert set(times) == set(edges)
    assert all(0 <= value < 864 for value in times.values())
    assert canonical_sha(times) == candidate["raw_schedule_sha256"]

    # Link every primary variable to the decoded schedule.
    primary_bit_checks = 0
    for edge in edges:
        observed = 0
        for bit, variable in enumerate(metadata["time_bit_variables"][edge]):
            observed |= int(bool(values[int(variable)])) << bit
            primary_bit_checks += 1
        assert observed == times[edge]

    # Enumerate the finite group orbit and prove that this retained model is its
    # least representative.  Collision handling is explicit through the image map.
    deltas = [(i, j) for i in range(L) for j in range(M)]
    elements = [(epsilon, delta) for epsilon in (0, 1) for delta in deltas]
    nonidentity = [(epsilon, delta) for epsilon, delta in elements
                   if not (epsilon == 0 and delta == (0, 0))]
    images = []
    for epsilon, delta in elements:
        transformed = {ge(edge, epsilon, delta): value for edge, value in times.items()}
        mapping = {edge: ge(edge, epsilon, delta) for edge in edges}
        images.append({"epsilon": epsilon, "delta": delta, "times": transformed,
                       "vector": schedule_vector(transformed, edges),
                       "sha256": canonical_sha(transformed),
                       "edge_map_sha256": canonical_sha(mapping)})
    image_by_element = {(row["epsilon"], tuple(row["delta"])): row for row in images}
    assert len(image_by_element) == 144
    assert len({row["edge_map_sha256"] for row in images}) == 144
    base_vector = schedule_vector(times, edges)
    least_vector = min(row["vector"] for row in images)
    assert base_vector == least_vector
    stabilizer = [row for row in images if row["vector"] == base_vector]
    distinct_images = {row["vector"] for row in images}
    assert len(distinct_images) * len(stabilizer) == len(elements)
    ordered_distinct = sorted(distinct_images)

    # All quotient auxiliaries have the uniquely required recurrence value.
    trace_rows = trace["rows"]
    assert len(trace_rows) == metadata["symmetry_nonidentity_roots"] == 143
    assert [(int(r["epsilon"]), tuple(r["delta"])) for r in trace_rows] == nonidentity
    recurrence_checks = 0
    root_checks = 0
    strict_roots = 0
    edge_map_hash_checks = 0
    for row in trace_rows:
        epsilon, delta = int(row["epsilon"]), tuple(row["delta"])
        image = image_by_element[(epsilon, delta)]
        assert row["edge_map_sha256"] == image["edge_map_sha256"]
        edge_map_hash_checks += 1
        pairs = []
        for edge in edges:
            mapped = ge(edge, epsilon, delta)
            left_bits = metadata["time_bit_variables"][edge]
            right_bits = metadata["time_bit_variables"][mapped]
            for bit in range(9, -1, -1):
                pairs.append((int(left_bits[bit]), int(right_bits[bit])))
        suffix = bool(values[int(metadata["constant_variable"])])
        current = int(row["first_variable"])
        for xvar, yvar in reversed(pairs):
            required = recurrence(bool(values[xvar]), bool(values[yvar]), suffix)
            assert bool(values[current]) == required
            suffix = required
            current += 1
            recurrence_checks += 1
        assert current - 1 == int(row["last_variable"])
        assert int(row["root_variable"]) == int(row["last_variable"])
        assert suffix and bool(values[int(row["root_variable"])])
        root_checks += 1
        if base_vector != image["vector"]:
            strict_roots += 1

    # A direction-corruption is rejected because the least representative is not
    # also the greatest representative when the orbit is nontrivial.
    assert len(ordered_distinct) > 1
    reversed_lex_direction_rejected = base_vector < ordered_distinct[-1]

    # Missing-root control: the second distinct orbit vector has exactly one smaller
    # image.  Removing the corresponding leader admits it while all other leaders
    # hold, demonstrating that root-clause coverage cannot be silently truncated.
    second_vector = ordered_distinct[1]
    second_row = next(row for row in images if row["vector"] == second_vector)
    second_times = second_row["times"]
    comparisons = []
    for epsilon, delta in nonidentity:
        image = {ge(edge, epsilon, delta): value for edge, value in second_times.items()}
        comparisons.append(((epsilon, delta), second_vector <= schedule_vector(image, edges)))
    failed_roots = [element for element, holds in comparisons if not holds]
    assert len(failed_roots) == len(stabilizer)
    assert all(holds for element, holds in comparisons if element not in failed_roots)

    result = {
        "schema": "circdist-gross-round118-order144-sat-orbit-controls-v1",
        "status": "PASS",
        "positive_model": {
            "variables": expected_variables,
            "assigned_variables": len(literals),
            "clauses": expected_clauses,
            "checked_clauses": checked,
            "all_clauses_satisfied": True,
            "primary_time_bits_checked": primary_bit_checks,
            "recurrence_values_checked": recurrence_checks,
            "root_values_checked": root_checks,
            "edge_map_hashes_checked": edge_map_hash_checks,
            "base_prefix_variables": int(metadata["base_variables"]),
            "base_prefix_clauses": int(metadata["base_clauses"]),
        },
        "orbit": {
            "group_order": len(elements),
            "distinct_schedule_vectors": len(distinct_images),
            "stabilizer_size": len(stabilizer),
            "orbit_stabilizer_product": len(distinct_images) * len(stabilizer),
            "candidate_is_lexicographically_least": True,
            "strict_nonidentity_roots": strict_roots,
            "candidate_raw_schedule_sha256": candidate["raw_schedule_sha256"],
            "candidate_compressed_schedule_sha256": candidate["compressed_schedule_sha256"],
            "stabilizer_elements": [{"epsilon": row["epsilon"], "delta": list(row["delta"])}
                                    for row in stabilizer],
        },
        "negative_controls": {
            "corrupt_assignment_mutation": {
                "operation": f"flip variable {metadata['constant_variable']}",
                "rejected": True,
                "first_failing_clause": first_failed_after_constant_flip,
            },
            "truncated_assignment": {
                "operation": "omit the last retained assignment literal",
                "rejected_by_complete_domain_check": True,
                "missing_variable": truncation_missing[0],
            },
            "reversed_lex_direction_rejected": reversed_lex_direction_rejected,
            "missing_root_control": {
                "second_orbit_schedule_sha256": second_row["sha256"],
                "failed_root_elements": [{"epsilon": e, "delta": list(d)} for e, d in failed_roots],
                "failed_root_count_equals_stabilizer_size": True,
                "all_other_nonidentity_roots_hold": True,
            },
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
