#!/usr/bin/env python3
"""Independent exact checker for the Round102 Gross translation quotient.

The checker reconstructs every appended DIMACS clause without importing the builder,
exhausts the Boolean recurrence truth table, proves the finite translation action on
the concrete Gross geometry, and verifies equivariance of every direct-360 column on
the retained iteration-184 schedule under all 72 translations.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import itertools
import json
import sys
import time


L, M, G, N = 12, 6, 72, 144


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def add(g, delta):
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def sum_delta(left, right):
    return ((left[0] + right[0]) % L, (left[1] + right[1]) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def tmask(value, delta):
    out = 0
    while value:
        bit = value & -value
        q = bit.bit_length() - 1
        out |= 1 << tq(q, delta)
        value ^= bit
    return out


def tcheck_mask(value, delta):
    out = 0
    while value:
        bit = value & -value
        check = bit.bit_length() - 1
        out |= 1 << add(check, delta)
        value ^= bit
    return out


def tname(name, delta):
    parts = name.split(":")
    if parts[0] == "D":
        return f"D:{tq(int(parts[1]), delta)}"
    assert parts[0] == "R" and len(parts) == 3
    return f"R:{add(int(parts[1]), delta)}:{int(parts[2])}"


def recurrence(x, y, suffix):
    return ((not x) and y) or ((x == y) and suffix)


def expected_clauses(x, y, suffix, out):
    rows = []
    for xv, yv, sv in itertools.product((False, True), repeat=3):
        target = recurrence(xv, yv, sv)
        rows.append([
            -x if xv else x,
            -y if yv else y,
            -suffix if sv else suffix,
            out if target else -out,
        ])
    return rows


def parse_clause(line):
    values = list(map(int, line.split()))
    assert values and values[-1] == 0 and all(value != 0 for value in values[:-1])
    return values[:-1]


def clause_holds(clause, values):
    return any(values[abs(lit)] == (lit > 0) for lit in clause)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-cnf", type=Path, required=True)
    ap.add_argument("--base-metadata", type=Path, required=True)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--quotient-cnf", type=Path, required=True)
    ap.add_argument("--quotient-metadata", type=Path, required=True)
    ap.add_argument("--roots", type=Path, required=True)
    ap.add_argument("--trace", type=Path, required=True)
    ap.add_argument("--vendor", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--direct", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    started = time.time()
    source = load(args.source)
    base = json.loads(args.base_metadata.read_text())
    meta = json.loads(args.quotient_metadata.read_text())
    trace = load(args.trace)
    roots = [json.loads(line) for line in args.roots.read_text().splitlines()]
    assert sha(args.base_cnf) == base["cnf_sha256"] == meta["base_cnf_sha256"]
    assert sha(args.quotient_cnf) == meta["cnf_sha256"]
    assert sha(args.roots) == meta["translation_roots_sha256"]
    assert sha(args.trace) == meta["translation_trace_sha256"]
    assert sha(args.source) == base["source_file_sha256"] == meta["source_file_sha256"]

    edges = sorted(source["edges"])
    edge_set = set(edges)
    assert len(edges) == len(edge_set) == 864
    deltas = [(i, j) for i in range(L) for j in range(M)]
    nonidentity = [delta for delta in deltas if delta != (0, 0)]
    assert len(roots) == len(trace["rows"]) == len(nonidentity) == 71
    assert [tuple(row["delta"]) for row in roots] == nonidentity

    # Exhaust the primitive four-variable relation independently.
    truth_table_cases = 0
    for xv, yv, sv, ov in itertools.product((False, True), repeat=4):
        values = {1: xv, 2: yv, 3: sv, 4: ov}
        observed = all(clause_holds(clause, values)
                       for clause in expected_clauses(1, 2, 3, 4))
        assert observed == (ov == recurrence(xv, yv, sv))
        truth_table_cases += 1

    # Exact group action: bijection, identity, composition, and concrete geometry.
    edge_maps = {}
    for delta in deltas:
        mapping = {edge: te(edge, delta) for edge in edges}
        assert set(mapping.values()) == edge_set
        edge_maps[delta] = mapping
    assert all(edge_maps[(0, 0)][edge] == edge for edge in edges)
    composition_edge_cases = 0
    for left in deltas:
        for right in deltas:
            total = sum_delta(left, right)
            for edge in edges:
                assert te(te(edge, left), right) == te(edge, total)
                composition_edge_cases += 1

    xchecks = source["x_checks"]
    zchecks = source["z_checks"]
    geometry_check_cases = 0
    for delta in deltas:
        for check in range(G):
            assert sorted(tq(q, delta) for q in xchecks[check]) == xchecks[add(check, delta)]
            assert sorted(tq(q, delta) for q in zchecks[check]) == zchecks[add(check, delta)]
            geometry_check_cases += 2
        for q in range(N):
            mapped = sorted(te(edge, delta) for edge in source["data_incidence"][q])
            assert mapped == sorted(source["data_incidence"][tq(q, delta)])
            geometry_check_cases += 1
    overlap_set = {(row["x_check"], row["z_check"], tuple(row["qubits"]))
                   for row in source["overlaps"]}
    overlap_cases = 0
    for delta in deltas:
        mapped = {(add(x, delta), add(z, delta), tuple(sorted(tq(q, delta) for q in qs)))
                  for x, z, qs in overlap_set}
        assert mapped == overlap_set
        overlap_cases += len(overlap_set)

    # Stabilizer/detector row spaces are permuted, so zero syndrome and quotient
    # nontriviality are invariant.  Check the concrete row permutations exactly.
    vendor = args.vendor.resolve()
    sys.path[:0] = [str(vendor / "src" / "round63_src"), str(vendor / "src")]
    import model as model
    import round68_build as builder
    assert model.L == L and model.M == M and model.G == G and model.N == N
    hx_set, hz_set = set(model.HX), set(model.HZ)
    row_permutation_cases = 0
    for delta in deltas:
        assert {tmask(row, delta) for row in model.HX} == hx_set
        assert {tmask(row, delta) for row in model.HZ} == hz_set
        row_permutation_cases += len(model.HX) + len(model.HZ)

    # Check the action on all 360 named columns in both sectors for every group
    # element on the retained legal iteration-184 schedule.
    candidate = json.loads(args.candidate.read_text())
    direct = json.loads(args.direct.read_text())
    times = {str(edge): int(value) for edge, value in candidate["compressed_times"].items()}
    assert model.audit_schedule(times, True)["ok"]
    _, _, logical_x, logical_z = builder.load_context()
    original_sectors = builder.sectors(times, logical_x, logical_z)
    direct_column_cases = 0
    direct_witness_cases = 0
    schedule_action_cases = 0
    for delta in deltas:
        translated_times = {te(edge, delta): value for edge, value in times.items()}
        audit = model.audit_schedule(translated_times, True)
        assert audit["ok"] and audit["global_interleaved"]
        assert sorted(translated_times.values()) == sorted(times.values())
        translated_sectors = builder.sectors(translated_times, logical_x, logical_z)
        schedule_action_cases += 1
        for label in ("Xerr", "Zerr"):
            left = original_sectors[label]
            right = translated_sectors[label]
            right_by_name = {column.name: column for column in right.columns}
            assert len(right_by_name) == 360
            for column in left.columns:
                mapped = right_by_name[tname(column.name, delta)]
                assert mapped.kind == column.kind
                assert mapped.residual_kind == column.residual_kind
                assert mapped.support == tmask(column.support, delta)
                assert mapped.physical_support == tmask(column.physical_support, delta)
                assert mapped.syndrome == tcheck_mask(column.syndrome, delta)
                assert tuple(sorted(mapped.u_options)) == tuple(sorted(
                    tcheck_mask(value, delta) for value in column.u_options))
                direct_column_cases += 1
            names = direct["sectors"][label]["mechanism"]["selected_names"]
            translated_names = [tname(name, delta) for name in names]
            replay = model.verify_named_selection(right, translated_names, 10)
            assert replay["ok"] and replay["weight"] == len(names) == 10
            assert replay["syndrome"] == [] and replay["nontrivial"]
            direct_witness_cases += 1

    # Verify the quotient DIMACS is the base body followed by exactly the independently
    # generated recurrence clauses and roots, with no omission or insertion.
    with args.base_cnf.open("r") as base_handle, args.quotient_cnf.open("r") as quotient_handle:
        base_header = base_handle.readline().split()
        quotient_header = quotient_handle.readline().split()
        base_vars, base_clauses = map(int, base_header[2:])
        quotient_vars, quotient_clauses = map(int, quotient_header[2:])
        assert [base_vars, base_clauses] == [base["variables"], base["clauses"]]
        assert [quotient_vars, quotient_clauses] == [meta["variables"], meta["clauses"]]
        prefix_lines = 0
        for base_line in base_handle:
            assert quotient_handle.readline() == base_line
            prefix_lines += 1
        assert prefix_lines == base_clauses
        next_var = base_vars + 1
        appended_lines = 0
        time_bits = {edge: tuple(map(int, base["time_bit_variables"][edge])) for edge in edges}
        constant_true = int(base["constant_variable"])
        for delta, root in zip(nonidentity, roots):
            pairs = []
            for edge in edges:
                mapped = te(edge, delta)
                for bit in range(9, -1, -1):
                    pairs.append((time_bits[edge][bit], time_bits[mapped][bit]))
            suffix = constant_true
            assert root["definition_first_variable"] == next_var
            for x, y in reversed(pairs):
                out = next_var
                next_var += 1
                for expected in expected_clauses(x, y, suffix, out):
                    actual = parse_clause(quotient_handle.readline())
                    assert actual == expected, (delta, appended_lines)
                    appended_lines += 1
                suffix = out
            assert root["root_variable"] == suffix
            assert parse_clause(quotient_handle.readline()) == [suffix]
            appended_lines += 1
        assert quotient_handle.readline() == ""
    assert next_var == quotient_vars + 1
    assert prefix_lines + appended_lines == quotient_clauses
    assert appended_lines == meta["translation_added_definition_clauses"] + meta["translation_added_root_clauses"]

    result = {
        "schema": "circdist-gross-round102-translation-quotient-check-v1",
        "status": "PASS",
        "base_cnf_sha256": sha(args.base_cnf),
        "quotient_cnf_sha256": sha(args.quotient_cnf),
        "group": {"name": "Z_12 x Z_6", "order": 72, "nonidentity": 71},
        "group_action": {
            "edge_bijections_checked": len(deltas),
            "edge_identity_cases": len(edges),
            "edge_composition_cases": composition_edge_cases,
            "geometry_check_and_incidence_cases": geometry_check_cases,
            "overlap_cases": overlap_cases,
            "stabilizer_detector_row_permutation_cases": row_permutation_cases,
            "schedule_action_cases": schedule_action_cases,
            "direct_column_equivariance_cases": direct_column_cases,
            "translated_direct_witness_cases": direct_witness_cases,
        },
        "encoding": {
            "truth_table_cases": truth_table_cases,
            "base_prefix_clauses": prefix_lines,
            "appended_clauses": appended_lines,
            "final_variables": quotient_vars,
            "final_clauses": quotient_clauses,
            "all_appended_clauses_reconstructed": True,
            "unique_extension": True,
        },
        "finite_coverage_theorem": {
            "statement": "For every bounded legal Gross schedule S, the finite orbit {d.S : d in Z_12 x Z_6} has a unique least schedule vector C(S). C(S) satisfies all 71 lex leaders. If multiple group elements attain C(S), they differ by the stabilizer and yield the same schedule vector.",
            "lifting": "A named weight<=10 mechanism on C(S) maps by the inverse translation to a distinct-name mechanism of equal weight, zero syndrome, and nontrivial logical class on S.",
            "root_use": "UNSAT of the checked quotient plus sound base exclusions would prove every legal schedule has a weight<=10 direct mechanism; SAT supplies only a canonical candidate.",
        },
        "integer_and_memory_safety": {
            "final_variables_below_signed_32": quotient_vars < (1 << 31),
            "final_clauses_below_signed_64": quotient_clauses < (1 << 63),
            "streaming_clause_comparison": True,
            "no_product_schedule_enumeration": True,
        },
        "wall_seconds": round(time.time() - started, 6),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "group_action": result["group_action"],
                      "encoding": result["encoding"], "wall_seconds": result["wall_seconds"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
