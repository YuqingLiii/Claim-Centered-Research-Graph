#!/usr/bin/env python3
"""Independent byte-for-byte EFSSC formula rebuild and local truth audit.

This script shares only the frozen Gross model/outer constructor with Round80.
It does not import either Round86 compiler.  The EFSSC equations are rebuilt
here from their public rank/parity definition, every new local membership
predicate is tested on all 6! orders, and the resulting SMT-LIB is compared by
the caller to the sealed formula.
"""
from pathlib import Path
import argparse, gzip, hashlib, itertools, json, os, sys

ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output-smt2", type=Path, required=True)
ap.add_argument("--output-summary", type=Path, required=True)
ap.add_argument("--compiler-smt2", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
P = R / "vendor" / "round80"
sys.path[:0] = [str(P / "src" / "round63_src"), str(P / "src")]
import z3
import model as M
import round68_build as B
from outer import OuterScheduler


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def sha_obj(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == ".gz" else blob)


def parity(arguments, constant=False):
    arguments = list(arguments)
    if not arguments:
        return z3.BoolVal(bool(constant))
    value = arguments[0]
    for argument in arguments[1:]:
        value = z3.Xor(value, argument)
    return z3.Not(value) if constant else value


def signature(vector, detectors, duals):
    return sum(((M.popcount(vector & h) & 1) << i) for i, h in enumerate(detectors)) | sum(
        ((M.popcount(vector & h) & 1) << (72 + i)) for i, h in enumerate(duals)
    )


def position_parity(kinds):
    answer = set()
    for kind in kinds:
        for position in M.RES_POS[int(kind)]:
            if position in answer:
                answer.remove(position)
            else:
                answer.add(position)
    return tuple(sorted(answer))


state = json.loads((R / "continuation" / "final_state.json").read_text())
dynamic = load(P / "restart" / "dynamic_blocks_iteration102.json.gz")
generalized = load(P / "restart" / "installed_generalized_terms_iteration102.json.gz")
raw = load(P / "restart" / "full_raw_mechanisms_iteration102.json.gz")
registry = load(P / "restart" / "online_mechanism_registry_iteration102.json.gz")
expected_semantic = {
    "dynamic": "62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2",
    "generalized": "4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3",
    "registry": "b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604",
    "raw": "fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600",
}
actual_semantic = {
    "dynamic": sha_obj(dynamic),
    "generalized": sha_obj(generalized),
    "registry": sha_obj(registry),
    "raw": sha_obj(raw),
}
assert actual_semantic == expected_semantic == state["reviewed_base_semantic_sha256"]
assert len(dynamic) == 204
assert generalized["term_count"] == len(generalized["terms"]) == 12820
assert raw["mechanism_count"] == len(raw["mechanisms"]) == 120
assert registry["mechanism_count"] == 120

px, pz, lx, lz = B.load_context()
round63_x, _ = B.global_single_records("Xerr", M.Xchecks, px, "X")
round63_z, _ = B.global_single_records("Zerr", M.Zchecks, pz, "Z")
round62 = load(P / "src" / "round62_cegar20.json.gz")
B.replay_round62_blocks(round62, lx, lz)
outer = OuterScheduler(True)
for i, record in enumerate(round63_x + round63_z):
    outer.add_block([tuple(atom) for atom in record["atoms"]], f"r63-{i}")
for block in round62["outer_blocks"]:
    outer.add_block([tuple(atom) for atom in block["atoms"]], "r62-" + block["tag"], block["trace_sha256"])
for term in generalized["terms"]:
    outer.add_block([tuple(atom) for atom in term["atoms"]], term["term_id"], term.get("source_term_sha256"))
for i, block in enumerate(dynamic):
    outer.add_block([tuple(atom) for atom in block["atoms"]], f"dynamic-{i}-{block['sector']}", block.get("mechanism_sha256"))
assert len(outer.blocks) == 14484

sector_data = {
    "Xerr": {"checks": M.Xchecks, "edge_kind": "X", "detectors": M.HZ, "duals": lz},
    "Zerr": {"checks": M.Zchecks, "edge_kind": "Z", "detectors": M.HX, "duals": lx},
}
for sector in sector_data.values():
    sector["qubit_signatures"] = [signature(1 << q, sector["detectors"], sector["duals"]) for q in range(144)]

rank_cache = {}
member_cache = {}


def rank_expression(label, check, qubit):
    key = (label, check, qubit)
    if key not in rank_cache:
        sector = sector_data[label]
        t_qubit = outer.t[M.edge_key(sector["edge_kind"], check, qubit)]
        rank_cache[key] = z3.Sum([
            z3.If(outer.t[M.edge_key(sector["edge_kind"], check, other)] < t_qubit, 1, 0)
            for other in sector["checks"][check] if other != qubit
        ])
    return rank_cache[key]


def member_expression(label, check, kinds, qubit):
    positions = position_parity(kinds)
    key = (label, check, positions, qubit)
    if key not in member_cache:
        rank = rank_expression(label, check, qubit)
        member_cache[key] = z3.Or([rank == p for p in positions]) if positions else z3.BoolVal(False)
    return member_cache[key]


def valid_expression(selector):
    label = selector["sector"]
    sector = sector_data[label]
    singleton_signature = signature(M.mask(selector["data_support"]), sector["detectors"], sector["duals"])
    bit_terms = [[] for _ in range(84)]
    for check_string, raw_kinds in sorted(selector["group_kinds"].items(), key=lambda item: int(item[0])):
        check = int(check_string)
        kinds = tuple(sorted(map(int, raw_kinds)))
        for qubit in sector["checks"][check]:
            member = member_expression(label, check, kinds, qubit)
            qubit_signature = sector["qubit_signatures"][qubit]
            for bit in range(84):
                if (qubit_signature >> bit) & 1:
                    bit_terms[bit].append(member)
    bits = [parity(bit_terms[bit], bool((singleton_signature >> bit) & 1)) for bit in range(84)]
    return z3.And(*[z3.Not(bit) for bit in bits[:72]], z3.Or(*bits[72:]))


source_truth = []
for selector in state["selectors"]:
    expression = valid_expression(selector)
    substitutions = [(variable, z3.IntVal(int(selector["source_times"][edge]))) for edge, variable in outer.t.items()]
    evaluated = z3.simplify(z3.substitute(expression, *substitutions))
    assert z3.is_true(evaluated), (selector["mechanism_id"], evaluated)
    outer.s.add(z3.Not(expression))
    source_truth.append(selector["mechanism_id"])

# Independent local truth table for every rank-membership domain introduced in
# Round86.  This checks 720 orders x 6 qubits for each distinct new domain.
new_domains = set()
for selector in state["selectors"][120:]:
    for check_string, raw_kinds in selector["group_kinds"].items():
        new_domains.add((selector["sector"], int(check_string), tuple(sorted(map(int, raw_kinds)))))
local_evaluations = 0
for label, check, kinds in sorted(new_domains):
    sector = sector_data[label]
    row = sector["checks"][check]
    selected_positions = set(position_parity(kinds))
    for order in itertools.permutations(row):
        substitutions = [
            (outer.t[M.edge_key(sector["edge_kind"], check, q)], z3.IntVal(position))
            for position, q in enumerate(order)
        ]
        for position, q in enumerate(order):
            observed = z3.simplify(z3.substitute(member_expression(label, check, kinds, q), *substitutions))
            assert z3.is_true(observed) == (position in selected_positions)
            local_evaluations += 1

formula = outer.s.to_smt2()
formula_sha256 = hashlib.sha256(formula.encode()).hexdigest()
a.output_smt2.write_text(formula)
assert len(outer.s.assertions()) == state["final_assertions"]
assert len(rank_cache) == state["rank_expressions"]
assert len(member_cache) == state["membership_expressions"]
parsed = z3.parse_smt2_string(formula)
assert len(parsed) == state["final_assertions"]
compiler_parsed = z3.parse_smt2_file(str(a.compiler_smt2))
assert len(compiler_parsed) == len(parsed)
structural_unequal = [i for i, (left, right) in enumerate(zip(compiler_parsed, parsed)) if not z3.eq(left, right)]
assert structural_unequal == []
normalized_ast = parsed.sexpr()
compiler_normalized_ast = compiler_parsed.sexpr()
assert normalized_ast == compiler_normalized_ast
normalized_ast_sha256 = hashlib.sha256(normalized_ast.encode()).hexdigest()
compiler_normalized_ast_sha256 = hashlib.sha256(compiler_normalized_ast.encode()).hexdigest()

# Negative control: a one-kind corruption changes the semantic selector hash.
control = dict(state["selectors"][120])
control_groups = {k: list(v) for k, v in control["group_kinds"].items()}
first_group = sorted(control_groups, key=int)[0]
control_groups[first_group] = [(control_groups[first_group][0] + 1) % 3] + control_groups[first_group][1:]
original_selector_hash = sha_obj({k: state["selectors"][120][k] for k in ("sector", "selected_names", "data_support", "group_kinds")})
corrupt_selector_hash = sha_obj({
    "sector": control["sector"],
    "selected_names": control["selected_names"],
    "data_support": control["data_support"],
    "group_kinds": control_groups,
})
assert original_selector_hash == state["selectors"][120]["selector_semantic_sha256"]
assert corrupt_selector_hash != original_selector_hash

summary = {
    "schema": "round86-independent-efssc-formula-rebuild-v1",
    "status": "PASS",
    "reviewed_semantic_hashes": actual_semantic,
    "reviewed_blocks": len(outer.blocks),
    "selector_count": len(state["selectors"]),
    "source_selector_truths_checked": len(source_truth),
    "new_local_domains_exhausted": len(new_domains),
    "new_local_membership_truth_evaluations": local_evaluations,
    "rank_expressions": len(rank_cache),
    "membership_expressions": len(member_cache),
    "assertions": len(outer.s.assertions()),
    "parsed_assertions": len(parsed),
    "compiler_parsed_assertions": len(compiler_parsed),
    "structurally_unequal_assertions": len(structural_unequal),
    "normalized_ast_sha256": normalized_ast_sha256,
    "compiler_normalized_ast_sha256": compiler_normalized_ast_sha256,
    "normalized_ast_exact_match": True,
    "formula_bytes": len(formula.encode()),
    "formula_sha256": formula_sha256,
    "compiler_formula_sha256": state["final_formula_sha256"],
    "byte_hash_matches_compiler_formula": formula_sha256 == state["final_formula_sha256"],
    "negative_control": {
        "original_selector_semantic_sha256": original_selector_hash,
        "corrupt_kind_selector_semantic_sha256": corrupt_selector_hash,
        "hash_changed": True,
    },
    "solver_check_called": False,
}
a.output_summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps(summary, sort_keys=True))
