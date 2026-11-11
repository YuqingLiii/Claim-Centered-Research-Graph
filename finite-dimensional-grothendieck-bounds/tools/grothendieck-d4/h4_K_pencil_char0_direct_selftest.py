#!/usr/bin/env python3
"""
h4_K_pencil_char0_direct_selftest.py

Characteristic-zero direct Boolean multiplication self-test for the full
product/pencil indexing.

Uses the trivial H4 irrep and
    q = 7 Phi_900 - 3 Phi_601,
where
    Phi_m=(1/|H_m|) sum_g g m
with the signed monomial action.

The two orbit sizes are 300 and 600.  q is expanded directly in the
180301-coordinate Boolean degree<=2 basis with exact integer coefficients.

An unrestricted integer invariant moment assignment is
    theta_k = 17 + 13 k + 3 (k mod 17)^2.

The script computes L(q^2) in two independent exact ways:
  (1) coefficient-by-coefficient Boolean multiplication using symmetric
      difference of supports and the signed moment-orbit maps;
  (2) the Reynolds/product-table formula
      L(Phi_i Phi_j)
        = |G|/(|H_i||H_j|)
          sum_g L(m_i * g m_j).

The two Python integers/Fractions must agree exactly.

Python 3.9+.  No floating arithmetic is used in the equality.
"""

import sys,json,hashlib,importlib.util,math
from fractions import Fraction
from pathlib import Path
import numpy as np

ORDER=14400
N=300
NV=600
MON_DIM=1+NV+NV*(NV-1)//2
EXPECTED_ACTION_SHA=(
 "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)


def die(x): raise SystemExit("ERROR: "+str(x))


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    if len(sys.argv)!=5:
        die("usage: python h4_K_pencil_char0_direct_selftest.py SYSTEM NOGAP DUALBASE SPECDIR")
    system_path,nogap_path,dual_path,specdir0=sys.argv[1:]
    specdir=Path(specdir0)

    ng=load(nogap_path,"ng_char0_direct")
    base=load(dual_path,"base_char0_direct")
    base.init_pairs()
    Q,Qd,G,Hd,ff=ng.structural_construction()
    system,els,gens,action=ng.load_and_match_certified_action(system_path,G)
    if action!=EXPECTED_ACTION_SHA:die("action hash")

    spec=json.load(open(specdir/"full_invariant_dual_spec.json"))
    offsets={
      tuple(map(int,k.split(","))):int(v)
      for k,v in spec["moment_coordinates"]["global_offsets"].items()
    }
    maps={}
    for a,b in [(2,0),(1,1),(0,2),(4,0),(3,1),(2,2),(1,3),(0,4)]:
        maps[(a,b)]=np.memmap(
            specdir/("moment_map_%d_%d.i32"%(a,b)),
            dtype="<i4",mode="r"
        )
    ids=np.memmap(
        specdir/"product_map.id.i32",dtype="<i4",mode="r",
        shape=(1485,ORDER)
    )
    sgn=np.memmap(
        specdir/"product_map.sgn.i8",dtype="i1",mode="r",
        shape=(1485,ORDER)
    )
    pairidx={}
    for line in open(specdir/"product_map.pairs.txt"):
        r,i,j=map(int,line.split());pairidx[(i,j)]=r

    # locate non-D indices by representative IDs
    reps=json.load(open(specdir/"nonD_orbit_reps.json"))
    lookup={int(r["rep_mid"]):int(r["nonD_index"]) for r in reps}
    oi=lookup[900]; oj=lookup[601]

    # Stabilizer data directly from action.
    inds_i,chars_i=base.orbit_stabilizer(900,els)
    inds_j,chars_j=base.orbit_stabilizer(601,els)
    if any(int(x)!=1 for x in list(chars_i)+list(chars_j)):
        die("chosen trivial-irrep orbits do not have positive stabilizer character")
    Hi=len(inds_i); Hj=len(inds_j)
    if (Hi,Hj)!=(48,24):
        die("unexpected stabilizer orders")

    # exact combinadic helpers
    C=[[0]*5 for _ in range(301)]
    for n in range(301):
        C[n][0]=1
        for k in range(1,min(4,n)+1):
            C[n][k]=C[n-1][k]+C[n-1][k-1]
    def crank(s):
        return sum(C[int(v)][j+1] for j,v in enumerate(s))

    to0=[[] for _ in range(N)]
    for gi,(p,s) in enumerate(els):
        for x in range(N):
            if int(p[x])==0:to0[x].append(gi)

    def theta(k):
        k=int(k);return 17+13*k+3*(k%17)**2

    def moment(supp):
        supp=sorted(int(x) for x in supp);deg=len(supp)
        if deg==0:return theta(0)
        if deg&1:return 0
        X=sorted(v for v in supp if v<N)
        Y=sorted(v-N for v in supp if v>=N)
        a,b=len(X),len(Y)
        anchor=X[0] if a else Y[0]
        gi=to0[anchor][0];p,s=els[gi]
        orient=1;XX=[];YY=[]
        for x in X:XX.append(int(p[x]));orient*=int(s[x])
        for y in Y:YY.append(int(p[y]));orient*=int(s[y])
        XX.sort();YY.sort()
        if a:
            idx=crank([x-1 for x in XX[1:]])*C[300][b]+crank(YY)
        else:
            idx=crank([y-1 for y in YY[1:]])
        code=int(maps[(a,b)][idx])
        if code==0:return 0
        k=offsets[(a,b)]+abs(code)-1
        return orient*(1 if code>0 else -1)*theta(k)

    def orbit_poly(rep_mid,H):
        acc={}
        for p,s in els:
            mid,os=base.act_mid(rep_mid,p,s)
            acc[int(mid)]=acc.get(int(mid),0)+int(os)
        out={}
        for mid,v in acc.items():
            if v%H:die("orbit average coefficient not integral")
            q=v//H
            if q:out[mid]=q
        return out

    phi_i=orbit_poly(900,Hi)
    phi_j=orbit_poly(601,Hj)
    if len(phi_i)!=300 or len(phi_j)!=600:
        die("unexpected orbit support counts")

    q={}
    for m,v in phi_i.items():q[m]=q.get(m,0)+7*v
    for m,v in phi_j.items():q[m]=q.get(m,0)-3*v
    q={m:v for m,v in q.items() if v}
    nz=sorted(q)

    # Direct characteristic-zero Boolean multiplication.
    supports={m:set(base.mid_support(m)) for m in nz}
    direct=0
    for ii,m in enumerate(nz):
        cm=q[m]
        direct += cm*cm*theta(0)
        sm=supports[m]
        for n in nz[ii+1:]:
            direct += 2*cm*q[n]*moment(sm.symmetric_difference(supports[n]))

    def product_sum(a,b):
        key=tuple(sorted((a,b)));r=pairidx[key]
        z=0
        for g in range(ORDER):
            k=int(ids[r,g])
            if k>=0:z += int(sgn[r,g])*theta(k)
        return z

    Sii=product_sum(oi,oi)
    Sij=product_sum(oi,oj)
    Sjj=product_sum(oj,oj)

    reynolds=(
        Fraction(ORDER,Hi*Hi)*49*Sii
        + 2*Fraction(ORDER,Hi*Hj)*(7*-3)*Sij
        + Fraction(ORDER,Hj*Hj)*9*Sjj
    )
    if reynolds.denominator!=1:
        die("Reynolds result unexpectedly nonintegral")
    if direct!=reynolds.numerator:
        die("characteristic-zero direct/product mismatch")

    # deterministic coefficient hash
    arr=np.zeros(MON_DIM,dtype=np.int64)
    for m,v in q.items():arr[m]=v

    out={
      "status":"CHARACTERISTIC_ZERO_DIRECT_PRODUCT_SELFTEST_PASSED",
      "field":"Z subset Q(sqrt(5),i)",
      "polynomial":"q=7*Phi_900-3*Phi_601",
      "stabilizer_orders":[Hi,Hj],
      "q_nonzero_coefficients":len(nz),
      "q_coefficient_sha256":hashlib.sha256(arr.astype("<i8").tobytes()).hexdigest(),
      "theta_rule":"theta(k)=17+13k+3(k mod 17)^2 over Z",
      "direct_L_q2":str(direct),
      "reynolds_product_table_L_q2":str(reynolds.numerator),
      "exact_equal":True,
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    p=specdir/"char0_direct_product_selftest.json";p.write_bytes(raw)
    disp=dict(out);disp["output_path"]=str(p)
    disp["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp,indent=2,sort_keys=True))


if __name__=="__main__":main()
