# L3 critical endpoint: noncommuting parent-mixing construction audit

Date: 2026-07-22
Canonical scope (not edited by this memo):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.noncommuting-parent-mixing-kernel`
Verdict: **the growing-parent representation gate passes, but only on an `r x r` parent grid;
the literal same-`r`-parents-on-both-sides mechanism is impossible.  A formula-defined balanced
grid is given below, but no `O(r^(-1/2))` bound for its physical off-equality Schur masks follows
from parent balance, and the outer/incidence gate is not closed.  The node remains OPEN.**
Status discipline: proposer-tier symbolic audit only; no completion status and no numerical
exponent inference

## 1. Bottom-line decision

There are two separate questions in the proposed parent-mixing mechanism.

1. Can a one-coordinate stabilizer type contain
   `r=Theta(m^(1/3))` distinct full-`G` parents in both exact answer modules?
2. Can parent-diagonal full-`G` Fourier coefficients have unit unmarked norm while every physical
   off-equality marked block has norm `O(r^(-1/2))` on both physical sides?

The first question has a positive, fully explicit answer on the legal `p=0,u=1` subsequence.
However, the same `r>1` parents cannot mix under both `H_L` and `H_R`.  The product-group labels
force a two-dimensional grid: left queries mix the `lambda` index down each fixed-`mu` column, and
right queries mix the `mu` index across each fixed-`lambda` row.  Section 3 proves this exact
typing obstruction, and Section 4 constructs an `r x r` grid present in both `M_0` and `M_1`.

The natural simultaneous balancing law is

\[
 b_{ij}=\begin{cases}
 1,&i=j,\\
 -1/(r-1),&i\ne j.
 \end{cases}
\tag{1.1}
\]

Every row and column sums to zero, and the resulting full-`G` Fourier multiplier has norm one.
This is a genuine nonseparable parent law, not a product `x_i y_j` and not a passive copy of one
two-parent diamond.

The second question is not settled by (1.1).  Restriction to `H_L` or `H_R` is parent diagonal,
but a physical query is the Schur map

\[
 T\longmapsto T-\sum_{z\in[q]}E_{1,z}TE_{0,z},
\tag{1.2}
\]

not restriction and not subtraction of a row or column mean.  Its matrix on the grid contains
Pieri/Littlewood--Richardson recoupling coefficients involving the common alphabet carrier.
Neither the zero row/column sums nor the number of parents determines those coefficients.  The
required `O(r^(-1/2))` estimate therefore remains an explicit unproved Wigner/one-point-orbital
inequality.  In fact, the exact hook weights of the selected singleton carrier are highly
nonuniform: the first-row corner has weight `1-O(r^2/a)`, while all other corners together have
weight `O(r^2/a)`.  The unweighted double-centering in (1.1) kills the uniform vector, not this
hook measure; in the naive parent/origin identification the residual is `1-O(1/r)`.  In the
actual typed system a Pieri 6j change of basis intervenes, so even that cancellation test is an
explicit uncomputed matrix functional.  Hook-weighted centering can kill one computed functional
but does not control its orthogonal complement; small total hook weight is not by itself an
operator-norm bound on normalized marked branches.  Moreover, the rank-one channels constructed
here do not yet carry the separate outer `a^(2/3)` numerator through normalized address
incidence.

Thus this memo supplies a real growing parent system and a formula-defined candidate, while also
pinning down the exact reason it is not yet an adversary construction.  It must not be credited
with the missing `m^(1/6)` factor.

The status of the natural law (1.1) is deliberately split:

* **scoped FAIL** for the proposed inference "zero parent row/column sums imply
  `sqrt(r)` physical-query cancellation";
* **UNRESOLVED** as an actual full off-equality orbital law, because the selected-corner 6j
  matrices and their equality/off-equality refinement have not been computed;
* **no gain credited** in either case.

## 2. Exact subsequence and multiplicity-space types

Use the infinite exact critical subsequence

\[
 a=k^2,\qquad q=4a,\qquad d=k,\qquad m=d+1,
 \qquad n=a(d+1)=am,
\tag{2.1}
\]

so `p=0` and `u=1`.  The exact symmetry group and answer modules are

\[
 G=S_n^{(L)}\times S_n^{(R)}\times S_q,
 \qquad
 V_t=\mathbb C[X_t]\cong\operatorname{Ind}_{K_t}^{G}{\bf1}.
\tag{2.2}
\]

For

\[
 \rho=(\lambda,\mu,\nu),\qquad
 \lambda,\mu\vdash n,\quad \nu\vdash q,
\tag{2.3}
\]

write the full, exact multiplicity space as

\[
 M_t(\lambda,\mu,\nu)
 =\left(S^\lambda\boxtimes S^\mu\boxtimes S^\nu\right)^{K_t}.
\tag{2.4}
\]

No total dimension for (2.4) is assumed below.  Instead, explicit multiplicity-one Pieri/LR
chains will define selected lines

\[
 L_{t,ij}\subseteq M_t(\lambda_i,\mu_j,\nu),
 \qquad \dim L_{t,ij}=1.
\tag{2.5}
\]

This distinction matters: a chosen one-dimensional channel inside the exact fixed space is not a
claim that the whole fixed space has dimension one.

For a fixed left coordinate,

\[
 H_L=S_{n-1}^{(L)}\times S_n^{(R)}\times S_q,
\tag{2.6}
\]

and an `H_L` type is

\[
 \tau_L=(\lambda^-,\mu,\nu),\qquad \lambda^-\vdash n-1.
\tag{2.7}
\]

Its marked multiplicity space is exactly

\[
 N_t^L(\tau_L)
 \cong
 \bigoplus_{\lambda:\lambda^-\nearrow\lambda}
 M_t(\lambda,\mu,\nu).
\tag{2.8}
\]

For a right coordinate,

\[
 N_t^R(\lambda,\mu^-,\nu)
 \cong
 \bigoplus_{\mu:\mu^-\nearrow\mu}
 M_t(\lambda,\mu,\nu).
\tag{2.9}
\]

Equations (2.8)--(2.9) are restriction statements.  The physical query Schur mask is introduced
separately in Section 6.

## 3. Exact obstruction: one parent star cannot serve both sides

Suppose distinct full-`G` irreducibles `rho_s=(lambda_s,mu_s,nu_s)` all occur as parents of one
fixed `H_L` type `tau_L=(lambda^-,mu,nu)`.  By the product-group branching rule,

\[
 \mu_s=\mu,\qquad \nu_s=\nu,
 \qquad \lambda^-\nearrow\lambda_s.
\tag{3.1}
\]

If the same irreducibles are also all parents of one fixed `H_R` type
`tau_R=(lambda,mu^-,nu)`, then

\[
 \lambda_s=\lambda,\qquad \nu_s=\nu,
 \qquad \mu^-\nearrow\mu_s.
\tag{3.2}
\]

Combining (3.1) and (3.2) makes every triple identical:

\[
 \rho_s=(\lambda,\mu,\nu).
\tag{3.3}
\]

Hence a common parent set for a single left type and a single right type has cardinality at most
one.  This is a type-level obstruction, independent of all coefficient choices and all orbit
normalizations.

To give every coefficient a growing left and right mixing neighborhood, the minimum natural
repair is a bipartite parent support

\[
 \rho_{ij}=(\lambda_i,\mu_j,\nu),
 \qquad 0\le i,j<r.
\tag{3.4}
\]

For fixed `j`, the `r` triples in column `j` share an `H_L` type.  For fixed `i`, the `r` triples
in row `i` share an `H_R` type.  More generally, if every nonzero parent coefficient is required
to have at least `r` partners in both its left and right restriction fiber, its support graph has
minimum degree at least `r` on both sides and therefore has at least `r^2` edges.  Parent count is
not a free one-dimensional selector.

## 4. An explicit `r x r` common-parent grid

Put

\[
 r=\lfloor m^{1/3}\rfloor,
 \qquad \ell=r-1,
 \qquad T={\ell(\ell-1)\over2},
\tag{4.1}
\]

and, for all sufficiently large members of (2.1), define the strict partition

\[
 \alpha=(a-T,\ell-1,\ell-2,\ldots,2,1)\vdash a.
\tag{4.2}
\]

It has `ell` parts and `ell` removable corners.  Define

\[
 L= n-a+\ell-1=ad+\ell-1
\tag{4.3}
\]

and

\[
 \lambda^-=(L,\alpha_1-1,\alpha_2-1,\ldots,\alpha_\ell-1)
 \vdash n-1,
\tag{4.4}
\]

where a trailing zero is omitted.  Because the positive parts in (4.4) are strictly decreasing,
`lambda^-` has exactly `ell+1=r` addable corners.  Let

\[
 \lambda_i=\lambda^-+\square_i,
 \qquad 0\le i<r,
\tag{4.5}
\]

be the `r` parents, ordered from the first-row addable box downward.  Set `mu_j=lambda_j`.

The interlacing inequalities

\[
 (\lambda_i)_s\ge\alpha_s\ge(\lambda_i)_{s+1}
 \qquad(s\ge1)
\tag{4.6}
\]

hold for every `i`.  Therefore every skew shape `lambda_i/alpha` is a horizontal strip of size
`ad`, and Pieri gives the exact coefficient

\[
 c^{\lambda_i}_{\alpha,(ad)}=1.
\tag{4.7}
\]

The same holds for every `mu_j`.

For the alphabet carrier, put

\[
 \nu=(2a+2\alpha_1,2\alpha_2,2\alpha_3,\ldots)\vdash4a=q.
\tag{4.8}
\]

The Cartan and Pieri chains

\[
 c^{2\alpha}_{\alpha,\alpha}=1,
 \qquad
 c^{(2a)}_{(a),(a)}=1,
 \qquad
 c^\nu_{2\alpha,(2a)}=1
\tag{4.9}
\]

give a formula-defined nonzero restriction channel

\[
 S^\nu\downarrow
 S_a^{(L_1)}\times S_a^{(R_1)}
 \times S_a^{(L_d)}\times S_a^{(R_d)}
 \supset
 S^\alpha\boxtimes S^\alpha\boxtimes{\bf1}\boxtimes{\bf1}.
\tag{4.10}
\]

Combine (4.7) on the two position sides with (4.10).  The two singleton `S_a` actions in `K_0`
act diagonally on equal real Specht carriers and have their normalized coevaluation invariant.
The heavy position carrier is invariant under the full `S_(ad)` and hence under
`S_d wr S_a`; the heavy alphabet carriers are trivial.  This constructs a selected line

\[
 L_{0,ij}\subseteq
 M_0(\lambda_i,\mu_j,\nu)
\tag{4.11}
\]

for every `(i,j)`.

For `K_1`, choose one fixed removable corner of `alpha`, for example the first-row corner, and
write

\[
 \bar\alpha=\alpha-\square_{\rm first}.
\tag{4.12}
\]

Branch each singleton carrier through
`S^alpha downarrow S_(a-1) superset S^baralpha`.  Equivalently, associativity of LR induction and
the displayed chain give the explicit nonvanishing coefficient

\[
 c^\nu_{\bar\alpha,\bar\alpha,(1),(1),(a),(a)}\ge1.
\tag{4.13}
\]

On the position sides, the remaining singleton is the distinguished common value; on the
alphabet side the two singleton factors in (4.13) are assigned to the unique common and unique
unused labels.  All singleton groups have order one, so no additional representation is being
identified.  The same coevaluation construction gives

\[
 L_{1,ij}\subseteq
 M_1(\lambda_i,\mu_j,\nu)
\tag{4.14}
\]

for every `(i,j)`.  Thus

\[
 \boxed{
 \dim M_t(\lambda_i,\mu_j,\nu)\ge1
 \quad(t=0,1;\ 0\le i,j<r).
 }
\tag{4.15}
\]

This proves the requested growing-parent *existence* without a regular-module ancilla.  The
selected lines are fixed by the displayed multiplicity-one chains; other channels in the full
spaces (2.4) are left untouched.

## 5. Formula-defined balanced parent-diagonal multiplier

Choose unit vectors

\[
 \kappa_{t,ij}\in L_{t,ij}.
\tag{5.1}
\]

The Young orthogonal basis, the top Cartan components in (4.9), and the fixed first-row branch in
(4.12) make this choice formula-defined up to phases; fix the phases by requiring the first
nonzero Young-basis coordinate to be positive.

Let `U_t` be the exact unitary Fourier decomposition

\[
 U_t:V_t\longrightarrow
 \bigoplus_\rho S^\rho\otimes M_t(\rho).
\tag{5.2}
\]

For the grid irreducible `rho_ij=(lambda_i,mu_j,nu)`, define

\[
 B_{ij}=b_{ij}
 |\kappa_{1,ij}\rangle\langle\kappa_{0,ij}|:
 M_0(\rho_{ij})\longrightarrow M_1(\rho_{ij}),
\tag{5.3}
\]

with `b_ij` from (1.1), and put every other Fourier block equal to zero.  The full operator is

\[
 \Gamma_{\rm grid}
 =U_1^*\left[
   \bigoplus_{i,j} I_{S^{\rho_{ij}}}\otimes B_{ij}
  \right]U_0:
 V_0\longrightarrow V_1.
\tag{5.4}
\]

Equation (5.4) is a `G`-intertwiner and hence has a unique expansion in the exact rectangular
orbital basis.  It is formula-defined through finite Young matrix coefficients and subgroup
averages; no optimizer is used.  Its norm is exactly

\[
 \|\Gamma_{\rm grid}\|
 =\max_{i,j}\|B_{ij}\|=1.
\tag{5.5}
\]

For every column and row,

\[
 \sum_i b_{ij}=0,
 \qquad
 \sum_j b_{ij}=0.
\tag{5.6}
\]

For fixed `j`, the left marked type

\[
 \tau_j^L=(\lambda^-,\mu_j,\nu)
\tag{5.7}
\]

contains all `r` parents `rho_ij`.  On the selected parent sum, *unmasked restriction* of
`Gamma_grid` is

\[
 D_j^L=\operatorname{diag}_{i}(b_{ij}):\mathbb C^r\to\mathbb C^r.
\tag{5.8}
\]

Likewise, for fixed `i`,

\[
 \tau_i^R=(\lambda_i,\lambda^-,\nu),
 \qquad
 D_i^R=\operatorname{diag}_{j}(b_{ij}).
\tag{5.9}
\]

This is the exact sense in which (1.1) is simultaneously parent-balanced.  It says nothing yet
about a physical query norm.

## 6. Restriction is not the query Schur mask

Fix a left coordinate.  For `z in [q]`, define the value-fiber projections

\[
 E^L_{t,z}:V_t\to V_t,
 \qquad
 (E^L_{t,z}f)(x)={\bf1}[x_L(i)=z]f(x).
\tag{6.1}
\]

They are orthogonal projections of dimensions

\[
 \dim E^L_{t,z}V_t=|X_t|/q,
\tag{6.2}
\]

because simultaneous alphabet relabeling is transitive.  For any rectangular operator
`T:V_0->V_1`, equality pinching and the physical unequal-value query are exactly

\[
 \Phi_L(T)=\sum_{z=1}^{q}E^L_{1,z}TE^L_{0,z},
 \qquad
 T\circ\Delta_i^L=T-\Phi_L(T).
\tag{6.3}
\]

Equivalently, the isometries

\[
 \mathcal D_{t,L}:V_t\longrightarrow V_t\otimes\mathbb C^q,
 \qquad
 \mathcal D_{t,L}|x\rangle=|x\rangle\otimes|x_L(i)\rangle
\tag{6.4}
\]

give the typed Stinespring formula

\[
 \Phi_L(T)=\mathcal D_{1,L}^*(T\otimes I_q)\mathcal D_{0,L}.
\tag{6.5}
\]

The maps in (6.4) are `H_L`-intertwiners when `C^q` carries the natural alphabet permutation
representation.  Splitting

\[
 \mathbb C^q={\bf1}\oplus S^{(q-1,1)}
\tag{6.6}
\]

shows explicitly that

\[
 \Phi_L(T)={1\over q}T
 +\mathcal D_{1,L}^{\circ *}
   (T\otimes I_{S^{(q-1,1)}})
  \mathcal D_{0,L}^{\circ}.
\tag{6.7}
\]

There is an identical right-side formula.  Therefore the selected block of the actual query is

\[
 Q_j^L=
 P_{1,j}^L\bigl(\Gamma_{\rm grid}-\Phi_L(\Gamma_{\rm grid})\bigr)P_{0,j}^{L*},
\tag{6.8}
\]

where

\[
 P_{t,j}^L:N_t^L(\tau_j^L)\to
 \bigoplus_i L_{t,ij}\cong\mathbb C^r
\tag{6.9}
\]

is the selected-channel projection.  In parent bases the first term in (6.8) is (5.8).  The
second term is not its row mean.  It contains the recoupling of

\[
 \lambda_i\downarrow\lambda^-,
 \qquad
 \alpha\downarrow\bar\alpha,
 \qquad
 \nu\downarrow
 S_a\times S_a\times S_a\times S_a,
\tag{6.10}
\]

and the standard alphabet carrier in (6.7).  The same issue holds for every unselected
multiplicity channel and every other marked `H_L` type.  A bound on (6.8) does not bound the full
query unless all of them are controlled.

In particular, (5.6) does **not** imply

\[
 \|\Gamma_{\rm grid}\circ\Delta_i^L\|
 =O(r^{-1/2})
\tag{6.11}
\]

or its right-side analogue.  Treating the query as a projection that merely averages the parent
labels would replace (6.3) by a different oracle.  The missing analytic gate is the exact
one-point-orbital/Wigner estimate

\[
 \max_{\tau_L}\|C^L_{\tau_L}(\Gamma_{\rm grid})\|,
 \quad
 \max_{\tau_R}\|C^R_{\tau_R}(\Gamma_{\rm grid})\|
 \stackrel{?}{=}O(r^{-1/2}),
\tag{6.12}
\]

including all channels outside (6.9).  No identity in the frozen orbit classification evaluates
(6.12), and no estimate proving it was obtained here.

This is the narrowest exact failure of the proposed shortcut: **parent balance is balance for
restriction, not balance for the off-equality Schur map.**  It does not prove that the grid
candidate violates (6.12); it proves that the requested cancellation has not been constructed.

### 6.1 Exact hook ratios for the selected-singleton carrier

The preceding warning can be made quantitative before computing the full one-point orbital
matrix.  For a partition `theta` of size `A` with `s` rows, put

\[
 h_i=\theta_i+s-i.
\tag{6.13}
\]

If the corner in row `i` is removable, the hook formula gives the exact down-branching ratio

\[
 p_i(\theta):={f^{\theta-\square_i}\over f^\theta}
 ={h_i\over A}
 \prod_{j<i}{h_j-h_i+1\over h_j-h_i}
 \prod_{j>i}{h_i-h_j-1\over h_i-h_j}.
\tag{6.14}
\]

The branching identity `f^theta=sum_i f^(theta-box_i)` gives

\[
 \sum_i p_i(\theta)=1.
\tag{6.15}
\]

Apply this to the singleton partition `theta=alpha` from (4.2), whose size is `A=a` and whose
number of rows is `s=ell=r-1`.  Then

\[
 h_1=a-T+\ell-1,
 \qquad
 h_j=2(\ell-j)+1\quad(2\le j\le\ell).
\tag{6.16}
\]

For the first-row corner, (6.14) is

\[
 p_1={a-T+\ell-1\over a}
 \prod_{j=2}^{\ell}
 \left(1-{1\over a-T-\ell+2j-2}\right).
\tag{6.17}
\]

Consequently, with `epsilon=1-p_1`,

\[
 {T-\ell+1\over a}
 \le \epsilon
 \le
 {T-\ell+1\over a}
 +{\ell-1\over a-T-\ell+2},
\tag{6.18}
\]

and expansion of the finite product gives

\[
 p_1=1-{T\over a}+O\left({\ell^3\over a^2}\right),
 \qquad
 \sum_{j=2}^{\ell}p_j
 =\Theta\left({\ell^2\over a}\right).
\tag{6.19}
\]

On the critical subsequence, `a=Theta(m^2)` and `ell=Theta(m^(1/3))`, so

\[
 \epsilon=\Theta(m^{-4/3})=\Theta(r^{-4})=O(r^{-1}).
\tag{6.20}
\]

No fitted exponent or finite numerical spectrum is used here.

Let

\[
 v=(\sqrt{p_1},\ldots,\sqrt{p_\ell},0)\in\mathbb R^r,
 \qquad
 u={1\over\sqrt r}(1,\ldots,1).
\tag{6.21}
\]

The vector `v` is written in the **marked-origin basis**: its first `ell` coordinates are the
normalized singleton-corner branches and its final coordinate is the complementary marked-origin
channel in the Pieri square.  The parent basis is different.  Let

\[
 \mathcal U_t^L(j):\mathbb C^r_{\rm parent}
 \longrightarrow\mathbb C^r_{\rm origin}
 \tag{6.22}
\]

be the exact unitary Pieri/LR recoupling matrix on the selected `tau_j^L` multiplicity space for
answer class `t`; define `mathcal U_t^R(i)` analogously.  Its entries are symmetric-group 6j
coefficients.  The hook ratios (6.14) are normalized branch weights in the origin decomposition;
they are **not**, without evaluating (6.22), coordinates in the parent basis.

For the unweighted coefficient table (1.1), a fixed left column gives

\[
 D_j={r\over r-1}|e_j\rangle\langle e_j|
       -{1\over r-1}I_r,
 \tag{6.23}
\]

and the normalized, unmasked selected-corner block is exactly

\[
 A_j^L=\mathcal U_1^L(j)D_j\mathcal U_0^L(j)^*.
\tag{6.24}
\]

Thus `||A_j^L||=1` for every `j`.  Entrywise,

\[
 (A_j^L)_{cd}
 ={r\over r-1}\mathcal U_1^L(j)_{cj}
       \overline{\mathcal U_0^L(j)_{dj}}
 -{1\over r-1}
  (\mathcal U_1^L(j)\mathcal U_0^L(j)^*)_{cd}.
\tag{6.25}
\]

Equations (6.24)--(6.25) are the explicit normalized selected-corner 6j test.  They show that
zero column sum is not a cancellation identity for a corner block.

Viewed as an `r x r` table across the two parent directions, (1.1) is

\[
 B_{\rm unif}={r\over r-1}(I-uu^*).
\tag{6.26}
\]

It cancels the uniform **parent** vector `u`.  The correctly typed test of a normalized corner
compression uses a coefficient functional, not an identification of the two bases.  For
normalized origin vectors `x_1,x_0 in C^r_origin`, (6.24) gives

\[
 \langle x_1,A_j^Lx_0\rangle
 =\sum_i b_{ij}\,\zeta_i(x_1,x_0),
 \qquad
 \zeta_i=
 \overline{(\mathcal U_1^L(j)^*x_1)_i}
          (\mathcal U_0^L(j)^*x_0)_i.
\tag{6.27}
\]

To cancel this compression for every column `j`, the coefficient table must satisfy

\[
 \zeta(x_1,x_0)^*B=0.
\tag{6.28}
\]

The row-sum identity in (5.6) supplies (6.28) only when `zeta` is proportional to the uniform
vector.  If the YES and NO recouplings coincide and `x_1=x_0=v`, then

\[
 \zeta_i=| (\mathcal U^*v)_i |^2,
 \qquad \zeta_i\ge0,
 \qquad \sum_i\zeta_i=1.
\tag{6.29}
\]

Thus even in the aligned case the required weights are squared 6j amplitudes in the parent
basis, not the hook ratios themselves.  Since `v` is within
`O(sqrt(epsilon))=O(r^(-2))` of the first-row origin vector, proving that `zeta` is uniform is a
specific first-row 6j statement, not a consequence of dimension or orthogonality.

The naive basis-identification surrogate `mathcal U=I` can be tested exactly.  It has
`zeta=(p_1,...,p_ell,0)`, and (6.26) gives

\[
 \|\zeta^*B_{\rm unif}\|_2
 ={r\over r-1}
 \left\|\zeta-{1\over r}{\bf1}\right\|_2
 \ge {r\over r-1}\sqrt{p_1^2-{1\over r}}
 =1-O(r^{-1}).
\tag{6.30}
\]

So the surrogate fails by a constant.  The actual matrices `mathcal U_t` were not evaluated in
the frozen orbit artifacts, so the corresponding physical 6j functional (6.27) cannot be
asserted uniform or nonuniform here.  This is the exact formulation gap left by the hook
calculation.

If a dominant aligned functional `zeta` were computed, one could formally center with the
oblique weighted projections

\[
 B_{\rm hook}
 =(I-\mathbf1\zeta^*)\,C\,(I-\zeta\mathbf1^*)
 \quad\Longrightarrow\quad
 \zeta^*B_{\rm hook}=B_{\rm hook}\zeta=0,
\tag{6.31}
\]

where `C` is any fixed seed table and `zeta^*1=1`.  Even if the same `zeta` works on the left and
right, (6.31) cancels only one normalized functional.  It does **not** close (6.12): other corner
pairs have the different coefficient vectors (6.27).  The physical marked operator takes a
maximum over normalized marked multiplicity blocks, not a dimension-weighted average.  The small
sum (6.20) can yield an `O(sqrt(epsilon))` bound only after proving from the actual off-equality
one-point matrices that every surviving block carries the corresponding `sqrt(p_j)` amplitude in
one common operator sum.  Restriction branching alone supplies no such statement, and the
fixed-middle audits show why dimension weights cannot be substituted for operator norms.

There is one further refinement that prevents (6.24) from being mistaken for the physical query.
An origin corner `c` still splits into one-point orbitals according to whether the marked YES and
NO raw labels are equal.  The actual query keeps only the off-equality pieces.  There is no
projection `P_off` on the `r`-dimensional origin multiplicity space for which the query block is
`P_off A_j^L P_off`: equality status is an additional orbital index.  The fully typed selected
corner block is

\[
 Q_{j,c,d}^L
 =\sum_{\substack{\eta:\text{origin corners }(c,d)\\
                  \text{marked edge off equality}}}
   c_{\operatorname{forget}(\eta)}B^L_{\tau_j,\eta},
\tag{6.32}
\]

and the equality-pointed terms completing (6.24) are absent.  No frozen formula separates the
two sums at the 6j level.  Therefore no corner compression has been shown to be an
identity/isometry **after** the physical mask, and no scoped physical-query FAIL is claimed.

Therefore (6.31) is only the formula for the evident weighted repair, not a proved adversary.  It
still requires the complete recoupling, equality-status split, and all-channel bound (6.12).

## 7. Incidence and outer-scale audit

The operator (5.4) is already a legal full-orbit intertwiner, so it does not need an address chart
to exist.  However, its unit numerator is only a selector normalization.  The desired endpoint
argument also needs the independent outer contribution `a^(2/3)` and the existing occurrence
factor.

There is no tensor factorization

\[
 V_t\cong V_t^{\rm outer}\otimes V_t^{\rm selector}
\tag{7.1}
\]

on which one may simply tensor (5.4) with the UIC adversary.  Both laws act on the same full input
pair, and entrywise multiplication changes the Fourier blocks.  To use addressed presentations,
one must construct a lifted operator

\[
 \widetilde\Gamma:\ell_2(\mathcal Y_0)\to\ell_2(\mathcal Y_1)
\tag{7.2}
\]

whose normalized compression

\[
 R_1\widetilde\Gamma R_0^*:V_0\to V_1
\tag{7.3}
\]

contains (5.3) on the same block that carries the outer numerator.  On `u=1` the presentation
fibers have size `C=(a!)^2`; both unmasked and physically masked entries carry the same factor
`1/C`.  Nothing in Sections 4--6 proves that (7.3) preserves an `a^(2/3)` block, and nothing
allows that factor to be multiplied into (5.5) by declaration.

Thus the outer/incidence obligation remains open even if (6.12) were later proved.

## 8. Gate ledger

| Obligation | Outcome |
|---|---|
| exact decisive regime | infinite legal `p=0,u=1` subsequence (2.1) |
| exact full multiplicity spaces | defined by (2.4); no hidden regular ancilla |
| one parent set common to both one-coordinate sides | **IMPOSSIBLE for size >1**, Section 3 |
| necessary two-sided organization | `r x r` parent grid |
| explicit `r=Theta(m^(1/3))` parent shapes | (4.1)--(4.7) |
| common parents present in exact NO module | selected lines (4.11) |
| common parents present in exact YES module | selected lines (4.14); common existence (4.15) |
| fixed common alphabet partition | explicit `nu`, (4.8)--(4.10) |
| formula-defined nonseparable Fourier coefficients | balanced grid (1.1), (5.3)--(5.4) |
| unmarked selector norm | exactly one, (5.5) |
| left and right parent-restriction balance | exact, (5.6)--(5.9) |
| inference from that balance to query cancellation | **SCOPED FAIL**, Sections 6 and 6.1 |
| actual natural `B` after full 6j/equality split | **UNRESOLVED**; no gain credited |
| distinction between restriction and query Schur mask | exact pinching (6.3)--(6.7) |
| all off-equality marked norms `O(r^(-1/2))` | **UNPROVED**, explicit gate (6.12) |
| preservation of outer `a^(2/3)` numerator | **UNPROVED**, Section 7 |
| exact incidence normalization | common `1/C` on this subsequence; no claimed gain |
| exponent improvement | none |
| numerical evidence | none used |
| completion-tier status | none; proposer-tier artifact only |

## 9. Coverage and noncoverage

This memo proves:

* the literal same-parent-star implementation cannot mix nontrivially on both physical sides;
* an explicit legal parent grid of the target width exists in both exact answer modules;
* the balanced grid (1.1) is a well-typed, formula-defined full-orbit Fourier multiplier with
  unit norm;
* zero row/column sums are not a physical-query calculation, so that cancellation argument is a
  scoped FAIL.

It does **not** prove:

* that the balanced grid passes or fails the exact marked inequality (6.12);
* the total dimensions of the full fixed spaces beyond the selected lines;
* inverse-incidence survival on the outer numerator block;
* any bound for `p>0` or `u>1`;
* any lower-bound exponent.

The live continuation, if pursued, is now sharply finite: compute the one-point orbital matrices
in (6.12) for the displayed Pieri/LR grid and control every selected and unselected channel.  A
different coefficient law is a new ansatz and must be registered before testing under Rule 8.

## 10. Source ledger

Frozen exact inputs used here:

* exact `K_t`, `M_t`, rectangular orbital Fourier blocks, and one-point query orbitals:
  `ksum/artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md`;
* exact `p=0,u=1` wreath-product stabilizers and full transportation-orbit classification:
  `ksum/artifacts/ksum_L3_critical_full_position_incidence_orbit_classification_20260722.md`, corrected
  SHA-256 `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088`;
* exact distinction between unrestricted parent mixing and fixed-centered/fixed-middle carriers:
  `ksum/artifacts/ksum_L3_critical_full_position_mask_obstruction_audit_20260722.md`, SHA-256
  `19521DEB54082A37553F6D98075F33DD2095FE6307DBACDEA0121D18927AA315`.

## 11. Final assessment

Growing full-`G` parent content is real; it is not the missing theorem.  Product-group typing
forces a two-dimensional parent grid before both physical sides can mix.  The explicit balanced
grid is the first formula in this route that is nonseparable in those two parent directions, but
its attractive row/column cancellation lives in the restriction algebra.  The oracle acts by
off-equality Schur pinching, whose LR/Wigner recoupling matrices have not been evaluated.

Accordingly, the representation gate passes and the query/outer gates remain open.  Crediting a
`sqrt(r)=Theta(m^(1/6))` gain at this point would repeat the exact restriction-versus-mask error
that the node was created to avoid.
