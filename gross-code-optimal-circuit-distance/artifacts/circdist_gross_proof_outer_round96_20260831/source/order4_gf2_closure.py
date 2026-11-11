#!/usr/bin/env python3
"""Exact same-sector order-4 GF(2) closure on the reviewed post-i136 frontier."""
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, math, sys, time


def canon(obj): return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
def objsha(obj): return hashlib.sha256(canon(obj)).hexdigest()
def filesha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def bits(mask): return [i for i in range(mask.bit_length()) if (mask >> i) & 1]
def bitstring(mask, n=12): return "".join(str((mask >> i) & 1) for i in range(n))


ap = argparse.ArgumentParser()
ap.add_argument("--state", type=Path, required=True)
ap.add_argument("--candidate", type=Path, required=True)
ap.add_argument("--direct", type=Path, required=True)
ap.add_argument("--vendor", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args(); t0 = time.time()

assert filesha(a.state) == "ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd"
assert filesha(a.candidate) == "9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640"
assert filesha(a.direct) == "f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e"
state = json.loads(a.state.read_text()); cand = json.loads(a.candidate.read_text()); direct = json.loads(a.direct.read_text())
assert state["next_iteration"] == 137 and state["started"] is False and state["stop"] is None
assert state["selector_count"] == len(state["selectors"]) == 234
state_keys = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
assert objsha([{k:s.get(k) for k in state_keys} for s in state["selectors"]]) == state["selector_state_sha256"] == "47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6"

sys.path[:0] = [str(a.vendor / "src/round63_src"), str(a.vendor / "src")]
import model
import round68_build as builder
_, _, lx, lz = builder.load_context()
times = {k:int(v) for k,v in cand["compressed_times"].items()}
assert objsha(times) == cand["compressed_schedule_sha256"] == "45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44"
assert model.audit_schedule(times, True) == cand["frozen_audit"] and cand["frozen_audit"]["ok"]
sectors = builder.sectors(times, lx, lz)

# A common name universe is used only to represent exact set symmetric difference.
names_by_sector = {label: [c.name for c in sectors[label].columns] for label in ("Xerr", "Zerr")}
assert len(names_by_sector["Xerr"]) == len(set(names_by_sector["Xerr"])) == 360
assert set(names_by_sector["Xerr"]) == set(names_by_sector["Zerr"])
name_universe = sorted(names_by_sector["Xerr"])
name_bit = {name:i for i,name in enumerate(name_universe)}

def parity_mask(support, duals):
    out = 0
    for i, dual in enumerate(duals): out |= ((model.popcount(support & dual) & 1) << i)
    return out

def named_fields(names):
    data = sorted(int(n.split(":")[1]) for n in names if n.startswith("D:"))
    groups = {}
    for n in names:
        p = n.split(":")
        if p[0] == "R": groups.setdefault(p[1], []).append(int(p[2]))
    groups = {k:sorted(v) for k,v in sorted(groups.items(), key=lambda x:int(x[0]))}
    return data, groups

def effect(label, selected_names):
    sec = sectors[label]; byname = {c.name:(j,c) for j,c in enumerate(sec.columns)}
    canonical = physical = 0; indices = []
    for name in selected_names:
        j, col = byname[name]; indices.append(j); canonical ^= col.support; physical ^= col.physical_support
    csyn = sec.syndrome_of(canonical); psyn = sec.syndrome_of(physical)
    clog = parity_mask(canonical, sec.logical_duals); plog = parity_mask(physical, sec.logical_duals)
    return canonical, physical, csyn, psyn, clog, plog, sorted(indices)

by_sector = {label:[] for label in ("Xerr", "Zerr")}
for index, selector in enumerate(state["selectors"]):
    label = selector["sector"]; assert label in by_sector
    # Inherited selectors preserve direct-column order, which is not lexical order.
    # GF(2) closure uses the exact set and therefore requires uniqueness, not sorting.
    selected = selector["selected_names"]; assert len(selected) == len(set(selected))
    data, groups = named_fields(selected)
    assert data == selector["data_support"] and groups == selector["group_kinds"]
    assert objsha({"sector":label,"selected_names":selected,"data_support":data,"group_kinds":groups}) == selector["selector_semantic_sha256"]
    nmask = sum(1 << name_bit[n] for n in selected)
    canonical, physical, csyn, psyn, clog, plog, indices = effect(label, selected)
    by_sector[label].append({"global_index":index,"selector":selector,"names":nmask,"canonical":canonical,"physical":physical,"csyn":csyn,"psyn":psyn,"clog":clog,"plog":plog,"indices":indices})

assert {k:len(v) for k,v in by_sector.items()} == {"Xerr":125,"Zerr":109}
expected_sector = {label:math.comb(len(rows),4) for label,rows in by_sector.items()}
assert expected_sector == {"Xerr":9691375,"Zerr":5563251}
assert sum(expected_sector.values()) == 15254626

sector_results = {}; all_retained = []; all_semantic = set(s["selector_semantic_sha256"] for s in state["selectors"])
for label in ("Xerr", "Zerr"):
    sec = sectors[label]; rows = by_sector[label]; n = len(rows)
    existing_masks = {r["names"] for r in rows}
    weight_hist = Counter(); canonical_support_hist = Counter(); physical_support_hist = Counter(); logical_valid_hist = Counter()
    seen = zero_location = zero_canonical = zero_physical = 0
    canonical_syndrome_zero = physical_syndrome_zero = 0
    canonical_logical_trivial = physical_logical_trivial = 0
    canonical_source_valid = physical_source_valid = conservative_source_valid = 0
    eligible = {}
    checksum_mod = 0; modulus_mask = (1 << 256) - 1
    left_pairs = []
    # Streaming MITM frontier.  Before c, left_pairs is exactly all (a,b) with a<b<c.
    for c in range(2, n-1):
        b = c - 1
        rb = rows[b]
        for ai in range(b):
            ra = rows[ai]
            left_pairs.append((ai,b,ra["names"]^rb["names"],ra["canonical"]^rb["canonical"],ra["physical"]^rb["physical"],ra["csyn"]^rb["csyn"],ra["psyn"]^rb["psyn"],ra["clog"]^rb["clog"],ra["plog"]^rb["plog"]))
        rc = rows[c]
        for d in range(c+1,n):
            rd = rows[d]
            rn = rc["names"] ^ rd["names"]; rcan = rc["canonical"] ^ rd["canonical"]; rphys = rc["physical"] ^ rd["physical"]
            rcsyn = rc["csyn"] ^ rd["csyn"]; rpsyn = rc["psyn"] ^ rd["psyn"]
            rclog = rc["clog"] ^ rd["clog"]; rplog = rc["plog"] ^ rd["plog"]
            for ai,bi,ln,lcan,lphys,lcsyn,lpsyn,lclog,lplog in left_pairs:
                seen += 1
                nm = ln ^ rn; can = lcan ^ rcan; phys = lphys ^ rphys
                csyn = lcsyn ^ rcsyn; psyn = lpsyn ^ rpsyn; clog = lclog ^ rclog; plog = lplog ^ rplog
                w = model.popcount(nm); cw = model.popcount(can); pw = model.popcount(phys)
                weight_hist[w] += 1; canonical_support_hist[cw] += 1; physical_support_hist[pw] += 1
                zero_location += (w == 0); zero_canonical += (can == 0); zero_physical += (phys == 0)
                canonical_syndrome_zero += (csyn == 0); physical_syndrome_zero += (psyn == 0)
                canonical_logical_trivial += (clog == 0); physical_logical_trivial += (plog == 0)
                cv = 1 <= w <= 10 and csyn == 0 and clog != 0
                pv = 1 <= w <= 10 and psyn == 0 and plog != 0
                conservative = cv and pv and clog == plog
                canonical_source_valid += cv; physical_source_valid += pv; conservative_source_valid += conservative
                if conservative: logical_valid_hist[bitstring(clog)] += 1
                checksum_mod = (checksum_mod + nm + (can << 1) + (phys << 2) + (ai+1)*3 + (bi+1)*5 + (c+1)*7 + (d+1)*11) & modulus_mask
                if 1 <= w <= 10:
                    row = eligible.get(nm)
                    effects = (can,phys,csyn,psyn,clog,plog)
                    if row is None:
                        eligible[nm] = {"multiplicity":1,"first_indices":[ai,bi,c,d],"effects":effects,"canonical_valid":cv,"physical_valid":pv,"conservative_valid":conservative}
                    else:
                        assert row["effects"] == effects
                        assert row["canonical_valid"] == cv and row["physical_valid"] == pv and row["conservative_valid"] == conservative
                        row["multiplicity"] += 1
    assert seen == expected_sector[label]
    assert len(left_pairs) == math.comb(n-2,2)
    assert zero_location == 0  # four distinct selector sets never cancel completely in this exact frontier

    unique_existing = unique_novel = unique_replayed = unique_source_valid = 0
    retained = []; miss = Counter(); multiplicity_hist = Counter(); max_mult = 0; max_mult_witness = None
    for nm,row in sorted(eligible.items()):
        multiplicity_hist[row["multiplicity"]] += 1
        if row["multiplicity"] > max_mult: max_mult = row["multiplicity"]; max_mult_witness = nm
        selected_names = [name_universe[i] for i in bits(nm)]
        replay = model.verify_named_selection(sec, selected_names, 10); unique_replayed += 1
        can,phys,csyn,psyn,clog,plog,indices = effect(label, selected_names)
        assert row["effects"] == (can,phys,csyn,psyn,clog,plog)
        assert replay["weight"] == len(selected_names) and replay["net_support"] == bits(can)
        assert replay["syndrome"] == bits(csyn) and replay["logical_parities"] == [((clog >> i)&1) for i in range(12)]
        assert replay["ok"] == row["canonical_valid"]
        if nm in existing_masks: unique_existing += 1; continue
        unique_novel += 1
        if not row["conservative_valid"]:
            if csyn: miss["canonical_nonzero_syndrome"] += 1
            elif not clog: miss["canonical_logical_trivial"] += 1
            elif psyn: miss["physical_nonzero_syndrome"] += 1
            elif not plog: miss["physical_logical_trivial"] += 1
            elif clog != plog: miss["canonical_physical_logical_mismatch"] += 1
            else: miss["other"] += 1
            continue
        unique_source_valid += 1
        data, groups = named_fields(selected_names)
        sem = objsha({"sector":label,"selected_names":selected_names,"data_support":data,"group_kinds":groups})
        assert sem not in all_semantic; all_semantic.add(sem)
        atoms = model.effective_block_atoms(sec, {"selected":indices}); assert model.block_holds(sec.times, atoms)
        first = row["first_indices"]
        retained.append({
            "mechanism_id": "", "sector":label, "fault_count":len(selected_names), "selected_names":selected_names,
            "data_support":data, "group_kinds":groups, "selector_semantic_sha256":sem,
            "source_iteration":136, "source_schedule_sha256":cand["compressed_schedule_sha256"],
            "source_times":times, "origin":"round96_exact_order4_same_sector_gf2",
            "first_input_indices":first, "first_input_ids":[rows[i]["selector"]["mechanism_id"] for i in first],
            "quadruple_multiplicity":row["multiplicity"], "canonical_replay":replay,
            "canonical_support":bits(can), "canonical_support_weight":model.popcount(can),
            "physical_support":bits(phys), "physical_support_weight":model.popcount(phys),
            "physical_syndrome":bits(psyn), "physical_logical_parities":[((plog>>i)&1) for i in range(12)],
            "physical_nontrivial":plog != 0, "canonical_physical_parities_equal":clog == plog,
            "source_atoms":atoms, "source_atom_count":len(atoms), "source_symbolic_validity":"True",
        })
    for j,row in enumerate(retained): row["mechanism_id"] = f"r96-order4-{label}-{j:05d}"
    all_retained.extend(retained)
    sector_results[label] = {
        "selector_count":n, "unordered_pairs":math.comb(n,2), "unordered_distinct_quadruples_expected":expected_sector[label],
        "unordered_distinct_quadruples_enumerated":seen, "canonical_left_pairs_final":len(left_pairs),
        "all_pair_pair_decompositions":math.comb(math.comb(n,2),2),
        "overlapping_pair_decompositions_excluded":3*math.comb(n,3),
        "noncanonical_disjoint_pairings_excluded":2*math.comb(n,4),
        "canonical_disjoint_pairing_retained":math.comb(n,4),
        "location_weight_histogram":dict(sorted(weight_hist.items())),
        "canonical_support_weight_histogram":dict(sorted(canonical_support_hist.items())),
        "physical_support_weight_histogram":dict(sorted(physical_support_hist.items())),
        "zero_location_results":zero_location, "zero_canonical_support_results":zero_canonical, "zero_physical_support_results":zero_physical,
        "canonical_syndrome_zero_results":canonical_syndrome_zero, "physical_syndrome_zero_results":physical_syndrome_zero,
        "canonical_logical_trivial_results":canonical_logical_trivial, "physical_logical_trivial_results":physical_logical_trivial,
        "canonical_source_valid_quadruples":canonical_source_valid, "physical_source_valid_quadruples":physical_source_valid,
        "conservative_source_valid_quadruples":conservative_source_valid,
        "conservative_logical_action_histogram":dict(sorted(logical_valid_hist.items())),
        "eligible_weight_1_to_10_with_multiplicity":sum(weight_hist[w] for w in range(1,11)),
        "unique_eligible_named_results":len(eligible), "unique_eligible_replayed":unique_replayed,
        "unique_existing_predicate_results":unique_existing, "unique_novel_eligible_results":unique_novel,
        "unique_novel_conservative_source_valid_retained":len(retained), "unique_novel_source_valid_counter":unique_source_valid,
        "novel_miss_reasons":dict(sorted(miss.items())),
        "multiplicity_histogram_for_unique_eligible_results":dict(sorted(multiplicity_hist.items())),
        "maximum_result_multiplicity":max_mult,
        "maximum_multiplicity_witness_names":[name_universe[i] for i in bits(max_mult_witness)] if max_mult_witness is not None else None,
        "enumeration_checksum_mod_2_256":f"{checksum_mod:064x}", "retained_terms":retained,
    }

# Cross-sector ambiguity: exhibit one exact name set with differing sector effects.
cross = None
for xr in by_sector["Xerr"]:
    for zr in by_sector["Zerr"]:
        nm = xr["names"] ^ zr["names"]
        if not nm: continue
        selected_names = [name_universe[i] for i in bits(nm)]
        xe = effect("Xerr", selected_names); ze = effect("Zerr", selected_names)
        if xe[:6] != ze[:6]:
            cross = {"x_input_id":xr["selector"]["mechanism_id"],"z_input_id":zr["selector"]["mechanism_id"],"selected_names":selected_names,
                     "Xerr":{"canonical_support":bits(xe[0]),"physical_support":bits(xe[1]),"syndrome":bits(xe[2]),"physical_syndrome":bits(xe[3]),"logical":bitstring(xe[4]),"physical_logical":bitstring(xe[5])},
                     "Zerr":{"canonical_support":bits(ze[0]),"physical_support":bits(ze[1]),"syndrome":bits(ze[2]),"physical_syndrome":bits(ze[3]),"logical":bitstring(ze[4]),"physical_logical":bitstring(ze[5])},
                     "conclusion":"mixed-sector XOR has no sector-independent effect and is excluded"}; break
    if cross: break
assert cross is not None

# Schedule globalization witness from an inherited exact selector.
schedule_counterexample = None
for selector in state["selectors"]:
    alt = selector.get("source_times")
    if not alt or alt == times: continue
    source_sectors = builder.sectors(alt, lx, lz)
    source_v = model.verify_named_selection(source_sectors[selector["sector"]], selector["selected_names"], 10)
    current_v = model.verify_named_selection(sectors[selector["sector"]], selector["selected_names"], 10)
    if source_v["ok"] and not current_v["ok"]:
        schedule_counterexample = {"selector_id":selector["mechanism_id"],"sector":selector["sector"],"selected_names":selector["selected_names"],
            "source_schedule_sha256":selector["source_schedule_sha256"],"source_verification":source_v,
            "iteration136_verification":current_v,"conclusion":"validity is schedule-local; retained terms remain dynamic exact EFSSC predicates"}; break
assert schedule_counterexample is not None

# Exact support-weight substitution witness from the checked i136 direct record.
weight_witness = None
for label in ("Xerr","Zerr"):
    mech = direct["sectors"][label]["mechanism"]
    if mech["fault_count"] != len(mech["canonical_replay"]["net_support"]):
        weight_witness = {"sector":label,"selected_names":mech["selected_names"],"named_location_weight":mech["fault_count"],
            "canonical_support_weight":len(mech["canonical_replay"]["net_support"]),"physical_support_weight":len(mech["physical_net_support"]),
            "conclusion":"neither canonical nor physical net-support weight may replace named elementary-fault weight"}; break
assert weight_witness is not None

for j,row in enumerate(all_retained):
    # Give a globally unique stable identifier while preserving sector-local index in provenance.
    row["mechanism_id"] = f"r96-order4-{j:05d}-{row['sector']}"

out = {
    "schema":"circdist-round96-exact-order4-same-sector-gf2-closure-v1", "status":"PASS",
    "strategy":"exact streaming meet-in-the-middle over canonical disjoint pair split (a,b)|(c,d) with a<b<c<d",
    "inputs":{"state_file_sha256":filesha(a.state),"selector_state_sha256":state["selector_state_sha256"],"candidate_file_sha256":filesha(a.candidate),
              "candidate_schedule_sha256":cand["compressed_schedule_sha256"],"direct_file_sha256":filesha(a.direct)},
    "finite_domain":{"selector_count":234,"sector_counts":{"Xerr":125,"Zerr":109},"sector_expected":expected_sector,
        "unordered_distinct_quadruples_expected":sum(expected_sector.values()),
        "unordered_distinct_quadruples_enumerated":sum(x["unordered_distinct_quadruples_enumerated"] for x in sector_results.values()),
        "coverage_proof":["Every domain member has unique sorted indices a<b<c<d.","The streaming left bucket before c contains exactly every pair a<b<c.","Pairing each bucket row with each c<d emits that quadruple once.","The observed per-sector counts equal C(125,4) and C(109,4); cross-sector and repeated-index tuples are outside the declared domain."],
        "no_sampling":True,"weight_cap_for_candidate_predicates":10},
    "sector_results":sector_results,
    "retained_term_count":len(all_retained), "retained_terms":all_retained,
    "audits":{"zero_support_and_logical_trivial":"tracked independently for all enumerated quadruples and replayed for every unique weight<=10 result",
              "cross_sector_ambiguity":cross,"overlapping_pair_decompositions":{"policy":"only canonical disjoint split is enumerated","per_sector_counts_match_closed_forms":True},
              "multiplicity":"all eligible exact-name result multiplicities counted; one semantic predicate retained per novel result",
              "schedule_globalization":schedule_counterexample,"support_weight_substitution":weight_witness,
              "semantic_predicate_dedup":"sector plus exact selected names/data/group fields; all hashes collision-free against 234 inherited selectors and each retained term"},
    "soundness_theorem":{"statement":"Within one fixed CSS sector and one frozen schedule, each named location is a GF(2) column. The sum of four selector name sets is their exact symmetric difference. Replaying that distinct-name set proves its actual named weight, canonical and physical support, detector syndrome and logical action. A novel result is retained only when weight is 1..10, both syndromes vanish, both logical actions are equal and nonzero, and its dynamic outer antecedent holds on the source schedule.",
        "does_not_prove":"No-go counts outside retained positives do not exhaust arbitrary mechanisms, mixed-sector combinations, repeated-selector algebra, closure orders other than four, or schedules other than the tested source; no D* branch closes."},
    "seconds":round(time.time()-t0,6),
}
a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":"PASS","domain":out["finite_domain"]["unordered_distinct_quadruples_enumerated"],"retained":len(all_retained),
                  "X_unique_eligible":sector_results["Xerr"]["unique_eligible_named_results"],"Z_unique_eligible":sector_results["Zerr"]["unique_eligible_named_results"],"seconds":out["seconds"]},sort_keys=True))
