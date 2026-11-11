#!/usr/bin/env python3
"""
h4_K_pencil_matrixfree.py

Matrix-free evaluator for the canonical 20 K-compressed pencils.

The characteristic-zero pencil is the exact object described in the canonical
cache:
  field K=Q(sqrt(5),i),
  rho_hat(g)=rho_struct(g^{-1}),
  B_OO'(theta)=V_O^* H [sum_g sigma(g)theta[kappa(g)]rho_hat(g)] V_O',
  M_rho(theta)=Z_exact^* B_rho(theta) Z_exact,
  Z_F=I, Z_P=-C_exact[R,P]^{-1}C_exact[R,F].

The cache serializes:
  - exact K generator numerators + common denominator;
  - exact Hermitian metric;
  - exact V numerator columns;
  - the canonical pivot rows/columns defining Z_exact;
  - the exact recipes/hashes needed to regenerate rho_hat(g), C_exact, Z_exact.

This executable evaluates the exact REDUCTION of that pencil in GF(24001).
It is the backend used for exact rank/indexing checks.  It must NOT be used
as a real PSD test.

Subcommands
-----------
  info CACHEDIR

  eval-modp BLOCK_OR_ALL THETA SYSTEM NOGAP SPECDIR CACHEDIR OUTDIR

THETA may be:
  * JSON object {"moment_id":"integer", ...} (sparse), or
  * .npy one-dimensional integer array indexed by global moment id.

The evaluator never constructs the 1,569,415 x 746,825 coefficient matrix.
For each orbit-module pair it gathers
  ell(g)=sigma(g)theta[kappa(g)]
from the 21,384,000-record product table, Fourier-transforms ell against
rho_hat(g), forms the fixed-space block, and compresses by Z.

All finite-field Fourier dot products are accelerated through float64 ONLY
when the absolute integer sum is <2^53.  The result is required to be
bitwise integral before conversion back to GF(24001), exactly as in the
certified complete-K calculation.

Python 3.9+.
"""

import sys, json, hashlib, importlib.util
from pathlib import Path
import numpy as np

P=24001
ORDER=14400
EXPECTED_MANIFEST_SHA=(
    "41eaa1a24984bdc456ec325c9e45f6e0d989d86dadfcbb7e88db2e10fc04a86b"
)
EXPECTED_ACTION_SHA=(
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)


def die(x):
    raise SystemExit("ERROR: "+str(x))


def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for z in iter(lambda:f.read(1<<20),b""):
            h.update(z)
    return h.hexdigest()


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def mm(A,B):
    """Exact small GF(p) matrix multiply with overflow-safe modular staging."""
    A=np.asarray(A,dtype=np.int64)%P
    B=np.asarray(B,dtype=np.int64)%P
    # inner dimensions here <= 914. Worst raw int64 dot could overflow,
    # so use blocks whose absolute bound is <2^60.
    k=A.shape[1]
    out=np.zeros((A.shape[0],B.shape[1]),dtype=np.int64)
    chunk=max(1,min(k,(1<<50)//((P-1)*(P-1)*max(1,min(A.shape[0],B.shape[1])))))
    # The extra dimension factor in that bound is conservative; modularize
    # every chunk.
    chunk=max(1,min(chunk,64))
    for lo in range(0,k,chunk):
        hi=min(k,lo+chunk)
        out=(out+A[:,lo:hi]@B[lo:hi,:])%P
    return out


def mv_quad(v,J,F):
    x=(np.asarray(v,dtype=np.int64)@np.asarray(J,dtype=np.int64))%P
    x=(<email-redacted>(F,dtype=np.int64))%P
    return (<email-redacted>(v,dtype=np.int64))%P


def parse_pairs(path):
    d={}
    for line in open(path):
        r,i,j=map(int,line.split())
        d[(i,j)]=r
    return d


def read_theta(path):
    p=Path(path)
    if p.suffix.lower()==".npy":
        a=np.load(p)
        if a.ndim!=1:
            die("dense theta .npy must be one-dimensional")
        return ("dense",np.asarray(a,dtype=np.int64)%P)
    x=json.load(open(p))
    if not isinstance(x,dict):
        die("sparse theta JSON must be an object moment_id -> integer")
    return ("sparse",{int(k):int(v)%P for k,v in x.items() if int(v)%P})


def exact_fourier(ell,Rflat):
    """
    ell and Rflat are canonical residues in [0,p-1].
    ORDER*(p-1)^2 = 8.2944e12 < 2^53.
    """
    ell=np.asarray(ell,dtype=np.int64)%P
    Rflat=np.asarray(Rflat,dtype=np.int64)%P
    bound=ORDER*(P-1)*(P-1)
    if bound >= (1<<53):
        die("global exact float-dot bound failed")
    X=ell.astype(np.float64).dot(Rflat.astype(np.float64))
    R=np.rint(X)
    if not np.array_equal(X,R):
        die("finite-field Fourier dot was not an exact integer")
    if np.max(np.abs(R)) >= (1<<53):
        die("finite-field Fourier result exceeded 2^53")
    return R.astype(np.int64)%P


def info(cachedir):
    c=Path(cachedir)
    manpath=c/"canonical_K_pencil_manifest.json"
    if sha(manpath)!=EXPECTED_MANIFEST_SHA:
        die("manifest SHA mismatch")
    m=json.load(open(manpath))
    out={
        "status":"CANONICAL_MATRIX_FREE_OPERATOR_READY",
        "manifest_sha256":EXPECTED_MANIFEST_SHA,
        "characteristic_zero_field":m["field_exact"],
        "contragredient_convention":m["contragredient_convention"],
        "exact_pencil":m["exact_pencil"],
        "Z_exact_generation":m["Z_exact_generation"],
        "normalization":m["normalization"],
        "block_count":m["block_count"],
        "total_symmetric_block_coordinates":m["total_symmetric_block_coordinates"],
        "effective_moment_coordinates_pre_K":m["effective_moment_coordinates_pre_K"],
        "rank_status":m["rank_of_moment_to_K_compressed_map"],
    }
    print(json.dumps(out,indent=2,sort_keys=True))


def evaluate_block(ir,theta_kind,theta,ng,G,ids,sgn,pairidx,cachedir):
    meta=json.load(open(cachedir/("block_%02d.json"%ir)))
    z=np.load(cachedir/("block_%02d.npz"%ir))
    d=int(meta["degree"])
    mWD=int(meta["m_W_minus_D"])
    mK=int(meta["m_K"])

    gmods=z["generator_modp"].astype(np.int64)
    # The operator builder and this evaluator are stored side by side.
    op_path=Path(__file__).with_name("h4_full_K_pencil_operator.py")
    if not op_path.exists():
        die("h4_full_K_pencil_operator.py must be beside evaluator")
    op=load(str(op_path),"h4op_eval_%d"%ir)
    Rstruct=op.build_rall_from_generators(list(gmods),G)
    Rhat=Rstruct[np.asarray(G["inv_idx"],dtype=np.int64)]
    RF=Rhat.reshape(ORDER,d*d)

    J=z["bilinear_J_modp"].astype(np.int64)
    Vcat=z["V_modp"].astype(np.int64)
    Z=z["Z_modp"].astype(np.int64)
    active=meta["active_modules"]

    B=np.zeros((mWD,mWD),dtype=np.int64)

    for ai,Oi in enumerate(active):
        si=slice(int(Oi["copy_start"]),int(Oi["copy_end"]))
        Vi=Vcat[:,si]
        Ti=(Vi.T@J)%P

        for aj in range(ai,len(active)):
            Oj=active[aj]
            sj=slice(int(Oj["copy_start"]),int(Oj["copy_end"]))
            Vj=Vcat[:,sj]
            key=tuple(sorted((int(Oi["nonD_index"]),int(Oj["nonD_index"]))))
            pr=int(pairidx[key])
            mids=np.asarray(ids[pr])
            ss=np.asarray(sgn[pr],dtype=np.int64)

            if theta_kind=="sparse":
                ell=np.zeros(ORDER,dtype=np.int64)
                for mid,val in theta.items():
                    q=np.flatnonzero(mids==mid)
                    if len(q):
                        ell[q]=(ss[q]*val)%P
            else:
                valid=(mids>=0)
                ell=np.zeros(ORDER,dtype=np.int64)
                mmid=mids[valid].astype(np.int64)
                if len(mmid) and int(np.max(mmid))>=len(theta):
                    die("dense theta too short for moment IDs")
                ell[valid]=(ss[valid]*theta[mmid])%P

            if not np.any(ell):
                continue

            F=exact_fourier(ell,RF).reshape(d,d)
            M=(Ti@F)%P
            M=(M@Vj)%P
            B[si,sj]=M
            if aj!=ai:
                B[sj,si]=M.T

    if not np.array_equal(B,B.T):
        die("pre-K block lost symmetry in block %d"%ir)

    # Compression with modular staging.
    T=mm(B,Z)
    M=mm(Z.T,T)
    if M.shape!=(mK,mK):
        die("compressed shape mismatch")
    if not np.array_equal(M,M.T):
        die("compressed block lost symmetry")

    return M,{
        "gap_irrep_id":ir,
        "degree":d,
        "m_W_minus_D":mWD,
        "m_K":mK,
        "compressed_matrix_sha256":hashlib.sha256(
            M.astype("<u2").tobytes()
        ).hexdigest(),
        "compressed_trace_mod_24001":int(np.trace(M)%P),
        "compressed_nonzero_entries":int(np.count_nonzero(M)),
    }


def eval_modp(args):
    if len(args)!=7:
        die(
            "eval-modp BLOCK_OR_ALL THETA SYSTEM NOGAP SPECDIR CACHEDIR OUTDIR"
        )
    blockarg,theta_path,system_path,nogap_path,specdir0,cachedir0,outdir0=args
    specdir=Path(specdir0); cachedir=Path(cachedir0); outdir=Path(outdir0)
    outdir.mkdir(parents=True,exist_ok=True)

    if sha(cachedir/"canonical_K_pencil_manifest.json")!=EXPECTED_MANIFEST_SHA:
        die("manifest SHA mismatch")

    ng=load(nogap_path,"h4nogap_eval")
    Q,Qdata,G,Hdata,ff=ng.structural_construction()
    system,els,gens,action_sha=ng.load_and_match_certified_action(system_path,G)
    if action_sha!=EXPECTED_ACTION_SHA:
        die("action hash mismatch")

    ids=np.memmap(
        specdir/"product_map.id.i32",
        dtype="<i4",mode="r",shape=(1485,ORDER)
    )
    sgn=np.memmap(
        specdir/"product_map.sgn.i8",
        dtype="i1",mode="r",shape=(1485,ORDER)
    )
    pairidx=parse_pairs(specdir/"product_map.pairs.txt")
    kind,theta=read_theta(theta_path)

    if blockarg.lower()=="all":
        blocks=list(range(1,21))
    else:
        ir=int(blockarg)
        if not (1<=ir<=20):
            die("block must be 1..20 or all")
        blocks=[ir]

    rows=[]
    for ir in blocks:
        print("evaluating block %d"%ir,file=sys.stderr,flush=True)
        M,rec=evaluate_block(
            ir,kind,theta,ng,G,ids,sgn,pairidx,cachedir
        )
        outpath=outdir/("M_modp_block_%02d.npy"%ir)
        np.save(outpath,M.astype(np.uint16))
        rec["matrix_path"]=str(outpath)
        rec["matrix_file_sha256"]=sha(outpath)
        rows.append(rec)

    out={
        "status":"EXACT_GF24001_K_PENCIL_EVALUATION",
        "logical_scope":"exact reduction/rank backend; NOT a real PSD certificate",
        "theta_source":str(theta_path),
        "theta_kind":kind,
        "manifest_sha256":EXPECTED_MANIFEST_SHA,
        "blocks":rows,
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    p=outdir/"evaluation_manifest.json"
    p.write_bytes(raw)
    disp=dict(out)
    disp["output_path"]=str(p)
    disp["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp,indent=2,sort_keys=True))


def main():
    if len(sys.argv)<2:
        die("subcommand info/eval-modp")
    if sys.argv[1]=="info":
        if len(sys.argv)!=3: die("info CACHEDIR")
        info(sys.argv[2])
    elif sys.argv[1]=="eval-modp":
        eval_modp(sys.argv[2:])
    else:
        die("unknown subcommand "+sys.argv[1])


if __name__=="__main__":
    main()
