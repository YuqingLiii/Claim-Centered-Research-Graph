#!/usr/bin/env python3
"""
h4_party_swap_reduction.py

Exact lossless party-swap reduction for the full effective H4-invariant
degree-4 moment space.

tau swaps x_i <-> y_i.  Since A=A^T and K is defined using both the right
equality-face orbit and its swapped left-face orbit, tau preserves f and K.
Therefore any separating functional may be averaged over tau.

The script canonicalizes every one of the 746825 effective signed moment
coordinates under tau and writes:
  eff_global_ids        : global moment IDs used by (W-D)^2
  swap_eff_index        : partner effective index
  swap_sign             : +/-1 orientation sign
  even_rep_index        : one representative per tau-even coordinate
  even_expand_partner   : partner index
  even_expand_sign      : sign used when expanding reduced even coordinate

For a two-cycle i<->j with tau(theta_i)=s theta_j, an invariant functional
satisfies theta_j=s theta_i.  A +fixed singleton supplies one variable; a
-fixed singleton is forced to zero.

Exact expected census:
  + fixed  = 2004
  - fixed  = 1
  2-cycles = 372410
  even dim = 374414
  odd dim  = 372411.

Python 3.9+. numpy.
"""

import sys, json, hashlib, importlib.util, re, math
from pathlib import Path
import numpy as np

N=300
NV=600
ORDER=14400
EXPECTED_ACTION=(
 "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)


def die(x): raise SystemExit("ERROR: "+str(x))
def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha_bytes(b): return hashlib.sha256(b).hexdigest()


def main():
    if len(sys.argv)!=5:
        die("usage: python h4_party_swap_reduction.py SYSTEM NOGAP SPECDIR OUTDIR")
    system,nogap,specdir0,outdir0=sys.argv[1:]
    D=Path(specdir0); O=Path(outdir0); O.mkdir(parents=True,exist_ok=True)

    ng=load(nogap,"h4ng_swap")
    Q,Qd,G,Hd,ff=ng.structural_construction()
    sys0,els,gens,ash=ng.load_and_match_certified_action(system,G)
    if ash!=EXPECTED_ACTION: die("action hash mismatch")

    spec=json.load(open(D/"full_invariant_dual_spec.json"))
    offs={tuple(map(int,k.split(","))):int(v)
          for k,v in spec["moment_coordinates"]["global_offsets"].items()}

    perm=np.memmap(D/"h4_perm_u16.bin",dtype="<u2",mode="r",shape=(ORDER,N))
    sgn=np.memmap(D/"h4_sign_i8.bin",dtype="i1",mode="r",shape=(ORDER,N))

    # First certified group element sending each line to line 0.
    to0=[]
    for l in range(N):
        q=np.flatnonzero(perm[:,l]==0)
        if not len(q): die("line orbit not transitive")
        to0.append(int(q[0]))

    C=[[0]*5 for _ in range(301)]
    for n in range(301):
        C[n][0]=1
        for k in range(1,min(4,n)+1):
            C[n][k]=C[n-1][k]+C[n-1][k-1]
    def crank(s):
        return sum(C[int(v)][j+1] for j,v in enumerate(s))

    cats=[(2,0),(1,1),(0,2),(4,0),(3,1),(2,2),(1,3),(0,4)]
    maps={c:np.memmap(D/("moment_map_%d_%d.i32"%c),dtype="<i4",mode="r")
          for c in cats}

    product_ids=np.memmap(
        D/"product_map.id.i32",dtype="<i4",mode="r",shape=(1485,ORDER)
    )
    used=np.unique(np.asarray(product_ids).ravel())
    used=np.sort(used[used>=0].astype(np.int64))
    if len(used)!=746825: die("effective moment count mismatch")
    used_set=set(map(int,used))
    g2e={int(g):i for i,g in enumerate(used)}

    def canon(X,Y):
        X=sorted(map(int,X));Y=sorted(map(int,Y))
        a,b=len(X),len(Y)
        anchor=X[0] if a else Y[0]
        gi=to0[anchor];p=perm[gi];s=sgn[gi]
        ori=1;XX=[];YY=[]
        for x in X:XX.append(int(p[x]));ori*=int(s[x])
        for y in Y:YY.append(int(p[y]));ori*=int(s[y])
        XX.sort();YY.sort()
        if a:
            if XX[0]!=0:die("canonical X anchor failure")
            idx=crank([x-1 for x in XX[1:]])*C[300][b]+crank(YY)
        else:
            if YY[0]!=0:die("canonical Y anchor failure")
            idx=crank([y-1 for y in YY[1:]])
        code=int(maps[(a,b)][idx])
        if code==0:die("swap landed on nonorientable orbit")
        return offs[(a,b)]+abs(code)-1, ori*(1 if code>0 else -1)

    partner=np.empty(len(used),dtype=np.int32)
    ss=np.empty(len(used),dtype=np.int8)
    done={0}
    partner[g2e[0]]=g2e[0];ss[g2e[0]]=1

    for a,b in cats:
        fn=D/("moment_reps_%d_%d.txt"%(a,b))
        for line in open(fn):
            h,rest=line.strip().split(" X:",1);idx=int(h)
            xs,ys=rest.split(" Y:",1)
            X=[int(x) for x in re.findall(r"\d+",xs)]
            Y=[int(x) for x in re.findall(r"\d+",ys)]
            gid=offs[(a,b)]+idx
            if gid not in used_set: continue
            sgid,s=canon(Y,X)
            if sgid not in used_set:die("swap partner not effective")
            ei=g2e[gid];ej=g2e[sgid]
            partner[ei]=ej;ss[ei]=s
            done.add(gid)

    if len(done)!=len(used):die("not every effective moment mapped")
    for i in range(len(used)):
        j=int(partner[i])
        if int(partner[j])!=i or int(ss[i])*int(ss[j])!=1:
            die("swap is not signed involution")

    fp=fm=pairs=0
    reps=[];repp=[];repsign=[]
    for i in range(len(used)):
        j=int(partner[i]);s=int(ss[i])
        if j==i:
            if s==1:
                fp+=1;reps.append(i);repp.append(i);repsign.append(1)
            else:
                fm+=1
        elif i<j:
            pairs+=1;reps.append(i);repp.append(j);repsign.append(s)

    even=fp+pairs;odd=fm+pairs
    if (fp,fm,pairs,even,odd)!=(2004,1,372410,374414,372411):
        die("unexpected swap census")

    npz=O/"party_swap_effective.npz"
    np.savez_compressed(
        npz,
        eff_global_ids=used.astype(np.int32),
        swap_eff_index=partner,
        swap_sign=ss,
        even_rep_index=np.asarray(reps,dtype=np.int32),
        even_expand_partner=np.asarray(repp,dtype=np.int32),
        even_expand_sign=np.asarray(repsign,dtype=np.int8),
    )

    out={
      "status":"PROVED_LOSSLESS_PARTY_SWAP_REDUCTION",
      "action_sha256":ash,
      "effective_dimension":len(used),
      "swap_plus_fixed":fp,
      "swap_minus_fixed":fm,
      "swap_two_cycles":pairs,
      "swap_even_dimension":even,
      "swap_odd_dimension":odd,
      "equality_supported_kernel_dimension":28,
      "equality_kernel_even_dimension":14,
      "equality_kernel_odd_dimension":14,
      "sharp_rank_targets_if_equality_kernel_is_full":{
        "even":even-14,
        "odd":odd-14,
        "total":len(used)-28,
      },
      "why_lossless_for_feasibility":(
        "tau swaps x and y; A=A^T and the equality set contains both right "
        "and swapped-left face orbits, hence f and K are tau-stable. "
        "Average any separator with its tau-pullback."
      ),
      "npz_file":str(npz),
      "npz_sha256":hashlib.sha256(npz.read_bytes()).hexdigest(),
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    p=O/"party_swap_effective.json";p.write_bytes(raw)
    disp=dict(out);disp["output_path"]=str(p)
    disp["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp,indent=2,sort_keys=True))


if __name__=="__main__":main()
