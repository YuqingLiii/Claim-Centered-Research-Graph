#!/usr/bin/env python3
"""Emit the raw one-clause block-contiguous counterexample as JSON.

The output contains the complete H_X/H_Z supports and checkable GF(2)
certificates.  It uses no repository imports and writes only to stdout.
"""

import json
from itertools import combinations

from construction import Builder, in_span, kernel_basis, rref
from z_companion import (canonical, from_code, parity, rank,
                         repetition3_matrix, support, weight)


def restricted_normalizer_basis(code, qubits):
    """Basis for ker(H_X) vectors whose support is contained in qubits."""
    positions = {q: i for i, q in enumerate(qubits)}
    restricted_rows = []
    for row in code.hx:
        restricted_rows.append(sum(
            1 << positions[q] for q in qubits if (row >> q) & 1
        ))
    local_basis = kernel_basis(restricted_rows, len(qubits))
    return [
        sum(1 << qubits[i] for i in range(len(qubits)) if (v >> i) & 1)
        for v in local_basis
    ]


def restricted_quotient_record(code, qubits, sz_rb, sz_piv, sz_rank):
    basis = restricted_normalizer_basis(code, qubits)
    normalizer_dimension = len(basis)
    joined_rank = rank(list(code.hz) + basis, code.n)
    intersection_dimension = normalizer_dimension + sz_rank - joined_rank
    quotient_dimension = normalizer_dimension - intersection_dimension
    witness = next((v for v in basis if not in_span(v, sz_rb, sz_piv)), None)
    return {
        "support_size": len(qubits),
        "restricted_normalizer_dimension": normalizer_dimension,
        "stabilizer_intersection_dimension": intersection_dimension,
        "nontrivial_quotient_dimension": quotient_dimension,
        "witness_support": None if witness is None else support(witness, code.n),
    }


def build_counterexample():
    builder = Builder()
    code = from_code(builder.build_formula(
        3, [((0, True), (1, True), (2, True))]
    ), "one-positive-clause-C0")
    lifted = repetition3_matrix(code, "R3(one-positive-clause-C0)")
    sz_rb, sz_piv = rref(list(code.hz), code.n)
    sz_rank = len(sz_rb)

    hook_specs = ((0, 8), (9, 2))
    hooks = []
    old_prefix_xor = 0
    old_suffix_xor = 0
    physical_prefix_xor = 0
    physical_suffix_xor = 0
    for row_index, old_cut in hook_specs:
        old_order = support(code.hz[row_index], code.n)
        old_prefix = sum(1 << q for q in old_order[:old_cut])
        old_suffix = sum(1 << q for q in old_order[old_cut:])
        physical_prefix = sum(
            1 << (3 * q + a) for q in old_order[:old_cut] for a in range(3)
        )
        physical_suffix = sum(
            1 << (3 * q + a) for q in old_order[old_cut:] for a in range(3)
        )
        old_prefix_xor ^= old_prefix
        old_suffix_xor ^= old_suffix
        physical_prefix_xor ^= physical_prefix
        physical_suffix_xor ^= physical_suffix
        hooks.append({
            "H_Z_row_index": row_index,
            "old_increasing_block_order": old_order,
            "old_block_cut": old_cut,
            "lifted_gate_cut": 3 * old_cut,
            "physical_prefix_support": support(physical_prefix, lifted.n),
            "physical_suffix_hook_support": support(physical_suffix, lifted.n),
        })

    old_logical = old_suffix_xor
    lifted_logical = physical_suffix_xor
    lifted_sz_rb, lifted_sz_piv = rref(list(lifted.hz), lifted.n)
    old_remainder = canonical(old_logical, sz_rb, sz_piv)
    lifted_remainder = canonical(lifted_logical, lifted_sz_rb, lifted_sz_piv)

    single_rows = []
    for i, row in enumerate(code.hz):
        qubits = support(row, code.n)
        rec = restricted_quotient_record(code, qubits, sz_rb, sz_piv, sz_rank)
        rec["rows"] = [i]
        single_rows.append(rec)

    extra_pairs = []
    for i, j in combinations(range(len(code.hz)), 2):
        qubits = sorted(set(support(code.hz[i], code.n)) |
                        set(support(code.hz[j], code.n)))
        rec = restricted_quotient_record(code, qubits, sz_rb, sz_piv, sz_rank)
        if rec["nontrivial_quotient_dimension"]:
            rec["rows"] = [i, j]
            extra_pairs.append(rec)

    return {
        "schema": "circdist-round66-block-counterexample-v1",
        "scope": (
            "Smallest nonempty valid source instance; this refutes the emitted "
            "increasing block-contiguous order, not existence of some other block order."
        ),
        "source": {
            "encoding": "p 3 1 1 2 3",
            "formula": "(x_0 OR x_1 OR x_2)",
            "why_smallest_in_source_family": (
                "Every valid nonempty (3,4)-SAT instance has at least one clause; "
                "the zero-clause branch emits only the fixed companion."
            ),
        },
        "C0": {
            "n": code.n,
            "H_X_row_supports": [support(row, code.n) for row in code.hx],
            "H_Z_row_supports": [support(row, code.n) for row in code.hz],
            "rank_H_X": rank(code.hx, code.n),
            "rank_H_Z": sz_rank,
        },
        "increasing_block_hooks": hooks,
        "certificate": {
            "old_suffix_xor_support": support(old_logical, code.n),
            "old_suffix_xor_weight": weight(old_logical),
            "old_prefix_xor_support": support(old_prefix_xor, code.n),
            "old_H_X_syndrome_nonzero_rows": [
                i for i, row in enumerate(code.hx) if parity(row & old_logical)
            ],
            "old_H_Z_rref_pivots": sz_piv,
            "old_H_Z_rref_remainder_support": support(old_remainder, code.n),
            "old_logical_not_in_H_Z_rowspan": old_remainder != 0,
            "old_prefix_suffix_same_quotient": in_span(
                old_prefix_xor ^ old_suffix_xor, sz_rb, sz_piv
            ),
            "lifted_suffix_xor_support": support(lifted_logical, lifted.n),
            "lifted_suffix_xor_weight": weight(lifted_logical),
            "lifted_prefix_xor_support": support(physical_prefix_xor, lifted.n),
            "lifted_H_X_syndrome_nonzero_rows": [
                i for i, row in enumerate(lifted.hx) if parity(row & lifted_logical)
            ],
            "lifted_H_Z_rref_remainder_support": support(
                lifted_remainder, lifted.n
            ),
            "lifted_logical_not_in_H_Z_rowspan": lifted_remainder != 0,
            "lifted_prefix_suffix_same_quotient": in_span(
                physical_prefix_xor ^ physical_suffix_xor,
                lifted_sz_rb,
                lifted_sz_piv,
            ),
        },
        "row_union_audit": {
            "single_rows_checked": len(single_rows),
            "all_single_row_restricted_quotients_trivial": all(
                rec["nontrivial_quotient_dimension"] == 0 for rec in single_rows
            ),
            "single_row_records": single_rows,
            "row_pairs_checked": len(code.hz) * (len(code.hz) - 1) // 2,
            "pairs_with_nontrivial_restricted_quotient": len(extra_pairs),
            "extra_pair_records": extra_pairs,
        },
    }


if __name__ == "__main__":
    print(json.dumps(build_counterexample(), indent=2, sort_keys=True))
