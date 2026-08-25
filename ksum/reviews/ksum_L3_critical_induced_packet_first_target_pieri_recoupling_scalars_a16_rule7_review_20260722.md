# Fresh Rule-7 review: first-target Pieri recoupling scalars at `a=16`

Date: 2026-07-22  
Controlling node (not edited by this reviewer):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_20260722.md`  
Observed SHA-256:
`07EF9D8E3BBC901B19E74D1F457C7E7BF0BD0607B14FF6B629A8EB60640012DC`

Reviewed tool:
`ksum/tools/ksum_l3_first_target_pieri_scalars.py`  
Observed SHA-256:
`11019D7CE0D289A76260D1EB0724059698611AD1A4C7D2E7F82DB7CB07F88048`

Reviewed JSON:
`ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_a16_20260722.json`  
Observed SHA-256:
`6C91B3C8D83EBFA0FF02DED17BE429DFB104CECA98C7A31DED685E257B544EBA`

Reviewed SHA manifest:
`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_20260722.sha256`  
Observed SHA-256:
`3AC77F0E315EE6EC3EECE43E13393A957E9A5EB00518EB14C952C0569C5D8BA8`

All four observed hashes equal the commissioned hashes, and every entry in the manifest equals the
current on-disk hash.

## 1. Verdict first

**Overall verdict: MINOR / SCOPED PASS for the finite, explicitly transported position-scalar
table, with a mandatory operator-formula correction.**

The review independently reconstructs and licenses, only at

\[
(s,a,d,r,n)=(4,16,17,4,288),
\qquad
(\theta,\lambda)=((267,4,1),(283,4,1)),
\]

the following facts:

1. the three exact skew-Specht interval dimensions are `1/17/17`;
2. the Young orthogonal generators, orthonormal inner product, Coxeter relations, and normalized
   positive-leading Pieri lines are exact;
3. the word `s_16 s_15 ... s_1` under rightmost-factor-first multiplication is the stated
   order-preserving map `1 -> 17`, `j -> j-1`;
4. after the heavy-coordinate transporter is inserted, every listed NO/YES heavy coefficient,
   its positive sign, and its rational square agree exactly with an independent construction;
5. the legal/zero path inventory is complete, and the transported NO and YES square sums are one
   for each `kappa`;
6. the rare/common/residual coefficients are one, and the separately stated status masses resolve
   exactly;
7. `p`, status mass `w`, occurrence matrices `O`, and alphabet matrices `C` remain separate.

One displayed-identification claim is not correct literally.  The planning equations (5.4) and
(5.6), which the proposer says the transported inner products “realize,” contain no transporter.
Their literal coefficients are the proposer's own no-transport values, not the main table.  The
correct finite physical identities must insert `rho_lambda(g)` as in Section 5 below.  This is a
mandatory correction, but it is local to the operator display: the proposer already constructs
`u_kappa=rho(g)v_kappa`, and all of its main numerical values are exactly the values of the
corrected transported identities.  No scalar value, sign, legal path, or transported resolution
changes.

There are three additional local qualifications:

- the endpoint transposition `(272,288)` is a different permutation from the order-preserving
  long cycle, but it produces **exactly the same transported vector and the same entire p-table**;
  the order-preserving representative is a valid deterministic choice, not a scalar-level
  necessity;
- the no-transport deficient sums are sums of projections onto normalized Pieri **lines**, not
  the resolution of the full last-letter branch projectors on the entire `17`-dimensional skew
  space;
- two TeX tokens in the proposer artifact, at lines containing
  `dim H_(kappa_T)=1,qquad` and `dim H_(kappa_M)=17,qquad`, are missing a backslash.  No C0 control
  character occurs in the proof, tool, or JSON.

The controlling node remains **OPEN**.  This review licenses no occurrence/alphabet/Pieri
assembly, no physical Gram or effect, no commutator, no attenuation, no numerator, no uniform
critical-family formula, and no exponent.

## 2. Freshness, blindness, and evidence

Before opening the proposer proof, tool, JSON, or manifest, the reviewer read
`DAG_PROTOCOL.md` and `research/RESEARCH_STRUCTURE_PROTOCOL.md`, resolved the existing
controlling node, and archived the independent hostile baseline

`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_rule7_hostile_baseline_20260722.md`

with SHA-256
`B03A123874ABDA0F53B938B6F999CAD0AA71CF77D5BD8A6720A9BCC535A54113`.
The baseline independently fixed the three source shapes, the `1/17/17` dimensions, the complete
last-corner rank table, the need for a physical heavy-coordinate alignment, the group-word and
normalization gates, and the no-transport and endpoint-transposition attacks.  It did not assume
the proposed coefficients or a favorable verdict.

The fresh independent checker is

`ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_rule7_review_20260722/independent_review_check.py`

with SHA-256
`ACCDF68F0D4C36DFF1FF33C524993941A9C5421793DE4BCAD3C6DF14FA268A94`.
It does not import the proposer.  Instead of copying the proposer's generic saturated-chain
enumerator, it uses the special linear-extension model of a 17-box row and a 16-box row plus one
incomparable cell.  Its exact output is

`ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_rule7_review_20260722/independent_review.json`

with SHA-256
`44961985ADD59EE13C743BF5182C47A9E39486E205B2D640D3E50B6517C1FC26`
and result `ALL_INDEPENDENT_FINITE_RECONSTRUCTION_GATES_PASS`.

A fresh proposer verification run used

```text
python ksum/tools/ksum_l3_first_target_pieri_scalars.py --verify-log ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_a16_20260722.json
```

and returned `ARCHIVED_PIERI_RESULT_VERIFIED`.  The command record is
`ksum/artifacts/logs_ksum_L3_first_target_pieri_scalars_rule7_review_20260722/fresh_proposer_verify.txt`,
SHA-256
`EB770D6746CB8F3D9511141A9424DE05132050B6B0C8BC6F914382F126D5F468`.

## 3. Independent shape and representation reconstruction

The removable children of `theta` are

\[
\kappa_T=(266,4,1),\qquad
\kappa_M=(267,3,1),\qquad
\kappa_B=(267,4).
\]

For

\[
\mathcal H_\kappa
=\operatorname{Hom}_{S_{271}}
\left(S^\kappa,\operatorname{Res}^{S_{288}}_{S_{271}}S^\lambda\right),
\]

the commuting action of the last seventeen letters makes this the skew module
`S^(lambda/kappa)`.  The three skew shapes are a 17-box row, a 16-box row plus the cell `(2,4)`,
and a 16-box row plus the cell `(3,1)`.  Hence

\[
\dim\mathcal H_{\kappa_T}=1,
\qquad
\dim\mathcal H_{\kappa_M}=17,
\qquad
\dim\mathcal H_{\kappa_B}=17.
\]

In either 17-dimensional case, a tableau is determined by the label placed in the incomparable
cell.  This gives an independent 17-vector basis without traversing the proposer's code.  With

\[
\delta_i(T)=c_T(i+1)-c_T(i)
\]

and positive off-diagonal square root, the independently built real matrices satisfy exactly

\[
\rho(s_i)^T=\rho(s_i),\qquad
\rho(s_i)^2=I,
\]

every braid identity and every far-commutation identity.  Therefore the standard tableau basis is
orthonormal and the action is genuinely orthogonal, not merely numerically close to orthogonal.

The source line is the path in which label `1` fills `theta/kappa` and labels `2,...,17` fill the
top strip increasingly.  Its unit vector `v_kappa` is fixed by `s_2,...,s_16`.  Every NO target
line is the unique unit `S_16`-fixed vector after label `17` is fixed in `lambda/beta`.  Every YES
target line is the unique unit `S_15`-fixed vector after labels `17` and `16` are fixed in
`lambda/beta` and `beta/xi`.  Independent nullspace calculations give dimension one in every
legal case and fix the first nonzero tableau coefficient positive.

The legal target support sizes are:

| `kappa` | NO target support | YES target support |
|---|---|---|
| `kappa_T` | `beta_T:1` | `beta_T/xi_T:1` |
| `kappa_M` | `beta_T:16`, `beta_M:1` | `beta_T/xi_T:15`, `beta_T/xi_M:1`, `beta_M/xi_M:1` |
| `kappa_B` | `beta_T:16`, `beta_B:1` | `beta_T/xi_T:15`, `beta_T/xi_B:1`, `beta_B/xi_B:1` |

The lines within each fixed `kappa` are mutually orthonormal because their fixed last-label data
have disjoint tableau support.

## 4. Transport and the endpoint-transposition attack

Under the ordinary convention that the rightmost factor acts first,

\[
g=s_{16}s_{15}\cdots s_1
\]

is operationally evaluated by applying `s_1,s_2,...,s_16`, and its label map is exactly

\[
g(1)=17,
\qquad
g(j)=j-1\quad(2\le j\le17).
\]

Thus the absolute-label word is `s_287 ... s_272`, and it fixes the first `271` physical
coordinates.  The independent checker verifies the label map, exact unitarity, and

\[
u_\kappa=\rho_\kappa(g)v_\kappa,
\qquad
\rho_\kappa(s_i)u_\kappa=u_\kappa\quad(1\le i\le15).
\]

The proposed text correctly says that this long cycle is not the group element `(1,17)`.
However, the suggestion that an endpoint transposition is not usable for this scalar table is too
strong.  If `h(1)=17` is any other representative, then

\[
g^{-1}h\in S_{\{2,\ldots,17\}},
\]

and that subgroup fixes `v_kappa`.  Consequently

\[
\rho_\kappa(h)v_\kappa
=\rho_\kappa(g)\rho_\kappa(g^{-1}h)v_\kappa
=\rho_\kappa(g)v_\kappa.
\]

In particular, the independent exact endpoint-transposition run agrees vector-for-vector, not
only after squaring, with the order-preserving run for every `kappa`.  The deterministic long cycle
is still a legitimate and convenient coordinate convention.  What is essential is sending the
heavy label to the last position; this finite Pieri scalar is independent of the representative
because of source-line invariance.

The inverse long cycle does **not** send label `1` to `17`.  Its table agrees here with the
identity/no-transport diagnostic and fails the middle/bottom fixed-line resolutions, as expected.

## 5. Mandatory correction to equations (5.3)--(5.6)

Embed the relative permutation `g` in `S_288`, fixing labels `1,...,271`.  Under the declared left
action, the heavy NO identity computed by the tool is

\[
\boxed{
(\iota_{\kappa,16}^{\beta})^*
b_{\lambda\to\beta}\,
\rho_\lambda(g)I_0
=p^{0,H}_{\beta,\kappa}\,b_{\theta\to\kappa}.}
\tag{R5.4}
\]

The heavy YES identity is

\[
\boxed{
(\iota_{\kappa,15}^{\xi})^*
(\iota_{\xi,1}^{\beta})^*
b_{\lambda\to\beta}\,
\rho_\lambda(g)I_1
=p^{1,H}_{\beta,\kappa,\xi}\,b_{\theta\to\kappa}.}
\tag{R5.6}
\]

Because `g` fixes `S_271`, each left-hand side is an `S_271`-intertwiner from `S^theta` to
`S^kappa`; the branching Hom space is one-dimensional, so it is a scalar multiple of the stated
normalized `b_(theta->kappa)`.  Passing to the skew multiplicity space gives exactly the
proposer's inner product with `rho_kappa(g)v_kappa`.

By contrast, planning (5.4) and (5.6) omit `rho_lambda(g)`.  Their literal multiplicity-space
coefficient is the overlap with `v_kappa`, not with `u_kappa`.  The difference is exact and large:

| literal no-transport branch | coefficient square |
|---|---:|
| NO `kappa_M,beta_T` | `7/106` |
| NO `kappa_M,beta_M` | `0` |
| NO `kappa_B,beta_T` | `71/1076` |
| NO `kappa_B,beta_B` | `0` |
| YES `kappa_M,xi_T,beta_T` | `93/1325` |
| other YES `kappa_M` lines | `0` |
| YES `kappa_B,xi_T,beta_T` | `283/4035` |
| other YES `kappa_B` lines | `0` |

Thus the sentence that the transported computation literally realizes the uncorrected (5.4) and
(5.6) is false as printed.  Equations (R5.4) and (R5.6) are the reviewed physical theorem.

Equation (5.3) is an endomorphism of `S^theta` and remains the unique all-top rare path with
coefficient one.  Equation (5.5) is also an endomorphism of `S^theta`; a physical
residual-to-last representative can be written explicitly, but it acts trivially on the
one-dimensional all-top interval, so the residual coefficient remains one.  Removing the common
singleton from the ordered YES attachment likewise gives coefficient one.  This explains why the
transport omission is visible only on the heavy formulas in this finite table.

## 6. Independently verified exact table

The rare/common/residual coefficients are all `+1`.  For the transported NO heavy paths, the
independent result is

\[
\begin{array}{c|c|c}
\kappa&\beta&p^2\\ \hline
\kappa_T&\beta_T&1\\
\kappa_M&\beta_T&2/9275\\
\kappa_M&\beta_M&9273/9275\\
\kappa_B&\beta_T&4/19099\\
\kappa_B&\beta_B&19095/19099.
\end{array}
\]

For transported YES heavy paths it is

\[
\begin{array}{c|c|c|c}
\kappa&\xi&\beta&p^2\\ \hline
\kappa_T&\xi_T&\beta_T&1\\
\kappa_M&\xi_T&\beta_T&1/4929\\
\kappa_M&\xi_M&\beta_T&11/862575\\
\kappa_M&\xi_M&\beta_M&9273/9275\\
\kappa_B&\xi_T&\beta_T&15/76127\\
\kappa_B&\xi_B&\beta_T&67/5405017\\
\kappa_B&\xi_B&\beta_B&19095/19099.
\end{array}
\]

Every independently reconstructed overlap is positive in the stated positive-leading gauge, so
`p=+sqrt(p^2)` in every nontrivial entry.  Every listed entry is exactly nonzero.

The exhaustive shape tests give exactly five legal NO heavy pairs out of nine and seven legal YES
heavy triples out of twenty-seven.  The other four NO pairs and twenty YES triples have zero path
space because containment, the required horizontal strip, or a required one-box difference fails.
The independent inventory equals the proposer JSON exactly.

The transported line vectors resolve the relevant invariant state, giving

\[
\frac2{9275}+\frac{9273}{9275}=1,
\qquad
\frac4{19099}+\frac{19095}{19099}=1,
\]

\[
\frac1{4929}+\frac{11}{862575}+\frac{9273}{9275}=1,
\]

\[
\frac{15}{76127}+\frac{67}{5405017}+\frac{19095}{19099}=1.
\]

The `kappa_T` resolutions are `1=1`.  Separately,

\[
\frac1{18}+\frac{17}{18}=1,
\qquad
\frac1{288}+\frac{15}{288}+\frac{17}{18}=1.
\]

These are respectively Pieri-line and status-weight resolutions.  They do not insert occurrence
or alphabet normalization.

### Correct interpretation of the no-transport diagnostic

For `kappa_M` and `kappa_B`, the full last-letter branch `beta_T` has rank `16`, and the source
`v_kappa` lies in that branch.  The scalar `p`, however, is its overlap with the unique normalized
`S_16`-fixed target line inside that branch.  Hence the deficient no-transport sum does not say
that the full last-letter projectors fail to resolve the 17-dimensional space.  It says that the
untransported source is not in the sum of the target invariant lines appropriate to the physical
heavy-to-last map.  The proposer's numerical diagnostic is correct; the word “projectors” must be
read as these rank-one Pieri-line projectors, not as the full last-corner projectors.

## 7. Rule 7(a): complete type and dimension audit

There is no hidden LR multiplicity parameter in this finite position-only calculation.  The only
nontrivial multiplicity-space dimensions are exactly `1/17/17`; the occurrence multiplicity
`C_r=4` does not enter `p`.

The exact carrier dimensions used in the type audit are:

| shape | size | Specht dimension |
|---|---:|---:|
| `theta=(267,4,1)` | 272 | `46,937,442,816` |
| `lambda=(283,4,1)` | 288 | `62,660,742,144` |
| `beta_T=(282,4,1)` | 287 | `61,569,010,503` |
| `beta_M=(283,3,1)` | 287 | `818,808,991` |
| `beta_B=(283,4)` | 287 | `272,922,650` |
| `xi_T=(281,4,1)` | 286 | `60,492,548,688` |
| `xi_M=(282,3,1)` | 286 | `807,356,550` |
| `xi_B=(282,4)` | 286 | `269,105,265` |
| `kappa_T=(266,4,1)` | 271 | `46,071,366,111` |
| `kappa_M=(267,3,1)` | 271 | `649,566,675` |
| `kappa_B=(267,4)` | 271 | `216,510,030` |

Every displayed operator identity in scope has the following type.

| object/display | domain -> codomain | matrix dimensions |
|---|---|---|
| `rho_kappa(s_i)`, `rho_kappa(g)` | `H_kappa -> H_kappa` | `m_kappa x m_kappa`, `m=(1,17,17)` |
| `I_0=iota_(theta,16)^lambda` | `S^theta -> S^lambda` | `f^lambda x f^theta` |
| `iota_(theta,15)^beta` | `S^theta -> S^beta` | `f^beta x f^theta` |
| `I_1=iota_(beta_T,1)^lambda iota_(theta,15)^(beta_T)` | `S^theta -> S^lambda` | factors `f^lambda x f^(beta_T)` and `f^(beta_T) x f^theta` |
| `b_(lambda->beta)` | `S^lambda -> S^beta` | `f^beta x f^lambda` |
| (5.3) | `S^theta -> S^theta` | `f^theta x f^theta` |
| `iota_(kappa,16)^beta` | `S^kappa -> S^beta` | `f^beta x f^kappa` |
| corrected (R5.4) and `b_(theta->kappa)` | `S^theta -> S^kappa` | `f^kappa x f^theta` |
| `iota_(xi,1)^beta` | `S^xi -> S^beta` | `f^beta x f^xi` |
| `iota_(theta,14)^xi` | `S^theta -> S^xi` | `f^xi x f^theta` |
| (5.5) | `S^theta -> S^theta` | `f^theta x f^theta` |
| `iota_(kappa,15)^xi` | `S^kappa -> S^xi` | `f^xi x f^kappa` |
| corrected (R5.6) and `b_(theta->kappa)` | `S^theta -> S^kappa` | `f^kappa x f^theta` |
| `v_kappa`, `u_kappa`, each target line | `R -> H_kappa` | `m_kappa x 1` |
| each line projector | `H_kappa -> H_kappa` | `m_kappa x m_kappa` |
| `sum_kappa b^*b=I` | `S^theta -> S^theta` | `f^theta x f^theta` |

All adjoints use the orthonormal Young basis.  Every product is well defined.  The corrected
transporter acts on `S^lambda`, not on the `S^theta` or `S^kappa` carrier, and it fixes the subgroup
`S_271` required for the one-dimensional branching-Hom argument.

## 8. Rule 7(b)--(g)

### 7(b): regime-complete identity gates

The independent exact gates cover all three skew multiplicity dimensions, all three `kappa`
branches, all three last corners, all five legal NO heavy pairs, all seven legal YES heavy triples,
the four/20 illegal inventories, the rare/common/residual lines, the identity/no-transport case,
the order-preserving move, its inverse, and the endpoint transposition.  Identity-level gates
include every Coxeter relation, fixed-line invariance, unit norm, orthogonality, exact overlap, and
per-`kappa` resolution.  No qualitative finite position branch in the claim is untested.

The review does not silently promote the single `a=16` instance to the whole `s>=4` family.

### 7(c): anchoring ban

The blind hostile baseline was archived before opening the proposal.  The independent checker was
then written from the special linear-extension model and does not import or call any proposer
function.  Its basis construction and explicit endpoint-transposition comparison are absent from
the proposer tool.  Notation coincides only where the reviewed claim fixes the shape names.

### 7(d): no frozen-input immunity

The planning artifact is proposer-tier and was reopened for the exact use made here.  In
particular, its (5.4)/(5.6) displays fail literally and are replaced by (R5.4)/(R5.6).  No reviewed
occurrence or alphabet result is used to infer a Pieri value, a physical alignment, or an assembly.

### 7(e): standing failure-mode list

- **Dropped/extra normalization:** unit lines, orthogonal supports, all p-square sums, and both
  status sums are exact.  No factor `17`, `16`, `15`, Specht dimension, coevaluation dimension,
  or status probability is absorbed into `p`.
- **Type/dimension mismatch:** Section 7 audits every map, including the mandatory location of
  `rho_lambda(g)`.
- **Undefined terms/stability:** “first target” is the one displayed finite tuple; “legal path” is
  resolved by containment/horizontal-strip/one-box tests; “positive-leading” fixes the first
  nonzero coefficient in the declared tableau order; “transported” means (R5.4)/(R5.6).
- **Colored/full-sum substitution:** no orbit sum, central sum, or physical raw-value sum is used.
  The finite line resolution is not advertised as a complete assembled query resolution.
- **Value versus broken formula:** the exact values pass, while uncorrected (5.4)/(5.6) fail as
  formulas for those values.
- **Gauge/sign laundering:** both constructions use an orthonormal tableau basis and a declared
  positive-leading line.  Every sign is independently positive; square claims remain gauge
  invariant.
- **Wrong group word:** identity, inverse, order-preserving, and endpoint-transposition words are
  checked at the label and matrix levels.
- **Rank-to-scalar collapse:** support dimensions `16/15/1` are recorded separately from the
  one-dimensional normalized fixed lines used for the scalar overlaps.
- **Finite-to-asymptotic leakage:** no uniform or asymptotic conclusion is licensed.

### 7(f): values versus formulas

The fresh proposer verification reruns the proposer's own formula implementation and proves only
that its archived JSON equals its current computation.  The independent checker constructs the
same transported object by a different exact basis model and establishes the transported scalar
values, signs, and resolutions independently.

Neither run verifies the printed claim that uncorrected planning (5.4)/(5.6) equal the transported
table.  Independent construction instead disproves that identification and supplies the corrected
operator formulas.  Thus the review establishes the **corrected transported theorem and its
values**, not the literal printed derivation.

### 7(g): quantifier hygiene

The licensed quantifier is exactly the finite first target `a=16,d=17,n=288,r=4`.  The words NO
rare/heavy and YES common/residual/heavy refer only to the fixed inventory in the controlling
classification.  “Every path” means every pair/triple in the explicit finite grids, not all stable
parameters.  No admissibility, taper, active range, or asymptotic qualifier is invoked.

## 9. Presentation and closeout

The proposer artifact has two broken TeX tokens: the missing backslashes before `qquad` in the two
interval-dimension lines.  The prose code token `emptyset` is not used as a TeX command; the table
it describes correctly uses `varnothing`.  A byte-level scan found no C0 control characters in
the proposer proof, proposer tool, or archived JSON.  These presentation defects do not change the
exact computation.

Canonical/shared DAG files changed by this reviewer: **none**.  The parent must record this review
on the existing node before commissioning downstream assembly, in accordance with Rule 8(c).

Final licensed statement: **the corrected, explicitly transported finite Pieri scalar table gets
MINOR / SCOPED PASS**.  The uncorrected claim that the main values literally realize planning
(5.4)/(5.6) does not pass.  The order-preserving representative is valid but not scalar-unique,
because the endpoint transposition yields the same vector.  Every assembly, commutator, norm,
numerator, lower bound, and exponent remains open.
