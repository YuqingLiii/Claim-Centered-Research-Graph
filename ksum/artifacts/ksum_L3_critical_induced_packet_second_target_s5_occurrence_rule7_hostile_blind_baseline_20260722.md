# Hostile blind Rule-7 baseline — finite second-target `s=5` occurrence reducer

Date: 2026-07-22  
Reviewer role: fresh independent Rule-7 checker  
Controlling canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

## 1. Blind seal and allowed inputs

This baseline was completed before the reviewer opened any file whose name contains
`second_target_s5_exact_wreath_occurrence_reducer` or `wreath_occurrence_reducer_s5`, and before
the reviewer read the canonical node's new `s=5` work paragraphs.  The proposer artifact, proposer
tool, proposer JSON, proposer log, and desired proposer answer were therefore unavailable to this
derivation.

The only mathematical inputs used were:

1. the reviewed target-family planning in
   `ksum/artifacts/ksum_L3_critical_induced_packet_one_point_double_pieri_wreath_gram_stack_20260722.md`;
2. the already reviewed finite `s=4` occurrence construction, only for its characteristic-zero
   James-kernel/orbit construction and marked-JM mechanism;
3. a new direct integer-partition orbit catalogue and new exact `s=5` nullspace, form, commutant,
   word-closure, and projector calculations.

The reviewed `s=4` inputs were unchanged at the freeze point:

| reviewed input | SHA-256 |
|---|---|
| `ksum/tools/ksum_l3_wreath_occurrence_reducer.py` | `06B842F0475B85691A76128864BE22D6996BBECDC7A9981FE6111929CA28F371` |
| `ksum/artifacts/ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_20260722.md` | `5A3CEF4C3A26C59FC0EDA3BF6DB1F9490F0D22D5096F9564A5671E400A1D5A91` |
| reviewed `s=4` JSON | `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16` |
| reviewed `s=4` log | `323AEBA68F87E24FB40EA51F78DD1304264B2B5E1BA86B0F503666DB061D1C76` |
| reviewed `s=4` independent checker | `A1DC19F3F8CE1198AC8FAA5EBEE9B57EF55C360526C077A1CD8C83ECFA459D39` |
| reviewed `s=4` independent output | `584F509AD728D9BA13FC6183ECA05F992279DC4A4A318C0ACED8E9A3CDEE2CC0` |

The blind `s=5` answer was not extrapolated from the `s=4` algebra
`M_1(Q) direct-sum M_3(Q)`.  In fact the independently discovered `s=5` block type below is
different.

## 2. Parameter tuple, shapes, and finite scope

The predecessor family is

\[
a=s^2,\qquad d=4s+1,\qquad r=s,\qquad q=4a,
\qquad n=a(d+1),\qquad N=2n.
\]

Its second finite member is

\[
\boxed{(s,a,d,r,q,n,N)=(5,25,21,5,100,550,1100)}.
\]

The occurrence carrier has size `ad=525` and

\[
\theta=(519,5,1),
\]

with the three removable-corner children

\[
\kappa_T=(518,5,1),\qquad
\kappa_M=(519,4,1),\qquad
\kappa_B=(519,5).
\]

For orientation only, the position-side planning shapes are

\[
\lambda=(544,5,1),\qquad
(\beta_T,\beta_M,\beta_B)=((543,5,1),(544,4,1),(544,5)).
\]

Those position shapes are not used to license any position, alphabet, Pieri, transfer, or query
claim in this review.

## 3. Independent size and James-kernel gates

Put

\[
H=S_{21}^{25},\qquad W=H\rtimes S_{25},\qquad
U_\theta=(S^\theta)^H.
\]

An independent exact horizontal-strip recurrence gives

\[
\dim U_\theta=[s_\theta]h_{21}^{25}=1{,}883{,}700,
\]

and, after replacing one block size `21` by `20`,

\[
([s_{\kappa_T}],[s_{\kappa_M}],[s_{\kappa_B}])
h_{20}h_{21}^{24}
=(1{,}883{,}700,322{,}920,98{,}280).
\]

The exact hook dimensions are

\[
f^\theta=139{,}672{,}485{,}907{,}500,
\]

\[
(f^{\kappa_T},f^{\kappa_M},f^{\kappa_B})
=(138{,}073{,}135{,}358{,}211,
1{,}279{,}485{,}207{,}936,
319{,}865{,}341{,}353),
\]

and the three child dimensions sum exactly to `f^theta`.

The distinguished-block quotient, whose group quotient is the block stabilizer `S_24`, has
permutation-orbit dimension `64`.  Its restricted James keep-map ranks for retained row-two sizes
`v=0,1,2,3,4` are

\[
2,5,11,21,38,
\]

and its merge-map rank is `30`.  The stacked map is `107 by 64`, has rank `56`, and hence has
kernel dimension `8`.

The full-block quotient has orbit dimension `19`; its keep-map ranks are

\[
1,2,4,7,12,
\]

its merge-map rank is `11`, and its `37 by 19` stack has rank `18` and kernel dimension `1`.
Since

\[
\operatorname{Ind}_{S_{24}}^{S_{25}}\mathbf1
\cong\mathbf1\oplus V_{25},\qquad V_{25}=S^{(24,1)},
\]

the standard multiplicity space

\[
Z=\operatorname{Hom}_{S_{25}}(V_{25},U_\theta)
\]

has

\[
\boxed{\dim Z=8-1=7}.
\]

Thus `V_25 tensor Z` has dimension `24*7=168`.  This is a complete isotypic multiplicity count,
not selection of a favorable copy.

## 4. Actual normalizer action and marked corner projectors

On the labelled `H`-orbit keys `(b_0,...,b_24;j)`, an adjacent physical block swap permutes the
two block occupancies and the third-row block label simultaneously.  Its domain and codomain are
the same labelled orbit carrier of dimension

\[
25{29\choose5}=2{,}968{,}875.
\]

The unnormalised orbit Gram weight is

\[
21{20\choose b_j}\prod_{i\ne j}{21\choose b_i}.
\]

Because the action is the adjacent permutation of all block indices, its involution, braid, and
far-commutation identities hold on every labelled key, and the displayed Gram weight is invariant.
This is the actual normalizer action before quotienting, not a colored-orbit surrogate.

Fix a point `x` in block zero.  The marked base group is

\[
H'=S_{20}\times S_{21}^{24},
\]

and the marked tabloid-orbit quotient has dimension `121`.  The relative operator

\[
J_x=\sum_{y\ne x}(x\ y)
\]

is an endomorphism `Q^121 -> Q^121` and is self-adjoint in the exact diagonal orbit Gram.  The
corner contents are

\[
c_T=518,\qquad c_M=3,\qquad c_B=-2.
\]

Therefore, on the embedded selected `S^theta` source columns,

\[
P_T={ (J-3I)(J+2I)\over267800},
\]

\[
P_M={ (J-518I)(J+2I)\over-2575},
\]

\[
P_B={ (J-518I)(J-3I)\over2600}.
\]

These polynomials must resolve that source and be mutually orthogonal idempotents there.  They are
not asserted to be global projectors on every other Specht summand of the `121`-dimensional marked
permutation quotient.

## 5. Eta sectors, six forms, and exact normalization

Restriction gives

\[
V_{25}\downarrow S_{24}\cong\mathbf1\oplus V_{24},
\qquad\dim V_{24}=23.
\]

The selected eta-sector dimensions are therefore `7` and `23*7=161`.  For an isometric eta
inclusion, each reduced form has domain and codomain `Z`, hence is `7 by 7`, and the normalization
is

\[
O_{\kappa,\eta}
={1\over\dim\eta}\operatorname{Tr}_\eta
\bigl(Q_\eta P_\kappa Q_\eta\bigr).
\]

Equivalently in a rational Gram basis,

\[
H^\mathbf1_\kappa+23H^{V_{24}}_\kappa
=24{f^\kappa\over f^\theta}G.
\]

The two mandatory resolutions are

\[
\sum_\kappa H^\mathbf1_\kappa=G,
\qquad
\sum_\kappa H^{V_{24}}_\kappa=G.
\]

The independent exact form ranks are

| form | `T,1` | `T,V24` | `M,1` | `M,V24` | `B,1` | `B,V24` |
|---|---:|---:|---:|---:|---:|---:|
| rank | 7 | 7 | 5 | 7 | 6 | 7 |

Every form is exactly positive semidefinite.  The permanent checker must provide exact rational
Gram/Schur or principal-minor certificates, not floating eigenvalues.  It must also check both
resolutions and all three trace identities at matrix level on all seven multiplicity columns.

## 6. Raw forms are not endomorphisms; exact algebra baseline

The raw matrices `H_(kappa,eta)` are bilinear forms.  Products such as `H_i H_j` have no
basis-invariant operator meaning in a nonorthonormal basis.  The actual endomorphisms are

\[
A_{\kappa,\eta}=G^{-1}H^\eta_\kappa\in\operatorname{End}_{\mathbb Q}(Z),
\qquad A^T G=GA.
\]

All commutators and algebra calculations below use these Gram-raised operators.  The exact fifteen
pairwise ranks are characterized as follows:

- each of the three same-`kappa`, different-eta pairs has commutator rank `0`;
- every one of the twelve different-`kappa` pairs has commutator rank `2`.

The common-commutant system in the `49`-dimensional space `End_Q(Z)` has rank `46`, hence common
commutant dimension `3`.  The commutant is commutative.  Exact word closure has dimension `27`.
The same generated dimension may independently be obtained from the exact bicommutant after using
the positive-Gram `*` structure; commutator ranks alone do not establish it.

In the deterministic blind rational Gram-orthogonal gauge, two common invariant lines are

\[
L_1=\operatorname{span}\left(
1,{296315649\over1426296086},{9569033\over299148822},0,0,0,0
\right),
\]

\[
L_2=\operatorname{span}\left(
0,0,0,1,-{254025453859000\over3670865456209749},0,0
\right).
\]

The rank-one `G`-orthogonal projector onto `L_1` has only the leading `3 by 3` block

\[
\begin{pmatrix}
\frac{119659528800}{213101878349}&
\frac{4247434634284800}{34562354343789263}&
\frac{1961957990527982919738}{151973187504213421007}\\
\frac{109308979558800}{937024468694861}&
\frac{3880031538419164800}{151973187504213421007}&
\frac{1792248624347312397180663}{668237166092854886307023}\\
\frac{23600}{1313927}&
\frac{837705600}{213101878349}&
\frac{386949614801261}{937024468694861}
\end{pmatrix},
\]

with every other entry zero.  The rank-one projector onto `L_2` has only the coordinate-`4,5`
block

\[
\begin{pmatrix}
\frac{1018418159693802}{12575365320022427}&
-\frac{9172756348127935401169679733}{690694677375443415942420712}\\
-\frac{4958000}{884692263}&
\frac{11556947160328625}{12575365320022427}
\end{pmatrix}.
\]

Let `P_5=I_7-P_1-P_2`.  The exact gates are

\[
P_i^2=P_i,\quad P_iP_j=0,\quad \sum_iP_i=I_7,
\quad P_i^TG=GP_i,
\]

with ranks `1,1,5`, and every `P_i` commutes with all six generators.  Since

\[
1^2+1^2+5^2=27,
\]

the exact rational classification expected from the independent construction is

\[
\boxed{\mathcal A_5\cong
M_1(\mathbb Q)\oplus M_1(\mathbb Q)\oplus M_5(\mathbb Q)}.
\]

Projector coordinates and invariant-line coordinates are gauge dependent.  Their ranks, exact
intertwining identities, central decomposition, and algebra isomorphism type are the comparison
invariants.

## 7. Rule-7 hostile checklist fixed before comparison

The proposer comparison must explicitly test all of the following.

1. **Per-display typing:** domain, codomain, and parameter-dependent dimensions for every displayed
   James map, block swap, marked embedding, JM polynomial, eta trace, form, Gram-raised operator,
   commutant equation, and central projector.
2. **Regime-complete identity gates:** all seven multiplicity columns; all three corners; both eta
   sectors; all six PSD forms; both resolutions; all three trace identities; all fifteen
   commutators.  The reviewed `s=4` `c=1` dense toy remains frozen only for the already-reviewed
   quotient/JM mechanism; the new `c=7` identity regime is reopened here in full.
3. **Anchoring ban:** no proposer formula or value may be used to repair this baseline.
4. **No frozen-input immunity:** any use of `s=4` beyond its reviewed orbit/James/JM scope must be
   reopened.  No `s=4` algebra formula is load bearing.
5. **Standing failure modes:** dropped or extra normalization (`21`, `25`, `24`, `23`, `525`,
   `dim eta`, orbit-size, Gram, hook, or central-sum factors); type/dimension mismatch; undefined
   terms or missing stability ranges; a colored-orbit sum substituted for the full central sum;
   and numerics agreeing with values while the printed derivation is broken.
6. **Further attacks:** naive products of raw forms instead of `G^-1 H`; rank-only algebra
   classification; floating spectral decisions; omitted eta resolution; a polynomial called a
   global marked-space projector when it is only a source projector; and accidental finite-to-
   uniform inference.
7. **Formula versus construction provenance:** exact agreement of an independent construction
   corroborates values but does not by itself verify an ill-typed printed derivation.  The final
   verdict must state separately which printed formulas were audited and which values were rebuilt.
8. **Quantifier hygiene:** `second target` means only the displayed finite tuple; `corner` means one
   of the three displayed removable boxes; `standard eta` means `V_24`; and no undefined
   `admissible`, `active`, `strict`, or `stable` range may enter the positive verdict.

## 8. Exact finite license and explicit withholding

If every comparison gate passes, this review may license exactly the finite occurrence-side table
and rational algebra above at `(s,a,d,r)=(5,25,21,5)`.  It may strengthen confidence that the
reviewed `s=4` phenomenon is not an isolated implementation accident, but two finite points do not
prove a sequence formula.

The baseline explicitly withholds every general-`s` formula, asymptotic statement, physical
alphabet/Pieri assembly, physical NO/YES or left/right transfer, feasibility conclusion, query
bound, numerator bound, and exponent improvement.

## 9. Blind computational provenance

Two exact blind constructions were run without importing or reading the proposer `s=5` tool:

- independent scratch reducer SHA-256
  `1D6524C94A238585FB253B13BDD37537910CC29723A7A84877160FD1D0E5DEFC`, output SHA-256
  `B0431EFE3EE4183E75A2D1CB2562D59ECA2EE55F2EA3A42BB6FFC256382DEE71`;
- independent rational projector splitter SHA-256
  `0897FD73761872777E6BAE94B5CCCD08E5190DEBAC9D3195414DDCA73FF98EC9`, output SHA-256
  `95A2DD8A8022BF122218524A001F7D3E5A8423E5267580212DF125552FE4C2BB`.

The permanent review checker in
`ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/` uses a direct partition catalogue,
exact rational Gram/Schur PSD certificates, exact commutant ranks, and the exact rational
bicommutant route.  No floating-point decision is admissible.
