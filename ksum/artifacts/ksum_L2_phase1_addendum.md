# KSUM.B4b.L2 phase-1 addendum — corrected-threshold repair

Date: 2026-07-19  
Status: **CONJECTURED · pending independent review.**  
Scope: append-only correction to [the reviewed phase-1 report](ksum_L2_phase1.md); the reviewed report is not rewritten.

## Decision

The corrected direct-error threshold does not kill the finite LP route.  Exact rational reruns of
both the single-histogram and joint-histogram LPs give corrected certified degrees (0\to2),
(0\to2), and (2\to3) at the three commissioned points.  Thus the joint-over-single certified-degree
gain survives at every point, and the preregistered all-points kill criterion is not triggered.

This is finite-instance evidence only.  The repaired asymptotic lemma below is an obligation, not a
proved consequence of the LPs.  The new work is pending independent review and carries no
completion-tier status.

## R1 — canonical direct-error convention

This section is the canonical convention for the L2 repair.  Let (F=-1) on NO inputs and (F=+1)
on YES inputs.  If a (T)-query quantum algorithm has output error (e), its acceptance-probability
polynomial has degree at most (2T), and its expected-sign polynomial (p=2P[\mathrm{YES}]-1)
satisfies

\[
  \deg p\le 2T,\qquad \lVert p-F\rVert_\infty\le 2e.
\]

At (e=1/3), the uniform error is (2/3).  Hence a unit-(\ell_1) dual witness of pure high degree
(d) directly excludes every such degree-(<d) expected-sign polynomial only when

\[
  \langle\mu,F\rangle>\frac23.
\]

Under this strict threshold, the certificate gives (Q_{1/3}(F)\ge d/2).  Equality at (2/3) does
not certify.  The phase-1 (>1/3) test remains a valid sign-approximate-degree test at uniform
approximation error (1/3), but it is not the direct (Q_{1/3}\ge d/2) test.

### Preregistration

The point-by-point expectations were frozen in
[predictions.txt](logs_ksum_L2r_20260719/predictions.txt) before the corrected solver was created or
run.  All three predicted that a certified-degree gain would survive: the two (q=3) single
optima sit exactly at the now-strict cutoff, while the joint spectra have unit correlation through
degree two; at ((5,4,1)), the joint degree-three value (5/7) is above the cutoff while the single
value (11/21) is below it.

### Corrected exact rational rerun

The LP objective and exact falling-factorial moment constraints are unchanged; only the direct-error
certification predicate is corrected to strict (>2/3).  The exact rerun of both bases gives:

| case | (d) | single optimum | joint optimum | direct (>2/3) outcome |
|---|---:|---:|---:|---|
| ((3,3,0)) | 1 | (2/3) | (1) | joint only |
|  | 2 | (2/3) | (1) | joint only |
|  | 3 | (1/9) | (1/2) | neither |
| ((4,3,0)) | 1 | (2/3) | (1) | joint only |
|  | 2 | (2/3) | (1) | joint only |
|  | 3 | (1/6) | (5/9) | neither |
|  | 4 | (1/6) | (3/8) | neither |
| ((5,4,1)) | 1 | (1) | (1) | both |
|  | 2 | (1) | (1) | both |
|  | 3 | (11/21) | (5/7) | joint only |
|  | 4 | (25/63) | (3/5) | neither |
|  | 5 | (1/11) | (1/11) | neither |

The corrected certified-degree table is:

| case | preregistered expectation | single degree | joint degree | joint gain | outcome |
|---|---|---:|---:|---:|---|
| ((3,3,0)) | survive | 0 | 2 | +2 | survived |
| ((4,3,0)) | survive | 0 | 2 | +2 | survived |
| ((5,4,1)) | survive | 2 | 3 | +1 | survived |

Degree zero means only that this LP provides no positive-degree certificate at the strict threshold.
It does not assert that the function has approximate degree or quantum query complexity zero.

The standalone exact solver is
[ksum/tools/ksum_l2r_exact_moment_lp.py](../tools/ksum_l2r_exact_moment_lp.py).  An independent driver,
[ksum/tools/ksum_l2r_exact_verify.py](../tools/ksum_l2r_exact_verify.py), rebuilt every orbit class and
moment row, checked exact (\ell_1=1), exact correlations, zero rational residuals, and independently
matched all 24 optima with maximum numerical discrepancy (1.12\times10^{-16}).  Results and raw logs
are in [logs_ksum_L2r_20260719](logs_ksum_L2r_20260719/).

## R2 — cap-compatible P4 obligation

### Exact corrected statement

**Conjectured cap-compatible joint-histogram witness lemma.**  There exist fixed constants

\[
  \eta\in(1/6,1/4],\qquad c_0>0,\qquad \delta\in(0,1/3),\qquad N_0\in\mathbb N
\]

such that for every (N\ge N_0), every integer (3\le q\le N), and every target
(t\in\mathbb Z_q), with (\sigma(a)=t-a), there is an
(S_N\times C(\sigma))-invariant signed measure (\mu_{N,q,t}) on ((\mathbb Z_q)^N) satisfying

\[
  \lVert\mu_{N,q,t}\rVert_1=1,
  \qquad
  \langle\mu_{N,q,t},F_{N,q,t}\rangle\ge\frac23+\delta,
\]

and

\[
  \langle\mu_{N,q,t},p\rangle=0
  \quad\text{for every query polynomial }p\text{ with }
  \deg p<c_0\min\{\sqrt N\,q^\eta,N^{2/3}\}.
\]

Equivalently, the unrestricted-form target (c_0\sqrt N,q^\eta) is required on

\[
  3\le q\le N^{1/(6\eta)},
\]

because

\[
  \sqrt N\,q^\eta\le N^{2/3}
  \iff q^\eta\le N^{1/6}
  \iff q\le N^{1/(6\eta)}.
\]

At (\eta=1/4), the endpoint is exactly (q=N^{2/3}).

### Cap sweep

The proved upper bounds relevant to cyclic 2-Sum in the paper are:

1. the range-independent Johnson bound (O(N^{2/3})), valid for every (q); and
2. B4a's independently reviewed (O_\varepsilon(N^{1/2+\varepsilon}q^{1/4})), valid for every
   (q\ge2), every target, and all sufficiently large (N).

At both endpoints of the unrestricted range, the target stays below both caps:

| endpoint | target (\sqrt N q^\eta) | versus (N^{2/3}) walk | versus (N^{1/2+\varepsilon}q^{1/4}) |
|---|---:|---|---|
| (q=3) | (3^\eta\sqrt N) | (3^\eta N^{-1/6}\to0) relative to the cap | (3^\eta\le3^{1/4}) since (\eta\le1/4) |
| (q=N^{1/(6\eta)}) | (N^{2/3}) | equal in exponent | upper exponent (1/2+1/(24\eta)+\varepsilon\ge2/3+\varepsilon) |

The same inequalities cover every intermediate point by monotonicity.  They also cover the capped
statement throughout (3\le q\le N): below the crossover,
(\sqrt N q^\eta\le\sqrt N q^{1/4}); above it, the target is (N^{2/3}), while
(q^{1/4}\ge N^{1/(24\eta)}\ge N^{1/6}), so
(N^{2/3}\le\sqrt N q^{1/4}).  Thus the restated target never exceeds either proved cap anywhere in
its stated range.  The trivial full-read (O(N)) bound is weaker than the walk cap and adds no
constraint.

The target value remains (\eta=1/4); any fixed (\eta>1/6) would advance the lower exponent while
remaining cap-compatible.  Constructing the witness, preserving low-degree cancellations under the
total-occupancy condition, and obtaining uniform norm/correlation constants remain open.

## R3 — P2 bookkeeping correction

The reviewed P2 result is only the shell deficit.  The two archived invariant optimizer matrices
have respectively (27.0428) and (25.2457) percentage points of squared Frobenius mass outside the
specified label/distinguished-pair/Hamming-distance coarsening.  Full joint-orbital capture is forced
by invariant reconstruction followed by projection onto the full symmetric orbital space; its 100%
column is a construction check and supplies no independent route evidence.

Accordingly, every L2 repair summary must describe P2 as narrow finite shell-deficit structure
evidence.  It does not establish one-input dual-polynomial expressiveness, optimizer uniqueness,
asymptotic separation, or separation from every Belovs--Spalek shell algebra.

## Provenance and limits

- Preregistration: [predictions.txt](logs_ksum_L2r_20260719/predictions.txt).
- Exact output: [exact_lp_results.json](logs_ksum_L2r_20260719/exact_lp_results.json).
- Solver log: [exact_lp.log](logs_ksum_L2r_20260719/exact_lp.log).
- Independent reconstruction log: [exact_verify.log](logs_ksum_L2r_20260719/exact_verify.log).
- Commands: [COMMANDS.txt](logs_ksum_L2r_20260719/COMMANDS.txt).
- SHA-256 manifest: [SHA256SUMS.txt](logs_ksum_L2r_20260719/SHA256SUMS.txt).

G11 remains binding: these (N\le5) exact LPs do not imply an exponent.  This pass did not construct
the asymptotic kernel, prove the cap-compatible lemma, test additional points or cycle types, rerun
the optimizer extraction, establish a one-input/held-out P2 discriminator, or perform an independent
completion review.
