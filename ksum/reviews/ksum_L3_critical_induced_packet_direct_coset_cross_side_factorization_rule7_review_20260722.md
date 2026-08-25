# Fresh Rule-7 review: direct-coset cross-side factorization

Date: 2026-07-22

Canonical node:

`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Reviewed proposer artifact:

`ksum/artifacts/ksum_L3_critical_induced_packet_direct_coset_cross_side_factorization_20260722.md`

## 1. Hash gate and verdict

| object | claimed SHA-256 | observed SHA-256 | result |
|---|---|---|---|
| proposer artifact | `66A16A7A414814535D6EB49B6B667FAC3C8B3EA7C15D8097BE9A9C4827743AAD` | `66A16A7A414814535D6EB49B6B667FAC3C8B3EA7C15D8097BE9A9C4827743AAD` | exact match |
| canonical node, read only | not commissioned as a claimed hash | `26D8D24CA32486E9F63EC93F0A65A98E9A39FCEBC7EA5502362CA5C32BF5C050` | recorded; not edited |

An independent exact inference-guard checker was created at

`ksum/tools/ksum_l3_direct_coset_cross_side_rule7_check.py`

with SHA-256 `A1AB28656C147EFEE01AF5074DFFCC51F4AB9D7A6920A0A7716067EAF207A0B1`.
It was run as

```text
python ksum/tools/ksum_l3_direct_coset_cross_side_rule7_check.py --output ksum/artifacts/logs_ksum_L3_direct_coset_cross_side_rule7_review_20260722/run.json
```

and printed `ALL_DIRECT_COSET_RULE7_GATES_PASS`.  The fresh JSON has SHA-256
`FD3A6F672841EA0F367F6DBEEFC268CF45D5F1C6D13BA4BFC3535F2290ABB873`.

**Overall verdict: MINOR / SCOPED PASS.**

The core new theorem is correct:

> For the complete induced packet, including all NO and YES alphabet multiplicities and the full
> YES complement of either orientation image, the canonical selected raw projection is the
> fiberwise product
> `P_t=direct-sum_xi P_(t,L)(xi) tensor P_(t,R)(xi)`.  Every raw query preserves `xi` and acts on
> one marginal.  Hence, within either answer, every aggregate left raw-value source effect
> commutes with every aggregate right raw-value source effect, for all coordinates and all raw
> values.  Consequently the two native rectangular transfer superoperators commute exactly.

This theorem supplies physical information that the earlier untouched-factor Gram identities did
not contain.  It is not a consequence of the abstract formulas
`G_L=Ghat_L tensor I_R`, `G_R=I_L tensor Ghat_R`; it follows from complete induced-module Fourier
inversion in the physical cell basis.

Three local corrections/clarifications are required.

1. **Range equality is not rank equality.**  An equivariant isometry and equal rank do not by
   themselves identify a canonical selected range when multiplicities are present.  The proof of
   proposer (3.5) is valid because the local product map and the existing Fourier selected map are
   induced from the *same reference `H_t`-intertwiner*, namely the tensor (3.4).  The universal
   property of induction first identifies the maps/ranges; the rank identity (3.4c) then proves
   that no selected sector is missing.  This load-bearing order should be stated explicitly.
2. Proposer (4.3) contains the malformed fragment `ight)` where `\right)` was intended, and (8.1)
   contains `\!left` where `\!\left` was intended.  The operator identities themselves are
   unambiguous and correct.
3. In (6.2), the multiplier is written in `Hom(E_0,E_1)` although (6.1) and the prior
   classification use the full spaces `bold E_t`.  Read it consistently as
   `B in Hom(bold E_0,bold E_1)` unless all carriers have first been explicitly suppressed.

These are MINOR repairs.  They do not weaken the aggregate cross-side or native-transfer
commutation theorem.

The canonical classification node nevertheless remains **OPEN**.  Same-side pointed occurrence
matrices, their ranks and spectra, orientation-dependent pullbacks, and all downstream coefficient,
attenuation, incidence, numerator, and exponent obligations remain unresolved.

## 2. Rule-7(c) anchoring record

Before opening or grepping the proposer artifact, this reviewer froze the following hostile
baseline.

Let the raw orbit have a cell-fiber decomposition

\[
\mathbb C[X_t]=\bigoplus_\xi\mathbb C[\Omega_{t,L}(\xi)]
                    \otimes\mathbb C[\Omega_{t,R}(\xi)].
\]

If, and only if, the *canonical* selected projection is proved to be

\[
P_t=\bigoplus_\xi P_{t,L}(\xi)\otimes P_{t,R}(\xi),
\tag{R2.1}
\]

then a left raw predicate and right raw predicate compress as

\[
\begin{aligned}
P_tM^L P_t|_{\operatorname{im}P_t}
 &=\bigoplus_\xi(P_LM^LP_L)\otimes I_{\mathcal L_R},\\
P_tM^R P_t|_{\operatorname{im}P_t}
 &=\bigoplus_\xi I_{\mathcal L_L}\otimes(P_RM^RP_R),
\end{aligned}
\tag{R2.2}
\]

and therefore commute.  No assumption that `M^s` preserves a local selected range is needed.

The blind derivation also recorded five failure guards.

* Equivariance plus rank equality can select a different same-rank multiplicity subspace; an
  explicit range/map identification is mandatory.
* A common `S_q` action can permute `xi` fibers, but it does not invalidate (R2.1) if the family of
  product projectors is covariant and every raw query preserves `xi`.
* A full-type pinch or any other nonproduct compression can destroy commutation.
* Commuting full YES effects can acquire a nonzero commutator after compression through a
  nonreducing orientation image.
* Same-`z` central point-child refinements may inherit commutation, whereas point-child projectors
  attached to different raw marks belong to different stabilizers and require no such conclusion.

This baseline was sent to the commissioning agent before the proposer was opened.  On comparison,
the proposer addresses every essential guard: it constructs the fixed-`xi` product, identifies the
reference inducing tensor, includes all of `M_1`, keeps the two local projectors in `PMP`, limits
point-child refinements to a common raw mark, and explicitly excludes orientation pullbacks and
same-side commutation.  The notation `xi`, `P_t`, `M^s`, and `F^s` is project-standard; coincident
notation was not obtained from the proposer.

## 3. Independent physical reconstruction and dimensions

Put

\[
W_{a,d}:=\frac{n!}{(d!)^a},
\qquad n=a(d+1),
\qquad D=a-1,
\qquad C=C_r.
\tag{R3.1}
\]

For every fixed palette partition `xi`, either marginal word set has size `W_(a,d)`: there are `a`
distinct rare labels occurring once and `a` heavy labels occurring `d` times.  Once `xi` is fixed,
the two position words are independent.  Therefore

\[
|\Omega_t(\xi)|=W_{a,d}^2.
\tag{R3.2}
\]

The palette-partition counts are

\[
|\Xi_0|=\frac{q!}{(a!)^4},
\qquad
|\Xi_1|=\frac{q!}{((a-1)!)^2(a!)^2}=a^2|\Xi_0|,
\tag{R3.3}
\]

so

\[
\dim\mathbb C[X_t]=|\Xi_t|W_{a,d}^2.
\tag{R3.4}
\]

For one side and one `xi`, the complete local covariant selected range is

\[
\mathcal L_{t,s}(\xi)\cong S^\lambda\otimes V(H_s)\otimes Z_s,
\qquad
\ell:=\dim\mathcal L_{t,s}(\xi)=f^\lambda DC.
\tag{R3.5}
\]

Hence the direct-coset product projection has rank

\[
k_t:=|\Xi_t|\ell^2
   =(f^\lambda)^2|\Xi_t|D^2C^2
   =(f^\lambda)^2\dim(M_t)C^2.
\tag{R3.6}
\]

This is exactly the dimension of the previously reviewed complete Fourier source

\[
\bigoplus_{\nu\vdash q}
(S^\lambda_L\otimes S^\lambda_R\otimes S^\nu)
\otimes(Y_{t,\nu}\otimes Z_L\otimes Z_R).
\tag{R3.7}
\]

In particular,

\[
k_1=a^2k_0,
\qquad
\dim(\text{YES complement of }J_o\mathbf E_0)=(a^2-1)k_0.
\tag{R3.8}
\]

No zero padding is involved.

### Why the two ranges are the same

Choose a reference palette partition `xi_0`.  The selected Fourier embedding and the direct-coset
product map are both induced `S_q`-intertwiners from the same `H_t`-map on the inducing fiber.  On
that fiber, for every occurrence pair `(h,k)`, both maps send the reference vector to

\[
\eta_{t,L,h}(\xi_0)\otimes\eta_{t,R,k}(\xi_0).
\tag{R3.9}
\]

Induction extends an `H_t`-intertwiner uniquely to the corresponding `S_q`-intertwiner on
`Ind_(H_t)^(S_q) tau_t`.  Thus the two maps agree before any dimension comparison.  Formula
(R3.6) then verifies that this induced image exhausts the complete selected Fourier rank.  This is
the missing physical projection equality.  Mere equivariance and (R3.6), without (R3.9), would
not suffice.

## 4. Rule-7(a): display-by-display type and identity audit

### 4.1 Main theorem and raw product

| display | independent audit |
|---|---|
| (1.1) | **PASS as prior context.**  Same-codomain left/right cross-Grams retain the untouched occurrence factor, but both hatted factors can share packet multiplicity.  This identity alone proves no commutation. |
| (1.2) | **PASS.**  Each `F_(t,i,z)^L,F_(t,j,w)^R` is an endomorphism of the `k_t`-dimensional selected range.  The commutator is square and the theorem quantifies all positions and raw values. |
| (1.3) | **PASS.**  `E_s` is an endomorphism of the `k_1k_0`-dimensional rectangular Hilbert--Schmidt space.  Each summand maps a `k_1 by k_0` matrix to the same shape. |
| (1.4) | **PASS after (4.4).**  This is the commutator of two self-adjoint endomorphisms on one rectangular Hilbert space, not an undefined NO/YES effect commutator. |
| (2.1)--(2.4) | **PASS.**  The printed cell sizes sum to `q=4a`; each marginal rare palette has `a` labels and the word length is `a+ad=n`. |
| (2.5) | **PASS for both answers.**  Conditional on `xi`, left and right position words have no shared positional constraint.  The common YES value `C` is a fixed raw label but its two coordinate locations are independent. |
| (2.6) | **PASS.**  It is an orthogonal direct sum of `|Xi_t|` blocks, each of dimension `W_(a,d)^2`; the common alphabet action permutes blocks unitarily rather than quotienting them. |

### 4.2 Local selected projectors and global range equality

| display | independent audit |
|---|---|
| (3.0) | **PASS.**  `theta_r` has size `ad`; attaching the residual `(a-1)` strip gives `zeta` of size `n-1`, and the common singleton gives `lambda` of size `n`.  Both Pieri coefficients are one. |
| (3.1) | **PASS with the proposer's noncentrality caveat.**  `P_lambda` acts through `S_n`, `P_V` through the commuting heavy-label group, and their product is a projector.  The path projector is defined as the range projection of a deterministic local Fourier isometry; it is not claimed central.  It is a `W_(a,d) by W_(a,d)` orthogonal projector. |
| (3.2) | **PASS.**  Its dimension is `ell=f^lambda D C` in (R3.5), for NO/YES and L/R alike. |
| (3.3) | **PASS.**  `T_h:S^(a-1,1)->S^theta` and `phi:V_a->V(H_s)` are isometries.  The `D` diagonal terms and coefficient `1/sqrt D` give `delta_(hk)`. |
| (3.4) | **PASS.**  It is literally the tensor product of the two local coevaluations and therefore has coefficient `1/D`; no cross-side entangled projection is introduced. |
| (3.4a) | **PASS.**  Rank is `f^lambda D C`. |
| (3.4b) | **PASS.**  Exact multinomial counting gives (R3.3); singleton factorials are one. |
| (3.4c) | **PASS as a rank identity.**  It equals (R3.6).  It is not, by itself, a range proof. |
| (3.5) | **PASS because of the reference-fiber/induction identification, not rank alone.**  Section 3 above independently reconstructs the same inducing map and then uses (3.4c) only for exhaustiveness.  The projector is `|Xi_t|W^2 by |Xi_t|W^2` with rank `k_t`. |
| (3.6) | **PASS.**  Fourier decomposition of `M_t=Ind_(H_t)^(S_q)tau_t` turns the raw direct sum into the previously reviewed all-`nu`, all-multiplicity source. |
| (3.7) | **PASS including the full YES complement.**  If `B_q=q!/(a!)^4`, the four summand dimensions are `B_qD^2`, two copies of `B_qD^3`, and `B_qD^4`; their sum is `B_qD^2(1+D)^2=a^2 dim M_0=dim M_1`. |

### 4.3 Raw multipliers and compressions

| display | independent audit |
|---|---|
| (4.1) | **PASS.**  On a fixed fiber, each multiplier is a `W^2 by W^2` diagonal projection of the form `M_L tensor I_R` or `I_L tensor M_R`; a missing value gives the zero projection. |
| (4.2) | **PASS with no extra normalization.**  For one fixed coordinate, normalized refinement followed by exact raw-value projection pulls back to multiplication by the corresponding predicate.  Summing all raw values gives identity on either side. |
| (4.3) | **PASS after repairing the malformed `right)` token.**  On the selected range, the left block is an `ell^2 by ell^2` operator `(P_LM_LP_L)|L_L tensor I_(L_R)` and the right block is its mirror.  `M_s` need not preserve `im P_s`; both local projectors remain. |
| (4.4) | **PASS for every `xi,z,w`.**  Multiplication gives `A_L(xi) tensor A_R(xi)` in either order.  Orthogonal direct summation proves the global all-`xi` identity. |

### 4.4 Refined status and child effects

| display | independent audit |
|---|---|
| status inventory | **PASS.**  NO/L has `A,H_L`, NO/R has `B,H_R`, YES/L has `C,L,H_L`, and YES/R has `C,R,H_R`.  `U` and opposite-side-only values produce zero local multipliers. |
| singleton/residual/heavy refinement | **PASS.**  It is a scalar mask on the physical `xi` direct-sum index and therefore preserves the product proof. |
| ordered position children | **PASS in cross-side scope.**  `beta_T,beta_M,beta_B` act only on the queried position marginal.  Every nonzero branch is retained; no top-only estimate is substituted. |
| internal heavy paths | **PASS in cross-side scope.**  Pointed wreath restriction occurs only on the queried marginal.  Summing or retaining every compatible local path leaves the opposite marginal passive. |
| (5.1) | **PASS for one common marked raw value `z`.**  `ell_(t,z)^s` intertwines the marked alphabet stabilizer, so its central isotypic projections satisfy `Pi_out ell=ell Pi_in`; adjointing proves `Q_tau=Pi_in F=F Pi_in`.  All parents sharing `tau` remain in the same source isotypic block. |
| common/private point child | **PASS without parent superselection.**  A common child contains all parent columns; a private child is simply a central block with one nonzero parent.  The statement proves commutation of complete same-`z` child effects, not a tensor factorization of literal codomains. |

Point-child projectors for `z!=w` belong to different conjugate stabilizers.  The review therefore
licenses refined commutation only when the refinement is taken inside one common marked `z`, just
as the proposer states.  The unrefined aggregate raw effects commute for all `z,w`.

### 4.5 Native transfer and reduced one-side objects

| display | independent audit |
|---|---|
| (6.1) | **PASS.**  NO and YES effects are endomorphisms of unequal spaces of dimensions `k_0` and `k_1=a^2k_0`. |
| (6.2) | **PASS with `B in Hom(bold E_0,bold E_1)`.**  The first line is `E_L(E_R(B))`; right multiplication reverses the source-effect order.  The second is `E_R(E_L(B))`.  Using (4.4) independently in each answer makes the lines identical. |
| (7.1) | **PASS.**  The three contents are those of the removable boxes in rows 1, 2, and 3 of `lambda=(n-r-1,r,1)`.  They are distinct on the legal range. |
| (7.2) | **PASS.**  The Jucys--Murphy operator is self-adjoint and has those three eigenvalues on the multiplicity-free restriction, so Lagrange interpolation gives the exact branch projectors. |
| (7.3)--(7.4) | **PASS.**  `C` has domain dimension `DC` and codomain dimension `f^lambda`; `T_h^*T_k=delta I` and the Pieri isometry make `C^*C=I_(V_a tensor Z)`. |
| (7.5) | **PASS.**  `C^*Pi_beta C` is a positive `DC by DC` operator commuting with the distinguished-label `S_(a-1)`.  Since `V_a downarrow S_(a-1)=1 direct-sum V_(a-1)` multiplicity-freely, it has the displayed form.  `P_0` has rank one, `P_1` rank `a-2`, and each `R_(beta,epsilon)` is `C by C`. |
| (7.6) | **PASS as the natural ambient centralizer algebra.**  Its possible noncommutativity proves nothing about the six physical compressed matrices. |
| (7.7) | **PASS on the reviewed stability range.**  It supplies the growing `C_r` dimension but no spectrum of (7.5). |
| (8.1) | **PASS after repairing `left`.**  `Tr([R,R']^*[R,R'])` is a nonnegative, gauge-invariant scalar and vanishes exactly when that commutator vanishes.  No value is currently computed. |

## 5. Rule-7(b): regime-complete gates and counterchecks

| required regime | independent result |
|---|---|
| NO and YES | The raw marginal product is exact for both.  YES `C` positions are independent after the raw label is fixed; `U` is absent.  `k_1=a^2k_0`. **PASS.** |
| left and right | The construction is an ordered tensor product; the proof mirrors exactly and does not identify the two position carriers. **PASS.** |
| genuine uncompressed `c=1` | At stable bicovariant `r=2`, `C_r=1`; the product theorem holds.  The reduced `R_(beta,epsilon)` are scalars, though this does not identify every same-side raw status effect. **PASS outside the critical family.** |
| selected/formal `c=1` | An arbitrary one-dimensional compression is not used to prove the theorem.  If it is entangled across the two occurrence factors, it need not preserve the visible product. **Correctly excluded from the proof.** |
| actual `C_r>1` critical family | For `a=s^2,d=4s+1,r=s,s>=4`, all reviewed stability conditions hold and `C_r` grows.  The direct-coset proof is formula-level for all `C_r`; finite gates infer no asymptotic spectrum. **PASS.** |
| `a=2` | The alphabet cell packet and product count remain exact, but no stable three-row occurrence exists for `r>=2`.  It is an alphabet-only countercheck. **Correctly scoped.** |
| singleton/residual/heavy | All actual status masks are `xi`-diagonal; heavy paths remain local.  No aggregate mass is substituted for a refined matrix. **PASS.** |
| top/other position paths | All three `beta` projectors have exact formulas and every compatible heavy path remains.  Their one-side `C by C` values are not claimed. **PASS as classification; values OPEN.** |
| common/private point children | Same-`z` central marked projectors reduce both cross-side effects and retain every parent column.  Different-`z` projectors are not claimed commuting. **PASS.** |
| full YES unmatched complement | The product range uses every YES `xi` and every `V(H_L) tensor V(H_R)` vector.  Dimension (3.7) equals all of `M_1`, including both orientation complements. **PASS.** |
| complete packet versus full-type truncation | Complete Fourier inversion is load-bearing.  A parent pinch is generally a nonproduct global compression and is outside the theorem; the independent checker gives an exact synthetic noncommuting pinch guard. **PASS with this boundary.** |
| unequal answers/native transfer | The transfer acts natively on `Hom(bold E_0,bold E_1)` and includes the entire target complement.  No padding or orientation map occurs. **PASS.** |
| orientation pullback | `J_o^*F_1J_o` is a nonreducing compression in general.  Full-space commutation is not transferred to it; the checker supplies an exact counterguard. **Correctly excluded.** |

## 6. Exact transfer calculation and consequence

For `B in Hom(bold E_0,bold E_1)`, the two compositions are

\[
\begin{aligned}
\mathcal E_L\mathcal E_R(B)
 &=\sum_{z,w}F^L_{1,z}F^R_{1,w}B F^R_{0,w}F^L_{0,z},\\
\mathcal E_R\mathcal E_L(B)
 &=\sum_{z,w}F^R_{1,w}F^L_{1,z}B F^L_{0,z}F^R_{0,w}.
\end{aligned}
\tag{R6.1}
\]

By the reviewed product theorem,

\[
F^L_{t,z}F^R_{t,w}=F^R_{t,w}F^L_{t,z}
\quad\text{for }t=0,1\text{ and all }z,w.
\tag{R6.2}
\]

Commuting the target pair and source pair in the first line of (R6.1) gives the second line term by
term.  Thus

\[
[\mathcal E_L,\mathcal E_R]=0
\tag{R6.3}
\]

on the full `k_1k_0`-dimensional rectangular Hilbert--Schmidt space.  Since each transfer is already
positive self-adjoint, the pair is simultaneously unitarily diagonalizable.

This **rejects the conditional native noncommuting-Sylvester premise** when that premise is the
noncommutation of the complete-packet aggregate L/R transfer pair.  It does not prove that every
same-side pointed effect commutes, that orientation-pulled NO/YES effects commute, or that every
possible matrix-valued successor is scalar.

It also proves no scalar/resolvent feasibility.  Two commuting positive superoperators can have a
high-dimensional joint spectrum, an inadmissible inverse, a constant retained query component, or
a vanishing outer numerator.

## 7. Rule-7(d): reopening frozen inputs

| source | observed SHA-256 | use in proposer | independent reopening and boundary |
|---|---|---|---|
| full position-incidence orbit classification | `A22D513B66D50635E76C6A2707AC3FC5EE657676FFEEA0C0B68B9EE6EDC2A088` | raw answer orbit and cell types | Reconstructed the exact `p=0,u=1` side-multiplicity table and stabilizer.  Conditional on `xi`, its position stabilizer is a direct product between sides, which proves (2.5).  None of its later orbital claims is used. |
| induced-packet first gate | `047CA5FEB7E4A5D27A687106F87F4BD1F838B68BF4695E79BE18B23EBBA1CC59` | `M_t`, cell fibers, `M_1` complement | Recomputed `Xi_t`, `dim M_t=Xi_tD^2`, and the four-summand dimension identity (3.7).  Its prior external-occurrence statement did not prove the present product projection. |
| induced-packet Rule-7 review | `CF1E853AE7BEBC689963409A03D19BBA96684AF0C4BBAF4ED59155E2F64741F2` | all multiplicities and physical orientations | Reopened the complete induced-module realization rather than pinching full types.  The new proof uses all cosets; no Johnson-degree scalarization is imported. |
| block-standard Rule-7 review | `6731D07408B5D3117FE59043E151B0412F5081D99D15405D59BEA5C35B68F1AF` | `C_r`, `T_h`, Pieri paths | Rechecked stability, `T_h^*T_k`, and coefficient-one NO/YES rare attachments.  Its one-cell opposite invariant and top-only query obstruction are not used. |
| bicovariant two-cell Rule-7 review | `2FE6AE8F38DE6BBFB85C070B2AA1904F17D99228D4D771438141A015789BEB6A` | double coevaluation | Recomputed (3.3)--(3.4) as a tensor of two local coevaluations.  The earlier fixed-full-type point-effect cap is not extrapolated. |
| previous occurrence-pencil Rule-7 review | `000E1E77B1C7A2F6A8E06EBC91EF527173568EAE0D1A36ADB3D2DBAB6676D6A4` | hostile untouched-factor baseline and transfer types | Reused only the typed full source and rectangular Hilbert--Schmidt interface.  Its conclusion that abstract shared-packet factors do not force commutation remains valid; the new raw range theorem supplies additional physical information. |

The product occurrence projection, the entire `M_1` complement, and refined raw-effect theorem are
therefore reopened rather than declared inherited from an earlier fixed-type or passive-tensor
review.

## 8. Rule-7(e): hostile failure-mode audit

| attack | result |
|---|---|
| dropped/extra normalization | Local coevaluations carry `1/sqrt D`, their product `1/D`; no additional query normalization appears in `Ref^*D_zRef=M_z`.  Partition and rank counts include both heavy-fiber factors. **PASS.** |
| type/dimension mismatch | All dimensions are given in Section 3.  The only mismatch is the local omission of boldface in (6.2), corrected above. **MINOR.** |
| undefined terms/ranges | `complete packet`, `every xi`, aggregate/refined effect, same-`z`, native transfer, pullback, and critical family are fixed in Sections 5 and 10. **PASS.** |
| fixed-`xi` or colored sum substituted for the full physical sum | The proof first works for every `xi` and then takes the entire orthogonal direct sum over `Xi_t`; no representative fiber or color average replaces the full orbit. **PASS.** |
| code checks values while derivation breaks | The independent checker is explicitly synthetic.  Physical projection equality is proved by induction from the same reference map, not by checker ranks. **PASS with provenance boundary.** |
| entangled-compression fallacy | The complete selected range is proved product before compression.  Arbitrary selected/full-type compressions are excluded and the checker shows they can destroy commutation. **PASS.** |
| mere rank equality sold as projection equality | Rank equality alone fails, even for two equivariant projections of the trivial group.  The proposer is saved by the preceding exact reference-fiber identity; this is made explicit as a MINOR clarification. |
| common `S_q` action couples `xi` fibers | `S_q` covariantly permutes the orthogonal fiber projectors; it does not identify them.  The direct sum is globally equivariant and Fourier-compatible. **PASS.** |
| query/refinement changes `xi` | A query reads one existing coordinate and leaves all value multiplicities/cell membership unchanged.  Both raw multipliers preserve each `xi`. **PASS.** |
| false centrality of intermediate projector | The path projector is defined as a range projector and expressly not called central.  Only genuine marked-group isotypic projectors are called central. **PASS.** |
| omitted YES complement | Exact partition/rank counts and (3.7) include all of `M_1`; no orientation image is substituted for YES. **PASS.** |
| false parent superselection | Same-`z` `Pi_tau` is the full marked child isotypic projector and therefore codiagonal across all parents. **PASS.** |
| status/private deletion | All actual statuses, all three position children, all compatible heavy paths, and common/private point children are retained. **PASS.** |
| aggregate-to-refined overclaim | Arbitrary-`z,w` commutation is claimed only for aggregate raw effects.  Point-child refinement is limited to one common `z`; same-side and pullback claims are excluded. **PASS.** |
| literal/effect confusion | The theorem concerns `PMP` source effects and native effect transfers, not commutators of rectangular literal rows. **PASS.** |
| finite-to-critical inference | The proof is formula-level in all legal parameters.  Checker samples prove no asymptotic spectrum or exponent. **PASS.** |

## 9. Rule-7(f): formula versus independent construction

| gate | verification provenance | license |
|---|---|---|
| raw marginal product (2.5)--(2.6) | independent reconstruction from the exact side-multiplicity table | physical formula verified for both answers; not a code value |
| partition and word counts | exact multinomial formulas; checker evaluates `a=2,3,4` samples | printed all-parameter formulas verified analytically; values corroborate only |
| local occurrence range | independent Frobenius/Pieri reconstruction using all `T_h` | formula and dimension verified |
| global projection (3.5) | same-reference-intertwiner induction argument plus rank exhaustiveness | physical range equality verified; checker deliberately does not claim it |
| full `M_1` complement | exact induced-module decomposition and dimension sum | formula verified for all `a>=2` alphabet packets |
| raw compression (4.3)--(4.4) | direct tensor multiplication on every fiber | printed commutation theorem verified; checker supplies a non-range-invariant exact guard |
| same-`z` point child (5.1) | independent marked-equivariance/central-idempotent proof | refined formula verified; no numerical child row computed |
| native transfer (6.2) | direct composition with both source multiplication orders | printed transfer commutator verified; checker tests one unequal-rank complement example |
| full-type/pullback exclusions | synthetic exact counterguards plus general compression logic | scope boundary corroborated; no physical truncated spectrum claimed |
| one-side JM projectors (7.1)--(7.2) | removable-box contents and Lagrange interpolation | printed formula verified |
| reduced `R_(beta,epsilon)` form | Schur decomposition under `S_(a-1)` | operator form verified; matrix values remain unknown |
| downstream feasibility | no calculation | **not verified and not claimed** |

## 10. Rule-7(g): quantifier hygiene

* **Complete packet:** the entire induced module `M_t`, equivalently every palette partition `xi`,
  every vector in `V(H_L) tensor V(H_R)`, every full type `nu`, every multiplicity copy, and every
  occurrence pair `(h,k)`.  It is not `J_oM_0` on YES and not a list of chosen parents.
* **Every `xi`:** every ordered physical palette-cell partition in `Xi_t`; the proof does not fix a
  representative after deriving the local identity.
* **Aggregate raw effect:** `P_tM_(i,z)^sP_t` on the complete selected source.  It sums no hidden
  child pinch and retains the whole point-restriction codiagonal.
* **All `z,w`:** arbitrary raw values, including zero effects when a value is absent from a
  marginal.  Cross-side aggregate commutation holds for every pair.
* **Refined same-`z` branch:** status, ordered position child, local heavy path, and any central
  alphabet point children of the one common stabilizer fixing `z`.  It does not compare child
  projectors from two different raw marks.
* **Native transfer:** `B -> sum_z F_(1,z)^s B F_(0,z)^s` on the full unequal-rank rectangular
  Hilbert--Schmidt space.  It uses neither orientation embedding nor padding.
* **Same-side path:** a family of reduced `C_r by C_r` matrices on one pointed occurrence factor.
  Its commutators remain open and are not settled by cross-side product locality.
* **Orientation pullback:** `J_o^*F_1J_o`, a compression to the common NO source.  It is not the
  native YES effect and need not inherit full-space commutation.
* **Target critical family:** `a=s^2,d=4s+1,r=s,s>=4`, with `q=4a,n=a(d+1)` on each side.  The
  structural theorem holds throughout this family and more broadly wherever the reviewed local
  occurrence/Pieri construction is legal.
* **Conditional native noncommuting premise:** noncommutation of the complete aggregate L/R native
  transfer pair.  That exact premise is false by (R6.3).  Broader one-side matrix algebras are a
  different question.

## 11. Independent checker audit

The fresh checker performs exact symbolic/rational inference guards only.

* `partition_count_gate` verifies exact `Xi_1=a^2Xi_0` and raw marginal counts at three finite
  parameter points.
* `product_projection_gate` uses two physical-style `xi` blocks and nonreducing local projectors.
  It obtains cross-side commutator rank zero while a same-side commutator has rank four.
* `rank_is_not_range_gate` gives two same-rank projectors, both equivariant for the trivial group,
  with different ranges.  This confirms why the reference-fiber induction argument is essential.
* `truncation_counterguard` starts from commuting raw left/right predicates and applies a
  nonproduct same-rank pinch; the compressed commutator has rank two.
* `transfer_and_complement_gate` uses source rank four and target rank six, with an explicit
  unmatched target complement.  The native transfer commutator vanishes, while compression through
  a nonreducing common isometry produces a pulled commutator of rank two.

The checker does not construct the physical Fourier embedding, any Young carrier, any physical
`R_(beta,epsilon)`, or any downstream coefficient.  Its JSON correctly lists those nonclaims.

## 12. Exact licensed scope and stopping point

Newly banked after this review:

1. the complete physical direct-coset decomposition of the raw orbit;
2. the exact product identity for the canonical complete selected projection;
3. inclusion of the entire YES packet and either orientation's unmatched complement;
4. all-`z,w`, all-coordinate aggregate cross-side source-effect commutation within each answer;
5. same-`z` commutation after actual status, ordered position, compatible heavy-path, and central
   common/private point-child refinements;
6. exact commutation and simultaneous unitary diagonalizability of the two native rectangular
   transfer superoperators;
7. exact reduced formulas for all three position children and the six unresolved one-side
   occurrence matrices.

Still not banked:

1. commutation of arbitrary same-side raw/status/path effects;
2. values, ranks, spectra, or commutators of `R_(beta,epsilon)` for `C_r>1`;
3. commutation after `J_L`/`J_R` pullback or arbitrary selected/full-type compression;
4. a literal-map raw-codomain tensor theorem;
5. scalar total-energy collapse or scalar/resolvent feasibility;
6. any coefficient, query attenuation, norm bound, incidence, remainder, numerator, lower bound,
   or exponent.

Therefore the direct-coset proposer receives **MINOR / SCOPED PASS**.  It is enough to reject the
conditional **native cross-side noncommuting-Sylvester premise** in the complete aggregate packet
scope.  It proves no scalar or rectangular resolvent feasible and does not complete the canonical
occurrence-pencil node, which remains **OPEN** for the one-side pointed occurrence algebra and the
other listed obligations.
