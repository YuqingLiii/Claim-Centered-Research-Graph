#!/usr/bin/env python3
"""Independent exact replay of the Round100 six-distinct MITM theorem."""
from pathlib import Path
from collections import Counter
from itertools import combinations
from bisect import bisect_left
import argparse
import hashlib
import json
import math
import struct
import sys
import time


MASK64 = (1 << 64) - 1
MASK256 = (1 << 256) - 1


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def object_sha256(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def from_words(words):
    return sum(int(word) << (64 * i) for i, word in enumerate(words))


def to_words(value, count):
    return tuple((value >> (64 * i)) & MASK64 for i in range(count))


def bit_positions(value):
    return [i for i in range(value.bit_length()) if (value >> i) & 1]


def parity_mask(support, duals, popcount):
    result = 0
    for i, dual in enumerate(duals):
        result |= (popcount(support & dual) & 1) << i
    return result


def add256(accumulator, value, limb):
    return (accumulator + (int(value) << (64 * limb))) & MASK256


def hex256(value):
    return f"{value:064x}"


def flat_pairs(counter):
    result = []
    for key, value in sorted(counter.items()):
        result.extend((int(key), int(value)))
    return result


def parse_rows(path):
    raw = Path(path).read_bytes()
    assert raw[:16] == b"CDR98O5V1\0\0\0\0\0\0\0"
    count = struct.unpack_from("<Q", raw, 16)[0]
    assert struct.unpack_from(">Q", raw, 16)[0] != count
    assert len(raw) == 24 + count * 19 * 8
    rows = []
    offset = 24
    for _ in range(count):
        values = struct.unpack_from("<19Q", raw, offset)
        offset += 19 * 8
        row = (
            values[0],
            from_words(values[1:7]),
            from_words(values[7:10]),
            from_words(values[10:13]),
            from_words(values[13:15]),
            from_words(values[15:17]),
            values[17],
            values[18],
        )
        assert row[1] >> 360 == row[2] >> 144 == row[3] >> 144 == 0
        assert row[4] >> 72 == row[5] >> 72 == row[6] >> 12 == row[7] >> 12 == 0
        rows.append(row)
    return rows


def parse_eligible(path):
    raw = Path(path).read_bytes()
    assert raw[:16] == b"CDR100O6V1\0\0\0\0\0\0"
    count = struct.unpack_from("<Q", raw, 16)[0]
    assert len(raw) == 24 + count * 25 * 8
    result = []
    offset = 24
    for _ in range(count):
        values = struct.unpack_from("<25Q", raw, offset)
        offset += 25 * 8
        result.append({
            "name_words": tuple(values[0:6]),
            "names": from_words(values[0:6]),
            "canonical": from_words(values[6:9]),
            "physical": from_words(values[9:12]),
            "canonical_syndrome": from_words(values[12:14]),
            "physical_syndrome": from_words(values[14:16]),
            "canonical_logical": values[16],
            "physical_logical": values[17],
            "multiplicity": values[18],
            "first_indices": tuple(values[19:25]),
        })
    assert [row["name_words"] for row in result] == sorted(row["name_words"] for row in result)
    assert len({row["name_words"] for row in result}) == len(result)
    return result, raw


def triple_table(rows):
    triples = []
    checksum = 0
    for a, b, c in combinations(range(len(rows)), 3):
        A, B, C = rows[a], rows[b], rows[c]
        names = A[1] ^ B[1] ^ C[1]
        canonical = A[2] ^ B[2] ^ C[2]
        physical = A[3] ^ B[3] ^ C[3]
        canonical_syndrome = A[4] ^ B[4] ^ C[4]
        physical_syndrome = A[5] ^ B[5] ^ C[5]
        canonical_logical = A[6] ^ B[6] ^ C[6]
        physical_logical = A[7] ^ B[7] ^ C[7]
        triples.append((canonical_syndrome, physical_syndrome, a, b, c,
                        names, canonical, physical, canonical_logical, physical_logical))
        checksum = add256(checksum, (a + 1) * 3 + (b + 1) * 5 + (c + 1) * 7, 0)
        for i, word in enumerate(to_words(names, 6)):
            checksum = add256(checksum, word, i & 3)
        for i, word in enumerate(to_words(canonical_syndrome, 2)):
            checksum = add256(checksum, word, (i + 1) & 3)
        for i, word in enumerate(to_words(physical_syndrome, 2)):
            checksum = add256(checksum, word, (i + 2) & 3)
    assert len(triples) == math.comb(len(rows), 3)
    return triples, checksum


def count_equal_separated(triples, key_function):
    ordered = sorted(triples, key=lambda triple: (key_function(triple), triple[2:5]))
    count = 0
    group_histogram = Counter()
    checksum = 0
    start = 0
    while start < len(ordered):
        key = key_function(ordered[start])
        end = start + 1
        while end < len(ordered) and key_function(ordered[end]) == key:
            end += 1
        group = ordered[start:end]
        group_histogram[len(group)] += 1
        maxima = sorted(triple[4] for triple in group)
        for upper in group:
            add = bisect_left(maxima, upper[2])
            count += add
            checksum = add256(checksum, add, 0)
            checksum = add256(checksum, upper[2] + 1, 1)
        start = end
    return count, group_histogram, checksum


def exact_combined_candidates(triples):
    ordered = sorted(triples, key=lambda triple: ((triple[0], triple[1]), triple[2:5]))
    combined_count = 0
    group_histogram = Counter()
    name_histogram = Counter()
    canonical_support_histogram = Counter()
    physical_support_histogram = Counter()
    canonical_logical_histogram = Counter()
    physical_logical_histogram = Counter()
    eligible = {}
    checksum = 0
    start = 0
    while start < len(ordered):
        key = ordered[start][0:2]
        end = start + 1
        while end < len(ordered) and ordered[end][0:2] == key:
            end += 1
        group = ordered[start:end]
        group_histogram[len(group)] += 1
        lower_order = sorted(group, key=lambda triple: (triple[4], triple[2:5]))
        for upper in group:
            for lower in lower_order:
                if lower[4] >= upper[2]:
                    break
                indices = lower[2:5] + upper[2:5]
                assert tuple(sorted(indices)) == indices and len(set(indices)) == 6
                combined_count += 1
                names = lower[5] ^ upper[5]
                canonical = lower[6] ^ upper[6]
                physical = lower[7] ^ upper[7]
                canonical_logical = lower[8] ^ upper[8]
                physical_logical = lower[9] ^ upper[9]
                named_weight = names.bit_count()
                name_histogram[named_weight] += 1
                canonical_support_histogram[canonical.bit_count()] += 1
                physical_support_histogram[physical.bit_count()] += 1
                canonical_logical_histogram[canonical_logical] += 1
                physical_logical_histogram[physical_logical] += 1
                checksum = add256(checksum,
                                  (indices[0] + 1) * 3 + (indices[1] + 1) * 5 +
                                  (indices[2] + 1) * 7 + (indices[3] + 1) * 11 +
                                  (indices[4] + 1) * 13 + (indices[5] + 1) * 17, 0)
                for i, word in enumerate(to_words(names, 6)):
                    checksum = add256(checksum, word, i & 3)
                for i, word in enumerate(to_words(canonical, 3)):
                    checksum = add256(checksum, word, (i + 1) & 3)
                for i, word in enumerate(to_words(physical, 3)):
                    checksum = add256(checksum, word, (i + 2) & 3)
                checksum = add256(checksum, canonical_logical, 2)
                checksum = add256(checksum, physical_logical, 3)
                if 1 <= named_weight <= 10:
                    key_words = to_words(names, 6)
                    effect = (canonical, physical, 0, 0, canonical_logical, physical_logical)
                    if key_words not in eligible:
                        eligible[key_words] = {"effect": effect, "multiplicity": 1, "witnesses": [indices]}
                    else:
                        assert eligible[key_words]["effect"] == effect
                        eligible[key_words]["multiplicity"] += 1
                        if len(eligible[key_words]["witnesses"]) < 2:
                            eligible[key_words]["witnesses"].append(indices)
        start = end
    return {
        "count": combined_count,
        "group_histogram": group_histogram,
        "name_histogram": name_histogram,
        "canonical_support_histogram": canonical_support_histogram,
        "physical_support_histogram": physical_support_histogram,
        "canonical_logical_histogram": canonical_logical_histogram,
        "physical_logical_histogram": physical_logical_histogram,
        "eligible": eligible,
        "checksum": checksum,
    }


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
started = time.time()
root = args.root.resolve()
synthesis = root / "synthesis"
vendor = root / "vendor/round80"
state_path = synthesis / "inputs/iter137_state.json"
candidate_path = synthesis / "inputs/iter136_candidate.json"
direct_path = synthesis / "inputs/iter136_direct_verification.json"
assert file_sha256(state_path) == "ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd"
assert file_sha256(candidate_path) == "9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640"
assert file_sha256(direct_path) == "f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e"
state = json.loads(state_path.read_text())
candidate = json.loads(candidate_path.read_text())
selector_keys = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
assert object_sha256([{key: selector.get(key) for key in selector_keys} for selector in state["selectors"]]) == \
       state["selector_state_sha256"] == "47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6"
sys.path[:0] = [str(vendor / "src/round63_src"), str(vendor / "src")]
import model
import round68_build as builder

_, _, logical_x, logical_z = builder.load_context()
times = {key: int(value) for key, value in candidate["compressed_times"].items()}
assert object_sha256(times) == candidate["compressed_schedule_sha256"] == \
       "45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44"
assert model.audit_schedule(times, True) == candidate["frozen_audit"] and candidate["frozen_audit"]["ok"]
sectors = builder.sectors(times, logical_x, logical_z)
names = json.loads((synthesis / "order5_input/name_universe.json").read_text())
assert names == sorted(names) and len(names) == len(set(names)) == 360
name_bit = {name: i for i, name in enumerate(names)}

# Pure combinatorial coverage control, independent of all syndrome data.
coverage_controls = {}
for n in range(6, 13):
    canonical_pairs = set()
    for lower in combinations(range(n), 3):
        for upper in combinations(range(n), 3):
            if lower[2] < upper[0]:
                canonical_pairs.add(lower + upper)
    expected = set(combinations(range(n), 6))
    assert canonical_pairs == expected
    coverage_controls[str(n)] = len(canonical_pairs)

sector_results = {}
retained = []
for label, expected_count in (("Xerr", 125), ("Zerr", 109)):
    sector = sectors[label]
    selectors = [selector for selector in state["selectors"] if selector["sector"] == label]
    assert len(selectors) == expected_count
    parsed_rows = parse_rows(synthesis / f"order5_input/{label}.rows.bin")
    assert len(parsed_rows) == expected_count
    by_name = {column.name: column for column in sector.columns}
    reconstructed_rows = []
    for global_index, selector in [(i, selector) for i, selector in enumerate(state["selectors"]) if selector["sector"] == label]:
        selected_names = selector["selected_names"]
        named = sum(1 << name_bit[name] for name in selected_names)
        canonical = physical = 0
        for name in selected_names:
            canonical ^= by_name[name].support
            physical ^= by_name[name].physical_support
        canonical_syndrome = sector.syndrome_of(canonical)
        physical_syndrome = sector.syndrome_of(physical)
        canonical_logical = parity_mask(canonical, sector.logical_duals, model.popcount)
        physical_logical = parity_mask(physical, sector.logical_duals, model.popcount)
        reconstructed_rows.append((global_index, named, canonical, physical, canonical_syndrome,
                                   physical_syndrome, canonical_logical, physical_logical))
    assert parsed_rows == reconstructed_rows

    triples, triple_checksum = triple_table(parsed_rows)
    canonical_count, canonical_groups, canonical_pair_checksum = count_equal_separated(triples, lambda triple: triple[0])
    physical_count, physical_groups, physical_pair_checksum = count_equal_separated(triples, lambda triple: triple[1])
    combined = exact_combined_candidates(triples)
    summary_path = synthesis / f"order6/{label}.order6.summary.json"
    summary = json.loads(summary_path.read_text())
    assert summary["status"] == "PASS" and summary["selector_count"] == expected_count
    assert summary["triple_count_expected"] == summary["triple_count_enumerated"] == math.comb(expected_count, 3)
    assert summary["full_six_distinct_domain_closed_form"] == math.comb(expected_count, 6)
    assert summary["canonical_syndrome_zero_six_tuples"] == canonical_count
    assert summary["physical_syndrome_zero_six_tuples"] == physical_count
    assert summary["combined_syndrome_zero_six_tuples"] == combined["count"]
    assert summary["canonical_triple_key_group_histogram_flat_pairs"] == flat_pairs(canonical_groups)
    assert summary["physical_triple_key_group_histogram_flat_pairs"] == flat_pairs(physical_groups)
    assert summary["combined_triple_key_group_histogram_flat_pairs"] == flat_pairs(combined["group_histogram"])
    assert summary["triple_checksum_mod_2_256"] == hex256(triple_checksum)
    assert summary["canonical_pair_count_checksum_mod_2_256"] == hex256(canonical_pair_checksum)
    assert summary["physical_pair_count_checksum_mod_2_256"] == hex256(physical_pair_checksum)
    assert summary["combined_candidate_checksum_mod_2_256"] == hex256(combined["checksum"])
    for key, size in (("combined_zero_named_weight_histogram", 61),
                      ("combined_zero_canonical_support_weight_histogram", 145),
                      ("combined_zero_physical_support_weight_histogram", 145),
                      ("combined_zero_canonical_logical_action_histogram", 4096),
                      ("combined_zero_physical_logical_action_histogram", 4096)):
        assert len(summary[key]) == size and sum(summary[key]) == combined["count"]
    assert summary["combined_zero_named_weight_histogram"] == [combined["name_histogram"].get(i, 0) for i in range(61)]
    assert summary["combined_zero_canonical_support_weight_histogram"] == [combined["canonical_support_histogram"].get(i, 0) for i in range(145)]
    assert summary["combined_zero_physical_support_weight_histogram"] == [combined["physical_support_histogram"].get(i, 0) for i in range(145)]
    assert summary["combined_zero_canonical_logical_action_histogram"] == [combined["canonical_logical_histogram"].get(i, 0) for i in range(4096)]
    assert summary["combined_zero_physical_logical_action_histogram"] == [combined["physical_logical_histogram"].get(i, 0) for i in range(4096)]

    eligible_rows, eligible_raw = parse_eligible(synthesis / f"order6/{label}.order6.eligible.bin")
    expected_eligible = combined["eligible"]
    assert len(eligible_rows) == len(expected_eligible) == summary["unique_eligible_named_results"]
    assert summary["eligible_named_weight_1_to_10_occurrences"] == sum(row["multiplicity"] for row in eligible_rows)
    assert summary["eligible_multiplicity_histogram_flat_pairs"] == flat_pairs(Counter(row["multiplicity"] for row in eligible_rows))
    assert summary["maximum_eligible_multiplicity"] == max((row["multiplicity"] for row in eligible_rows), default=0)
    replayed = 0
    conservative_occurrences = 0
    for row in eligible_rows:
        expected = expected_eligible[row["name_words"]]
        assert expected["effect"] == (row["canonical"], row["physical"], row["canonical_syndrome"],
                                      row["physical_syndrome"], row["canonical_logical"], row["physical_logical"])
        assert expected["multiplicity"] == row["multiplicity"]
        indices = row["first_indices"]
        assert tuple(sorted(indices)) == indices and len(set(indices)) == 6 and indices[-1] < expected_count
        effect = [0] * 7
        for index in indices:
            for component, value in enumerate(parsed_rows[index][1:]):
                effect[component] ^= value
        assert tuple(effect) == (row["names"], row["canonical"], row["physical"],
                                 row["canonical_syndrome"], row["physical_syndrome"],
                                 row["canonical_logical"], row["physical_logical"])
        selected_names = [names[i] for i in bit_positions(row["names"])]
        assert 1 <= len(selected_names) <= 10
        canonical_replay = model.verify_named_selection(sector, selected_names, 10)
        assert canonical_replay["weight"] == len(selected_names)
        assert canonical_replay["net_support"] == bit_positions(row["canonical"])
        assert canonical_replay["syndrome"] == [] == bit_positions(row["canonical_syndrome"])
        assert canonical_replay["logical_parities"] == [((row["canonical_logical"] >> i) & 1) for i in range(12)]
        physical = 0
        for name in selected_names:
            physical ^= by_name[name].physical_support
        assert physical == row["physical"] and sector.syndrome_of(physical) == row["physical_syndrome"] == 0
        assert parity_mask(physical, sector.logical_duals, model.popcount) == row["physical_logical"]
        conservative = (row["canonical_logical"] != 0 and row["physical_logical"] != 0 and
                        row["canonical_logical"] == row["physical_logical"])
        if conservative:
            conservative_occurrences += row["multiplicity"]
            retained.append({"sector": label, "selected_names": selected_names,
                             "input_indices": list(indices), "input_ids": [selectors[i]["mechanism_id"] for i in indices],
                             "multiplicity": row["multiplicity"], "canonical_replay": canonical_replay,
                             "physical_support": bit_positions(row["physical"]),
                             "physical_logical_parities": [((row["physical_logical"] >> i) & 1) for i in range(12)]})
        replayed += 1
    assert conservative_occurrences == summary["conservative_source_valid_occurrences"]
    assert sum(1 for row in eligible_rows if row["canonical_logical"] != 0 and
               row["physical_logical"] != 0 and row["canonical_logical"] == row["physical_logical"]) == \
           summary["unique_conservative_source_valid_results"]
    sector_results[label] = {
        "selector_count": expected_count,
        "triple_count": len(triples),
        "full_domain": math.comb(expected_count, 6),
        "canonical_syndrome_zero": canonical_count,
        "physical_syndrome_zero": physical_count,
        "combined_syndrome_zero": combined["count"],
        "eligible_unique_replayed": replayed,
        "eligible_occurrences": sum(row["multiplicity"] for row in eligible_rows),
        "conservative_valid_occurrences": conservative_occurrences,
        "summary_file_sha256": file_sha256(summary_path),
        "eligible_file_sha256": hashlib.sha256(eligible_raw).hexdigest(),
        "eligible_file_bytes": len(eligible_raw),
        "row_file_sha256": file_sha256(synthesis / f"order5_input/{label}.rows.bin"),
        "big_endian_count_rejected": True,
    }

domain_total = math.comb(125, 6) + math.comb(109, 6)
assert domain_total == 6_715_648_864
output = {
    "schema": "circdist-round100-exact-order6-mitm-validation-v1",
    "status": "PASS",
    "input_binding": {
        "selector_state_sha256": state["selector_state_sha256"],
        "source_schedule_sha256": candidate["compressed_schedule_sha256"],
        "row_input_metadata_sha256": file_sha256(synthesis / "order5_input/input_metadata.json"),
    },
    "full_domain_size": domain_total,
    "full_domain_streamed": False,
    "exact_reduced_domain_statement": (
        "For every sorted six-set i0<...<i5, the unique pair (i0,i1,i2),(i3,i4,i5) has max(lower)<min(upper). "
        "The six-set has zero canonical and physical syndrome exactly when these two triples have equal complete "
        "canonical-plus-physical syndrome vectors. Sorting all triples by that full vector and checking every separated "
        "equal-key pair therefore enumerates all and only potentially conservative-valid six-distinct tuples once."
    ),
    "small_n_bijection_controls": coverage_controls,
    "sector_results": sector_results,
    "retained_terms": retained,
    "retained_term_count": len(retained),
    "collision_controls": {
        "decision_key_words": 4,
        "decision_key_bits": 256,
        "meaningful_syndrome_bits": 144,
        "hash_used_for_decision": False,
        "checksums_used_for_decision": False,
        "full_named_result_words": 6,
    },
    "overflow_controls": {
        "largest_full_domain": max(math.comb(125, 6), math.comb(109, 6)),
        "uint64_max": (1 << 64) - 1,
        "binomials_cross_checked_with_python_arbitrary_precision": True,
        "every_reported_histogram_sums_to_its_exact_domain": True,
    },
    "endianness_controls": {
        "input_and_output_parsed_explicit_little_endian": True,
        "big_endian_row_count_differs_and_is_rejected": True,
        "unused_high_bits_zero": True,
    },
    "theorem": {
        "statement": (
            "On the reviewed post-iteration-136 frozen schedule, every potentially valid XOR of six distinct "
            "same-sector selectors from the 125 Xerr or 109 Zerr bases is covered exactly once by the exact MITM "
            "reduction, and every named-weight-1..10 result is replayed in canonical and physical semantics."
        ),
        "scope_exclusions": ["mixed sectors", "other selector bases", "other schedules", "seven or more distinct indices",
                             "arbitrary mechanisms outside the reviewed selector span"],
    },
    "seconds": round(time.time() - started, 6),
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "full_domain": domain_total,
                  "X_combined": sector_results["Xerr"]["combined_syndrome_zero"],
                  "Z_combined": sector_results["Zerr"]["combined_syndrome_zero"],
                  "retained": len(retained), "seconds": output["seconds"]}, sort_keys=True))
