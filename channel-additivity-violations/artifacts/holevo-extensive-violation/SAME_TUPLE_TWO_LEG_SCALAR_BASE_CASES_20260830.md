# Same-tuple two-leg scalar norm: rigorous base cases

Date: 2026-08-30

Status: proposer-side base-case analysis for the one-layer global `n=2` coefficient problem.  No
canonical YAML is changed.  The general coefficient statement remains **OPEN**.

All logarithms are base two unless `ln` is written explicitly.

## 1. Setup and summary

Let `U_1,...,U_m in U(d)` be one fixed tuple and define

\[
 C^*(X)=\frac1m\sum_{v,w=1}^m X_{v,w}U_v^*U_w.
\tag{1}
\]

For a scalar coefficient matrix `Y in M_(m^2)=M_m tensor M_m`, the same-tuple two-leg map is

\[
 \mathcal M_U(Y):=(C^*\otimes C^*)(Y)
 =\frac1{m^2}\sum_{v,a,w,b}
 Y_{(v,a),(w,b)}
 (U_v^*U_w)\otimes(U_a^*U_b).
\tag{2}
\]

For Hermitian `Y` with `||Y||_2=1`, the desired global two-copy coefficient estimate is

\[
 \|\mathcal M_U(Y)\|_\infty\le\frac{A}{m},
 \qquad A=1+\frac{9(1+\eta)^2}{m}.
\tag{3}
\]

This note proves (3) for the following strict subclasses:

1. every matrix unit, and more generally every coefficient with entrywise `l_1` norm at most
   `Am`;
2. every diagonal coefficient, with exact norm `|Tr Y|/m^2`;
3. every simple tensor `Y=Y_1 tensor Y_2`, using only the successful one-leg scalar coefficient
   event;
4. every coefficient supported on `v=w` on one output leg (or on `a=b`), again using only the
   one-leg event;
5. rank-one coefficients `Y=|z><z|` whose coefficient vector is sparse on at most `Am` positions;
6. rank-one coefficients whose vector `z` has coefficient-Schmidt rank
   `r<=Am/(2+delta)^4`, on the ordinary one-leg strong-convergence event
   `sup_x ||sum x_v U_v||<=(2+delta)||x||_2`;
7. the canonical Bell rank-one coefficient and the normalized flip coefficient, by deterministic
   norm bounds.

For an arbitrary rank-one coefficient, ordinary one-leg convergence plus operator
Cauchy--Schwarz gives the uniform but non-target-tight bound `(2+delta)^2/m`, exposing a residual
constant-factor gap near four.

The following do **not** follow from these base cases:

- a general entangled rank-one vector `z` of full coefficient-Schmidt rank and dense support;
- arbitrary flip-invariant, Bell-invariant, Werner, or isotropic linear combinations;
- a general sum of simple tensors whose projective coefficient norm exceeds one.

These are already genuine repeated-tuple cases.  Ordinary single-leg strong convergence does not
control their cancellations or their two-leg operator norm.

## 2. The one-leg norm available on the successful event

Write

\[
 \beta=\sqrt{A/m}.
\tag{4}
\]

The scalar coefficient event used in the finite absolute-unbounded proof implies

\[
 \boxed{\ \|C^*(X)\|_\infty\le\beta\|X\|_2
 \quad\text{for every complex }X\in M_m.\ }
\tag{5}
\]

For completeness, decompose

\[
 X=\alpha I_m/\sqrt m+X_0,qquad \operatorname{Tr}X_0=0.
\tag{6}
\]

The scalar part maps to `alpha I/sqrt(m)`, while the trace-zero coefficient estimate gives

\[
 \|C^*(X_0)\|_\infty
 \le\sqrt{\frac{A-1}{m}}\|X_0\|_2.
\tag{7}
\]

The triangle inequality followed by Cauchy--Schwarz in the two orthogonal coefficient components
gives (5).  This derivation applies to complex, not only Hermitian, coefficients.

## 3. Matrix units and coefficient sparsity

Let `E_(v,a),(w,b)` be a matrix unit of `M_(m^2)`.  Equation (2) gives the exact spectrum

\[
 \mathcal M_U(E_{(v,a),(w,b)})
 =\frac1{m^2}(U_v^*U_w)\otimes(U_a^*U_b),
\tag{8}
\]

and therefore

\[
 \boxed{\ \|\mathcal M_U(E_{(v,a),(w,b)})\|_\infty=\frac1{m^2}.\ }
\tag{9}
\]

No randomness or asymptotic limit is used.  A Hermitian off-diagonal matrix-unit pair, normalized
as `(E_ij+E_ji)/sqrt(2)` or `i(E_ij-E_ji)/sqrt(2)`, consequently has norm at most
`sqrt(2)/m^2`, also far below (3).

More generally, because every word in (2) is unitary,

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\frac{\|Y\|_{\ell_1(\mathrm{entries})}}{m^2}.
\tag{10}
\]

Thus every unit-Hilbert--Schmidt coefficient satisfying

\[
 \|Y\|_{\ell_1(\mathrm{entries})}\le Am
\tag{11}
\]

obeys (3).  In particular, a unit-Hilbert--Schmidt matrix supported on at most `s` matrix entries
is safe whenever

\[
 s\le A^2m^2,
\tag{12}
\]

because its entrywise `l_1` norm is at most `sqrt(s)`.  This is a sparsity base case only; a dense
coefficient may have `m^4` nonzero entries.

## 4. Diagonal and one-leg-diagonal coefficients

### 4.1 Fully diagonal coefficients

If `Y` is diagonal in the pair basis, every word in (2) is the identity.  Hence

\[
 \boxed{
 \mathcal M_U(Y)=\frac{\operatorname{Tr}Y}{m^2}I_{d^2},
 \qquad
 \|\mathcal M_U(Y)\|_\infty
 =\frac{|\operatorname{Tr}Y|}{m^2}.}
\tag{13}
\]

For `||Y||_2=1`, `|TrY|<=m`, so (13) is at most `1/m<=A/m`.  The normalized identity
`I_(m^2)/m` attains `1/m` exactly.

### 4.2 Diagonal on one channel-copy leg

Suppose

\[
 Y_{(v,a),(w,b)}=0\quad\text{unless }v=w.
\tag{14}
\]

Define `Z in M_m` by

\[
 Z_{a,b}=\sum_{v=1}^mY_{(v,a),(v,b)}.
\tag{15}
\]

Then

\[
 \mathcal M_U(Y)=\frac1m I_d\otimes C^*(Z).
\tag{16}
\]

Cauchy--Schwarz in `v` gives

\[
 \|Z\|_2\le\sqrt m\|Y\|_2.
\tag{17}
\]

Combining (5), (16), and (17), for `||Y||_2=1`,

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\frac{\beta}{\sqrt m}
 =\frac{\sqrt A}{m}
 \le\frac A m.
\tag{18}
\]

The same proof applies when `Y` is supported on `a=b`.  This class is much larger than the fully
diagonal class and still needs no repeated-tuple estimate.

## 5. Simple tensor coefficients

For arbitrary complex `Y_1,Y_2 in M_m`, algebraic factorization is exact:

\[
 \mathcal M_U(Y_1\otimes Y_2)=C^*(Y_1)\otimes C^*(Y_2).
\tag{19}
\]

Consequently (5) gives

\[
 \|\mathcal M_U(Y_1\otimes Y_2)\|_\infty
 \le\frac A m\|Y_1\|_2\|Y_2\|_2
 =\frac A m\|Y_1\otimes Y_2\|_2.
\tag{20}
\]

Thus every normalized simple tensor satisfies (3), including every product rank-one coefficient

\[
 |x\otimes y\rangle\langle x\otimes y|
 =|x\rangle\langle x|\otimes|y\rangle\langle y|.
\tag{21}
\]

For a general operator-Schmidt decomposition

\[
 Y=\sum_s t_sY_{1,s}\otimes Y_{2,s},
 \qquad \|Y_{1,s}\|_2=\|Y_{2,s}\|_2=1,
\tag{22}
\]

the same argument yields only

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\frac A m\sum_s|t_s|.
\tag{23}
\]

It proves (3) when the projective Hilbert--Schmidt coefficient norm is at most one.  For a generic
unit-Hilbert--Schmidt entangled coefficient, `sum|t_s|` can be much larger than one.  Equation (23)
must not be read as a general-`Y` proof.

## 6. Rank-one coefficients

Let `z in C^m tensor C^m` be a unit vector and set `Y=|z><z|`.  Regard `z` as an `m x m` matrix
`Z=(z_(v,a))`.  Define

\[
 T_z=\sum_{v,a}\overline{z_{v,a}}\,U_v\otimes U_a.
\tag{24}
\]

Then (2) factorizes positively:

\[
 \boxed{
 \mathcal M_U(|z\rangle\langle z|)
 =\frac1{m^2}T_z^*T_z,
 \qquad
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 =\frac{\|T_z\|_\infty^2}{m^2}.}
\tag{25}
\]

Thus the rank-one problem is exactly the norm of a scalar linear combination of the dependent
two-leg tuple `(U_v tensor U_a)_(v,a)`.

### 6.1 Sparse rank-one vectors

If `z` has at most `s` nonzero coordinates, then

\[
 \|T_z\|_\infty
 \le\sum_{v,a}|z_{v,a}|\le\sqrt s.
\tag{26}
\]

Therefore

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le\frac s{m^2},
\tag{27}
\]

and (3) holds whenever `s<=Am`.  This recovers matrix-unit rank-one coefficients and will include
the canonical Bell vector below.

### 6.2 Low coefficient-Schmidt rank from ordinary one-leg convergence

Define

\[
 B_U=\sup_{\|x\|_2=1}\left\|\sum_{v=1}^m x_vU_v\right\|_\infty.
\tag{28}
\]

For fixed `m`, ordinary one-leg strong convergence, the length-one free Haagerup bound, and a
finite coefficient net give, for every fixed `delta>0`,

\[
 B_U\le2+\delta
\tag{29}
\]

with probability tending to one as `d->infinity`.

Let the coefficient matrix `Z` have singular-value decomposition

\[
 Z=\sum_{j=1}^r s_jx_jy_j^T,
 \qquad \sum_js_j^2=1.
\tag{30}
\]

Using (28) on both factors,

\[
 \|T_z\|_\infty
 \le B_U^2\sum_js_j
 \le B_U^2\sqrt r.
\tag{31}
\]

Equations (25), (29), and (31) imply the rigorous high-probability base case

\[
 \boxed{
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le\frac{(2+\delta)^4r}{m^2}.}
\tag{32}
\]

Hence (3) holds for every rank-one coefficient vector of coefficient-Schmidt rank

\[
 r\le\frac{Am}{(2+\delta)^4}.
\tag{33}
\]

This conclusion is simultaneous in all such `z`: the only random event is the uniform one-leg
bound (29).  It does not use a net over the rank-`r` two-leg vectors.

For `r=1`, the exact tensor factorization (20) is stronger than (32).  For `r` comparable to `m`,
(32) loses a constant near 16 and no longer reaches the target.  This is the first rank-one point
at which ordinary one-leg strong convergence stops being sufficient.

### 6.3 A constant-factor bound for every rank-one coefficient

There is a better non-target-tight estimate for arbitrary `z`.  Write

\[
 T_z=\sum_v U_v\otimes B_v,
 \qquad
 B_v=\sum_a\overline{z_{v,a}}U_a.
\tag{33a}
\]

The operator Cauchy--Schwarz inequality gives

\[
 T_z^*T_z\preceq
 m I\otimes\sum_vB_v^*B_v.
\tag{33b}
\]

By (28),

\[
 \left\|\sum_vB_v^*B_v\right\|_\infty
 \le\sum_v\|B_v\|_\infty^2
 \le B_U^2\sum_{v,a}|z_{v,a}|^2
 =B_U^2.
\tag{33c}
\]

Hence, on (29), every rank-one coefficient satisfies

\[
 \boxed{
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le\frac{(2+\delta)^2}{m}.}
\tag{33d}
\]

This improves the trivial bound one for dense vectors, but it misses (3) by a constant approaching
four.  Increasing `d` does not remove that constant.  A general rank-one proof therefore needs an
operator-valued orthogonality estimate beyond ordinary one-leg strong convergence and operator
Cauchy--Schwarz.

## 7. Bell and flip coefficients

### 7.1 Canonical Bell rank-one coefficient

Let

\[
 |\Omega_m\rangle=\frac1{\sqrt m}\sum_{v=1}^m|v,v\rangle,
 \qquad Y_\Omega=|\Omega_m\rangle\langle\Omega_m|.
\tag{34}
\]

Although `Omega_m` has coefficient-Schmidt rank `m`, it has only `m` nonzero coordinates.  From
(24),

\[
 T_{\Omega}=\frac1{\sqrt m}\sum_vU_v\otimes U_v,
 \qquad
 \|T_\Omega\|_\infty\le\sqrt m.
\tag{35}
\]

Therefore

\[
 \boxed{
 \|\mathcal M_U(Y_\Omega)\|_\infty\le\frac1m\le\frac A m.}
\tag{36}
\]

This is deterministic.  It does not prove the same statement for
`(I tensor V)|Omega_m>` with a dense unitary `V`, because the tuple distribution is invariant under
permutations and phases of Kraus labels, not under arbitrary unitary mixing of those labels.

### 7.2 Normalized flip coefficient

Let

\[
 F_m=\sum_{v,a}|v,a\rangle\langle a,v|,
 \qquad \|F_m\|_2=m.
\tag{37}
\]

Define the Hermitian contraction

\[
 R_U=\frac1{m^2}\sum_{v,a}
 U_v^*U_a\otimes U_a^*U_v.
\tag{38}
\]

Every summand is unitary, so `||R_U||_infty<=1`.  Direct substitution gives

\[
 \mathcal M_U(F_m/m)=R_U/m,
\tag{39}
\]

and consequently

\[
 \boxed{
 \|\mathcal M_U(F_m/m)\|_\infty\le\frac1m\le\frac A m.}
\tag{40}
\]

Again, no randomness is used.

### 7.3 Symmetry alone is not a base case

The symmetric and antisymmetric projectors

\[
 P_\pm=(I\pm F_m)/2,
 \qquad
 \|P_\pm\|_2=\sqrt{m(m\pm1)/2},
\tag{41}
\]

satisfy

\[
 \mathcal M_U(P_\pm/\|P_\pm\|_2)
 =\frac{I\pm R_U}{2\|P_\pm\|_2}.
\tag{42}
\]

The deterministic estimate `||R_U||<=1` gives only an upper bound asymptotic to `sqrt(2)/m`,
which is larger than `A/m` for the intended large `m`.  Proving the needed cancellation requires
a target-scale upper bound on the repeated-tuple operator `R_U`.  The fact that `F_m/m` and
`I_(m^2)/m` are separately safe does not permit their normalized sum to be bounded by the maximum
of the two norms.

Thus general flip-invariant/Werner coefficients are not settled by (40).  The same warning applies
to arbitrary Bell-invariant or isotropic combinations: canonical Bell sparsity proves (36), not a
whole symmetry sector.

## 8. Where the repeated-tuple obstruction first appears

For a general entangled rank-one coefficient, equation (25) asks for

\[
 \left\|\sum_{v,a}\overline{z_{v,a}}U_v\otimes U_a\right\|_\infty.
\tag{43}
\]

Ordinary strong convergence controls every scalar polynomial `sum_v x_vU_v` on one copy.  It
does not imply strong convergence of (43), because the same tuple is reused in both tensor
factors.  The following operations would be invalid:

1. treating the `m^2` matrices `U_v tensor U_a` as independent Haar unitaries;
2. replacing the second tuple by an independently sampled copy and identifying the resulting norm
   with (43);
3. using (20) after a Schmidt decomposition and dropping the nuclear-norm factor `sum s_j`;
4. extending the sparse canonical Bell estimate to an arbitrary maximally entangled coefficient
   by a nonexistent `U(m)` invariance on Kraus labels.

The low-rank result (33) and sparsity result (27) give two rigorous ways to stay below this gate.
Dense vectors with coefficient-Schmidt rank of order `m`, and symmetry-sector combinations such
as (42), already require new same-tuple information.

## 9. Base-case table

| coefficient `Y`, normalized in Hilbert--Schmidt norm | proved upper bound | input needed | status |
|---|---:|---|---|
| matrix unit | `1/m^2` | none | proved |
| entrywise `l_1(Y)<=Am` | `A/m` | none | proved |
| diagonal | `1/m` | none | proved |
| supported on `v=w` or `a=b` | `sqrt(A)/m` | one-leg event (5) | proved |
| simple tensor `Y_1 tensor Y_2` | `A/m` | one-leg event (5) | proved |
| rank-one, support size `s<=Am` | `s/m^2` | none | proved |
| rank-one, coefficient-Schmidt rank `r<=Am/(2+delta)^4` | `(2+delta)^4r/m^2` | ordinary one-leg strong convergence | proved |
| canonical Bell projector | `1/m` | none | proved |
| normalized flip `F_m/m` | `1/m` | none | proved |
| arbitrary rank-one coefficient | `(2+delta)^2/m` | one-leg event plus Cauchy; constant too large | open at target constant |
| normalized `P_+` or `P_-` | only about `sqrt(2)/m` from triangle inequality | `R_U` spectrum missing | open at target constant |
| arbitrary Hermitian `Y` | no target-tight bound | full same-tuple scalar lemma missing | open |

No row marked proved is used to infer a later open row.

## 10. Minimal next lemmas

1. Improve (31), or the universal bound (33d), for coefficient matrices `Z` with rank near `m` by
   exploiting orthogonality among
   the singular-vector terms, rather than their nuclear norm.  A gain from `sum s_j` to
   `(sum s_j^2)^(1/2)=1` would close every rank-one coefficient, but is itself a same-tuple
   operator-valued Khintchine statement.
2. Prove `||R_U||_infty<=1/m+O(1/sqrt(m))` or the sharper target needed in (42), with high
   probability.  This would settle the normalized symmetric/antisymmetric projectors but not a
   general coefficient.
3. Extend the coefficient class by its projective Hilbert--Schmidt norm: (23) already proves the
   unit ball exactly.  Any enlargement must record the projective-norm loss.
4. Keep the quantifier fixed: these are one-layer, same-tuple, scalar-coefficient `n=2` base cases.
   They imply neither arbitrary `Y` nor any `n>=3` statement.

## Repository interfaces

1. `COMPLEX_HAAR_GLOBAL_N2_CONCENTRATION_GATE_20260830.md`, equations (33)--(37), exact output
   duality and the missing same-tuple lemma.
2. `PRODUCT_HAAR_PHYSICAL_SELF_PURITY_N2_ANALYSIS_20260830.md`, physical Gram versus arbitrary cb
   scope and the exact replica formulation.
3. `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`, one-leg scalar coefficient event and
   compact coefficient net.
4. `UNBOUNDED_GAP_ADVERSARIAL_AUDIT_20260830.md`, quantifier and coefficient-norm audit.
5. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2, ordinary fixed-depth strong convergence used in (29).
