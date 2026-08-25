# L3 critical endpoint: exact orbit-intertwiner reduction and first missing inequality

Date: 2026-07-21  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary`  
Status of this memo: **partial progress only; no endpoint witness and no DAG/status edit**

## 1. Verdict

This pass closes the representation-theoretic setup but does **not** construct the requested
`Omega(N^(2/3))` adversary.  The concrete outcomes are:

1. The two exact critical answer classes are written as homogeneous spaces `X_t=G/K_t`, and the
   stabilizers `K_0,K_1` and their orders are explicit.
2. A double coset in `K_1\G/K_0` is exactly a colored two-layer incidence graph.  Marking one
   queried coordinate turns it into the corresponding one-point extension; the query mask keeps
   precisely marked edges whose endpoint labels are unequal.
3. This gives an exact finite-dimensional block system for both the numerator and every masked
   norm.  No SDP optimizer or numerical exponent is used.
4. The smallest local two-orbital coefficient law can be solved completely.  It has masked norms
   one but numerator only `2 sqrt(a)=Theta(N^(1/3))`, so local repair of the unique collision is far
   too weak.
5. The known addressed construction is recovered, including its exact block norms, at
   `Omega(a^(2/3)sqrt(m))=Omega(N^(11/18))`.
6. Symmetrizing over hidden block addresses leads to a substantially smaller colored
   matching-cycle algebra.  In the separated address-erasure ansatz, the first still-unproved
   statement is one explicit norm inequality: the unmarked address operator must dominate every
   one-point marked operator by `Omega(m^(1/6))`.  This is exactly the missing
   `N^(1/18)` factor.

Thus the route remains open, but its next obligation is no longer the unconstrained full
double-coset search.  It is the marked-versus-unmarked norm separation in (9.7) below.

## 2. Frozen endpoint notation

Each side has length `n`; the total query length is `N=2n`.  The alphabet has size `q`.  Put

\[
 a=\lfloor q/4\rfloor,\qquad
 d=\left\lfloor {n-a\over a}\right\rfloor,\qquad
 p=(n-a)-ad,\qquad 0\le p<a,
 \tag{2.1}
\]

and write `m=d+1`.  At the critical endpoint,

\[
 a=\Theta(N^{2/3}),\qquad m=\Theta(N^{1/3}),\qquad N=\Theta(am).
 \tag{2.2}
\]

For an input pair `(x_L,x_R)`, let `h_rs` denote the number of alphabet symbols occurring `r`
times on the left and `s` times on the right.  The NO orbit `X_0` has

\[
\begin{array}{c|ccccccc}
(r,s)&(0,0)&(1,0)&(0,1)&(d,0)&(d+1,0)&(0,d)&(0,d+1)\\ \hline
h^{(0)}_{rs}&q-4a&a&a&a-p&p&a-p&p,
\end{array}
 \tag{2.3}
\]

and all other entries zero.  The YES orbit `X_1` has

\[
\begin{array}{c|cccccccc}
(r,s)&(0,0)&(1,1)&(1,0)&(0,1)&(d,0)&(d+1,0)&(0,d)&(0,d+1)\\ \hline
h^{(1)}_{rs}&q-4a+1&1&a-1&a-1&a-p&p&a-p&p.
\end{array}
 \tag{2.4}
\]

The action preserving the problem is

\[
 G=S_n^{(L)}\times S_n^{(R)}\times S_q,
 \tag{2.5}
\]

where the first two factors permute positions and the last factor relabels the alphabet
simultaneously on both sides.  It is transitive on each table (2.3) and (2.4).

## 3. Exact stabilizers

For any joint histogram `h=(h_rs)`, a representative has stabilizer

\[
 K(h)\cong S_{h_{00}}\times
 \prod_{(r,s)\ne(0,0)}
 \left((S_r\times S_s)^{h_{rs}}\rtimes S_{h_{rs}}\right).
 \tag{3.1}
\]

Here `S_r x S_s` permutes occurrences of one label within its left and right fibers.  The final
`S_(h_rs)` permutes labels of the same joint type together with their position fibers.  Factors
`S_0` and `S_1` are harmless and may be omitted.

Let `K_t=K(h^(t))`.  Define the common heavy factor

\[
 H_{a,d,p}:=
 \left[(d!)^{a-p}(a-p)!\right]^2
 \left[((d+1)!)^p p!\right]^2.
 \tag{3.2}
\]

Then

\[
 |K_0|=(q-4a)!(a!)^2H_{a,d,p},
 \tag{3.3}
\]

\[
 |K_1|=(q-4a+1)!((a-1)!)^2H_{a,d,p}.
 \tag{3.4}
\]

Consequently

\[
 X_t\cong G/K_t,
 \qquad
 {|X_1|\over |X_0|}={|K_0|\over |K_1|}
 ={a^2\over q-4a+1}.
 \tag{3.5}
\]

Since `a=floor(q/4)`, the denominator in (3.5) is an integer in `{1,2,3,4}`.  This large orbit-size
imbalance is real and must be included in orbital normalizations.

## 4. Complete double-coset parameter

Fix one YES input `x` and one NO input `y`.  Associate to `(x,y)` the following finite object
`D(x,y)`.

* Make one vertex `z_1` for every alphabet label as used by `x`, colored by its YES joint type
  `(r,s)`, and one vertex `z_0` for every alphabet label as used by `y`, colored by its NO joint
  type.
* Add a distinguished perfect matching `M_=` between the two copies: `z_1` is matched to `z_0`
  exactly when they are the same raw alphabet symbol.
* For each left position `i`, add an `L`-colored edge from the YES label `x_L(i)` to the NO label
  `y_L(i)`.  Parallel edges record multiplicity.
* Do the same for right positions, using `R`-colored edges.

The row and column degrees in the `L` layer are fixed by the left multiplicities of the endpoint
vertices; the analogous statement holds in the `R` layer.

**Completeness.**  Two pairs `(x,y)` and `(x',y')` lie in the same diagonal `G`-orbit if and only
if `D(x,y)` and `D(x',y')` are isomorphic preserving vertex colors, `M_=`, and the `L/R` edge
colors.  The forward implication is immediate.  Conversely, an isomorphism gives the common
alphabet permutation through `M_=`.  Equality of edge multiplicities lets one choose independent
left and right position permutations carrying every occurrence-pair fiber to its mate.  These
three permutations form the required element of `G`.

Therefore

\[
 K_1\backslash G/K_0
 \quad\longleftrightarrow\quad
 \{\text{isomorphism classes of the graphs }D(x,y)\}.
 \tag{4.1}
\]

This is an exact combinatorial parameter, not yet a small list: the full algebra still contains
exponentially rich incidence data.  Section 9 isolates the smaller matching-cycle subalgebra that
is relevant to hiding the known addressed witness.

For a double coset `omega=K_1 g K_0`, let `A_omega` be its zero-one orbital matrix, with YES rows and
NO columns.  If

\[
 I_\omega=K_1\cap gK_0g^{-1},
 \tag{4.2}
\]

then its row and column degrees are

\[
 r_\omega={|K_1|\over |I_\omega|},\qquad
 s_\omega={|K_0|\over |I_\omega|},
 \tag{4.3}
\]

and hence

\[
 \|A_\omega\|=\sqrt{r_\omega s_\omega}.
 \tag{4.4}
\]

Thus either the raw basis `A_omega` or the normalized basis
`Ahat_omega=A_omega/sqrt(r_omega s_omega)` can be used without an implicit measure convention.

## 5. Query masks are one-point extensions

Fix a left coordinate `i`.  Its stabilizer is

\[
 H_L=S_{n-1}^{(L)}\times S_n^{(R)}\times S_q;
 \tag{5.1}
\]

for a right coordinate, interchange the first two factors and call the result `H_R`.

Marking coordinate `i` in the pair `(x,y)` is exactly the operation of distinguishing one
occurrence of an `L` edge in `D(x,y)`.  The two queried values agree if and only if this marked edge
lies on the equality matching `M_=`.  Consequently, if `eta` runs over marked graph isomorphism
classes and `T^L_eta` is the associated `H_L` orbital,

\[
 A_\omega\circ\Delta_i
 =\sum_{\substack{\eta:\;\operatorname{forget}(\eta)=\omega\\
                   \text{marked edge is off }M_=}}
 T^L_\eta.
 \tag{5.2}
\]

The identical formula with a marked `R` edge holds for a right query.  Hence for coefficients
`c_omega`,

\[
 \left(\sum_\omega c_\omega A_\omega\right)\circ\Delta_i
 =\sum_\eta c_{\operatorname{forget}(\eta)}T^L_\eta,
 \tag{5.3}
\]

where marked equality edges are omitted.  Formula (5.3) is the exact query-mask action; no
entrywise-mask estimate has been replaced by a Frobenius bound.

## 6. Exact finite-dimensional operator system

Work over `C`; all matrices and coefficients can subsequently be chosen real.  The answer modules
are

\[
 V_t=\mathbb C[X_t]\cong\operatorname{Ind}_{K_t}^{G}{\bf 1}.
 \tag{6.1}
\]

An irreducible representation of `G` is indexed by

\[
 \rho=(\lambda,\mu,\nu),\qquad
 \lambda,\mu\vdash n,\quad \nu\vdash q,
 \tag{6.2}
\]

and has carrier `S^lambda tensor S^mu tensor S^nu`.  Its multiplicity space in `V_t` is

\[
 M_t(\rho)=
 (S^\lambda\otimes S^\mu\otimes S^\nu)^{K_t}.
 \tag{6.3}
\]

Choose orthonormal bases of these fixed spaces and the standard unitary matrix-coefficient Fourier
maps `U_t`.  For each orbital define, without any normalization ambiguity,

\[
 B_{\rho,\omega}:=
 \left[U_1^*A_\omega U_0\right]_{M_1(\rho)\leftarrow M_0(\rho)}.
 \tag{6.4}
\]

Equivalently, (6.4) is a finite sum of Specht matrix coefficients over the explicitly given double
coset.  It is therefore an exact symbolic definition, not an optimization prescription.  An
invariant candidate

\[
 \Gamma(c)=\sum_\omega c_\omega A_\omega
 \tag{6.5}
\]

has

\[
 \|\Gamma(c)\|
 =\max_\rho\left\|
       \sum_\omega c_\omega B_{\rho,\omega}
                 \right\|.
 \tag{6.6}
\]

For a left query, irreducibles of `H_L` are indexed by

\[
 \tau=(\lambda^-,\mu,\nu),\qquad
 \lambda^-\vdash n-1,quad\mu\vdash n,quad\nu\vdash q.
 \tag{6.7}
\]

Fourier transforming each marked orbital in (5.3) defines exact matrices
`B^L_(tau,eta)` between the corresponding `H_L` multiplicity spaces.  Therefore

\[
 \|\Gamma(c)\circ\Delta_i\|
 =\max_\tau
 \left\|
   \sum_{\substack{\eta:\text{ marked }L\text{ edge off }M_=}}
     c_{\operatorname{forget}(\eta)}B^L_{\tau,\eta}
 \right\|.
 \tag{6.8}
\]

There is an analogous expression with `mu^-` a partition of `n-1` for a right query.  Transitivity makes (6.8)
independent of the selected coordinate within a side.

Equations (6.6) and (6.8) are the promised finite-dimensional operator system.  A successful
formula-defined family must satisfy

\[
 \max_\rho\left\|\sum_\omega c_\omega B_{\rho,\omega}\right\|
      =\Omega(N^{2/3}),
 \tag{6.9}
\]

and both left and right versions of (6.8) must be at most one.  The present pass does not supply
such `c_omega`.

## 7. Fully solved two-orbital ansatz: local collision splitting fails

Let

\[
 u=q-4a+1\in\{1,2,3,4\},
 \tag{7.1}
\]

the number of unused labels in a YES input.  Define two relations.

* `A_L`: replace the left occurrence of the unique shared singleton by one YES-unused label,
  leaving all other coordinates fixed.
* `A_R`: make the analogous replacement on the right.

Both outputs are legal NO inputs, including all heavy multiplicities and every remainder `p`.
For a fixed YES row, `A_L+A_R` has degree `2u`.  For a fixed NO column, reversing the left move
requires choosing one of its `a` left singletons and one of its `a` right singletons, and similarly
on the right.  Thus its column degree is `2a^2`, and

\[
 \|A_L+A_R\|=\sqrt{(2u)(2a^2)}=2a\sqrt u.
 \tag{7.2}
\]

For a fixed left coordinate, only `A_L` survives the query mask.  On its nonzero rows and columns,
the masked relation has row degree `u` and column degree `a`.  Therefore

\[
 \|(A_L+A_R)\circ\Delta_i\|=\sqrt{au}
 \tag{7.3}
\]

for every left coordinate, with the same result for right coordinates.  The normalized witness

\[
 \Gamma_{\rm split}:={A_L+A_R\over\sqrt{au}}
 \tag{7.4}
\]

has the explicit orbital coefficient law

\[
 c_\omega=
 \begin{cases}
 (au)^{-1/2},&\omega\in\{\omega_L,\omega_R\},\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{7.5}
\]

It has all masked norms exactly one, but

\[
 \|\Gamma_{\rm split}\|=2\sqrt a=\Theta(N^{1/3}).
 \tag{7.6}
\]

This is optimal within the whole two-orbital span, including signed coefficients.  Indeed, for
`Gamma=alpha A_L+beta A_R`, the left and right masks separately force

\[
 |\alpha|\sqrt{au}\le1,
 \qquad
 |\beta|\sqrt{au}\le1.
 \tag{7.7}
\]

Since `||A_L||=||A_R||=a sqrt(u)`, the triangle inequality gives

\[
 \|\Gamma\|
 \le (|\alpha|+|\beta|)a\sqrt u
 \le2\sqrt a.
 \tag{7.8}
\]

The positive equal coefficients in (7.5) attain this bound because both orbitals have the same
constant left and right top singular vectors.

This gives a scoped obstruction: coefficients supported only on the two immediate collision-split
orbitals do not even recover the addressed baseline.  Any useful law must correlate pairs that
differ throughout many singleton/heavy incidences.

## 8. Recovery of the addressed `N^(11/18)` baseline

The exact promise contains the literal addressed subfunction

\[
 \mathrm{UIC}_a\circ(\mathrm{pSearch}_m)^{2a},
 \qquad m=d+1,
 \tag{8.1}
\]

with one fixed public heavy coordinate for each of the `p` long heavy labels on each side.  Let
`Gamma_UIC` be an outer adversary normalized by

\[
 \max_j\|\Gamma_{\rm UIC}\circ\Delta_j\|\le1,
 \qquad
 \|\Gamma_{\rm UIC}\|=\Omega(a^{2/3}).
 \tag{8.2}
\]

In the explicit block composition, a differing outer symbol uses the inner block `J_m`, while an
equal outer symbol uses the modified diagonal block `m I_m`.  Every unmasked inner block has norm
`m`, so the composed numerator is

\[
 \|\Gamma_{\rm comp}\|
 =\|\Gamma_{\rm UIC}\|m^{2a}.
 \tag{8.3}
\]

Masking one physical coordinate changes only its one `pSearch` block, whose relevant norm becomes
`sqrt(m-1)` instead of `m`.  Consequently

\[
 \max_i\|\Gamma_{\rm comp}\circ\Delta_i\|
 \le \sqrt{m-1}\,m^{2a-1}.
 \tag{8.4}
\]

The fixed remainder coordinates have zero mask.  Dividing (8.3) by (8.4) gives

\[
 \operatorname{Adv}^{\pm}(X_0,X_1)
 \ge
 \Omega\!\left(a^{2/3}{m\over\sqrt{m-1}}\right)
 =\Omega(a^{2/3}\sqrt m)
 =\Omega(N^{11/18}).
 \tag{8.5}
\]

This is a sanity restriction of the exact endpoint operator problem, not yet a coefficient law in
the full `G`-orbital basis.  Averaging the restriction over all hidden addresses is precisely where
unmarked and query-marked norms can interfere, so (8.5) cannot simply be declared invariant.

The desired endpoint scale is

\[
 a^{2/3}m^{2/3}=\Theta(N^{2/3}).
 \tag{8.6}
\]

Thus the exact additional gain is

\[
 {a^{2/3}m^{2/3}\over a^{2/3}m^{1/2}}
 =m^{1/6}=\Theta(N^{1/18}).
 \tag{8.7}
\]

## 9. Tractable address-erasure algebra

### 9.1 Addresses of a full-orbit input

On either side, an addressing consists of:

1. a perfect matching between the `a` singleton labels and the `a` private heavy labels; and
2. for every frequency-`d+1` heavy label, a choice of one of its `d+1` occurrences as the public
   extra coordinate.

The remaining `d` heavy occurrences together with the matched singleton form a `pSearch_m` block.
Internal block order may be quotiented because the matrices `J_m` and `mI_m` in Section 8 commute
with every permutation of the `m` positions.

Given two addresses of the same input, the union of their two perfect matchings is a disjoint union
of alternating cycles.  Heavy vertices are colored `short` or `long`.  At a long vertex, the two
excluded occurrences are either equal or distinct.  Therefore a relative-address orbit is exactly
an isomorphism class

\[
 \theta=\{\text{two-edge-colored alternating cycles with short/long vertex colors and
 long-exclusion equality flags}\}.
 \tag{9.1}
\]

Equivalently, it is a multiset of colored cyclic words, with the total numbers of short and long
heavy vertices fixed to `a-p` and `p`.  Let `R_theta` be the zero-one matrix of this relation.  The
span

\[
 \mathcal A_{\rm addr}=\operatorname{span}\{R_\theta\}
 \tag{9.2}
\]

is a finite coherent-configuration algebra (a colored permutation/rook algebra).  It discards the
irrelevant full position-incidence graph while retaining exactly the ambiguity absent from the
addressed construction.

### 9.2 Marked address algebras

A physical query makes a one-point extension of (9.2).  The marked types that must all be retained
are:

* a singleton coordinate, which marks its incident edge in each matching;
* an occurrence of a short heavy label;
* an occurrence of a long heavy label, together with the two bits recording whether that
  occurrence is excluded by the first and/or second address.

The last item has all feasible statuses in `{0,1}^2`; merging them would lose the actual query-mask
action.  Write `R^(bullet,zeta)_theta` for the resulting marked relation, where `zeta` includes the
side and the marked type.

For formula weights `w=(w_theta)`, set

\[
 K(w)=\sum_\theta w_\theta R_\theta,
 \qquad
 K^\bullet_\zeta(w)=\sum_\theta w_\theta R^{\bullet,\zeta}_\theta.
 \tag{9.3}
\]

Fourier decomposition of the finite coherent configuration gives blocks

\[
 K_\chi(w)=\sum_\theta w_\theta\widehat R_{\theta,\chi},
 \qquad
 K^\bullet_{\zeta,\psi}(w)
 =\sum_\theta w_\theta\widehat R^{\bullet,\zeta}_{\theta,\psi}.
 \tag{9.4}
\]

These matrices can be obtained by exact cycle induction and restriction; (9.4) is the small
operator system to analyze before returning to all graph orbitals in Section 4.

### 9.3 The first missing norm inequality

Normalize the incidence maps from addressed copies to full-orbit inputs so that the same-address
kernel has address ratio one.  In the separated ansatz consisting of the Section 8 adversary and an
address kernel (9.3), define

\[
 \mathcal R_{\rm addr}(w):=
 {\displaystyle\max_\chi\|K_\chi(w)\|
  \over
  \displaystyle\max_{\zeta,\psi}
                  \|K^\bullet_{\zeta,\psi}(w)\|}.
 \tag{9.5}
\]

The diagonal/same-address choice has

\[
 \mathcal R_{\rm addr}=1,
 \tag{9.6}
\]

so merely summing independent addressed witnesses cannot improve (8.5).  A sufficient new
coefficient theorem inside this ansatz is the following explicit inequality for formula-defined
weights, uniformly in `a,d,p`:

\[
 \boxed{
 \max_\chi\left\|\sum_\theta w_\theta\widehat R_{\theta,\chi}\right\|
 \ \ge\ c\,m^{1/6}
 \max_{\zeta,\psi}
 \left\|\sum_\theta
 w_\theta\widehat R^{\bullet,\zeta}_{\theta,\psi}\right\|
 }
 \tag{9.7}
\]

for an absolute `c>0`.  Combining (9.7) with (8.5) would give

\[
 \Omega(a^{2/3}\sqrt m)\,\Omega(m^{1/6})
 =\Omega(a^{2/3}m^{2/3})
 =\Omega(N^{2/3}).
 \tag{9.8}
\]

No weights satisfying (9.7) were found in this pass.  In particular, (9.7) must come from signed
interference among off-diagonal alternating-cycle types; the diagonal relation cannot provide it.
Before crediting any future candidate, its incidence normalization must also be checked against the
full masked system (6.8), including every long-heavy exclusion status.

## 10. Gate ledger

| Obligation | Outcome |
|---|---|
| exact YES/NO stabilizers | closed by (3.1)--(3.5) |
| complete double-coset parameter | closed by the colored graph in Section 4 |
| exact query-mask action | closed by marked orbitals (5.2)--(5.3) |
| finite numerator/mask operator system | closed by (6.6)--(6.8) |
| explicit local coefficient test | solved; only `Theta(N^(1/3))` |
| recover addressed baseline | `Omega(N^(11/18))`, equation (8.5) |
| quantify missing gain | exactly `m^(1/6)=N^(1/18)` |
| smaller relevant subalgebra | colored matching-cycle algebra (9.2) |
| formula weights proving endpoint | **not found** |
| all masked norms `O(1)` with numerator `Omega(N^(2/3))` | **not proved** |
| numerical/SDP evidence | none used |
| DAG/status edit | none |

## 11. Untested ideas and scope control

Within this registered node, a natural next coefficient family is a signed cycle-weight law whose
weight depends on alternating-cycle length and long-exclusion mismatch count, followed by an exact
diagonalization of both (9.4) systems.  This is only a proposed calculation; it has not been tested
and is not evidence for (9.7).

No outside-node proof route was generated in this pass.  In particular, this memo does not propose
a new walk, learning graph, polynomial dual, endpoint algorithm, or promise change.

## 12. Bottom line

The exact critical endpoint has a clean orbit-intertwiner formulation.  Its full double cosets are
colored YES/NO incidence graphs, and a query is exactly a marked off-equality edge.  The immediate
two-orbital repair law is rigorously too small, while the addressed restriction remains at
`N^(11/18)`.

The only identified mechanism capable of supplying the remaining exponent inside this route is
coherent cancellation between different hidden block addresses.  Its first auditable target is
the marked-versus-unmarked matching-cycle norm separation (9.7), with gain `m^(1/6)`.  Until an
explicit signed weight law and all marked block bounds are proved, the endpoint node must remain
open.
