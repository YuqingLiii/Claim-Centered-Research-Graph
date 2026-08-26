"""
Finite Bridge-II check at n=3, q=6, restored from the archived checker.
Requires NumPy. Run: python3 se/tools/se_bridge2_legal_rebuild_n3.py

The numerical construction is unchanged. It builds X/Y with the primed
S_(n-1) x S_n projector and restricts to the 720 legal rows and columns.
Definitions: Belovs--Rosmanis, https://arxiv.org/abs/1310.5185v4,
source equations for Psi_0/Psi_1, X/Y, and the primed projector (source
lines 486--488, 548--551, 639, and 1342). The legality normalization is
q^(3n/2)/sqrt((q)_n*(q)_(2n)) = 10.8.

Only k=0 is in the n=3 witness window; k=1,2 test the broader candidate
inequality. The ambient Y norms are supplied rounded anchors from the
historical run, NOT recomputed here. Matrix norms use floating-point SVD.
A finite PASS is not a proof for arbitrary n or a formal certificate.
"""
import itertools
import numpy as np
from math import factorial, sqrt

n, q = 3, 6
NL = 2 * n                                   # 6 legs
DIM = q ** NL                                # 46656

# ---------------------------------------------------------------- e-basis, Pi_0/Pi_1, Psi mats
e0 = np.ones(q) / sqrt(q)
P0 = np.outer(e0, e0)                        # Pi_0 = J/q
P1 = np.eye(q) - P0

def as6x36(fun):
    M = np.zeros((q, q * q))
    for u in range(q):
        for v in range(q):
            eu = np.zeros(q); eu[u] = 1.0
            ev = np.zeros(q); ev[v] = 1.0
            M[:, u * q + v] = fun(eu, ev)
    return M

PSI0 = as6x36(lambda u, v: e0 * (e0 @ u) * (e0 @ v))                 # Pi_0 (x) e_0*
PSI1 = as6x36(lambda u, v: (P1 @ u) * (e0 @ v) + (e0 @ u) * (P1 @ v))  # BR:488
YQ   = as6x36(lambda u, v: (e0 @ u) * (P1 @ v))                      # e_0* (x) Pi_1  (BR:549)

# ---------------------------------------------------------------- Pibar^{(m)}_j by characters
def partitions(k, mx=None):
    if mx is None: mx = k
    if k == 0: yield (); return
    for f in range(min(k, mx), 0, -1):
        for rest in partitions(k - f, f): yield (f,) + rest

def hook_f(lam):
    lam = [x for x in lam if x > 0]
    if not lam: return 1
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    num, den = factorial(sum(lam)), 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    return num // den

def mn_char(lam, rho):
    if not rho: return 1 if not lam else 0
    if not lam: return 0
    r, rest = rho[0], rho[1:]
    lam = tuple(lam); L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]
    bset = set(beta); tot = 0
    for b in beta:
        nb = b - r
        if nb < 0 or nb in bset: continue
        nb_list = sorted([x for x in beta if x != b] + [nb], reverse=True)
        ht = sum(1 for x in beta if nb < x < b)
        M = len(nb_list)
        nl = tuple(x for x in (nb_list[i] - (M - 1 - i) for i in range(M)) if x > 0)
        tot += (-1) ** ht * mn_char(nl, rest)
    return tot

def cyc_type(g):
    m = len(g); seen = [False] * m; ct = []
    for i in range(m):
        if not seen[i]:
            L, j = 0, i
            while not seen[j]:
                seen[j] = True; j = g[j]; L += 1
            ct.append(L)
    return tuple(sorted(ct, reverse=True))

def leg_perm_matrix(g, m):
    """matrix of the leg permutation v_{i_1..i_m} -> v_{i_{g^{-1}(1)}...}: build via reshape/transpose."""
    d = q ** m
    idx = np.arange(d).reshape((q,) * m)
    inv = np.argsort(g)
    idxp = np.transpose(idx, axes=inv).reshape(d)
    M = np.zeros((d, d))
    M[idxp, np.arange(d)] = 1.0
    return M

def weight_proj(m, j):
    """exact-weight-j projector on (C^q)^{(x)m} (e-basis grading)."""
    U = np.zeros((q, q)); U[0] = e0
    # complete e_0 to an orthonormal basis via QR
    A = np.eye(q) - np.outer(e0, e0)
    Q, _ = np.linalg.qr(A)
    B = np.vstack([e0, Q.T[:q - 1]])          # rows: e_0, e_1..e_{q-1}
    d = q ** m
    P = np.zeros((d, d))
    full = np.eye(1)
    # build sum over index-tuples with exactly j nonzero labels of |E_t><E_t|
    # do it leg-wise: P = sum over patterns of tensor(prod of P0e or P1e)
    P0e = np.outer(B[0], B[0])                # rank-1 e_0 leg
    P1e = np.eye(q) - P0e
    for pat in itertools.combinations(range(m), j):
        term = np.eye(1)
        for leg in range(m):
            term = np.kron(term, P1e if leg in pat else P0e)
        P += term
    return P

def pibar(m, j):
    """projector onto barH^{(m)}_j: shapes (m-j, lam), lam |- j, inside exact weight j (BR:602)."""
    Wp = weight_proj(m, j)
    shapes = [ (m - j,) + lam for lam in partitions(j) if (m - j) >= (lam[0] if lam else 0) ]
    if not shapes: return np.zeros((q ** m, q ** m))
    G = list(itertools.permutations(range(m)))
    Piso = np.zeros((q ** m, q ** m))
    for sh in shapes:
        acc = np.zeros((q ** m, q ** m))
        for g in G:
            acc += mn_char(sh, cyc_type(g)) * leg_perm_matrix(g, m)
        Piso += (hook_f(sh) / factorial(m)) * acc
    return Piso @ Wp

# sanity vs the fresh-log anchors
PB2 = {j: pibar(2, j) for j in range(0, 3)}
PB3 = {j: pibar(3, j) for j in range(0, 3)}
assert abs(np.trace(PB2[1]) - 5) < 1e-9 and abs(np.trace(PB3[1]) - 10) < 1e-9
assert np.linalg.norm(PB2[2]) < 1e-12          # barH^{(2)}_2 = 0 (no shape fits)
for M in (*PB2.values(), *PB3.values()):
    assert np.linalg.norm(M @ M - M) < 1e-9    # idempotent

# ---------------------------------------------------------------- legal sets
legal_no = [w for w in itertools.permutations(range(q))]              # 720 bijections
no_idx = np.array([sum(w[i] * q ** (NL - 1 - i) for i in range(NL)) for w in legal_no])
z_words = [z for z in itertools.permutations(range(q), n)]            # 120 injections
z_idx = np.array([sum(z[i] * q ** (n - 1 - i) for i in range(n)) for z in z_words])
matchings = list(itertools.permutations(range(n)))                    # sigma: i -> n + sigma(i)

c0 = q ** (1.5 * n) / sqrt(np.prod([q - i for i in range(n)]) * float(factorial(q)))
assert abs(c0 - 10.8) < 1e-9

# ---------------------------------------------------------------- operators on legal columns
def project_cols(k, cols):
    """apply Pi_0[leg1] (x) Pibar'_{se,k}[legs 2..6] to one-hot columns (indices cols)."""
    nc = len(cols)
    V = np.zeros((DIM, nc))
    V[cols, np.arange(nc)] = 1.0
    V = V.reshape(q, q * q, q ** 3, nc)
    V = np.einsum('ab,bxyc->axyc', P0, V)
    out = np.zeros_like(V)
    for l in range(0, k + 1):
        A, B = PB2[k - l], PB3[l]
        if np.linalg.norm(A) < 1e-14 or (np.linalg.norm(B) < 1e-14 and l > 0): continue
        T = np.einsum('xu,auyc->axyc', A, V)
        T = np.einsum('yv,axvc->axyc', B, T)
        out += T
    return out.reshape(q, q, q, q, q, q, nc)

def channel_block(kind, k, mu, Vt):
    """apply X^mu_k or Y^mu_k (BR:548-551) to projected tensor Vt (6^6 x nc), restrict rows to z."""
    pairs = [(0, n + mu[0]), (1, n + mu[1]), (2, n + mu[2])]
    order = [pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1], pairs[2][0], pairs[2][1], 6]
    W = np.transpose(Vt, axes=order).reshape(q * q, q * q, q * q, -1)
    nc = W.shape[-1]
    acc = np.zeros((q, q, q, nc))
    others = [0, 1] if kind == 'X' else [0, 1]
    kk = k if kind == 'X' else k - 1
    if kk < 0: return np.zeros((len(z_idx), nc))
    Mq = PSI0 if kind == 'X' else YQ
    for act in itertools.combinations(others, kk):
        M2 = PSI1 if 0 in act else PSI0
        M3 = PSI1 if 1 in act else PSI0
        T = np.einsum('pa,axyc->pxyc', Mq, W)
        T = np.einsum('sx,pxyc->psyc', M2, T)
        T = np.einsum('ty,psyc->pstc', M3, T)
        acc += T
    flat = acc.reshape(q ** 3, nc)
    return flat[z_idx, :]

def legal_R(kind, k):
    R = np.zeros((len(matchings) * len(z_idx), len(legal_no)))
    CH = 180
    for s in range(0, len(legal_no), CH):
        cols = no_idx[s:s + CH]
        Vt = project_cols(k, cols)
        for mi, mu in enumerate(matchings):
            R[mi * len(z_idx):(mi + 1) * len(z_idx), s:s + len(cols)] = channel_block(kind, k, mu, Vt)
    return c0 / sqrt(len(matchings)) * R

# ---------------------------------------------------------------- r_top table (exact)
def r_top(qq, k, th):
    return (qq ** k) * hook_f(th) / (factorial(k) * hook_f((qq - k,) + th))

RT = {0: 1.0,
      1: max(r_top(q, 1, th) for th in partitions(1)),
      2: max(r_top(q, 2, th) for th in partitions(2))}

print("=" * 88)
print("BRIDGE II legal rebuild, n=3 q=6, PRIMED projector Pibar'_{se,k} (S_{n-1} x S_n, BR:639)")
print("PASS criterion (pre-registered): s_k = ||R(Xbar_k)|| <= max_theta r_top(6,k,theta)")
print("r_top table: k=0: 1   k=1: %.6f (=6/5)   k=2: %.6f (=2)" % (RT[1], RT[2]))
print("G8: K(3)=1 -- only k=0 in spec; k=1,2 test the general inequality, not the witness regime")
print("=" * 88)
amb_Y = {0: 0.0, 1: 0.57735027, 2: 0.81649658}   # fresh-log ambient anchors (ybar_norms_fresh.log)
ok = True
for k in (0, 1, 2):
    RX = legal_R('X', k)
    sx = np.linalg.svd(RX, compute_uv=False)[0]
    RY = legal_R('Y', k)
    sy = np.linalg.svd(RY, compute_uv=False)[0] if np.linalg.norm(RY) > 1e-14 else 0.0
    bx = RT[k]
    by = RT[k] * amb_Y[k]
    vx = "PASS" if sx <= bx + 1e-9 else "*** VIOLATION ***"
    vy = "PASS" if sy <= by + 1e-9 else ("(vacuous k=0)" if k == 0 else "*** VIOLATION ***")
    print("k=%d  ||R(Xbar_k)|| = %.10f  <=? r_top=%.6f   %s" % (k, sx, bx, vx))
    print("     ||R(Ybar_k)|| = %.10f  <=? r_top*ambY=%.6f   %s" % (sy, by, vy))
    ok = ok and (sx <= bx + 1e-9) and (k == 0 or sy <= by + 1e-9)
print("=" * 88)
print("ANCHOR k=0 must be 1.0 exactly; H_B: is s_1 = 1.2 exactly?")
print("OVERALL: %s" % ("ALL PASS -- Bridge II's X/Y inequalities HOLD numerically at n=3 (off-spec k>=1)"
                       if ok else "VIOLATION FOUND -- Bridge II FALSE AS STATED at n=3; report, do not massage"))

raise SystemExit(0 if ok else 1)
