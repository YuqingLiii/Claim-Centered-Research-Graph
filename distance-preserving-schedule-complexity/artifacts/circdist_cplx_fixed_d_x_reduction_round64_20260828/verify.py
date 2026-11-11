#!/usr/bin/env python3
"""Independent finite controls for the round-64 proof package.

No third-party packages, randomness, SAT solver, or repository imports are used.
"""
import json, sys
from itertools import combinations, product
from construction import *

checks=[]
def ok(name,cond,detail=None):
    if not cond: raise AssertionError(name+((": "+str(detail)) if detail is not None else ""))
    checks.append({"check":name,"status":"PASS","detail":detail})

def pairmask(b,u,i):
    a,bq=b.pair(i,u); return (1<<a)|(1<<bq)

def formal_audit(code):
    b=code.builder; qlab={}
    for pl in b.planes:
        for q,x in zip(pl['row'],pl['qlabels']): qlab[q]=x
    for ri,row in enumerate(code.rows):
        val=0
        for q in row: val ^= qlab[q]
        ok("formal map kills SX row %d"%ri,val==0)
    rb,piv=rref(code.hx,code.n)
    bypoint={}
    for i,pl in enumerate(b.planes):
        for u in (pl['u'],pl['v'],pl['u']^pl['v']):
            bypoint.setdefault(u,[]).append((i,b.label_at(i,u),pairmask(b,u,i)))
    pairs=0
    for u,a in bypoint.items():
        for (i,x,p),(j,y,q) in combinations(a,2):
            equal=in_span(p^q,rb,piv)
            ok("actual pair partition equals formal partition",equal==(x==y),{"u":u,"planes":[i,j]})
            pairs+=1
    return pairs

def gadget_truth(table,neg):
    # Candidate selections are the labels occurring at a point plus '*'.
    vals=set(range(4)); star=4; rel=set()
    for a,b,c in product(range(5),repeat=3):
        served=all(a==x or b==y or c==z for x,y,z in table)
        if served: rel.add((a,b))
    target={(0,1),(1,0)} if neg else {(0,0),(1,1)}
    ok(("NEGATE" if neg else "COPY")+" exact relation over larger alphabet",rel==target,sorted(rel))

def main():
    gadget_truth(COPY,False); gadget_truth(NEGATE,True)

    b=Builder(); one=b.build_formula(3,[((0,True),(1,True),(2,True))])
    ok("one-clause deterministic size",(one.n,len(one.rows),one.t)==(64,37,21),(one.n,len(one.rows),one.t))
    ok("one-clause CSS",one.css())
    ok("private-base columns are a cap",one.cap())
    ok("old HZ row weight observed",max(map(wt,one.hz))==22,max(map(wt,one.hz)))
    npairs=formal_audit(one)
    ok("all shared-point plane pairs classified",npairs>0,npairs)

    # The selected auxiliary syndrome e_i+e_j+u of every connector is unique.
    aux=[]
    for m in b.rowmeta:
        if m[0]=="connector": aux.append((1<<(b.P+b.planes[m[1]]['b']))^(1<<(b.P+b.planes[m[2]]['b']))^m[3])
    ok("connector selected auxiliary syndromes unique",len(aux)==len(set(aux)),len(aux))
    ok("connector selected syndromes avoid core point space",all(x>>b.P for x in aux))

    rep=repetition3(one)
    ok("three-copy repetition CSS",rep.css())
    ok("three-copy size",(rep.n,len(rep.rows))==(192,37+128),(rep.n,len(rep.rows)))
    ok("observed repeated HZ max weight",max(map(wt,rep.hz))==66,max(map(wt,rep.hz)))

    comp=companion(); dx,dz,k=comp.exact_distances()
    ok("G_neq3 CSS",comp.css())
    ok("G_neq3 exact distances and k",(dx,dz,k)==(4,3,2),(dx,dz,k))
    wit=find_companion_x_witness()
    ok("G_neq3 explicit X schedule",wit==(0,1,0,0,0),wit)

    # Reviewer Proposition-5 counterexample is present and is not denied.
    p5=prop5_counterexample(); rb,piv=rref(p5.hx,p5.n)
    ps=[(1<<(4*i))|(1<<(4*i+1)) for i in range(4)]
    ok("Proposition-5 counterexample CSS/cap",p5.css() and p5.cap())
    ok("Proposition-5 four-term relation exists",in_span(ps[0]^ps[1]^ps[2]^ps[3],rb,piv))
    ok("Proposition-5 relation has no pairwise merge",all(not in_span(a^b,rb,piv) for a,b in combinations(ps,2)))
    ok("Proposition-5 counterexample dX=4",p5.exact_distances()[0]==4,p5.exact_distances())

    # Old K4 route is attacked directly: it really is a domain-3 NO and is used
    # only as the fixed malformed-input output, not as the SAT reduction.
    k4=k4_no(); rb,piv=rref(k4.hx,k4.n)
    vals=[[split_value(k4,row,j) for j in range(3)] for row in k4.rows]
    ok("K4 cap/CSS/dX",k4.cap() and k4.css() and k4.exact_distances()[0]==4,k4.exact_distances())
    neq=all(vals[i][r][0]!=vals[j][s][0] or vals[i][r][1]==vals[j][s][1]
            for i,j in combinations(range(4),2) for r,s in product(range(3),repeat=2) if r!=s)
    # More direct exhaustive schedule decision is the actual control.
    sat=[ch for ch in product(range(3),repeat=4) if schedule_ok(k4,ch)]
    ok("K4 exhaustive domain-3 negative control",not sat,len(sat))
    ok("K4 repetition CSS",repetition3(k4).css())

    report={"verdict":"PASS","python":sys.version.split()[0],"checks":len(checks),"details":checks}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=="__main__": main()
