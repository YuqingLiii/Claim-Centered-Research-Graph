#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,sys,time

def canon(o):return json.dumps(o,sort_keys=True,separators=(",",":")).encode()
def sha_obj(o):return hashlib.sha256(canon(o)).hexdigest()
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def file_sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
ap=argparse.ArgumentParser()
ap.add_argument("--solver-log",type=Path,required=True);ap.add_argument("--cnf",type=Path,required=True)
ap.add_argument("--source",type=Path,required=True);ap.add_argument("--metadata",type=Path,required=True)
ap.add_argument("--frozen",type=Path,required=True);ap.add_argument("--assignment",type=Path,required=True)
ap.add_argument("--candidate",type=Path,required=True);ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();t0=time.time();S=load(a.source);M=json.loads(a.metadata.read_text())
lines=a.solver_log.read_text().splitlines();assert "s SATISFIABLE" in lines
signed=[]
for line in lines:
 if line.startswith("v "):signed += [int(x) for x in line.split()[1:] if x!="0"]
assert len(signed)==M["variables"] and {abs(x) for x in signed}==set(range(1,M["variables"]+1))
truth=bytearray(M["variables"]+1)
for x in signed:truth[abs(x)]=x>0
assert truth[M["constant_variable"]]
a.assignment.write_text("s SATISFIABLE\n"+"\n".join(
 "v "+" ".join(map(str,signed[i:i+20]))+(" 0" if i+20>=len(signed) else "")
 for i in range(0,len(signed),20))+"\n")
# Complete independent DIMACS assignment replay.
with a.cnf.open() as f:
 h=f.readline().split();nv,nc=map(int,h[2:]);assert [nv,nc]==[M["variables"],M["clauses"]]
 checked=0
 for line in f:
  clause=list(map(int,line.split()))[:-1];assert any(bool(truth[abs(x)])==(x>0) for x in clause)
  checked+=1
assert checked==nc
# Decode all primary words.
def word(bits):return sum((1<<i) for i,v in enumerate(bits) if truth[v])
raw={e:word(bits) for e,bits in M["time_bit_variables"].items()}
ext={e:word(bits) for e,bits in M["extrema_bit_variables"].items()}
assert len(raw)==864 and all(0<=v<864 for v in raw.values())
values=sorted(set(raw.values()));remap={v:i for i,v in enumerate(values)}
compressed={e:remap[v] for e,v in raw.items()}
# Source-native base audit independent of frozen Python implementation.
errors=[];conflicts=[]
for kind,checks in (("X",S["x_checks"]),("Z",S["z_checks"])):
 for c,row in enumerate(checks):
  ts=[raw[f"{kind}:{c}:{q}"] for q in row]
  if len(set(ts))!=6:conflicts.append([kind,c])
for q,row in enumerate(S["data_incidence"]):
 if len({raw[e] for e in row})!=6:conflicts.append(["data",q])
mc=[]
for o in S["overlaps"]:
 xa,zb=o["x_check"],o["z_check"];q0,q1=o["qubits"]
 if (raw[f"Z:{zb}:{q0}"]<raw[f"X:{xa}:{q0}"]) != (raw[f"Z:{zb}:{q1}"]<raw[f"X:{xa}:{q1}"]):
  mc.append([xa,zb])
xs=[raw[e] for e in S["edges"] if e.startswith("X:")];zs=[raw[e] for e in S["edges"] if e.startswith("Z:")]
assert ext=={"xmin":min(xs),"xmax":max(xs),"zmin":min(zs),"zmax":max(zs)}
interleaved=not(max(xs)<min(zs) or max(zs)<min(xs))
assert not conflicts and not mc and interleaved
block_hits=[]
for i,b in enumerate(S["blocks"]):
 if all(raw[x]<raw[y] for x,y in b["atoms"]):block_hits.append(i)
assert not block_hits
# Symbolically replay all exact EFSSCs from ranks and stored signatures.
respos=[set(x) for x in S["residual_positions"]]
def positions(kinds):
 z=set()
 for k in kinds:z.symmetric_difference_update(respos[int(k)])
 return z
selector_valid=[]
for s in S["selectors"]:
 sd=S["sector_definitions"][s["sector"]];kind=sd["edge_kind"];qs=[int(x) for x in sd["qubit_signatures"]]
 sig=0
 for q in s["data_support"]:sig^=qs[q]
 for cs,kinds in s["group_kinds"].items():
  c=int(cs);row=sd["checks"][c];order=sorted(row,key=lambda q:raw[f"{kind}:{c}:{q}"]);pos=positions(kinds)
  for i,q in enumerate(order):
   if i in pos:sig^=qs[q]
 valid=(sig & ((1<<72)-1))==0 and (sig>>72)!=0
 selector_valid.append(valid)
assert not any(selector_valid)
# Frozen-model independent implementation replay, including named faults.
P=a.frozen.resolve()
sys.path[:0]=[str(P/"src"/"round63_src"),str(P/"src")]
import model as FM
import round68_build as B
frozen_audit=FM.audit_schedule(compressed,True);assert frozen_audit["ok"] and frozen_audit["global_interleaved"]
px,pz,lx,lz=B.load_context();sectors=B.sectors(compressed,lx,lz)
named=[]
for s in S["selectors"]:
 v=FM.verify_named_selection(sectors[s["sector"]],s["selected_names"],10)
 named.append({"mechanism_id":s["mechanism_id"],"sector":s["sector"],"valid":v["ok"],
               "weight":v.get("weight"),"syndrome_weight":v.get("syndrome_weight"),
               "nontrivial":v.get("nontrivial")})
assert not any(x["valid"] for x in named)
# Rank compression preserves all equality and strict-order relations actually used.
order_pairs=set()
for b in S["blocks"]:
 for x,y in b["atoms"]:order_pairs.add((x,y))
for o in S["overlaps"]:
 xa,zb=o["x_check"],o["z_check"]
 for q in o["qubits"]:order_pairs.add((f"Z:{zb}:{q}",f"X:{xa}:{q}"))
for s in S["selectors"]:
 sd=S["sector_definitions"][s["sector"]];kind=sd["edge_kind"]
 for cs in s["group_kinds"]:
  c=int(cs);row=sd["checks"][c]
  for q in row:
   for r in row:
    if q!=r:order_pairs.add((f"{kind}:{c}:{q}",f"{kind}:{c}:{r}"))
assert all((raw[x]<raw[y])==(compressed[x]<compressed[y]) and
           (raw[x]==raw[y])==(compressed[x]==compressed[y]) for x,y in order_pairs)
candidate={
 "schema":"circdist-gross-finite-outer-sat-candidate-v2",
 "source_semantic_payload_sha256":S["semantic_payload_sha256"],
 "cnf_sha256":M["cnf_sha256"],"solver_log_sha256":file_sha(a.solver_log),
 "assignment_sha256":file_sha(a.assignment),"raw_times":raw,"compressed_times":compressed,
 "raw_schedule_sha256":sha_obj(raw),"compressed_schedule_sha256":sha_obj(compressed),
 "raw_used_layers":len(values),"compressed_layers":len(values),"raw_extrema":ext,
 "frozen_audit":frozen_audit,
}
a.candidate.write_text(json.dumps(candidate,indent=2,sort_keys=True)+"\n")
out={
 "schema":"circdist-gross-finite-outer-sat-replay-v2","status":"PASS",
 "solver_status":"SATISFIABLE","complete_assignment_variables":len(signed),
 "all_dimacs_clauses_satisfied":True,"dimacs_clauses_checked":checked,
 "raw_schedule_sha256":candidate["raw_schedule_sha256"],
 "compressed_schedule_sha256":candidate["compressed_schedule_sha256"],
 "raw_used_layers":len(values),"compressed_max_time":max(compressed.values()),
 "frozen_schedule_audit":frozen_audit,"reviewed_block_hits":len(block_hits),
 "efssc_symbolic_valid_selectors":sum(selector_valid),
 "efssc_named_frozen_valid_selectors":sum(x["valid"] for x in named),
 "rank_compression_pairs_checked":len(order_pairs),
 "assignment_sha256":candidate["assignment_sha256"],
 "candidate_sha256":file_sha(a.candidate),"seconds":round(time.time()-t0,6),
}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,sort_keys=True))
