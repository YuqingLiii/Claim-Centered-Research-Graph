# L3 critical endpoint: repaired-full-matching growing selector and multiplicity-one collapse

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.growing-selector-specht-branching-kernel`  
Verdict: **FAIL for the multiplicity-one repaired-full-matching transport formula below; PARTIAL
for the registered growing-selector node**  
Status discipline: proposer-tier analytic calculation; no completion status and no numerical
exponent claim

## 1. Verdict

The actual outer `UIC_a` YES/NO transition does contain a common growing Specht sector with
`r=Theta(m^(1/3))` removable branches.  It is not necessary, and would be incorrect, to attach an
unjustified regular-module ancilla.

There is nevertheless an exact obstruction for the first canonical formula.  Repairing the
unique YES collision with its unique unused outer label gives a full permutation between the
`2a` outer slots of a YES presentation and those of a NO presentation.  In every representation
of `S_(2a)` this permutation is an input-wise unitary transport.  In a common `K=S_a^L x S_a^R`
type of multiplicity one, incidence contraction has only one scalar Schur channel.  The transport
maps its normalized coevaluation vector exactly to the corresponding vector on the other input,
so its coefficient is identically one.

After a physical query breaks one `S_a` factor to `S_(a-1)`, the chosen partition does branch into
`r` distinct removable-corner channels.  The actual mask does not select one channel.  The same
transport is the identity on all `r` channels simultaneously, so its marked multiplicity operator
is `I_r`, of norm one.  Thus removable corners give a direct sum, not a `1/sqrt(r)` load split.

Consequently this full-matching selector leaves both the unmasked incidence-compressed kernel and
every physical-query-compressed kernel exactly equal to the corresponding kernels without the
selector.  With standard BHK occurrence blocks its best possible scale remains

\[
 O\!\left(a^{2/3}{m\over\sqrt{m-1}}\right)
 =O(a^{2/3}\sqrt m)=O(N^{11/18})
\tag{1.1}
\]

on the decisive legal `p=0,u=1` subsequence.  The missing `sqrt(r)=Theta(m^(1/6))` factor is zero:
the selector contribution to the ratio is exactly one.

This does not test a transition carrier in which the common `K`-type has growing multiplicity, or
a selector whose cycle-word coefficient is not the factorized repaired-matching transport.  Those
are separately registered Rule-8 successors and are outside this memo.

## 2. Exact subsequence, groups, and repaired matching

Use the infinite exact critical subsequence

\[
 a=k^2,\qquad q=4k^2,\qquad d=k,\qquad m=k+1,
 \qquad n=a(d+1),
\tag{2.1}
\]

so

\[
 p=0,\qquad u=q-4a+1=1,\qquad N=2am.
\tag{2.2}
\]

The `UIC_a` outer coordinate set is

\[
 P=([a]_L)\sqcup([a]_R),\qquad |P|=2a,
\tag{2.3}
\]

and its selected outer palette `A` has `2a` labels.  The hidden block-reindexing gauge group is

\[
 K=S_a^{(L)}\times S_a^{(R)}\le S_P\cong S_{2a}.
\tag{2.4}
\]

For a NO outer input `z_0`, the label map

\[
 \tau_0(z_0):P\longrightarrow A,\qquad c\longmapsto z_0(c),
\tag{2.5}
\]

is a bijection.  A YES outer input `z_1` has one common label `s` at coordinates
`c_L in [a]_L,c_R in [a]_R` and one unused palette label `h`.  Use the fixed side-respecting repair

\[
 \tau_1(z_1)(c)=
 \begin{cases}
 h,&c=c_R,\\
 z_1(c),&c\ne c_R.
 \end{cases}
\tag{2.6}
\]

This is also a bijection `P -> A`.  Choosing the right collision endpoint is equivariant because
the problem symmetry preserves the two sides.  It introduces no arbitrary ordering of the other
`2a-1` labels.

The repaired full transition is the permutation

\[
 \pi(z_1,z_0)=\tau_1(z_1)^{-1}\tau_0(z_0):P\longrightarrow P.
\tag{2.7}
\]

If `k_t in K` reindexes the outer slots of presentation `z_t`, using
`(k_t z_t)(c)=z_t(k_t^{-1}c)`, then

\[
 \tau_t(k_tz_t)=\tau_t(z_t)k_t^{-1},\qquad
 \pi(k_1z_1,k_0z_0)=k_1\pi(z_1,z_0)k_0^{-1}.
\tag{2.8}
\]

Thus (2.7) is an actual `K`-by-`K` covariant of the UIC transition.  It is not a regular-module
label attached independently of the transition.

The available transition set really supplies the carrier used below.  As `z_0` ranges over NO
inputs, `tau_0` ranges over every bijection `P -> A`.  Conversely, given any bijection
`b:P -> A`, choose `c_L in [a]_L,c_R in [a]_R`, replace the value `b(c_R)` by `b(c_L)` in the
YES input, and declare `b(c_R)` unused.  The repaired map (2.6) is then exactly `b`.  Hence
`tau_1` also ranges over every bijection and the set of repaired transitions (2.7) ranges over all
of `S_(2a)`.  Its matrix coefficients contain each `S_(2a)` Fourier carrier with its genuine
regular multiplicity; Section 3 selects one explicit irreducible carrier and audits its actual
`K`-multiplicity instead of assuming an extra copy.

## 3. An explicit common growing Specht sector

Let

\[
 r=\lfloor m^{1/3}\rfloor,
 \qquad s={r(r-1)\over2},
\tag{3.1}
\]

and, for all sufficiently large members of (2.1), define

\[
 \lambda=(a-s,r-1,r-2,\ldots,2,1)\vdash a.
\tag{3.2}
\]

All row lengths in (3.2) are distinct, so `lambda` has exactly `r` removable corners.  Its depth
below the first row is

\[
 a-\lambda_1=s=\Theta(r^2)=\Theta(m^{2/3})=o(a).
\tag{3.3}
\]

Put

\[
 \Theta=2\lambda
 =(2a-2s,2r-2,2r-4,\ldots,4,2)\vdash2a.
\tag{3.4}
\]

The extremal Littlewood--Richardson coefficient is

\[
 c^{\Theta}_{\lambda,\lambda}=c^{2\lambda}_{\lambda,\lambda}=1.
\tag{3.5}
\]

Equivalently, the highest-weight summand of weight `lambda+lambda` occurs once.  Therefore the
restriction of the genuine full-matching carrier contains

\[
 S^\Theta\downarrow_K
 \supset \Lambda:=S^\lambda\boxtimes S^\lambda
\tag{3.6}
\]

with multiplicity exactly one.  If `D_Theta=f^Theta` and
`D_Lambda=(f^lambda)^2`, choose an isometric intertwiner

\[
 J:V_\Lambda\longrightarrow V_\Theta,
 \qquad
 \rho_\Theta(k)J=J\rho_\Lambda(k),
 \quad k\in K.
\tag{3.7}
\]

Equations (2.7) and (3.4)--(3.7) answer the first type question positively: a formula from the
actual transition carries the same growing `K`-type as the hidden-address module on both answer
classes.

## 4. Typed matrix-valued outer transport

Fix reference identifications of `P` and `A` only to write permutation matrices.  Let

\[
 U_t(z_t)=\rho_\Theta(\tau_t(z_t))\in U(V_\Theta),
\tag{4.1}
\]

where changing either reference conjugates every display below by fixed unitaries.  The repaired
transport from the NO slot carrier to the YES slot carrier is

\[
 T(z_1,z_0)=U_1(z_1)^{-1}U_0(z_0)
 =\rho_\Theta(\pi(z_1,z_0))
 \in\operatorname{Hom}(V_\Theta,V_\Theta).
\tag{4.2}
\]

Let

\[
 \Gamma_{\rm UIC}:\ell_2(U_0)\longrightarrow\ell_2(U_1)
\tag{4.3}
\]

be any scalar outer UIC adversary.  Define the block matrix

\[
 \mathcal B_\Theta:
 \ell_2(U_0)\otimes V_\Theta
 \longrightarrow
 \ell_2(U_1)\otimes V_\Theta
\tag{4.4}
\]

by its `D_Theta x D_Theta` blocks

\[
 \mathcal B_\Theta[z_1,z_0]
 =\Gamma_{\rm UIC}[z_1,z_0]T(z_1,z_0).
\tag{4.5}
\]

With the block-diagonal unitaries

\[
 \mathcal D_t=\bigoplus_{z_t\in U_t}U_t(z_t)^{-1},
\tag{4.6}
\]

formula (4.5) is exactly

\[
 \mathcal B_\Theta
 =\mathcal D_1(\Gamma_{\rm UIC}\otimes I_{D_\Theta})\mathcal D_0^*.
\tag{4.7}
\]

Hence

\[
 \|\mathcal B_\Theta\|=\|\Gamma_{\rm UIC}\|.
\tag{4.8}
\]

If `M` is any scalar zero-one mask on UIC input pairs, it multiplies every block of (4.5) by one
scalar.  Therefore

\[
 \mathcal B_\Theta\circ(M\otimes J_{D_\Theta})
 =\mathcal D_1((\Gamma_{\rm UIC}\circ M)\otimes I_{D_\Theta})\mathcal D_0^*,
\tag{4.9}
\]

and

\[
 \|\mathcal B_\Theta\circ(M\otimes J_{D_\Theta})\|
 =\|\Gamma_{\rm UIC}\circ M\|.
\tag{4.10}
\]

This applies in particular to every outer coordinate-query mask.  It also applies after replacing
the scalar entries of `Gamma_UIC` by the standard BHK occurrence blocks: a physical query is still
a scalar entrywise mask on each pair of presentation inputs, while `T` acts only on the selector
carrier.  Thus the repaired matching does not lose the outer `a^(2/3)` numerator, but (4.10)
already shows that it creates no selector-layer gain before incidence.

## 5. Exact incidence Schur contraction

The covariant `Lambda` frame over input `z_t` is

\[
 F_t(z_t)=U_t(z_t)^{-1}J:
 V_\Lambda\longrightarrow V_\Theta.
\tag{5.1}
\]

Equation (2.8) gives `F_t(k_tz_t)=rho_Theta(k_t)F_t(z_t)`.  Couple this frame to the dual hidden-
address carrier.  For any orthonormal basis `(e_b)_(b=1)^(D_Lambda)`, the normalized coevaluation
vector is

\[
 \Phi_t(z_t)
 ={1\over\sqrt{D_\Lambda}}
 \sum_{b=1}^{D_\Lambda}
 F_t(z_t)e_b\otimes\overline{e_b}
 \in V_\Theta\otimes\overline{V_\Lambda}.
\tag{5.2}
\]

It is the unique normalized `K`-invariant channel in this `Lambda` sector because the
multiplicity (3.5) is one.  The transport is exact on the whole frame:

\[
 T(z_1,z_0)F_0(z_0)=F_1(z_1).
\tag{5.3}
\]

Consequently

\[
 (T(z_1,z_0)\otimes I)\Phi_0(z_0)=\Phi_1(z_1),
\qquad
 \left\langle\Phi_1,(T\otimes I)\Phi_0\right\rangle=1.
\tag{5.4}
\]

This is the typed Schur pairing for the candidate.  It is stronger than a norm estimate: the
proposed growing coefficient collapses entrywise to the coefficient without the selector.

To include the exact rectangular incidence normalization, let `A` be any scalar lifted kernel on
the presentation spaces `Y_0,Y_1`.  Define extended incidence contractions by averaging the
functional `bra Phi_t` over each presentation fiber.  Their row normalizations are
`C^(-1/2)` on NO and `(uC)^(-1/2)` on YES, exactly as for `R_0,R_1`.  Sandwiching the block lift
`A[z_1,z_0]T(z_1,z_0) tensor I` between these contractions and using (5.4) gives

\[
 \mathcal R_1\widetilde A_{\Theta,\Lambda}\mathcal R_0^*
 =R_1AR_0^*.
\tag{5.5}
\]

The full entry normalization is therefore still `1/(C sqrt(u))`.  On the decisive subsequence
`u=1,C=(a!)^2`.  No hidden dimension, `sqrt(r)`, or unbalanced incidence scalar appears.

Because the physical presentation mask `tilde Delta_i` is scalar on every pair of presentation
fibers, (4.9), (5.4), and the exact incidence/mask commutation give simultaneously

\[
 \mathcal R_1(\widetilde A_{\Theta,\Lambda}\circ\widetilde\Delta_i)
 \mathcal R_0^*
 =R_1(A\circ\widetilde\Delta_i)R_0^*.
\tag{5.6}
\]

Thus the selector changes neither the unmasked compressed operator nor any physical-query-
masked compressed operator.

## 6. Why the `r` removable corners do not load-balance queries

Marking a coordinate on the left changes the gauge group to

\[
 H_L=S_{a-1}^{(L)}\times S_a^{(R)}.
\tag{6.1}
\]

The branching rule is multiplicity-free:

\[
 V_\lambda\downarrow S_{a-1}
 =\bigoplus_{j=1}^r V_{\mu_j},
 \qquad \mu_j\nearrow\lambda,
\tag{6.2}
\]

where the `mu_j` are the `r` diagrams obtained by deleting the removable corners of (3.2).  Hence

\[
 V_\Lambda\downarrow H_L
 =\bigoplus_{j=1}^r(V_{\mu_j}\boxtimes V_\lambda).
\tag{6.3}
\]

For each summand define the normalized `H_L` coevaluation vector `Phi_(t,j)` by restricting the
sum in (5.2) to an orthonormal basis of that summand.  Equation (5.3) holds on every vector of
`V_Lambda`, not only on its average.  Therefore

\[
 (T\otimes I)\Phi_{0,j}=\Phi_{1,j}
 \quad(1\le j\le r),
\tag{6.4}
\]

and the exact marked multiplicity operator is

\[
 \boxed{I_r:\mathbb C^r\longrightarrow\mathbb C^r},
 \qquad \|I_r\|=1.
\tag{6.5}
\]

The same statement holds for a right query, with the two factors interchanged.  The `r` channels
are parallel direct-sum blocks.  The operator norm is their maximum, not the Euclidean norm of a
vector with `r` separately queried components.

Schur's lemma makes the obstruction unavoidable inside this precise formula.  Since (3.5) is a
multiplicity-one occurrence, the unmarked `K`-intertwiner on the common `Lambda` channel is a
scalar.  It has no formula-defined multiplicity vector whose coordinates could be balanced over
the corners.  Restricting that scalar identity to `H_L` gives (6.5).  A physical query marks a
coordinate and hence exposes the full `H_L` restriction; it does not project onto a chosen
`mu_j`.  Claiming a `sqrt(r)` gain from the mere number of removable corners would replace the
actual mask by a different oracle.

## 7. Restoring the BHK occurrence layer

Now specialize the scalar lift `A` in Section 5 to the standard same-address
`UIC_a o (pSearch_m)^(2a)` composition.  This is the diagonal address subalgebra whose normalized
address ratio is exactly one in the orbit-intertwiner audit; no off-diagonal address law is being
silently included.  Every unmasked occurrence block has
norm `m`.  At a differing selected outer coordinate, one physical query replaces its `J_m` block
by a block of norm `sqrt(m-1)`.  The repaired-matching selector contributes the factor one in both
the unmasked and marked systems by (5.5)--(6.5).  Therefore the ratio of this entire formula is
exactly the ratio of its selector-free base:

\[
 {\|\Gamma_{\rm candidate}\|
  \over\max_i\|\Gamma_{\rm candidate}\circ\Delta_i\|}
 \le
 O\!\left(
 {\|\Gamma_{\rm UIC}\|
  \over\max_j\|\Gamma_{\rm UIC}\circ\Delta_j\|}
 {m\over\sqrt{m-1}}
 \right).
\tag{7.1}
\]

The general-adversary upper bound for `UIC_a` is `O(a^(2/3))`, including operator-valued
coefficients with query-invisible carriers.  Hence

\[
 {\|\Gamma_{\rm candidate}\|
  \over\max_i\|\Gamma_{\rm candidate}\circ\Delta_i\|}
 =O(a^{2/3}\sqrt m)=O(N^{11/18}).
\tag{7.2}
\]

If the incidence-compressed selector-free base loses norm, the candidate is only weaker; equations
(5.5)--(5.6) show that the growing selector cannot repair it.  If that base preserves the outer
`a^(2/3)` numerator, this selector preserves it exactly but still supplies no additional factor.

On (2.1), the target is `a^(2/3)m^(2/3)=Theta(N^(2/3))`, and

\[
 {a^{2/3}m^{2/3}\over a^{2/3}\sqrt m}=m^{1/6}
 =\Theta(\sqrt r).
\tag{7.3}
\]

The proposed `r`-corner mechanism contributes `1`, not `sqrt(r)`.

## 8. Scope and remainder parameters

The **FAIL** verdict covers exactly:

* the repaired full matching (2.5)--(2.7), with either fixed collision endpoint used for repair;
* any `S_(2a)` carrier and any common `K`-type that occurs once, including the explicit growing
  family (3.1)--(3.6);
* its canonical covariant transport coefficient (4.5) and scalar multiples;
* arbitrary scalar or operator-valued outer `UIC_a` adversary coefficients;
* the standard BHK `J_m,mI_m` occurrence blocks;
* all unmasked and physical-query masks, through the exact identities (5.5)--(6.5).

Testing `p=0,u=1` is decisive against a uniform critical-endpoint formula.  For `p>0`, the
repaired outer matching is still defined after choosing the unused outer-palette member in the
presentation, and the exact incidence factor is `1/(C sqrt(u))`.  Long-heavy exclusion variables
would add marked statuses, not remove the identity block (6.5).  No claim about a different
nonfactorizable selector at `p>0` is made.

Outside this memo are:

* a genuine growing Littlewood--Richardson/common-`K` multiplicity space with a non-scalar mixing
  law;
* a nonfactorizable cycle-word or equality-graph coefficient which is not
  `U_1(z_1)^(-1)U_0(z_0)`;
* any joint modification of several occurrence blocks.

The first two have separate Rule-8 nodes.  The last belongs to the already registered
delocalized-multiblock node.

## 9. Gate ledger

| Obligation | Outcome |
|---|---|
| selector comes from actual UIC transition | repaired bijection (2.5)--(2.8) |
| exact selector module | `S^Theta` restricted to `K`, not an assumed regular ancilla |
| common growing address sector | explicit `Lambda=lambda box-times lambda`, multiplicity one |
| `r=Theta(m^(1/3))` removable corners | explicit partition (3.1)--(3.3) |
| row/codomain types | (4.3)--(4.5) |
| preserve outer numerator and outer masks | exact input-wise conjugation (4.7)--(4.10) |
| exact `C/uC` incidence normalization | unchanged by (5.5); factor `1/(C sqrt(u))` |
| physical mask versus branching channels | full marked block is `I_r`, equation (6.5) |
| selector gain `sqrt(r)` | **FAIL; exact gain one** |
| total formula scale | at most `O(a^(2/3)sqrt(m))=O(N^(11/18))` |
| `p=0,u=1` decisive sequence | exact |
| `p>0` | no rescue of this formula; different selectors not tested |
| numerics | none used |

## 10. Bottom line

The representation-content gate passes but the load-balancing gate fails.  A repaired full UIC
matching supplies an explicit common growing Specht sector with the requested number of removable
corners.  Its canonical coefficient, however, is an input-wise change of basis.  Multiplicity-one
Schur contraction turns it into the scalar one, and a physical query retains all removable-corner
branches as an identity direct sum.

Therefore a full matching plus a high Specht label is not yet a coupled adversary.  The first
formula is exactly the selector-free addressed incidence kernel in disguise and cannot provide
the missing `m^(1/6)` factor.
