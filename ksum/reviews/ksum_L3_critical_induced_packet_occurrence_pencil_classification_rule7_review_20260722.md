# Fresh Rule-7 review: induced-packet occurrence-pencil classification

Date: 2026-07-22

Canonical node:

`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Reviewed proposer artifact:

`ksum/artifacts/ksum_L3_critical_induced_packet_occurrence_pencil_classification_20260722.md`

## 1. Hash gate and verdict

| object | claimed SHA-256 | observed SHA-256 | result |
|---|---|---|---|
| proposer artifact | `DBB6D4024473D58D097EA1D16D688B5B213A1AB691C13F3D8B799561432A2AE0` | `DBB6D4024473D58D097EA1D16D688B5B213A1AB691C13F3D8B799561432A2AE0` | exact match |
| structural checker | `6D96E025E3B28E01153CF1813DD859B47F11CDDCD4925F38A3567E7C1AD6A2C9` | `6D96E025E3B28E01153CF1813DD859B47F11CDDCD4925F38A3567E7C1AD6A2C9` | exact match |
| original raw JSON | `8AB84417DB98C52332F13611613F289B656134094D6D4EA1E16BFB3AB65FEF8C` | `8AB84417DB98C52332F13611613F289B656134094D6D4EA1E16BFB3AB65FEF8C` | exact match |
| canonical node | not commissioned as a claimed hash | `144CB090C00FB195059132D03E439049FE723A57066A709912A29881406E7BDE` | recorded only |

The checker was independently rerun as

```text
python ksum/tools/ksum_l3_occurrence_pencil_classification_check.py --output ksum/artifacts/logs_ksum_L3_occurrence_pencil_classification_rule7_review_20260722/run.json
```

It printed `ALL_EXACT_STRUCTURAL_GATES_PASS`.  The fresh JSON has SHA-256
`8AB84417DB98C52332F13611613F289B656134094D6D4EA1E16BFB3AB65FEF8C` and is byte-for-byte equal
to the original raw JSON.

**Overall verdict: MINOR / SCOPED PASS.**

The following proposer-tier statement is independently licensed:

> On the complete, uncompressed induced packet, every same-codomain left marked cross-Gram has
> the untouched right occurrence factor and every right marked cross-Gram has the untouched left
> occurrence factor.  This remains true after assembling all full parents sharing one marked
> child.  The result is a Gram/effect theorem, not a literal-map codomain tensor theorem.  The
> correctly typed cross-answer object is the positive self-adjoint rectangular transfer
> `B -> sum_z F_(1,z)^s B F_(0,z)^s`.  The presently available rows do not decide any physical
> commute/noncommute or simultaneous-diagonalization verdict.

Four local corrections are required.

1. In proposer (8.1), `B` was already defined as a full map
   `B:mathbf E_0 ->mathbf E_1`.  The literal sandwich is therefore
   `ell_(1,z)^s B ell_(0,z)^(s*)`.  The printed `I tensor B` is well typed only if `B` is redefined
   there as a carrier-suppressed multiplicity map.
2. The marked index `b` in (4.1) already contains `z`, while (5.6) separately sums `z` and `b`.
   One must either write `bar b=(chi,beta,tau,gamma)` and sum `(z,bar b)`, or use
   `B_t^s(z)` in the inner sum.  There is no mathematical double counting after this notational
   repair.
3. The reduced marked codomain `mathcal N_(t,z;b)^s`, its dimension, and the branch inclusion
   `I_(t,b)` are only named, not explicitly defined.  The correct full block is
   `I_(S^beta tensor S^lambda tensor S^tau) tensor A_(t,z;b)^s`; the carrier factor multiplies
   every full rank.  The missing numerical marked multiplicities remain an OPEN obligation, as
   the proposer itself states.
4. The checker demonstrates only synthetic tensor/rank and rectangular-transfer inference guards.
   Its hard-coded status inventory is not an independent physical construction, and it does not
   execute (5.6), the physical all-parent cross-Grams, or the transfer commutator (9.7).  Those
   printed formulas are licensed by the analytic derivations below, not by the checker values.

None of these repairs changes the exact stopping point.  Individual physical ranks, kernels,
images, commutators, and simultaneous-diagonalizability relations are not determined.  The
canonical node must remain **OPEN**.

## 2. Rule-7(c) anchoring record

Before reading or grepping the proposer artifact, this reviewer reconstructed the typed system
from the archived packet and coevaluation inputs.  That blind reconstruction found:

* the full occurrence product `Z_L tensor Z_R` and the parent-multiplicity coordinate;
* the matrix-element identities
  `G_L=Ghat_L tensor I_(Z_R)` and `G_R=I_(Z_L) tensor Ghat_R` at Gram/effect level;
* persistence of the untouched Kronecker delta across a full-parent codiagonal;
* the absence of a licensed literal-map tensor factorization without a factored raw codomain;
* the fact that left/right effects still share the packet/parent coordinate, so the tensor law
  alone proves neither commutation nor noncommutation;
* the native cross-answer map `B -> sum_z F_1,z B F_0,z` rather than an undefined NO/YES
  commutator;
* the actual NO/YES by L/R status table, the need to retain residual and private branches, and the
  prohibition on zero-padding unequal ranks;
* the separation among the actual critical `C_r>1` family, a selected/formula-level `c=1` gate,
  the genuine bicovariant `r=2` rank-one case outside the critical family, the older one-cell
  `g_2=0` absence, and the alphabet-only `a=2` degeneration.

Only after that reconstruction was frozen in a report to the commissioning agent did this reviewer
open the proposer.  The proposer's central conclusions (1.1)--(1.2), status inventory, and stopping
point agree with the blind reconstruction.  The notation `Z_L,Z_R`, `A`, `G`, and the words
`singleton/residual` are project-standard and therefore coincident; the blind derivation did not
obtain them from the proposer.  The local (8.1) type issue and the `(z,b)` indexing ambiguity were
noticed only on comparison and are reported rather than silently normalized away.

## 3. Independent source and dimension reconstruction

Write

\[
c=C_r=\dim Z,
\qquad
d_t^{\rm pkt}=\dim M_t,
\qquad
d_1^{\rm pkt}=a^2d_0^{\rm pkt},
\]

where

\[
d_0^{\rm pkt}=\frac{(4a)!}{(a!)^4}(a-1)^2.
\]

For one alphabet full type `nu`, the selected full source block has dimension

\[
k_{t,\nu}=(f^\lambda)^2f^\nu m_{t,\nu}c^2.
\tag{R3.1}
\]

Frobenius reciprocity gives
`sum_nu f^nu m_(t,nu)=d_t^pkt`, hence

\[
\dim\mathbf E_t=(f^\lambda)^2c^2d_t^{\rm pkt},
\qquad
\dim\mathbf E_1=a^2\dim\mathbf E_0.
\tag{R3.2}
\]

Thus the physical orientation maps embed the whole NO selected packet into a strictly larger YES
selected packet.  The unmatched YES complement has dimension
`(a^2-1) dim bold E_0`; it is not a zero-padded NO space.  A marked projector need not reduce the
common image, so a pullback `J_o^*F_1J_o` is a compression and does not classify leakage into that
complement.

For a marked branch, let

\[
P_{t,b}=\{\nu:\tau\nearrow\nu\text{ and the deterministic coupling is nonzero}\},
\qquad
d_{t,b}=c^2\sum_{\nu\in P_{t,b}}m_{t,\nu}.
\tag{R3.3}
\]

Let `n_(t,z;b)^s=dim mathcal N_(t,z;b)^s`, which is not presently evaluated, and put

\[
g_{s,b}=f^\beta f^\lambda f^\tau.
\tag{R3.4}
\]

Then the reduced row is an `n_(t,z;b)^s by d_(t,b)` matrix.  Restoring carriers gives

\[
I_{S^\beta\otimes S^\lambda\otimes S^\tau}\otimes A_{t,z;b}^s:
\mathbb C^{g_{s,b}d_{t,b}}longrightarrow
\mathbb C^{g_{s,b}n_{t,z;b}^s},
\tag{R3.5}
\]

with left/right order exchanged as in proposer (4.4).  Consequently the full block rank is
`g_(s,b) rank(A_(t,z;b)^s)`, whereas proposer (5.5) correctly states the carrier-suppressed rank.

For same-codomain rows `b,b'`, the cross-Gram has type

\[
(A_{t,z;b}^s)^*A_{t,z;b'}^s:
\mathbb C^{d_{t,b'}}\longrightarrow\mathbb C^{d_{t,b}}.
\tag{R3.6}
\]

It can be rectangular.  It is an endomorphism and positive only when `b=b'` (or after assembling a
single row on the direct sum).  This distinction is required before asking for a commutator.

## 4. Rule-7(a): display-by-display type and identity audit

### 4.1 Verdict and unmarked-source displays

| display | independent audit |
|---|---|
| (1.1) | **PASS in the stated same-codomain, uncompressed scope.**  The hatted left block maps `(packet,parent) tensor Z_L` to its possibly different same-child counterpart and is tensored with `I_(Z_R)`; the right formula is the mirror.  Cross-Grams may be rectangular. |
| (1.2) | **PASS.**  If `k_t=dim bold E_t`, then `F_(1,z)^s` is `k_1 by k_1`, `B` is `k_1 by k_0`, and `F_(0,z)^s` is `k_0 by k_0`; every summand and the sum are `k_1 by k_0`. |
| (2.1)--(2.4) | **PASS on the printed stability range.**  `D=a-1`; each `T_h:S^(a-1,1)->S^theta` is `f^theta by D`, and Schur normalization gives `T_h^*T_k=delta_(hk)I_D`.  The coefficient formula requires `a>=r+1`, `d>=r`, and `ad>=2r+1`, all satisfied by (3.1). |
| (2.5) | **PASS.**  `Y_(t,nu)` is the multiplicity space of the irreducible `H_t`-module `tau_t` in `Res S^nu`; its dimension is `m_(t,nu)`. |
| (2.6) | **PASS after the order-defined identification of the two heavy standards.**  Each `Phi_(t,nu,alpha)` is an `f^nu by D^2` isometric `H_t`-intertwiner.  Orthogonal copies may be normalized so `Phi_alpha^*Phi_alpha'=delta I_(D^2)`. |
| (2.7)--(2.8a) | **PASS.**  Per-type and total dimensions are (R3.1)--(R3.2).  `mathcal E_t` is multiplicity-only; `bold E_t=mathcal K_t` retains carriers. |
| (2.9) | **PASS.**  The sum has `D^2` terms.  Applying (2.4) on both position factors and (2.6) on the alphabet factor gives `D^2/D^2=1`; hence the coefficient is `1/D`, not `1/sqrt D`. |
| (2.10) | **PASS.**  The `nu` block has target dimension `(f^lambda)^2f^nu m_(1,nu)c^2` and source dimension `(f^lambda)^2f^nu m_(0,nu)c^2`; `j_(o,nu)` is rectangular isometric and the occurrence identities are square. |
| (2.11) | **PASS with suppressed position identities understood.**  `K` acts on the full NO alphabet packet `direct-sum_nu S^nu tensor Y_(0,nu)`; the two position carrier identities and both occurrence identities are passive.  If the orientations use different external occurrence maps, the factor is `R_L^*R_R`, not `I`. |
| (3.1) | **PASS.**  `a=s^2,d=4s+1,r=s,s>=4` obeys all coefficient and three-row stability inequalities. |

### 4.2 Regime and marked-index displays

| display | independent audit |
|---|---|
| (4.1) | **PASS after the `(z,b)` notation correction.**  The full row label is `(s,z,chi,beta,tau,gamma)`.  Later sums should use `bar b=(chi,beta,tau,gamma)` at fixed `(s,z)`. |
| (4.2) | **PASS for the actual `r>=4` family.**  Removing a box from rows 1, 2, or 3 of `lambda=(n-r-1,r,1)` gives exactly `beta_T,beta_M,beta_B`.  This lists possible ordered children; it does not assert that every status/path coupling to every child is nonzero. |
| (4.3) | **PASS.**  The dimension is `d_(t,b)` from (R3.3).  All parents reaching the same physical `tau` are columns of one row, so no output parent superselection is inserted. |
| (4.4) | **PASS.**  The left carrier is `S^beta_L tensor S^lambda_R tensor S^tau`, the right carrier reverses the first two factors, and each has dimension `g_(s,b)` in (R3.4). |

### 4.3 Literal rows, Grams, and completeness

| display | independent audit |
|---|---|
| (5.1) | **PASS.**  `mathcal J_t:bold E_t->X_t` and `Ref_t^s:X_t->X_t^(s,#)` are isometries; `D_(t,z)^s` is a projection.  Thus `ell_(t,z)^s:bold E_t->mathscr R_(t,z)^s` is rectangular and contractive. |
| (5.2) | **MINOR clarification.**  The reduced row is well defined as the matrix of (5.1) in deterministic unmarked and marked bases, with dimensions `n_(t,z;b)^s by d_(t,b)`.  The proposer does not construct `mathcal N`, its basis, or its numerical dimension; this is precisely the remaining physical-row obligation. |
| (5.3) | **PASS only for rows with literally the same target Hilbert space.**  Its type is (R3.6).  Sharing only an abstract dimension or a child name without a fixed target identification is insufficient. |
| (5.4) | **PASS.**  `Q=A^*A` is a `d_(t,b) by d_(t,b)` positive contraction. |
| (5.5) | **PASS in finite dimension.**  `rank A=rank A^*A`, the kernels agree, `im(A^*A)=(ker A)^perp`, and `im A=A[(ker A)^perp]`.  Restoring carriers multiplies ranks by `g_(s,b)`. |
| (5.6) | **PASS as a formal consequence of a complete marked orthogonal decomposition, with the `(z,b)` and `I_(t,b)` repairs.**  Directly, `sum_z ell_z^*ell_z=J_t^*Ref_t^(s*)Ref_t^sJ_t=I`.  Decomposing every marked carrier and multiplicity row gives the displayed resolution.  The checker does not construct or verify these physical rows. |

### 4.4 Untouched-factor and mass displays

| display | independent audit |
|---|---|
| (6.1)--(6.2) | **PASS analytically for every cross-Gram with a common codomain.**  In a left row, the marked operation is identity on the right position carrier.  Contracting the right coevaluation gives `T_k^*T_k'=delta_(kk')I_D`, leaving exactly `delta_(kk')`; the right-side proof is the mirror.  The argument is independent of `nu,nu'`, so cross-parent codiagonal terms are included. |
| (6.3) | **PASS for the complete uncompressed product.**  The packet/parent coordinate belongs to the hatted active factor on both sides, so this formula alone gives no left/right commutation theorem. |
| (6.4) | **PASS for genuine singleton/residual attachment rows.**  Neither heavy block is marked, so both occurrence Hom indices are passive.  This is not a statement about a heavy row or an arbitrary entangled selected compression. |
| (6.5) | **PASS.**  For `c_R=dim Z_R`, standard tensor algebra gives `rank(Qhat tensor I)=c_R rank Qhat`, `ker=(ker Qhat) tensor Z_R`, and the analogous image formula.  The singleton/residual specialization multiplies by `c^2`. |
| (7.1) | **PASS as an aggregate alphabet-packet identity.**  Direct refinement counting gives masses `1/a` and `(a-1)/a`; the two fine literal targets are orthogonal and sum to the coarse cell effect.  The formula is not an individual position/point-child scalar law. |
| (7.2) | **PASS by exact coordinate counting.**  Per queried side, NO has `a` singleton and `ad` heavy positions; YES has `1` common, `a-1` residual, and `ad` heavy positions out of `n=a(d+1)`.  The listed masses sum to one for each answer. |

### 4.5 Literal/effect transfer displays

| display | independent audit |
|---|---|
| (8.1) | **MINOR type correction.**  With the printed full-map definition `B:bold E_0->bold E_1`, the typed formula is `ell_(1,z)^s B ell_(0,z)^(s*)`.  Retain `I tensor B` only after redefining `B` as a multiplicity-only block.  The corrected map is `mathscr R_(0,z)^s->mathscr R_(1,z)^s`. |
| (8.2) | **PASS.**  `F_(1,z)^s B F_(0,z)^s` is a full-source effect sandwich, not the literal map in (8.1).  Polar partial isometries are needed to return to literal codomains. |
| (8.3) | **PASS.**  Unmarked equivariance forces a direct sum over equal `nu`; `B_nu` has dimensions `m_(1,nu)c^2 by m_(0,nu)c^2`, with the full carrier identity restored.  There is no unmarked map between inequivalent `S_q` types. |
| (8.4) | **PASS for unequal ranks.**  The rectangular Hilbert--Schmidt space has complex dimension `k_1k_0`; no zero padding occurs.  The full transfer restricts to the equivariant block subspace when `B` is physical. |
| (8.5) | **PASS by formula, not merely by the checker value.**  For arbitrary rectangular `B`, cyclicity of trace gives the stated square norm.  For arbitrary `B,C`, `Tr(C^*F_1BF_0)=Tr((F_1CF_0)^*B)`, proving self-adjointness.  Here “positive” means a positive operator on Hilbert--Schmidt space; rectangular matrices themselves have no PSD order. |
| (8.6) | **PASS under the standard column-vectorization convention.**  `vec(F_1BF_0)=(F_0^T tensor F_1)vec(B)`.  The matrix is `k_1k_0 by k_1k_0`, Hermitian positive because `F_0^T=bar F_0` and `F_1` are positive. |

### 4.6 Commutator and Johnson displays

| display | independent audit |
|---|---|
| (9.1)--(9.2) | **PASS.**  Multiplying the two kernels and summing the intermediate occurrence labels forces the printed order.  The common packet index `u` remains active in both factors and can generate a nonzero commutator. |
| (9.3)--(9.4) | **PASS.**  NO and YES effects lie in different endomorphism algebras.  A commutator is defined only after choosing one physical orientation embedding and compressing YES back to NO. |
| (9.5) | **PASS for exactly the stated common subspace.**  `R_t^*F_tR_t` are endomorphisms of `U`; unmatched components remain outside the claim and may not be zero padded. |
| (9.6) | **PASS provided `R_L,R_R` have one common domain and codomain.**  The orientation cross-Gram is `K tensor R_L^*R_R`; it is `K tensor I` only for one common occurrence isometry. |
| (9.7) | **PASS; both multiplication orders are correct.**  Expanding `E_L(E_R(B))` gives `F_1,z^L F_1,w^R B F_0,w^R F_0,z^L`; expanding `E_R(E_L(B))` gives the second printed order.  Since both transfers are self-adjoint, they are simultaneously unitarily diagonalizable exactly when this superoperator commutator vanishes.  The checker does not execute this identity on physical or synthetic L/R POVMs. |
| (10.1) | **PASS.**  On `J(2a,a)`, there are `a^2` one-swap neighbors and coefficient `1/a^2`. |
| (10.2) | **PASS for every `a>=2`.**  If `z in A`, the edge `A -> A-z+u` crosses the `P_z` support boundary with coefficient `1/a^2`, so `[K,P_z]` is nonzero.  This rules out one global Johnson/raw-status eigenbasis but does not prove a nonzero physical occurrence-pencil commutator. |

## 5. Rule-7(b): regime-complete identity gates

| required regime | independent result |
|---|---|
| actual critical family | For `s>=4`, `a=s^2,d=4s+1,r=s`, all stability inequalities hold, `C_r>1`, and the uncompressed occurrence rank is `C_r^2`.  The factorization proof is symbolic in `C_r`; no finite sample establishes its growth. **PASS.** |
| genuine bicovariant `c=1` | At `r=2`, `C_2=1`; the two-covariant construction is stable when `a>=3,d>=2`.  It is outside the critical family.  Every occurrence factor is scalar, but the packet/parent algebra can still be nontrivial. **PASS as a separate feasible regime.** |
| selected/formal `c=1` | A one-dimensional compression inside actual `C_r^2>1` is algebraically legal.  It is not the complete critical occurrence and an entangled compression need not preserve (6.3). **PASS with this scope.** |
| older one-cell rank one | That different construction additionally requires a wreath-invariant opposite vector; `g_2=0`, so its physical `r=2` realization is absent.  It does not contradict the bicovariant row above. **Correctly separated.** |
| `c>=2` and unequal selected ranks | Literal rows and `F_1BF_0` remain rectangular.  The untouched-factor theorem is licensed only before arbitrary entangled compression; no zero padding or common unitary is used. **PASS.** |
| NO versus YES | `dim bold E_1=a^2 dim bold E_0`; all `Y_(1,nu)` columns, including the unmatched YES complement, are in the complete YES source.  Pullback by `J_o` classifies only the common image and can miss marked leakage. **PASS with this explicit complement qualification.** |
| left versus right | The coevaluation proof is mirrored and ordered carrier tags differ.  Literal codomains and top polar carriers are not identified. **PASS.** |
| singleton versus residual | Both are mandatory actual rows; their aggregate alphabet masses are `1/a` and `(a-1)/a`, and both occurrence factors are passive.  The checker only hard-codes their names/masses. **PASS analytically.** |
| heavy top/other | `beta_T,beta_M,beta_B` are all possible Young children and every nonzero `gamma` row must be retained.  Existing sources provide a top aggregate bound but not all physical rows. **PASS as an inventory; numerical pencils remain OPEN.** |
| common/private point children | Every `tau` is retained, and all `nu` sharing `tau` enter one row.  A private child is physical rather than discarded.  Complete common/private cross-Grams are not yet constructed. **PASS as typing; values remain OPEN.** |
| YES complement | It is included through all `Y_(1,nu)`, is not an orthogonal post-query superselection sector, and is not controlled by padding NO with zeros. **PASS after the explicit qualification above.** |
| `a=2` | `V_2 tensor V_2` is one-dimensional and singleton/residual masses are both `1/2`, but `a>=r+1` fails for every three-row `r>=2`.  This is an alphabet-only exact gate and proves no physical three-row scalar pencil. **Correct infeasibility gate.** |

The commissioned status inventory is therefore complete at the cell level:

| answer/side | nonzero queried statuses | zero or opposite-side statuses |
|---|---|---|
| NO/L | `A,H_L` | `B,H_R` |
| NO/R | `B,H_R` | `A,H_L` |
| YES/L | `C,L,H_L` | `U,R,H_R` |
| YES/R | `C,R,H_R` | `U,L,H_L` |

This table does not replace the independent `beta`, `tau`, and `gamma` refinements.

## 6. Rectangular Hilbert--Schmidt transfer and superoperator order

Because this point was specifically commissioned, here is the derivation without assuming real,
diagonal, square, or commuting effects.  Let

\[
F_{0,z}\succeq0\text{ on }\mathbb C^{k_0},
\qquad
F_{1,z}\succeq0\text{ on }\mathbb C^{k_1},
\qquad
B,C\in\mathbb C^{k_1\times k_0}.
\]

Then

\[
\begin{aligned}
\langle B,\mathcal E_s(B)\rangle_{HS}
&=\sum_z\operatorname{Tr}(B^*F_{1,z}BF_{0,z})\\
&=\sum_z\|F_{1,z}^{1/2}BF_{0,z}^{1/2}\|_{HS}^2\ge0,
\end{aligned}
\tag{R6.1}
\]

and

\[
\begin{aligned}
\langle C,\mathcal E_s(B)\rangle_{HS}
&=\sum_z\operatorname{Tr}(C^*F_{1,z}BF_{0,z})\\
&=\sum_z\operatorname{Tr}((F_{1,z}CF_{0,z})^*B)
=\langle\mathcal E_s(C),B\rangle_{HS}.
\end{aligned}
\tag{R6.2}
\]

Thus `mathcal E_s` is genuinely positive self-adjoint on the rectangular Hilbert--Schmidt space.
No NO/YES identification is used.

For the L/R commutator,

\[
\begin{aligned}
\mathcal E_L\mathcal E_R(B)
&=\sum_{z,w}F_{1,z}^LF_{1,w}^R B F_{0,w}^RF_{0,z}^L,\\
\mathcal E_R\mathcal E_L(B)
&=\sum_{z,w}F_{1,w}^RF_{1,z}^L B F_{0,z}^LF_{0,w}^R.
\end{aligned}
\tag{R6.3}
\]

This exactly confirms proposer (9.7).  Notice that the right-side source effects occur in reverse
composition order because they multiply `B` from the right.  Replacing either line by the same
right order would be an error; the proposer does not make that error.

## 7. Rule-7(d): reopening every cited input

All six cited source hashes were independently checked and match the proposer ledger.

| cited source | scope used by proposer | independent reopening in this review | what remains frozen / not extrapolated |
|---|---|---|---|
| induced-packet first gate, SHA `047CA5...CC59` | `M_0,M_1`, `J_L,J_R`, Johnson `K`, cell masses | Recomputed dimensions, unique-coarsening isometries, the `a^2` rank ratio, and the cell refinements.  Rechecked that the heavy fibers are unchanged and that point restriction is not full-parent diagonal. | The exact subgroup-induced modules and reviewed Johnson spectrum are accepted in their `p=0,u=1,q=4a` scope only.  They do not contain physical occurrence rows. |
| induced-packet fresh review, SHA `CF1E85...1F2` | all multiplicities and external occurrence caution | Reopened the all-`nu` decomposition and verified that `j_(o,nu)` is rectangular isometric for every multiplicity.  Reused its warning that different occurrence embeddings give `R_L^*R_R`. | Its passive external tensor statement is not treated as proof of the new coevaluation cross-Grams. |
| block-standard proposer/review, SHAs `3FE61B...B0DD` and `6731D...8F1AF` | `C_r`, `T_h`, stability, position restriction | Rechecked the exact stability inequalities, Hom normalization, and `T_h^*T_k`.  Independently enumerated the three removable-box predecessors of `lambda`. | The prior theorem supplies only the top aggregate Gram and, in its one-cell construction, needs `g_r`.  It does not supply all three physical marked rows and its `g_2=0` conclusion is not transferred to the two-covariant construction. |
| bicovariant two-cell review, SHA `2FE6AE...BEB6A` | double coevaluation and `C_r^2` | Recomputed the `1/D` normalization and orthonormality.  Extended the contraction to arbitrary parent intertwiners `Phi, Phi'`: the untouched `T_k^*T_k'` delta survives even for cross-parent Grams. | Its licensed theorem is fixed-full-type.  No fixed-type point coefficient or obstruction is extrapolated to the complete packet. |
| mixed two-box review, SHA `0D6AA6...9506` | common/private codiagonal and rectangular precedent | Rebuilt the row-map rule `L_p^*L_p'` for arbitrary unequal domains and confirmed why all parents sharing one target must be columns of a common row. | Its two-parent masses, phases, and norm obstruction remain frozen to those two full types and are not used here. |

The genuinely wider claims in this proposer--all parents, all multiplicities, and all cross-Grams--
are therefore supported by the new arbitrary-`Phi` contraction, not by declaring an earlier
fixed-type review immune from rechecking.

## 8. Rule-7(e): standing failure-mode attacks

| attack | result |
|---|---|
| dropped/extra normalization | `1/D` is correct for two coevaluations; `1/sqrt D` would fail.  Aggregate masses and all `q` raw values are retained.  The only repair is the `(z,b)` indexing ambiguity in (5.6). |
| type/dimension mismatch | Core maps are typed by (R3.1)--(R3.6).  The printed `I tensor B` in (8.1) conflicts with the full-map definition of `B` and must be removed or locally redefined.  The uncomputed `n_(t,z;b)^s` is an acknowledged open datum, not a fabricated equal rank. |
| undefined terminology/stability | The critical family, actual/uncompressed versus selected `c=1`, `a=2`, complete packet, common/private, and same-codomain cross-Gram are resolved in Sections 3, 5, and 10 below. |
| colored-orbit sum substituted for a full raw sum | The mathematical normalization uses every raw `z` and every compatible branch.  No one-color or top-only sum is used.  The checker does not verify this physical completeness. |
| code checks values while derivation is broken | The checker is correctly labelled synthetic, but its `proved_by_gates` wording is broader than its execution for the physical factor theorem.  Formula-level proofs in Sections 4 and 6, not the sample values, license the result. |
| literal/effect/polar confusion | The four levels are correctly separated.  The local `(8.1)` identity-factor typo does not identify literal and effect sandwiches; the proposer explicitly preserves the polar maps as future obligations. |
| false parent superselection | **PASS.**  Every parent reaching one `tau` is in a common row.  Ordered parent labels remain source matrix indices, not orthogonal output tags. |
| private/residual/status deletion | **PASS as inventory.**  Residual cells, private point children, other position predecessors, and heavy paths are mandatory.  Their matrices remain missing and no numerical conclusion is drawn. |
| illegal cross-irrep map | **PASS.**  Unmarked `B` is block diagonal in `nu`; only marked restriction produces cross-parent Gram blocks sharing a child. |
| unequal-rank padding | **PASS.**  The native transfer acts on `Hom(bold E_0,bold E_1)`, while common-source comparisons use explicit isometries.  YES complement is not replaced by zeros. |
| finite-to-asymptotic inference | **PASS.**  Johnson `a=2,3` and critical `s=4,5,6` values are corroboration only.  No uniform physical commutator, attenuation, or exponent is inferred. |
| answer-dependent basis alignment | **PASS.**  Deterministic bases are fixed; coherent changes conjugate an already chosen pullback, while changing physical orientation is not called a gauge. |

## 9. Rule-7(f): value-versus-formula decoupling

| claim | actual verification mode | license |
|---|---|---|
| Johnson spectrum at `a=2,3` | checker constructs exact finite matrices | values corroborate the archived all-`a` spectrum; they do not prove it |
| `[K,P_z]!=0` for all `a>=2` | independent one-edge formula (10.1)--(10.2); checker gives two finite instances | printed formula and all-parameter derivation verified |
| double-coevaluation normalization | direct inner-product calculation using arbitrary `T_h,Phi_alpha` | printed formula verified; no code dependence |
| all-parent untouched-factor theorem | arbitrary-parent matrix-element contraction | new operator-level derivation verified; checker synthetic tensor example is only an inference guard |
| tensor rank/kernel rules | exact finite-dimensional tensor algebra; checker gives one rational instance | printed formulas verified analytically |
| status inventory | independent physical side-multiplicity table | inventory verified analytically; checker merely asserts the same list |
| singleton/residual/heavy masses | exact position and alphabet counting | printed formulas verified; checker records only alphabet masses |
| completeness resolution (5.6) | isometry/projector identity plus exhaustive branch decomposition | formula verified conditionally on the declared complete row inventory; physical row values not checked |
| rectangular HS positivity/self-adjointness | general trace proof (R6.1)--(R6.2); checker uses one real diagonal sample | printed formula verified for arbitrary complex PSD effects and unequal ranks |
| transfer commutator (9.7) | direct symbolic composition (R6.3) | printed order verified; checker does not test it |
| physical ranks/commutators | no matrices exist | **not verified and not claimed** |

## 10. Rule-7(g): quantifier and terminology hygiene

* **Complete packet:** every `nu` with `m_(t,nu)>0`, every alphabet occurrence
  `alpha=1,...,m_(t,nu)`, and every `(h,k) in Z_L tensor Z_R`; not one full type, Johnson degree,
  or selected occurrence copy.
* **Complete common packet:** the whole NO source embedded by one fixed physical orientation into
  YES.  It does not mean equality of full NO/YES ranks and does not include the unmatched YES
  complement in a common unitary.
* **All cross-Grams:** every pair of literal rows with one explicitly identical physical marked
  codomain.  It does not authorize multiplying rows whose targets merely have equal dimensions or
  similarly named children.
* **Common codomain:** one fixed side, raw value, ordered position child, alphabet child, cell/path
  sector, and deterministic marked multiplicity realization.  All unmarked parents feeding it are
  codiagonal columns.
* **Actual status:** a cell type occurring at the queried coordinate on that answer and side.  `U`
  and opposite-side-only cells are zero sectors, not decorative rows.
* **Common/private point child:** a statement about how many selected `S_q` parents reach one
  `S_(q-1)` child.  It is unrelated to singleton/residual cell splitting or the YES unmarked
  complement.
* **Critical family:** exactly `a=s^2,d=4s+1,r=s,s>=4`; only there are critical asymptotic words
  used.
* **`c=1`:** must be qualified as genuine uncompressed bicovariant `r=2`, a selected one-dimensional
  compression, or the infeasible older one-cell construction.  These are not interchangeable.
* **`c>1`:** the actual critical ambient occurrence is `C_r^2`; arbitrary unequal selected ranks
  are separate compressions and may erase the visible tensor product.
* **Simultaneous diagonalization:** applies only to a family of normal endomorphisms on one fixed
  Hilbert space.  It applies to same-answer positive effects, orientation-pulled compressions, or
  the positive transfer superoperators after their spaces are fixed; it does not apply to literal
  rectangular rows or unpulled NO/YES effects.
* **Positive rectangular transfer:** positivity is Hilbert-space positivity of the superoperator
  on `Hom(bold E_0,bold E_1)`, not a PSD-preserving order on rectangular matrices.

## 11. Checker audit

The checker is deterministic, exact, and its rerun is reproducible.  Its claims must nevertheless
be read at the granularity of its code.

* `johnson_gate` constructs the complete `J(2a,a)` walk only for `a=2,3`, checks the exact finite
  spectrum, and finds a nonzero raw-status commutator.  The all-`a` result comes from (10.1), not
  extrapolation.
* `gram_tensor_and_commutator_gate` uses labelled synthetic packet dimensions `(2,2,3)`.  It
  correctly proves that untouched-factor forms can commute or fail to commute depending on their
  shared packet action.  It is not a physical row calculation.
* `rectangular_transfer_gate` checks one real diagonal pair with ranks `3` and `5`.  It correctly
  verifies shape, one positive self-adjoint vectorization, pullback dependence, and coherent-gauge
  invariance.  The general complex statement is instead proved in Section 6.
* `status_inventory_gate` compares hard-coded lists.  It is a regression assertion, not an
  independent orbit construction.
* `regime_gate` checks finite partition-number samples.  It correctly separates the regimes but
  proves no asymptotic statement.
* The checker does not construct `Phi`, `A_(t,z;b)^s`, `mathcal N_(t,z;b)^s`, common/private
  leakage rows, the resolution (5.6), any physical occurrence commutator, or (9.7).

The JSON and terminal success line are therefore valid evidence for the explicitly labelled
structural inference guards, not completion-tier evidence for the canonical classification.

## 12. Exact licensed scope and stopping point

The review confirms the proposer's stopping point.

Banked:

1. the complete deterministic unmarked source and its exact dimensions;
2. the full actual cell-status and parent/child/path index inventory;
3. all-parent Gram/effect untouched-factor identities on the complete uncompressed occurrence
   product;
4. the rank/kernel/image consequences that follow formally from those identities;
5. exact aggregate singleton/residual/heavy masses;
6. the distinction among literal rows, source effects, literal sandwiches, and effect transfers;
7. the positive self-adjoint rectangular NO-to-YES transfer and the correctly ordered L/R
   superoperator commutator;
8. the exact Johnson/raw-status noncommutation warning.

Not banked:

1. a common tensor factorization of the literal raw codomains or literal maps;
2. the complete deterministic marked row matrices;
3. numerical physical ranks, kernels, images, or leakage blocks;
4. any physical same-side, cross-side, pulled cross-answer, or transfer commute/noncommute verdict;
5. simultaneous diagonalizability on the critical family;
6. a scalar resolvent, noncommuting Sylvester premise, rectangular resolvent value, query
   attenuation, coefficient norm, incidence, remainder, numerator, or lower bound.

Accordingly the partial proposer classification receives **MINOR / SCOPED PASS**, while the
canonical node remains **OPEN**.  Neither the scalar total-energy successor nor the conditional
noncommuting Sylvester successor is activated.  The rectangular-transfer successor has a valid
input type only; no feasibility statement follows.
