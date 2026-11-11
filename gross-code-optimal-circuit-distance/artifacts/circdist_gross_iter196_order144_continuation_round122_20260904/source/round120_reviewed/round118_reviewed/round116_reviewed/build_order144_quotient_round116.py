#!/usr/bin/env python3
"""Append exact lex leaders for the 144-element Gross CSS/translation action.

The group elements are T_delta D^epsilon, with delta in Z_12 x Z_6 and
epsilon in {0,1}.  The identity is omitted.  For each remaining element g,
the canonical primary-time vector x is constrained by x <=_lex g.x.  Each
comparison is represented by a unique right-to-left Boolean recurrence.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import shutil
import time
from pathlib import Path

L, M, G = 12, 6, 72


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


def neg(g: int) -> int:
    i, j = divmod(int(g), M)
    return ((-i) % L) * M + ((-j) % M)


def tq(q: int, delta: tuple[int, int]) -> int:
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def dq(q: int) -> int:
    q = int(q)
    return G + neg(q) if q < G else neg(q - G)


def te(edge: str, delta: tuple[int, int]) -> str:
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def de(edge: str) -> str:
    kind, check, qubit = edge.split(":")
    assert kind in ("X", "Z")
    return f"{'Z' if kind == 'X' else 'X'}:{neg(int(check))}:{dq(int(qubit))}"


def ge(edge: str, epsilon: int, delta: tuple[int, int]) -> str:
    return te(de(edge), delta) if epsilon else te(edge, delta)


def recurrence_value(x: bool, y: bool, suffix_le: bool) -> bool:
    return ((not x) and y) or ((x == y) and suffix_le)


def recurrence_clauses(x: int, y: int, suffix: int, out: int):
    for xv, yv, sv in itertools.product((False, True), repeat=3):
        target = recurrence_value(xv, yv, sv)
        yield [-x if xv else x, -y if yv else y,
               -suffix if sv else suffix, out if target else -out]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-cnf", type=Path, required=True)
    ap.add_argument("--base-metadata", type=Path, required=True)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output-cnf", type=Path, required=True)
    ap.add_argument("--output-metadata", type=Path, required=True)
    ap.add_argument("--output-roots", type=Path, required=True)
    ap.add_argument("--output-trace", type=Path, required=True)
    args = ap.parse_args()
    started = time.time()
    source = load(args.source)
    base = json.loads(args.base_metadata.read_text())
    assert sha(args.base_cnf) == base["cnf_sha256"]
    assert sha(args.source) == base["source_file_sha256"]
    assert source["semantic_payload_sha256"] == base["source_semantic_payload_sha256"]
    with args.base_cnf.open("rb") as f:
        header = f.readline().split()
    assert header[:2] == [b"p", b"cnf"]
    base_vars, base_clauses = map(int, header[2:])
    assert [base_vars, base_clauses] == [base["variables"], base["clauses"]]

    edges = sorted(map(str, source["edges"]))
    assert len(edges) == len(set(edges)) == 864
    time_bits = {edge: tuple(map(int, base["time_bit_variables"][edge])) for edge in edges}
    assert all(len(row) == 10 for row in time_bits.values())
    constant_true = int(base["constant_variable"])
    deltas = [(i, j) for i in range(L) for j in range(M)]
    elements = [(epsilon, delta) for epsilon in (0, 1) for delta in deltas
                if not (epsilon == 0 and delta == (0, 0))]
    assert len(elements) == 143

    # Refuse to build unless all 144 actions are distinct concrete permutations.
    action_hashes = set()
    edge_set = set(edges)
    for epsilon in (0, 1):
        for delta in deltas:
            mapping = {edge: ge(edge, epsilon, delta) for edge in edges}
            assert set(mapping.values()) == edge_set
            action_hashes.add(csha(mapping))
    assert len(action_hashes) == 144

    bits_per_vector = len(edges) * 10
    added_vars = len(elements) * bits_per_vector
    added_definition_clauses = added_vars * 8
    added_root_clauses = len(elements)
    final_vars = base_vars + added_vars
    final_clauses = base_clauses + added_definition_clauses + added_root_clauses
    assert final_vars < 1 << 31 and final_clauses < 1 << 63

    args.output_cnf.parent.mkdir(parents=True, exist_ok=True)
    roots, trace_rows = [], []
    next_var, next_clause = base_vars + 1, base_clauses + 1
    with args.output_cnf.open("wb", buffering=8 << 20) as out:
        out.write(f"p cnf {final_vars} {final_clauses}\n".encode())
        with args.base_cnf.open("rb") as inp:
            inp.readline()
            shutil.copyfileobj(inp, out, 8 << 20)
        for epsilon, delta in elements:
            transformed = {edge: ge(edge, epsilon, delta) for edge in edges}
            flat_pairs = []
            for edge in edges:
                mapped = transformed[edge]
                for bit in range(9, -1, -1):
                    flat_pairs.append((time_bits[edge][bit], time_bits[mapped][bit]))
            assert len(flat_pairs) == bits_per_vector
            first_var, definition_first_clause = next_var, next_clause
            suffix = constant_true
            for x, y in reversed(flat_pairs):
                current = next_var
                next_var += 1
                for clause in recurrence_clauses(x, y, suffix, current):
                    out.write((" ".join(map(str, clause)) + " 0\n").encode())
                    next_clause += 1
                suffix = current
            root_clause_id = next_clause
            out.write(f"{suffix} 0\n".encode())
            next_clause += 1
            row = {
                "epsilon": epsilon, "delta": list(delta),
                "group_element": f"T_({delta[0]},{delta[1]})D^{epsilon}",
                "semantic": "raw primary time vector is lexicographically <= its transformed vector",
                "edge_order": "UTF-8 lexical order of canonical edge names",
                "time_bit_order": "MSB 9 through LSB 0",
                "recurrence": "le_i = (not x_i and y_i) or (x_i == y_i and le_(i+1))",
                "base_case": "le_n = true",
                "definition_first_variable": first_var,
                "definition_last_variable": next_var - 1,
                "definition_first_clause": definition_first_clause,
                "definition_last_clause": root_clause_id - 1,
                "root_variable": suffix, "root_clause_id": root_clause_id,
            }
            roots.append(row)
            trace_rows.append({
                "epsilon": epsilon, "delta": list(delta),
                "edge_map_sha256": csha(transformed),
                "first_variable": first_var, "last_variable": next_var - 1,
                "root_variable": suffix,
            })
    assert next_var == final_vars + 1 and next_clause == final_clauses + 1

    with args.output_roots.open("w", encoding="utf-8", newline="\n") as f:
        for index, row in enumerate(roots):
            f.write(json.dumps({"assertion_index": index, **row}, sort_keys=True,
                               separators=(",", ":")) + "\n")
    trace = {
        "schema": "circdist-gross-round116-order144-lex-leader-trace-v1",
        "group": {"name": "(Z_12 x Z_6) semidirect C_2", "order": 144,
                  "presentation": "D^2=1; D T_delta D = T_-delta", "nonidentity": 143},
        "element_order": "epsilon=0 then 1; delta lexicographic; identity omitted",
        "edge_action": "T_delta D^epsilon, applied right-to-left",
        "edge_order": edges, "bits_per_time": 10,
        "bits_per_vector": bits_per_vector, "base_constant_true": constant_true,
        "recurrence_truth_table_clauses_per_bit": 8,
        "distinct_concrete_edge_permutations": len(action_hashes), "rows": trace_rows,
        "finite_orbit_theorem": "Every finite group orbit has at least one least schedule vector; each least vector satisfies all 143 non-strict lex leaders. Stabilizers are permitted and require no freeness assumption.",
    }
    args.output_trace.write_bytes(gzip.compress(
        (json.dumps(trace, sort_keys=True, separators=(",", ":")) + "\n").encode(),
        compresslevel=9, mtime=0))
    meta = dict(base)
    meta.update({
        "schema": "circdist-gross-round116-order144-quotient-cnf-v1", "status": "PASS",
        "base_cnf_sha256": base["cnf_sha256"], "base_variables": base_vars,
        "base_clauses": base_clauses, "variables": final_vars, "clauses": final_clauses,
        "assertions": int(base["assertions"]) + added_root_clauses,
        "symmetry_group": "(Z_12 x Z_6) semidirect C_2",
        "symmetry_group_order": 144, "symmetry_nonidentity_roots": 143,
        "symmetry_bits_per_vector": bits_per_vector,
        "symmetry_added_variables": added_vars,
        "symmetry_added_definition_clauses": added_definition_clauses,
        "symmetry_added_root_clauses": added_root_clauses,
        "symmetry_roots_sha256": sha(args.output_roots),
        "symmetry_trace_sha256": sha(args.output_trace), "cnf_sha256": sha(args.output_cnf),
        "compile_seconds": round(time.time() - started, 6),
        "equivalence_kind": "base unique definitional extension plus all 143 exact non-strict lex leaders; exact projection onto least schedule vectors of complete order-144 orbits; stabilizers permitted",
        "integer_safety": {"dimacs_variable_limit_signed_32": (1 << 31) - 1,
                           "final_variables": final_vars, "final_clauses": final_clauses,
                           "clause_identifier_limit_signed_64": (1 << 63) - 1},
    })
    args.output_metadata.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "cnf_sha256": meta["cnf_sha256"],
                      "variables": final_vars, "clauses": final_clauses,
                      "roots": len(elements), "seconds": meta["compile_seconds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
