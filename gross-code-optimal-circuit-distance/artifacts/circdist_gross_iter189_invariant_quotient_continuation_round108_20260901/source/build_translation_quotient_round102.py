#!/usr/bin/env python3
"""Append an exact Z_12 x Z_6 lex-leader quotient to a Gross outer DIMACS CNF.

For each nonidentity translation d, the primary time vector x is constrained by
    x <=_lex d.x
where edges are sorted by their canonical names and each ten-bit time is read MSB
first.  One recurrence variable per bit gives a unique extension of every base
assignment.  The construction is a quotient of schedule translations only; all
base order blocks and exact selectors are retained byte-for-byte.
"""
from pathlib import Path
import argparse
import datetime
import gzip
import hashlib
import itertools
import json
import os
import shutil
import time


L, M, G = 12, 6, 72


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


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def recurrence_value(x, y, suffix_le):
    return ((not x) and y) or ((x == y) and suffix_le)


def recurrence_clauses(x, y, suffix, out):
    """Truth-table CNF for out <-> (x<y or (x=y and suffix))."""
    clauses = []
    for xv, yv, sv in itertools.product((False, True), repeat=3):
        target = recurrence_value(xv, yv, sv)
        clauses.append([
            -x if xv else x,
            -y if yv else y,
            -suffix if sv else suffix,
            out if target else -out,
        ])
    return clauses


def main():
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

    with args.base_cnf.open("rb") as handle:
        header = handle.readline().split()
    assert header[:2] == [b"p", b"cnf"]
    base_vars, base_clauses = map(int, header[2:])
    assert (base_vars, base_clauses) == (base["variables"], base["clauses"])

    edges = sorted(source["edges"])
    assert len(edges) == len(set(edges)) == 864
    time_bits = {edge: tuple(map(int, base["time_bit_variables"][edge])) for edge in edges}
    assert all(len(bits) == 10 for bits in time_bits.values())
    constant_true = int(base["constant_variable"])
    deltas = [(i, j) for i in range(L) for j in range(M) if (i, j) != (0, 0)]
    bits_per_vector = len(edges) * 10
    added_vars = len(deltas) * bits_per_vector
    added_definition_clauses = added_vars * 8
    added_root_clauses = len(deltas)
    final_vars = base_vars + added_vars
    final_clauses = base_clauses + added_definition_clauses + added_root_clauses
    assert final_vars < (1 << 31)
    assert final_clauses < (1 << 63)

    args.output_cnf.parent.mkdir(parents=True, exist_ok=True)
    roots = []
    trace_rows = []
    next_var = base_vars + 1
    next_clause = base_clauses + 1
    with args.output_cnf.open("wb", buffering=1 << 20) as out:
        out.write(f"p cnf {final_vars} {final_clauses}\n".encode())
        with args.base_cnf.open("rb") as inp:
            inp.readline()
            shutil.copyfileobj(inp, out, 1 << 20)
        for delta in deltas:
            transformed = {edge: te(edge, delta) for edge in edges}
            assert set(transformed.values()) == set(edges)
            flat_pairs = []
            for edge in edges:
                mapped = transformed[edge]
                for bit in range(9, -1, -1):
                    flat_pairs.append((time_bits[edge][bit], time_bits[mapped][bit]))
            assert len(flat_pairs) == bits_per_vector
            first_var = next_var
            suffix = constant_true
            definition_first_clause = next_clause
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
                "delta": list(delta),
                "semantic": "raw primary time vector is lexicographically <= its translated vector",
                "edge_order": "UTF-8 lexical order of canonical edge names",
                "time_bit_order": "MSB 9 through LSB 0",
                "recurrence": "le_i = (not x_i and y_i) or (x_i == y_i and le_(i+1))",
                "base_case": "le_n = true",
                "definition_first_variable": first_var,
                "definition_last_variable": next_var - 1,
                "definition_first_clause": definition_first_clause,
                "definition_last_clause": root_clause_id - 1,
                "root_variable": suffix,
                "root_clause_id": root_clause_id,
            }
            roots.append(row)
            trace_rows.append({
                "delta": list(delta),
                "edge_map_sha256": hashlib.sha256(
                    json.dumps(transformed, sort_keys=True, separators=(",", ":")).encode()
                ).hexdigest(),
                "first_variable": first_var,
                "last_variable": next_var - 1,
                "root_variable": suffix,
            })
    assert next_var == final_vars + 1
    assert next_clause == final_clauses + 1

    args.output_roots.parent.mkdir(parents=True, exist_ok=True)
    with args.output_roots.open("w", encoding="utf-8", newline="\n") as handle:
        for index, row in enumerate(roots):
            handle.write(json.dumps({"assertion_index": index, **row}, sort_keys=True,
                                    separators=(",", ":")) + "\n")
    trace = {
        "schema": "circdist-gross-round102-translation-lex-leader-trace-v1",
        "group": {"name": "Z_12 x Z_6", "order": 72, "nonidentity": 71},
        "edge_order": edges,
        "bits_per_time": 10,
        "bits_per_vector": bits_per_vector,
        "base_constant_true": constant_true,
        "recurrence_truth_table_clauses_per_bit": 8,
        "rows": trace_rows,
        "finite_orbit_theorem": "every 72-image orbit has a unique least schedule vector; group stabilizers may give multiple elements mapping to that same vector",
    }
    args.output_trace.write_bytes(gzip.compress(
        (json.dumps(trace, sort_keys=True, separators=(",", ":")) + "\n").encode(),
        compresslevel=9, mtime=0))

    meta = dict(base)
    meta.update({
        "schema": "circdist-gross-round102-translation-quotient-cnf-v1",
        "status": "PASS",
        "base_cnf_sha256": base["cnf_sha256"],
        "base_variables": base_vars,
        "base_clauses": base_clauses,
        "variables": final_vars,
        "clauses": final_clauses,
        "assertions": int(base["assertions"]) + added_root_clauses,
        "translation_group": "Z_12 x Z_6",
        "translation_group_order": 72,
        "translation_nonidentity_roots": 71,
        "translation_bits_per_vector": bits_per_vector,
        "translation_added_variables": added_vars,
        "translation_added_definition_clauses": added_definition_clauses,
        "translation_added_root_clauses": added_root_clauses,
        "translation_roots_sha256": sha(args.output_roots),
        "translation_trace_sha256": sha(args.output_trace),
        "cnf_sha256": sha(args.output_cnf),
        "compile_seconds": round(time.time() - started, 6),
        "equivalence_kind": "base unique definitional extension plus exact lex-leader recurrence; exact projection onto orbit-minimal base schedules",
        "integer_safety": {
            "dimacs_variable_limit_signed_32": (1 << 31) - 1,
            "final_variables": final_vars,
            "final_clauses": final_clauses,
            "clause_identifier_limit_signed_64": (1 << 63) - 1,
        },
    })
    args.output_metadata.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS", "cnf_sha256": meta["cnf_sha256"],
        "base_variables": base_vars, "base_clauses": base_clauses,
        "variables": final_vars, "clauses": final_clauses,
        "added_variables": added_vars,
        "added_definition_clauses": added_definition_clauses,
        "added_root_clauses": added_root_clauses,
        "seconds": meta["compile_seconds"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
