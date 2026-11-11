# WHGAP P9b — repaired no-ascent hierarchy G0' execution (2026-07-29)

Node: `WHGAP.no-ascent-hierarchy`

Role: executor

Interpreter: `C:<home>/cpython3119/python.exe`

Pre-registered interpretation: **G2(c), G0' failure — repair falsified; STOP**

## Verdict

**G0' FAIL; S1'/S2'/S3' were not entered.**

The repaired isotropic spectra, the exact \(\tau\)-interpolation, all three random
isotropic checks, and all five unbalanced epsilon fits pass. The failed component
is the commissioned construction of at least three nontrivial balanced pairs at
\(x=9/20\): no such pair exists.

For the canonical isotropic state
\[
  \psi=(0,1,-i)^T/\sqrt2
\]
and the basis \((e_0,\bar\psi,\psi)\), exact SymPy arithmetic gives
\[
 D_\psi:=M_B-M_E
 =\operatorname{diag}\!\left(-\frac{99}{620},-\frac{11}{124},0\right),
 \qquad
 w_B-w_E=\operatorname{Tr}(D_\psi\phi).
\]
Thus \(D_\psi\preceq0\) and its kernel is the single ray
\(\operatorname{span}\{\psi\}\). For a density matrix \(\phi\),
\(\operatorname{Tr}(D_\psi\phi)=0\) holds only for
\(\phi=|\psi\rangle\langle\psi|\). Mixing that endpoint with any distinct state
immediately makes \(w_B-w_E<0\). The standard \(O(3)\) covariance transports
this diagonalization to every isotropic pure state because the isotropic
projectors form one \(O(3)\)-orbit. Consequently zero of the required three
distinct balanced pairs can be constructed.

This is narrower than a failure of the whole isotropic repair: it falsifies the
decision layer's assumed **nontrivial balanced layer at \(x=9/20\)**, while the
isotropic spectra and unbalanced leading asymptotic pass. The pre-registered
gate nevertheless says that any G0' failure stops the campaign, so no S1', S2',
or S3' result is claimed.

## G0'(i): parameterized isotropic spectra

Use the rational stereographic chart
\[
\begin{aligned}
d&=1+p^2+q^2,\\
u&=(1-p^2+q^2,-2pq,-2p)^T/d,\\
v&=(-2pq,1+p^2-q^2,-2q)^T/d,\\
\psi&=(u+iv)/\sqrt2 .
\end{aligned}
\]
Exact simplification verifies \(u^Tu=v^Tv=1\), \(u^Tv=0\),
\(\psi^\dagger\psi=1\), and \(\psi^T\psi=0\). This chart covers the
isotropic pure projectors, apart from one chart point supplied by continuity.

For symbolic \(p,q,x\), the receiver characteristic polynomial reduces exactly
to
\[
 \lambda(\lambda-x/2)(\lambda-(1-x/2)).
\]
If \(C=[K_0\psi,\ldots,K_3\psi]\), the receiver and environment outputs are
\(CC^\dagger\) and \(C^\dagger C\). Sylvester's determinant identity gives
\[
 \det(\lambda I_4-C^\dagger C)
 =\lambda\det(\lambda I_3-CC^\dagger),
\]
so the spectra are
\[
\operatorname{spec}\Lambda(P)
 =\{0,x/2,1-x/2\},\qquad
\operatorname{spec}\Lambda^c(P)
 =\{0,0,x/2,1-x/2\}.
\]

Three seeded QR-generated isotropic samples at \(x=9/20\) passed. The largest
receiver-spectrum error was \(2.22\times10^{-16}\); the largest environment
error was \(4.44\times10^{-16}\).

## G0'(ii): exact \(\tau\)-interpolation

For
\[
 \psi_\tau=\left(\sqrt{\frac{1+\tau}{2}},
 i\sqrt{\frac{1-\tau}{2}},0\right)^T,
\]
one has \(|\psi_\tau^T\psi_\tau|=\tau\). With \(a=1-x\) and \(b=x/2\),
the receiver spectrum is
\[
 \left\{
 b,\frac{1-b-\sqrt{(1-b)^2-4ab\tau^2}}2,
 \frac{1-b+\sqrt{(1-b)^2-4ab\tau^2}}2
 \right\},
\]
and the environment has the same nonzero spectrum plus one zero.

At \(x=9/20\):

| \(\tau\) | Receiver spectrum | Environment spectrum | Result |
|---:|---|---|---|
| \(1\) | \(\{9/40,9/40,11/20\}\) | receiver plus \(0\) | PASS |
| \(1/2\) | \(\{(31-\sqrt{763})/80,9/40,(31+\sqrt{763})/80\}\) | receiver plus \(0\) | PASS |
| \(0\) | \(\{0,9/40,31/40\}\) | \(\{0,0,9/40,31/40\}\) | PASS |

The prior P9 failure sample \((1,i,1)^T/\sqrt3\) has
\(\tau=1/3\) and reproduces exactly
\[
 \left\{\frac{31-3\sqrt{97}}{80},\frac9{40},
 \frac{31+3\sqrt{97}}{80}\right\},
\]
with one additional environment zero. This is the previously observed spectrum.

## G0'(iii): epsilon fits

The script used 90-decimal-digit Mpmath eigensolvers. Five deterministic
rational-chart isotropic states and five seeded rational positive density
matrices were fitted across 16 logarithmically spaced epsilon values from
\(10^{-9}\) through \(10^{-4}\). The regression model was
\[
 I_c=a\epsilon\log(1/\epsilon)+c\epsilon
 +d\epsilon^2\log(1/\epsilon)+e\epsilon^2.
\]
The last two terms stabilize extraction of the first two coefficients across
the full prescribed range.

| Sample | \(p\) | \(q\) | Exact-object \(w_B-w_E\) | Fitted \(a\) | Relative error |
|---:|---:|---:|---:|---:|---:|
| 0 | \(1/3\) | \(2/5\) | -0.06172878525512547 | -0.06172878552169949 | \(4.32\times10^{-9}\) |
| 1 | \(-2/7\) | \(3/4\) | -0.10109315429973359 | -0.10109315467951449 | \(3.76\times10^{-9}\) |
| 2 | \(4/9\) | \(-1/5\) | -0.10955155473632119 | -0.10955155536620661 | \(5.75\times10^{-9}\) |
| 3 | \(2/11\) | \(5/8\) | -0.07516111939293748 | -0.07516111952925204 | \(1.81\times10^{-9}\) |
| 4 | \(-3/8\) | \(-2/9\) | -0.09132820501949583 | -0.09132820528944114 | \(2.96\times10^{-9}\) |

All five leading coefficients agree far beyond the commissioned six digits.

For the balanced requirement, the exact diagonalization above proves that the
only balanced state at \(x=9/20\) is \(\phi=P_\psi\). Three chart points were
also checked numerically: solving the proposed convex-mixing equation always
returns the endpoint mixing parameter \(t=0\), and \(I_c(P_\psi)=0\) to the
90-digit eigensolver floor. These are trivial diagnostics, not three distinct
balanced pairs. Component verdict: **FAIL**.

## Scope and pre-registered stopping rule

| Stage | Outcome |
|---|---|
| G0'(i), parameterized and random spectra | PASS |
| G0'(ii), \(\tau\)-generic cross-check | PASS |
| G0'(iii), five unbalanced fits | PASS |
| G0'(iii), three nontrivial balanced pairs by mixing | **FAIL: set is trivial at \(x=9/20\)** |
| S1' | NOT ENTERED — G2(c) stop |
| S2' | NOT ENTERED — G2(c) stop |
| S3' | NOT ENTERED — G2(c) stop |

No strip-positive or bounded-null G2(a)/(b) interpretation is made.
`WHGAP.no-ascent-hierarchy` remains `CONJECTURED`; this executor appends evidence
only, with `pending-review:`.

## Provenance and retained failed attempts

Primary machine record:
`artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.json`.
Raw log:
`artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.log`.
Script: `tools/whgap_p9b_g0.py`.

Three earlier checker-only attempts are retained append-only. Attempt 1 used an
overstrict symbolic characteristic-polynomial equality and an unsorted expected
multiset; attempts 2 and 3 retained the overstrict symbol-assumption comparison.
Their printed polynomials and spectra already agreed; the final record fixes
only those checker defects. They are not used for the verdict.

The generic reload prompt requested the WindowsApps Python path for validators,
while this problem-specific commission and dispatch require
`C:<home>/cpython3119/python.exe` for every invocation and call it the
pinned interpreter. This conflict was reported in the pre-action report; the
problem-specific pinned interpreter was used throughout.

All exact file hashes, including the raw and retained attempt logs, are in
`artifacts/logs_whgap_p9b_20260729/SHA256SUMS.txt`.

