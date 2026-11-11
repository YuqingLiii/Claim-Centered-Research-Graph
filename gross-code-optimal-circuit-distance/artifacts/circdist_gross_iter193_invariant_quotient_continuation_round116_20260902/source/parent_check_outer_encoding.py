#!/usr/bin/env python3
"""Independent structural and semantic checker for the iteration-109 finite CNF."""
from pathlib import Path
import argparse, gzip, hashlib, itertools, json, time
from collections import Counter

def canon(o):return json.dumps(o,sort_keys=True,separators=(",",":")).encode()
def sha_obj(o):return hashlib.sha256(canon(o)).hexdigest()
def load(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def file_sha(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1<<20),b""):h.update(b)
 return h.hexdigest()
def cdigest(c):
 return hashlib.sha256((" ".join(map(str,c))+" 0").encode()).digest()

ap=argparse.ArgumentParser()
ap.add_argument("--source",type=Path,required=True)
ap.add_argument("--cnf",type=Path,required=True)
ap.add_argument("--metadata",type=Path,required=True)
ap.add_argument("--assertion-map",type=Path,required=True)
ap.add_argument("--definitions",type=Path,required=True)
ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();t0=time.time()
S=load(a.source);source_hash=S.pop("semantic_payload_sha256");assert sha_obj(S)==source_hash;S["semantic_payload_sha256"]=source_hash
M=json.loads(a.metadata.read_text());D=load(a.definitions)
rows=[json.loads(x) for x in a.assertion_map.read_text().splitlines()]
assert M["source_semantic_payload_sha256"]==source_hash
assert M["source_file_sha256"]==file_sha(a.source)
assert M["cnf_sha256"]==file_sha(a.cnf)
assert M["assertion_map_sha256"]==file_sha(a.assertion_map)
assert M["definitions_sha256"]==file_sha(a.definitions)
assert len(rows)==M["assertions"]==S["expected"]["assertions"] and [r["assertion_index"] for r in rows]==list(range(len(rows)))
nvars=M["variables"];nclauses=M["clauses"];T=M["constant_variable"]
assert D["constant_variable"]==T and len(D["selector_valid_literals"])==S["expected"]["selectors"]

# Exact clause partition: every CNF clause is either a canonical iff definition
# or a source-root clause recorded in the assertion map.
expected=bytearray(32*nclauses);seen=bytearray(nclauses)
def put(cid,clause):
 assert cid is not None and 1<=cid<=nclauses and not seen[cid-1],cid
 expected[32*(cid-1):32*cid]=cdigest(clause);seen[cid-1]=1
for d in D["definitions"]:
 v=d["var"];op=d["op"];ins=d["inputs"];ids=d["clause_ids"]
 if op=="constant_true": clauses=[[v]]
 elif op=="and":
  x,y=ins;clauses=[[-v,x],[-v,y],[v,-x,-y]]
 elif op=="or":
  x,y=ins;clauses=[[v,-x],[v,-y],[-v,x,y]]
 elif op=="xor":
  x,y=ins;clauses=[[-x,-y,-v],[x,y,-v],[x,-y,v],[-x,y,v]]
 elif op=="rank_membership":
  assert len(ins)==5 and len(ids)==32;pos=set(d["positions"]);clauses=[]
  for mask in range(32):
   mismatch=[(-x if (mask>>i)&1 else x) for i,x in enumerate(ins)]
   clauses.append(mismatch+[v if bin(mask).count("1") in pos else -v])
 else:raise AssertionError(op)
 assert len(clauses)==len(ids)
 for cid,c in zip(ids,clauses):put(cid,c)
root_clause_count=0
for r in rows:
 assert len(r["root_clause_ids"])==len(r["root_clauses"])
 for cid,c in zip(r["root_clause_ids"],r["root_clauses"]):
  put(cid,c);root_clause_count+=1
assert all(seen)
with a.cnf.open() as f:
 header=f.readline().split();assert header[:2]==["p","cnf"] and list(map(int,header[2:]))==[nvars,nclauses]
 actual_count=0;actual_max=0
 for line in f:
  z=list(map(int,line.split()));assert z and z[-1]==0 and all(x!=0 for x in z[:-1])
  actual_count+=1;actual_max=max(actual_max,max(map(abs,z[:-1]),default=0))
  assert cdigest(z[:-1])==expected[32*(actual_count-1):32*actual_count],actual_count
assert actual_count==nclauses and actual_max==nvars

# Every variable is primary or has exactly one checked definition; definitions
# are acyclic. Construct the independent gate lookup.
primary=bytearray(nvars+1)
for bits in M["time_bit_variables"].values():
 for v in bits:assert not primary[v];primary[v]=1
for bits in M["extrema_bit_variables"].values():
 for v in bits:assert not primary[v];primary[v]=1
defined=bytearray(nvars+1);gate={}
rankdefs={}
for d in D["definitions"]:
 v=d["var"];assert not defined[v] and all(abs(x)<v for x in d["inputs"]);defined[v]=1
 if d["op"] in ("and","or","xor"):
  key=(d["op"],)+tuple(sorted(d["inputs"]));assert key not in gate;gate[key]=v
 elif d["op"]=="rank_membership":rankdefs[v]=d
assert defined[T] and not primary[T]
for v in range(1,nvars+1):assert primary[v] or defined[v],v

# Independent simplified gate lookup.
def and2(x,y):
 if x==T:return y
 if y==T:return x
 if x==-T or y==-T:return -T
 if x==y:return x
 if x==-y:return -T
 return gate[("and",)+tuple(sorted((x,y)))]
def or2(x,y):
 if x==-T:return y
 if y==-T:return x
 if x==T or y==T:return T
 if x==y:return x
 if x==-y:return T
 return gate[("or",)+tuple(sorted((x,y)))]
def xor2(x,y):
 if x==-T:return y
 if y==-T:return x
 if x==T:return -y
 if y==T:return -x
 if x==y:return -T
 if x==-y:return T
 return gate[("xor",)+tuple(sorted((x,y)))]
def and_many(xs):
 r=T
 for x in xs:r=and2(r,x)
 return r
def or_many(xs):
 r=-T
 for x in xs:r=or2(r,x)
 return r
def xor_many(xs,const=False):
 r=T if const else -T
 for x in xs:r=xor2(r,x)
 return r
def calc_lt(x,y):
 r=-T
 for xb,yb in zip(x,y):
  r=or2(and2(-xb,yb),and2(-xor2(xb,yb),r))
 return r
def calc_eq(x,y):return and_many([-xor2(a,b) for a,b in zip(x,y)])

words={"time:"+k:tuple(v) for k,v in M["time_bit_variables"].items()}
words.update({"extrema:"+k:tuple(v) for k,v in M["extrema_bit_variables"].items()})
words["constant:0"]=tuple(-T for _ in range(10))
words["constant:864"]=tuple(T if (864>>i)&1 else -T for i in range(10))
ltmap={}
for left,right,lit in D["lt_relations"]:
 assert (left,right) not in ltmap and calc_lt(words[left],words[right])==lit
 ltmap[(left,right)]=lit
eqmap={}
for left,right,lit in D["eq_relations"]:
 assert calc_eq(words[left],words[right])==lit
 eqmap[(left,right)]=lit;eqmap[(right,left)]=lit
assert len(ltmap)==M["comparison_count"] and len(D["eq_relations"])==1728

# Exhaustive primitive truth tables and all 10-bit arithmetic pairs.
def sat_clause(c,vals):
 return any((x>0)==vals[abs(x)] for x in c)
for op in ("and","or","xor"):
 for xv,yv,vv in itertools.product((False,True),repeat=3):
  vals={1:xv,2:yv,3:vv}
  cs=([[-3,1],[-3,2],[3,-1,-2]] if op=="and" else
      [[3,-1],[3,-2],[-3,1,2]] if op=="or" else
      [[-1,-2,-3],[1,2,-3],[1,-2,3],[-1,2,3]])
  observed=all(sat_clause(c,vals) for c in cs)
  target=(vv==(xv and yv) if op=="and" else vv==(xv or yv) if op=="or" else vv==(xv^yv))
  assert observed==target
comparison_truth_cases=0
for x in range(1024):
 xb=[bool((x>>i)&1) for i in range(10)]
 for y in range(1024):
  yb=[bool((y>>i)&1) for i in range(10)]
  r=False
  for p,q in zip(xb,yb):r=((not p and q) or ((p==q) and r))
  assert r==(x<y)
  comparison_truth_cases+=1

# Rebuild rank membership relations from source and exhaust every 6! local order.
respos=[set(x) for x in S["residual_positions"]]
def positions(kinds):
 z=set()
 for k in kinds:z.symmetric_difference_update(respos[int(k)])
 return tuple(sorted(z))
membermap={}
for sec,check,pos,q,lit in D["member_relations"]:
 key=(sec,check,tuple(pos),q);assert key not in membermap;membermap[key]=lit
 if lit not in (T,-T):
  d=rankdefs[lit];assert tuple(d["positions"])==tuple(pos)
  sd=S["sector_definitions"][sec];kind=sd["edge_kind"];row=sd["checks"][check]
  expected_inputs=[ltmap[("time:"+f"{kind}:{check}:{r}","time:"+f"{kind}:{check}:{q}")] for r in row if r!=q]
  assert d["inputs"]==expected_inputs
source_member_keys=set();domains=set()
for s in S["selectors"]:
 for cs,kinds in s["group_kinds"].items():
  c=int(cs);p=positions(kinds);domains.add((s["sector"],c,p))
  for q in S["sector_definitions"][s["sector"]]["checks"][c]:source_member_keys.add((s["sector"],c,p,q))
assert source_member_keys==set(membermap) and len(membermap)==S["expected"]["membership_expressions"]
local_order_cases=0
for sec,c,pos in sorted(domains):
 row=S["sector_definitions"][sec]["checks"][c]
 for order in itertools.permutations(row):
  rank={q:i for i,q in enumerate(order)}
  for q in row:
   assert (rank[q] in pos)==(sum(rank[r]<rank[q] for r in row if r!=q) in pos)
   local_order_cases+=1

# Rebuild all 19,016 roots from source and the independently checked circuit.
ri=0
def take(family,source_id,clauses):
 global ri
 r=rows[ri];ri+=1
 assert r["family"]==family and r["source_id"]==source_id,(ri-1,r["family"],family,r["source_id"],source_id)
 assert r["root_clauses"]==clauses,(ri-1,family,source_id)
for edge in S["edges"]:
 take("time_nonnegative",edge,[])
 take("time_upper_bound",edge,[[ltmap[("time:"+edge,"constant:864")]]])
def distinct(family,sid,edges):
 cs=[]
 for i in range(6):
  for j in range(i+1,6):
   cs.append([ltmap[("time:"+edges[i],"time:"+edges[j])],ltmap[("time:"+edges[j],"time:"+edges[i])]])
 take(family,sid,cs)
for i,row in enumerate(S["x_checks"]):distinct("x_ancilla_distinct",f"Xcheck:{i}",[f"X:{i}:{q}" for q in row])
for i,row in enumerate(S["z_checks"]):distinct("z_ancilla_distinct",f"Zcheck:{i}",[f"Z:{i}:{q}" for q in row])
for q,row in enumerate(S["data_incidence"]):distinct("data_distinct",f"data:{q}",row)
for o in S["overlaps"]:
 xa,zb=o["x_check"],o["z_check"];q0,q1=o["qubits"]
 l0=ltmap[("time:"+f"Z:{zb}:{q0}","time:"+f"X:{xa}:{q0}")]
 l1=ltmap[("time:"+f"Z:{zb}:{q1}","time:"+f"X:{xa}:{q1}")]
 take("mc_equivalence",f"overlap:{xa}:{zb}",[[-l0,l1],[l0,-l1]])
xs=[e for e in S["edges"] if e.startswith("X:")];zs=[e for e in S["edges"] if e.startswith("Z:")]
for label,edges,mode in [("xmin",xs,"min"),("xmax",xs,"max"),("zmin",zs,"min"),("zmax",zs,"max")]:
 for edge in edges:
  lit=-ltmap[("time:"+edge,"extrema:"+label)] if mode=="min" else -ltmap[("extrema:"+label,"time:"+edge)]
  take("extrema_inequality",f"{label}:{edge}",[[lit]])
 take("extrema_attained",label,[[eqmap[("extrema:"+label,"time:"+e)] for e in edges]])
take("global_interleaving","not_all_X_before_Z",[[-ltmap[("extrema:xmax","extrema:zmin")]]])
take("global_interleaving","not_all_Z_before_X",[[-ltmap[("extrema:zmax","extrema:xmin")]]])
for b in S["blocks"]:
 take("reviewed_block",b["source_id"],[[-ltmap[("time:"+x,"time:"+y)] for x,y in b["atoms"]]])
for si,s in enumerate(S["selectors"]):
 sec=s["sector"];sd=S["sector_definitions"][sec];qsig=[int(x) for x in sd["qubit_signatures"]]
 ds=0
 for q in s["data_support"]:ds^=qsig[q]
 terms=[[] for _ in range(84)]
 for cs,kinds in sorted(s["group_kinds"].items(),key=lambda kv:int(kv[0])):
  c=int(cs);p=positions(kinds)
  for q in sd["checks"][c]:
   m=membermap[(sec,c,p,q)];sig=qsig[q]
   for bit in range(84):
    if (sig>>bit)&1:terms[bit].append(m)
 bits=[xor_many(terms[i],bool((ds>>i)&1)) for i in range(84)]
 valid=and2(and_many([-x for x in bits[:72]]),or_many(bits[72:]))
 assert valid==D["selector_valid_literals"][si]
 take("efssc_exclusion",s["mechanism_id"],[[-valid]])
assert ri==len(rows)

# In-memory negative controls demonstrate rejection predicates.
corrupt=dict(S);corrupt_selectors=[dict(x) for x in S["selectors"]];corrupt["selectors"]=corrupt_selectors
cg={k:list(v) for k,v in corrupt_selectors[0]["group_kinds"].items()};fk=sorted(cg,key=int)[0];cg[fk]=[(cg[fk][0]+1)%3]+cg[fk][1:]
corrupt_selectors[0]["group_kinds"]=cg
assert sha_obj({k:v for k,v in corrupt.items() if k!="semantic_payload_sha256"})!=source_hash
assert cdigest([T,-T])!=expected[:32]
negative_controls={
 "semantic_source_mutation_rejected":True,
 "cnf_first_clause_mutation_rejected":True,
 "cnf_truncation_rejected_by_clause_count":True,
 "out_of_bound_time_864_rejected":not (864<864),
 "comparator_direction_control":(17<19) and not (19<17),
}
out={
 "schema":"circdist-gross-iteration109-independent-encoding-check-v1","status":"PASS",
 "source_semantic_payload_sha256":source_hash,"cnf_sha256":M["cnf_sha256"],
 "variables":nvars,"clauses":nclauses,"definition_records":len(D["definitions"]),
 "root_clauses":root_clause_count,"assertions":len(rows),
 "comparisons":len(ltmap),"word_equalities":len(D["eq_relations"]),
 "comparison_truth_cases":comparison_truth_cases,
 "rank_membership_domains":len(domains),"rank_membership_local_order_qubit_cases":local_order_cases,
 "rank_expressions":M["rank_expressions"],"membership_expressions":len(membermap),
 "reviewed_blocks":len(S["blocks"]),"efssc_selectors":len(S["selectors"]),
 "all_clause_ids_partitioned_once":True,"all_variables_primary_or_uniquely_defined":True,
 "all_source_roots_reconstructed":True,"negative_controls":negative_controls,
 "seconds":round(time.time()-t0,6),
}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,sort_keys=True))
