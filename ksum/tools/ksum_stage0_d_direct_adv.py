"""STAGE 0 TASK D — INDEPENDENT cross-check / small exact atlas of Adv_pm for 2-Sum
over Z_q. Builds the HLS/LMRSS dual-adversary SDP DIRECTLY (single PSD matrix on
(input, position) pairs, NO symmetry reduction — same formulation as
tools/adv_sdp_direct.py, generalised from the Boolean cube to Z_q):

   Adv_pm(f) = min t
     s.t.  M >= 0                                        (dim = q^n * n)
           sum_{i: x_i != y_i} M[(x,i),(y,i)] = 1        for all f(x) != f(y)
           sum_i M[(x,i),(x,i)] <= t                     for all x

f(x)=1 iff exists i<j with x_i + x_j == t_target (mod q).  Default t_target=0 to
match ksum_probe.py.  Constraints are assembled as VECTORIZED sparse selectors on
vec(M) (row-major) so canonicalisation is fast.  If the unreduced value here equals
ksum_probe's symmetry-reduced value, that confirms (a) ksum_probe computes Adv_pm and
(b) its reduction is lossless.

Usage: python ksum_stage0_d_direct_adv.py n q [t_target=0] [solver=SCS] [eps=1e-6] [max_iters=200000]
"""
import sys, time
from itertools import product
import numpy as np
import scipy.sparse as sp
import cvxpy as cp

n = int(sys.argv[1]); q = int(sys.argv[2])
t_target = int(sys.argv[3]) if len(sys.argv) > 3 else 0
solver = sys.argv[4] if len(sys.argv) > 4 else "SCS"
eps = float(sys.argv[5]) if len(sys.argv) > 5 else 1e-6
max_iters = int(sys.argv[6]) if len(sys.argv) > 6 else 200000

inp = list(product(range(q), repeat=n))
lab = np.array([1 if any((x[i] + x[j]) % q == t_target
                         for i in range(n) for j in range(i + 1, n)) else 0
                for x in inp], dtype=np.int8)
m = len(inp); N = n; dim = m * N
print(f"2Sum(n={n},q={q},t={t_target}): |D|={m} N={N} PSDdim={dim} "
      f"labels(1={int(lab.sum())}/{m})", flush=True)
if dim > 1400:
    print(f"  PSDdim {dim} > 1400 -> refusing (dense SDP too big); pick smaller n,q.")
    sys.exit(2)

inp_arr = np.array(inp, dtype=np.int64)          # (m, n)
YES = np.where(lab == 1)[0]; NO = np.where(lab == 0)[0]

def vidx(r, c):                                  # row-major index into vec(M)
    return r * dim + c

# equality constraints: one row per (a in YES, b in NO); picks (a*N+i, b*N+i) for i where they differ
eq_rows, eq_cols = [], []
rc = 0
for a in YES:
    xa = inp_arr[a]
    diff = (inp_arr[NO] != xa)                    # (|NO|, n) bool
    for jb, b in enumerate(NO):
        ds = np.where(diff[jb])[0]
        for i in ds:
            eq_rows.append(rc); eq_cols.append(vidx(a * N + i, b * N + i))
        rc += 1
n_eq = rc
Aeq = sp.csr_matrix((np.ones(len(eq_rows)), (eq_rows, eq_cols)), shape=(n_eq, dim * dim))

# diagonal constraints: one row per input a; picks (a*N+i, a*N+i) for all i
d_rows, d_cols = [], []
for a in range(m):
    for i in range(N):
        d_rows.append(a); d_cols.append(vidx(a * N + i, a * N + i))
Adiag = sp.csr_matrix((np.ones(len(d_rows)), (d_rows, d_cols)), shape=(m, dim * dim))
print(f"  equality constraints: {n_eq}   diagonal constraints: {m}", flush=True)

M = cp.Variable((dim, dim), PSD=True)
t = cp.Variable(nonneg=True)
mvec = cp.reshape(M, (dim * dim, 1), order="C")
cons = [Aeq @ mvec == 1, Adiag @ mvec <= t]

prob = cp.Problem(cp.Minimize(t), cons)
kw = dict(eps=eps, max_iters=max_iters) if solver == "SCS" else {}
_t0 = time.time()
prob.solve(solver=solver, **kw)
print(f"  DIRECT Adv_pm(2Sum,n={n},q={q},t={t_target}) = {t.value:.6f}  "
      f"status={prob.status}  solver={solver}  eps={eps}  solve={time.time()-_t0:.1f}s",
      flush=True)
