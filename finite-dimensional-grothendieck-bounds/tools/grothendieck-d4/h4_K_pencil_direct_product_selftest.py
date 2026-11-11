#!/usr/bin/env python3
"""
h4_K_pencil_direct_product_selftest.py

Independent coefficient-level self-test for the canonical K-pencil cache.

It does NOT solve the SDP.  It verifies, for five nontrivial irreducible
blocks, that the group-Fourier block formula agrees exactly over GF(24001)
with direct Boolean multiplication of an explicitly assembled polynomial in
the full 180301-dimensional degree<=2 monomial basis.

The tested polynomial is a single transitive-orbit intertwiner:
    q = sum_g (u^T J rho_hat(g) v) (g m_O).

The direct side:
    expand q coefficient-by-coefficient in the Boolean monomial basis,
    multiply q*q by symmetric difference of supports,
    canonicalize every resulting support through the independently generated
    signed moment-orbit index, and evaluate a deterministic invariant moment
    vector theta.

The block side:
    use the exact product-map row for (O,O), the cached rho_hat representation,
    and Schur orthogonality:
        theta(q^2)
          = (|G|/d) (u^T J u)
             v^T J [sum_g ell(g)rho_hat(g)] v.
All arithmetic is in GF(24001).

This is a convention/indexing identity test, not a characteristic-zero PSD
test.  Combined with the builder's exact characteristic-zero representation
recipes and exact C*Z=0 canonicalization, it independently audits the
multiplication layer.

Usage:
  python h4_K_pencil_direct_product_selftest.py \
      SYSTEM_JSON h4_nogap_irrep_cache.py DUALBASE.py \
      FULL_DUAL_SPEC_DIR CANONICAL_CACHE_DIR
"""

import sys, json, hashlib, importlib.util, math
from pathlib import Path
import numpy as np

P = 24001
ORDER = 14400
N = 300
NV = 600
MON_DIM = 1 + NV + NV*(NV-1)//2

EXPECTED_ACTION_SHA = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_MANIFEST_SHA = (
    "41eaa1a24984bdc456ec325c9e45f6e0d989d86dadfcbb7e88db2e10fc04a86b"
)
TEST_BLOCKS = [1,2,6,9,20]


def die(x):
    raise SystemExit("ERROR: "+str(x))


def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for z in iter(lambda:f.read(1<<20),b""):
            h.update(z)
    return h.hexdigest()


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def choose_u(J):
    d=J.shape[0]
    for i in range(d):
        e=np.zeros(d,dtype=np.int64); e[i]=1
        if int(((e@J)%P)@e)%P:
            return e
    for i in range(d):
        for j in range(i+1,d):
            e=np.zeros(d,dtype=np.int64); e[i]=e[j]=1
            if int(((e@J)%P)@e)%P:
                return e
    die("could not find u with u^T J u nonzero")


def main():
    if len(sys.argv)!=6:
        die(
            "usage: python h4_K_pencil_direct_product_selftest.py "
            "SYSTEM NOGAP DUALBASE SPECDIR CACHEDIR"
        )
    system_path,nogap_path,dual_path,specdir0,cachedir0=sys.argv[1:]
    specdir=Path(specdir0); cachedir=Path(cachedir0)

    if sha(cachedir/"canonical_K_pencil_manifest.json")!=EXPECTED_MANIFEST_SHA:
        die("canonical manifest SHA mismatch")

    ng=load(nogap_path,"h4nogap_direct")
    base=load(dual_path,"h4dual_direct")
    # Import the operator only for its deterministic finite-field BFS helper.
    op_path=Path(__file__).with_name("h4_full_K_pencil_operator.py")
    if not op_path.exists():
        die("h4_full_K_pencil_operator.py must be beside this self-test")
    op=load(str(op_path),"h4op_direct")

    base.init_pairs()
    Q,Qdata,G,Hdata,ff=ng.structural_construction()
    system,els,gens,action_sha=ng.load_and_match_certified_action(system_path,G)
    if action_sha!=EXPECTED_ACTION_SHA:
        die("action hash mismatch")

    spec=json.load(open(specdir/"full_invariant_dual_spec.json"))
    offsets={
        tuple(map(int,k.split(","))):int(v)
        for k,v in spec["moment_coordinates"]["global_offsets"].items()
    }

    maps={}
    for a,b in [(2,0),(1,1),(0,2),(4,0),(3,1),(2,2),(1,3),(0,4)]:
        maps[(a,b)]=np.memmap(
            specdir/("moment_map_%d_%d.i32"%(a,b)),
            dtype="<i4", mode="r"
        )

    ids=np.memmap(
        specdir/"product_map.id.i32",
        dtype="<i4", mode="r", shape=(1485,ORDER)
    )
    sgn=np.memmap(
        specdir/"product_map.sgn.i8",
        dtype="i1", mode="r", shape=(1485,ORDER)
    )
    pairidx=op.parse_pairs(specdir/"product_map.pairs.txt")

    # Exact combinatorial rank helpers for supports of size <=4.
    C=[[0]*5 for _ in range(301)]
    for n in range(301):
        C[n][0]=1
        for k in range(1,min(4,n)+1):
            C[n][k]=C[n-1][k]+C[n-1][k-1]

    def crank(s):
        return sum(C[int(v)][j+1] for j,v in enumerate(s))

    # For canonicalizing a support, choose the first group element sending
    # its first x-line (or first y-line) to line 0.
    to0=[[] for _ in range(N)]
    for gi,(p,s) in enumerate(els):
        for i in range(N):
            if int(p[i])==0:
                to0[i].append(gi)

    def theta(mid):
        mid=int(mid)
        return (17+13*mid+3*(mid%17)**2)%P

    def moment(supp):
        supp=sorted(int(x) for x in supp)
        deg=len(supp)
        if deg==0:
            return theta(0)
        if deg&1:
            return 0
        X=sorted(v for v in supp if v<N)
        Y=sorted(v-N for v in supp if v>=N)
        a,b=len(X),len(Y)
        anchor=X[0] if a else Y[0]
        gi=to0[anchor][0]
        p,s=els[gi]
        orient=1
        XX=[]; YY=[]
        for x in X:
            XX.append(int(p[x])); orient*=int(s[x])
        for y in Y:
            YY.append(int(p[y])); orient*=int(s[y])
        XX.sort(); YY.sort()

        if a:
            idx=crank([x-1 for x in XX[1:]])*C[300][b]+crank(YY)
        else:
            idx=crank([y-1 for y in YY[1:]])

        code=int(maps[(a,b)][idx])
        if code==0:
            return 0
        mid=offsets[(a,b)]+abs(code)-1
        return orient*(1 if code>0 else -1)*theta(mid)%P

    results=[]

    for ir in TEST_BLOCKS:
        z=np.load(cachedir/("block_%02d.npz"%ir))
        meta=json.load(open(cachedir/("block_%02d.json"%ir)))
        d=int(meta["degree"])

        gmods=z["generator_modp"].astype(np.int64)
        R=op.build_rall_from_generators(list(gmods),G)
        Rhat=R[np.asarray(G["inv_idx"],dtype=np.int64)]
        J=z["bilinear_J_modp"].astype(np.int64)
        Vcat=z["V_modp"].astype(np.int64)

        # Use the smallest active orbit, except the trivial constant orbit.
        active=[r for r in meta["active_modules"] if int(r["orbit_size"])>1]
        rec=min(active,key=lambda r:(int(r["orbit_size"]),int(r["nonD_index"])))
        c0=int(rec["copy_start"]); c1=int(rec["copy_end"])
        rng=np.random.default_rng(20260828+ir)
        # Deterministic pseudorandom exact vector in the fixed-space copy.
        coeff=rng.integers(0,P,size=c1-c0,dtype=np.int64)
        if not np.any(coeff): coeff[0]=1
        v=(Vcat[:,c0:c1]@coeff)%P
        # Deterministic pseudorandom exact representation vector with nonzero J norm.
        u=None
        for _ in range(100):
            e=rng.integers(0,P,size=d,dtype=np.int64)
            qn=int(((e@J)%P)@e)%P
            if qn:
                u=e;break
        if u is None: u=choose_u(J)%P
        uJu=int(((u@J)%P)@u)%P
        if uJu==0: die("internal uJu zero")

        # Assemble q directly in the 180301-coordinate Boolean monomial basis.
        qcoef=np.zeros(MON_DIM,dtype=np.int64)
        uJ=(u@J)%P
        for g,(p,s) in enumerate(els):
            a=int((((uJ@Rhat[g])%P)@v))%P
            mid,os=base.act_mid(int(rec["rep_mid"]),p,s)
            qcoef[int(mid)]=(qcoef[int(mid)]+a*int(os))%P

        nz=np.flatnonzero(qcoef)
        if len(nz)==0:
            die("block %d direct q vanished"%ir)

        # Direct Boolean square.
        direct=0
        supports={int(i):set(base.mid_support(int(i))) for i in nz}
        for ii,i0 in enumerate(nz):
            i=int(i0); ci=int(qcoef[i])
            direct=(direct+ci*ci*theta(0))%P
            si=supports[i]
            for j0 in nz[ii+1:]:
                j=int(j0)
                mu=moment(si.symmetric_difference(supports[j]))
                direct=(direct+2*ci*int(qcoef[j])*mu)%P

        # Group-Fourier side.
        key=tuple(sorted((int(rec["nonD_index"]),int(rec["nonD_index"]))))
        pr=int(pairidx[key])
        ell=np.zeros(ORDER,dtype=np.int64)
        for g in range(ORDER):
            mid=int(ids[pr,g])
            ell[g]=0 if mid<0 else int(sgn[pr,g])*theta(mid)%P

        RF=Rhat.reshape(ORDER,d*d)
        # Here entries are canonical residues and the exact integer dot bound is
        # ORDER*(P-1)^2 < 2^53.
        Ff=ell.astype(np.float64).dot(RF.astype(np.float64))
        Fr=np.rint(Ff)
        if not np.array_equal(Ff,Fr):
            die("block %d Fourier dot not exact integral"%ir)
        if np.max(np.abs(Fr)) >= (1<<53):
            die("block %d Fourier dot exceeded 2^53"%ir)
        F=Fr.astype(np.int64).reshape(d,d)%P

        b=int((((((v@J)%P)@F)%P)@v))%P
        pred=(
            ORDER
            * pow(d,P-2,P)
            * uJu
            * b
        )%P

        if direct!=pred:
            die(
                "block %d direct/product mismatch: %d != %d"
                %(ir,direct,pred)
            )

        results.append({
            "gap_irrep_id":ir,
            "degree":d,
            "nonD_index":int(rec["nonD_index"]),
            "representative_id":int(rec["rep_mid"]),
            "orbit_size":int(rec["orbit_size"]),
            "q_nonzero_coefficients":int(len(nz)),
            "uTJu_mod_24001":int(uJu),
            "direct_L_q2_mod_24001":int(direct),
            "block_formula_L_q2_mod_24001":int(pred),
            "passed":True,
            "q_coefficient_sha256":hashlib.sha256(
                qcoef.astype("<u2").tobytes()
            ).hexdigest(),
        })

    out={
        "status":"DIRECT_BOOLEAN_PRODUCT_SELFTEST_PASSED",
        "field":"GF(24001)",
        "tested_blocks":TEST_BLOCKS,
        "test_count":len(results),
        "pseudorandom_seed_rule":"20260828 + gap_irrep_id",
        "moment_rule":"theta(k)=17+13k+3(k mod 17)^2 mod 24001",
        "identity_checked":(
            "direct coefficient-by-coefficient Boolean q^2 evaluation equals "
            "(|G|/d)(u^TJu)v^TJ[sum_g ell(g)rho_hat(g)]v"
        ),
        "results":results,
        "logical_scope":(
            "exact convention/indexing self-test; not a real PSD certificate"
        ),
    }

    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    outpath=cachedir/"direct_boolean_product_selftest.json"
    outpath.write_bytes(raw)
    disp=dict(out)
    disp["output_path"]=str(outpath)
    disp["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
