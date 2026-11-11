#!/usr/bin/env python3
"""Independent checker for the Round122 iteration-197 order-144 Gross quotient.

This checker does not import the builder.  It reconstructs every appended clause,
exhausts the recurrence relation, verifies all 144 concrete edge permutations and
their generalized-dihedral multiplication law, and binds independently completed
base-encoding and full-registry closure audits.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import time
from pathlib import Path

L, M, G, N = 12, 6, 72, 144


def load(path: Path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def csha(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def add(g: int, delta: tuple[int, int]) -> int:
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def dsum(left, right):
    return ((left[0] + right[0]) % L, (left[1] + right[1]) % M)


def dneg(delta):
    return ((-delta[0]) % L, (-delta[1]) % M)


def neg(g: int) -> int:
    i, j = divmod(int(g), M)
    return ((-i) % L) * M + ((-j) % M)


def tq(q: int, delta) -> int:
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def dq(q: int) -> int:
    q = int(q)
    return G + neg(q) if q < G else neg(q - G)


def te(edge: str, delta) -> str:
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def de(edge: str) -> str:
    kind, check, qubit = edge.split(":")
    return f"{'Z' if kind == 'X' else 'X'}:{neg(int(check))}:{dq(int(qubit))}"


def ge(edge: str, epsilon: int, delta) -> str:
    return te(de(edge), delta) if epsilon else te(edge, delta)


def multiply(left, right):
    """Composition left after right for T_d D^e coordinates."""
    e1, d1 = left
    e2, d2 = right
    return (e1 ^ e2, dsum(d1, dneg(d2) if e1 else d2))


def recurrence(x: bool, y: bool, suffix: bool) -> bool:
    return ((not x) and y) or ((x == y) and suffix)


def expected_clauses(x: int, y: int, suffix: int, out: int):
    rows = []
    for xv, yv, sv in itertools.product((False, True), repeat=3):
        target = recurrence(xv, yv, sv)
        rows.append([-x if xv else x, -y if yv else y,
                     -suffix if sv else suffix, out if target else -out])
    return rows


def parse_clause(line: str):
    values = list(map(int, line.split()))
    assert values and values[-1] == 0 and all(x != 0 for x in values[:-1])
    return values[:-1]


def clause_holds(clause, values):
    return any(values[abs(lit)] == (lit > 0) for lit in clause)


def block_key(block):
    return tuple(sorted((str(a), str(b)) for a, b in block["atoms"]))


def gblock(key, epsilon, delta):
    return tuple(sorted((ge(a, epsilon, delta), ge(b, epsilon, delta)) for a, b in key))


def selector_key(selector):
    groups = tuple(sorted((int(c), tuple(sorted(map(int, kinds))))
                          for c, kinds in selector["group_kinds"].items()))
    return (str(selector["sector"]), tuple(sorted(map(int, selector["data_support"]))), groups)


def gselector(key, epsilon, delta):
    sector, data, groups = key
    if epsilon:
        sector = "Zerr" if sector == "Xerr" else "Xerr"
        data = tuple(dq(q) for q in data)
        groups = tuple((neg(c), kinds) for c, kinds in groups)
    return (sector, tuple(sorted(tq(q, delta) for q in data)),
            tuple(sorted((add(c, delta), kinds) for c, kinds in groups)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-cnf", type=Path, required=True)
    ap.add_argument("--base-metadata", type=Path, required=True)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--quotient-cnf", type=Path, required=True)
    ap.add_argument("--quotient-metadata", type=Path, required=True)
    ap.add_argument("--roots", type=Path, required=True)
    ap.add_argument("--trace", type=Path, required=True)
    ap.add_argument("--base-encoding-check", type=Path, required=True)
    ap.add_argument("--translation-registry-check", type=Path, required=True)
    ap.add_argument("--css-closure-check", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    started = time.time()
    source = load(args.source)
    base = json.loads(args.base_metadata.read_text())
    meta = json.loads(args.quotient_metadata.read_text())
    trace = load(args.trace)
    roots = [json.loads(line) for line in args.roots.read_text().splitlines()]
    base_check = json.loads(args.base_encoding_check.read_text())
    translation_check = json.loads(args.translation_registry_check.read_text())
    css_check = json.loads(args.css_closure_check.read_text())

    assert sha(args.base_cnf) == base["cnf_sha256"] == meta["base_cnf_sha256"]
    assert sha(args.quotient_cnf) == meta["cnf_sha256"]
    assert sha(args.roots) == meta["symmetry_roots_sha256"]
    assert sha(args.trace) == meta["symmetry_trace_sha256"]
    assert sha(args.source) == base["source_file_sha256"] == meta["source_file_sha256"]
    assert base_check["status"] == translation_check["status"] == css_check["status"] == "PASS"
    assert base_check["cnf_sha256"] == sha(args.base_cnf)
    assert translation_check["source_sha256"] == css_check["bindings"]["source_sha256"] == sha(args.source)
    assert translation_check["blocks"]["generator_cases"] == 2 * len(source["blocks"])
    assert translation_check["selectors"]["generator_cases"] == 2 * len(source["selectors"])
    assert css_check["blocks"]["missing_dual_image_count"] == 0
    assert css_check["selectors"]["missing_dual_image_count"] == 0

    edges = sorted(map(str, source["edges"]))
    edge_set = set(edges)
    assert len(edges) == len(edge_set) == 864
    deltas = [(i, j) for i in range(L) for j in range(M)]
    group = [(epsilon, delta) for epsilon in (0, 1) for delta in deltas]
    nonidentity = [element for element in group if element != (0, (0, 0))]
    assert len(group) == 144 and len(nonidentity) == 143
    assert len(roots) == len(trace["rows"]) == 143
    assert [(r["epsilon"], tuple(r["delta"])) for r in roots] == nonidentity

    # Primitive relation, including adversarial single-literal and truncation controls.
    truth_table_cases = 0
    primitive = expected_clauses(1, 2, 3, 4)
    for xv, yv, sv, ov in itertools.product((False, True), repeat=4):
        values = {1: xv, 2: yv, 3: sv, 4: ov}
        observed = all(clause_holds(clause, values) for clause in primitive)
        assert observed == (ov == recurrence(xv, yv, sv))
        truth_table_cases += 1
    corrupted = [list(row) for row in primitive]
    corrupted[0][0] *= -1
    assert any(all(clause_holds(clause, {1: xv, 2: yv, 3: sv, 4: ov}) for clause in corrupted)
               != (ov == recurrence(xv, yv, sv))
               for xv, yv, sv, ov in itertools.product((False, True), repeat=4))
    truncated = primitive[:-1]
    assert any(all(clause_holds(clause, {1: xv, 2: yv, 3: sv, 4: ov}) for clause in truncated)
               != (ov == recurrence(xv, yv, sv))
               for xv, yv, sv, ov in itertools.product((False, True), repeat=4))

    # Concrete faithful group action and exact multiplication law.
    edge_maps, action_hashes = {}, set()
    for element in group:
        epsilon, delta = element
        mapping = {edge: ge(edge, epsilon, delta) for edge in edges}
        assert set(mapping.values()) == edge_set
        edge_maps[element] = mapping
        action_hashes.add(csha(mapping))
    assert len(action_hashes) == 144
    assert all(edge_maps[(0, (0, 0))][edge] == edge for edge in edges)
    composition_cases = 0
    for left in group:
        for right in group:
            product = multiply(left, right)
            for edge in edges:
                assert ge(ge(edge, right[0], right[1]), left[0], left[1]) == \
                       ge(edge, product[0], product[1])
                composition_cases += 1

    # Full action on concrete checks, data incidence, and MC-overlap triples.
    geometry_cases = 0
    overlap_set = {(int(r["x_check"]), int(r["z_check"]), tuple(map(int, r["qubits"])))
                   for r in source["overlaps"]}
    for epsilon, delta in group:
        for c in range(G):
            if epsilon:
                assert sorted(tq(dq(q), delta) for q in source["x_checks"][c]) == \
                       sorted(source["z_checks"][add(neg(c), delta)])
                assert sorted(tq(dq(q), delta) for q in source["z_checks"][c]) == \
                       sorted(source["x_checks"][add(neg(c), delta)])
            else:
                assert sorted(tq(q, delta) for q in source["x_checks"][c]) == \
                       sorted(source["x_checks"][add(c, delta)])
                assert sorted(tq(q, delta) for q in source["z_checks"][c]) == \
                       sorted(source["z_checks"][add(c, delta)])
            geometry_cases += 2
        for q in range(N):
            mapped = sorted(ge(edge, epsilon, delta) for edge in source["data_incidence"][q])
            target = tq(dq(q), delta) if epsilon else tq(q, delta)
            assert mapped == sorted(source["data_incidence"][target])
            geometry_cases += 1
        if epsilon:
            mapped_overlaps = {(add(neg(z), delta), add(neg(x), delta),
                                tuple(sorted(tq(dq(q), delta) for q in qs)))
                               for x, z, qs in overlap_set}
        else:
            mapped_overlaps = {(add(x, delta), add(z, delta),
                                tuple(sorted(tq(q, delta) for q in qs)))
                               for x, z, qs in overlap_set}
        assert mapped_overlaps == overlap_set

    # Independently sample the installed full registry under every group element.
    # Generator closure checks bind every record; here first/last/middle records catch
    # action-convention mismatches while avoiding a redundant 117M-object materialization.
    blocks = source["blocks"]
    block_set = {block_key(b) for b in blocks}
    selectors = source["selectors"]
    selector_set = {selector_key(s) for s in selectors}
    block_indices = sorted({0, 1, len(blocks)//2, len(blocks)-2, len(blocks)-1})
    selector_indices = sorted({0, 1, len(selectors)//2, len(selectors)-2, len(selectors)-1})
    registry_sample_cases = 0
    for epsilon, delta in group:
        for i in block_indices:
            assert gblock(block_key(blocks[i]), epsilon, delta) in block_set
            registry_sample_cases += 1
        for i in selector_indices:
            assert gselector(selector_key(selectors[i]), epsilon, delta) in selector_set
            registry_sample_cases += 1

    # Byte-exact base prefix plus independently reconstructed appended body.
    with args.base_cnf.open("r") as bf, args.quotient_cnf.open("r") as qf:
        bh, qh = bf.readline().split(), qf.readline().split()
        base_vars, base_clauses = map(int, bh[2:])
        quotient_vars, quotient_clauses = map(int, qh[2:])
        assert [base_vars, base_clauses] == [base["variables"], base["clauses"]]
        assert [quotient_vars, quotient_clauses] == [meta["variables"], meta["clauses"]]
        prefix_lines = 0
        for line in bf:
            assert qf.readline() == line
            prefix_lines += 1
        assert prefix_lines == base_clauses
        time_bits = {edge: tuple(map(int, base["time_bit_variables"][edge])) for edge in edges}
        constant_true = int(base["constant_variable"])
        next_var, appended_lines = base_vars + 1, 0
        for (epsilon, delta), root, trace_row in zip(nonidentity, roots, trace["rows"]):
            mapping = edge_maps[(epsilon, delta)]
            assert trace_row["edge_map_sha256"] == csha(mapping)
            pairs = [(time_bits[edge][bit], time_bits[mapping[edge]][bit])
                     for edge in edges for bit in range(9, -1, -1)]
            suffix = constant_true
            assert root["definition_first_variable"] == next_var
            for x, y in reversed(pairs):
                out = next_var
                next_var += 1
                for expected in expected_clauses(x, y, suffix, out):
                    assert parse_clause(qf.readline()) == expected
                    appended_lines += 1
                suffix = out
            assert root["definition_last_variable"] == next_var - 1
            assert root["root_variable"] == suffix == trace_row["root_variable"]
            assert parse_clause(qf.readline()) == [suffix]
            appended_lines += 1
        assert qf.readline() == ""
    assert next_var == quotient_vars + 1
    assert prefix_lines + appended_lines == quotient_clauses
    assert appended_lines == meta["symmetry_added_definition_clauses"] + meta["symmetry_added_root_clauses"]

    result = {
        "schema": "circdist-gross-round122-iter197-order144-quotient-check-v1", "status": "PASS",
        "bindings": {"source_sha256": sha(args.source), "base_cnf_sha256": sha(args.base_cnf),
                     "quotient_cnf_sha256": sha(args.quotient_cnf),
                     "base_encoding_check_sha256": sha(args.base_encoding_check),
                     "translation_registry_check_sha256": sha(args.translation_registry_check),
                     "css_closure_check_sha256": sha(args.css_closure_check)},
        "group": {"name": "(Z_12 x Z_6) semidirect C_2", "order": 144,
                  "nonidentity": 143, "distinct_edge_permutations": len(action_hashes),
                  "edge_identity_cases": len(edges), "edge_composition_cases": composition_cases,
                  "geometry_and_incidence_cases": geometry_cases,
                  "overlap_sets_checked": len(group), "registry_action_sample_cases": registry_sample_cases},
        "registry_closure": {"blocks": len(block_set), "selectors": len(selector_set),
                             "full_translation_generator_audit_bound": True,
                             "full_css_involution_audit_bound": True,
                             "therefore_full_order144_action_closed": True},
        "encoding": {"truth_table_cases": truth_table_cases,
                     "corrupt_primitive_rejected": True, "truncated_primitive_rejected": True,
                     "base_prefix_clauses": prefix_lines, "appended_clauses": appended_lines,
                     "final_variables": quotient_vars, "final_clauses": quotient_clauses,
                     "all_appended_clauses_reconstructed": True, "unique_extension": True},
        "equisatisfiability_theorem": {
            "hypotheses": "The checked base semantics are invariant under every group generator: concrete Gross geometry under translations and D; order-block and selector registries are closed under both generators; the compiled base CNF exactly represents those semantics.",
            "forward": "A quotient model projects to a base model because the base CNF is a byte-exact prefix.",
            "reverse": "For any base schedule S, choose a lexicographically least time vector in its finite 144-image orbit. Invariance makes it a base schedule. It is <= every group image and the exact recurrence has one satisfying extension for each of the 143 comparisons.",
            "stabilizers": "Non-strict <= permits equal images. No freeness or orbit-size-144 assumption is used.",
            "conclusion": "The order-144 quotient is satisfiable iff the full iteration-197 base family is satisfiable. A future proof-producing UNSAT result therefore covers the full frozen iteration-197 family encoded by the base, subject to the soundness scope of its exclusion registries."
        },
        "integer_safety": {"variables_below_signed_32": quotient_vars < 1 << 31,
                           "clauses_below_signed_64": quotient_clauses < 1 << 63,
                           "streaming_clause_comparison": True},
        "wall_seconds": round(time.time() - started, 6),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "group": result["group"],
                      "encoding": result["encoding"], "wall_seconds": result["wall_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
