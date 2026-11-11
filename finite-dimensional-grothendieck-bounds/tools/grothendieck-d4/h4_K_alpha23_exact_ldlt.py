#!/usr/bin/env python3
"""
h4_K_alpha23_exact_ldlt.py

Exact finite verifier for the degree-4 dual candidate L_{2/3} on the
complete equality-face vanishing module K.

RUN WITH SAGEMATH:
    sage -python h4_K_alpha23_exact_ldlt.py \
        d4_n1_300x300.mat \
        d4_n1_300x300.mat.H4_level2_exact_system.json \
        d4_n1_300x300.mat.complete_K_isotypic.json \
        h4_nogap_irrep_cache.py \
        h4_K_full_dual_slice_release.py

The last two source files are hash-pinned below.

STATUS RULE
===========
The script prints PROVED_DEGREE4_DUAL_SEPARATOR only if:
  * all immutable hashes match;
  * the exact 20 nonzero K blocks are reconstructed;
  * every exact K block has zero negative inertia under block LDL^*;
  * the objective L_{2/3}(C-x^T A y) is verified exactly negative.

If any exact K block has negative inertia, the script prints
REFUTED_ALPHA_2_OVER_3 and writes an exact negative vector in the
multiplicity-coordinate model.  It verifies C v = 0 and v^* B v < 0
exactly before reporting it.

Otherwise any construction/rank/factorization failure aborts.  There is no
"numerically probably positive" success state.

MATHEMATICAL NORMALIZATION
==========================
Let z=(x_0,...,x_299,y_0,...,y_299) and
    X = [[P,P],[P,P]].

Before applying L, every product is reduced in the Boolean quotient
z_a^2=1.  For a squarefree support S with |S| <= 4,

 L(1)=1,
 L(z_S)=0                                      if |S|=1 or 3,
 L(z_a z_b)=X_ab                              if |S|=2,
 L(z_a z_b z_c z_d)
   = (2/3)(X_ab X_cd + X_ac X_bd + X_ad X_bc) if |S|=4.

The coefficient 2/3 is the fourth-moment coefficient obtained from
2<u,r> with r uniform on S^3:
  E[2<u,r> 2<v,r>] = <u,v>,
  E[prod_{j=1}^4 2<u_j,r>]
     = (2/3) sum_pairings prod inner-products.
Repeated Boolean variables are nevertheless reduced FIRST, so this is not
the ordinary spherical moment functional on all degree-four words.

For f=C-x^T A y,
  L(f)=C-<A,P>
      = C-(1539823299061914600
             +706968072319078800 sqrt(5)) < 0.

EXACT REPRESENTATIONS
=====================
The script reconstructs H4 from the no-GAP structural model
  ((2I x 2I)/<(-1,-1)>) semidirect C2.

The 120 elements of 2I are represented by exact quaternions with coordinates
in (1/4) Z[sqrt(5)].  The fundamental SU(2) representation therefore has
entries in Q(sqrt(5),i).

All nine irreducibles of 2I are reconstructed exactly:
  Sym^n(U), Sym^n(U^sigma), n=0,...,5,
and the missing 4-dimensional U tensor U^sigma.
The symmetric powers use the UNNORMALIZED symmetric tensor basis; hence no
sqrt(binomial) terms occur.  Their invariant Hermitian metrics are exactly
diag(binomial(n,k)).  Thus all exact representation entries remain in
Q(sqrt(5),i).

The 34 H4 irreducibles are then constructed by the same Clifford
diagonal-extension/off-diagonal-induction formulas used by the certified
no-GAP cache.  Characters reduced modulo 24001 are matched EXACTLY against
the certified cache before a representation is accepted.

FULL-K BLOCKS WITHOUT A NUMERICAL NULLSPACE
============================================
For each non-D monomial orbit O and each irreducible rho, let H_O be the
signed stabilizer of an orbit representative.  We form the exact projector
numerator
   P_O = sum_{h in H_O} chi_O(h) rho(h)
and take an exact basis V_O of its column space over Q(sqrt(5),i).

These bases need not be orthonormal.  If M_rho is the exact invariant
Hermitian metric of rho, the exact moment-form block between orbit modules is

  B_{O,O'} =
    V_O^* M_rho
      [ sum_g ell_{O,O'}(g) rho(g) ]
    V_{O'},

where ell_{O,O'}(g)=L(m_O * g m_{O'}).
All omitted factors (|G|, stabilizer orders and common field denominators)
are strictly positive scalars/congruence scalings and therefore do not
affect inertia on the kernel.

The exact residual equality map is

  C_O =
    [ sum_g r_s(g) rho(g) V_O ]_{s=1}^{14}.

Thus the complete K multiplicity space is ker(C), computed by Sage over the
exact number field:
   Z = basis matrix of right_kernel(C),
and the exact K block is
   K_rho = Z^* B Z.

The code requires
   rank(C) = m(W-D)-m(K)
from the already-proved complete-K theorem before any inertia claim.

EXACT INERTIA
=============
For every K_rho the script calls the exact Sage block_ldlt() factorization

  P^* K_rho P = L D L^*.

It checks this identity exactly.  The 1x1/2x2 diagonal blocks of D are then
classified over the chosen real embedding.  This gives the exact inertia.

The output records a SHA-256 of K_rho and of P,L,D in canonical
Q(sqrt(5),i) coefficient form, so the certificate is reproducible without
trusting printed decimals.

FAST BUT EXACT GROUP FOURIER SUMS
==================================
Representation matrices are stored as four INTEGER coefficient arrays for
  a+b*sqrt(5)+i(c+d*sqrt(5))
with a common positive denominator.

The 14400-term group Fourier sums are integer matrix products.  To use BLAS
speed safely, each row chunk is chosen so that
  chunk * max|A| * max|B| < 2^50.
Thus every multiplication and every possible absolute partial sum is an
exact IEEE-754 binary64 integer (<2^53).  Every BLAS result is required to be
bitwise integral before conversion back to integers.  Chunk results are
then accumulated with Python arbitrary-precision integers if int64 would
not suffice.

This is an acceleration of exact integer summation, not a floating-point
certificate.

Dependencies
============
- SageMath 10.x (`sage -python`)
- numpy
- scipy
- h5py
- sympy

Python source syntax is 3.9-compatible, but exact execution requires Sage.
"""

import sys
import os
import json
import math
import hashlib
import itertools
import collections
import importlib.util
import tempfile
from fractions import Fraction

import numpy as np
import h5py
import scipy.linalg as sla
import sympy as sp

EXPECTED_MD5 = "b5223ca2fd5c4cbe52e93a23a4570b9f"
EXPECTED_A_SHA = (
    "5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5"
)
EXPECTED_ACTION_SHA = (
    "1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097"
)
EXPECTED_ISOTYPIC_SHA = (
    "48a2ab8d4485825bf26c2903b7ded2331dc04af3927399e36cc54433bdeb865d"
)
EXPECTED_COMPLETE_OUTPUT_SHA = (
    "1b44a00376ba29e8c0815870c16f000c2f165573b299b522055b9e8ea701eb9c"
)
EXPECTED_NOGAP_SHA = (
    "44835ca3c57ca8b172a539c081a046a79282d15ae38c1968955bdb9871d3ccb8"
)
EXPECTED_DUALBASE_SHA = (
    "2dac591911395609f300260a704554a9b791433491b9584ae753fa0e97594149"
)

EXPECTED_C = 2081044153087351400
NUM_A = 1539823299061914600
NUM_B = 706968072319078800

N = 300
NV = 600
ORDER = 14400
PRIME = 24001
PAIR_OFFSET = 1 + NV
MON_DIM = PAIR_OFFSET + NV * (NV - 1) // 2

EXPECTED_SURVIVING_BLOCKS_SORTED = sorted([
    582,465,611,211,611,822,235,162,107,397,
    504,43,17,107,166,235,162,504,384,286,
])


# ============================================================================
# General utilities
# ============================================================================

def die(msg):
    raise SystemExit("ERROR: " + str(msg))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            z = f.read(1 << 20)
            if not z:
                break
            h.update(z)
    return h.hexdigest()


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            z = f.read(1 << 20)
            if not z:
                break
            h.update(z)
    return h.hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exact_int_matrix(raw, name):
    a = np.asarray(raw)
    if a.shape != (N, N):
        die("%s shape=%r" % (name, a.shape))
    out = np.empty(a.shape, dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        if not math.isfinite(x):
            die("%s%s nonfinite" % (name, it.multi_index))
        q = int(x)
        if float(q) != x:
            die("%s%s not exactly integral" % (name, it.multi_index))
        out[it.multi_index] = q
    return out


def exact_sign_vector(raw, name):
    a = np.asarray(raw).reshape(-1)
    if len(a) != N:
        die("%s length != 300" % name)
    z = np.empty(N, dtype=np.int8)
    for i, x0 in enumerate(a):
        x = float(x0)
        if x == 1.0:
            z[i] = 1
        elif x == -1.0:
            z[i] = -1
        else:
            die("%s[%d] not +/-1" % (name, i))
    return z


def canonical_A_sha(A):
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


# ============================================================================
# Integer Q(sqrt(5),i) coefficient arithmetic
#
# A coefficient tuple (a,b,c,d) denotes
#     a + b*s + i(c+d*s),   s^2=5, i^2=-1.
# Denominators are tracked separately and are always common positive scalars.
# ============================================================================

def cadd(x, y):
    return (
        x[0] + y[0], x[1] + y[1],
        x[2] + y[2], x[3] + y[3],
    )


def cneg(x):
    return (-x[0], -x[1], -x[2], -x[3])


def cscale(x, n):
    return (n*x[0], n*x[1], n*x[2], n*x[3])


def cconj(x):
    return (x[0], x[1], -x[2], -x[3])


def cmul(x, y):
    a,b,c,d = [int(t) for t in x]
    e,f,g,h = [int(t) for t in y]
    return (
        a*e + 5*b*f - c*g - 5*d*h,
        a*f + b*e - c*h - d*g,
        a*g + 5*b*h + c*e + 5*d*f,
        a*h + b*g + c*f + d*e,
    )


CONE = (1,0,0,0)
CZERO = (0,0,0,0)


def cpow(x, n):
    r = CONE
    b = tuple(int(t) for t in x)
    while n:
        if n & 1:
            r = cmul(r, b)
        b = cmul(b, b)
        n //= 2
    return r


def q5mul(x, y):
    a,b = x
    c,d = y
    return (a*c + 5*b*d, a*d + b*c)


def cmod(x, p, sroot, iroot):
    return (
        int(x[0])
        + int(x[1]) * sroot
        + iroot * (int(x[2]) + int(x[3]) * sroot)
    ) % p


# ============================================================================
# Exact binary-icosahedral quaternions, all at common coordinate denominator 4
# ============================================================================

def perm_parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                inv += 1
    return inv & 1


def exact_binary_icosahedral():
    # Each quaternion coordinate is a pair (a,b) meaning (a+b*sqrt5)/4.
    V = []

    for i in range(4):
        for sg in (-1, 1):
            q = [(0,0)] * 4
            q[i] = (4*sg, 0)
            V.append(tuple(q))

    for signs in itertools.product((-1,1), repeat=4):
        V.append(tuple((2*sg,0) for sg in signs))

    base = ((0,0), (2,0), (1,1), (-1,1))
    for perm in itertools.permutations(range(4)):
        if perm_parity(perm):
            continue
        arr = [base[perm[i]] for i in range(4)]
        nz = [i for i,x in enumerate(arr) if x != (0,0)]
        for signs in itertools.product((-1,1), repeat=3):
            q = list(arr)
            for i,sg in zip(nz, signs):
                q[i] = (sg*q[i][0], sg*q[i][1])
            V.append(tuple(q))

    uniq = []
    seen = set()
    for q in V:
        if q not in seen:
            seen.add(q)
            uniq.append(q)
    V = uniq

    if len(V) != 120:
        die("exact 2I quaternion count %d != 120" % len(V))

    lookup = {q:i for i,q in enumerate(V)}

    def qmul_num(q, r):
        w,x,y,z = q
        W,X,Y,Z = r

        def A(u,v): return (u[0]+v[0], u[1]+v[1])
        def S(u,v): return (u[0]-v[0], u[1]-v[1])
        def M(u,v): return q5mul(u,v)

        # Numerators currently have denominator 16.
        t0 = S(S(S(M(w,W), M(x,X)), M(y,Y)), M(z,Z))
        t1 = A(A(M(w,X), M(x,W)), S(M(y,Z), M(z,Y)))
        t2 = A(S(A(M(w,Y), M(y,W)), M(x,Z)), M(z,X))
        t3 = A(A(S(M(w,Z), M(y,X)), M(z,W)), M(x,Y))

        # Convert denominator 16 back to denominator 4.
        out = []
        for t in (t0,t1,t2,t3):
            if t[0] % 4 or t[1] % 4:
                die("2I multiplication not divisible back to denominator 4")
            out.append((t[0]//4, t[1]//4))
        return tuple(out)

    mul = np.empty((120,120), dtype=np.int16)
    for a in range(120):
        for b in range(120):
            q = qmul_num(V[a], V[b])
            if q not in lookup:
                die("exact quaternion product left the 120-set")
            mul[a,b] = lookup[q]

    eid = lookup[(
        (4,0),(0,0),(0,0),(0,0)
    )]

    return V, mul, eid


def quat_fund_matrix_num(q):
    # denominator 4
    w,x,y,z = q
    # q5 real pair -> complex-field tuple
    def R(t): return (t[0],t[1],0,0)
    def I(t): return (0,0,t[0],t[1])
    return np.asarray([
        [cadd(R(w), I(x)), cadd(R(y), I(z))],
        [cadd(cneg(R(y)), I(z)), cadd(R(w), cneg(I(x)))],
    ], dtype=object)


def sympow_num(U, n):
    """
    Sym^n in the unnormalized symmetric tensor basis
       v_k = sum_{bitstrings |b|=k} |b>.
    If U has denominator 4 then result has denominator 4^n.
    """
    if n == 0:
        out = np.empty((1,1), dtype=object)
        out[0,0] = CONE
        return out, 1, [1]

    a = tuple(U[0,0]); b = tuple(U[0,1])
    c = tuple(U[1,0]); d = tuple(U[1,1])

    out = np.empty((n+1,n+1), dtype=object)

    pa = [cpow(a,k) for k in range(n+1)]
    pb = [cpow(b,k) for k in range(n+1)]
    pc = [cpow(c,k) for k in range(n+1)]
    pd = [cpow(d,k) for k in range(n+1)]

    for ell in range(n+1):
        for k in range(n+1):
            z = CZERO
            rlo = max(0, k-(n-ell))
            rhi = min(k, ell)
            for r in range(rlo, rhi+1):
                coeff = math.comb(ell,r) * math.comb(n-ell,k-r)
                term = cmul(
                    cmul(pa[n-ell-k+r], pb[k-r]),
                    cmul(pc[ell-r], pd[r]),
                )
                z = cadd(z, cscale(term, coeff))
            out[ell,k] = z

    return out, 4**n, [math.comb(n,k) for k in range(n+1)]


def q5c_kron(A, B):
    m,n = A.shape
    p,q = B.shape
    out = np.empty((m*p,n*q), dtype=object)
    for i in range(m):
        for j in range(n):
            aa = tuple(A[i,j])
            for r in range(p):
                for s in range(q):
                    out[i*p+r,j*q+s] = cmul(aa, tuple(B[r,s]))
    return out


def block_diag_object(A, B):
    m,n = A.shape
    p,q = B.shape
    Z = np.empty((m+p,n+q), dtype=object)
    for i in range(m+p):
        for j in range(n+q):
            Z[i,j] = CZERO
    Z[:m,:n] = A
    Z[m:,n:] = B
    return Z


def flip_perm(du, dv):
    # F: U tensor V -> V tensor U, F[dst,src]=1.
    r = du*dv
    out = np.empty(r, dtype=np.int32)
    for i in range(du):
        for j in range(dv):
            src = i*dv+j
            dst = j*du+i
            out[src] = dst
    return out


def right_perm_columns(M, row_for_col, sign=1):
    out = np.empty_like(M)
    for c in range(M.shape[1]):
        src = int(row_for_col[c])
        for r in range(M.shape[0]):
            out[r,c] = cscale(tuple(M[r,src]), sign)
    return out


# ============================================================================
# Build all 9 exact Q irreps and match them to the no-GAP Qdata character IDs
# ============================================================================

def order_table(mul, eid, a, cap=120):
    x = eid
    for k in range(1,cap+1):
        x = int(mul[x,a])
        if x == eid:
            return k
    return None


def generated_set(mul, eid, gens):
    seen = {eid}
    q = collections.deque([eid])
    while q:
        x = q.popleft()
        for g in gens:
            y = int(mul[x,g])
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def labelled_iso(mulA,eA,gensA,mulB,eB,gensB):
    mp={eA:eB}; rev={eB:eA}; q=collections.deque([eA])
    while q:
        x=q.popleft(); y=mp[x]
        for ga,gb in zip(gensA,gensB):
            xx=int(mulA[x,ga]); yy=int(mulB[y,gb])
            if xx in mp:
                if mp[xx]!=yy: return None
            else:
                if yy in rev: return None
                mp[xx]=yy; rev[yy]=xx; q.append(xx)
    if len(mp)!=len(mulA):
        return None
    for a in range(len(mulA)):
        for b in range(len(mulA)):
            if mp[int(mulA[a,b])] != int(mulB[mp[a],mp[b]]):
                return None
    return mp


def find_structural_to_quat_iso(Q, Vmul, Veid):
    mulQ=Q["mul"]; eQ=int(Q["I"])
    oq=[order_table(mulQ,eQ,i) for i in range(120)]
    ov=[order_table(Vmul,Veid,i) for i in range(120)]

    qpair=None
    for a in range(120):
        if oq[a]!=4: continue
        for b in range(120):
            if oq[b]!=6: continue
            if order_table(mulQ,eQ,int(mulQ[a,b]))!=10: continue
            if len(generated_set(mulQ,eQ,[a,b]))==120:
                qpair=(a,b); break
        if qpair is not None: break
    if qpair is None:
        die("could not find structural Q pair")

    for a in range(120):
        if ov[a]!=4: continue
        for b in range(120):
            if ov[b]!=6: continue
            if order_table(Vmul,Veid,int(Vmul[a,b]))!=10: continue
            z=labelled_iso(mulQ,eQ,qpair,Vmul,Veid,(a,b))
            if z is not None:
                return z,qpair,(a,b)

    die("exact structural-Q to quaternion isomorphism failed")


def sqrt_roots_mod(p, a):
    rr = sp.sqrt_mod(a, p, all_roots=True)
    return sorted(int(x) for x in rr)


def matrix_char_mod(Mnum, den, p, sroot, iroot):
    z=0
    for i in range(Mnum.shape[0]):
        z += cmod(tuple(Mnum[i,i]),p,sroot,iroot)
    return (z * pow(int(den)%p,p-2,p)) % p


def exact_outer_Q_automorphism(Q, qpair, fundamental_char, target_char):
    mulQ=Q["mul"]; eQ=int(Q["I"])
    oq=[order_table(mulQ,eQ,i) for i in range(120)]

    for a in range(120):
        if oq[a]!=4: continue
        for b in range(120):
            if oq[b]!=6: continue
            if order_table(mulQ,eQ,int(mulQ[a,b]))!=10: continue
            mp=labelled_iso(mulQ,eQ,qpair,mulQ,eQ,(a,b))
            if mp is None: continue
            if all(int(fundamental_char[mp[i]])==int(target_char[i])
                   for i in range(120)):
                return mp,(a,b)
    die("exact outer Q automorphism not found")


def tensor_rep_num(repA, repB):
    A,DA,MA=repA["num"],repA["den"],repA["metric"]
    B,DB,MB=repB["num"],repB["den"],repB["metric"]
    mats=[]
    for g in range(120):
        mats.append(q5c_kron(A[g],B[g]))
    return {
        "num": mats,
        "den": DA*DB,
        "metric": [int(x)*int(y) for x in MA for y in MB],
    }


def build_exact_Q_irreps(Q,Qdata):
    V,Vmul,Veid=exact_binary_icosahedral()
    iso,qpair,vpair=find_structural_to_quat_iso(Q,Vmul,Veid)

    fund=[]
    for qi in range(120):
        fund.append(quat_fund_matrix_num(V[iso[qi]]))

    p=PRIME
    sroot=sqrt_roots_mod(p,5)[0]
    iroot=sqrt_roots_mod(p,-1)[0]

    two_ids=[i for i,r in enumerate(Qdata["irreps"]) if int(r["degree"])==2]

    fchar=[matrix_char_mod(fund[i],4,p,sroot,iroot) for i in range(120)]
    match=[
        i for i in two_ids
        if all(int(Qdata["irreps"][i]["character"][g])%p == fchar[g]
               for g in range(120))
    ]
    if len(match)!=1:
        die("exact fundamental Q irrep did not match uniquely")
    fund_id=match[0]
    other_id=[i for i in two_ids if i!=fund_id][0]

    auto,autopair=exact_outer_Q_automorphism(
        Q,qpair,fchar,[int(x)%p for x in Qdata["irreps"][other_id]["character"]]
    )
    fundg=[fund[auto[i]] for i in range(120)]

    reps=[None]*9

    def install(mats,den,metric):
        d=mats[0].shape[0]
        ch=[matrix_char_mod(mats[g],den,p,sroot,iroot) for g in range(120)]
        hits=[
            i for i,r in enumerate(Qdata["irreps"])
            if int(r["degree"])==d
            and all(int(r["character"][g])%p==ch[g] for g in range(120))
        ]
        if len(hits)!=1:
            die("exact Q irrep character match failed d=%d hits=%r"%(d,hits))
        i=hits[0]
        rec={"num":mats,"den":den,"metric":list(metric)}
        if reps[i] is None:
            reps[i]=rec
        else:
            # Character equality is enough for irreducible isomorphism.
            pass

    for base in (fund,fundg):
        for n in range(6):
            mats=[]; den=None; metric=None
            for g in range(120):
                M,D,met=sympow_num(base[g],n)
                mats.append(M); den=D; metric=met
            install(mats,den,metric)

    # U tensor U^sigma
    mats=[q5c_kron(fund[g],fundg[g]) for g in range(120)]
    install(mats,16,[1,1,1,1])

    if any(r is None for r in reps):
        die("failed to build all nine exact Q irreps")

    return reps,{
        "structural_Q_pair":list(qpair),
        "quaternion_pair":list(vpair),
        "fundamental_Q_id":fund_id+1,
        "galois_fundamental_Q_id":other_id+1,
        "outer_pair":list(autopair),
        "sqrt5_root_mod_24001":sroot,
        "i_root_mod_24001":iroot,
    }


# ============================================================================
# Exact H4 representation numerator matrices for a single irreducible
# ============================================================================

def q5c_kron_int(A,B):
    # Inputs object matrices of tuples. Output object.
    return q5c_kron(A,B)


def h_rep_element_num(meta,Qreps,G,gi):
    pairs=G["pairs"]; elems=G["elements"]
    pid,e=elems[gi]
    a,b=pairs[pid]

    if meta["type"]=="diagonal_extension":
        U=Qreps[int(meta["i"])]
        M=q5c_kron_int(U["num"][a],U["num"][b])
        du=U["num"][0].shape[0]
        if e:
            fp=flip_perm(du,du)
            M=right_perm_columns(M,fp,int(meta["extension_sign"]))
        return M,U["den"]*U["den"],[
            int(x)*int(y) for x in U["metric"] for y in U["metric"]
        ]

    U=Qreps[int(meta["i"])]
    V=Qreps[int(meta["j"])]
    A=q5c_kron_int(U["num"][a],V["num"][b])
    B=q5c_kron_int(V["num"][a],U["num"][b])
    M=block_diag_object(A,B)

    du=U["num"][0].shape[0]; dv=V["num"][0].shape[0]
    r=du*dv

    if e:
        F=flip_perm(du,dv)
        # Build sparse T column action exactly.
        # T[:r,r:]=F.T ; T[r:,:r]=F.
        row_for_col=np.empty(2*r,dtype=np.int32)
        # first-block columns
        for c in range(r):
            row_for_col[c]=r+int(F[c])
        # second-block columns: inverse F
        invF=np.empty(r,dtype=np.int32)
        for src,dst in enumerate(F):
            invF[int(dst)]=src
        for c in range(r):
            row_for_col[r+c]=int(invF[c])
        M=right_perm_columns(M,row_for_col,1)

    metric=[
        int(x)*int(y) for x in U["metric"] for y in V["metric"]
    ] + [
        int(x)*int(y) for x in V["metric"] for y in U["metric"]
    ]

    return M,U["den"]*V["den"],metric


def object_comp_matrix_to_int(M):
    m,n=M.shape
    out=np.empty((m,n,4),dtype=np.int64)
    for i in range(m):
        for j in range(n):
            z=tuple(int(x) for x in M[i,j])
            for k in range(4):
                if not (-(1<<63)<=z[k]<(1<<63)):
                    die("representation numerator exceeded int64")
                out[i,j,k]=z[k]
    return out


def build_R_components(meta,Qreps,G,tmpdir,tag):
    d=int(meta["degree"])
    # Determine denominator/metric from identity first.
    M0,den,metric=h_rep_element_num(meta,Qreps,G,0)
    if M0.shape!=(d,d):
        die("exact H irrep dimension mismatch")

    # Conservative magnitude prebound from first component data of Q reps.
    # Allocate int64 memmaps; they are removed block-by-block.
    paths=[]
    mm=[]
    for c in range(4):
        p=os.path.join(tmpdir,"%s_R%d.dat"%(tag,c))
        paths.append(p)
        mm.append(np.memmap(p,dtype=np.int64,mode="w+",shape=(ORDER,d*d)))

    maxabs=0
    for g in range(ORDER):
        M,D,met=h_rep_element_num(meta,Qreps,G,g)
        if D!=den or met!=metric:
            die("H representation denominator/metric changed across group")
        C=object_comp_matrix_to_int(M).reshape(d*d,4)
        for c in range(4):
            mm[c][g,:]=C[:,c]
            if C.shape[0]:
                maxabs=max(maxabs,int(np.max(np.abs(C[:,c]))))
        if (g+1)%2000==0:
            print("    exact rho numerators %d/%d"%(g+1,ORDER),file=sys.stderr)

    for z in mm:
        z.flush()

    return mm,paths,int(den),list(metric),maxabs


# ============================================================================
# Exact integer BLAS
# ============================================================================

def exact_int_dot_AT_B(A,B):
    """
    Return A^T B exactly.

    A: (G,r), B:(G,q), signed integers.

    Each floating BLAS chunk is chosen with
        chunk*max|A|*max|B| < 2^50,
    so every multiplication and absolute partial sum is exactly representable
    as binary64 integer. Chunk outputs are required to be bitwise integral.
    """
    A=np.asarray(A)
    B=np.asarray(B)
    if A.shape[0]!=B.shape[0]:
        die("dot dimension mismatch")
    G=A.shape[0]
    ma=int(np.max(np.abs(A))) if A.size else 0
    mb=int(np.max(np.abs(B))) if B.size else 0
    if ma==0 or mb==0:
        return np.zeros((A.shape[1],B.shape[1]),dtype=np.int64)

    per=ma*mb
    chunk=max(1,min(G,(1<<49)//max(1,per)))
    total_bound=G*per

    use_object = total_bound >= (1<<61)
    if use_object:
        acc=np.zeros((A.shape[1],B.shape[1]),dtype=object)
    else:
        acc=np.zeros((A.shape[1],B.shape[1]),dtype=np.int64)

    for lo in range(0,G,chunk):
        hi=min(G,lo+chunk)
        cb=(hi-lo)*per
        if cb >= (1<<50):
            die("internal exact-BLAS chunk bound failure")
        P=A[lo:hi].astype(np.float64).T.dot(
            B[lo:hi].astype(np.float64)
        )
        R=np.rint(P)
        if not np.array_equal(P,R):
            die("BLAS exact-integer dot produced nonintegral float")
        if np.max(np.abs(R)) >= (1<<53):
            die("BLAS exact-integer chunk output exceeded 2^53")
        Ri=R.astype(np.int64)
        if use_object:
            acc += Ri.astype(object)
        else:
            # Total absolute bound already proves no int64 overflow.
            acc += Ri
    return acc


def exact_field_weighted_fourier(E0,E1,Rcomp):
    """
    E=(E0+E1 sqrt5), R=(Ra+Rb sqrt5)+i(Rc+Rd sqrt5).
    Returns four exact coefficient matrices of E^T R.
    """
    Ra,Rb,Rc,Rd=Rcomp

    A0=exact_int_dot_AT_B(E0,Ra)
    A1=exact_int_dot_AT_B(E1,Rb)
    Fa=A0 + 5*A1

    Fb=exact_int_dot_AT_B(E0,Rb) + exact_int_dot_AT_B(E1,Ra)
    Fc=exact_int_dot_AT_B(E0,Rc) + 5*exact_int_dot_AT_B(E1,Rd)
    Fd=exact_int_dot_AT_B(E0,Rd) + exact_int_dot_AT_B(E1,Rc)

    return Fa,Fb,Fc,Fd


# ============================================================================
# Sage exact field conversion and canonical hashes
# ============================================================================

def sage_setup():
    try:
        from sage.all import (
            QQ, ZZ, AA, CC, PolynomialRing, QuadraticField,
            matrix, vector, diagonal_matrix, zero_matrix
        )
    except Exception as e:
        die(
            "SageMath is required. Run with `sage -python ...`. "
            "Import error: %r"%e
        )

    K5=QuadraticField(5,names=("s",),embedding=AA(5).sqrt())
    s=K5.gen()
    R=PolynomialRing(K5,names=("t",))
    t=R.gen()
    K=K5.extension(t*t+1,names=("ii",),embedding=CC(0,1))
    ii=K.gen()

    return {
        "QQ":QQ,"ZZ":ZZ,"AA":AA,"CC":CC,
        "matrix":matrix,"vector":vector,
        "diag":diagonal_matrix,"zero":zero_matrix,
        "K5":K5,"s":K5(s),"K":K,"ii":ii,
    }


def comp_entry_to_K(S,z):
    K=S["K"]; s=K(S["s"]); ii=S["ii"]
    a,b,c,d=[int(x) for x in z]
    return K(a)+K(b)*s + ii*(K(c)+K(d)*s)


def comp_arrays_to_K_matrix(S, comps, nrows, ncols):
    A,B,C,D=comps
    matrix=S["matrix"]; K=S["K"]
    vals=[]
    for i in range(nrows):
        for j in range(ncols):
            vals.append(comp_entry_to_K(S,(
                int(A[i,j]),int(B[i,j]),int(C[i,j]),int(D[i,j])
            )))
    return matrix(K,nrows,ncols,vals)


def num3_to_K_matrix(S,A):
    # A shape (m,n,4)
    matrix=S["matrix"]; K=S["K"]
    m,n,_=A.shape
    vals=[]
    for i in range(m):
        for j in range(n):
            vals.append(comp_entry_to_K(S,A[i,j]))
    return matrix(K,m,n,vals)


def canonical_field_tuple(z):
    """
    Canonical four rational coefficients
      a+b*s + ii(c+d*s).
    """
    # K is degree-2 over K5. list() gives [u,v].
    q=list(z)
    while len(q)<2: q.append(0)
    out=[]
    for u in q[:2]:
        p=list(u)
        while len(p)<2: p.append(0)
        for x in p[:2]:
            out.append((int(x.numerator()),int(x.denominator())))
    # order is a,b,c,d
    return tuple(out)


def hash_K_matrix(M):
    h=hashlib.sha256()
    h.update(("%dx%d;"%(M.nrows(),M.ncols())).encode())
    for z in M.list():
        for a,b in canonical_field_tuple(z):
            h.update(("%d/%d;"%(a,b)).encode())
    return h.hexdigest()


def field_real_sign(S,z):
    AA=S["AA"]
    # Hermitian diagonal/pivot quantities must be real.
    zz=AA(z)
    if zz>0: return 1
    if zz<0: return -1
    return 0


# ============================================================================
# Exact P numerator and the L_{2/3} ell sequences
# ============================================================================

def transformed_arrays(base,rep_mid,cert_elements):
    supp=base.mid_support(rep_mid)
    deg=len(supp)
    sg=np.empty(ORDER,dtype=np.int64)
    aa=np.full(ORDER,-1,dtype=np.int16)
    bb=np.full(ORDER,-1,dtype=np.int16)
    for g,(p,s) in enumerate(cert_elements):
        mm,z=base.act_mid(rep_mid,p,s)
        ss=base.mid_support(mm)
        sg[g]=int(z)
        if len(ss): aa[g]=int(ss[0])
        if len(ss)==2: bb[g]=int(ss[1])
    return {"deg":deg,"sign":sg,"a":aa,"b":bb}


def q5prod_arrays(x1,y1,x2,y2):
    return x1*x2+5*y1*y2, x1*y2+y1*x2


def ell_scaled_for_pair(base,rep_mid,trans,X6,Y6,D):
    """
    Common positive denominator DL=3D^2 is omitted.
    Returns integer E0,E1 such that
      DL*ell(g) = E0(g)+E1(g)*sqrt5.
    """
    S=base.mid_support(rep_mid)
    d1=len(S); d2=int(trans["deg"])
    sg=trans["sign"].astype(np.int64)
    E0=np.zeros(ORDER,dtype=np.int64)
    E1=np.zeros(ORDER,dtype=np.int64)
    DL=3*D*D

    if (d1+d2)&1:
        return E0,E1

    if d1==0 and d2==0:
        E0=sg*DL
        return E0,E1

    if d1==0 and d2==2:
        a=trans["a"].astype(np.int64); b=trans["b"].astype(np.int64)
        E0=sg*(3*D)*X6[a,b]
        E1=sg*(3*D)*Y6[a,b]
        return E0,E1

    if d1==2 and d2==0:
        a,b=S
        E0[:]=sg*(3*D)*int(X6[a,b])
        E1[:]=sg*(3*D)*int(Y6[a,b])
        return E0,E1

    if d1==1 and d2==1:
        a=S[0]
        c=trans["a"].astype(np.int64)
        same=(c==a)
        E0[same]=sg[same]*DL
        ns=~same
        E0[ns]=sg[ns]*(3*D)*X6[a,c[ns]]
        E1[ns]=sg[ns]*(3*D)*Y6[a,c[ns]]
        return E0,E1

    if d1!=2 or d2!=2:
        return E0,E1

    a,b=S
    c=trans["a"].astype(np.int64)
    d=trans["b"].astype(np.int64)

    eq=((c==a)&(d==b))|((c==b)&(d==a))
    E0[eq]=sg[eq]*DL

    share_a=(c==a)|(d==a)
    share_b=(c==b)|(d==b)
    share=(share_a|share_b)&(~eq)

    inds=np.flatnonzero(share)
    if len(inds):
        cc=c[inds]; dd=d[inds]
        rem1=np.where(share_a[inds],b,a)
        shared=np.where((cc==a)|(cc==b),cc,dd)
        rem2=np.where(cc==shared,dd,cc)
        E0[inds]=sg[inds]*(3*D)*X6[rem1,rem2]
        E1[inds]=sg[inds]*(3*D)*Y6[rem1,rem2]

    dis=(~eq)&(~share)
    inds=np.flatnonzero(dis)
    if len(inds):
        cc=c[inds]; dd=d[inds]

        xab=int(X6[a,b]); yab=int(Y6[a,b])

        r0,r1=q5prod_arrays(
            xab,yab,X6[cc,dd],Y6[cc,dd]
        )
        s0,s1=q5prod_arrays(
            X6[a,cc],Y6[a,cc],X6[b,dd],Y6[b,dd]
        )
        t0,t1=q5prod_arrays(
            X6[a,dd],Y6[a,dd],X6[b,cc],Y6[b,cc]
        )
        # (2/3) pairings / D^2, then multiply by 3D^2.
        E0[inds]=sg[inds]*2*(r0+s0+t0)
        E1[inds]=sg[inds]*2*(r1+s1+t1)

    return E0,E1


# ============================================================================
# Exact fixed spaces, residual map and moment block
# ============================================================================

def exact_projector_basis(
    S,base,Rcomp,rec,cert_elements,d
):
    inds,chars=base.orbit_stabilizer(rec["rep_mid"],cert_elements)
    comps=[]
    for c in range(4):
        A=np.asarray(Rcomp[c][inds,:],dtype=np.int64)
        ch=np.asarray(chars,dtype=np.int64).reshape(-1,1)
        z=np.sum(A*ch,axis=0,dtype=np.int64).reshape(d,d)
        comps.append(z)
    P=num3_to_K_matrix(
        S,np.stack(comps,axis=2)
    )
    Vbasis=P.column_space().basis()
    if not Vbasis:
        return None,inds,chars
    V=S["matrix"](S["K"],Vbasis).transpose()

    # Exact stabilizer eigen-character audit.
    for h,ch in zip(inds,chars):
        Rh=num3_to_K_matrix(
            S,np.stack([
                np.asarray(Rcomp[c][int(h),:]).reshape(d,d)
                for c in range(4)
            ],axis=2)
        )
        if Rh*V != int(ch)*V:
            die("exact fixed-space stabilizer audit failed")
    return V,inds,chars


def residual_rvals_int(base,rep_mid,Rseed,cert_elements):
    out=np.empty((ORDER,14),dtype=np.int64)
    for g,(p,s) in enumerate(cert_elements):
        mm,z=base.act_mid(rep_mid,p,s)
        out[g,:]=int(z)*Rseed[:,mm]
    return out


def build_exact_C(
    S,base,Rcomp,active,Rseed,cert_elements,d,mWD
):
    C=S["zero"](S["K"],14*d,mWD)
    for oi,rec in enumerate(active):
        V=rec["V"]
        k=V.ncols()
        rvals=residual_rvals_int(
            base,rec["rep_mid"],Rseed,cert_elements
        )
        # rvals^T * rho(g), separately for four exact field coefficients.
        comps=[]
        for c in range(4):
            z=exact_int_dot_AT_B(
                rvals,np.asarray(Rcomp[c])
            ).reshape(14,d,d)
            comps.append(z)

        # For each seed, multiply exact Fourier matrix by exact V.
        for ss in range(14):
            F=num3_to_K_matrix(
                S,np.stack([comps[c][ss] for c in range(4)],axis=2)
            )
            W=F*V
            C[ss*d:(ss+1)*d,rec["copy_start"]:rec["copy_end"]]=W
        print(
            "      C orbit %d/%d"%(oi+1,len(active)),
            file=sys.stderr
        )
    return C


def build_exact_B(
    S,base,Rcomp,active,cert_elements,X6,Y6,D,metric,d,mWD
):
    B=S["zero"](S["K"],mWD,mWD)
    M=S["diag"](S["K"],[int(x) for x in metric])

    trans=[
        transformed_arrays(base,rec["rep_mid"],cert_elements)
        for rec in active
    ]

    for ii,Oi in enumerate(active):
        js=list(range(ii,len(active)))
        E0=np.empty((ORDER,len(js)),dtype=np.int64)
        E1=np.empty_like(E0)

        for col,jj in enumerate(js):
            a,b=ell_scaled_for_pair(
                base,Oi["rep_mid"],trans[jj],X6,Y6,D
            )
            E0[:,col]=a
            E1[:,col]=b

        Fa,Fb,Fc,Fd=exact_field_weighted_fourier(
            E0,E1,Rcomp
        )
        # shapes len(js) x d^2

        Vi=Oi["V"]
        si=slice(Oi["copy_start"],Oi["copy_end"])

        for col,jj in enumerate(js):
            Oj=active[jj]
            Vj=Oj["V"]
            sj=slice(Oj["copy_start"],Oj["copy_end"])

            F=num3_to_K_matrix(
                S,np.stack([
                    np.asarray(Fa[col],dtype=object).reshape(d,d),
                    np.asarray(Fb[col],dtype=object).reshape(d,d),
                    np.asarray(Fc[col],dtype=object).reshape(d,d),
                    np.asarray(Fd[col],dtype=object).reshape(d,d),
                ],axis=2)
            )

            Bij=Vi.conjugate_transpose()*M*F*Vj
            B[si,sj]=Bij
            if jj!=ii:
                B[sj,si]=Bij.conjugate_transpose()

        print(
            "      B orbit row %d/%d"%(ii+1,len(active)),
            file=sys.stderr
        )

    if B != B.conjugate_transpose():
        die("exact moment block is not Hermitian")

    return B


# ============================================================================
# Exact block LDL inertia and negative witness
# ============================================================================

def scan_D_inertia(S,D):
    n=D.nrows()
    pos=neg=zero=0
    blocks=[]
    i=0
    while i<n:
        if i+1<n and D[i,i+1] != 0:
            a=D[i,i]; b=D[i,i+1]; c=D[i+1,i+1]
            tr=a+c
            det=a*c-b*b.conjugate()
            sd=field_real_sign(S,det)
            st=field_real_sign(S,tr)
            if sd<0:
                pp,nn,zz=1,1,0
            elif sd>0:
                if st>0: pp,nn,zz=2,0,0
                elif st<0: pp,nn,zz=0,2,0
                else: die("2x2 Hermitian block det>0 trace=0 impossible")
            else:
                if st>0: pp,nn,zz=1,0,1
                elif st<0: pp,nn,zz=0,1,1
                else: pp,nn,zz=0,0,2
            blocks.append({
                "start":i,"size":2,
                "trace_sign":st,"det_sign":sd,
                "inertia":[pp,zz,nn],
            })
            pos+=pp; neg+=nn; zero+=zz
            i+=2
        else:
            s=field_real_sign(S,D[i,i])
            if s>0: pos+=1; it=[1,0,0]
            elif s<0: neg+=1; it=[0,0,1]
            else: zero+=1; it=[0,1,0]
            blocks.append({
                "start":i,"size":1,"sign":s,"inertia":it
            })
            i+=1
    return pos,zero,neg,blocks


def find_negative_D_vector(S,D,blocks):
    """
    Return y with y^* D y < 0 if D has a negative block.
    """
    K=S["K"]; vector=S["vector"]; AA=S["AA"]
    n=D.nrows()

    for rec in blocks:
        if rec["inertia"][2]==0:
            continue
        i=rec["start"]
        y=vector(K,[0]*n)

        if rec["size"]==1:
            y[i]=1
        else:
            a=D[i,i]; b=D[i,i+1]; c=D[i+1,i+1]
            if field_real_sign(S,a)<0:
                y[i]=1
            elif field_real_sign(S,c)<0:
                y[i+1]=1
            elif field_real_sign(S,a)>0:
                # [b,-a] has value a*det < 0 for det<0.
                y[i]=b
                y[i+1]=-a
            else:
                # a=0, det=-|b|^2<0.  Search integer n:
                # y=(-n*b,1) gives c-2n|b|^2.
                bb=b*b.conjugate()
                found=False
                for m in [1,2,4,8,16,32,64,128,256,512,1024,2048]:
                    y[i]=-m*b
                    y[i+1]=1
                    val=(y.conjugate()*D*y)[0]
                    if field_real_sign(S,val)<0:
                        found=True
                        break
                if not found:
                    die("could not construct exact negative 2x2 D vector")

        val=(y.conjugate()*D*y)[0]
        if field_real_sign(S,val)>=0:
            die("constructed D negative vector is not negative")
        return y,val

    return None,None


def exact_inertia_certificate(S,Kblock):
    if Kblock != Kblock.conjugate_transpose():
        die("K block not exactly Hermitian")

    P,L,D=Kblock.block_ldlt()

    lhs=P.conjugate_transpose()*Kblock*P
    rhs=L*D*L.conjugate_transpose()
    if lhs != rhs:
        die("exact block LDL identity failed")

    pos,zero,neg,db=scan_D_inertia(S,D)

    rec={
        "dimension":Kblock.nrows(),
        "inertia_positive_zero_negative":[int(pos),int(zero),int(neg)],
        "Kblock_sha256":hash_K_matrix(Kblock),
        "LDL_P_sha256":hash_K_matrix(P),
        "LDL_L_sha256":hash_K_matrix(L),
        "LDL_D_sha256":hash_K_matrix(D),
        "D_block_inertias":db,
        "exact_factor_identity":True,
    }

    return rec,(P,L,D)


# ============================================================================
# Main
# ============================================================================

def main(argv):
    if len(argv)!=6:
        die(
            "usage: sage -python h4_K_alpha23_exact_ldlt.py "
            "MAT SYSTEM_JSON COMPLETE_K_JSON "
            "h4_nogap_irrep_cache.py h4_K_full_dual_slice_release.py"
        )

    mat_path,system_path,complete_path,nogap_path,dualbase_path=argv[1:]

    if sha256_file(nogap_path)!=EXPECTED_NOGAP_SHA:
        die("no-GAP source SHA mismatch")
    if sha256_file(dualbase_path)!=EXPECTED_DUALBASE_SHA:
        die("dual-base source SHA mismatch")

    base=load_module(dualbase_path,"h4dualbase")
    ng=load_module(nogap_path,"h4nogap")
    S=sage_setup()

    if md5_file(mat_path)!=EXPECTED_MD5:
        die("MAT MD5 mismatch")

    with h5py.File(mat_path,"r") as f:
        A=exact_int_matrix(f["A"][()],"A")
        Pfloat=np.asarray(f["P"][()],dtype=np.float64)
        ax=exact_sign_vector(f["ax"][()],"ax")
        by=exact_sign_vector(f["by"][()],"by")

    if canonical_A_sha(A)!=EXPECTED_A_SHA:
        die("A SHA mismatch")
    if not np.array_equal(A,A.T):
        die("A not symmetric")

    Cw=sum(
        int(ax[i])*int(A[i,j])*int(by[j])
        for i in range(N) for j in range(N)
    )
    if Cw!=EXPECTED_C:
        die("archived witness C mismatch")

    with open(complete_path,"rb") as f:
        complete_bytes=f.read()
    complete=json.loads(complete_bytes)
    if complete.get("final_status")!="PROVED_COMPLETE_K_DECOMPOSITION":
        die("complete-K status is not proved")
    if complete.get("isotypic_table_sha256")!=EXPECTED_ISOTYPIC_SHA:
        die("complete-K isotypic hash mismatch")

    blocks=complete.get("isotypic_blocks")
    if not isinstance(blocks,list) or len(blocks)!=34:
        die("complete-K JSON must contain 34 isotypic blocks")
    byid={int(r["gap_irrep_id"]):r for r in blocks}
    surv=sorted(
        int(r["m_K_if_certified"])
        for r in blocks if int(r["m_K_if_certified"])>0
    )
    if surv!=EXPECTED_SURVIVING_BLOCKS_SORTED:
        die("surviving K block multiset mismatch")

    # Reconstruct exact P = (PX+PY sqrt5)/PD from the already-audited routine.
    Pex=base.reconstruct_P_exact_and_AP(A,Pfloat)
    PX=np.asarray(Pex["X"],dtype=np.int64)
    PY=np.asarray(Pex["Y"],dtype=np.int64)
    PD=int(Pex["D"])

    # Exact separation normalization.
    # N-C = (NUM_A-C)+NUM_B sqrt5 > 0.
    da=NUM_A-EXPECTED_C
    db=NUM_B
    if not (db>0 and 5*db*db > da*da):
        die("exact separation sign check failed")
    sep_square_gap=5*db*db-da*da

    # Structural group and certified action.
    Q,Qdata,G,Hdata,ff=ng.structural_construction()
    system,cert_elements,cert_gens,action_sha=ng.load_and_match_certified_action(
        system_path,G
    )
    if action_sha!=EXPECTED_ACTION_SHA:
        die("certified action SHA mismatch")
    if len(G["elements"])!=ORDER:
        die("structural H4 order mismatch")

    print("building exact 2I/H4 representation models",file=sys.stderr)
    Qreps,q_audit=build_exact_Q_irreps(Q,Qdata)

    # Exact line-pair D data and residual equality seeds.
    base.init_pairs()
    pair_rel,pair_records=base.enumerate_pair_support_orbits(cert_gens)

    hright=[
        sum(int(ax[i])*int(A[i,j]) for i in range(N))
        for j in range(N)
    ]
    Zlines=[j for j,h in enumerate(hright) if h==0]
    if Zlines!=[46,56,85,99,131,148]:
        die("zero-field set mismatch")

    killed_ids,killed_bool=base.killed_pair_data(pair_rel,Zlines)
    faceR=base.Face(ax,by,"y",Zlines)
    faceL=base.Face(by,ax,"x",Zlines)

    Rseed_float=np.vstack([
        base.direct_residual_seed_matrix(faceR,killed_bool),
        base.direct_residual_seed_matrix(faceL,killed_bool),
    ])
    Rseed=np.rint(Rseed_float).astype(np.int64)
    if not np.array_equal(Rseed_float,Rseed.astype(float)):
        die("residual seed matrix is not exactly integral")

    orbit_rel,orbit_records=base.enumerate_W_orbits(
        cert_gens,pair_rel,set(killed_ids)
    )
    Ddim=sum(r["size"] for r in orbit_records if r["in_D"])
    if Ddim!=13200:
        die("D dimension != 13200")

    idx=np.arange(NV)%N
    X6=PX[np.ix_(idx,idx)]
    Y6=PY[np.ix_(idx,idx)]

    results=[]
    any_negative=False
    negative_witnesses=[]

    with tempfile.TemporaryDirectory(prefix="h4alpha23_") as td:
        for ri,meta in enumerate(Hdata["irreps"]):
            exact=byid[ri+1]
            mK=int(exact["m_K_if_certified"])
            if mK==0:
                results.append({
                    "gap_irrep_id":ri+1,
                    "degree":int(meta["degree"]),
                    "mK":0,
                    "status":"ZERO_K_BLOCK",
                })
                continue

            d=int(meta["degree"])
            mWD=int(exact["m_W_minus_D_exact"])
            expected_rank=mWD-mK

            print(
                "irrep %d/34 d=%d m(W-D)=%d mK=%d"
                %(ri+1,d,mWD,mK),
                file=sys.stderr
            )

            Rcomp,paths,rhoden,metric,rmax=build_R_components(
                meta,Qreps,G,td,"irrep%02d"%(ri+1)
            )

            # Exact fixed-space bases for every non-D orbit.
            active=[]
            copy_total=0
            for rec0 in orbit_records:
                if rec0["in_D"]:
                    continue
                V,inds,chars=exact_projector_basis(
                    S,base,Rcomp,rec0,cert_elements,d
                )
                if V is None or V.ncols()==0:
                    continue
                rr=dict(rec0)
                rr["V"]=V
                rr["stab_indices"]=inds
                rr["stab_chars"]=chars
                rr["copy_start"]=copy_total
                rr["copy_end"]=copy_total+V.ncols()
                rr["fixed_dim"]=V.ncols()
                active.append(rr)
                copy_total+=V.ncols()

            if copy_total!=mWD:
                die(
                    "irrep %d exact orbit multiplicity %d != complete-K mWD %d"
                    %(ri+1,copy_total,mWD)
                )

            print("    exact residual map C",file=sys.stderr)
            Cmat=build_exact_C(
                S,base,Rcomp,active,Rseed,cert_elements,d,mWD
            )
            Crank=Cmat.rank()
            if Crank!=expected_rank:
                die(
                    "irrep %d exact C rank %d != expected %d"
                    %(ri+1,Crank,expected_rank)
                )

            Kspace=Cmat.right_kernel()
            Zbasis=Kspace.basis_matrix().transpose()
            if Zbasis.ncols()!=mK:
                die("irrep %d exact K kernel dimension mismatch"%(ri+1))
            if Cmat*Zbasis != S["zero"](S["K"],Cmat.nrows(),mK):
                die("irrep %d exact C*Z != 0"%(ri+1))

            print("    exact moment form B for alpha=2/3",file=sys.stderr)
            Bmat=build_exact_B(
                S,base,Rcomp,active,cert_elements,
                X6,Y6,PD,metric,d,mWD
            )

            print("    exact K compression and block LDL*",file=sys.stderr)
            Kblock=Zbasis.conjugate_transpose()*Bmat*Zbasis
            cert,fac=exact_inertia_certificate(S,Kblock)
            Pld,Lld,Dld=fac

            cert.update({
                "gap_irrep_id":ri+1,
                "degree":d,
                "m_W_minus_D_exact":mWD,
                "residual_rank_exact":Crank,
                "mK":mK,
                "active_orbit_modules":len(active),
                "representation_common_denominator":int(rhoden),
                "representation_max_integer_numerator":int(rmax),
                "C_sha256":hash_K_matrix(Cmat),
                "K_basis_sha256":hash_K_matrix(Zbasis),
                "B_sha256":hash_K_matrix(Bmat),
                "exact_kernel_audit":True,
            })

            pos,zero,neg=cert["inertia_positive_zero_negative"]
            if pos+zero+neg!=mK:
                die("inertia dimension sum failed")

            if neg:
                any_negative=True

                y,dval=find_negative_D_vector(
                    S,Dld,cert["D_block_inertias"]
                )
                # xK is vector in Kblock basis, then xWD in W-D multiplicity.
                # P^* K P = L D L^*, z=L^{-H}y, xK=P z.
                z=Lld.conjugate_transpose().solve_right(y)
                xK=Pld*z
                xWD=Zbasis*xK

                if Cmat*xWD != S["vector"](S["K"],[0]*Cmat.nrows()):
                    die("reported negative vector is not in exact kernel")
                qv=(xWD.conjugate()*Bmat*xWD)[0]
                if field_real_sign(S,qv)>=0:
                    die("reported exact negative vector is not negative")

                wrec={
                    "gap_irrep_id":ri+1,
                    "degree":d,
                    "quadratic_value":str(qv),
                    "quadratic_value_sign":-1,
                    "multiplicity_vector":[
                        str(v) for v in xWD
                    ],
                }
                wraw=json.dumps(
                    wrec,sort_keys=True,separators=(",",":")
                ).encode()
                wrec["witness_sha256"]=hashlib.sha256(wraw).hexdigest()
                negative_witnesses.append(wrec)

            results.append(cert)

            # Remove large exact/numeric objects before the next irrep.
            del Cmat,Zbasis,Bmat,Kblock,Pld,Lld,Dld
            del Rcomp
            for p in paths:
                try:
                    os.remove(p)
                except OSError:
                    pass

    # Exact objective.
    objective={
        "rational_part":str(Fraction(EXPECTED_C-NUM_A)),
        "sqrt5_part":str(Fraction(-NUM_B)),
        "sign_exact":-1,
        "equivalent_positive_N_minus_C_rational_part":str(Fraction(da)),
        "equivalent_positive_N_minus_C_sqrt5_part":str(Fraction(db)),
        "N_minus_C_square_gap_5b2_minus_a2":str(sep_square_gap),
    }

    if any_negative:
        status="REFUTED_ALPHA_2_OVER_3"
        proof_status="PROVED_EXACT_NEGATIVE_K_BLOCK"
    else:
        if len([r for r in results if r.get("mK",0)>0])!=20:
            die("did not certify exactly 20 nonzero K blocks")
        if any(
            r["inertia_positive_zero_negative"][2] != 0
            for r in results if r.get("mK",0)>0
        ):
            die("internal negative-inertia inconsistency")
        status="PROVED_DEGREE4_DUAL_SEPARATOR"
        proof_status="PROVED"

    out={
        "status":status,
        "proof_status":proof_status,
        "moment_functional":{
            "boolean_reduction":"reduce repeated variables first: z_i^2=1",
            "L_empty":"1",
            "L_odd":"0 for squarefree degree 1 or 3",
            "L_degree2":"X_ab",
            "L_four_distinct":"(2/3)*(X_ab*X_cd+X_ac*X_bd+X_ad*X_bc)",
            "X":"[[P,P],[P,P]]",
        },
        "separation":objective,
        "provenance":{
            "mat_md5":EXPECTED_MD5,
            "A_sha256":EXPECTED_A_SHA,
            "action_sha256":EXPECTED_ACTION_SHA,
            "complete_K_isotypic_table_sha256":EXPECTED_ISOTYPIC_SHA,
            "nogap_source_sha256":EXPECTED_NOGAP_SHA,
            "dualbase_source_sha256":EXPECTED_DUALBASE_SHA,
        },
        "exact_representation_audit":q_audit,
        "complete_K":{
            "dimension":149701,
            "D_rank":13200,
            "equality_restriction_rank":30600,
            "nonzero_block_count":20,
            "surviving_block_sizes":EXPECTED_SURVIVING_BLOCKS_SORTED,
        },
        "per_irrep":results,
        "negative_witnesses":negative_witnesses,
        "preserved_facts":{
            "prior_invariant_seed_SOS_test":"INCONCLUSIVE",
            "invariant_vanishing_dimension":43,
            "rank4_full_elliptope_extension":"PROVED_IMPOSSIBLE",
        },
    }

    raw=json.dumps(
        out,sort_keys=True,separators=(",",":")
    ).encode()
    outpath=mat_path+".K_alpha23_exact_ldlt.json"
    with open(outpath,"wb") as f:
        f.write(raw)

    display=dict(out)
    display["output_path"]=outpath
    display["output_sha256"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(display,indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    sys.exit(main(sys.argv))
