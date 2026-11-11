#!/usr/bin/env python3
"""Deterministic projectively exact CNF compiler for Gross iteration 109.

Primary words are ten-bit unsigned times. Every auxiliary gate is constrained by
an iff definition, so every primary assignment has a unique auxiliary extension.
"""
from pathlib import Path
import argparse, gzip, hashlib, json, shutil, time
from collections import Counter

def canon(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":")).encode()
def sha_obj(obj):
    return hashlib.sha256(canon(obj)).hexdigest()
def load(path):
    p=Path(path); b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def file_sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

class CNF:
    def __init__(self,body_path):
        self.body_path=Path(body_path)
        self.f=self.body_path.open("w",buffering=1<<20)
        self.nvars=0; self.nclauses=0
        self.names={}; self.gate_cache={}; self.lt_cache={}; self.eq_cache={}
        self.gate_stats=Counter(); self.clause_stats=Counter()
        self.definitions=[]; self.root_clauses={}
        self.T=self.var("constant:true")
        self.nclauses+=1; self.clause_stats["constant"]+=1; self.f.write(str(self.T)+" 0\n")
        cid=self.nclauses
        self.definitions.append({"var":self.T,"op":"constant_true","inputs":[],"clause_ids":[cid]})
    def close(self): self.f.close()
    def var(self,name=None):
        self.nvars+=1
        if name is not None:
            assert name not in self.names
            self.names[name]=self.nvars
        return self.nvars
    def add_clause(self,lits,family):
        out=[]; seen=set()
        for x in lits:
            x=int(x); assert x
            if x==self.T: return None
            if x==-self.T: continue
            if -x in seen: return None
            if x not in seen: seen.add(x); out.append(x)
        if not out:
            out=[-self.T]
        self.nclauses+=1; self.clause_stats[family]+=1
        self.f.write(" ".join(map(str,out))+" 0\n")
        if family.startswith("root:"): self.root_clauses[self.nclauses]=list(out)
        return self.nclauses
    def and2(self,a,b):
        if a==self.T:return b
        if b==self.T:return a
        if a==-self.T or b==-self.T:return -self.T
        if a==b:return a
        if a==-b:return -self.T
        key=("and",)+tuple(sorted((a,b)))
        if key in self.gate_cache:return self.gate_cache[key]
        v=self.var();self.gate_cache[key]=v;self.gate_stats["and"]+=1
        ids=[self.add_clause([-v,a],"def:and"),self.add_clause([-v,b],"def:and"),
             self.add_clause([v,-a,-b],"def:and")]
        self.definitions.append({"var":v,"op":"and","inputs":[a,b],"clause_ids":ids})
        return v
    def or2(self,a,b):
        if a==-self.T:return b
        if b==-self.T:return a
        if a==self.T or b==self.T:return self.T
        if a==b:return a
        if a==-b:return self.T
        key=("or",)+tuple(sorted((a,b)))
        if key in self.gate_cache:return self.gate_cache[key]
        v=self.var();self.gate_cache[key]=v;self.gate_stats["or"]+=1
        ids=[self.add_clause([v,-a],"def:or"),self.add_clause([v,-b],"def:or"),
             self.add_clause([-v,a,b],"def:or")]
        self.definitions.append({"var":v,"op":"or","inputs":[a,b],"clause_ids":ids})
        return v
    def xor2(self,a,b):
        if a==-self.T:return b
        if b==-self.T:return a
        if a==self.T:return -b
        if b==self.T:return -a
        if a==b:return -self.T
        if a==-b:return self.T
        key=("xor",)+tuple(sorted((a,b)))
        if key in self.gate_cache:return self.gate_cache[key]
        v=self.var();self.gate_cache[key]=v;self.gate_stats["xor"]+=1
        ids=[self.add_clause([-a,-b,-v],"def:xor"),
             self.add_clause([a,b,-v],"def:xor"),
             self.add_clause([a,-b,v],"def:xor"),
             self.add_clause([-a,b,v],"def:xor")]
        self.definitions.append({"var":v,"op":"xor","inputs":[a,b],"clause_ids":ids})
        return v
    def and_many(self,args):
        r=self.T
        for x in args:r=self.and2(r,x)
        return r
    def or_many(self,args):
        r=-self.T
        for x in args:r=self.or2(r,x)
        return r
    def xor_many(self,args,constant=False):
        r=self.T if constant else -self.T
        for x in args:r=self.xor2(r,x)
        return r
    def lt(self,a,b):
        a=tuple(a);b=tuple(b);assert len(a)==len(b)==10
        key=(a,b)
        if key in self.lt_cache:return self.lt_cache[key]
        r=-self.T
        for ai,bi in zip(a,b):
            less=self.and2(-ai,bi)
            eq=-self.xor2(ai,bi)
            r=self.or2(less,self.and2(eq,r))
        self.lt_cache[key]=r;self.gate_stats["comparators"]+=1
        return r
    def eq_word(self,a,b):
        a=tuple(a);b=tuple(b);key=(a,b)
        if key in self.eq_cache:return self.eq_cache[key]
        r=self.and_many([-self.xor2(x,y) for x,y in zip(a,b)])
        self.eq_cache[key]=r;self.eq_cache[(b,a)]=r;self.gate_stats["word_equalities"]+=1
        return r

ap=argparse.ArgumentParser()
ap.add_argument("--source",type=Path,required=True)
ap.add_argument("--cnf",type=Path,required=True)
ap.add_argument("--metadata",type=Path,required=True)
ap.add_argument("--assertion-map",type=Path,required=True)
ap.add_argument("--definitions",type=Path,required=True)
a=ap.parse_args(); t0=time.time()
S=load(a.source)
given=S.pop("semantic_payload_sha256")
assert sha_obj(S)==given
assert S["schema"].startswith("circdist-gross-iteration") and S["schema"].endswith("-finite-source-v1")
assert len(S["edges"])==864 and len(set(S["edges"]))==864
assert len(S["blocks"])==S["expected"]["reviewed_blocks"] and len(S["selectors"])==S["expected"]["selectors"]
assert S["frozen_semantics"]["time_bound_exclusive"]==864
S["semantic_payload_sha256"]=given
a.cnf.parent.mkdir(parents=True,exist_ok=True)
body=a.cnf.with_suffix(a.cnf.suffix+".body")
C=CNF(body)
time_words={}
for edge in S["edges"]:
    time_words[edge]=tuple(C.var(f"time:{edge}:bit:{i}") for i in range(10))
ext_words={name:tuple(C.var(f"extrema:{name}:bit:{i}") for i in range(10))
           for name in ("xmin","xmax","zmin","zmax")}
const_words={n:tuple(C.T if (n>>i)&1 else -C.T for i in range(10)) for n in (0,864)}
assertions=[]
def record(family,source_id,clause_ids,semantic,extra=None):
    kept=[x for x in clause_ids if x is not None]
    row={"assertion_index":len(assertions),"family":family,"source_id":source_id,
         "root_clause_ids":kept,"root_clauses":[C.root_clauses[x] for x in kept],"semantic":semantic}
    if extra:row.update(extra)
    assertions.append(row)
def unit(lit,family):
    return C.add_clause([lit],"root:"+family)

# 1,728 bound assertions in exact outer-constructor order.
for edge in S["edges"]:
    record("time_nonnegative",edge,[],"ten-bit unsigned primary word implies t>=0")
    lit=C.lt(time_words[edge],const_words[864])
    record("time_upper_bound",edge,[unit(lit,"time_upper_bound")],"t<864")

# 288 six-way Distinct assertions, each exactly pairwise unequal.
def distinct_assert(family,source_id,edges):
    assert len(edges)==6 and len(set(edges))==6
    ids=[]
    for i in range(6):
        for j in range(i+1,6):
            l=C.lt(time_words[edges[i]],time_words[edges[j]])
            r=C.lt(time_words[edges[j]],time_words[edges[i]])
            ids.append(C.add_clause([l,r],"root:distinct"))
    record(family,source_id,ids,"pairwise t_i!=t_j via (t_i<t_j) or (t_j<t_i)",
           {"edge_count":6,"pair_clauses":15})
for i,row in enumerate(S["x_checks"]):
    distinct_assert("x_ancilla_distinct",f"Xcheck:{i}",[f"X:{i}:{q}" for q in row])
for i,row in enumerate(S["z_checks"]):
    distinct_assert("z_ancilla_distinct",f"Zcheck:{i}",[f"Z:{i}:{q}" for q in row])
for q,row in enumerate(S["data_incidence"]):
    distinct_assert("data_distinct",f"data:{q}",row)

# 648 MC equalities.
for i,o in enumerate(S["overlaps"]):
    xa,zb=o["x_check"],o["z_check"];q0,q1=o["qubits"]
    l0=C.lt(time_words[f"Z:{zb}:{q0}"],time_words[f"X:{xa}:{q0}"])
    l1=C.lt(time_words[f"Z:{zb}:{q1}"],time_words[f"X:{xa}:{q1}"])
    ids=[C.add_clause([-l0,l1],"root:mc"),C.add_clause([l0,-l1],"root:mc")]
    record("mc_equivalence",f"overlap:{xa}:{zb}",ids,
           "(t_Z(q0)<t_X(q0)) iff (t_Z(q1)<t_X(q1))")

# 1,734 extrema/interleaving assertions, mirroring four add() calls and final pair.
xs=[e for e in S["edges"] if e.startswith("X:")]
zs=[e for e in S["edges"] if e.startswith("Z:")]
assert len(xs)==len(zs)==432
for label,word,edges,mode in [
    ("xmin",ext_words["xmin"],xs,"min"),
    ("xmax",ext_words["xmax"],xs,"max"),
    ("zmin",ext_words["zmin"],zs,"min"),
    ("zmax",ext_words["zmax"],zs,"max"),
]:
    for edge in edges:
        lit=-C.lt(time_words[edge],word) if mode=="min" else -C.lt(word,time_words[edge])
        record("extrema_inequality",f"{label}:{edge}",[unit(lit,"extrema_inequality")],
               f"{label}<={edge}" if mode=="min" else f"{label}>={edge}")
    eqlits=[C.eq_word(word,time_words[e]) for e in edges]
    cid=C.add_clause(eqlits,"root:extrema_attained")
    record("extrema_attained",label,[cid],"extremum equals at least one edge time",
           {"disjuncts":len(eqlits)})
lit=-C.lt(ext_words["xmax"],ext_words["zmin"])
record("global_interleaving","not_all_X_before_Z",[unit(lit,"global_interleaving")],"xmax>=zmin")
lit=-C.lt(ext_words["zmax"],ext_words["xmin"])
record("global_interleaving","not_all_Z_before_X",[unit(lit,"global_interleaving")],"zmax>=xmin")

# 14,484 reviewed order-region exclusions.
block_counts=Counter()
for i,b in enumerate(S["blocks"]):
    lits=[-C.lt(time_words[x],time_words[y]) for x,y in b["atoms"]]
    cid=C.add_clause(lits,"root:block:"+b["family"])
    block_counts[b["family"]]+=1
    record("reviewed_block",b["source_id"],[cid],"negation of conjunction of strict-order atoms",
           {"block_index":i,"block_family":b["family"],"atom_count":len(lits)})

# Exact fixed-selector semantic cuts.
respos=[set(x) for x in S["residual_positions"]]
rank_keys=set(); member_cache={}; member_keys=set()
def positions(kinds):
    out=set()
    for k in kinds: out.symmetric_difference_update(respos[int(k)])
    return tuple(sorted(out))
def member(sector,check,kinds,q):
    pos=positions(kinds);key=(sector,check,pos,q)
    member_keys.add(key)
    if key in member_cache:return member_cache[key]
    if not pos:
        member_cache[key]=-C.T;return -C.T
    if pos==tuple(range(6)):
        member_cache[key]=C.T;return C.T
    d=S["sector_definitions"][sector];kind=d["edge_kind"];row=d["checks"][check]
    inputs=[]
    target=f"{kind}:{check}:{q}"
    for r in row:
        if r!=q:inputs.append(C.lt(time_words[f"{kind}:{check}:{r}"],time_words[target]))
    assert len(inputs)==5
    rank_keys.add((sector,check,q))
    v=C.var(f"member:{sector}:{check}:{','.join(map(str,pos))}:{q}")
    ids=[]
    for mask in range(32):
        pc=bin(mask).count("1"); allowed=pc in pos
        mismatch=[(-x if (mask>>i)&1 else x) for i,x in enumerate(inputs)]
        ids.append(C.add_clause(mismatch+[v if allowed else -v],"def:rank_membership"))
    C.definitions.append({"var":v,"op":"rank_membership","inputs":inputs,"positions":list(pos),"clause_ids":ids})
    member_cache[key]=v
    return v

selector_roots=[]
for si,s in enumerate(S["selectors"]):
    sector=s["sector"];d=S["sector_definitions"][sector]
    qsig=[int(x) for x in d["qubit_signatures"]]
    data_sig=0
    for q in s["data_support"]:data_sig ^= qsig[int(q)]
    terms=[[] for _ in range(84)]
    for cs,kinds0 in sorted(s["group_kinds"].items(),key=lambda kv:int(kv[0])):
        check=int(cs);kinds=tuple(sorted(map(int,kinds0)))
        for q in d["checks"][check]:
            m=member(sector,check,kinds,q);sig=qsig[q]
            for bit in range(84):
                if (sig>>bit)&1:terms[bit].append(m)
    bits=[C.xor_many(terms[bit],bool((data_sig>>bit)&1)) for bit in range(84)]
    detector_zero=C.and_many([-x for x in bits[:72]])
    logical_nonzero=C.or_many(bits[72:])
    valid=C.and2(detector_zero,logical_nonzero)
    cid=unit(-valid,"efssc")
    selector_roots.append(valid)
    record("efssc_exclusion",s["mechanism_id"],[cid],
           "not(all 72 detector parities zero and at least one of 12 logical parities one)",
           {"selector_index":si,"sector":sector,"fault_count":s["fault_count"],
            "group_count":len(s["group_kinds"])})

assert len(assertions)==S["expected"]["assertions"],(len(assertions),S["expected"]["assertions"])
assert block_counts==Counter(S["expected"]["block_family_counts"])
assert len(rank_keys)==S["expected"]["rank_expressions"],(len(rank_keys),S["expected"]["rank_expressions"])
assert len(member_keys)==S["expected"]["membership_expressions"],(len(member_keys),S["expected"]["membership_expressions"])
C.close()
with a.cnf.open("wb") as out, body.open("rb") as inp:
    out.write(f"p cnf {C.nvars} {C.nclauses}\n".encode())
    shutil.copyfileobj(inp,out,1<<20)
body.unlink()
with a.assertion_map.open("w") as f:
    for row in assertions:f.write(json.dumps(row,sort_keys=True,separators=(",",":"))+"\n")
word_labels={tuple(v):"time:"+k for k,v in time_words.items()}
word_labels.update({tuple(v):"extrema:"+k for k,v in ext_words.items()})
word_labels.update({tuple(v):"constant:"+str(k) for k,v in const_words.items()})
lt_relations=[]
for (left,right),lit in C.lt_cache.items():
    assert left in word_labels and right in word_labels
    lt_relations.append([word_labels[left],word_labels[right],lit])
eq_relations=[]
for (left,right),lit in C.eq_cache.items():
    if word_labels[left] <= word_labels[right]:
        eq_relations.append([word_labels[left],word_labels[right],lit])
member_relations=[]
for key,lit in member_cache.items():
    sector,check,pos,q=key
    member_relations.append([sector,check,list(pos),q,lit])
definition_payload={
 "schema":"circdist-gross-iteration109-circuit-trace-v1",
 "constant_variable":C.T,"definitions":sorted(C.definitions,key=lambda x:x["var"]),
 "lt_relations":sorted(lt_relations),"eq_relations":sorted(eq_relations),
 "member_relations":sorted(member_relations),"selector_valid_literals":selector_roots,
}
a.definitions.write_bytes(gzip.compress((json.dumps(definition_payload,sort_keys=True,separators=(",",":"))+"\n").encode(),compresslevel=9,mtime=0))

metadata={
 "schema":"circdist-gross-iteration109-cnf-v1","status":"PASS",
 "source_semantic_payload_sha256":given,
 "source_file_sha256":file_sha(a.source),"cnf_sha256":file_sha(a.cnf),
 "assertion_map_sha256":file_sha(a.assertion_map),"definitions_sha256":file_sha(a.definitions),
 "variables":C.nvars,"clauses":C.nclauses,"assertions":len(assertions),
 "primary_edge_time_words":864,"primary_extrema_words":4,"bits_per_word":10,
 "constant_variable":C.T,
 "time_bit_variables":{e:list(time_words[e]) for e in S["edges"]},
 "extrema_bit_variables":{k:list(v) for k,v in ext_words.items()},
 "comparison_count":len(C.lt_cache),"word_equality_count":len(C.eq_cache)//2,
 "rank_expressions":len(rank_keys),"membership_expressions":len(member_keys),
 "gate_stats":dict(C.gate_stats),"clause_family_counts":dict(C.clause_stats),
 "block_family_counts":dict(block_counts),"selector_count":len(selector_roots),
 "compile_seconds":round(time.time()-t0,6),
 "equivalence_kind":"unique definitional extension; exact projection between bounded schedules and CNF models",
}
a.metadata.write_text(json.dumps(metadata,indent=2,sort_keys=True)+"\n")
print(json.dumps({k:metadata[k] for k in ("status","variables","clauses","assertions","comparison_count",
 "rank_expressions","membership_expressions","cnf_sha256","compile_seconds")},sort_keys=True))
