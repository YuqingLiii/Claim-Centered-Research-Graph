# Same-tuple rank-one coefficients: Gram contraction and sharp dense subclasses

Date: 2026-08-30

Status: proposer-side exact/conditional lemmas and route obstructions.  No canonical YAML is
changed.  The general same-tuple two-leg scalar strong-norm node remains **OPEN**.

This note continues
[SAME_TUPLE_TWO_LEG_SCALAR_BASE_CASES_20260830.md](SAME_TUPLE_TWO_LEG_SCALAR_BASE_CASES_20260830.md).
It addresses the first unresolved rank-one class there: dense coefficient matrices of high or
full coefficient-Schmidt rank.  No browser, external comparison theorem, or large computation is
used.

## 1. Setup

Let `U_1,...,U_m` be an arbitrary unitary tuple, let `z` be a unit vector in
`C^m tensor C^m`, and identify `z` with the matrix `Z=(z_(v,a))`, so

\[
 \|Z\|_F^2=1.
\tag{1}
\]

As in the base-case note, define

\[
 T_Z=\sum_{v,a}\overline{z_{v,a}}\,U_v\otimes U_a,
 \qquad
 \mathcal M_U(|z\rangle\langle z|)=m^{-2}T_Z^*T_Z.
\tag{2}
\]

The one-leg coefficient map is

\[
 C^*(X)={1\over m}\sum_{a,b}X_{a,b}U_a^*U_b.
\tag{3}
\]

The target is

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty\le {A\over m},
 \qquad
 A=1+{9(1+\eta)^2\over m}.
\tag{4}
\]

## 2. Exact rank-one Gram contraction lemma

Define the two coefficient Gram matrices

\[
 G_R:=\overline{Z^*Z}=Z^T\overline Z,
 \qquad
 G_L:=ZZ^*.
\tag{5}
\]

Both are positive semidefinite and have trace one.  Then, for every deterministic unitary tuple,

\[
 \boxed{
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le \min\{\|C^*(G_R)\|_\infty,\|C^*(G_L)\|_\infty\}.}
\tag{6}
\]

### Proof using the right Gram

Write

\[
 T_Z=\sum_v U_v\otimes B_v,
 \qquad
 B_v=\sum_a\overline{z_{v,a}}U_a.
\tag{7}
\]

Matrix Cauchy--Schwarz gives

\[
 T_Z^*T_Z
 \preceq m\sum_v(I\otimes B_v^*B_v).
\tag{8}
\]

The square function is not estimated term by term.  It has the exact one-leg coefficient form

\[
 \begin{aligned}
 \sum_vB_v^*B_v
 &=\sum_{a,b}\left(\sum_v z_{v,a}\overline{z_{v,b}}\right)U_a^*U_b\\
 &=mC^*(\overline{Z^*Z})=mC^*(G_R).
 \end{aligned}
\tag{9}
\]

Divide (8) by `m^2`, use (2), and take norms to obtain the first bound in (6).

### Proof using the left Gram

Instead write

\[
 T_Z=\sum_a C_a\otimes U_a,
 \qquad C_a=\sum_v\overline{z_{v,a}}U_v.
\tag{10}
\]

The same argument gives

\[
 \sum_aC_a^*C_a=mC^*(ZZ^*)=mC^*(G_L),
\tag{11}
\]

and hence the second bound in (6).

The conjugation in `G_R` is load-bearing: the coefficient of `U_a^*U_b` in (9) is
`sum_v z_(v,a) overline(z_(v,b))`.  It may be omitted in norm-only Frobenius corollaries, but not
from the exact identity.

## 3. Deterministic dense, full-rank base cases

### 3.1 Orthogonal columns or rows

If `Z^*Z` is diagonal, then `G_R` is the same diagonal matrix and

\[
 C^*(G_R)={\operatorname{Tr}G_R\over m}I={1\over m}I.
\tag{12}
\]

Equation (6) gives the deterministic target-sharp estimate

\[
 \boxed{
 Z^*Z\text{ diagonal}\quad\Longrightarrow\quad
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty\le {1\over m}.}
\tag{13}
\]

The same conclusion holds when `ZZ^*` is diagonal.  This class is not a sparsity restatement.  For
example, let

\[
 Z=WD,
\tag{14}
\]

where `W` is any dense unitary and `D` is any diagonal matrix with `||D||_F=1`.  Then `Z` is dense,
may have coefficient-Schmidt rank exactly `m`, and may have arbitrarily non-flat nonzero singular
values, yet `Z^*Z=D^*D` is diagonal and (13) holds for every unitary tuple.  Likewise `Z=DW` is
safe by the row-Gram version.

### 3.2 Every maximally entangled coefficient vector

Every maximally entangled coefficient vector has

\[
 Z={1\over\sqrt m}V
\tag{15}
\]

for a unitary `V`.  Both Grams in (5) equal `I/m`, so

\[
 \boxed{
 Z=V/\sqrt m\quad\Longrightarrow\quad
 \|T_Z\|_\infty\le\sqrt m,
 \qquad
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty\le {1\over m}.}
\tag{16}
\]

This is deterministic and covers dense `V`.  It does not use a nonexistent `U(m)` invariance of
the Haar tuple under arbitrary Kraus-label mixing.  The earlier warning that canonical-Bell
sparsity cannot be transported by such an invariance remains correct; (16) is a new proof based
on exact column/row orthogonality.

## 4. Near-orthogonal Gram subclasses

For a matrix `G`, let

\[
 \operatorname{Off}(G)=G-\operatorname{diag}(G).
\tag{17}
\]

Since `Tr G_R=Tr G_L=1` and every `U_a^*U_a=I`,

\[
 C^*(G)={1\over m}I+C^*(\operatorname{Off}(G))
\tag{18}
\]

for either Gram.

### 4.1 Deterministic entrywise condition

Every off-diagonal word in (18) is unitary, so

\[
 \|C^*(G)\|_\infty
 \le {1+\|\operatorname{Off}(G)\|_{\ell_1(\mathrm{entries})}\over m}.
\tag{19}
\]

Consequently

\[
 \boxed{
 \min_{\sigma\in\{L,R\}}
 \|\operatorname{Off}(G_\sigma)\|_{\ell_1}
 \le A-1
 \quad\Longrightarrow\quad (4).}
\tag{20}
\]

No randomness is used.

### 4.2 Conditional Frobenius condition

On the uniform one-leg trace-zero event from the base-case note,

\[
 \|C^*(X_0)\|_\infty
 \le \alpha\|X_0\|_F,
 \qquad
 \alpha:=\sqrt{{A-1\over m}},
 \qquad \operatorname{Tr}X_0=0,
\tag{21}
\]

equations (6) and (18) imply

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le {1\over m}
 +\alpha\min_{\sigma\in\{L,R\}}
 \|\operatorname{Off}(G_\sigma)\|_F.
\tag{22}
\]

Thus the target follows simultaneously for every `z` satisfying

\[
 \boxed{
 \min_{\sigma\in\{L,R\}}
 \|\operatorname{Off}(G_\sigma)\|_F
 \le\sqrt{{A-1\over m}}
 ={3(1+\eta)\over m}.}
\tag{23}
\]

The quantifier is important: no net over `z` is needed, because (21) is already uniform over all
one-leg coefficient matrices.

### 4.3 Relation to singular-value flatness

The weaker full-Gram use of the one-leg event gives

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le \sqrt{{A\over m}}\,\|Z^*Z\|_F
 =\sqrt{{A\over m}}\left(\sum_js_j^4\right)^{1/2}.
\tag{24}
\]

This proves the target when the effective coefficient-Schmidt rank

\[
 r_{\rm eff}:={1\over\sum_js_j^4}
\tag{25}
\]

satisfies `r_eff>=m/A`.  Condition (23) is stronger in orientation-sensitive cases because it
discards arbitrary diagonal variation exactly: diagonal Grams are safe even when their effective
rank is small.

Together with the previous low-Schmidt-rank estimate, one now has the rigorous union

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le \min\left\{
 {B_U^4\operatorname{rank}(Z)\over m^2},
 {1\over m}+\alpha\min_\sigma\|\operatorname{Off}(G_\sigma)\|_F
 \right\}.
\tag{26}
\]

The first term controls sufficiently low rank; the second controls full-rank matrices whose left
or right singular basis is Kraus-coordinate-aligned or whose singular values are sufficiently
flat.

## 5. Precise limitation of the Gram-contraction route

Coefficient-Schmidt rank `m` alone does not make (23) small.  Let `V` be a dense complex Hadamard
unitary, choose positive numbers `p_j` with `sum p_j=1`, and set

\[
 Z=V\operatorname{diag}(\sqrt{p_1},\ldots,\sqrt{p_m})V^*.
\tag{27}
\]

Then `Z` is dense and full rank, and both Grams equal

\[
 G=V\operatorname{diag}(p_1,\ldots,p_m)V^*.
\tag{28}
\]

The Hadamard property makes every diagonal entry of `G` equal `1/m`, hence

\[
 \|\operatorname{Off}(G)\|_F^2
 =\sum_jp_j^2-{1\over m}.
\tag{29}
\]

For example, take `p_1=1/2` and `p_2=...=p_m=1/(2(m-1))`.  The coefficient matrix remains dense
and full rank, while the right-hand side of (29) tends to `1/4`, far above the `O(m^(-2))` square
threshold in (23).  Bound (22) is then only `1/m+Theta(m^(-1))` with the inherited constants and
does not reach (4).

This is an obstruction to **this one-leg Gram-contraction proof**, not a counterexample to the
same-tuple target.  A general dense full-rank proof must exploit cancellations inside
`C^*(G_L)` or `C^*(G_R)` beyond the uniform Hilbert--Schmidt coefficient event, or avoid the factor
`m` in matrix Cauchy--Schwarz.

## 6. Why standard decoupling does not close the remaining case

### 6.1 Phase symmetrization is still same-tuple

Haar invariance permits replacing `U_v` by `epsilon_v U_v`, where the `epsilon_v` are independent
Steinhaus phases (or signs).  Distributionally this gives the coupled chaos

\[
 \sum_{v,a}\overline{z_{v,a}}\epsilon_v\epsilon_a U_v\otimes U_a.
\tag{30}
\]

A standard decoupling step would replace the second phase by an independent `delta_a`.  But

\[
 \sum_{v,a}\overline{z_{v,a}}\epsilon_v\delta_a U_v\otimes U_a
\tag{31}
\]

still uses the same underlying matrices `U_i` on both legs.  The pairs
`(epsilon_i U_i,delta_i U_i)` are scalar multiples of one another, not independent Haar matrices.
Thus phase decoupling does not invoke the known independent-leg strong-convergence theorem.

For Rademacher signs, diagonal terms `v=a` are unchanged because `epsilon_v^2=1`; standard
tetrahedral-chaos decoupling must first split them off.  Steinhaus phases randomize the diagonal
but do not remove the shared matrix.

### 6.2 A constant-factor comparison is not target-sharp

Suppose a decoupling or Gaussian comparison supplied only

\[
 \mathbb E\|T_Z(U,U)\|\le C\,\mathbb E\|T_Z(U,V)\|
\tag{32}
\]

with a universal `C>1` and an independent tuple `V`.  As written, this first-moment comparison is
already insufficient to transfer the desired high-probability norm statement: it cannot be
directly squared through (2).  Even granting the stronger transferable pointwise or tail
comparison `||T_Z(U,U)||<=C||T_Z(U,V)||`, the sharp independent-leg target `sqrt(A m)` would yield
only `C sqrt(A m)` and hence `C^2A/m` after (2), not `A/m`.  The available slack
`A-1=O(1/m)` cannot absorb a fixed decoupling constant.  Standard chaos decoupling is therefore
useful only if refined to an asymptotic constant `1+O(1/m)` together with strong-tail control;
ordinary expectation-only or fixed-constant comparisons do not close this gate.

### 6.3 Noncommutative Khintchine and Gaussian replacement

Iterated noncommutative Khintchine applied after (30) produces row/column square functions.  The
right square function is exactly (9), so the sharp information it would need is already the
one-leg norm of `C^*(G_R)`.  Generic operator-norm Khintchine additionally pays a dimension- or
moment-dependent constant; iterating the ordinary one-leg bound recovers the previous constant
near four or the Gram bounds above, not the target for (27).

Replacing Haar unitaries by Gaussian matrices does not fix the quantifier.  Same-sample quadratic
Gaussian chaos also needs decoupling, has additional diagonal Wick contractions, and comparison
through polar decomposition is not a norm-preserving constant-one operation.  No standard
Gaussian comparison identified here transfers the required sharp strong norm.

These observations do not rule out a specialized asymptotically exact decoupling theorem.  They
only delimit what the usual constant-factor tools actually prove.

## 7. Flip/representation decomposition: exact identities but no general gain

Let `S` be the flip on `C^d tensor C^d`.  Directly,

\[
 ST_ZS=T_{Z^T}.
\tag{33}
\]

Hence symmetric `Z` gives an operator commuting with `S` and splits into symmetric/antisymmetric
physical blocks; antisymmetric `Z` gives an operator anticommuting with `S` and exchanges the two
blocks.  This is an exact representation decomposition.

It does not by itself lower the norm of either block.  Decomposing a general coefficient as
`Z=(Z+Z^T)/2+(Z-Z^T)/2` and using the triangle inequality can lose a factor up to `sqrt(2)` before
squaring, already too large for the target.  Thus flip symmetry is a useful organization of
special coefficients, not a decoupling of the reused Haar tuple.

## 8. Suggested atomic nodes (not registered here)

### 8.1 `HEXT.same-tuple-rank-one-gram-contraction`

Suggested role: `proof`.

Suggested claim:

> For every deterministic unitary tuple and unit coefficient vector `z` with matrix `Z`, the
> same-tuple rank-one output obeys
> `||M_U(|z><z|)|| <= min(||C^*(overline(Z^*Z))||,||C^*(ZZ^*)||)`.  Consequently the sharp
> deterministic bound `1/m` holds whenever either coefficient Gram is diagonal, including all
> dense maximally entangled coefficient vectors `Z=V/sqrt(m)`.

This is a route-free direct algebraic node supported by equations (6)--(16).

### 8.2 `HEXT.same-tuple-near-orthogonal-gram-base-case`

Suggested role: `proof`.

Suggested claim:

> On the uniform one-leg trace-zero coefficient event
> `||C^*(X_0)|| <= sqrt((A-1)/m)||X_0||_2`, every rank-one coefficient satisfies the two-leg target
> if either its left or conjugated-right Gram has off-diagonal Frobenius norm at most
> `sqrt((A-1)/m)=3(1+eta)/m`.  Deterministically, off-diagonal entrywise `l_1` norm at most `A-1`
> is also sufficient.

This conditional node should list the existing one-leg coefficient event as a premise or exact
model input according to its canonical ownership.  It must not be stated for arbitrary high-rank
coefficients.

### 8.3 `HEXT.same-tuple-standard-decoupling-obstruction`

Suggested role: `obstruction`.

Suggested claim:

> Phase decoupling of the order-two coefficient chaos leaves the same underlying Haar matrices on
> both tensor legs, while a comparison with any fixed multiplicative constant greater than one
> cannot transfer the target-sharp `A/m` bound.  This refutes only the unrefined standard
> phase/constant-factor decoupling route, not the same-tuple claim or an asymptotically exact
> specialized comparison.

Equations (30)--(32) give the required scope and prevent over-propagation.

## 9. Status boundary

The exact Gram contraction adds a genuinely dense full coefficient-Schmidt-rank subclass and a
uniform near-orthogonal-Gram neighborhood to the earlier base cases.  It does not prove strong
convergence for a generic fixed `Z`, does not handle arbitrary Hermitian `Y`, and does not identify
the same-tuple free-model norm.  In particular, the dense non-flat family (27) remains outside the
new sufficient conditions.  The canonical same-tuple strong-norm node must remain OPEN.
