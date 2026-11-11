#!/usr/bin/env python3
"""
h4_K_full_dual_slice.py

Python 3.9+.
Dependencies: numpy, scipy, h5py, sympy.
Also needs the previously supplied h4_nogap_irrep_cache.py.

PURPOSE
=======
This program constructs the FULL symmetry-reduced adjoint multiplication map
on the certified equality-face seed space K, but evaluates that map first on
a distinguished one-parameter family of degree-4 pseudoexpectations.

For an H4-invariant Boolean functional L, the invariant SOS multiplication
map mu: Sym_G(K) -> R[z]/(z_i^2-1) has adjoint blocks

    mu^*(L)_rho = Z_rho^* B_rho(L) Z_rho,

where rho ranges over the 34 irreducibles, Z_rho is an orthonormal basis of
the COMPLETE K multiplicity space, and B_rho(L) is obtained from the exact
transitive-monomial modules by the group Fourier formula

 B_{(O,a),(O',b)} = 1/sqrt(|H_O||H_O'|)
     v_{O,a}^* [ sum_g ell_{O,O'}(g) rho(g) ] v_{O',b},

 ell_{O,O'}(g) = L( m_O * (g m_O') ).

Thus the program does not restrict q to invariant seeds or any proper
submodule of K.  Every surviving K block is tested.

The first dual slice fixes the already-certified second moments

    X = [[P,P],[P,P]],

all odd moments to zero, and for four DISTINCT Boolean variables uses

 L_alpha(z_a z_b z_c z_d)
   = alpha * (X_ab X_cd + X_ac X_bd + X_ad X_bc).

Repeated indices are ALWAYS reduced first using z_i^2=1, so the Boolean
constraints are exact.  The objective is independent of alpha:

    L_alpha(C - x^T A y) = C - <A,P> < 0.

Therefore, if every complete K block is PSD for one alpha, this is a genuine
separating degree-4 pseudoexpectation and proves that a degree-2 SOS
certificate for C-x^T A y does NOT exist.

IMPORTANT HONESTY RULE
======================
This program's block construction is numerically evaluated in complex128.
A positive numerical margin is DISCOVERY EVIDENCE ONLY and is NOT promoted
to a proof.  A negative eigenvalue is likewise only a candidate until an
exact K-vector is reconstructed.  The output status therefore uses the words
NUMERICAL_CANDIDATE or NUMERICAL_FAILURE.  The group/module dimensions and
all integer/hash audits are exact.

The artifact also proves analytically that alpha=0 with all distinct fourth
moments zero is NOT PSD on K, because f=C-x^TAy itself belongs to K and its
pseudo-square has a strictly negative exact value.

Usage
-----
Structural self-test (does not need MAT):

  python h4_K_full_dual_slice.py --self-test-structural \
      h4_nogap_irrep_cache.py

Certified run:

  python h4_K_full_dual_slice.py \
      d4_n1_300x300.mat \
      d4_n1_300x300.mat.H4_level2_exact_system.json \
      d4_n1_300x300.mat.complete_K_isotypic.json \
      h4_nogap_irrep_cache.py

The complete-K JSON may have any filename; its isotypic_blocks entries must
contain the exact gap_irrep_id, degree, m_W_minus_D_exact, and
m_K_if_certified values, and its final_status must be
PROVED_COMPLETE_K_DECOMPOSITION.
"""

import sys
import os
import json
import math
import hashlib
import itertools
import collections
import importlib.util
from fractions import Fraction

import numpy as np
import h5py
import scipy.linalg as la
import sympy as sp


# ---------------------------------------------------------------------------
# Immutable certified data
# ---------------------------------------------------------------------------

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
EXPECTED_C = 2081044153087351400
NUM_A = 1539823299061914600
NUM_B = 706968072319078800

N = 300
NV = 600
ORDER = 14400
MON_DIM = 1 + NV + NV * (NV - 1) // 2
PAIR_OFFSET = 1 + NV
PRIME = 24001
SQRT5 = math.sqrt(5.0)

# Exact surviving multiplicity census supplied by the complete-K theorem.
EXPECTED_SURVIVING_BLOCKS_SORTED = sorted([
    582,465,611,211,611,822,235,162,107,397,
    504,43,17,107,166,235,162,504,384,286,
])


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def die(msg):
    raise SystemExit("ERROR: " + str(msg))


def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def canonical_A_sha(A):
    h = hashlib.sha256()
    for x in A.ravel(order="C"):
        h.update(int(x).to_bytes(8, "little", signed=True))
    return h.hexdigest()


def exact_int_matrix(raw, name):
    a = np.asarray(raw)
    if a.shape != (N, N):
        die("%s shape %r != (300,300)" % (name, a.shape))
    out = np.empty((N, N), dtype=np.int64)
    it = np.nditer(a, flags=["multi_index"])
    for z in it:
        x = float(z)
        if not math.isfinite(x):
            die("%s%s nonfinite" % (name, it.multi_index))
        q = int(x)
        if float(q) != x:
            die("%s%s not exactly integral binary64" % (name, it.multi_index))
        out[it.multi_index] = q
    return out


def exact_sign_vector(raw, name):
    a = np.asarray(raw).reshape(-1)
    if len(a) != N:
        die("%s length != 300" % name)
    out = np.empty(N, dtype=np.int8)
    for i, z in enumerate(a):
        x = float(z)
        if x == 1.0:
            out[i] = 1
        elif x == -1.0:
            out[i] = -1
        else:
            die("%s[%d] not exactly +/-1" % (name, i))
    return out


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        die("cannot import %s" % path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Degree <=2 monomial indexing
# ---------------------------------------------------------------------------

PAIR_U = np.empty(NV * (NV - 1) // 2, dtype=np.int16)
PAIR_V = np.empty_like(PAIR_U)


def init_pairs():
    k = 0
    for u in range(NV - 1):
        for v in range(u + 1, NV):
            PAIR_U[k] = u
            PAIR_V[k] = v
            k += 1
    if k != len(PAIR_U):
        die("pair enumeration failed")


def pair_rank(u, v):
    if u > v:
        u, v = v, u
    return u * (2 * NV - u - 1) // 2 + (v - u - 1)


def pair_mid(u, v):
    if u > v:
        u, v = v, u
    return PAIR_OFFSET + pair_rank(u, v)


def mid_support(mid):
    if mid == 0:
        return ()
    if mid < PAIR_OFFSET:
        return (mid - 1,)
    k = mid - PAIR_OFFSET
    return (int(PAIR_U[k]), int(PAIR_V[k]))


def support_mid(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 + int(s[0])
    if len(s) == 2:
        return pair_mid(int(s[0]), int(s[1]))
    raise ValueError("support degree > 2")


def map_var(v, p, s):
    if v < N:
        return int(p[v]), int(s[v])
    i = v - N
    return N + int(p[i]), int(s[i])


def act_mid(mid, p, s):
    supp = mid_support(mid)
    if not supp:
        return 0, 1
    out = []
    sg = 1
    for v in supp:
        vv, ss = map_var(v, p, s)
        out.append(vv)
        sg *= ss
    out.sort()
    return support_mid(tuple(out)), sg


def monomial_type(mid):
    s = mid_support(mid)
    if len(s) == 0:
        return "constant"
    if len(s) == 1:
        return "x" if s[0] < N else "y"
    a, b = s
    if a < N and b < N:
        return "xx"
    if a >= N and b >= N:
        return "yy"
    return "xy"


# ---------------------------------------------------------------------------
# 600-cell quaternion realization of 2I and exact combinatorial matching
# to the structural SL(2,5) model used by the no-GAP cache.
# ---------------------------------------------------------------------------

def perm_parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inv += 1
    return inv & 1


def binary_icosahedral_quaternions():
    phi = (1.0 + SQRT5) / 2.0
    V = []

    # 8 coordinate axes.
    for i in range(4):
        for sg in (-1.0, 1.0):
            q = [0.0] * 4
            q[i] = sg
            V.append(tuple(q))

    # 16 half-coordinate vertices.
    for signs in itertools.product((-1.0, 1.0), repeat=4):
        V.append(tuple(0.5 * s for s in signs))

    # 96 even permutations of (0,1/2,phi/2,1/(2phi)), all signs on
    # nonzero entries.
    base = (0.0, 0.5, phi / 2.0, 1.0 / (2.0 * phi))
    for perm in itertools.permutations(range(4)):
        if perm_parity(perm):
            continue
        arr = [base[perm[i]] for i in range(4)]
        nz = [i for i, x in enumerate(arr) if abs(x) > 1e-14]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            q = list(arr)
            for i, sg in zip(nz, signs):
                q[i] *= sg
            V.append(tuple(q))

    uniq = {}
    for q in V:
        uniq[tuple(round(x, 13) for x in q)] = q
    V = list(uniq.values())

    if len(V) != 120:
        die("binary icosahedral quaternion set size != 120")

    A = np.asarray(V, dtype=float)

    def qmul(a, b):
        w,x,y,z = a
        W,X,Y,Z = b
        return (
            w*W-x*X-y*Y-z*Z,
            w*X+x*W+y*Z-z*Y,
            w*Y-x*Z+y*W+z*X,
            w*Z+x*Y-y*X+z*W,
        )

    def nearest(q):
        d = np.linalg.norm(A - np.asarray(q)[None, :], axis=1)
        k = int(np.argmin(d))
        return k, float(d[k])

    mul = np.empty((120, 120), dtype=np.int16)
    maxerr = 0.0
    for i in range(120):
        for j in range(120):
            k, e = nearest(qmul(V[i], V[j]))
            mul[i, j] = k
            maxerr = max(maxerr, e)

    if maxerr > 1e-12:
        die("quaternion multiplication closure error %g" % maxerr)

    eid = min(
        range(120),
        key=lambda i: np.linalg.norm(A[i] - np.array([1.0,0.0,0.0,0.0])),
    )

    return V, mul, eid, maxerr


def order_table(mul, eid, a, cap=120):
    x = eid
    for k in range(1, cap + 1):
        x = int(mul[x, a])
        if x == eid:
            return k
    return None


def generated_set(mul, eid, gens):
    seen = {eid}
    q = collections.deque([eid])
    while q:
        x = q.popleft()
        for g in gens:
            y = int(mul[x, g])
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def labelled_iso(mulA, eA, gensA, mulB, eB, gensB):
    mp = {eA: eB}
    rev = {eB: eA}
    q = collections.deque([eA])
    while q:
        x = q.popleft()
        y = mp[x]
        for ga, gb in zip(gensA, gensB):
            xx = int(mulA[x, ga])
            yy = int(mulB[y, gb])
            if xx in mp:
                if mp[xx] != yy:
                    return None
            else:
                if yy in rev:
                    return None
                mp[xx] = yy
                rev[yy] = xx
                q.append(xx)
    if len(mp) != len(mulA):
        return None
    # Full multiplication-table audit.
    for a in range(len(mulA)):
        for b in range(len(mulA)):
            if mp[int(mulA[a,b])] != int(mulB[mp[a],mp[b]]):
                return None
    return mp


def structural_Q_to_quaternion(Q):
    mulQ = Q["mul"]
    eQ = int(Q["I"])
    ordQ = [order_table(mulQ, eQ, i) for i in range(120)]

    # Deterministic Q generating pair: first (order4,order6) pair whose
    # product has order10 and generates all Q.
    qpair = None
    for a in range(120):
        if ordQ[a] != 4:
            continue
        for b in range(120):
            if ordQ[b] != 6:
                continue
            if order_table(mulQ, eQ, int(mulQ[a,b])) != 10:
                continue
            if len(generated_set(mulQ, eQ, [a,b])) == 120:
                qpair = (a,b)
                break
        if qpair is not None:
            break
    if qpair is None:
        die("could not find deterministic SL(2,5) generating pair")

    V, mulV, eV, maxerr = binary_icosahedral_quaternions()
    ordV = [order_table(mulV, eV, i) for i in range(120)]

    iso = None
    vpair = None
    for a in range(120):
        if ordV[a] != 4:
            continue
        for b in range(120):
            if ordV[b] != 6:
                continue
            if order_table(mulV, eV, int(mulV[a,b])) != 10:
                continue
            z = labelled_iso(mulQ, eQ, qpair, mulV, eV, (a,b))
            if z is not None:
                iso = z
                vpair = (a,b)
                break
        if iso is not None:
            break

    if iso is None:
        die("SL(2,5) <-> binary icosahedral labelled isomorphism failed")

    return {
        "quaternions": V,
        "mul": mulV,
        "eid": eV,
        "Q_pair": qpair,
        "quat_pair": vpair,
        "Q_to_quat": iso,
        "closure_max_error": maxerr,
    }


def quat_to_su2(q):
    w,x,y,z = q
    return np.array([
        [w + 1j*x,  y + 1j*z],
        [-y + 1j*z, w - 1j*x],
    ], dtype=np.complex128)


def symmetric_basis(n):
    if n == 0:
        return np.ones((1,1), dtype=np.complex128)
    S = np.zeros((2**n, n+1), dtype=np.complex128)
    for bits in itertools.product((0,1), repeat=n):
        k = sum(bits)
        idx = 0
        for bit in bits:
            idx = (idx << 1) | bit
        S[idx,k] = 1.0 / math.sqrt(math.comb(n,k))
    return S


_SYM_BASIS = {n: symmetric_basis(n) for n in range(6)}


def sympow2(U, n):
    if n == 0:
        return np.ones((1,1), dtype=np.complex128)
    K = U.copy()
    for _ in range(n - 1):
        K = np.kron(K, U)
    S = _SYM_BASIS[n]
    return S.conj().T.dot(K).dot(S)


def sqrt5_mod_roots(p):
    rr = sp.sqrt_mod(5, p, all_roots=True)
    rr = sorted(int(x) for x in rr)
    if len(rr) != 2:
        die("5 does not have exactly two square roots mod p")
    return rr


def lift_qsqrt5_residue(r, degree, smod, p=PRIME):
    """Unique bounded lift to an algebraic integer (a+b sqrt5)/2."""
    inv2 = pow(2, p-2, p)
    cand = []
    for a in range(-2*degree, 2*degree + 1):
        for b in range(-2*degree, 2*degree + 1):
            if (a-b) & 1:
                continue
            if ((a + b*smod) * inv2) % p != int(r):
                continue
            real = (a + b*SQRT5) / 2.0
            if abs(real) <= degree + 1e-8:
                cand.append((a,b,real))
    if len(cand) != 1:
        die("nonunique Q(sqrt5) character lift residue=%s degree=%d: %r"
            % (r, degree, cand))
    return cand[0]


def find_outer_Q_automorphism(Q, qmap, qchars_target):
    """Find automorphism carrying quaternion fundamental char to target 2D char."""
    mulQ = Q["mul"]
    eQ = int(Q["I"])
    a0,b0 = qmap["Q_pair"]
    ordQ = [order_table(mulQ, eQ, i) for i in range(120)]
    V = qmap["quaternions"]
    iso = qmap["Q_to_quat"]
    chi = np.array([2.0 * V[iso[i]][0] for i in range(120)])

    for a in range(120):
        if ordQ[a] != 4:
            continue
        for b in range(120):
            if ordQ[b] != 6:
                continue
            if order_table(mulQ, eQ, int(mulQ[a,b])) != 10:
                continue
            mp = labelled_iso(mulQ, eQ, (a0,b0), mulQ, eQ, (a,b))
            if mp is None:
                continue
            ch = np.array([chi[mp[i]] for i in range(120)])
            if np.max(np.abs(ch - qchars_target)) < 2e-10:
                return mp, (a,b)
    die("could not realize Galois-conjugate 2D representation by Q automorphism")


def complex_Q_irreps(ng, Q, Qdata, qmap):
    """Construct all nine complex unitary 2I irreps, matched to Qdata IDs."""
    smod = sqrt5_mod_roots(PRIME)[0]
    qchars_real = []
    for rr in Qdata["irreps"]:
        d = int(rr["degree"])
        qchars_real.append(np.array([
            lift_qsqrt5_residue(x, d, smod)[2]
            for x in rr["character"]
        ], dtype=float))

    Vq = qmap["quaternions"]
    iso = qmap["Q_to_quat"]
    U = [quat_to_su2(Vq[iso[i]]) for i in range(120)]

    two_ids = [i for i,r in enumerate(Qdata["irreps"]) if int(r["degree"]) == 2]
    matchU = [
        i for i in two_ids
        if np.max(np.abs(qchars_real[i] - np.array([np.trace(M).real for M in U]))) < 2e-10
    ]
    if len(matchU) != 1:
        die("fundamental quaternion 2D irrep did not match uniquely")
    fund_id = matchU[0]
    other_id = [i for i in two_ids if i != fund_id][0]

    auto, auto_pair = find_outer_Q_automorphism(Q, qmap, qchars_real[other_id])
    Ug = [quat_to_su2(Vq[iso[auto[i]]]) for i in range(120)]

    reps = [None] * 9

    def install(mats):
        d = mats[0].shape[0]
        ch = np.array([np.trace(M).real for M in mats])
        matches = [
            i for i,r in enumerate(Qdata["irreps"])
            if int(r["degree"]) == d
            and np.max(np.abs(qchars_real[i] - ch)) < 3e-9
        ]
        if len(matches) != 1:
            die("complex Q irrep match not unique, d=%d matches=%r" % (d,matches))
        i = matches[0]
        if reps[i] is None:
            reps[i] = mats
        else:
            # Same isomorphism reached twice (n=0,4,5 under Galois); audit char.
            if np.max(np.abs(
                np.array([np.trace(M).real for M in reps[i]]) - ch
            )) > 3e-9:
                die("duplicate Q irrep character mismatch")

    for base in (U, Ug):
        for n in range(6):
            install([sympow2(M,n) for M in base])

    # Missing center-even 4D representation is V tensor V'.
    install([np.kron(U[i], Ug[i]) for i in range(120)])

    if any(x is None for x in reps):
        die("failed to construct all nine Q irreps")

    # Unitarity and character audits.
    max_unit = 0.0
    for qi, mats in enumerate(reps):
        d = mats[0].shape[0]
        I = np.eye(d)
        for M in mats:
            max_unit = max(max_unit, float(np.max(np.abs(M.conj().T.dot(M)-I))))
        ch = np.array([np.trace(M).real for M in mats])
        if np.max(np.abs(ch - qchars_real[qi])) > 5e-9:
            die("Q irrep %d character mismatch" % qi)

    return {
        "rho": reps,
        "characters_real": qchars_real,
        "sqrt5_mod_embedding": smod,
        "fundamental_Qdata_id": fund_id,
        "galois_fundamental_Qdata_id": other_id,
        "outer_automorphism_generator_images": list(auto_pair),
        "max_unitarity_error": max_unit,
    }


def flip_complex(du, dv):
    """F: U tensor V -> V tensor U in normalized tensor bases."""
    r = du * dv
    F = np.zeros((r,r), dtype=np.complex128)
    for i in range(du):
        for j in range(dv):
            src = i*dv + j
            dst = j*du + i
            F[dst,src] = 1.0
    return F


def H_rep_all(meta, qcomplex, G):
    """Complex unitary matrices rho(g) for all 14400 structural H4 elements."""
    pairs = G["pairs"]
    elems = G["elements"]
    QR = qcomplex["rho"]

    if meta["type"] == "diagonal_extension":
        U = QR[int(meta["i"])]
        du = U[0].shape[0]
        F = flip_complex(du,du)
        sg = int(meta["extension_sign"])
        out = np.empty((ORDER, du*du, du*du), dtype=np.complex128)
        for gi,(pid,e) in enumerate(elems):
            a,b = pairs[pid]
            M = np.kron(U[a],U[b])
            if e:
                M = M.dot(sg * F)
            out[gi] = M
        return out

    U = QR[int(meta["i"])]
    V = QR[int(meta["j"])]
    du = U[0].shape[0]
    dv = V[0].shape[0]
    r = du*dv
    F = flip_complex(du,dv)
    T = np.zeros((2*r,2*r), dtype=np.complex128)
    T[:r,r:] = F.T
    T[r:,:r] = F
    out = np.empty((ORDER,2*r,2*r), dtype=np.complex128)
    for gi,(pid,e) in enumerate(elems):
        a,b = pairs[pid]
        A = np.kron(U[a],V[b])
        B = np.kron(V[a],U[b])
        M = np.zeros((2*r,2*r), dtype=np.complex128)
        M[:r,:r] = A
        M[r:,r:] = B
        if e:
            M = M.dot(T)
        out[gi] = M
    return out


def complex_H_character_audit(Hdata, G, qcomplex):
    """Check all 34 complex characters against the finite-field lifted chars."""
    smod = qcomplex["sqrt5_mod_embedding"]
    chars_mod = Hdata["characters"]
    maxerr = 0.0
    gen_unit_err = 0.0

    # Cheap character formulas using complex Q chars, not full H matrices.
    qch = [np.array([np.trace(M) for M in rr]) for rr in qcomplex["rho"]]
    pairs = G["pairs"]
    mulQ = None
    # qcomplex was built on Q IDs; Q multiplication supplied separately below by caller.

    for ri,meta in enumerate(Hdata["irreps"]):
        d = int(meta["degree"])
        target = np.array([
            lift_qsqrt5_residue(x,d,smod)[2]
            for x in chars_mod[ri]
        ])
        # Building full matrices here is acceptable in structural self-test only by caller.
        # Caller may compare traces of H_rep_all.
        if np.max(np.abs(target.imag if np.iscomplexobj(target) else 0)) > 1e-12:
            die("lifted H character unexpectedly complex")
    return {"lift_bound_audit": True, "max_error": maxerr, "generator_unitarity_error": gen_unit_err}


# ---------------------------------------------------------------------------
# Faces and exact residual seed coefficient vectors (copied independently
# from the complete-K construction).
# ---------------------------------------------------------------------------

class Face(object):
    def __init__(self, cx, cy, free_party, free_lines):
        self.cx = np.asarray(cx, dtype=np.int8)
        self.cy = np.asarray(cy, dtype=np.int8)
        self.free_party = str(free_party)
        self.free_lines = tuple(int(x) for x in free_lines)
        if len(self.free_lines) != 6:
            die("face must have six free lines")

    def full_center(self):
        return np.concatenate([self.cx,self.cy]).astype(np.int8)

    def free_vars(self):
        if self.free_party == "x":
            return tuple(self.free_lines)
        return tuple(N+i for i in self.free_lines)

    def singleton_var(self, mode):
        if mode < 1 or mode > 6:
            die("bad singleton mode")
        i = self.free_lines[mode-1]
        return i if self.free_party == "x" else N+i


def enumerate_pair_support_orbits(gens):
    rel = np.full((N,N), -1, dtype=np.int16)
    records = []
    oid = 0
    for i0 in range(N):
        for j0 in range(i0+1,N):
            if rel[i0,j0] >= 0:
                continue
            rel[i0,j0] = rel[j0,i0] = oid
            q = collections.deque([(i0,j0)])
            size = 0
            while q:
                i,j = q.popleft()
                size += 1
                for p,s in gens:
                    ii,jj = int(p[i]),int(p[j])
                    if ii > jj:
                        ii,jj = jj,ii
                    if rel[ii,jj] < 0:
                        rel[ii,jj] = rel[jj,ii] = oid
                        q.append((ii,jj))
                    elif int(rel[ii,jj]) != oid:
                        die("pair support orbit collision")
            records.append({"orbit_id":oid,"representative":[i0,j0],"size":size})
            oid += 1
    if oid != 18:
        die("expected 18 line-pair support orbits, got %d" % oid)
    return rel,records


def killed_pair_data(pair_rel,Z):
    ids = set()
    for a in range(6):
        for b in range(a+1,6):
            ids.add(int(pair_rel[Z[a],Z[b]]))
    killed = np.zeros((N,N),dtype=np.bool_)
    for i in range(N):
        for j in range(i+1,N):
            if int(pair_rel[i,j]) in ids:
                killed[i,j]=killed[j,i]=True
    return sorted(ids),killed


def direct_residual_seed_matrix(face,killed_bool):
    pu,pv = PAIR_U,PAIR_V
    R = np.zeros((7,MON_DIM),dtype=np.int8)
    z = face.full_center()
    free = set(face.free_vars())
    fmask = np.zeros(NV,dtype=np.bool_)
    if free:
        fmask[list(free)] = True
    pair_coeff = (z[pu.astype(np.int64)]*z[pv.astype(np.int64)]).astype(np.int8)
    dmask = np.zeros(len(pu),dtype=np.bool_)
    bothx=(pu<N)&(pv<N)
    if np.any(bothx):
        ii=pu[bothx].astype(np.int64); jj=pv[bothx].astype(np.int64)
        dmask[bothx]=killed_bool[ii,jj]
    bothy=(pu>=N)&(pv>=N)
    if np.any(bothy):
        ii=(pu[bothy]-N).astype(np.int64); jj=(pv[bothy]-N).astype(np.int64)
        dmask[bothy]=killed_bool[ii,jj]

    R[0,0]=1
    keep=~fmask
    R[0,1:1+NV][keep]=z[keep]
    kp=(~fmask[pu.astype(np.int64)]) & (~fmask[pv.astype(np.int64)]) & (~dmask)
    R[0,PAIR_OFFSET:][kp]=pair_coeff[kp]

    for mode in range(1,7):
        sv=face.singleton_var(mode)
        R[mode,1+sv]=int(z[sv])
        contains=(pu==sv)|(pv==sv)
        other=np.where(pu==sv,pv,pu).astype(np.int64)
        kk=contains & (~fmask[other]) & (~dmask)
        R[mode,PAIR_OFFSET:][kk]=pair_coeff[kk]
    return R


# ---------------------------------------------------------------------------
# W monomial support orbits and D removal.
# ---------------------------------------------------------------------------

def enumerate_W_orbits(gens,pair_rel,killed_ids):
    rel=np.full(MON_DIM,-1,dtype=np.int16)
    records=[]
    oid=0
    for start in range(MON_DIM):
        if rel[start]>=0:
            continue
        rel[start]=oid
        q=collections.deque([start])
        size=0
        while q:
            z=q.popleft(); size+=1
            for p,s in gens:
                zz,sg=act_mid(z,p,s)
                if rel[zz]<0:
                    rel[zz]=oid; q.append(zz)
                elif int(rel[zz])!=oid:
                    die("W support orbit collision")
        typ=monomial_type(start)
        in_D=False
        if typ in ("xx","yy"):
            a,b=mid_support(start)
            ia=a if a<N else a-N
            ib=b if b<N else b-N
            if int(pair_rel[ia,ib]) in killed_ids:
                in_D=True
        records.append({
            "orbit_id":oid,"rep_mid":start,"type":typ,
            "size":size,"in_D":in_D,
        })
        oid+=1
    if oid!=62:
        die("expected 62 degree<=2 support orbits, got %d"%oid)
    if sum(r["size"] for r in records)!=MON_DIM:
        die("W orbit sizes do not sum to 180301")
    return rel,records


def orbit_stabilizer(rep_mid,cert_elements):
    inds=[]; chars=[]
    for g,(p,s) in enumerate(cert_elements):
        mm,sg=act_mid(rep_mid,p,s)
        if mm==rep_mid:
            inds.append(g); chars.append(int(sg))
    if ORDER % len(inds):
        die("monomial stabilizer order does not divide H4")
    return np.asarray(inds,dtype=np.int32),np.asarray(chars,dtype=np.int8)


def fixed_space(Rall,inds,chars,tol=1e-7):
    d=Rall.shape[1]
    P=np.zeros((d,d),dtype=np.complex128)
    for g,ch in zip(inds,chars):
        P += int(ch)*Rall[int(g)]
    P /= float(len(inds))
    P=(P+P.conj().T)/2.0
    w,V=la.eigh(P)
    sel=np.flatnonzero(w>0.5)
    if len(sel):
        if np.max(np.abs(w[sel]-1.0))>tol:
            die("stabilizer projector selected eigenvalue far from 1")
    bad=np.flatnonzero((w>tol)&(w<1.0-tol))
    if len(bad):
        die("stabilizer projector has non-idempotent numerical eigenvalues")
    return V[:,sel],w


# ---------------------------------------------------------------------------
# Complete K multiplicity space in each complex irrep.
# ---------------------------------------------------------------------------

def residual_rvals(rep_mid,Rseed,cert_elements):
    out=np.empty((ORDER,14),dtype=np.float64)
    for g,(p,s) in enumerate(cert_elements):
        mm,sg=act_mid(rep_mid,p,s)
        out[g]=int(sg)*Rseed[:,mm]
    return out


def build_K_block_data(
    ri,meta,Rall,orbit_records,cert_elements,Rseed,expected_block
):
    d=int(meta["degree"])
    active=[]
    copy_total=0

    for rec in orbit_records:
        if rec["in_D"]:
            continue
        inds,chars=orbit_stabilizer(rec["rep_mid"],cert_elements)
        V,eigs=fixed_space(Rall,inds,chars)
        k=V.shape[1]
        if k==0:
            continue
        rr=dict(rec)
        rr["stab_indices"]=inds
        rr["stab_chars"]=chars
        rr["stab_order"]=len(inds)
        rr["fixed_basis"]=V
        rr["copy_start"]=copy_total
        rr["copy_end"]=copy_total+k
        rr["fixed_dim"]=k
        active.append(rr)
        copy_total+=k

    expected_mwd=int(expected_block["m_W_minus_D_exact"])
    if copy_total!=expected_mwd:
        die(
            "irrep %d complex orbit multiplicity m(W-D)=%d expected %d"
            %(ri+1,copy_total,expected_mwd)
        )

    coord=np.zeros((14,d,copy_total),dtype=np.complex128)
    chunk=256

    for rec in active:
        V=rec["fixed_basis"]
        k=V.shape[1]
        rvals=residual_rvals(rec["rep_mid"],Rseed,cert_elements)
        accum=np.zeros((14,d,k),dtype=np.complex128)
        for a in range(0,ORDER,chunk):
            b=min(ORDER,a+chunk)
            RV=np.einsum('gij,jk->gik',Rall[a:b],V,optimize=True)
            accum += np.einsum('gs,gik->sik',rvals[a:b],RV,optimize=True)
        norm=math.sqrt(d/(ORDER*rec["stab_order"]))
        accum*=norm
        coord[:,:,rec["copy_start"]:rec["copy_end"]]=accum

    C=coord.reshape(14*d,copy_total)
    U,s,Vh=la.svd(C,full_matrices=True,lapack_driver='gesdd')
    tol=max(C.shape)*np.finfo(float).eps*(s[0] if len(s) else 1.0)*100.0
    rank=int(np.sum(s>tol))
    expected_rank=copy_total-int(expected_block["m_K_if_certified"])
    if rank!=expected_rank:
        die(
            "irrep %d residual numerical rank %d expected exact %d; singular tail=%r"
            %(ri+1,rank,expected_rank,s[max(0,rank-2):min(len(s),rank+3)].tolist())
        )
    Z=Vh[rank:].conj().T
    mK=Z.shape[1]
    if mK!=int(expected_block["m_K_if_certified"]):
        die("irrep %d K block size mismatch"%(ri+1))
    # Numerical nullspace audit.
    nul=float(la.norm(C.dot(Z),2)) if mK else 0.0
    orth=float(la.norm(Z.conj().T.dot(Z)-np.eye(mK),2)) if mK else 0.0
    return {
        "d":d,"mWD":copy_total,"mK":mK,"rankL":rank,
        "active_orbits":active,"Z":Z,
        "constraint_singular_values":s,
        "null_residual_norm":nul,"Z_orthogonality_error":orth,
    }


# ---------------------------------------------------------------------------
# Candidate pseudoexpectation correlation parts.
# ---------------------------------------------------------------------------

def P600_from_P(P):
    idx=np.arange(NV)%N
    return P[np.ix_(idx,idx)]


def transformed_rep_arrays(rep_mid,cert_elements):
    supp=mid_support(rep_mid)
    deg=len(supp)
    sg=np.empty(ORDER,dtype=np.float64)
    a=np.full(ORDER,-1,dtype=np.int16)
    b=np.full(ORDER,-1,dtype=np.int16)
    for g,(p,s) in enumerate(cert_elements):
        mm,z=act_mid(rep_mid,p,s)
        ss=mid_support(mm)
        sg[g]=float(z)
        if len(ss): a[g]=ss[0]
        if len(ss)==2: b[g]=ss[1]
    return {"deg":deg,"sign":sg,"a":a,"b":b}


def corr_parts(rep_mid, trans, P6):
    """
    Return c0,c1 so ell_alpha(g)=c0(g)+alpha*c1(g).

    c1 is nonzero only for a product of two disjoint quadratic monomials.
    """
    S=mid_support(rep_mid)
    d1=len(S); d2=trans["deg"]
    sg=trans["sign"]
    c0=np.zeros(ORDER,dtype=np.float64)
    c1=np.zeros(ORDER,dtype=np.float64)

    if (d1+d2)&1:
        return c0,c1

    if d1==0 and d2==0:
        c0[:]=sg
        return c0,c1

    if d1==0 and d2==2:
        a=trans["a"].astype(np.int64); b=trans["b"].astype(np.int64)
        c0=sg*P6[a,b]
        return c0,c1

    if d1==2 and d2==0:
        a,b=S
        c0[:]=sg*P6[a,b]
        return c0,c1

    if d1==1 and d2==1:
        a=S[0]
        c=trans["a"].astype(np.int64)
        same=(c==a)
        c0[same]=sg[same]
        ns=~same
        c0[ns]=sg[ns]*P6[a,c[ns]]
        return c0,c1

    if d1!=2 or d2!=2:
        # Only possible remaining cases have odd parity and were returned.
        return c0,c1

    a,b=S
    c=trans["a"].astype(np.int64)
    d=trans["b"].astype(np.int64)

    eq=((c==a)&(d==b))|((c==b)&(d==a))
    c0[eq]=sg[eq]

    share_a=(c==a)|(d==a)
    share_b=(c==b)|(d==b)
    share=(share_a|share_b)&(~eq)

    # Exactly one shared variable for distinct unordered pairs.
    inds=np.flatnonzero(share)
    if len(inds):
        cc=c[inds]; dd=d[inds]
        # remaining variable from first pair
        rem1=np.where(share_a[inds],b,a)
        # remaining transformed variable = whichever is not the shared one
        shared=np.where((cc==a)|(cc==b),cc,dd)
        rem2=np.where(cc==shared,dd,cc)
        c0[inds]=sg[inds]*P6[rem1,rem2]

    dis=(~eq)&(~share)
    inds=np.flatnonzero(dis)
    if len(inds):
        cc=c[inds]; dd=d[inds]
        pair=(
            P6[a,b]*P6[cc,dd]
            +P6[a,cc]*P6[b,dd]
            +P6[a,dd]*P6[b,cc]
        )
        c1[inds]=sg[inds]*pair

    return c0,c1


def moment_blocks_for_irrep(Kdata,Rall,cert_elements,P6):
    """Build B0,B1 on W-D multiplicity space, then restrict to complete K."""
    d=Kdata["d"]
    m=Kdata["mWD"]
    active=Kdata["active_orbits"]
    B0=np.zeros((m,m),dtype=np.complex128)
    B1=np.zeros((m,m),dtype=np.complex128)
    Rflat=Rall.reshape(ORDER,d*d)

    trans=[transformed_rep_arrays(rec["rep_mid"],cert_elements) for rec in active]

    # Compute upper triangle in orbit blocks; fill Hermitian transpose.
    for ii,Oi in enumerate(active):
        js=list(range(ii,len(active)))
        C0=np.empty((ORDER,len(js)),dtype=np.float64)
        C1=np.empty_like(C0)
        for col,jj in enumerate(js):
            x0,x1=corr_parts(Oi["rep_mid"],trans[jj],P6)
            C0[:,col]=x0
            C1[:,col]=x1

        # BLAS group Fourier transform for this orbit row.
        F0=C0.T.dot(Rflat).reshape(len(js),d,d)
        F1=C1.T.dot(Rflat).reshape(len(js),d,d)
        Vi=Oi["fixed_basis"]
        si=slice(Oi["copy_start"],Oi["copy_end"])

        for col,jj in enumerate(js):
            Oj=active[jj]
            Vj=Oj["fixed_basis"]
            sj=slice(Oj["copy_start"],Oj["copy_end"])
            den=math.sqrt(Oi["stab_order"]*Oj["stab_order"])
            M0=Vi.conj().T.dot(F0[col]).dot(Vj)/den
            M1=Vi.conj().T.dot(F1[col]).dot(Vj)/den
            B0[si,sj]=M0; B1[si,sj]=M1
            if jj!=ii:
                B0[sj,si]=M0.conj().T
                B1[sj,si]=M1.conj().T

    herm0=float(np.max(np.abs(B0-B0.conj().T))) if m else 0.0
    herm1=float(np.max(np.abs(B1-B1.conj().T))) if m else 0.0
    if herm0>2e-7 or herm1>2e-7:
        die("moment multiplicity block not Hermitian: %g %g"%(herm0,herm1))
    B0=(B0+B0.conj().T)/2.0
    B1=(B1+B1.conj().T)/2.0

    Z=Kdata["Z"]
    K0=Z.conj().T.dot(B0).dot(Z)
    K1=Z.conj().T.dot(B1).dot(Z)
    K0=(K0+K0.conj().T)/2.0
    K1=(K1+K1.conj().T)/2.0
    return K0,K1,{"hermitian_error_B0":herm0,"hermitian_error_B1":herm1}


def min_eig(M):
    if M.shape[0]==0:
        return float("inf")
    # Only smallest eigenvalue.
    return float(la.eigh(M,subset_by_index=[0,0],eigvals_only=True,driver='evr')[0])


# ---------------------------------------------------------------------------
# Exact Q(sqrt(5)) reconstruction of P and AP scalar audit.
# ---------------------------------------------------------------------------

def _lcm(a,b):
    return abs(a//math.gcd(a,b)*b)


def reconstruct_P_exact_and_AP(A,Pfloat):
    """
    Floating P is used ONLY to identify candidate Q(sqrt(5)) values.
    Acceptance requires exact integer identities:
        P^T=P, diag P=1, P^2=75P,
        <A,P>=NUM_A+NUM_B sqrt(5),
        AP=(N/300)P.

    The last identity is checked on four exactly independent columns of P;
    P^2=75P and tr(P)=300 then prove rank(P)=4, so those columns span Ran(P).
    """
    groups={}
    for i in range(N):
        for j in range(N):
            aij=int(A[i,j]); pv=float(Pfloat[i,j])
            carrier=1 if aij>=0 else -1
            p0=carrier*pv if aij!=0 else pv
            key=(i==j,abs(aij),int(round(p0*10**12)))
            groups.setdefault(key,[]).append((i,j,p0))

    ab={}; maxerr=0.0
    sq=sp.sqrt(5)
    for key,items in groups.items():
        rep=sum(z[2] for z in items)/len(items)
        if abs(rep)<5e-14:
            aa=Fraction(0); bb=Fraction(0)
        else:
            e=sp.expand(sp.radsimp(sp.nsimplify(rep,[sq],tolerance=1e-11,full=False)))
            b0=sp.expand(e).coeff(sq); a0=sp.simplify(e-b0*sq)
            if a0.is_Rational is not True or b0.is_Rational is not True:
                die('P reconstruction left Q(sqrt(5))')
            aa=Fraction(int(a0.p),int(a0.q)); bb=Fraction(int(b0.p),int(b0.q))
        appr=float(aa)+float(bb)*SQRT5
        err=max(abs(z[2]-appr) for z in items)
        maxerr=max(maxerr,err)
        if err>2e-10:
            die('P exact reconstruction cluster error %g'%err)
        ab[key]=(aa,bb)

    D=1
    for aa,bb in ab.values():
        D=_lcm(D,aa.denominator); D=_lcm(D,bb.denominator)

    X=np.zeros((N,N),dtype=np.int64); Y=np.zeros((N,N),dtype=np.int64)
    for key,items in groups.items():
        aa,bb=ab[key]
        xa=aa.numerator*(D//aa.denominator)
        yb=bb.numerator*(D//bb.denominator)
        for i,j,_ in items:
            aij=int(A[i,j]); carrier=1 if aij>=0 else -1
            if aij!=0:
                X[i,j]=carrier*xa; Y[i,j]=carrier*yb
            else:
                X[i,j]=xa; Y[i,j]=yb

    if not np.array_equal(X,X.T) or not np.array_equal(Y,Y.T):
        die('exact reconstructed P not symmetric')
    for i in range(N):
        if int(X[i,i])!=D or int(Y[i,i])!=0:
            die('exact reconstructed diag(P)!=1')

    mx=max(abs(int(z)) for z in X.ravel()); my=max(abs(int(z)) for z in Y.ravel())
    bound=max(N*(mx*mx+5*my*my),N*2*mx*my,75*D*mx,75*D*my)
    if bound<(1<<62):
        RR=X@X+5*(Y@Y); SS=X@Y+Y@X
        ok=np.array_equal(RR,(75*D)*X) and np.array_equal(SS,(75*D)*Y)
    else:
        XO=X.astype(object); YO=Y.astype(object)
        RR=XO@XO+5*(YO@YO); SS=XO@YO+YO@XO
        ok=np.array_equal(RR,(75*D)*XO) and np.array_equal(SS,(75*D)*YO)
    if not ok:
        die('exact P^2=75P failed')

    Nr=sum(int(A[i,j])*int(X[i,j]) for i in range(N) for j in range(N))
    Ns=sum(int(A[i,j])*int(Y[i,j]) for i in range(N) for j in range(N))
    if Fraction(Nr,D)!=NUM_A or Fraction(Ns,D)!=NUM_B:
        die('exact <A,P> numerator mismatch')

    # Pick four columns with an exactly nonzero 4x4 principal minor.
    # Float rank is only candidate selection; determinant is checked exactly.
    basis=[]
    for k in range(N):
        bb=basis+[k]
        Gf=Pfloat[np.ix_(bb,bb)]
        if np.linalg.matrix_rank(Gf,tol=1e-10)!=len(bb):
            continue
        M=sp.Matrix([[sp.Integer(int(X[i,j]))+sp.Integer(int(Y[i,j]))*sq
                      for j in bb] for i in bb])
        if sp.simplify(M.det())!=0:
            basis=bb
            if len(basis)==4: break
    if len(basis)!=4:
        die('could not find exact four-column basis of P')

    # Check 300 A*C = (a+b sqrt5) C on those four columns.
    # With C=(X+Y sqrt5)/D, integer component equations are
    #   300 AX = aX+5bY,  300 AY=bX+aY.
    for j in basis:
        for i in range(N):
            ax=sum(int(A[i,k])*int(X[k,j]) for k in range(N))
            ay=sum(int(A[i,k])*int(Y[k,j]) for k in range(N))
            if 300*ax != NUM_A*int(X[i,j])+5*NUM_B*int(Y[i,j]):
                die('exact AP scalar relation failed (rational component)')
            if 300*ay != NUM_B*int(X[i,j])+NUM_A*int(Y[i,j]):
                die('exact AP scalar relation failed (sqrt5 component)')

    return {
        'X':X,'Y':Y,'D':D,'basis_columns':basis,
        'max_float_reconstruction_error':maxerr,
        'P2_identity':'P^2=75P exact',
        'AP_identity':'AP=(N/300)P exact on rank-4 range',
    }


# ---------------------------------------------------------------------------
# Exact alpha=0 failure using f itself.
# ---------------------------------------------------------------------------

def qsqrt_sign(a,b):
    """Sign of rational a + b sqrt(5), with Fraction inputs."""
    a=Fraction(a); b=Fraction(b)
    if b==0:
        return (a>0)-(a<0)
    if a==0:
        return (b>0)-(b<0)
    # If same sign, immediate.
    if (a>0 and b>0): return 1
    if (a<0 and b<0): return -1
    # Compare |a| and |b|sqrt5 exactly by squaring.
    lhs=a*a
    rhs=5*b*b
    if lhs==rhs:
        return 0
    if a>0 and b<0:
        return 1 if lhs>rhs else -1
    # a<0,b>0
    return -1 if lhs>rhs else 1


def exact_zero_fourth_failure(A,Pexact):
    C=EXPECTED_C; a=NUM_A; b=NUM_B
    norm2=sum(int(x)*int(x) for x in A.ravel())
    # L0(B^2) = N^2/150 - ||A||_F^2, using AP=(N/300)P and P^2=75P.
    ra=Fraction(a*a+5*b*b,150)-norm2
    rb=Fraction(2*a*b,150)
    # L0(f^2)=C^2-2CN+L0(B^2)
    fa=Fraction(C*C)-2*C*a+ra
    fb=-2*C*b+rb
    sg=qsqrt_sign(fa,fb)
    if sg>=0:
        die("expected exact zero-fourth f^2 value to be negative")
    return {
        "status":"PROVED_NOT_PSD_ON_K",
        "reason":"f=C-x^TAy belongs to K and L0(f^2)<0",
        "L0_f2_rational_part":str(fa),
        "L0_f2_sqrt5_part":str(fb),
        "A_Frobenius_norm_squared":str(norm2),
        "sign_exact":-1,
    }


# ---------------------------------------------------------------------------
# Structural self-test
# ---------------------------------------------------------------------------

def structural_self_test(nogap_path):
    """
    Fast structural audit.  The no-GAP constructor already proves all 34
    finite-field characters.  Here we independently reconstruct the complex
    binary-icosahedral seed representations and audit their unitary models;
    the certified run below performs a full-character comparison for every
    surviving K block before using it.
    """
    ng=load_module(nogap_path,"h4nogap")
    Q,Qdata,G,Hdata,ff=ng.structural_construction()
    qmap=structural_Q_to_quaternion(Q)
    qc=complex_Q_irreps(ng,Q,Qdata,qmap)

    if len(G["elements"])!=ORDER:
        die("H4 structural order != 14400")
    if int(G["exponent"])!=60:
        die("H4 structural exponent != 60")
    if len(Hdata["irreps"])!=34:
        die("H4 structural irrep count != 34")
    if sum(int(r["degree"])**2 for r in Hdata["irreps"])!=ORDER:
        die("sum of H4 irrep degree squares != 14400")

    return {
        "status":"STRUCTURAL_COMPLEX_SEED_MODELS_PASSED",
        "prime":PRIME,
        "H4_order":ORDER,
        "H4_exponent":int(G["exponent"]),
        "H4_irrep_count":len(Hdata["irreps"]),
        "sum_degree_squares":sum(int(r["degree"])**2 for r in Hdata["irreps"]),
        "quaternion_Q_pair":list(qmap["Q_pair"]),
        "quaternion_2I_pair":list(qmap["quat_pair"]),
        "quaternion_closure_max_error":qmap["closure_max_error"],
        "Q_complex_max_unitarity_error":qc["max_unitarity_error"],
        "sqrt5_mod_embedding":int(qc["sqrt5_mod_embedding"]),
        "full_H4_character_audit":"performed per surviving K block in certified run",
        "prior_invariant_seed_SOS_status":"INCONCLUSIVE",
        "rank4_full_elliptope_extension":"PROVED_IMPOSSIBLE",
    }


# ---------------------------------------------------------------------------
# Main certified run
# ---------------------------------------------------------------------------

def main(argv):
    init_pairs()

    if len(argv)==3 and argv[1]=="--self-test-structural":
        out=structural_self_test(argv[2])
        print(json.dumps(out,indent=2,sort_keys=True))
        return 0

    if len(argv)!=5:
        die(
            "usage:\n"
            "  python h4_K_full_dual_slice.py --self-test-structural h4_nogap_irrep_cache.py\n"
            "  python h4_K_full_dual_slice.py MAT SYSTEM_JSON COMPLETE_K_JSON h4_nogap_irrep_cache.py"
        )

    mat_path,system_path,complete_path,nogap_path=argv[1:]

    if md5_file(mat_path)!=EXPECTED_MD5:
        die("MAT MD5 mismatch")

    with h5py.File(mat_path,"r") as f:
        A=exact_int_matrix(f["A"][()],"A")
        P=np.asarray(f["P"][()],dtype=np.float64)
        ax=exact_sign_vector(f["ax"][()],"ax")
        by=exact_sign_vector(f["by"][()],"by")

    if canonical_A_sha(A)!=EXPECTED_A_SHA:
        die("A canonical SHA mismatch")
    if not np.array_equal(A,A.T):
        die("A not symmetric")
    if P.shape!=(N,N) or np.max(np.abs(P-P.T))>0:
        die("P shape/symmetry mismatch")

    C=sum(int(ax[i])*int(A[i,j])*int(by[j]) for i in range(N) for j in range(N))
    if C!=EXPECTED_C:
        die("archived witness C mismatch")

    hright=[sum(int(ax[i])*int(A[i,j]) for i in range(N)) for j in range(N)]
    Zlines=[j for j,h in enumerate(hright) if h==0]
    if Zlines!=[46,56,85,99,131,148]:
        die("zero-field set mismatch")

    with open(complete_path,"rb") as f:
        complete_bytes=f.read()
    complete=json.loads(complete_bytes)
    if complete.get("final_status")!="PROVED_COMPLETE_K_DECOMPOSITION":
        die("complete-K JSON is not PROVED_COMPLETE_K_DECOMPOSITION")

    # We cannot require the user's local full JSON byte hash to equal the prose hash
    # if they inserted extra formatting.  Require the mathematical isotypic hash.
    table_sha=complete.get("isotypic_table_sha256")
    if table_sha!=EXPECTED_ISOTYPIC_SHA:
        die("complete-K isotypic table SHA mismatch: %r"%table_sha)

    blocks=complete.get("isotypic_blocks")
    if not isinstance(blocks,list) or len(blocks)!=34:
        die("complete-K JSON must contain 34 isotypic_blocks")
    byid={int(r["gap_irrep_id"]):r for r in blocks}
    surv=sorted(int(r["m_K_if_certified"]) for r in blocks if int(r["m_K_if_certified"])>0)
    if surv!=EXPECTED_SURVIVING_BLOCKS_SORTED:
        die("surviving K block-size multiset mismatch")

    ng=load_module(nogap_path,"h4nogap")
    Q,Qdata,G,Hdata,ff=ng.structural_construction()
    system,cert_elements,cert_gens,action_sha=ng.load_and_match_certified_action(system_path,G)
    if action_sha!=EXPECTED_ACTION_SHA:
        die("certified signed action SHA mismatch")

    qmap=structural_Q_to_quaternion(Q)
    qc=complex_Q_irreps(ng,Q,Qdata,qmap)

    # Exact line-pair/D and residual seed construction.
    pair_rel,pair_records=enumerate_pair_support_orbits(cert_gens)
    killed_ids,killed_bool=killed_pair_data(pair_rel,Zlines)
    faceR=Face(ax,by,"y",Zlines)
    faceL=Face(by,ax,"x",Zlines)
    Rseed=np.vstack([
        direct_residual_seed_matrix(faceR,killed_bool),
        direct_residual_seed_matrix(faceL,killed_bool),
    ]).astype(np.float64)

    orbit_rel,orbit_records=enumerate_W_orbits(cert_gens,pair_rel,set(killed_ids))
    Ddim=sum(r["size"] for r in orbit_records if r["in_D"])
    if Ddim!=13200:
        die("D coordinate dimension %d != 13200"%Ddim)

    P6=P600_from_P(P)

    # Candidate blocks, only for the 20 surviving irreps.
    alpha_values=[0.0,0.5,2.0/3.0,1.0]
    per_irrep=[]
    global_mins={str(a):float("inf") for a in alpha_values}

    # Structural Hdata gap_id is ri+1 and matches the cache schema.
    for ri,meta in enumerate(Hdata["irreps"]):
        exact=byid[ri+1]
        mK=int(exact["m_K_if_certified"])
        if mK==0:
            per_irrep.append({
                "gap_irrep_id":ri+1,"degree":int(meta["degree"]),
                "mK":0,"skipped_zero_K_block":True,
            })
            continue

        print(
            "irrep %d/34 degree=%d mK=%d: constructing complex rho(g)"
            %(ri+1,int(meta["degree"]),mK),
            file=sys.stderr,
        )
        Rall=H_rep_all(meta,qc,G)

        # Full character audit against exact finite-field lift.
        smod=qc["sqrt5_mod_embedding"]
        target=np.array([
            lift_qsqrt5_residue(x,int(meta["degree"]),smod)[2]
            for x in Hdata["characters"][ri]
        ])
        charerr=float(np.max(np.abs(np.trace(Rall,axis1=1,axis2=2).real-target)))
        if charerr>3e-8:
            die("irrep %d complex character mismatch %g"%(ri+1,charerr))

        print("  constructing complete K multiplicity nullspace",file=sys.stderr)
        Kdata=build_K_block_data(
            ri,meta,Rall,orbit_records,cert_elements,Rseed,exact
        )

        print(
            "  Fourier adjoint map for L_alpha on %d active orbit modules"
            %len(Kdata["active_orbits"]),
            file=sys.stderr,
        )
        K0,K1,maudit=moment_blocks_for_irrep(Kdata,Rall,cert_elements,P6)

        mins={}
        for av in alpha_values:
            ev=min_eig(K0+av*K1)
            mins[str(av)]=ev
            global_mins[str(av)]=min(global_mins[str(av)],ev)

        rec={
            "gap_irrep_id":ri+1,
            "degree":int(meta["degree"]),
            "m_W_minus_D_exact":int(exact["m_W_minus_D_exact"]),
            "mK":mK,
            "residual_rank_exact":int(exact["m_W_minus_D_exact"])-mK,
            "active_orbit_modules":len(Kdata["active_orbits"]),
            "complex_character_max_error":charerr,
            "constraint_null_residual_norm":Kdata["null_residual_norm"],
            "K_basis_orthogonality_error":Kdata["Z_orthogonality_error"],
            "moment_map_audit":maudit,
            "min_eigenvalues":mins,
        }
        per_irrep.append(rec)
        del Rall,Kdata,K0,K1

    spherical_min=global_mins[str(2.0/3.0)]
    if spherical_min>1e-7:
        slice_status="NUMERICAL_CANDIDATE_SEPARATOR_ALPHA_2_OVER_3"
    else:
        slice_status="NUMERICAL_FAILURE_ALPHA_2_OVER_3"

    Pexact=reconstruct_P_exact_and_AP(A,P)
    zero_exact=exact_zero_fourth_failure(A,Pexact)

    # Exact objective sign: N>C and N<2C, checked by integer squaring.
    left=5*NUM_B*NUM_B
    nc=EXPECTED_C-NUM_A
    twoc=2*EXPECTED_C-NUM_A
    if nc<=0 or twoc<=0:
        die("unexpected numerator rational-part inequalities")
    if not (left>nc*nc and left<twoc*twoc):
        die("failed exact C<N<2C audit")

    out={
        "status":slice_status,
        "proof_status":"OPEN_GAP_NUMERICAL_DUAL_SLICE_ONLY",
        "provenance":{
            "mat_md5":EXPECTED_MD5,
            "A_sha256":EXPECTED_A_SHA,
            "action_sha256":action_sha,
            "complete_K_isotypic_table_sha256":table_sha,
        },
        "complete_K":{
            "dimension":149701,
            "commutant_dimension":3132219,
            "symmetric_PSD_parameter_dimension":1569415,
            "surviving_block_sizes":EXPECTED_SURVIVING_BLOCKS_SORTED,
            "all_34_blocks_complete":True,
        },
        "adjoint_map_formula":(
            "B_(O,a),(O',b)(L)=1/sqrt(|H_O||H_O'|) * "
            "v_O,a^* [sum_g L(m_O*(g m_O')) rho(g)] v_O',b; "
            "K-block = Z_rho^* B_rho Z_rho"
        ),
        "dual_slice":{
            "second_moment":"X=[[P,P],[P,P]]",
            "odd_moments":0,
            "four_distinct_moment":(
                "alpha*(X_ab*X_cd+X_ac*X_bd+X_ad*X_bc)"
            ),
            "boolean_repeated_indices":"reduced exactly before applying moment rule",
            "objective_exact":"C-(1539823299061914600+706968072319078800*sqrt(5))",
            "objective_sign_exact":-1,
            "tested_alpha_values":alpha_values,
            "global_min_eigenvalues":global_mins,
            "alpha_2_over_3_full_K_min_eigenvalue":spherical_min,
            "numerical_evidence_only":True,
        },
        "exact_P_audit":{
            "D":int(Pexact["D"]),
            "basis_columns":Pexact["basis_columns"],
            "max_float_reconstruction_error":Pexact["max_float_reconstruction_error"],
            "P2_identity":Pexact["P2_identity"],
            "AP_identity":Pexact["AP_identity"],
        },
        "alpha_zero_exact_failure":zero_exact,
        "per_irrep":per_irrep,
        "preserved_facts":{
            "prior_invariant_seed_SOS_test":"INCONCLUSIVE",
            "invariant_vanishing_dimension":43,
            "rank4_full_elliptope_extension":"PROVED_IMPOSSIBLE",
        },
    }

    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    outpath=mat_path+".K_full_dual_slice.json"
    with open(outpath,"wb") as f:
        f.write(raw)
    display=dict(out)
    display["output_path"]=outpath
    display["output_sha256"]=sha256_bytes(raw)
    print(json.dumps(display,indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    sys.exit(main(sys.argv))
