#!/usr/bin/env python3
"""Build an exact CNF for a novel low-named-weight mechanism in a full selector GF(2) span."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import struct


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
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
        rows.append({
            "global_index": values[0],
            "names": from_words(values[1:7]),
            "canonical": from_words(values[7:10]),
            "physical": from_words(values[10:13]),
            "canonical_syndrome": from_words(values[13:15]),
            "physical_syndrome": from_words(values[15:17]),
            "canonical_logical": values[17],
            "physical_logical": values[18],
        })
    return rows


parser = argparse.ArgumentParser()
parser.add_argument("--rows", type=Path, required=True)
parser.add_argument("--ids", type=Path, required=True)
parser.add_argument("--state", type=Path, required=True)
parser.add_argument("--sector", choices=("Xerr", "Zerr"), required=True)
parser.add_argument("--cnf", type=Path, required=True)
parser.add_argument("--metadata", type=Path, required=True)
args = parser.parse_args()
rows = parse_rows(args.rows)
ids = json.loads(args.ids.read_text())
state = json.loads(args.state.read_text())
selectors = [selector for selector in state["selectors"] if selector["sector"] == args.sector]
assert len(rows) == len(ids) == len(selectors)
assert ids == [selector["mechanism_id"] for selector in selectors]
for row, selector in zip(rows, selectors):
    assert state["selectors"][row["global_index"]]["mechanism_id"] == selector["mechanism_id"]

clauses = []
families = Counter()
variables = {}
next_variable = 0


def new_variable(label):
    global next_variable
    assert label not in variables
    next_variable += 1
    variables[label] = next_variable
    return next_variable


def add_clause(clause, family):
    assert clause and all(literal and abs(literal) <= next_variable for literal in clause)
    clauses.append(tuple(clause))
    families[family] += 1


def equivalence(output, source, family):
    add_clause((-output, source), family)
    add_clause((output, -source), family)


def xor_equivalence(output, left, right, family):
    add_clause((-left, -right, -output), family)
    add_clause((left, right, -output), family)
    add_clause((left, -right, output), family)
    add_clause((-left, right, output), family)


def and_equivalence(output, left, right, family):
    add_clause((-output, left), family)
    add_clause((-output, right), family)
    add_clause((output, -left, -right), family)


def or_equivalence(output, left, right, family):
    add_clause((output, -left), family)
    add_clause((output, -right), family)
    add_clause((-output, left, right), family)


coefficients = [new_variable(f"coefficient:{index}") for index in range(len(rows))]
name_outputs = [new_variable(f"name:{bit}") for bit in range(360)]


def parity_output(label, inputs, requested_output=None):
    output = requested_output if requested_output is not None else new_variable(label)
    if not inputs:
        add_clause((-output,), f"parity:{label}:zero")
    elif len(inputs) == 1:
        equivalence(output, inputs[0], f"parity:{label}:single")
    else:
        current = inputs[0]
        for position, value in enumerate(inputs[1:], 1):
            target = output if position == len(inputs) - 1 else new_variable(f"{label}:xor:{position}")
            xor_equivalence(target, current, value, f"parity:{label}:xor")
            current = target
        assert current == output
    return output


for bit, output in enumerate(name_outputs):
    inputs = [coefficients[index] for index, row in enumerate(rows) if (row["names"] >> bit) & 1]
    parity_output(f"name:{bit}", inputs, output)

canonical_syndrome_outputs = []
physical_syndrome_outputs = []
logical_difference_outputs = []
canonical_logical_outputs = []
for bit in range(72):
    canonical = parity_output(f"canonical_syndrome:{bit}",
                              [coefficients[index] for index, row in enumerate(rows)
                               if (row["canonical_syndrome"] >> bit) & 1])
    physical = parity_output(f"physical_syndrome:{bit}",
                             [coefficients[index] for index, row in enumerate(rows)
                              if (row["physical_syndrome"] >> bit) & 1])
    canonical_syndrome_outputs.append(canonical)
    physical_syndrome_outputs.append(physical)
    add_clause((-canonical,), "root:canonical_syndrome_zero")
    add_clause((-physical,), "root:physical_syndrome_zero")
for bit in range(12):
    difference = parity_output(f"logical_difference:{bit}",
                               [coefficients[index] for index, row in enumerate(rows)
                                if ((row["canonical_logical"] ^ row["physical_logical"]) >> bit) & 1])
    canonical = parity_output(f"canonical_logical:{bit}",
                              [coefficients[index] for index, row in enumerate(rows)
                               if (row["canonical_logical"] >> bit) & 1])
    logical_difference_outputs.append(difference)
    canonical_logical_outputs.append(canonical)
    add_clause((-difference,), "root:logical_equality")
add_clause(tuple(canonical_logical_outputs), "root:logical_nonzero")
add_clause(tuple(name_outputs), "root:named_nonzero")

# Exact dynamic-programming recurrence for at least j true inputs among the first i.
# Only j<=11 is materialized; asserting not(at_least_11) is exactly weight<=10.
previous = {}
for i, named in enumerate(name_outputs, 1):
    current = {}
    for j in range(1, min(i, 11) + 1):
        output = new_variable(f"at_least:{i}:{j}")
        if i == 1 and j == 1:
            equivalence(output, named, "cardinality:boundary")
        elif j == 1:
            or_equivalence(output, previous[1], named, "cardinality:or")
        elif j == i:
            and_equivalence(output, previous[j - 1], named, "cardinality:and")
        else:
            conjunction = new_variable(f"at_least_and:{i}:{j}")
            and_equivalence(conjunction, previous[j - 1], named, "cardinality:and")
            or_equivalence(output, previous[j], conjunction, "cardinality:or")
        current[j] = output
    previous = current
add_clause((-previous[11],), "root:named_at_most_10")

# A novel result is different as a complete 360-bit named mask from each installed selector.
existing_masks = []
for selector in selectors:
    mask = next(row["names"] for row in rows if row["global_index"] == state["selectors"].index(selector))
    existing_masks.append(mask)
assert len(existing_masks) == len(set(existing_masks))
for mask in sorted(existing_masks):
    add_clause(tuple(-output if (mask >> bit) & 1 else output for bit, output in enumerate(name_outputs)),
               "root:novel_named_mask")

args.cnf.parent.mkdir(parents=True, exist_ok=True)
with args.cnf.open("w", encoding="ascii", newline="\n") as output:
    output.write(f"p cnf {next_variable} {len(clauses)}\n")
    for clause in clauses:
        output.write(" ".join(map(str, clause)) + " 0\n")
metadata = {
    "schema": "circdist-round100-full-span-cnf-v1",
    "status": "PASS",
    "sector": args.sector,
    "row_count": len(rows),
    "coefficient_variables": coefficients,
    "name_variables": name_outputs,
    "canonical_syndrome_variables": canonical_syndrome_outputs,
    "physical_syndrome_variables": physical_syndrome_outputs,
    "logical_difference_variables": logical_difference_outputs,
    "canonical_logical_variables": canonical_logical_outputs,
    "variables": next_variable,
    "clauses": len(clauses),
    "clause_families": dict(sorted(families.items())),
    "row_file_sha256": file_sha256(args.rows),
    "ids_file_sha256": file_sha256(args.ids),
    "state_file_sha256": file_sha256(args.state),
    "cnf_sha256": file_sha256(args.cnf),
    "existing_named_masks_blocked": len(existing_masks),
    "theorem_query": (
        "Does the complete GF(2) span contain a named-weight-1..10 result with both syndromes zero, "
        "equal nonzero canonical/physical logical action, and a full named mask unequal to every installed selector?"
    ),
    "xor_encoding": "four-clause equivalence for every binary XOR in a deterministic chain",
    "cardinality_encoding": "equivalent at-least-j dynamic program through j=11; final at-least-11 output false",
}
args.metadata.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: metadata[key] for key in ("status", "sector", "row_count", "variables", "clauses", "cnf_sha256")}, sort_keys=True))
