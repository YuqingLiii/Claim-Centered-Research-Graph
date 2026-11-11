# WHGAP P2 — covariant signed-lift extension (2026-07-28)

Target node: `WHGAP.signed-lift-extension`
Role: executor
Status ceiling: **NUMERICAL; pending independent rule-7 review**

## Outcome

All commissioned gates passed. Exact all-principal-minor elimination gives

\[
s_1(x)=\frac{2(1-x)}{3x},\qquad
s_2(x)=\frac{5x-2}{3x},
\]

and the covariant residual family has a positive-semidefinite defect Choi matrix exactly for
\(1/2\leq x<1\). Therefore

\[
x_{\min}=1/2,\qquad x_{\max}=\sup[1/2,1)=1
\quad (x_{\max}=1.00000000\text{ numerically}).
\]

This is pre-registered interpretation **G2(a)**: covariant signed-lift certificates cover
\([1/2,4/7]\), so they are a gap-closure candidate, pending independent review and the
decision layer's write-up of the generic-theorem application. This executor does not claim a
completion-tier proof status.

## Conventions, maps, and adjoint

The run used the commission's frozen family, Kraus operators, epsilon ordering, row-major
Hilbert–Schmidt identification \(E_{ij}\leftrightarrow |i\rangle|j\rangle\), and
\(k^2=x(1-x)/2\).

For \(Z=\begin{bmatrix}z_{00}&r^T\\c&D\end{bmatrix}\in M_4\), direct matrix-unit adjunction gives

\[
(\Lambda_x^c)^\dagger(Z)
=(1-x)z_{00}I_3
+k\sum_{\mu=0}^2(r_\mu-c_\mu)A_\mu
+\frac{x}{2}\left(\operatorname{Tr}(D)I_3-D^T\right).
\]

The exact calibration verified

- \(\Lambda_x(I)=I\) and
  \(\Lambda_x^c(I)=\operatorname{diag}(3(1-x),x,x,x)\), positive definite for \(0<x<1\);
- scalar/symmetric-traceless/skew eigenvalues
  \(1,1-3x/2,1-x/2\);
- the frozen general-\(x\) complement and its \(x=1/2\) specialization (Zhu–Wang Eq. 4.9);
- adjoint preservation of the five-real-parameter ansatz through
  \(J(E_{ji})=J(E_{ij})^T\) for all nine matrix units.

The generic signed-lift criterion itself is Zhu–Wang, Theorem 3.3 in the local
[`arxiv_2607.24693.pdf`](../channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf);
it was cited, not re-proved.

## Residual two-parameter family

The three Schur-sector equations in \((p,q,c_1,c_2,c_3)\) are

\[
\begin{aligned}
3(1-x)p+x(3c_1+c_2+c_3)&=1,\\
-\frac{x}{2}(c_2+c_3)&=1-\frac{3x}{2},\\
4kq+\frac{x}{2}(c_2-c_3)&=1-\frac{x}{2}.
\end{aligned}
\]

Their coefficient matrix has rank three for every \(0<x<1\). With
\(s_1=c_1\) and \(s_2=c_2-c_3\), the residual family is

\[
\begin{aligned}
p&=\frac{s_1x+x-1}{x-1},&
q&=-\frac{s_2x+x-2}{8k},\\
c_1&=s_1,&
c_2&=\frac{s_2x+3x-2}{2x},&
c_3&=-\frac{s_2x-3x+2}{2x}.
\end{aligned}
\]

At \((x,s_1,s_2)=(1/2,2/3,1/3)\), these are exactly
\((1/3,\sqrt2/3,2/3,-1/3,-2/3)\), recovering the Zhu–Wang lift.

At the feasible point forced by the PSD conditions, the lift simplifies to

\[
(p,q,c_1,c_2,c_3)=
\left(
\frac13,\frac13\sqrt{\frac{2(1-x)}x},
\frac{2(1-x)}{3x},\frac{7x-4}{3x},-\frac{2(1-x)}{3x}
\right).
\]

## G0: exact calibration

The 27-by-27 defect Choi matrix is real symmetric. All occurrences of \(k\) canceled to even
powers and were reduced using \(k^2=x(1-x)/2\).

At the Zhu–Wang point, the script checked entrywise

\[
C=\frac29\sum_{\mu=0}^2\operatorname{Choi}
  \bigl(\tau\mapsto G_\mu\tau G_\mu^\dagger\bigr),
\]

found exact PSD rank three, and reproduced the direct spectrum from the spin blocks.
D1–D4 and **G0 passed**. The final run independently reconstructed the complement from the
frozen Kraus operators and checked the displayed general-\(x\) adjoint on all matrix units. See
[`exact_calibration_final.log`](logs_whgap_p2_20260728/exact_calibration_final.log) and
[`exact_blocks.json`](logs_whgap_p2_20260728/exact_blocks.json).

The first calibration run passed the mathematical gates but failed during JSON serialization;
that append-only failure is retained in
[`exact_calibration.log`](logs_whgap_p2_20260728/exact_calibration.log).

## Spin reduction and exact PSD characterization

Let \(L_\mu=A_\mu\otimes I\otimes I+I\otimes A_\mu\otimes I+
I\otimes I\otimes A_\mu\) and \(\mathcal C=-\sum_\mu L_\mu^2\).
The script took the rational kernel of \(L_0\), applied the exact Casimir projectors

\[
P_j=\prod_{\ell\ne j}\frac{\mathcal C-\ell(\ell+1)I}
{j(j+1)-\ell(\ell+1)},\qquad j=0,1,2,3,
\]

and extracted rational column bases \(U_j\) of dimensions \(1,3,2,1\).
The pair \((U_j,G_j=U_j^TU_j)\) is a sqrt-free exact encoding of the isometry
\(U_jG_j^{-1/2}\). Blocks are represented by the congruences \(B_j=U_j^TCU_j\);
spectra are obtained from the generalized pencils \(B_j-zG_j\). Every basis column,
Gram matrix, and symbolic block is in
[`exact_blocks.json`](logs_whgap_p2_20260728/exact_blocks.json).

The full exact principal-minor characterization is:

- Spin 0: \(B_0\geq0\), where
  \[
  B_0=-\frac{(3s_2x-5x+2)(3s_2x+3x+2)}{24x}.
  \]
- Spin 1: its three diagonal entries must be nonnegative, its determinant is identically zero,
  and its three order-two principal minors are
  \[
  \begin{aligned}
  M_{01}&=-(3s_1x+2x-2)^2,\\
  M_{02}&=-\frac{(4s_1x+s_2x+x-2)^2}{16},\\
  M_{12}&=-\frac{(8s_1x-s_2x+7x-6)^2}{16}.
  \end{aligned}
  \]
  The exact diagonal formulas are recorded under `principal_minors.spin1` in the JSON.
- Spin 2: its two diagonal entries must be nonnegative and
  \[
  \det B_2=-\frac{(3s_2x-5x+2)^2}{16}.
  \]
- Spin 3: \(B_3=0\).

This uses every principal minor for the 3-by-3 block; no leading-minor shortcut was used.
The negative squares force the unique \(s_1,s_2\) above. Substitution reduces the blocks to

\[
\begin{aligned}
B_0&=0,\\
B_1&=\frac{4(1-x)(3x-1)}{9x}
  \begin{bmatrix}1\\-1\\1\end{bmatrix}
  \begin{bmatrix}1&-1&1\end{bmatrix},\\
B_2&=\frac{4(1-x)(2x-1)}{3x}
  \begin{bmatrix}1\\-1\end{bmatrix}
  \begin{bmatrix}1&-1\end{bmatrix},\\
B_3&=0.
\end{aligned}
\]

On \(0<x<1\), these are PSD exactly when \(x\geq1/2\). This symbolic elimination
completed in seconds, so the 15-minute per-\(x\) fallback was not triggered.

## Exact feasibility grids

Every entry uses the forced rational \(s_1,s_2\) and checks all principal minors exactly.

| \(x\) | \(s_1\) | \(s_2\) | exact PSD |
|---:|---:|---:|:---:|
| \(1/2\) | \(2/3\) | \(1/3\) | yes |
| \(26/51\) | \(25/39\) | \(14/39\) | yes |
| \(13/25\) | \(8/13\) | \(5/13\) | yes |
| \(27/52\) | \(50/81\) | \(31/81\) | yes |
| \(27/50\) | \(46/81\) | \(35/81\) | yes |
| \(5/9\) | \(8/15\) | \(7/15\) | yes |
| \(4/7-1/1000=3993/7000\) | \(6014/11979\) | \(5965/11979\) | yes |
| \(4/7\) | \(1/2\) | \(1/2\) | yes |
| \(4/7+1/100=407/700\) | \(586/1221\) | \(635/1221\) | yes |
| \(3/5\) | \(4/9\) | \(5/9\) | yes |
| \(2/3\) | \(1/3\) | \(2/3\) | yes |
| \(3/4\) | \(2/9\) | \(7/9\) | yes |

The lower-reach checks at \(1/4,1/3,2/5,49/100\) all fail because the spin-2 pivot is
negative; \(1/2\) passes. Hence \(x_{\min}=1/2\).

G1 passed at both \(1/2\) and \(26/51\). Exact feasibility at
\(x=99999999/100000000\) corroborates the endpoint report
\(x_{\max}=1.00000000\), while \(x=1\) itself is outside the commissioned faithful range.

## Three solver-free exact certificates

For each certificate, \(B_0=B_3=0\). The table gives rank-one LDL/congruence data
\(B_j=d_j\ell_j\ell_j^T\); positive rational \(d_j\) proves PSD without a solver.

| \(x\) | \((s_1,s_2)\) | \(q\) | spin-1 \((d_1,\ell_1)\) | spin-2 \((d_2,\ell_2)\) |
|---:|---:|---:|---:|---:|
| \(26/51\) | \((25/39,14/39)\) | \(5\sqrt{13}/39\) | \((50/221,(1,-1,1))\) | \((50/1989,(1,-1))\) |
| \(4/7\) | \((1/2,1/2)\) | \(\sqrt6/6\) | \((5/21,(1,-1,1))\) | \((1/7,(1,-1))\) |
| \(3/4\) | \((2/9,7/9)\) | \(\sqrt6/9\) | \((5/27,(1,-1,1))\) | \((2/9,(1,-1))\) |

At all three points, the direct 27-by-27 characteristic polynomial equals the product of
the four generalized spin-block characteristic polynomials with multiplicities \(2j+1\).
The exact polynomials and full block matrices are in
[`feasibility_certificates.json`](logs_whgap_p2_20260728/feasibility_certificates.json).

## Twirling-WLOG ingredients

The exact covariance checks use

\[
V(O)=\operatorname{diag}(1,\det(O)O),\qquad
a(OXO^T)=\det(O)\,Oa(X).
\]

Both channel covariance identities passed for a generic one-parameter rotation modulo
\(c^2+s^2=1\), and for a quarter-turn, coordinate cycle, and orientation-reversing axis
reflection generating the signed-permutation/octrahedral action.

For \(L\succeq0\), exact expansion gives the matrix-convex direction

\[
\frac{J_1^\dagger LJ_1+J_2^\dagger LJ_2}{2}
-\left(\frac{J_1+J_2}{2}\right)^\dagger
 L\left(\frac{J_1+J_2}{2}\right)
=\frac14(J_1-J_2)^\dagger L(J_1-J_2)\succeq0.
\]

Thus the defect is matrix concave under averaging. The symbolic identity and three exact
rational PSD instances passed. See
[`twirling_rerun.log`](logs_whgap_p2_20260728/twirling_rerun.log) and
[`twirling_checks.json`](logs_whgap_p2_20260728/twirling_checks.json).
The first Groebner-domain failure remains in
[`twirling.log`](logs_whgap_p2_20260728/twirling.log).

## Commands, runtimes, and provenance

Every Python invocation used `C:<home>/cpython3119/python.exe`.

```powershell
& 'C:<home>/cpython3119/python.exe' 'tools/whgap_p2_exact.py'
& 'C:<home>/cpython3119/python.exe' 'tools/whgap_p2_feasibility.py'
& 'C:<home>/cpython3119/python.exe' 'tools/whgap_p2_twirling.py'
```

Successful-run runtimes:

- exact calibration and symbolic blocks: 44.933428 s;
- exact feasibility, grids, certificates, and direct/block spectra: 8.859314 s;
- twirling ingredients: 0.552347 s.

Total successful compute was under one minute; including retained failed setup runs, it was
well below the 75-minute budget. The symbolic route never approached the 15-minute fallback
threshold.

Scripts:

- [`whgap_p2_exact.py`](../tools/whgap_p2_exact.py)
- [`whgap_p2_feasibility.py`](../tools/whgap_p2_feasibility.py)
- [`whgap_p2_twirling.py`](../tools/whgap_p2_twirling.py)

All raw logs, JSON outputs, and script hashes are covered by
[`SHA256SUMS.txt`](logs_whgap_p2_20260728/SHA256SUMS.txt).

