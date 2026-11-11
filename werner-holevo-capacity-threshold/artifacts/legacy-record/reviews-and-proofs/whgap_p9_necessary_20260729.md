# WHGAP P9 necessary-condition scans — execution artifact (2026-07-29)

Nodes: `WHGAP.no-ascent-hierarchy` (E1) and
`WHGAP.choi-distillation-necessary` (E2). Executor evidence only. E1 remains
CONJECTURED as commissioned. E2 is NUMERICAL with `pending-review:`. No
completion-tier status is claimed.

## Executive result

E1 stopped at G0. The displayed fixed pure-output spectrum is exact on the
real-up-to-phase orbit but false for a generic complex pure input. More
fundamentally, the stated environment-support constraint left only
\(\phi=\psi\) in four generic tests, so the requested distinct
kernel-avoiding epsilon pairs and the S1/S2 optimization domains could not be
formed. The kernel-hitting \(-\epsilon\log(1/\epsilon)\) plunge did pass.

E2 passed D2 and returned the pre-registered G2-E2 bounded null after the
one-way direction was enforced: at every requested strip point, 273 one-copy
and 36 correlated two-copy filtered-hashing trials stayed below the
\(10^{-10}\)-bit/use numerical floor. The \(77/200\) hashing anchor was
positive and the proved-zero \(1/2,11/20\) anchors were at floor.

## Frozen conventions and commands

All entropies in the derivation check are natural. Filtered-hashing rates are
reported in bits. The channel Kraus operators were
\[
K_0=\sqrt{1-x}\,I_3,\qquad
K_{\mu+1}=\sqrt{x/2}\,A_\mu,\quad
(A_\mu)_{jk}=\epsilon_{\mu jk}.
\]

Execution interpreter:
`C:<home>/cpython3119/python.exe`.

```powershell
& 'C:<home>/cpython3119/python.exe' tools/whgap_p9_g0.py
& 'C:<home>/cpython3119/python.exe' tools/whgap_p9_distillation.py --allow-two-sided
& 'C:<home>/cpython3119/python.exe' tools/whgap_p9_distillation.py
```

The first command exited 2 by design after writing its G0-failure JSON. The
second direction-valid command exited 0. The earlier literal two-sided-filter
calibration attempt is preserved in the log directory.

The disk pre-task prompt required
`C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe` for the two
closeout validators, conflicting with the dispatch's cpython-only rule. The
conflict was reported before work. At closeout the disk-requested path was
absent (`CommandNotFoundException`), so both validators were run successfully
with `C:<home>/cpython3119/python.exe`; the failed launch is preserved in
`validator_interpreter_missing.log`.

## E1 — D1 and gate G0

### Exact pure-output spectra

For \(a=1-x\), \(b=x/2\), \(u=\psi\), and \(v=\bar\psi\),
\[
\Lambda_x(|\psi\rangle\langle\psi|)
  =bI+a uu^\dagger-bvv^\dagger.
\]
Writing \(r^2=|\psi^T\psi|^2\), its exact eigenvalues are
\[
b,\qquad
\frac{1-b\pm\sqrt{(1-b)^2-4abr^2}}2.
\]
The complementary pure output has the same three nonzero eigenvalues and one
additional zero. Thus the commission's displayed fixed spectra follow only
when \(r^2=1\), i.e. for a real-up-to-phase input.

At \(x=9/20\), the exact real test \(\psi=(1,0,0)\) passed:
\[
\operatorname{spec}\Lambda_x(\psi)=\{11/20,9/40,9/40\},\qquad
\operatorname{spec}\Lambda_x^c(\psi)=\{11/20,9/40,9/40,0\}.
\]
The exact generic complex test
\(\psi=(1,i,1)/\sqrt3\), for which \(r^2=1/9\), failed the claim:
\[
\operatorname{spec}\Lambda_x(\psi)=
\left\{9/40,\frac{31-3\sqrt{97}}{80},
\frac{31+3\sqrt{97}}{80}\right\},
\]
with the same nonzero environment spectrum plus zero.

### Support and epsilon-expansion gate

Let \(z\) span the kernel of \(\Lambda_x^c(\psi)\) and
\(L_z=\sum_a\bar z_aK_a\). Positivity gives
\[
\operatorname{supp}\Lambda_x^c(\phi)
 \subseteq\operatorname{supp}\Lambda_x^c(\psi)
\quad\Longrightarrow\quad
0=z^\dagger\Lambda_x^c(\phi)z
  =\operatorname{Tr}(L_z\phi L_z^\dagger),
\]
so \(\operatorname{supp}\phi\subseteq\ker L_z\).
For four seeded generic complex pure inputs, \(L_z\) had a one-dimensional
kernel, with annihilation residuals between \(6.4\times10^{-17}\) and
\(2.6\times10^{-16}\). Consequently the only allowed state was
\(\phi=\psi\): there were no distinct random kernel-avoiding pairs on which
to perform the commissioned eight-digit slope fit.

For random kernel-hitting states, the numerical ratios
\[
\frac{I_c((1-\epsilon)\psi+\epsilon\phi)}
 {\epsilon\log(1/\epsilon)}
\]
were strictly negative at
\(\epsilon=10^{-5},10^{-7},10^{-9}\) in all four tests and approached the
independently computed kernel weights with the expected negative sign.

**G0: FAIL.** S1 and S2 were not entered.

### S1 table

| \(x\) | restarts | max \(A_1\) | argmax | certified? |
|---:|---:|---:|---|---|
| \(77/200\) | 0 | not run | G0 failed | no |
| \(2/5\) | 0 | not run | G0 failed | no |
| \(21/50\) | 0 | not run | G0 failed | no |
| \(11/25\) | 0 | not run | G0 failed | no |
| \(23/50\) | 0 | not run | G0 failed | no |
| \(12/25\) | 0 | not run | G0 failed | no |
| \(49/100\) | 0 | not run | G0 failed | no |
| \(11/20\) | 0 | not run | G0 failed | no |

### S2 table

| \(x\) | restarts | max \(A_2\) | per-\(\psi_2\) support projector | certified? |
|---:|---:|---:|---|---|
| \(21/50\) | 0 | not run | not constructed after G0 fail | no |
| \(11/25\) | 0 | not run | not constructed after G0 fail | no |
| \(23/50\) | 0 | not run | not constructed after G0 fail | no |
| \(12/25\) | 0 | not run | not constructed after G0 fail | no |
| \(49/100\) | 0 | not run | not constructed after G0 fail | no |

G2-E1 interpretations (a)–(c) were not reached. In particular, there is no
positive strip point and no bounded-null statement for the no-ascent
hierarchy.

## E2 — D2 hashing calibration

The normalized Choi state has exact spectrum
\[
\{1-x,x/3,x/3,x/3,0,0,0,0,0\}.
\]
Therefore
\[
-S(A|B)_{\omega_x}
=\log_2 3+(1-x)\log_2(1-x)+x\log_2(x/3)
=I_c(\pi,x).
\]
The 80-digit root was
\[
x_1=0.39091023207618132348272185313419912790500737721327\ldots.
\]
Formula and direct Choi-matrix evaluation agreed within
\(2\times10^{-14}\) bits at all calibration points; signs were positive
exactly below \(x_1\) on the registered test set.

## E2 — S3 filtered hashing

### Direction audit

The commission's literal arbitrary \(F_A,F_B\) postselection was run first.
It produced apparent positive rates \(0.0408521\) at \(x=1/2\) and
\(0.0205158\) at \(x=11/20\), contradicting the proved-zero calibration
regime. The winning rank-two projector on both sides requires conditioning
on Bob's success, hence backward communication. This failed attempt is
preserved but is not interpreted as a one-way \(A\to B\) protocol.

The registered rerun permits stochastic postselection on Alice and leaves
Bob's operation trace preserving (\(F_B=I\)). This is the direction-valid
meaning of the filtered-hashing lower bound used below.

The one-copy inventory at every \(x\) was:

- 117 diagonal rank-\(\le3\) filters and coordinate projectors;
- 36 real \(O(3)\)-adapted rank-one/rank-two projectors;
- 120 random complex low-rank filters.

The correlated two-copy inventory at every \(x\) was:

- identity, maximally correlated, antisymmetric, symmetric, and two crossed
  named projectors;
- 30 random correlated low-rank filters on Alice's \(A_1A_2\) system.

### One-copy table

| \(x\) | trials | best rate (bits/use) | result |
|---:|---:|---:|---|
| \(21/50\) | 273 | \(2.22\times10^{-16}\) | floor |
| \(11/25\) | 273 | \(2.22\times10^{-16}\) | floor |
| \(23/50\) | 273 | \(4.81\times10^{-16}\) | floor |
| \(12/25\) | 273 | \(2.59\times10^{-16}\) | floor |
| \(49/100\) | 273 | \(4.44\times10^{-16}\) | floor |
| \(77/200\) | 273 | \(1.32549871199557\times10^{-2}\) | positive anchor |
| \(1/2\) | 273 | \(2.59\times10^{-16}\) | floor anchor |
| \(11/20\) | 273 | \(2.96\times10^{-16}\) | floor anchor |

### Correlated two-copy table

Rates are divided by two to report bits per channel use.

| \(x\) | trials | best rate (bits/use) | result |
|---:|---:|---:|---|
| \(21/50\) | 36 | \(0\) | floor |
| \(11/25\) | 36 | \(0\) | floor |
| \(23/50\) | 36 | \(2.47\times10^{-17}\) | floor |
| \(12/25\) | 36 | \(0\) | floor |
| \(49/100\) | 36 | \(0\) | floor |
| \(77/200\) | 36 | \(1.32549871199554\times10^{-2}\) | positive anchor |
| \(1/2\) | 36 | \(0\) | floor anchor |
| \(11/20\) | 36 | \(0\) | floor anchor |

**G2-E2: bounded-null.** No positive direction-valid filtered-hashing rate
above \(10^{-10}\) bits/use was found in the strip. This statement is limited
to the listed families and budgets; it is not a proof of one-way
undistillability.

## Runtime and caps

| step | wall/recorded runtime | cap | outcome |
|---|---:|---:|---|
| E1 G0 | about 6.6 s shell wall | 20 min | failed gate, stopped |
| preliminary two-sided E2 | 13.938 s | 20 min | rejected by anchors |
| direction-valid E2 total | 14.750 s | 20 min | completed |
| direction-valid two-copy E2 | 13.844 s | 30 min | completed |
| total commissioned compute | below 40 s | 90 min | respected |

No single step approached 20 minutes; both specially capped layers remained
well below 30 minutes.

## Provenance

Scripts:

- `tools/whgap_p9_g0.py`
- `tools/whgap_p9_distillation.py`

Machine outputs and raw logs are under
`artifacts/logs_whgap_p9_20260729/`. `SHA256SUMS.txt` inventories this
artifact, both scripts, all JSON outputs, raw logs, the run manifest, and
validator logs.

`pending-review:` all findings are executor-authored and await an independent
rule-7 review.

