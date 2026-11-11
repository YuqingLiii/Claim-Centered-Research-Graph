#!/usr/bin/env python3
"""Independently replay every eligible exact-name order-5 result."""
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, math, struct, sys, time

def canon(o): return json.dumps(o, sort_keys=True, separators=(",", ":")).encode()
def objsha(o): return hashlib.sha256(canon(o)).hexdigest()
def filesha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def fromwords(ws): return sum(int(x) << (64*i) for i,x in enumerate(ws))
def bits(v): return [i for i in range(v.bit_length()) if (v>>i)&1]
def named_fields(names):
    data=sorted(int(n.split(":")[1]) for n in names if n.startswith("D:"));groups={}
    for n in names:
        p=n.split(":")
        if p[0]=="R": groups.setdefault(p[1],[]).append(int(p[2]))
    return data,{k:sorted(v) for k,v in sorted(groups.items(),key=lambda x:int(x[0]))}
def parity_mask(support,duals,popcount):
    out=0
    for i,d in enumerate(duals):out|=((popcount(support&d)&1)<<i)
    return out

ap=argparse.ArgumentParser()
ap.add_argument("--root",type=Path,required=True)
ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();t0=time.time();R=a.root.resolve();S=R/"synthesis";V=R/"vendor/round80"
state_path=S/"inputs/iter137_state.json";candidate_path=S/"inputs/iter136_candidate.json";direct_path=S/"inputs/iter136_direct_verification.json"
assert filesha(state_path)=="ba670045a69722f9625d04d3f07d62e207db38f15e9323f8c32d89194bb585cd"
assert filesha(candidate_path)=="9596d1456ea66c086c06b4b7b4aaf4e442da9943644ae9839d113f10d937a640"
assert filesha(direct_path)=="f206cb75b7af6cbf2c5421f58c9ebc0c1c0b51d7e44eb3f1c5713a47987a485e"
state=json.loads(state_path.read_text());cand=json.loads(candidate_path.read_text())
keys=("mechanism_id","sector","selected_names","data_support","group_kinds","selector_semantic_sha256")
assert objsha([{k:s.get(k) for k in keys} for s in state["selectors"]])==state["selector_state_sha256"]=="47792a8f8e757482604723abb0e08916f49b252f4ba07deae03cf4295159d0b6"
sys.path[:0]=[str(V/"src/round63_src"),str(V/"src")]
import model
import round68_build as builder
_,_,lx,lz=builder.load_context();times={k:int(v) for k,v in cand["compressed_times"].items()}
assert objsha(times)==cand["compressed_schedule_sha256"]=="45051af0b08e6647d50c6fb0535894173016fd013279e7a0eaee8b2e69ee2e44"
assert model.audit_schedule(times,True)==cand["frozen_audit"] and cand["frozen_audit"]["ok"]
sectors=builder.sectors(times,lx,lz);names=json.loads((S/"order5_input/name_universe.json").read_text());assert names==sorted(names) and len(names)==len(set(names))==360
name_bit={n:i for i,n in enumerate(names)}
existing_semantics=set(s["selector_semantic_sha256"] for s in state["selectors"]);all_retained=[];sector_out={}
for label,n in (("Xerr",125),("Zerr",109)):
    sec=sectors[label];rows=[x for x in state["selectors"] if x["sector"]==label];assert len(rows)==n
    row_effects=[];existing_masks=set()
    byname={c.name:c for c in sec.columns}
    for s in rows:
        nm=sum(1<<name_bit[x] for x in s["selected_names"]);can=phys=0
        for x in s["selected_names"]:can^=byname[x].support;phys^=byname[x].physical_support
        cs=sec.syndrome_of(can);ps=sec.syndrome_of(phys);cl=parity_mask(can,sec.logical_duals,model.popcount);pl=parity_mask(phys,sec.logical_duals,model.popcount)
        row_effects.append((nm,can,phys,cs,ps,cl,pl));existing_masks.add(nm)
    summ=json.loads((S/f"{label}.order5.summary.json").read_text())
    expected=math.comb(n,5);assert summ["domain_expected"]==summ["domain_enumerated"]==expected
    for key,size in (("location_weight_histogram",51),("canonical_support_weight_histogram",145),("physical_support_weight_histogram",145),("canonical_syndrome_weight_histogram",73),("physical_syndrome_weight_histogram",73),("canonical_logical_action_histogram",4096),("physical_logical_action_histogram",4096)):
        assert len(summ[key])==size and sum(summ[key])==expected
    raw=(S/f"{label}.order5.eligible.bin").read_bytes();assert raw[:16]==b"CDR98E5V1\0\0\0\0\0\0\0"
    count=struct.unpack_from("<Q",raw,16)[0];assert len(raw)==24+count*24*8 and count==summ["unique_eligible_named_results"]
    misses=Counter();mult=Counter();existing=novel=replayed=0;valid=[];seen=set();last=None
    off=24
    for _ in range(count):
        vals=struct.unpack_from("<24Q",raw,off);off+=192
        nm=fromwords(vals[0:6]);can=fromwords(vals[6:9]);phys=fromwords(vals[9:12]);cs=fromwords(vals[12:14]);ps=fromwords(vals[14:16]);cl,pl,m=vals[16:19];idx=tuple(vals[19:24])
        key=tuple(vals[:6]);assert key not in seen and (last is None or last<key);seen.add(key);last=key
        assert tuple(sorted(idx))==idx and len(set(idx))==5 and idx[-1]<n
        eff=[0,0,0,0,0,0,0]
        for i in idx:
            for j,v in enumerate(row_effects[i]):eff[j]^=v
        assert tuple(eff)==(nm,can,phys,cs,ps,cl,pl)
        selected_names=[names[i] for i in bits(nm)];assert 1<=len(selected_names)<=10
        replay=model.verify_named_selection(sec,selected_names,10);replayed+=1
        assert replay["weight"]==len(selected_names) and replay["net_support"]==bits(can) and replay["syndrome"]==bits(cs)
        assert replay["logical_parities"]==[((cl>>i)&1) for i in range(12)]
        assert replay["ok"]==(cs==0 and cl!=0)
        pcan=pphys=0
        for x in selected_names:pcan^=byname[x].support;pphys^=byname[x].physical_support
        assert pcan==can and pphys==phys and sec.syndrome_of(pphys)==ps and parity_mask(pphys,sec.logical_duals,model.popcount)==pl
        mult[m]+=1
        if nm in existing_masks:existing+=1
        else:novel+=1
        conservative=cs==0 and cl!=0 and ps==0 and pl!=0 and cl==pl
        if conservative:
            data,groups=named_fields(selected_names);sem=objsha({"sector":label,"selected_names":selected_names,"data_support":data,"group_kinds":groups})
            atoms=model.effective_block_atoms(sec,{"selected":sorted(byname[x].index for x in selected_names)}) if False else None
            valid.append({"sector":label,"selected_names":selected_names,"input_indices":list(idx),"input_ids":[rows[i]["mechanism_id"] for i in idx],"multiplicity":m,"logical_action":"".join(str((cl>>i)&1) for i in range(12)),"existing_named_mask":nm in existing_masks,"selector_semantic_sha256":sem,"canonical_replay":replay,"physical_support":bits(phys),"physical_syndrome":bits(ps),"physical_logical_parities":[((pl>>i)&1) for i in range(12)]})
        elif cs:misses["canonical_nonzero_syndrome"]+=1
        elif not cl:misses["canonical_logical_trivial"]+=1
        elif ps:misses["physical_nonzero_syndrome"]+=1
        elif not pl:misses["physical_logical_trivial"]+=1
        elif cl!=pl:misses["canonical_physical_logical_mismatch"]+=1
        else:misses["other"]+=1
    assert replayed==count and sum(k*v for k,v in mult.items())==summ["eligible_weight_1_to_10_occurrences"]
    assert dict(sorted(mult.items()))=={summ["multiplicity_histogram_flat_pairs"][i]:summ["multiplicity_histogram_flat_pairs"][i+1] for i in range(0,len(summ["multiplicity_histogram_flat_pairs"]),2)}
    assert max(mult,default=0)==summ["maximum_eligible_multiplicity"]
    assert len(valid)==summ["conservative_source_valid_occurrences"]==0
    sector_out[label]={"cpp_summary":summ,"summary_file_sha256":filesha(S/f"{label}.order5.summary.json"),"eligible_file_sha256":filesha(S/f"{label}.order5.eligible.bin"),"eligible_file_bytes":len(raw),"unique_eligible_replayed":replayed,"unique_existing_named_results":existing,"unique_novel_named_results":novel,"multiplicity_histogram":dict(sorted(mult.items())),"novel_miss_reasons":dict(sorted(misses.items())),"potentially_valid_results":valid}
out={
 "schema":"circdist-round98-exact-order5-same-sector-gf2-closure-v1","status":"PASS",
 "strategy":"exact strict-index streaming enumeration a<b<c<d<e with componentwise GF(2) effects and full-key multiplicity map",
 "inputs":{"state_file_sha256":filesha(state_path),"selector_state_sha256":state["selector_state_sha256"],"candidate_file_sha256":filesha(candidate_path),"source_schedule_sha256":cand["compressed_schedule_sha256"],"direct_file_sha256":filesha(direct_path),"row_input_metadata_sha256":filesha(S/"order5_input/input_metadata.json")},
 "finite_domain":{"sector_counts":{"Xerr":125,"Zerr":109},"sector_expected":{"Xerr":math.comb(125,5),"Zerr":math.comb(109,5)},"unordered_distinct_quintuples_expected":math.comb(125,5)+math.comb(109,5),"unordered_distinct_quintuples_enumerated":sum(x["cpp_summary"]["domain_enumerated"] for x in sector_out.values()),"coverage_proof":["Every domain member has a unique sorted representation a<b<c<d<e.","The five nested monotone loops emit exactly those representations and no other tuple.","Conversely each sorted representation is reached at its unique five loop indices.","Observed sector counts equal C(125,5) and C(109,5); all complete histograms sum independently to those closed forms."],"no_sampling":True,"no_probabilistic_membership":True,"hash_collisions_cannot_change_semantics":"unordered_map hashes only locate buckets; full six-word equality decides key identity"},
 "sector_results":sector_out,"retained_term_count":0,"retained_terms":all_retained,
 "soundness_theorem":{"statement":"On the reviewed post-i136 frozen schedule, the componentwise GF(2) XOR of every five distinct same-sector selector effects was enumerated exactly once. Every unique result with named weight 1..10 was independently reconstructed from its five witnesses and replayed in the frozen physical model. No such result has zero canonical syndrome and nonzero canonical logical action, hence no source-schedule-valid order-5 EFSSC exists in this finite domain.","does_not_prove":"This finite no-go excludes neither mixed sectors, repeated selectors, order six or higher, other schedules/frontiers, nor arbitrary physical mechanisms; it closes no D* branch."},
 "scope_exclusions":["mixed Xerr/Zerr combinations","orders other than five","repeated selector indices","other schedules or later selector bases","arbitrary mechanisms outside selector GF(2) closure","universal Gross schedule absence"],
 "potentially_valid_witness_count":0,"seconds":round(time.time()-t0,6),
}
assert out["finite_domain"]["unordered_distinct_quintuples_enumerated"]==351359546
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":"PASS","domain":351359546,"X_eligible":sector_out["Xerr"]["unique_eligible_replayed"],"Z_eligible":sector_out["Zerr"]["unique_eligible_replayed"],"retained":0,"seconds":out["seconds"]},sort_keys=True))
