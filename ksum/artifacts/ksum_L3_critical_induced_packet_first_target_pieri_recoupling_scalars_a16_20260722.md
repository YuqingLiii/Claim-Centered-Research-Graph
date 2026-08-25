# Exact first-target deterministic Pieri recoupling scalars at `a=16`

## 1. Scope and verdict

This artifact closes only the finite first-target position-scalar datum requested by equations
(5.3)--(5.6) of
`ksum/artifacts/ksum_L3_critical_induced_packet_one_point_double_pieri_wreath_gram_stack_20260722.md`
(SHA-256
`7EC0E42F84D08E0C8E53DE3AEF82F2C482ACD86722CD6134253EB4C024DDADFF`).
The parameters and shapes are

\[
(s,a,d,r,n)=(4,16,17,4,288),\qquad ad=272,
\]

\[
\theta=(267,4,1),\qquad \lambda=(283,4,1).
\]

All legal NO rare/heavy and YES common/residual/heavy position paths have been enumerated.
Every legal transported coefficient is exactly nonzero and, in the gauge fixed below, positive.
Every unlisted path has exactly zero projector for a shape-containment, horizontal-strip, or
one-box reason.  The resulting heavy coefficients obey an exact square-sum resolution for each
fixed `kappa`.

This is a position-only calculation.  It neither reads nor assembles the occurrence matrices
`O`, the alphabet cross-Grams `C`, or a physical Gram/effect pencil.  It makes no DAG status
change.

## 2. Shapes and complete legal inventory

The removable children are

\[
\begin{array}{c|c|c}
X&\beta_X&\kappa_X\\ \hline
T&(282,4,1)&(266,4,1)\\
M&(283,3,1)&(267,3,1)\\
B&(283,4)&(267,4).
\end{array}
\]

The YES intermediates are

\[
\xi_T=(281,4,1),\qquad
\xi_M=(282,3,1),\qquad
\xi_B=(282,4).
\]

The complete legal inventory is:

* NO rare: `beta_T`;
* YES common: `beta_T`;
* YES residual: `(beta_T,xi_T)`;
* NO heavy:
  `(kappa_T,beta_T)`, `(kappa_M,beta_T)`, `(kappa_M,beta_M)`,
  `(kappa_B,beta_T)`, `(kappa_B,beta_B)`;
* YES heavy:
  `(kappa_T,xi_T,beta_T)`,
  `(kappa_M,xi_T,beta_T)`, `(kappa_M,xi_M,beta_T)`,
  `(kappa_M,xi_M,beta_M)`,
  `(kappa_B,xi_T,beta_T)`, `(kappa_B,xi_B,beta_T)`, and
  `(kappa_B,xi_B,beta_B)`.

## 3. Exact reduced construction and gauge

For fixed `kappa`, all work is done in the multiplicity interval

\[
\mathcal H_\kappa
=\operatorname{Hom}_{S_{271}}
 \bigl(S^\kappa,\operatorname{Res}^{S_{288}}_{S_{271}}S^\lambda\bigr)
\cong S^{\lambda/\kappa}.
\]

Its orthonormal Young-path basis is indexed by saturated chains from `kappa` to `lambda`.
The three interval dimensions are only

\[
\dim\mathcal H_{\kappa_T}=1,qquad
\dim\mathcal H_{\kappa_M}=17,qquad
\dim\mathcal H_{\kappa_B}=17.
\]

Thus the calculation never constructs the dense carriers `S^theta` or `S^lambda`.  On a standard
skew tableau `T`, the exact Young-orthogonal generator uses

\[
\delta_i(T)=c_T(i+1)-c_T(i),
\]

with diagonal entry `1/delta_i` and positive off-diagonal entry
`sqrt(1-delta_i^{-2})` when swapping `i,i+1` remains standard.  The same-row and same-column
cases reduce to `+1` and `-1`.  The implementation checks symmetry, involutivity, every braid
relation, and every far-commutation relation exactly.

For every horizontal strip, the Pieri line is the unique normalized vector fixed by the relevant
symmetric group.  Its phase is fixed by requiring the coefficient of the lexicographically first
saturated tableau to be positive.  This is the positive-leading gauge used for every sign below.

### 3.1 Physical heavy-coordinate transport

The last-letter branch map must first align the actual heavy coordinate with the queried last
coordinate.  In absolute labels the order-preserving move-to-last permutation is

\[
g_{(ad\to n)}(272)=288,qquad
g_{(ad\to n)}(j)=j-1\quad(273\le j\le288).
\]

On the relative labels `1,...,17` of `lambda/kappa`, this is

\[
g(1)=17,\qquad g(j)=j-1\quad(2\le j\le17).
\]

With standard rightmost-factor-first group multiplication,

\[
g=s_{16}s_{15}\cdots s_1;
\]

hence its matrix is evaluated by applying `s_1,s_2,...,s_16` to the source vector.  Equivalently,
in absolute labels the word is `s_287 s_286 ... s_272`, operationally applied from `s_272` up to
`s_287`.  This is not the single transposition `(272,288)`, and it is not the identity.

For fixed `kappa`, let `v_kappa` be the unique source path with label 1 in the box
`theta/kappa` and labels 2 through 17 placed increasingly in the top-row strip `lambda/theta`.
Set

\[
u_\kappa=\rho_{\lambda/\kappa}(g)v_\kappa.
\]

For NO heavy, fix label 17 in `lambda/beta` and take the unique normalized `S_16`-fixed target
vector.  For YES heavy, additionally fix label 16 in `beta/xi` and take the unique normalized
`S_15`-fixed target vector.  The required `p` is exactly the inner product of this target vector
with `u_kappa`.  The rare, common, and residual intervals are one-dimensional all-top paths.

This realizes (5.3) and (5.5) in `End(S^theta)`.  Equations (5.4) and (5.6) lie in
`Hom(S^theta,S^kappa)`; multiplicity one forces each left-hand side to be the displayed scalar
times the same normalized branch map `b_(theta->kappa)`.  Consequently these inner products have
exactly the types asserted in (5.3)--(5.6), rather than being merely dimension ratios.

## 4. Exact scalars

The scalar `p` below does not include a status probability.

### 4.1 Rare, common, and residual

\[
\begin{array}{c|c|c|c}
\text{status/path}&p&p^2&\text{sign}\\ \hline
\text{NO rare }\beta_T&1&1&+\\
\text{YES common }\beta_T&1&1&+\\
\text{YES residual }(\beta_T,\xi_T)&1&1&+
\end{array}
\]

### 4.2 NO heavy

\[
\begin{array}{c|c|c|c|c}
\kappa&\beta&p&p^2&\text{sign}\\ \hline
\kappa_T&\beta_T&1&1&+\\
\kappa_M&\beta_T&\sqrt{2/9275}&2/9275&+\\
\kappa_M&\beta_M&\sqrt{9273/9275}&9273/9275&+\\
\kappa_B&\beta_T&\sqrt{4/19099}&4/19099&+\\
\kappa_B&\beta_B&\sqrt{19095/19099}&19095/19099&+
\end{array}
\]

### 4.3 YES heavy

\[
\begin{array}{c|c|c|c|c|c}
\kappa&\xi&\beta&p&p^2&\text{sign}\\ \hline
\kappa_T&\xi_T&\beta_T&1&1&+\\
\kappa_M&\xi_T&\beta_T&\sqrt{1/4929}&1/4929&+\\
\kappa_M&\xi_M&\beta_T&\sqrt{11/862575}&11/862575&+\\
\kappa_M&\xi_M&\beta_M&\sqrt{9273/9275}&9273/9275&+\\
\kappa_B&\xi_T&\beta_T&\sqrt{15/76127}&15/76127&+\\
\kappa_B&\xi_B&\beta_T&\sqrt{67/5405017}&67/5405017&+\\
\kappa_B&\xi_B&\beta_B&\sqrt{19095/19099}&19095/19099&+
\end{array}
\]

All entries in these three tables are exactly nonzero.  In particular, none of the candidate
paths retained in the planning artifact disappears after the physical coordinate alignment.

## 5. Exact zero inventory

For NO heavy, the following grid is exhaustive; an empty entry is exactly zero:

\[
\begin{array}{c|ccc}
&\beta_T&\beta_M&\beta_B\\ \hline
\kappa_T&\ne0&0&0\\
\kappa_M&\ne0&\ne0&0\\
\kappa_B&\ne0&0&\ne0
\end{array}
\]

For YES heavy, each entry gives the complete set of nonzero intermediates; `emptyset` means that
all three `xi_T,xi_M,xi_B` choices have exactly zero projector:

\[
\begin{array}{c|ccc}
&\beta_T&\beta_M&\beta_B\\ \hline
\kappa_T&\{\xi_T\}&\varnothing&\varnothing\\
\kappa_M&\{\xi_T,\xi_M\}&\{\xi_M\}&\varnothing\\
\kappa_B&\{\xi_T,\xi_B\}&\varnothing&\{\xi_B\}
\end{array}
\]

These zeros occur before taking an inner product: the corresponding path space is absent because
`beta` does not contain `kappa`, `xi` does not contain `kappa`, `xi/kappa` is not the required
horizontal strip, or `beta/xi` is not one box.  The JSON log records the reason for every one of
the 4 unlisted NO pairs and 20 unlisted YES triples.  NO rare, YES common, and YES residual have
only the unique paths listed in Section 4.1; all other children/intermediates are zero by the same
shape tests.

## 6. Resolution and normalization proof

For each fixed heavy child, orthogonality of the last-letter and intermediate branches gives a
resolution of the relevant `S_16`- or `S_15`-fixed subspace.  Since `u_kappa` is normalized and
the target Pieri lines are normalized, the computed coefficients obey

\[
\sum_\beta (p^{0,H}_{\beta,\kappa})^2=1,
\qquad
\sum_{\beta,\xi}(p^{1,H}_{\beta,\kappa,\xi})^2=1.
\]

Explicitly, the nontrivial identities are

\[
\frac2{9275}+\frac{9273}{9275}=1,
\qquad
\frac4{19099}+\frac{19095}{19099}=1,
\]

\[
\frac1{4929}+\frac{11}{862575}+\frac{9273}{9275}=1,
\]

\[
\frac{15}{76127}+\frac{67}{5405017}+\frac{19095}{19099}=1.
\]

The `kappa_T` identities are `1=1`.  Combining these with the ordinary one-box branching
resolution

\[
\sum_\kappa b_{\theta\to\kappa}^{*}b_{\theta\to\kappa}=I_{S^\theta}
\]

and keeping raw status masses separate gives

\[
\text{NO}:\quad \frac1{18}+\frac{17}{18}=1,
\]

\[
\text{YES}:\quad
\frac1{288}+\frac{15}{288}+\frac{17}{18}
=\frac1{18}+\frac{17}{18}=1.
\]

Thus both position resolutions are normalized exactly.

## 7. Why the literal no-transport reading is rejected

As a convention diagnostic, the same projectors were applied directly to `v_kappa`, with the
move-to-last transporter omitted.  The complete result is

\[
\begin{array}{c|c|c|c}
\text{case}&\kappa&\text{nonzero coefficient(s)}&\sum p^2\\ \hline
\text{NO}&\kappa_T&1&1\\
\text{NO}&\kappa_M&p_{\beta_T}=\sqrt{7/106},\ p_{\beta_M}=0&7/106\\
\text{NO}&\kappa_B&p_{\beta_T}=\sqrt{71/1076},\ p_{\beta_B}=0&71/1076\\
\text{YES}&\kappa_T&p_{\xi_T,\beta_T}=1&1\\
\text{YES}&\kappa_M&p_{\xi_T,\beta_T}=\sqrt{93/1325},\ \text{other two}=0&93/1325\\
\text{YES}&\kappa_B&p_{\xi_T,\beta_T}=\sqrt{283/4035},\ \text{other two}=0&283/4035
\end{array}
\]

For `kappa_M` and `kappa_B`, these sums are strictly below one and the unique `beta_M` or
`beta_B` channel vanishes.  Hence the identity/no-transport interpretation fails the status
resolution and cannot represent the physical last-coordinate branch.  This diagnostic also
distinguishes the order-preserving move-to-last convention from a silent rephasing.

## 8. Separation from occurrence, alphabet, and status data

The four kinds of factors remain distinct:

* `p` is the position-only Pieri recoupling scalar computed here;
* `w` is the raw status probability in Section 6 and is not absorbed into `p`;
* `O` is an occurrence multiplicity Gram matrix and was not read or assembled;
* `C` is an alphabet point-child cross-Gram and was not read or assembled.

Consequently this artifact is sufficient to replace the missing first-target values in
(5.3)--(5.6), but it does not authorize assembling (6.9)--(6.11) with unreviewed `O` or `C` data.
It proves no commutator, Sylvester, query-attenuation, coefficient-norm, adversary, or asymptotic
claim.

## 9. Reproduction and finite exclusions

Exact tool:
`ksum/tools/ksum_l3_first_target_pieri_scalars.py` (pre-archive SHA-256
`11019D7CE0D289A76260D1EB0724059698611AD1A4C7D2E7F82DB7CB07F88048`).

Archived machine-readable result:
`ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_a16_20260722.json`.

Commands:

```text
python ksum/tools/ksum_l3_first_target_pieri_scalars.py
python ksum/tools/ksum_l3_first_target_pieri_scalars.py --verify-log ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_a16_20260722.json
```

The verification command returns `ARCHIVED_PIERI_RESULT_VERIFIED`.  The exact run checks all
Coxeter relations, one-dimensional Pieri fixed spaces, unit norm, unitary transport, the complete
legal/nonlegal inventory, every nonzero assertion, and all square-sum and status resolutions.

Finite-scope exclusions are: no all-`s` formula; no asymptotic inference; no occurrence or
alphabet table; no assembled Gram/effect/pencil or commutator; no pullback or nonproduct
full-type truncation conclusion; no query attenuation, coefficient norm, numerator, lower bound,
or exponent; and no DAG status change.
