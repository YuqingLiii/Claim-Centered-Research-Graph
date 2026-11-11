#!/usr/bin/env python3
from pathlib import Path
import argparse, gzip, hashlib, json, sys

def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()

def sha_obj(obj):
    return hashlib.sha256(canon(obj)).hexdigest()

def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == ".gz" else blob)

def signature(M, vector, detectors, duals):
    return sum(((M.popcount(vector & h) & 1) << i) for i, h in enumerate(detectors)) | sum(
        ((M.popcount(vector & h) & 1) << (72 + i)) for i, h in enumerate(duals)
    )

ap=argparse.ArgumentParser()
ap.add_argument("--round86",type=Path,required=True)
ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args()
R=a.round86.resolve(); P=R/"vendor"/"round80"
sys.path[:0]=[str(P/"src"/"round63_src"),str(P/"src")]
import model as M
import round68_build as B

state=json.loads((R/"continuation"/"final_state.json").read_text())
assert state["next_iteration"]==109 and state["started"] is False and len(state["selectors"])==134
assert state["selector_state_sha256"]=="9be75eba643ac167d5c51497ca8e5cd23eb1656f803a49cbd8e7f1285b004113"
assert state["final_formula_sha256"]=="94d404da1777ef108a2a508dc55ca0f3fda68bc489482a00337d9acb7317ac4d"
px,pz,lx,lz=B.load_context()
rx,_=B.global_single_records("Xerr",M.Xchecks,px,"X")
rz,_=B.global_single_records("Zerr",M.Zchecks,pz,"Z")
r62=load(P/"src"/"round62_cegar20.json.gz")
B.replay_round62_blocks(r62,lx,lz)
generalized=load(P/"restart"/"installed_generalized_terms_iteration102.json.gz")
dynamic=load(P/"restart"/"dynamic_blocks_iteration102.json.gz")
raw=load(P/"restart"/"full_raw_mechanisms_iteration102.json.gz")
registry=load(P/"restart"/"online_mechanism_registry_iteration102.json.gz")
semantic={
 "dynamic":sha_obj(dynamic),"generalized":sha_obj(generalized),
 "raw":sha_obj(raw),"registry":sha_obj(registry),
}
assert semantic==state["reviewed_base_semantic_sha256"]
assert len(rx)+len(rz)==1440 and len(r62["outer_blocks"])==20
assert generalized["term_count"]==len(generalized["terms"])==12820 and len(dynamic)==204
blocks=[]
for i,row in enumerate(rx+rz):
    blocks.append({"family":"unary","family_index":i,"source_id":f"r63-{i}",
                   "atoms":[[x[0],x[2]] for x in row["atoms"]]})
for i,row in enumerate(r62["outer_blocks"]):
    blocks.append({"family":"round62","family_index":i,"source_id":"r62-"+row["tag"],
                   "trace_sha256":row.get("trace_sha256"),"atoms":[[x[0],x[2]] for x in row["atoms"]]})
for i,row in enumerate(generalized["terms"]):
    blocks.append({"family":"generalized","family_index":i,"source_id":row["term_id"],
                   "trace_sha256":row.get("source_term_sha256"),"atoms":[[x[0],x[2]] for x in row["atoms"]]})
for i,row in enumerate(dynamic):
    blocks.append({"family":"dynamic","family_index":i,"source_id":f"dynamic-{i}-{row['sector']}",
                   "trace_sha256":row.get("mechanism_sha256"),"atoms":[[x[0],x[2]] for x in row["atoms"]]})
assert len(blocks)==14484 and all(x["atoms"] for x in blocks)
sector_defs={}
for label,kind,checks,det,duals in [
    ("Xerr","X",M.Xchecks,M.HZ,lz),
    ("Zerr","Z",M.Zchecks,M.HX,lx),
]:
    sector_defs[label]={
      "edge_kind":kind,
      "checks":checks,
      "detector_rows":[str(x) for x in det],
      "logical_duals":[str(x) for x in duals],
      "qubit_signatures":[str(signature(M,1<<q,det,duals)) for q in range(144)],
    }
selectors=[]
keep=("mechanism_id","source_iteration","sector","fault_count","selected_names","data_support",
      "group_kinds","source_schedule_sha256","origin","selector_semantic_sha256")
for row in state["selectors"]:
    entry={k:row[k] for k in keep if k in row}
    entry["source_iteration"]=row.get("source_iteration",row.get("iteration"))
    selectors.append(entry)
assert len(selectors)==134
data_incidence=[]
for q in range(M.N):
    data_incidence.append(
      [M.edge_key("X",c,q) for c in M.Xof[q]]+
      [M.edge_key("Z",c,q) for c in M.Zof[q]]
    )
assert all(len(x)==6 for x in data_incidence)
source={
 "schema":"circdist-gross-iteration109-finite-source-v1",
 "frozen_semantics":{
   "qubits":144,"checks_per_sector":72,"check_weight":6,"named_edges":864,
   "time_bound_exclusive":864,"time_bits":10,"mc_overlaps":648,
   "require_global_interleaving":True,"terminal_residual_convention":"frozen Round80/Round86 direct residual",
 },
 "bindings":{
   "round86_root_manifest_sha256":"94322390a648262e8cc035f8e843617f134fe2d29ff36191720b646c021c89ff",
   "round86_payload_manifest_sha256":"443b84ce18c568bdd6b88c4737d03b222b518897eecab787ffa1cc43718f182b",
   "round86_formula_sha256":state["final_formula_sha256"],
   "round86_normalized_ast_sha256":"6ac624f2acb35a6311034829970b4d2993fcdf208080898a8e1dbeff1dcb3c7d",
   "selector_state_sha256":state["selector_state_sha256"],
   "reviewed_base_semantic_sha256":semantic,
 },
 "edges":list(M.ALL_EDGES),
 "x_checks":M.Xchecks,
 "z_checks":M.Zchecks,
 "data_incidence":data_incidence,
 "overlaps":[{"x_check":a,"z_check":b,"qubits":list(sh)} for a,b,sh in M.OVERLAPS],
 "residual_positions":[list(x) for x in M.RES_POS],
 "blocks":blocks,
 "selectors":selectors,
 "sector_definitions":sector_defs,
 "expected":{
   "assertions":19016,"reviewed_blocks":14484,
   "block_family_counts":{"unary":1440,"round62":20,"generalized":12820,"dynamic":204},
   "selectors":134,"rank_expressions":852,"membership_expressions":2274,
 },
}
source["semantic_payload_sha256"]=sha_obj(source)
a.output.parent.mkdir(parents=True,exist_ok=True)
raw_bytes=json.dumps(source,indent=2,sort_keys=True).encode()+b"\n"
if a.output.suffix==".gz":
    a.output.write_bytes(gzip.compress(raw_bytes,compresslevel=9,mtime=0))
else:
    a.output.write_bytes(raw_bytes)
print(json.dumps({"status":"PASS","output":str(a.output),"bytes":a.output.stat().st_size,
                  "semantic_payload_sha256":source["semantic_payload_sha256"],
                  "blocks":len(blocks),"selectors":len(selectors)},sort_keys=True))
