# Fresh Rule-7 review — exact first-target wreath occurrence reducer

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the proposer mathematics or code  
Controlling canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_20260722.md`  

## 1. Verdict

**PASS / STRICTLY SCOPED PASS.**

The following finite, occurrence-only statements are independently verified for

\[
(s,a,d,r)=(4,16,17,4),\qquad \theta=(267,4,1):
\]

1. the exact invariant-space and branching dimensions, including
   `dim U_theta=34272`, the marked child counts `34272/7140/3060`, and
   `dim Hom_(S_17 wr S_16)(V_16,S^theta)=4`;
2. the exact James-kernel/orbit-quotient realization used by the reducer;
3. the physical block-normalizer action and its Coxeter/Gram descent;
4. the marked relative Jucys--Murphy construction and the three corner projectors on the
   selected `S^theta` source;
5. all six `4 by 4` normalized occurrence forms
   `O_(kappa,eta)`, including exact PSD and both `eta` resolutions;
6. the three same-`kappa` zero commutators and the twelve different-`kappa` commutators of
   exact rank two;
7. common commutant dimension two, generated rational algebra dimension ten, the displayed
   common invariant line, and the rational algebra classification
   `M_1(Q) direct-sum M_3(Q)`.

This does **not** complete the controlling node.  The node's claim asks for complete physical
NO/YES, left/right, status/path, and cross-answer pencils.  The reviewed artifact supplies only
the first finite heavy-occurrence restriction table.  In particular, this review licenses no
alphabet point-child table, no Pieri attachment scalar, no assembled physical Gram, no NO/YES or
L/R commutator, no distinct-mark conclusion, no uniform-in-`s` theorem, no attenuation, no
numerator, no query-norm bound, and no exponent improvement.  The canonical node must remain
**OPEN**.

There is no mathematical correction required for the statements within that scope.  Two
scope qualifications are important but are already respected by the proposer:

- the degree-two polynomials in the `71 by 71` marked permutation quotient are branch
  projectors only on the embedded `S^theta` source; they are not asserted to be global
  projectors on every other Specht summand of that quotient;
- the tool represents the adjacent block swaps by their exhaustive action formula on the
  `62016` labelled `H`-orbit keys.  It does not materialize a dense `34272 by 34272` matrix;
  descent to the James kernel follows from exact `S_272`-equivariance.

## 2. Review provenance and frozen hostile baseline

Before opening the proposer artifact, tool, or logs, the reviewer derived and archived a hostile
baseline:

`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_rule7_blind_baseline_20260722.md`,
SHA-256
`3818339B7E5D54AEB6BB8C10802B5DD29B4C613AA0F003CC6683CA893AF96F42`.

That baseline fixed, without choosing a desired commutation answer:

- the spaces `U_theta`, `V_16 tensor Z`, and the marked `eta` sectors;
- `dim U_theta=34272`, `dim Z=4`, and selected isotypic dimension `60`;
- the three children, their Specht dimensions and marked-invariant counts;
- corner contents `266,2,-2` and the exact Lagrange denominators;
- the `1/dim(eta)` normalization and per-`eta` identity resolution;
- exact Gram, Coxeter, PSD, commutator, commutant, algebra, and invariant-line gates;
- the prohibition on every finite-to-asymptotic or occurrence-to-physical-pencil inference.

The blind baseline was communicated to the commissioning parent before the proposer inputs were
opened.  This meets the Rule-7(c) anchoring requirement.

The proposer inputs have the claimed hashes:

| Input | SHA-256 |
|---|---|
| proposer artifact | `5A3CEF4C3A26C59FC0EDA3BF6DB1F9490F0D22D5096F9564A5671E400A1D5A91` |
| proposer tool `ksum/tools/ksum_l3_wreath_occurrence_reducer.py` | `06B842F0475B85691A76128864BE22D6996BBECDC7A9981FE6111929CA28F371` |
| proposer JSON | `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16` |
| proposer log | `323AEBA68F87E24FB40EA51F78DD1304264B2B5E1BA86B0F503666DB061D1C76` |

The original tool was rerun into the fresh directory
`ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_rule7_review_20260722/`.  Its fresh JSON and log
are byte-identical to the proposer outputs, with the same two hashes above.

The separate checker

`ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_rule7_review_20260722/independent_review_check.py`,
SHA-256
`A1DC19F3F8CE1198AC8FAA5EBEE9B57EF55C360526C077A1CD8C83ECFA459D39`,

does not import the proposer tool.  Its exact output is

`ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_rule7_review_20260722/independent_review.json`,
SHA-256
`584F509AD728D9BA13FC6183ECA05F992279DC4A4A318C0ACED8E9A3CDEE2CC0`,

and begins `ALL_INDEPENDENT_RULE7_GATES_PASS`.

## 3. Independent mathematical reconstruction

### 3.1 Unmarked carrier and `C_4` gate

Put

\[
n_0=ad=272,\quad
H=S_d^a=S_{17}^{16},\quad
W=H\rtimes S_{16},\quad
U_\theta=(S^\theta)^H.
\]

The horizontal-strip character identity gives

\[
\dim U_\theta
=\langle s_\theta,h_{17}^{16}\rangle
=K_{\theta,(17^{16})}=34272.
\]

The quotient normalizer `W/H` is `S_16`.  Let `W_0/H` be the `S_15` subgroup fixing block zero.
Independent James-kernel computations on the corresponding orbit sums give

\[
\dim U_\theta^{S_{15}}=38-33=5,
\qquad
\dim U_\theta^{S_{16}}=12-11=1.
\]

By

\[
\operatorname{Ind}_{S_{15}}^{S_{16}}\mathbf1
\cong\mathbf1\oplus S^{(15,1)},
\]

the only `S_16` types with an `S_15`-fixed line are the trivial and standard types.  Therefore

\[
\dim Z
=\dim\operatorname{Hom}_{W}(S^{(15,1)},S^\theta)
=5-1=4.
\]

This is a multiplicity computation, not a favorable-copy selection.  Since
`dim V_16=15`, the complete selected isotypic carrier has dimension `15*4=60`.

### 3.2 James kernel and orbit quotient

For the general three-row shape

\[
\theta=(n_0-r-1,r,1),
\]

the Young permutation module has

\[
\dim M^\theta=n_0\binom{n_0-1}{r};
\]

at the reviewed target this is `59,783,011,920`.  A tabloid is specified by its second-row
`r`-set `B` and disjoint third-row singleton `C`.  James's characteristic-zero kernel
intersection is

\[
S^\theta=
\left(\bigcap_{v=0}^{r-1}\ker\psi_{1,v}\right)
\cap\ker\psi_{2,0}.
\]

Here

\[
\psi_{1,v}:M^{(n_0-r-1,r,1)}
\longrightarrow M^{(n_0-v-1,v,1)}
\]

retains a `v`-subset of `B`, while

\[
\psi_{2,0}:M^{(n_0-r-1,r,1)}
\longrightarrow M^{(n_0-r-1,r+1)}
\]

merges `C` into `B`.  At `n_0=272,r=4`, the ambient target dimensions for `v=0,1,2,3` are
`272`, `73,712`, `9,951,120`, and `892,283,760`; the merge target has dimension
`11,956,602,384`.

Taking invariants is exact in characteristic zero.  Thus restricting the equivariant James maps
to orbit sums and then taking their common kernel is exactly `(S^theta)^G`, not a numerical
surrogate.  In the block-zero distinguished quotient the restricted map dimensions are

\[
2,5,11,21,19\quad\text{from a 38-dimensional source},
\]

and the stacked rank is `33`.  In the full block quotient they are

\[
1,2,4,7,7\quad\text{from a 12-dimensional source},
\]

and the stacked rank is `11`.

The coefficient from a source orbit sum to a target orbit sum is

\[
\frac{|O_{\rm source}|}{|O_{\rm target}|}
\prod_i\binom{b_i}{b'_i};
\]

the review checker independently derives these coefficients.  It also compares them against a
fully expanded `60`-tabloid model for `(a,d,r,theta)=(3,2,2,(3,2,1))`.  Every keep map and the
merge map agree exactly.  This toy gate has standard multiplicity `c=1`, while the reviewed first
target has `c=4`; consequently both the scalar and genuinely matrix-valued multiplicity regimes
are exercised at identity level.

### 3.3 Block swaps and Gram

On the labelled `H`-orbit key `(b_0,...,b_15;j)`, an adjacent physical block swap has domain and
codomain the same `62016`-dimensional labelled orbit space and acts by

\[
(b_i,b_{i+1};j)\longmapsto(b_{i+1},b_i;s_i(j)).
\]

The orbit-sum Gram is diagonal with positive weight

\[
17\binom{16}{b_j}\prod_{i\ne j}\binom{17}{b_i}.
\]

The key permutation satisfies every involution, braid, and far-commutation identity and preserves
this weight on all `62016` keys.  Each James map is `S_272`-equivariant, so the action preserves
the common kernel and induces the physical `S_16` action on `U_theta`.  No Euclidean-transpose
substitution is made: all reduced adjoints use the transported orbit Gram.

### 3.4 Marking, corner projectors, and types

Fix a point `x` in block zero.  The marked base group is

\[
H'=S_{16}\times S_{17}^{15},
\]

with the other fifteen blocks permuted by `S_15`.  Its marked tabloid-orbit quotient has dimension
`71`.  The relative Jucys--Murphy operator

\[
J_x=\sum_{y\ne x}(x\ y)
\]

is an endomorphism of this `71`-dimensional quotient and is self-adjoint in its diagonal orbit
Gram.  The review checker reconstructs `J_x` with a different transition loop and obtains the
same compressed moments.  In the dense `60`-tabloid toy construction, the reduced marked `J_x`
also agrees exactly with the literal sum of transpositions.

The restriction

\[
S^{(267,4,1)}\downarrow S_{271}
\cong
S^{(266,4,1)}\oplus S^{(267,3,1)}\oplus S^{(267,4)}
\]

is multiplicity-free.  The three contents are `266,2,-2`; hence on the embedded `S^theta` source
the three Lagrange polynomials have denominators `70752,-1056,1072`.  They are mutually
orthogonal idempotents and resolve that source.  The exact Specht dimensions are

\[
46,071,366,111,\quad649,566,675,\quad216,510,030,
\]

and sum to

\[
f^\theta=46,937,442,816.
\]

The marked base-invariant dimensions, independently regenerated by horizontal-strip recursion,
are `34272`, `7140`, and `3060`.

### 3.5 `eta` normalization and resolution

The selected source has type

\[
V_{16}\otimes Z,
\qquad \dim(V_{16}\otimes Z)=15\cdot4=60.
\]

Under the block-zero stabilizer,

\[
V_{16}\downarrow S_{15}\cong\mathbf1\oplus V_{15},
\]

so the two sectors have dimensions `1*4=4` and `14*4=56`.  For an isometric inclusion
`i_eta:eta -> V_16`, the reviewed occurrence form is

\[
O_{\kappa,\eta}[h,h']
=\frac1{\dim\eta}
\operatorname{Tr}_\eta
\left[(b_{\theta\to\kappa}T_hi_\eta)^*
(b_{\theta\to\kappa}T_{h'}i_\eta)\right].
\]

Thus `O_(kappa,eta)` is a Hermitian form on `Z`, i.e. a `4 by 4` matrix.  The factor
`1/dim(eta)` is present.

For each point `x`, let `P_(kappa,x)` be the `kappa` branch projection.  The full sum over all
`272` points is central on the irreducible `S^theta` carrier, and its trace gives

\[
\sum_xP_{\kappa,x}
=272\frac{f^\kappa}{f^\theta}I_{S^\theta}.
\]

The wreath group is transitive on points.  Taking the normalized `V_16` partial trace therefore
gives, on the four-dimensional multiplicity space,

\[
H^\mathbf1_\kappa+14H^{V_{15}}_\kappa
=15\frac{f^\kappa}{f^\theta}G.
\]

There is no missing factor `272`, `16`, `17`, or `14`: `272` cancels against the orbit average,
and `14` is the unnormalized trace multiplicity before division by `dim V_15`.  Both exact
resolutions

\[
\sum_\kappa H^\mathbf1_\kappa=G,
\qquad
\sum_\kappa H^{V_{15}}_\kappa=G
\]

hold.  Every raw `H` is symmetric and has all principal minors nonnegative.  Congruence by
`G^(-1/2)` proves PSD of the normalized occurrence matrices.

## 4. Matrix algebra audit

On the rational Gram-orthogonal basis, each operator is

\[
A_{\kappa,\eta}=G^{-1}H^\eta_\kappa\in\operatorname{End}_{\mathbb Q}(Z),
\qquad \dim Z=4.
\]

Since `H` is symmetric,

\[
A_{\kappa,\eta}^{T}G=GA_{\kappa,\eta};
\]

therefore the generators are self-adjoint for the positive form `G`.  Independent exact RREF
reproduces the complete pairwise rank multiset

\[
\{0,0,0,\underbrace{2,\ldots,2}_{12}\}.
\]

The zero pairs are exactly the two `eta` operators with the same `kappa`.  This also follows from
the trace identity, because one is an affine polynomial in the other.  Every different-`kappa`
pair has rank two.

The common-centralizer system has rank `14` in `End_Q(Z)`, hence commutant dimension `2`.  Exact
word closure gives generated-algebra dimension `10`.  The displayed rational projector is
idempotent, has rank one, is `G`-self-adjoint, commutes with all six generators, and has image

\[
\operatorname{span}_{\mathbb Q}
\left(1,{1839664\over39414687},0,0\right).
\]

Its `G`-orthogonal complement has dimension three.  Every generated operator is block diagonal
for this `1+3` decomposition, so the largest possible rational block algebra has dimension
`1^2+3^2=10`.  Since exact word closure attains ten, the generated algebra is the entire block
algebra

\[
M_1(\mathbb Q)\oplus M_3(\mathbb Q).
\]

This argument is stronger than a numerical eigendecomposition and remains valid after
complexification.  Commutator ranks alone were not used to infer the algebra type.

## 5. Rule-7 checklist

### 7(a) Type audit

Every displayed operator identity in the proposer artifact is typed as follows.

| Proposer display | Domain and codomain | Dimension audit |
|---|---|---|
| (2.1), James intersection | subspace identity inside `M^theta` | ambient `n_0 binom(n_0-1,r)`; first target `59,783,011,920` |
| (2.4), `psi_(1,v)` | `M^(n_0-r-1,r,1) -> M^(n_0-v-1,v,1)` | orbit restrictions `38 -> 2,5,11,21` or `12 -> 1,2,4,7` |
| (2.4), `psi_(2,0)` | `M^(n_0-r-1,r,1) -> M^(n_0-r-1,r+1)` | orbit restrictions `38 -> 19` or `12 -> 7` |
| (3.1)--(3.3), block swaps | endomorphisms of the labelled `H`-orbit carrier, descending to `U_theta` | labelled `62016`; `dim U_theta=34272` |
| (4.1), `J_x` | endomorphism of the marked orbit quotient induced from `M^theta` | `71 -> 71` |
| (4.3)--(4.4), `P_kappa(J_x)` | polynomials on the marked quotient, restricted to the selected embedded source | source columns `Q^4 -> Q^71`; branch identities checked on all four columns |
| (5.2)--(5.3), `H` and `O` | bilinear forms on `Z`; normalized endomorphism forms after `G^(-1/2)` | `4 by 4`, with `dim Z=4` |
| (5.6), eta trace identity | equality in `Bil(Z)` | both sides `4 by 4`; eta dimensions `1,14` |
| (5.8), resolutions | equality in `Bil(Z)` | each sum is the `4 by 4` Gram `G` |
| (6.1), `A=G^-1 H` | endomorphism of `Z` | `4 -> 4` |
| (6.2), common commutant | linear system for `X in End_Q(Z)` | 16 variables, rank 14, kernel dimension 2 |
| (6.3), central projector | `G`-orthogonal endomorphism of `Z` | rank `1` on `Q^4` |
| (6.5), generated algebra | unital subalgebra of `End_Q(Z)` | dimension `10=1+9` |

The maps `T_h:V_16->S^theta`, `i_eta:eta->V_16`, and
`b_(theta->kappa):S^theta->S^kappa` compose in the stated order.  No multiplicity factor is
silently identified with a Specht carrier.

### 7(b) Regime-complete identity gates

The claimed first target is the genuinely matrix-valued `c=4` regime.  All four multiplicity
columns, all three removable corners, both `eta=1` and `eta=V_15`, all six PSD forms, both
resolutions, and all fifteen pairwise commutators are checked exactly.  The independent dense toy
gate additionally checks a `c=1` standard-multiplicity branch at identity level, including James
maps, marked JM, both eta resolutions, and corner PSD.  No qualitative multiplicity or corner
branch in the stated occurrence claim is left untested.

NO/YES, left/right, rare/common/residual, alphabet-parent, Pieri-path, and distinct-mark regimes
are not silently declared tested: they are outside this artifact's stated claim and are explicit
open obligations of the controlling node.

### 7(c) Anchoring ban

The blind baseline in Section 2 was archived and communicated before the proposer proof or code
was read.  It independently fixed the spaces, dimensions, corner contents, eta normalization,
algebra gates, and scope exclusions without fixing a desired commutator result.

### 7(d) No frozen-input immunity

No prior aggregate-packet review is used to immunize the operator-level occurrence calculation.
The review independently reopens:

- hook and horizontal-strip dimensions;
- James-kernel restriction and invariant quotient;
- actual block-normalizer action and Gram;
- marked-JM transitions and branch projectors;
- eta partial-trace normalization;
- all matrix-algebra conclusions.

The complete packet, alphabet point-child, and Pieri coefficients are not load-bearing inputs to
the six occurrence matrices and are expressly excluded rather than treated as frozen.

### 7(e) Failure-mode diversity

- **Dropped/extra normalization:** the factors `15`, `14`, `f^kappa/f^theta`, and the cancellation
  of `272` are independently derived; both eta resolutions pass.
- **Type/dimension mismatch:** all maps and all `c=4` multiplicity columns are audited in 7(a).
- **Undefined terms/stability ranges:** `first target` means the single displayed tuple;
  `corner` means one of the three removable boxes; `same-side occurrence algebra` means only the
  six operators on one `Z`, not an assembled query.  No hidden stability range is invoked.
- **Colored-orbit versus full sums:** orbit sums are the exact fixed-space basis.  The central
  trace identity uses all `272` points, and the block-swap audit covers every `62016` labelled
  `H`-orbit key.
- **Value/formula disconnect:** addressed separately in 7(f).
- **Wrong inner product:** self-adjointness and orthogonality use the exact orbit Gram, not
  Euclidean transpose in a nonorthonormal basis.
- **Dense-space substitution:** neither the `46,937,442,816`-dimensional Specht carrier nor a
  dense `34272` carrier is constructed or claimed.
- **Rank substituted for algebra:** the commutant, word closure, central projector, and maximum
  block-dimension argument are all checked in addition to commutator ranks.

### 7(f) Value-versus-formula decoupling

Three evidence layers are separated.

1. The fresh proposer-tool rerun exercises the printed formulas for James maps, block swaps,
   marked JM, Lagrange projectors, eta trace identity, and `A=G^-1H`; it is byte-identical to the
   original output.
2. The independent checker does not import the proposer.  It reconstructs the first-target orbit
   spaces, James kernels, fixed-line multiplicity, marked JM, all six matrices, and the rational
   algebra, obtaining exact entry-by-entry agreement in the deterministic gauge.
3. The dense toy construction applies the James maps and literal transposition sum directly to
   individual tabloids before orbit compression.  It independently validates the quotient
   coefficient and marked-JM mechanisms in a feasible carrier.

The review's mathematical derivations in Sections 3--4 verify the printed route, while the two
independent constructions corroborate the resulting values.  The review does not claim that
matching values alone would repair an ill-typed derivation.

### 7(g) Quantifier hygiene

All positive conclusions are quantified only at
`(s,a,d,r)=(4,16,17,4)` and only for the six matrices indexed by

\[
\kappa\in\{(266,4,1),(267,3,1),(267,4)\},
\qquad\eta\in\{\mathbf1,V_{15}\}.
\]

`Every different-kappa pair` means the twelve pairs among those six matrices.  `PSD`, `rank`,
`commutant`, and `generated algebra` mean exact rational statements after the stated positive-Gram
identification.  No statement is quantified over `s>=4`, `q`, `N`, answers, sides, point labels,
or physical query pencils.

## 6. Banked result and stopping point

The exact first-target occurrence table and its finite algebra can now be treated as reviewed
input.  What is banked is precisely:

\[
\{O_{\kappa,\eta}:\kappa=T,M,B;\ \eta=\mathbf1,V_{15}\}
\]

for the first target, together with its dimension, PSD, resolution, commutator, commutant,
invariant-line, and `M_1(Q) direct-sum M_3(Q)` facts.

The next physical calculation still requires the separately reviewed all-parent alphabet matrices
and every relevant Pieri scalar, followed by assembly with complete NO/YES, left/right, status,
path, and unmatched-complement bookkeeping.  Even a later nonzero assembled finite commutator
would remain a finite witness until a uniform legal-family formula is proved.  No downstream
feasibility or k-Sum lower-bound claim is made in this review.
