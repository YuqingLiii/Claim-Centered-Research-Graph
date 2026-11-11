#!/usr/bin/env python3
"""
h4_K_pencil_rank_bottleneck.py

Exact upper bound and reproducible bottleneck report for the rank of the full
moment-to-K-compressed-block linear map.

It recomputes the exact rank-12 restriction of H4-invariant degree<=2
polynomials to the two base equality six-faces.  The dual of that restriction
space gives 12 linearly independent H4-invariant functionals supported on the
equality set.  Every such functional annihilates q1*q2 for q1,q2 in K.
Because their independence is already witnessed in the constant/quadratic
moment coordinates, they remain independent after deleting the 5796 quartic
coordinates unused by (W-D)^2.

Consequently, for the effective 746825-coordinate full moment domain,

    rank(moment -> direct_sum Sym(K_rho)) <= 746825 - 12 = 746813.

This script does NOT claim equality.  Proving a GF(24001) lower rank 746813
would close the exact rank by the characteristic-zero sandwich.  Finding a
larger modular/characteristic-zero kernel would lower the rank further.

It also reports the exact sizes of the present deterministic matrix-free
rank problem.

Python 3.9+. Dependencies numpy, h5py, sympy.
"""

import sys,json,hashlib,importlib.util,math,collections
from pathlib import Path
import numpy as np
import h5py
import sympy as sp

EXPECTED_MANIFEST_SHA=(
    "41eaa1a24984bdc456ec325c9e45f6e0d989d86dadfcbb7e88db2e10fc04a86b"
)
EXPECTED_SYSTEM_SHA=(
    "45621c09720050d0f6ffded8712d018c68eb6e72a93fc773cb940a00e3578fb8"
)
EXPECTED_COMPLETE_SHA=(
    "1b44a00376ba29e8c0815870c16f000c2f165573b299b522055b9e8ea701eb9c"
)
EFFECTIVE=746825
OUTPUT_SYM=1569415
ORDER=14400
EXPECTED_RESTRICTION_RANK=12


def die(x): raise SystemExit("ERROR: "+str(x))


def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for z in iter(lambda:f.read(1<<20),b""):h.update(z)
    return h.hexdigest()


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def exact_int_matrix(raw):
    a=np.asarray(raw)
    out=np.empty(a.shape,dtype=np.int64)
    it=np.nditer(a,flags=["multi_index"])
    for z in it:
        x=float(z);q=int(x)
        if float(q)!=x:die("nonintegral A")
        out[it.multi_index]=q
    return out


def exact_sign(raw):
    a=np.asarray(raw).reshape(-1)
    z=np.empty(len(a),dtype=np.int8)
    for i,x0 in enumerate(a):
        x=float(x0)
        if x==1:z[i]=1
        elif x==-1:z[i]=-1
        else:die("non-sign")
    return z


def recompute_rank12(mat_path,system_path,nogap_path,probe_path):
    probe=load(probe_path,"h4probe_rankonly")
    ng=load(nogap_path,"h4nogap_rankonly")

    with h5py.File(mat_path,"r") as f:
        A=exact_int_matrix(f["A"][()])
        ax=exact_sign(f["ax"][()])
        by=exact_sign(f["by"][()])

    system=json.load(open(system_path))
    gj=system["group"]["coxeter_generators"]
    gens=[]
    for g in gj:
        gens.append((
            np.asarray(g["perm"],dtype=np.uint16),
            np.asarray(g["sign"],dtype=np.int8),
        ))

    GP,GS,parent,parent_gen=probe.generate_group(gens)
    if len(GP)!=14400:die("group order")

    probe.init_pairs()
    basis_id,orient,all_orbits,inv_orbits=probe.invariant_monomial_basis(
        gens,GP,GS
    )
    if len(inv_orbits)!=55:die("degree<=2 invariant dimension !=55")

    hright=[
        sum(int(ax[i])*int(A[i,j]) for i in range(300))
        for j in range(300)
    ]
    Z=[j for j,h in enumerate(hright) if h==0]
    if Z!=[46,56,85,99,131,148]:die("zero fields")

    zR=np.concatenate([ax,by]).astype(np.int8)
    zL=np.concatenate([by,ax]).astype(np.int8)
    corners_R=probe.face_corners(zR,[300+j for j in Z])
    corners_L=probe.face_corners(zL,Z)

    vals_R=np.stack([
        probe.eval_invariant_basis(
            z,basis_id,orient,len(inv_orbits)
        ) for z in corners_R
    ])
    vals_L=np.stack([
        probe.eval_invariant_basis(
            z,basis_id,orient,len(inv_orbits)
        ) for z in corners_L
    ])

    RR=probe.face_restriction_matrix(vals_R)
    RL=probe.face_restriction_matrix(vals_L)
    M=sp.Matrix(RR+RL)
    rank=int(M.rank())
    return rank,{
        "invariant_degree_le_2_dimension":55,
        "restriction_rows":44,
        "right_face_fourier_rows":22,
        "left_face_fourier_rows":22,
        "right_zero_fields":Z,
    }


def main():
    if len(sys.argv)!=8:
        die(
            "usage: python h4_K_pencil_rank_bottleneck.py "
            "MAT SYSTEM COMPLETE NOGAP PROBE CACHEDIR SPECDIR"
        )
    mat,system,complete,nogap,probe,cachedir0,specdir0=sys.argv[1:]
    cachedir=Path(cachedir0);specdir=Path(specdir0)

    if sha(system)!=EXPECTED_SYSTEM_SHA:die("system SHA")
    if sha(complete)!=EXPECTED_COMPLETE_SHA:die("complete SHA")
    if sha(cachedir/"canonical_K_pencil_manifest.json")!=EXPECTED_MANIFEST_SHA:
        die("canonical manifest SHA")

    rank12,audit=recompute_rank12(mat,system,nogap,probe)
    if rank12!=EXPECTED_RESTRICTION_RANK:
        die("expected restriction rank 12, got %d"%rank12)

    man=json.load(open(cachedir/"canonical_K_pencil_manifest.json"))
    if man["total_symmetric_block_coordinates"]!=OUTPUT_SYM:
        die("output symmetric dimension")
    if man["effective_moment_coordinates_pre_K"]!=EFFECTIVE:
        die("effective moment dimension")

    # Exact raw matrix-free group Fourier work count:
    pair_d2=sum(
        int(b["active_pair_count"])*int(b["degree"])**2
        for b in man["blocks"]
    )
    fourier_scalar_contributions=pair_d2*ORDER

    # Double-coset/moment aggregation count.  It is still too large to be a
    # convenient explicitly stored coefficient operator.
    ids=np.memmap(
        specdir/"product_map.id.i32",
        dtype="<i4",mode="r",shape=(1485,ORDER)
    )
    uniq=np.zeros(1485,dtype=np.int64)
    for r in range(1485):
        a=np.asarray(ids[r])
        uniq[r]=len(np.unique(a[a>=0]))

    weighted_aggregated=0
    for b in man["blocks"]:
        z=np.load(cachedir/b["cache_file"])
        rows=z["active_pair_rows"][:,2].astype(np.int64)
        weighted_aggregated += (
            int(np.sum(uniq[rows])) * int(b["degree"])**2
        )

    explicit_entries=OUTPUT_SYM*EFFECTIVE

    out={
        "status":"EXACT_RANK_NOT_YET_COMPUTED",
        "rigorous_rank_upper_bound":EFFECTIVE-rank12,
        "effective_moment_domain_dimension":EFFECTIVE,
        "compressed_symmetric_codomain_dimension":OUTPUT_SYM,
        "known_kernel_dimension_lower_bound":rank12,
        "known_kernel_source":(
            "12 independent H4-invariant equality-supported functionals; "
            "independence already witnessed by degree<=2 invariant restrictions"
        ),
        "restriction_rank_exact":rank12,
        "restriction_audit":audit,
        "why_the_12_functionals_annihilate_K_products":(
            "K consists of degree<=2 polynomials vanishing on every translated "
            "equality face; hence any distribution supported on their union "
            "annihilates q1*q2 for q1,q2 in K"
        ),
        "why_independence_survives_5796_quartic_pruning":(
            "the rank-12 independence is witnessed using only the retained "
            "constant and quadratic coordinates"
        ),
        "rank_closing_lemma":(
            "prove rank over GF(24001) >= 746813 for the canonical compressed "
            "operator, or exhibit additional independent kernel functionals"
        ),
        "matrix_free_cost":{
            "sum_active_pair_count_times_d_squared":int(pair_d2),
            "raw_group_fourier_scalar_contributions_per_dense_evaluation":
                int(fourier_scalar_contributions),
            "unique_pair_moment_d2_coefficients_before_K_compression":
                int(weighted_aggregated),
            "explicit_final_coefficient_matrix_entries":int(explicit_entries),
            "explicit_final_matrix_bytes_uint16":int(2*explicit_entries),
            "explicit_final_matrix_bytes_float64":int(8*explicit_entries),
        },
        "logical_bottleneck":(
            "no deterministic exact rank certificate for the 746825-column "
            "canonical operator has been computed.  Full-column rank is "
            "impossible; a sharp lower-rank certificate must reach 746813 "
            "or reveal further kernel."
        ),
        "manifest_sha256":EXPECTED_MANIFEST_SHA,
    }

    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    outpath=cachedir/"rank_bottleneck_exact.json"
    outpath.write_bytes(raw)
    disp=dict(out);disp["output_path"]=str(outpath)
    disp["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(disp,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
