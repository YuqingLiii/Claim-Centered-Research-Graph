# Product-Haar physical self-purity: the two-copy problem

Date: 2026-08-30

Status: independent proposer-side reduction for `n=2` only.  No canonical YAML is changed.
The all-copy node `HEXT.product-haar-physical-self-purity-multiplicativity` remains **OPEN**.

All logarithms are base two.

## Executive result

Let `L=L_J` be one fixed finite successful product-random-unitary block, let `C=L^c`, put
`q=m^J`, and write its `q` unitary Kraus words as `W_v`, `v in [q]`.  Set

\[
 A=A_{J,\eta}=1+(1+\eta)^2\big((1+9/m)^J-1\big),
 \qquad p=A/q.
\tag{1}
\]

The node's two-copy assertion is

\[
 \sup_{\rho\in\mathcal D((\mathbb C^{D^J})^{\otimes2})}
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]\le p^2.
\tag{2}
\]

This note does not prove (2) for a generic complex product-Haar realization and does not find a
generic complex-Haar counterexample.  It gives the following exact reductions and boundary
results.

1. The optimization has exact Kraus-Gram, quadratic-superoperator, and separability-conic forms.
   It is not an ordinary finite SDP; an exact lift requires the separable cone on two replicas.
2. Equation (2) holds for **every input separable across the two channel copies**.  Therefore any
   counterexample must be a pure entangled input.
3. After separating the depolarizing part of `C`, all one-body terms are already controlled by the
   one-copy estimate.  The exact missing condition is one state-dependent two-body correlation
   inequality for the centered map `E=C-Tr(.)I_q/q`.
4. A convenient stronger sufficient inequality is

   \[
      \|(E\otimes E)(\rho)\|_2^2
      \le \frac{(A-1)^2}{q^2}.
   \tag{3}
   \]

   It holds for separable `rho`, but it is not logically necessary for (2); entanglement can move
   purity from marginal terms into the correlation term.
5. There is a strict physical `n=2` obstruction for every simultaneously real/orthogonal tuple.
   If all `W_v` are real orthogonal, a maximally entangled input gives

   \[
      \operatorname{Tr}[C^{\otimes2}(\Omega)^2]
      \ge \frac{2}{q^2}-\frac1{q^3}.
   \tag{4}
   \]

   Hence (2) fails whenever `A^2<2-1/q`.  For `J=1`, `eta=0`, this holds for every `m>=23`, in
   particular throughout `ln m>18`.  This excludes real/orthogonal or simultaneously-real
   orientations, but not a generic complex Haar tuple.

The smallest unresolved inequality for a complex tuple is equation (29) below.  It involves only
physical two-copy density matrices; arbitrary cb coefficient matrices do not appear.

## 1. Channel and one-copy normalization

Write `H=C^(D^J)` for the input Hilbert space and

\[
 L(X)=\frac1q\sum_{v=1}^q W_vXW_v^*,
\tag{5}
\]

where every `W_v` is unitary.  A complementary channel is

\[
 C(X)_{v,w}=\frac1q\operatorname{Tr}(XW_w^*W_v).
\tag{6}
\]

For every operator `X`, all diagonal entries equal `Tr(X)/q`.  Define

\[
 D_0(X)=\operatorname{Tr}(X)\frac{I_q}{q},
 \qquad E=C-D_0.
\tag{7}
\]

Then every `E(X)` has zero diagonal, hence zero trace, and the two ranges in (7) are orthogonal in
Hilbert--Schmidt inner product.  For a state `tau`,

\[
 \operatorname{Tr}[C(\tau)^2]=\frac1q+\|E(\tau)\|_2^2.
\tag{8}
\]

The successful one-copy coefficient estimate used in the absolute-unbounded proof gives

\[
 \|E(\tau)\|_2^2\le \frac{A-1}{q}
 \quad\text{for every state }\tau,
\tag{9}
\]

and therefore `sup_tau Tr[C(tau)^2]<=A/q=p`.

The underlying adjoint estimate is slightly stronger.  If `Y` has zero diagonal, then

\[
 E^*(Y)=\frac1q\sum_{v\ne w}Y_{v,w}W_v^*W_w,
 \qquad
 \|E^*(Y)\|_\infty\le\kappa\|Y\|_2,
\tag{10}
\]

with

\[
 \kappa^2=\frac{A-1}{q}.
\tag{11}
\]

Duality consequently gives

\[
 \|E(X)\|_2\le\kappa\|X\|_1
\tag{12}
\]

for arbitrary trace-class `X`, not only states.  Equation (12) is a scalar induced norm.  Its
tensor-square amplification is exactly where entangled physical inputs can differ from arbitrary
coefficient or product inputs.

There is also an exact complementary-channel reformulation.  Write

\[
 \mu_2(\Phi)=\sup_{\rho\in\mathcal D}\operatorname{Tr}[\Phi(\rho)^2].
\tag{12a}
\]

Output purity is convex, so its maximum is attained on a pure input.  On every pure input a
channel and its complement have the same nonzero output spectrum.  Applying this once to `L,C`
and once to `L tensor L,C tensor C` gives

\[
 \mu_2(C)=\mu_2(L),\qquad
 \mu_2(C\otimes C)=\mu_2(L\otimes L).
\tag{12b}
\]

Thus a theorem proving self-multiplicativity
`mu_2(L tensor L)=mu_2(L)^2` for this random-unitary class would imply (2), because the one-copy
event gives `mu_2(L)=mu_2(C)<=p`.  The standard complementary-channel equivalence itself supplies
only (12b); it does **not** supply the missing multiplicativity theorem.

## 2. Exact Kraus/Gram expression

For the two-copy channel, label its Kraus words by pairs `i=(v,a)` and put

\[
 K_{v,a}=W_v\otimes W_a.
\tag{13}
\]

For any input state `rho`, define the `q^2 x q^2` correlation matrix

\[
 G_\rho[(v,a),(w,b)]
 =\operatorname{Tr}\!\left[\rho
   (W_w^*W_v\otimes W_b^*W_a)\right].
\tag{14}
\]

Then

\[
 C^{\otimes2}(\rho)=\frac1{q^2}G_\rho,
\tag{15}
\]

up to the harmless transpose convention for complementary-channel indices, and

\[
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]
 =\frac1{q^4}\sum_{v,a,w,b}
  \left|\operatorname{Tr}\!\left[\rho
  (W_w^*W_v\otimes W_b^*W_a)\right]\right|^2
 =\frac{\|G_\rho\|_2^2}{q^4}.
\tag{16}
\]

This is a physical Gram matrix:

\[
 G_\rho[i,j]
 =\langle K_j\sqrt\rho,K_i\sqrt\rho\rangle_{\rm HS}.
\tag{17}
\]

Consequently

\[
 G_\rho\succeq0,\qquad G_\rho[i,i]=1,
\tag{18}
\]

and all its entries arise from one common density matrix and one common unitary orbit.  Conditions
(17)--(18) are much narrower than an arbitrary matrix-valued coefficient ball.  In particular the
cb-distortion witness in `FINITE_UNITARY_CB_DISTORTION_OBSTRUCTION_20260829.md` is not itself a
physical scalar Gram matrix of the form (17).

In these variables, (2) is exactly

\[
 \boxed{\ \|G_\rho\|_2^2\le A^2q^2
 \quad\text{for every physical }G_\rho.\ }
\tag{19}
\]

The diagonal of `G_rho` already contributes `q^2`; equation (19) permits at most
`(A^2-1)q^2` total off-diagonal squared correlation.

## 3. Quadratic-superoperator expression

Let

\[
 \mathcal T=C^*C:M_{D^J}\longrightarrow M_{D^J}.
\tag{20}
\]

This map is completely positive and positive semidefinite as a Hilbert--Schmidt superoperator.
For every two-copy input state,

\[
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]
 =\operatorname{Tr}\!\left[\rho
   (\mathcal T\otimes\mathcal T)(\rho)\right].
\tag{21}
\]

Equivalently, introduce a second replica of the two-copy input space and define

\[
 Q=\frac1{q^4}\sum_{i,j}
  K_j^*K_i\otimes K_i^*K_j.
\tag{22}
\]

Then

\[
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]
 =\operatorname{Tr}[Q(\rho\otimes\rho)].
\tag{23}
\]

The objective is convex in `rho`, because it is the squared Hilbert--Schmidt norm of a linear
channel output.  Its maximum over density matrices is therefore attained on a pure state.

Let `h=D^(2J)` be the dimension of the two-copy input and let `P_sym` project onto the symmetric
subspace of `C^h tensor C^h` across the two replicas.  The optimization has the exact conic form

\[
 \begin{aligned}
  \text{maximize }&\operatorname{Tr}(QX)\\
  \text{subject to }&\operatorname{Tr}X=1,\quad X\succeq0,\\
  &X=P_{\rm sym}XP_{\rm sym},\\
  &X\text{ separable across the replica cut.}
 \end{aligned}
\tag{24}
\]

Indeed, a product vector in the symmetric subspace has identical factors, so the feasible cone is
the convex hull of `|psi><psi| tensor |psi><psi|`.  This is exact, but it is a separability-cone
program rather than an ordinary SDP.  Replacing separability by PPT, or by finite symmetric
extensions, gives certified SDP upper bounds; no finite level is known to be exact in these large
dimensions.

## 4. Exact centered two-copy decomposition

Let `rho_1` and `rho_2` be the input marginals.  Expanding
`C tensor C=(D_0+E) tensor (D_0+E)` gives

\[
 \begin{aligned}
 (C\otimes C)(\rho)
  ={}&\frac{I_q}{q}\otimes\frac{I_q}{q}
  +\frac{I_q}{q}\otimes E(\rho_2)
  +E(\rho_1)\otimes\frac{I_q}{q}\\
  &+(E\otimes E)(\rho).
 \end{aligned}
\tag{25}
\]

All four terms are pairwise Hilbert--Schmidt orthogonal.  The last term has zero partial trace on
either output leg.  Therefore

\[
 \boxed{
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]
 =\frac1{q^2}
 +\frac1q\|E(\rho_1)\|_2^2
 +\frac1q\|E(\rho_2)\|_2^2
 +\|(E\otimes E)(\rho)\|_2^2.}
\tag{26}
\]

Put `a=A-1`.  By (9), both one-body terms in (26) are at most `a/q^2`.  Thus the simple uniform
two-body estimate

\[
 \|(E\otimes E)(\rho)\|_2^2\le\frac{a^2}{q^2}
\tag{27}
\]

is sufficient for (2).

It is not necessary.  The **exact smallest missing inequality**, equivalent state by state to
(2), is

\[
 \boxed{
 \|(E\otimes E)(\rho)\|_2^2
 \le \frac{A^2-1}{q^2}
 -\frac1q\left(\|E(\rho_1)\|_2^2+\|E(\rho_2)\|_2^2\right).}
\tag{28}
\]

Since `A^2-1=2a+a^2`, the one-copy estimates ensure that the right side of (28) is at least
`a^2/q^2`.  Inequality (27) is therefore a clean stronger target, while (28) is the precise
boundary if marginal slack is to be used.

For the product-Haar words, the unresolved scalar assertion is consequently

\[
 \boxed{\text{Prove (28) for every entangled pure }\rho=|\psi\rangle\langle\psi|,
 \text{ or find one physical }|\psi\rangle\text{ that violates it.}}
\tag{29}
\]

No arbitrary matrix-level coefficient estimate is required by (29).

## 5. What is already proved at `n=2`

### 5.1 All separable inputs satisfy the target

Let

\[
 \rho=\sum_s p_s\tau_s\otimes\omega_s
\tag{30}
\]

be separable across the two channel copies.  The squared Hilbert--Schmidt norm is convex, so

\[
 \begin{aligned}
 \operatorname{Tr}[C^{\otimes2}(\rho)^2]
 &\le\sum_sp_s
 \operatorname{Tr}[C(\tau_s)^2]\operatorname{Tr}[C(\omega_s)^2]\\
 &\le p^2.
 \end{aligned}
\tag{31}
\]

This proves (2) on the entire separable input set.  In centered form, (12) also gives

\[
 \|(E\otimes E)(\rho)\|_2
 \le\sum_sp_s\|E(\tau_s)\|_2\|E(\omega_s)\|_2
 \le\kappa^2,
\tag{32}
\]

which is (27).  Hence any violation of (2) must use entanglement across the two repeated uses.

### 5.2 Cross-norm control for bounded entanglement

For an arbitrary bipartite operator, the projective trace norm and (12) give

\[
 \|(E\otimes E)(X)\|_2
 \le\kappa^2\|X\|_{S_1\widehat\otimes_\pi S_1}.
\tag{33}
\]

For a pure state with Schmidt coefficients `sqrt(lambda_r)`,

\[
 \||\psi\rangle\langle\psi|\|_{S_1\widehat\otimes_\pi S_1}
 =\left(\sum_r\sqrt{\lambda_r}\right)^2.
\tag{34}
\]

Thus a Schmidt-rank-`s` input obeys the coarse estimate

\[
 \|(E\otimes E)(\psi)\|_2^2\le\kappa^4s^2.
\tag{35}
\]

For every `s>1` this is too weak to imply (27); it nevertheless records exactly how much
amplification can enter through an operator-Schmidt decomposition.  Equation (35) is a
physical-state bound; it is not a cb norm assertion.

### 5.3 The stronger centered inequality is not logically automatic

The one-copy estimate alone cannot imply (27).  As an elementary model, take the identity qubit
channel and center it by the completely depolarizing channel.  A pure one-qubit input has centered
squared norm `1/2`, but a Bell input has centered two-body squared norm `3/4`, rather than
`(1/2)^2`.  The full output-purity target is nevertheless saturated because the Bell marginals
are maximally mixed and (28) allocates their unused marginal budget to the correlation term.

This example is not a product-Haar counterexample.  It shows why (28), rather than the stronger
(27), is the genuinely minimal missing inequality.

## 6. A strict physical obstruction: simultaneously real tuples

Assume first that all `W_v` are real orthogonal.  Apply `L tensor L` to the normalized maximally
entangled input `Omega` on `H tensor H`.  For every equal Kraus label,

\[
 (W_v\otimes W_v)|\Omega\rangle=|\Omega\rangle.
\tag{36}
\]

There are `q` such labels among the `q^2` equally weighted Kraus pairs.  Hence the output has the
positive decomposition

\[
 (L\otimes L)(\Omega)=\frac1q|\Omega\rangle\langle\Omega|+R,
 \qquad R\succeq0,
\tag{37}
\]

where

\[
 \operatorname{Tr}R=1-1/q,\qquad\operatorname{rank}R\le q^2-q.
\tag{38}
\]

Using `Tr(R^2)>=(Tr R)^2/rank(R)` and dropping the nonnegative cross term gives

\[
 \begin{aligned}
 \operatorname{Tr}[(L\otimes L)(\Omega)^2]
 &\ge\frac1{q^2}+\frac{(1-1/q)^2}{q^2-q}\\
 &=\frac2{q^2}-\frac1{q^3}.
 \end{aligned}
\tag{39}
\]

On a pure input, `L tensor L` and its complementary channel `C tensor C` have the same nonzero
output spectrum.  This proves (4).

Comparison with the target `A^2/q^2` shows strict failure whenever

\[
 A^2<2-1/q.
\tag{40}
\]

For `J=1`, `eta=0`, `q=m` and `A=1+9/m`; condition (40) becomes

\[
 m^2-19m-81>0,
\tag{41}
\]

which holds for every integer `m>=23`.  For sufficiently small positive `eta`, it continues to
hold with a strict margin.  The same argument applies after a common input/output orientation that
makes all words real up to phases; the phases disappear from the pure Kraus outputs.

This is a genuine physical density-matrix violation at `n=2`, but only for the simultaneously-real
subclass.  Complex Haar tuples are almost surely not simultaneously real, so (39)--(41) do **not**
refute the existential complex product-Haar node.  They do rule out replacing the complex ensemble
by Haar orthogonal matrices or imposing a common real orientation.

## 7. The maximally entangled test for a general complex tuple

For a general complex tuple, define

\[
 |\phi_{v,a}\rangle=(W_v\otimes W_a)|\Omega\rangle.
\tag{42}
\]

Complementarity and the pure-state ensemble give the exact computable test

\[
 \operatorname{Tr}[C^{\otimes2}(\Omega)^2]
 =\frac1{q^4}\sum_{v,a,w,b}
 \left|\frac1{D^J}\operatorname{Tr}\!\left[
   (W_vW_a^T)^*(W_wW_b^T)\right]\right|^2.
\tag{43}
\]

Thus the Bell input violates (2) exactly when the frame potential in (43) exceeds `A^2q^2`.
For a real tuple the `q` equal-label frame vectors coincide, recovering the collision in Section 6.
For generic complex product-Haar words, those equal-label vectors are not invariant and no
comparable deterministic collision follows.  (The words are dependent as `v` varies because they
reuse the per-leg generators.)  Equation (43) is a small-memory, finite certificate for testing a
specified tuple, but testing one input cannot prove the global inequality (2).

## 8. Relation to the free model and fixed-depth convergence

Collins--Youn Theorem 3.4 proves in the infinite free/commuting model, for every copy number `k`,

\[
 \sup_S\left\|(\Phi_m^c)^{\otimes k}(S)-I/m^k\right\|_2^2
 \le \frac{(1+9/m)^k-1}{m^k}.
\tag{44}
\]

Consequently its purity bound is exactly

\[
 \sup_S\operatorname{Tr}[(\Phi_m^c)^{\otimes k}(S)^2]
 \le\left(\frac{1+9/m}{m}\right)^k.
\tag{45}
\]

At `k=2J`, this is the `eta=0` analogue of (2) for the free model.  Therefore the numerical
constant is not the issue.

The finite construction spatializes a prescribed `J`-leg free product by using independent Haar
tuples on those `J` legs.  In `L_J tensor L_J`, the second outer copy reuses the same `J` tuples.
Bordenave--Collins Theorem 9.2 instead supplies the direct-product free limit when the tuples on
all tensor legs are independently sampled.  It does not state that the repeated representation

\[
 (g,h)\longmapsto\rho_D(g)\otimes\rho_D(h)
\tag{46}
\]

formed from one common finite representation has the required uniform physical-output bound.
For fixed `n=2`, proving only (28) is a much smaller target than proving strong convergence of the
entire repeated coefficient algebra, but it is still an additional theorem.

This note makes no inference from `n=2` to arbitrary `n`.  Even a proof of (2) would establish only
the first nontrivial repeated-tuple case; the all-copy node would remain open.

## 9. Minimal next actions

1. For a specified successful complex tuple, evaluate the Bell frame potential (43).  A violation
   is a rigorous physical counterexample to `n=2`; passing it is only one-input evidence.
2. Attempt (28) through the exact conic program (24), using PPT/DPS levels only as upper bounds and
   keeping the relaxation gap explicit.
3. Prove a same-tuple, two-leg estimate only on the physical Gram cone (17), rather than on all
   `M_{q^2}` coefficients.  The required constant is exactly `A^2q^2` in (19).
4. Do not use real/orthogonal tuples: Section 6 gives an exact Bell collision against them.
5. If (2) is proved, register it as an `n=2` lemma only.  A separate argument is still needed for
   every `n>=3` and for uniform all-copy control.

## Primary sources and repository interfaces

1. Benoit Collins and Sang-Gyun Youn, *Additivity Violation of the Regularized Minimum Output
   Entropy*, arXiv:1907.07856v2, Theorems 3.3--3.5, local PDF pp. 11--14:
   `holevo-extensive-violation/artifacts/primary-sources/collins-youn-1907.07856.pdf`.
2. Charles Bordenave and Benoit Collins, *Norm of matrix-valued polynomials in random unitaries
   and permutations*, arXiv:2304.05714v2, Theorem 9.2.
3. Christopher King, Keiji Matsumoto, Michael Nathanson, and Mary Beth Ruskai, *Properties of
   Conjugate Channels with Applications to Additivity and Multiplicativity*, arXiv:quant-ph/0509126.
4. `FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`, especially Steps 1--2.
5. `FINITE_UNITARY_CB_DISTORTION_OBSTRUCTION_20260829.md`, especially its scope limit.
6. `FULL_SIZE_SELF_LEAKAGE_PARALLEL_ANALYSIS_20260830.md`, Sections 6--7.
