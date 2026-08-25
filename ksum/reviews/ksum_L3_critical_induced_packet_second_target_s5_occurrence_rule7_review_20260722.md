# Fresh Rule-7 review - exact second-target `s=5` wreath occurrence reducer

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the proposer mathematics or code  
Controlling canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_second_target_s5_exact_wreath_occurrence_reducer_20260722.md`

## 1. Verdict and exact license

**MINOR / STRICTLY SCOPED PASS.**

The finite mathematical result passes.  One localized field-of-scalars annotation is wrong: the
radical-normalized matrices in proposer display (1.2), and again in the sentence following (6.1),
are generally not rational matrices.  The correction is

\[
 H^\eta_\kappa\in\operatorname{Bil}_{\mathbb Q}(Z),\qquad
 A_{\kappa,\eta}=G^{-1}H^\eta_\kappa\in\operatorname{End}_{\mathbb Q}(Z),
 \qquad
 \mathsf O_{\kappa,\eta}=D^{-1}H^\eta_\kappa D^{-1}
 \in\operatorname{End}_{K}(Z\otimes_{\mathbb Q}K),
\]

where `dim_Q Z=7`, `D=diag(sqrt(n_1),...,sqrt(n_7))`, and
`K=Q(sqrt(n_1),...,sqrt(n_7))` is a real algebraic extension.  In particular,
`O_(T,1)[1,2]` in the submitted data is exactly

\[
 {15292208\sqrt{84864617117}\over3871830361735122475},
\]

which is not rational.  Also `O=D A D^(-1)`, so the similarity asserted after (6.1) is over `K`
(or over `R`), not a rational similarity.  This does not alter any rank, PSD, commutant, word
closure, invariant-subspace, or rational-algebra conclusion, because the proposer performs the
rational algebra calculation with the correctly typed matrices `A=G^(-1)H`.

Subject to that correction, this review licenses exactly the following occurrence-side facts at

\[
 (s,a,d,r,q,n,N)=(5,25,21,5,100,550,1100),
 \qquad ad=525,qquad \theta=(519,5,1):
\]

1. the invariant and marked-branch dimensions, including occurrence multiplicity `C_5=7`;
2. the exact James-kernel orbit construction and the physical block-normalizer action;
3. the relative-Jucys--Murphy projectors for the three displayed removable corners, restricted to
   the selected source;
4. all six `7 by 7` rational occurrence forms, their exact ranks and PSD certificates, both eta
   resolutions, and all three full matrix trace identities;
5. the fifteen exact pairwise commutator ranks of the Gram-raised endomorphisms;
6. common commutant dimension `3`, generated unital algebra dimension `27`, two rational common
   invariant lines, central block ranks `1,1,5`, and

\[
 \boxed{\mathcal A_{s=5}\cong
 M_1(\mathbb Q)\oplus M_1(\mathbb Q)\oplus M_5(\mathbb Q)}.
\]

Thus the proposed finite `s=5` extrapolation `M_1(Q) direct-sum M_6(Q)` is false.  The controlling
node nevertheless remains **OPEN**: this review licenses no general-`s` decomposition, asymptotic
claim, alphabet/Pieri assembly, physical NO/YES or left/right transfer, feasibility result, query
bound, numerator bound, or exponent improvement.

## 2. Blind chronology and exact evidence

Before opening any proposer `s=5` artifact, tool, JSON, log, or the canonical node's new `s=5`
paragraphs, the reviewer derived and sealed

`ksum/artifacts/ksum_L3_critical_induced_packet_second_target_s5_occurrence_rule7_hostile_blind_baseline_20260722.md`,
SHA-256
`AE7022D999129D8B4FB432C58EC78B58032F7D2604A6831D1DDC1060A5CA4CC0`.

The hash and completion of that baseline were communicated to the commissioning parent before the
proposer inputs were opened.  The blind construction obtained `C_5=7`, all six ranks, every
commutator rank, commutant dimension `3`, word-closure dimension `27`, two common invariant lines,
and the `1+1+5` rational central decomposition without a desired proposer answer.

The blind driver deliberately used a different `s=5` assembly and gauge.  It imported only the
already reviewed generic orbit/James/marked-JM primitives from the hash-pinned `s=4` reducer; it
did not call or import the proposer `s=5` driver.  Its permanent sources and outputs are:

| Blind evidence | SHA-256 |
|---|---|
| `ksum/artifacts/ksum_L3_s5_occurrence_rule7_independent_blind_model_20260722.py` | `1D6524C94A238585FB253B13BDD37537910CC29723A7A84877160FD1D0E5DEFC` |
| `ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/independent_blind_model.json` | `B0431EFE3EE4183E75A2D1CB2562D59ECA2EE55F2EA3A42BB6FFC256382DEE71` |
| `ksum/artifacts/ksum_L3_s5_occurrence_rule7_independent_projectors_20260722.py` | `0897FD73761872777E6BAE94B5CCCD08E5190DEBAC9D3195414DDCA73FF98EC9` |
| `ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/independent_projectors.json` | `95A2DD8A8022BF122218524A001F7D3E5A8423E5267580212DF125552FE4C2BB` |
| `ksum/artifacts/ksum_L3_s5_occurrence_rule7_independent_low_tail_kostka_20260722.py` | `91A16AD53D40AFDB5E626A557389CEB106E8D4A006FDDF685D00DDC90750B758` |

The post-seal comparison checker reads exact JSON certificates and never imports the proposer
`s=5` tool:

| Comparison evidence | SHA-256 |
|---|---|
| `ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/independent_audit.py` | `2728760D86770091466678A3DB4D3359A054375DF5A4897D6C858BA52605613E` |
| `ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/independent_audit.json` | `7CE910819C12D1AEEE05F1DFE6E38DF76DB5E76749350EA3092D06FA766C5457` |
| `ksum/artifacts/logs_ksum_L3_s5_occurrence_rule7_independent_20260722/independent_audit.log` | `AD8B9335E4487B9D9DA6792E53CC942A0F6488E460675F2B218C2DD300C2A775` |

The log begins `ALL_INDEPENDENT_S5_RULE7_GATES_PASS`, with empty discrepancy and failure lists.  It
certifies exact rational LDL decompositions for all six forms, both resolutions, the three trace
identities, `G`-self-adjointness of all six operators, all central-projector identities, and an
invertible exact simultaneous intertwiner between the blind and proposer six-operator families.
The intertwiner solution space has dimension `3`; the selected intertwiner has a nonzero exact
rational determinant.  Hence the two differently gauged families are exactly, simultaneously
conjugate, not merely equal in a list of scalar invariants.

After that independent comparison, the proposer command was rerun into
`ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_rule7_review_20260722/`.  The fresh JSON is
byte-identical to the original JSON with SHA-256
`11B7C2EF09D38B171C4721452CE4D0D4A4F07C4711282D30A1429CEB95B88933`; the fresh log is
byte-identical to the original log with SHA-256
`06916370884E1AD3F94899DAFD91124F898C4D87792E92ED1A6D022ABDA90583`.

The reviewed proposer inputs are pinned as follows.

| Proposer input | SHA-256 |
|---|---|
| reviewed artifact | `DEB179A24DE6C8722C4F901DF9C1FF8A5F1AFFA99DBA0427DF486B46A05F6352` |
| `ksum/tools/ksum_l3_wreath_occurrence_reducer_s5.py` | `C086195BCB3AF0976CAD84B35750B3B89A4D4D50729B40374816618B2820BAE1` |
| original `run.json` | `11B7C2EF09D38B171C4721452CE4D0D4A4F07C4711282D30A1429CEB95B88933` |
| original `run.log` | `06916370884E1AD3F94899DAFD91124F898C4D87792E92ED1A6D022ABDA90583` |

The labels `T/M/B`, the symbols `H`, `P`, and `J`, and the orbit/James notation coincide with the
proposer notation because both constructions inherit those conventions from the already reviewed
`s=4` package.  That notational coincidence is declared here; it was not copied from the unopened
`s=5` submission.  The two independently produced invariant-line coordinates differ substantially
because the rational gauges differ, while the exact simultaneous intertwiner identifies the same
subspaces.

## 3. Frozen-input scope and independent reconstruction

The following `s=4` inputs were unchanged at the blind freeze point:

| Reviewed `s=4` input | SHA-256 |
|---|---|
| generic reducer `ksum/tools/ksum_l3_wreath_occurrence_reducer.py` | `06B842F0475B85691A76128864BE22D6996BBECDC7A9981FE6111929CA28F371` |
| reviewed first-target artifact | `5A3CEF4C3A26C59FC0EDA3BF6DB1F9490F0D22D5096F9564A5671E400A1D5A91` |
| reviewed first-target JSON | `BAA0501B082D8ACD20A280A363198F68A13B8CD3989F78E7E9BD9B225A52FF16` |
| reviewed first-target log | `323AEBA68F87E24FB40EA51F78DD1304264B2B5E1BA86B0F503666DB061D1C76` |
| first-target independent checker | `A1DC19F3F8CE1198AC8FAA5EBEE9B57EF55C360526C077A1CD8C83ECFA459D39` |
| first-target independent output | `584F509AD728D9BA13FC6183ECA05F992279DC4A4A318C0ACED8E9A3CDEE2CC0` |

Only the characteristic-zero orbit-sum/James-kernel formulas, equivariant block action, and
marked-JM transition mechanism are frozen under their already reviewed scope.  This review does
not grant them immunity outside that scope.  In particular, it independently reopened the new
`c=7` source, the direct `s=5` partition catalogues, all map ranks, all six forms, every eta
identity, all commutators, the common commutant, central projectors, and the generated algebra.  No
`s=4` algebra pattern is load bearing; the blind result actually contradicts the naive `1+6`
extrapolation.

Write

\[
 m=ad=525,\qquad H=S_{21}^{25},\qquad W=H\rtimes S_{25},\qquad
 U_\theta=(S^\theta)^H,
\]

and let `V_25=S^(24,1)` be the `24`-dimensional standard `S_25` module.  The multiplicity space is

\[
 Z=\operatorname{Hom}_{S_{25}}(V_{25},U_\theta),\qquad \dim_{\mathbb Q}Z=c=7.
\]

An independent horizontal-strip recurrence gives

\[
 \dim U_\theta=[s_{(519,5,1)}]h_{21}^{25}=1{,}883{,}700,
\]

and the three marked child counts are

\[
 1{,}883{,}700,\qquad322{,}920,\qquad98{,}280.
\]

The exact hook dimensions are

\[
 f^\theta=139{,}672{,}485{,}907{,}500,
\]

\[
 (f^{\kappa_T},f^{\kappa_M},f^{\kappa_B})=
 (138{,}073{,}135{,}358{,}211,
 1{,}279{,}485{,}207{,}936,
 319{,}865{,}341{,}353),
\]

and the three child dimensions sum to `f^theta`.

The distinguished-block orbit quotient has dimension `64`.  Its five keep-map ranks are
`2,5,11,21,38`, its merge-map rank is `30`, and its `107 by 64` James stack has rank `56`, leaving
an `8`-dimensional kernel.  The full-block quotient has dimension `19`; the corresponding ranks
are `1,2,4,7,12` and `11`, and its `37 by 19` stack has rank `18`, leaving a one-dimensional
kernel.  Since

\[
 \operatorname{Ind}_{S_{24}}^{S_{25}}\mathbf1\cong\mathbf1\oplus V_{25},
\]

the complete standard multiplicity is `8-1=7`, and the selected isotypic carrier has dimension
`24*7=168`.  No favorable copy is selected or discarded.

## 4. Rule-7(a): per-display type audit

For parameter dependence in this finite review, retain the symbols
`m=ad=525`, `a=25`, `d=21`, `r=5`, and `c=dim Z=7`.  The Young permutation carrier for
`theta=(m-r-1,r,1)` has dimension

\[
 \dim M^\theta=m{m-1\choose r}=169{,}559{,}685{,}804{,}600.
\]

Every numbered display in the proposer artifact is audited below.  Scalar shape/count displays are
included so that no implicit carrier change is hidden between operator displays.

| Proposer display | Typed meaning and dimensions | Review result |
|---|---|---|
| (1.1) | Fixed scalar tuple and partition: `m=525`, with `theta=(519,5,1)` a partition of `525`. | Well defined. |
| (1.2) | Six reduced forms act on `c=7` multiplicity coordinates.  `H` is in `Bil_Q(Z)` and `A=G^(-1)H` is in `End_Q(Z)`; the radical-normalized `O` is in `End_K(Z tensor K)`, all `7 by 7`. | **Minor field correction:** `O in End(Q^7)` is false in general. |
| (1.3) | `C_5=dim_Q Hom_(S_25)(V_25,U_theta)=c=7`, a scalar multiplicity. | Exact. |
| (1.4) | Isomorphism of finite-dimensional unital associative `Q`-algebras inside `End_Q(Z)=M_7(Q)`. | Exact after using the rational `A` family. |
| (1.5) | Two one-dimensional `Q`-subspaces of the proposer's pre-Gram--Schmidt copy `Z_0=Q^7`. | Exact; gauge-dependent coordinates, invariant subspaces. |
| (2.1) | Common-kernel subspace identity in `M^theta`: `S^theta=(intersection_(v=0)^4 ker psi_(1,v)) intersection ker psi_(2,0)`. | Exact in characteristic zero. |
| (2.2) | Scalar dimension of the labelled `H`-orbit carrier: `a binom(a+r-1,r)=25 binom(29,5)=2,968,875`. | Exact; no dense carrier is built. |
| (2.3) | Restricted James stacks `Q^64 -> Q^107` and `Q^19 -> Q^37`, of ranks `56` and `18`. | Exact matrix ranks. |
| (2.4) | Fixed subspaces `(S^theta)^(H semidirect S_24)` and `(S^theta)^(H semidirect S_25)` have dimensions `8` and `1`. | Exact. |
| (2.5) | Multiplicity difference `8-1=c=7`, justified by `Ind_(S_24)^(S_25) 1 = 1 direct-sum V_25`. | Exact and complete. |
| (2.6) | Four scalar symmetric-function coefficients for partitions of `525` or `524`; values `1,883,700`, `1,883,700`, `322,920`, `98,280`. | Independently reproduced. |
| (3.1) | Each `s_i`, `1<=i<=24`, is in `End_Q(M_H)` for the `2,968,875`-dimensional labelled orbit carrier; it descends through the equivariant James kernel to `End_Q(U_theta)`. | Exact index-permutation identities; block permutations normalize `H=S_21^25`. |
| (3.2) | Positive integer local orbit-weight factor `binom(21,c_i) binom(21-c_i,b_i)` with `c_i in {0,1}`, `sum c_i=1`, `sum b_i=5`, and `b_i+c_i<=21`. | Exact; the two swapped factors exchange, so the full diagonal Gram is preserved. |
| (4.1) | `J_x=sum_(y != x)(x y)` is in `End_Q(M_mark)` for the `121`-dimensional marked orbit quotient; `H'=S_20 times S_21^24` permutes the summands and makes the descent well defined. | Exact, with `J_x^T G_mark=G_mark J_x`. |
| (4.2) | Three scalar contents `518,3,-2` of the removable boxes of `theta`. | Exact and distinct. |
| (4.3) | Each displayed polynomial is a rational endomorphism of `Q^121`.  Its branch-projector identities are asserted only after composition with the source embedding `B:Q^7 -> Q^121`. | Exact on all seven columns. |
| (4.4) | Correct typed reading is `(P_T+P_M+P_B)B=B` in `Hom_Q(Q^7,Q^121)`, not a global equality to `I_121` on every marked permutation summand. | Prose supplies the restriction; no defect. |
| (5.1) | Seven positive rational scalars `n_i`; `G=diag(n_i)` is a nonsingular symmetric form in `Bil_Q(Z)`, dimension `7 by 7`. | Exact. |
| (5.2) | With the embedding suppressed, `H^1_kappa[i,j]=<P_kappa Bv_i,P_kappa Bv_j>_(G_mark)` is a rational symmetric bilinear form `Z times Z -> Q`. | Exact. |
| (5.3) | With `D=diag(sqrt(n_i))`, `O=D^(-1)HD^(-1)` is a `7 by 7` symmetric matrix over `K subset R`. | **Minor field correction;** formula and normalization are otherwise exact. |
| (5.4) | `S_25`-module restriction `V_25 downarrow S_24 = 1 direct-sum V_24`, dimensions `24=1+23`; after tensoring with `Z`, eta sectors have dimensions `7` and `161`. | Exact. |
| (5.5) | Equality in `Bil_Q(Z)`: `H^1_kappa+23 H^V24_kappa=24(f^kappa/f^theta)G`; both sides are rational `7 by 7` forms. | Exact for all three corners at matrix level. |
| (5.6) | Four positive integer Specht dimensions; `sum_kappa f^kappa=f^theta`. | Exact hook calculation. |
| unnumbered rank table after (5.6) | Ranks of six forms on `Z`: `(7,7),(5,7),(6,7)` for `T,M,B` and eta `1,V24`. | Exact rational LDL certificates. |
| (5.7) | Two identities in `Bil_Q(Z)`, each a sum of three `7 by 7` forms equal to `G`. | Both exact on all seven columns. |
| (6.1) | In the rational pre-orthogonal basis, `G_0,H_0 in M_7(Q)`, `G_0` nonsingular, and `A=G_0^(-1)H_0 in End_Q(Z_0)` with `A^T G_0=G_0 A`. | Exact.  Similarity to `O` is over `K`, not rational. |
| unnumbered commutator table | Fifteen commutators in `End_Q(Z_0)`.  Three same-corner ranks are `0`; all twelve different-corner ranks are `2`. | Exact, including nonzero `2 by 2` minors for the rank-two cases. |
| (6.2) | `A'={X in End_Q(Z_0): XA_i=A_iX for all i}` is the kernel of a rational linear system on `49=c^2` unknowns.  System rank `46`, kernel dimension `3`. | Exact. |
| (6.3) | Characteristic polynomial of a `G_0`-self-adjoint `X in A' subset End_Q(Z_0)`.  Its rational eigenspaces have dimensions `5,1,1`. | Exact; the three eigenvalues are distinct and rational. |
| (6.4) | The unital `Q`-span of words in the six `A` operators is a subalgebra of `End_Q(Z_0)` of dimension `27=5^2+1^2+1^2`. | Exact word closure. |

For completeness, the ambient James maps suppressed by proposer display (2.1) are

\[
 \psi_{1,v}:M^{(m-r-1,r,1)}\longrightarrow M^{(m-v-1,v,1)},
 \qquad 0\le v<r,
\]

and

\[
 \psi_{2,0}:M^{(m-r-1,r,1)}\longrightarrow M^{(m-r-1,r+1)}.
\]

At `m=525,r=5`, the five keep-target dimensions are
`525`, `275,100`, `71,938,650`, `12,517,325,100`, and `1,630,381,594,275`; the merge target has
dimension `28,259,947,634,100`.  On the distinguished quotient, the restricted matrix shapes are
`2,5,11,21,38 by 64` and `30 by 64`; on the full quotient they are `1,2,4,7,12 by 19` and
`11 by 19`.  Thus the common-kernel statement is typed at both ambient and reduced levels.

The normalizer issue that motivated Rule 7 is also explicit here.  A physical permutation of the
twenty-five equal-size blocks conjugates `S_21^25` to itself and hence acts on `U_theta`; after a
point in block zero is fixed, the other-block group `S_24` normalizes
`S_20 times S_21^24`.  The selected eta maps therefore compose on the claimed multiplicity
carrier.  No `f^theta`-dimensional Specht frame is mistaken for the `c=7` multiplicity factor.

## 5. Rule-7(b): regime-complete identity gates

The stated second target is genuinely matrix-valued with `c=7`.  The review exercises, at exact
identity level:

- all seven multiplicity columns, not a trace or one selected column;
- all three corners
  `kappa_T=(518,5,1)`, `kappa_M=(519,4,1)`, `kappa_B=(519,5)`;
- both eta sectors `1` and `V_24`, of full selected dimensions `7` and `161`;
- all six rational forms and six exact PSD/rank gates;
- both three-corner resolutions and all three eta trace identities as `7 by 7` residuals;
- all fifteen pairwise commutators, including the three zero and twelve rank-two regimes;
- the full common-commutant, central-projector, and word-closure identities.

The previously reviewed small dense gate covers the literal tabloid/marked-transposition mechanism
in a `c=1` regime.  The present review reopens the qualitatively different `c=7` regime in full.
No claimed multiplicity, corner, or eta branch remains tested only by an aggregate trace.

NO/YES, left/right, status/path, alphabet-parent, Pieri-path, distinct-mark, transfer, and physical
query regimes are not declared tested.  They are outside the exact occurrence-only statement and
remain open obligations of the controlling node.

## 6. Formula audit and hostile failure modes

### 6.1 Full central sum and eta normalization

Fix a point `x` among the `m=525` underlying points.  On the irreducible `S^theta` carrier, the
relative branch projector `P_(kappa,x)` has trace `f^kappa`.  The full point sum, not a sum over
block colors, is central in `Q[S_525]`; Schur's lemma and traces give

\[
 \sum_{x=1}^{525}P_{\kappa,x}
 =525{f^\kappa\over f^\theta}I_{S^\theta}.
\]

The wreath group `S_21^25 semidirect S_25` is transitive on all `525` points.  Taking the partial
trace over the complete `24`-dimensional `V_25` factor makes the `525` equal conjugate terms cancel
the `525` in the central scalar, yielding

\[
 \operatorname{Tr}_{V_{25}}P_{\kappa,x}
 =24{f^\kappa\over f^\theta}I_Z.
\]

Under `V_25 downarrow S_24=1 direct-sum V_24`, and with each reduced eta form normalized by
`1/dim(eta)`, this is exactly

\[
 H^\mathbf1_\kappa+23H^{V_{24}}_\kappa
 =24{f^\kappa\over f^\theta}G.
\]

This derivation accounts separately for `525`, `24`, and `23`; the factors `25` and `21` enter the
transitive `525=25*21` point orbit.  There is no colored-block sum standing in for the full central
sum, and there is no dropped or extra `dim(eta)` factor.  Exact comparison verifies the resulting
identity for every entry of all three `7 by 7` matrices.

### 6.2 Projector scope, Gram, and PSD

The polynomials in (4.3) are evaluated exactly, with denominators
`267800`, `-2575`, and `2600`.  The checked statements are

\[
 (J_x-c_\kappa I)P_\kappa B=0,
 \qquad P_\kappa^2B=P_\kappa B,
 \qquad P_\kappa P_{\kappa'}B=0\quad(\kappa\ne\kappa'),
\]

and

\[
 (P_T+P_M+P_B)B=B.
\]

No global `I_121` claim is licensed on unrelated marked-permutation summands.

All adjoints use the exact positive orbit Gram.  Raw matrices `H` are bilinear forms, so products
`H_i H_j` would be basis-dependent and are not used.  Every algebra calculation instead uses the
Gram-raised endomorphism `A_i=G^(-1)H_i`.  The independent checker supplies exact rational LDL
certificates with positive pivots and zero remainders, giving PSD and ranks

\[
 (7,7,5,7,6,7)
\]

in the order `T1,TV24,M1,MV24,B1,BV24`.  No floating eigenvalue or tolerance makes a decision.
The proposer's characteristic-polynomial test is also valid: for a real symmetric matrix with
eigenvalues `lambda_i`, nonnegativity of all elementary symmetric coefficients is equivalent to
the polynomial `product_i(t+lambda_i)` having no positive root, hence to every `lambda_i>=0`.

### 6.3 Exact rational algebra classification

Commutator ranks alone do not determine a generated algebra.  The review additionally checks:

1. the exact `49`-unknown commutant system has rank `46` and nullity `3`;
2. its rational basis is commutative;
3. a rational `G_0`-self-adjoint separator has three rational eigenspaces of dimensions `1,1,5`;
4. the corresponding rational projectors are idempotent, pairwise orthogonal, sum to `I_7`, are
   `G_0`-self-adjoint, and commute with all six generators;
5. exact word closure has dimension `27`.

The generated algebra is contained in the rational block algebra
`M_1(Q) direct-sum M_1(Q) direct-sum M_5(Q)`, whose dimension is at most
`1^2+1^2+5^2=27`.  Equality of the exact word-closure dimension forces equality with that full
block algebra.  This proves the displayed rational algebra type without floating spectral
clustering or a rank-only inference.

### 6.4 Standing failure-mode disposition

- **Dropped or extra normalization:** the point-orbit, eta-dimension, Gram, hook-ratio, and
  central-sum factors `21`, `25`, `525`, `24`, and `23` are derived above; both resolutions pass.
- **Type or dimension mismatch:** Section 4 audits every proposer display and finds the one minor
  rational-versus-algebraic field annotation.  All source, marked, eta, and multiplicity dimensions
  otherwise compose.
- **Undefined terms or missing stability ranges:** no stability range is used.  All positive terms
  are defined in Section 8 at one finite tuple.
- **Colored-orbit sum substituted for a full central sum:** Section 6.1 derives the complete sum
  over all `525` points before reduction.
- **Numerics matching values while printed derivation is broken:** exact construction agreement is
  separated from the human formula/type audit in Section 7; the field defect is reported rather
  than repaired by matching outputs.
- **Wrong inner product:** marked self-adjointness, source orthogonality, and all raised operators
  use the invariant Gram, never an unjustified Euclidean transpose.
- **Raw-form multiplication:** commutants and commutators use `G^(-1)H`, not products of `H` forms.
- **Rank substituted for algebra:** the exact commutant, rational central projectors, and word
  closure supply the algebra proof.
- **Floating spectral decisions:** all decisive arithmetic is integer or rational; radicals occur
  only in the corrected orthonormal presentation.
- **Finite-to-uniform inference:** Section 8 expressly withholds it.

## 7. Rule-7(c), (d), (f), and (g)

### 7(c) Anchoring ban

The SHA-pinned hostile baseline and blind outputs in Section 2 predate inspection of the proposer
`s=5` proof and code.  The baseline fixed the spaces, normalization, dimensions, required identity
gates, exact algebra proof obligations, and exclusions before comparison.  The shared notation is
the inherited reviewed `s=4` notation and has been explicitly flagged.

### 7(d) No frozen-input immunity

Section 3 states exactly which already reviewed generic primitives were reused and verifies their
hashes.  Every `s=5`, `c=7`, matrix-level, and algebra-level consequence was reopened.  Neither the
reviewed `s=4` algebra nor any aggregate packet claim is treated as frozen evidence for this new
finite algebra.

### 7(f) Value-versus-formula decoupling

Four evidence layers are kept distinct.

1. The fresh proposer rerun executes the formulas actually implemented by the submitted tool and
   reproduces the submitted JSON and log byte for byte.  This establishes reproducibility of the
   implementation, not by itself correctness of the prose.
2. The pre-inspection blind driver, low-tail recurrence, and rational projector splitter construct
   the same finite object through a separate `s=5` assembly and a different rational gauge.  This
   independently corroborates the mathematical values but shares only the explicitly frozen
   generic `s=4` primitives.
3. The post-seal audit compares the two exact objects, supplies exact LDL and central-projector
   certificates, and solves an invertible simultaneous rational intertwiner for all six operators.
   This is stronger than matching scalar outputs, but still would not repair a bad printed formula.
4. Sections 4 and 6 directly audit the printed domains, codomains, normalization, central-sum
   derivation, projector restriction, PSD logic, and rational algebra proof.  That audit finds and
   isolates the minor field annotation while validating the corrected formulas.

Accordingly, the verdict is not inferred from numerical agreement.  The constructed values and
the printed derivation were checked separately.

### 7(g) Quantifier hygiene

In this review:

- `second target` means only `(s,a,d,r,q,n,N)=(5,25,21,5,100,550,1100)`;
- `corner` means one of the three removable boxes giving exactly
  `(518,5,1)`, `(519,4,1)`, or `(519,5)`;
- `V_24` means the `23`-dimensional standard `S_24` module `S^(23,1)`;
- `same-kappa` means the three pairs differing only in eta;
- `different-kappa` means the other twelve unordered pairs among the six matrices;
- `occurrence algebra` means the unital `Q`-algebra generated by the six
  `A_(kappa,eta)=G^(-1)H_(kappa,eta)` on this one `Z`;
- `PSD`, `rank`, `commutant`, and `generated algebra` mean exact characteristic-zero statements,
  with no numerical tolerance.

No undefined `admissible`, `strict`, `active`, `taper`, or `stable` range enters the licensed
statement.

## 8. Banked finite result and stopping point

With the field correction in Section 1, the following finite table is reviewed:

| Corner | `eta=1` rank | `eta=V_24` rank |
|---|---:|---:|
| `T=(518,5,1)` | 7 | 7 |
| `M=(519,4,1)` | 5 | 7 |
| `B=(519,5)` | 6 | 7 |

The three same-corner commutators vanish; every different-corner commutator has exact rank `2`.
The common rational central blocks have dimensions `1,1,5`, and the generated algebra is
`M_1(Q) direct-sum M_1(Q) direct-sum M_5(Q)`.

This is an exact finite occurrence reducer only.  The provisional general-`s` pattern recorded
elsewhere in the open canonical node is not reviewed here and may not cite this artifact as a
uniform proof.  This review explicitly withholds every general-`s` formula, asymptotic statement,
physical alphabet/Pieri assembly, physical transfer matrix, feasibility conclusion, query bound,
numerator bound, and exponent claim.

The complete SHA-256 evidence manifest is stored beside the fresh rerun under
`ksum/artifacts/logs_ksum_L3_wreath_occurrence_reducer_s5_rule7_review_20260722/manifest.json`.
