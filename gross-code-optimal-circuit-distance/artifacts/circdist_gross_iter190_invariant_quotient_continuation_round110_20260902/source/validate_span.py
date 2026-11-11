#!/usr/bin/env python3
"""Independent direct-semantics validation of the full-span UNSAT theorems."""
from pathlib import Path
from itertools import product
import argparse
import gzip
import hashlib
import json
import struct
import time
import z3


def actual(path):
    path = Path(path)
    if path.exists():
        return path
    encoded = path.with_name(path.name + ".gz")
    assert encoded.exists(), path
    return encoded


def open_data(path, text=False):
    path = actual(path)
    if path.suffix == ".gz":
        return gzip.open(path, "rt" if text else "rb", encoding="utf-8" if text else None)
    return path.open("r" if text else "rb", encoding="utf-8" if text else None)


def file_sha256(path):
    digest = hashlib.sha256()
    with open_data(path) as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def from_words(words):
    return sum(int(word) << (64 * i) for i, word in enumerate(words))


def parse_rows(path):
    raw = Path(path).read_bytes()
    assert raw[:16] == b"CDR98O5V1\0\0\0\0\0\0\0"
    count = struct.unpack_from("<Q", raw, 16)[0]
    assert len(raw) == 24 + count * 19 * 8
    rows = []
    for index in range(count):
        values = struct.unpack_from("<19Q", raw, 24 + index * 19 * 8)
        rows.append((values[0], from_words(values[1:7]), from_words(values[7:10]),
                     from_words(values[10:13]), from_words(values[13:15]),
                     from_words(values[15:17]), values[17], values[18]))
    return rows


def xor_all(values):
    values = list(values)
    if not values:
        return z3.BoolVal(False)
    result = values[0]
    for value in values[1:]:
        result = z3.Xor(result, value)
    return result


def gf2_rank(columns):
    basis = {}
    for value in columns:
        remaining = value
        while remaining:
            pivot = remaining.bit_length() - 1
            if pivot in basis:
                remaining ^= basis[pivot]
            else:
                basis[pivot] = remaining
                break
    return len(basis)


# Exhaustive gate controls, stated independently of the emitted CNFs.
gate_cases = 0
for left, right, output in product((False, True), repeat=3):
    xor_clauses = ((not left or not right or not output), (left or right or not output),
                   (left or not right or output), (not left or right or output))
    and_clauses = ((not output or left), (not output or right), (output or not left or not right))
    or_clauses = ((output or not left), (output or not right), (not output or left or right))
    assert all(xor_clauses) == (output == (left ^ right))
    assert all(and_clauses) == (output == (left and right))
    assert all(or_clauses) == (output == (left or right))
    gate_cases += 1

# Exhaustively recompute the at-least-j recurrence for every input through n=12.
cardinality_cases = 0
for n in range(1, 13):
    for bits in product((False, True), repeat=n):
        previous = {}
        for i, value in enumerate(bits, 1):
            current = {}
            for j in range(1, min(i, 11) + 1):
                if i == 1 and j == 1:
                    current[j] = value
                elif j == 1:
                    current[j] = previous[1] or value
                elif j == i:
                    current[j] = previous[j - 1] and value
                else:
                    current[j] = previous[j] or (previous[j - 1] and value)
                assert current[j] == (sum(bits[:i]) >= j)
                cardinality_cases += 1
            previous = current

parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
synthesis = root / "synthesis"
sector_results = {}
for label, expected_count in (("Xerr", 125), ("Zerr", 109)):
    started = time.time()
    rows = parse_rows(synthesis / f"order5_input/{label}.rows.bin")
    ids = json.loads((synthesis / f"order5_input/{label}.ids.json").read_text())
    metadata = json.loads((synthesis / f"span/{label}.metadata.json").read_text())
    certificate = json.loads((synthesis / f"span/{label}.unsat_certificate/certificate.json").read_text())
    assert len(rows) == len(ids) == expected_count == metadata["row_count"]
    cnf_path = synthesis / f"span/{label}.cnf"
    with open_data(cnf_path, text=True) as source:
        header = source.readline().split()
        assert header[:2] == ["p", "cnf"]
        variable_count, clause_count = map(int, header[2:])
        parsed_clauses = 0
        for line in source:
            clause = [int(value) for value in line.split()]
            assert clause[-1] == 0 and clause[:-1]
            assert all(1 <= abs(value) <= variable_count for value in clause[:-1])
            parsed_clauses += 1
    assert variable_count == metadata["variables"] and clause_count == parsed_clauses == metadata["clauses"]
    assert file_sha256(cnf_path) == metadata["cnf_sha256"] == certificate["formula_sha256"]
    assert certificate["status"] == "PASS" and certificate["valid_drat_accepted"] and certificate["generated_lrat_accepted"]
    assert certificate["corrupt_drat_rejected"] and certificate["truncated_drat_rejected"]
    assert certificate["corrupt_lrat_rejected"] and certificate["truncated_lrat_rejected"]
    assert certificate["all_children_reaped"] and certificate["detached_processes"] == 0
    assert len(certificate["processes"]) == 6 and all(row["reaped"] and not row["detached"] for row in certificate["processes"])

    coefficients = [z3.Bool(f"{label}_coefficient_{index}") for index in range(expected_count)]
    name_bits = [xor_all(coefficients[index] for index, row in enumerate(rows) if (row[1] >> bit) & 1)
                 for bit in range(360)]
    canonical_syndrome_bits = [xor_all(coefficients[index] for index, row in enumerate(rows) if (row[4] >> bit) & 1)
                               for bit in range(72)]
    physical_syndrome_bits = [xor_all(coefficients[index] for index, row in enumerate(rows) if (row[5] >> bit) & 1)
                              for bit in range(72)]
    canonical_logical_bits = [xor_all(coefficients[index] for index, row in enumerate(rows) if (row[6] >> bit) & 1)
                              for bit in range(12)]
    physical_logical_bits = [xor_all(coefficients[index] for index, row in enumerate(rows) if (row[7] >> bit) & 1)
                             for bit in range(12)]
    solver = z3.Solver()
    weight = z3.Sum([z3.If(bit, 1, 0) for bit in name_bits])
    solver.add(weight >= 1, weight <= 10)
    solver.add(*[z3.Not(bit) for bit in canonical_syndrome_bits])
    solver.add(*[z3.Not(bit) for bit in physical_syndrome_bits])
    solver.add(*[canonical_logical_bits[bit] == physical_logical_bits[bit] for bit in range(12)])
    solver.add(z3.Or(canonical_logical_bits))
    existing_masks = sorted({row[1] for row in rows})
    assert len(existing_masks) == expected_count
    for mask in existing_masks:
        solver.add(z3.Or(*[z3.Not(name_bits[bit]) if (mask >> bit) & 1 else name_bits[bit]
                           for bit in range(360)]))
    result = solver.check()
    assert result == z3.unsat
    combined_syndromes = [row[4] | (row[5] << 72) for row in rows]
    sector_results[label] = {
        "status": "UNSAT",
        "row_count": expected_count,
        "coefficient_domain_size": f"2^{expected_count}",
        "name_matrix_rank": gf2_rank([row[1] for row in rows]),
        "combined_syndrome_matrix_rank": gf2_rank(combined_syndromes),
        "cnf_variables": variable_count,
        "cnf_clauses": clause_count,
        "cnf_sha256": metadata["cnf_sha256"],
        "drat_sha256": certificate["drat_sha256"],
        "lrat_sha256": certificate["lrat_sha256"],
        "z3_direct_semantics": "UNSAT",
        "z3_seconds": round(time.time() - started, 6),
        "existing_full_named_masks_blocked": len(existing_masks),
    }

output = {
    "schema": "circdist-round100-full-span-independent-validation-v1",
    "status": "PASS",
    "z3_version": z3.get_version_string(),
    "gate_truth_table_cases": gate_cases,
    "cardinality_recurrence_cases": cardinality_cases,
    "sector_results": sector_results,
    "theorem": (
        "For each sector on the reviewed post-iteration-136 schedule, no GF(2) combination of the entire reviewed "
        "125-row Xerr or 109-row Zerr basis yields a new full named mask of weight 1..10 with both canonical and "
        "physical syndrome zero and equal nonzero logical action. Existing selector named masks are explicitly "
        "quotiented; the theorem does not exclude arbitrary mechanisms outside either selector span."
    ),
}
args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "Xerr": sector_results["Xerr"]["status"],
                  "Zerr": sector_results["Zerr"]["status"],
                  "gate_cases": gate_cases, "cardinality_cases": cardinality_cases}, sort_keys=True))
