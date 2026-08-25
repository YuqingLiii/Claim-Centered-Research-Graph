# L3 critical endpoint: exact query cut for the second balanced parent grid

Date: 2026-07-22  
Canonical scope (not edited by this memo):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.noncommuting-parent-mixing-kernel`  
Verdict: **every parent of the second grid below the first-row parent has a unique
first-row-removal marked type; that type contains a heavy-unselected Pieri branch on which the
physical off-equality mask retains a constant fraction.  Consequently the natural balanced
coefficient table fails both the left and right query bounds, without any 6j calculation.**  
Status discipline: scoped proposer-tier closure of this candidate only; no canonical-node edit,
no completion-tier claim, and no claim about other parent or multiplicity families

## 1. Frozen candidate and notation

Use the exact `p=0,u=1` subsequence and the second grid of the frozen construction:

\[
 a=k^2,\qquad q=4a,\qquad d=k,\qquad m=d+1,\qquad n=am,
\tag{1.1}
\]

\[
 r=\lfloor m^{1/3}\rfloor,\qquad
 \ell=r-1,\qquad
 T={\ell(\ell-1)\over2},\qquad
 \alpha=(a-T,\ell-1,\ell-2,\ldots,1),
\tag{1.2}
\]

\[
 L=ad+\ell-1,\qquad
 \lambda^-=(L,\alpha_1-1,\alpha_2-1,\ldots,\alpha_\ell-1)
 \vdash n-1.
\tag{1.3}
\]

Let

\[
 \lambda_i=\lambda^-+\square_i,\qquad 0\le i<r,
\tag{1.4}
\]

where the addable corners are ordered from the first row downward, and put
`mu_j=lambda_j`.  Thus `lambda_0` is the first-row parent, while every `lambda_i` with
`1<=i<r` has first part exactly `L`.  The selected full-group types are

\[
 \rho_{ij}=(\lambda_i,\mu_j,\nu),
\tag{1.5}
\]

with the fixed alphabet partition `nu` of the frozen construction.  Their chosen multiplicity
lines occur in both exact answer modules.

The natural coefficient table is

\[
 b_{ij}=\begin{cases}
 1,&i=j,\\[2mm]
 -1/(r-1),&i\ne j.
 \end{cases}
\tag{1.6}
\]

Its unmarked Fourier multiplier has norm one.

## 2. Every lower parent has a unique predecessor

For `1<=i<r`, remove the first-row corner and define

\[
 \beta_i=\lambda_i-\square_{\rm first}\vdash n-1.
\tag{2.1}
\]

This is a legal partition: its first part is `L-1`, still strictly larger than every lower part.
The consecutive staircase rows in `lambda^-` may make two lower parts equal after a lower box is
added, but they cannot produce a collision at (2.1).

Indeed, suppose a supported parent `lambda_h` restricts to `beta_i` after one corner is removed.

* If `h=0`, its first part is `L+1`; a one-box removal leaves first part at least `L`, whereas
  `beta_i` has first part `L-1`.
* If `h>=1`, its first part is `L`.  Removing any non-first-row corner leaves that first part
  equal to `L`.  Hence a predecessor equal to `beta_i` must also remove the first-row corner.
  Equality then gives `lambda_h=lambda_i`, and therefore `h=i`.

Thus

\[
 \boxed{
 \beta_i\nearrow\lambda_h
 \text{ for a supported parent }\lambda_h
 \quad\Longrightarrow\quad h=i
 }
 \qquad(1\le i<r).
\tag{2.2}
\]

For a fixed right parent `mu_j`, the left marked type

\[
 (\beta_i,\mu_j,\nu)
\tag{2.3}
\]

therefore receives no coefficient from another row of the grid.  The right-side statement is
identical: for fixed `lambda_i`, the type `(lambda_i,beta_j,nu)` receives no coefficient from
another column.  This first-part argument is insensitive to all consecutive lower-row gaps, so
no 6j matrix is involved.

## 3. The predecessor is a heavy-unselected branch

The skew diagram `lambda_i/alpha` is a horizontal strip of size `ad`.  Its removed first-row box
lies outside `alpha`; deleting it preserves the horizontal-strip property.  Hence

\[
 \beta_i/\alpha\text{ is horizontal of size }ad-1,
 \qquad
 c^{\beta_i}_{\alpha,(ad-1)}=1.
\tag{3.1}
\]

This is precisely the Pieri branch in which the queried position lies in the heavy complement
and the singleton carrier `alpha` is unchanged.  Denote this marked status by `U`.

Write

\[
 t_i=(\lambda_i)_2
 =\begin{cases}
 a-T,&i=1,\\
 a-T-1,&2\le i<r.
 \end{cases}
\tag{3.2}
\]

The first-row hook ratio, valid whether or not lower parts repeat, gives

\[
 {f^{\beta_i}\over f^{\lambda_i}}
 ={1\over n}
 \prod_{c=1}^{L-1}
 {h_{\lambda_i}(1,c)\over h_{\beta_i}(1,c)}
 \ge {L-t_i\over n}.
\tag{3.3}
\]

For columns beyond `t_i` the product telescopes to `L-t_i`; every omitted factor is larger than
one.

Let `p_i` be the squared `U` overlap of this marked branch on either selected answer copy.  Since
exactly `a` of the `n` positions are singleton positions,

\[
 {1\over n}\sum_{x=1}^nP_U(x)={n-a\over n}I.
\tag{3.4}
\]

Taking the trace after the multiplicity-free Young restriction of `S^{lambda_i}`, and bounding
every branch other than `beta_i` by one, yields

\[
 p_i
 \ge 1-{a\over n}{f^{\lambda_i}\over f^{\beta_i}}
 \ge 1-{a\over L-t_i}.
\tag{3.5}
\]

Both the NO and YES selected copies obey the same bound, so their rectangular `U/U` compression
retains at least the product of the two overlap amplitudes, namely the right-hand side of (3.5).

Uniformly over all lower parents, set

\[
 D_*=L-(a-T)=a(d-1)+T+\ell-1.
\tag{3.6}
\]

Then

\[
 p_i\ge1-{a\over D_*}\ge1-{1\over d-1}.
\tag{3.7}
\]

Thus the `U` branch is norm-retaining, not diluted by the `r` lower corners.

## 4. Exact physical off-equality lower bounds

Conditioned on the singleton skeleton and on status `U`, the marked heavy value is uniform on the
unused raw-label complement.  Those complements have sizes `2a` on NO and `2a+1` on YES.

The applicability to the selected lines is exact: their construction uses the trivial heavy
position and heavy alphabet carriers, so they lie in the normalized singleton-skeleton pullback
on which conditional heavy-completion averaging acts.

The equality multiplier therefore has rectangular Schur norm at most

\[
 \delta_a={1\over\sqrt{2a(2a+1)}}.
\tag{4.1}
\]

Consequently the physical off-equality mask retains at least `1-delta_a` of every `U/U`
compression.  Combining uniqueness (2.2), (3.5), and (4.1), any scalar grid coefficient obeys
the left query bound

\[
 \boxed{
 \|\Gamma(B)\circ\Delta_x^L\|
 \ge
 (1-\delta_a)
 \left(1-{a\over L-t_i}\right)|b_{ij}|
 }
 \qquad(1\le i<r),
\tag{4.2}
\]

for every physical left coordinate `x`.  Symmetrically,

\[
 \boxed{
 \|\Gamma(B)\circ\Delta_y^R\|
 \ge
 (1-\delta_a)
 \left(1-{a\over L-t_j}\right)|b_{ij}|
 }
 \qquad(1\le j<r),
\tag{4.3}
\]

for every physical right coordinate `y`.

The common uniform lower factor is

\[
 c_{a,d,\ell}
 :=(1-\delta_a)\left(1-{a\over D_*}\right)
 \ge
 \left(1-{1\over\sqrt{2a(2a+1)}}\right)
 \left(1-{1\over d-1}\right),
\tag{4.4}
\]

which tends to one along the exact subsequence.  These bounds use an isolated marked type, not
the common `lambda^-` marked type whose parent-basis recoupling contains the unresolved 6j
matrix.

## 5. The natural balanced table is ruled out

For every lower index `h` with `1<=h<r`, the diagonal coefficient in (1.6) is

\[
 b_{hh}=1.
\tag{5.1}
\]

Apply (4.2) and (4.3) to the single Fourier block `(h,h)`.  Since the unmarked norm of the natural
multiplier is one,

\[
 \boxed{
 {\|\Gamma_{\rm grid}\circ\Delta_x^L\|
  \over\|\Gamma_{\rm grid}\|}
 \ge c_{a,d,\ell},
 \qquad
 {\|\Gamma_{\rm grid}\circ\Delta_y^R\|
  \over\|\Gamma_{\rm grid}\|}
 \ge c_{a,d,\ell}.
 }
\tag{5.2}
\]

Therefore the natural balanced table does not have an `O(r^{-1/2})` query norm on either side;
its normalized query norms instead tend to one.  Row and column sums cancel only the shared
restriction branch and cannot cancel the isolated types (2.3).  The second balanced-grid
candidate is thus a scoped **FAIL** at the physical query gate, with no 6j computation required.

## 6. Gate and noncoverage ledger

| Obligation | Outcome |
|---|---|
| every lower parent has a first-row-removal predecessor | PASS, (2.1) |
| collision caused by consecutive lower rows | none; first-part separation proves uniqueness, (2.2) |
| predecessor is a legal heavy-unselected branch | PASS by Pieri, (3.1) |
| first-row hook ratio | at least `(L-t_i)/n`, (3.3) |
| `U` overlap | at least `1-a/(L-t_i)`, (3.5) |
| physical off-equality retention | at least `1-delta_a`, (4.1) |
| exact left/right query cuts | (4.2)--(4.4) |
| natural balanced `B` | **SCOPED FAIL**, (5.2) |
| 6j evaluation | unnecessary for this cut |
| other coefficient laws or parent families | not audited |
| outer `a^(2/3)` numerator and incidence composition | not audited |
| completion-tier claim or canonical status change | none |

Frozen inputs:

* `ksum/artifacts/ksum_L3_critical_noncommuting_parent_mixing_construct_20260722.md`, SHA-256
  `A48883B3E33B3FFF6BAAB8B4E8EC1F0473B4D5EE39C0FF24F411C507F7CB8A43`;
* `ksum/artifacts/ksum_L3_critical_noncommuting_parent_mixing_audit_20260722.md`, corrected SHA-256
  `66A6A60F0D5FCF095BE30078E1309E1B1694E0840098E96423A187F840632DE2`.

This memo adds only the candidate-specific query closure above.  It does not edit or reinterpret
the canonical proof DAG.
