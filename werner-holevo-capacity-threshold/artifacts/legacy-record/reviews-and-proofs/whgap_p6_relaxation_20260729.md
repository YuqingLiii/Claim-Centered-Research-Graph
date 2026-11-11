# WHGAP P6: cBKM order boundary and relaxed two-sided lift

Date: 2026-07-29
Primary node: `WHGAP.order-boundary`
Secondary evidence node: `WHGAP.relaxed-lift`
Role: executor
Interpreter for every Python invocation: `C:<home>/cpython3119/python.exe`

## Outcome

Both calibrated campaigns passed.

- E1 found and directed-interval-certified a cBKM-order violation at every prescribed
  below-\(1/2\) grid point, including \(x=499/1000\). The 150-restart searches at \(x=1/2\)
  and \(x=11/20\) found no value below the preregistered \(-10^{-9}\) floor. Warm bisection
  gives the numerical bracket
  \[
  x_B\in[7999/16000,1/2],\qquad |I|=1/16000.
  \]
  The upper/no-violation side is bounded-search evidence, not a theorem.
- D2 found no counterexample in 200 random complex-linear instances and 4,000 random
  Hermitian-direction tests.
- S3 imposed the intertwining identity with the true Hilbert--Schmidt adjoint. The complex
  covariant ansatz has a six-real-dimensional residual family. Both real forced-point sanity
  solutions were recovered, but 100-restart two-Choi searches at \(49/100,47/100,9/20\)
  remained infeasible. This agrees with the E1 containment requirement.

Accordingly, preregistered interpretations **G2-E1(a)** and **G2-E2(b)** apply. The evidence
supports the numerical picture that the tested cBKM-order reach ends at \(1/2\), and that
criterion (W) does not extend below \(1/2\) within the full complex covariant ansatz.

This is proposer-authored numerical evidence. `WHGAP.order-boundary` is therefore capped at
`NUMERICAL` with `pending-review:`. No status change is made to `WHGAP.relaxed-lift`.

## Conventions and scanner

The channel and four-dimensional padded complement use the frozen P1/P2 Kraus convention.
All operator matrices use row-major Hilbert--Schmidt coordinates. For reference dimension
\(d_R\), the scanner builds dense superoperators for
\(\operatorname{id}_R\otimes\Lambda_x\) and
\(\operatorname{id}_R\otimes\Lambda_x^c\). At faithful \(\sigma_{RA}\), it diagonalizes each
output state and constructs
\[
\Gamma_\theta^{-1}(Z)_{ij}
=c(\lambda_i,\lambda_j)Z_{ij},\qquad
c(a,b)=\frac{\log a-\log b}{a-b},\quad c(a,a)=a^{-1}.
\]
It then diagonalizes
\[
T_{\Lambda_x^c}[\sigma]-T_{\Lambda_x}[\sigma]
\]
on the full complex operator space. The Hermitian eigendirections returned in every
reported minimum were checked directly.

Every \((x,d_R)\) received 150 faithful Cholesky starts:
one maximally mixed start, 30 P3-direction starts, 50 near-pure starts, 29 random product
starts, and 40 random full-rank starts. The first configuration projected past the
commission's 20-minute single-step limit because each \(d_R=3\) pair took about 144 seconds.
The preserved cheaper route still evaluated all 150 \(d_R=3\) Cholesky starts, followed by
a five-step incumbent refinement; it reduced those pairs to roughly 40--69 seconds.

Two calibration-only conditioning attempts are preserved. Attempt 2 exposed cancellation
at the known-good \(x=11/20\) anchor for an ill-conditioned generic product start. The final
run imposed a \(10^{-3}\) conditioning floor on generic product/random starts while retaining
separate near-pure and P3 categories. Its clean-side absolute floors passed G0b.

## E1: calibrated scan

All entries are the smallest eigenvalue found after 150 restarts. `--` is not used: every
prescribed pair completed successfully.

| \(x\) | \(d_R=1\) | \(d_R=2\) | \(d_R=3\) |
|---:|---:|---:|---:|
| \(7/20\) | -7.068337e2 | -2.213657e3 | -2.423620e3 |
| \(1/2\) | -3.56e-13 | -1.60e-12 | -2.22e-11 |
| \(11/20\) | -2.84e-13 | -7.01e-13 | -6.85e-10 |
| \(2/5\) | -5.095018e2 | -6.786109e2 | -1.685558e3 |
| \(21/50\) | -3.460440e2 | -4.642966e2 | -1.192390e3 |
| \(11/25\) | -1.999487e2 | -2.720432e2 | -7.573760e2 |
| \(23/50\) | -7.129618e1 | -1.576446e2 | -3.769972e2 |
| \(12/25\) | -8.622217 | -5.273382 | -4.867273e1 |
| \(49/100\) | -2.716873 | -5.726223e-1 | -5.48e-10 |
| \(499/1000\) | -1.882155e-2 | -1.03e-12 | -1.73e-10 |

G0a passes numerically by a large margin at every reference dimension. G0b passes:
the worst clean-side value is \(-6.85\times10^{-10}>-10^{-9}\).

The best-state character changes toward the edge. P3 and warm P3-derived starts dominate
through much of the strip; near-pure \(d_R=1\) starts produce the decisive \(12/25\) and
\(499/1000\) witnesses; product starts contribute at several \(d_R=2,3\) points. Full
per-restart categories, conditioning, state spectra, rational matrices, and optimizer
statistics are in `logs_whgap_p6_20260729/e1_scan.json`.

## S2: rational witnesses and boundary

For each violating \(x\), the best \(d_R=1\) state and eigendirection were rationalized with
denominator cap \(10^8\), Hermitized, trace/Frobenius normalized, and re-evaluated at 110
mpmath digits and 80 directed interval digits. Approximate Hermitian eigensystems were
enclosed using the eigenpair residual divided by the nearest distinct spectral gap.
Overlapping eigenvalue intervals used reciprocal monotonicity bounds for the logarithmic
divided difference, avoiding division through zero at degeneracies.

The certified Rayleigh-quotient upper bounds are:

| \(x\) | directed interval upper bound |
|---:|---:|
| \(7/20\) | -706.8337153347308908 |
| \(2/5\) | -509.5018499367674946 |
| \(21/50\) | -346.0439601283458224 |
| \(11/25\) | -199.9487051908100587 |
| \(23/50\) | -71.29618296453720144 |
| \(12/25\) | -8.622217377750481749 |
| \(49/100\) | -2.716872982752963483 |
| \(499/1000\) | -0.01882155247271301806 |

The full rational state/eigendirection data and spectral enclosures are in
`logs_whgap_p6_20260729/e1_certificates.json`.

Warm \(d_R=1\), 150-restart bisection classified \(999/2000\), \(1999/4000\),
\(3999/8000\), and \(7999/16000\) as violations. Together with the calibrated no-violation
search at \(1/2\), this gives
\[
[x_B^-,x_B^+]=[7999/16000,1/2],\qquad x_B^+-x_B^-=1/16000<10^{-4}.
\]
Only the lower endpoint is a certified violation. The upper classification remains
bounded-search evidence.

## D2: criterion-(W) soundness stress test

Each of 200 instances used output dimensions \(m\leq3\), \(n\leq4\), faithful positive
\(\sigma,\omega\), and a scaled isometric feasible map plus a random complex perturbation in
the exact affine nullspace of \(J^\dagger(\omega)=\sigma\). This is the one-dimensional
state-preparation specialization, in which the two endpoint defect matrices are exactly
the left/right defect Chois. The perturbation was shrunk until both were PSD. This
construction deliberately left the adjoint-preserving class: the maximum sampled
adjoint-preservation residual was 0.9875.

Twenty random Hermitian \(Z\)'s per instance tested
\[
g_\omega(Z)-g_\sigma(J^\dagger Z)\geq0.
\]
All 4,000 tests passed. The minimum defect floor was \(1.5705\times10^{-4}\), and the minimum
conclusion margin was \(2.3553\times10^{-7}\). No decisive counterexample was found.

This is a randomized stress test of the endpoint linear-algebra core, not an independent
proof of criterion (W).

## S3: true-adjoint complex covariant ansatz

The ansatz
\[
J(Y)=\begin{pmatrix}
p\operatorname{Tr}Y&u\,a(Y)^T\\
v\,a(Y)&c_1\operatorname{Tr}(Y)I+c_2Y+c_3Y^T
\end{pmatrix}
\]
was represented as a \(16\times9\) complex superoperator. Its adjoint in the intertwining
identity was its conjugate transpose, not its transpose.

An exact SymPy calculation on all nine complex matrix units at the generic interior
calibration \(x=2/5\) gives real rank 6 and therefore residual real dimension 6. One exact
parameterization is recorded verbatim in `s3_feasibility.json`; the six free real variables
may be taken as the real and imaginary parts of \(v,c_1,c_3\).

For CP testing, the left Choi uses block \(\Delta^L(E_{ab})\). Right multiplication lives on
the opposite algebra, so the right-action Choi uses block \(\Delta^R(E_{ba})\). This
convention is forced by the P2 sanity gate: using ordinary \(E_{ab}\) blocks produces a
partial transpose and a false negative floor, preserved in
`s3_feasibility_attempt1_right_choi_bug.log`. With the correct convention, both P2
forced-point Chois are reproduced at numerical zero.

Every point received 100 penalty-minimization restarts over the six-dimensional affine
family. The objective was total squared negative-eigenvalue mass of the two \(27\times27\)
Chois.

| \(x\) | left floor | right floor | penalty | feasible? |
|---:|---:|---:|---:|:---:|
| \(13/25\) | -3.66e-16 | -3.29e-16 | 6.53e-31 | yes (sanity) |
| \(1/2\) | -8.47e-16 | -8.24e-16 | 4.41e-30 | yes (sanity) |
| \(49/100\) | -6.453736e-2 | -6.453736e-2 | 4.716205e-2 | no |
| \(47/100\) | -2.086487e-1 | -2.086487e-1 | 4.879670e-1 | no |
| \(9/20\) | -3.752621e-1 | -3.752621e-1 | 1.563743 | no |

The spin commutator residual is at most \(6.1\times10^{-16}\), so the O(3) spin reduction
extends to the complex ansatz and to both right/left Chois. The implementation nevertheless
diagonalized the full matrices. S3 used 794.6 seconds, below its 2,100-second cap.

No below-\(1/2\) point was feasible, so there is no exact PSD certificate to rationalize and
no containment contradiction with E1.

## Preregistered interpretations

- **G2-E1(a): applies.** Certified violations occur at every prescribed strip grid point
  through \(499/1000\). The signed-lift reach \([1/2,1)\) coincides with the tested order
  reach, with only bounded-search evidence on the no-violation side.
- **G2-E2(b): applies.** All complex-covariant two-sided searches floor out below \(1/2\);
  the forced structure and spin symmetry persist. Within this ansatz, the edge appears
  order-driven rather than an artifact of adjoint preservation.

No interpolation beyond the displayed bisection bracket is claimed.

## Reproduction and provenance

Scripts:

- `tools/whgap_p6_common.py`
- `tools/whgap_p6_e1_scan.py`
- `tools/whgap_p6_e1_certify.py`
- `tools/whgap_p6_d2_soundness.py`
- `tools/whgap_p6_s3_feasibility.py`

Machine results and raw logs are under `artifacts/logs_whgap_p6_20260729/`. The directory's
`SHA256SUMS.txt` covers the scripts, this artifact, JSON results, raw logs, and validator
logs. Failed/capped attempts are append-only and remain in that directory.

Closeout disk note: while P6 was running, repository HEAD advanced to commit `8a094c0`
(registering P9--P11 and the in-flight P6 scaffold), so those concurrent disk additions
were preserved. The required global `git diff --check` exited 0 before the live tracked
session transcript accumulated pasted patch lines with trailing spaces. A final scoped
check over every commissioned code, artifact, node, index, DAG, and forwarding-stub path
also exited 0; the active `tmp/codex_whgap_p6_20260729.log` was not rewritten.

