# Fresh hostile Rule-7 review: first-target YES physical assembly and central-transfer decision

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the target mathematics or target tool  
Controlling node (read only; not edited):
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law`

Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_yes_physical_central_transfer_decision_a16_20260722.md`

## 1. Verdict

**Overall verdict: MINOR / STRICTLY SCOPED PASS.**

The mathematical decision in the proposer is correct.  Fresh pre-target reconstruction and
post-seal exact comparison independently license the following finite statement:

> At `(s,a,d,r,q)=(4,16,17,4,64)`, for one fixed raw mark and the single common
> `S_63` child `tau=(61,2)`, the complete sixteen-column YES multiplicity component assembles from
> the reviewed occurrence forms, unequal-cell alphabet tables, and corrected transported Pieri
> paths.  On the carrier-suppressed active one-side space `Q^16 tensor Q^4`, its branch ranks are
> `4,4,24,14,24` for common, residual, and `beta_T,beta_M,beta_B`; the one-side sum has rank `32`,
> and the full two-occurrence lifts have branch ranks `16,16,96,56,96` and sum rank `128` on
> dimension `256`.  Every heavy-pair commutator has rank `12` actively and `48` after the passive
> occurrence factor.  The two physical orientation images are distinct and neither unmatched
> complement can be dropped.

The proposer's central conclusion also passes:

> A **literal complete** fixed-mark seed determines its all-mark native transfer by an exact
> `S_64/S_63` correlated same-coset twirl.  The reviewed common child is not that literal seed:
> four private `S_63` children are absent.  Two positive same-central-marginal completions give
> unequal exact equality-transfer coefficients `1240/75579` and `40/61`.  Even the legitimate
> common-child filtered orbit still needs the actual correlated carrier/Wigner kernel before a
> full-Hilbert--Schmidt matrix, rank, kernel, or spectrum can be reported.

Accordingly, this review licenses a **partial filtered component and an insufficiency theorem**.
It does not license the literal native central transfer or any spectrum, resolvent, query,
numerator, lower-bound, or exponent statement.  The controlling node must remain **OPEN**.

### Why the verdict is MINOR rather than unqualified PASS

The qualifications are provenance/presentation issues, not false finite mathematics.

1. The proposer output records the complete `5 by 5` fixed-mark cross-side support conclusion as
   prose; its code loop does not actually materialize or multiply the `256 by 256` effects.  The
   support proof from the eight disjoint coordinate projectors is exact, and the independent
   checker covers all 25 products, so no value changes.
2. Target Section 10 prints the raw-form/effect guard as ranks `10` versus `8` without saying in
   that table row that these are the separately reviewed **NO** assembly ranks.  The current YES
   heavy-pair effect rank is `12`; the code comments identify the NO provenance correctly.
3. The proposer complement table is aggregate by `(orientation, queried side)`.  The independent
   checker constructs every individual common, residual, and heavy branch block in both
   orientations.  That strengthening confirms the advertised aggregate complement survival and
   leakage.

These are local and do not weaken the scoped result.

## 2. Anchoring and immutable provenance

Both repository protocols were read in full.  Before the target artifact, tool, JSON, log,
checksum package, or newly updated node was opened or grepped, the reviewer used only the older
reviewed occurrence, NO/YES alphabet, corrected transported Pieri, NO assembly, typing, and
direct-coset inputs to archive

`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_yes_physical_central_transfer_rule7_blind_baseline_20260722.md`,

SHA-256
`7D6210B003110C9CC802B9DE3F9F405D3CDA260993833BCF8EC20DDD6CFFC5A4`.

The baseline fixed the spaces, all five branch ranks, all ten within-side commutator ranks, both
orientation decompositions, the full `S_63` child inventory, the correlated-twirl type, an exact
two-completion nonuniqueness guard, and the withheld scope.  It did not assume a favorable target
verdict.

Only after that seal was written did the reviewer open the proposer checksum package.  Its own
SHA-256 is
`870EDC21F7B0AB870CEE48F0CE76D96F9B0AE11DC539147D13622E50FA620ECD`,
and all sixteen entries match current disk bytes:

| proposer object | manifest SHA-256 | result |
|---|---|---|
| target artifact | `07277D64CD33D385CF4DC05F843BD2A4FF0F3D9B705623C0B09E34807F2D752B` | exact |
| target tool | `0179A097C3C99A4190D1466919625903C49831C7C182FD46172C03685A583725` | exact |
| archived JSON | `C6EF5ED201E1570AF86D8F7867CF27D1EBA48B117688F6B4052681931E143D0F` | exact |
| archived log | `8B1A6C295A58DC557C4438C54E896C98214873C7A78BCE451E8CF2A7D076F5B1` | exact |

The independent pre-target checker is

`ksum/tools/ksum_l3_first_target_yes_physical_central_rule7_independent.py`,
SHA-256
`337B1D04AD31E7B4220CD71C7CA2360D5A4ECF37E87A64B2C59F8496AFF03470`.

It imports no proposer target code.  Its output and log are

- `ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_rule7_review_20260722/independent.json`,
  SHA-256 `80B21C9598308DEBE0AE87F8B1C742958876952D42FF419C441CF852A893214E`;
- `ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_rule7_review_20260722/independent.log`,
  SHA-256 `3AFCC6A96521E67634F66BBEFA761BC04412C28767CB16F4E802B5A0BBDD41C6`.

It reports `ALL_INDEPENDENT_YES_CENTRAL_RULE7_GATES_PASS`.

The post-seal comparison checker, which pins the blind evidence and does not import the target
tool, is

`ksum/artifacts/logs_ksum_L3_first_target_yes_physical_central_rule7_review_20260722/independent_target_comparison.py`,
SHA-256
`EA2BE05504314895DFCC3494A9202A9712AA5140E74F0DCAB717AEB85140F003`.

Its JSON and log have SHA-256 values
`844AFA2B71AF5AD5BFD77C56E64F2FA7947CBC28BCF99393BD4DF6884118C2B3`
and
`A8405F60F484900A6BC52670D4AA3F77FFB6950F35876FD1D2DD332B51B8A50E`,
and report `ALL_INDEPENDENT_TARGET_COMPARISON_GATES_PASS`.

Only after all independent gates passed was the proposer rerun.  The fresh JSON and log are
byte-identical to the archive, with the same two hashes above; the proposer's built-in verifier
prints `ARCHIVED_YES_PHYSICAL_CENTRAL_DECISION_VERIFIED`.  This establishes reproducibility only.

## 3. Independent exact reconstruction

### 3.1 Forms, effects, and weights

Let `Z=Q^4` carry the reviewed positive diagonal source Gram `G`.  For every
`kappa in {T,M,B}` and `eta in {1,V15}`, the archived matrix `H_(kappa,eta)` is a symmetric form,
and the endomorphism used in the assembly is

\[
O_{\kappa,\eta}=G^{-1}H_{\kappa,\eta}.
\]

The independent checker reconstructs all six effects from the raw forms, matches the archived
effects entry by entry, verifies `O^T G=GO`, and verifies both eta resolutions
`O_T+O_M+O_B=I_4`.  On the YES active space,

\[
\Gamma_{64}=I_{16}\otimes G,
\qquad \mathcal H_i=\Gamma_{64}F_i,
\qquad F_i=\Gamma_{64}^{-1}\mathcal H_i.
\]

Every assembled form is exactly symmetric.  The typed form commutator is

\[
\mathcal H_i\Gamma_{64}^{-1}\mathcal H_j
-\mathcal H_j\Gamma_{64}^{-1}\mathcal H_i
=\Gamma_{64}[F_i,F_j],
\]

not the raw product `[H_i,H_j]`.

The exact weights appear once each:

\[
w_C={1\over288},\qquad w_{\rm residual}={15\over288}={5\over96},
\qquad w_H={17\over18},
\qquad {d_1\over15}={1\over15},\quad {d_V\over15}={14\over15}.
\]

The YES alphabet normalization is the unequal-cell factor

\[
\sqrt{\frac{n_dd_d}{n_cd_c}}.
\]

The independent checker redoes the failure guard: the old equal-cell substitution has exact skew
rank eight, with first skew entry `(0,2)=14`.

### 3.2 Corrected transported paths and complete fixed-mark effects

Summing every legal intermediate `xi` gives

\[
\begin{array}{c|ccc}
 &T&M&B\\ \hline
\beta_T&1&2/9275&4/19099\\
\beta_M&0&9273/9275&0\\
\beta_B&0&0&19095/19099.
\end{array}
\]

The `2/9275` and `4/19099` entries are respectively the sums of two separately retained legal
paths.  The literal no-transport table is not used.

In the marked-Mackey gauge the left effects are

\[
F_C^L={1\over288}P_C\otimes I_4,
\qquad
F_R^L={5\over96}P_L\otimes I_4,
\]

\[
F_\beta^L={17\over18}\sum_{\eta}
{d_\eta\over15}P_{HL,\eta}\otimes
\sum_\kappa p^2_{\beta,\kappa}O_{\kappa,\eta}.
\]

The right family is the exact mirror on `P_C,P_R,P_HR,eta` and `Z_R`.  All sixteen alphabet
columns and all three parent blocks `1|5|10` are retained.  The five independent effect digests
are exactly the five proposer digests.

The exact rank table is:

| branch | eta active ranks | active rank/kernel | full rank/kernel |
|---|---:|---:|---:|
| common | n/a | `4 / 60` | `16 / 240` |
| residual | n/a | `4 / 60` | `16 / 240` |
| `beta_T` | `20+4` | `24 / 40` | `96 / 160` |
| `beta_M` | `10+4` | `14 / 50` | `56 / 200` |
| `beta_B` | `20+4` | `24 / 40` | `96 / 160` |

The heavy sum has active rank `24`, and the complete queried-side sum has active/full ranks
`32/128`.  Of the ten unordered within-side pairs, exactly the three heavy pairs are nonzero.
With

\[
K=[O_{M,1},O_{B,1}],\quad \operatorname{rank}K=2,
\quad [O_{M,V},O_{B,V}]={1\over196}K,
\]

each heavy-pair commutator is six alphabet copies of `K`, with signs `+,-,+` for `TM,TB,MB` and
common scalar

\[
{1137169627\over286972024500}.
\]

Thus their active/full ranks are `12/48`.

At the same fixed mark all 25 left/right branch pairs commute.  Exactly one product is nonzero:

\[
F_C^LF_C^R={1\over288^2}P_C\otimes I_4\otimes I_4,
\]

of rank `16`.  The two full queried-side sums each have rank `128`, their product has rank `16`,
and their commutator is zero.

### 3.3 Both orientation images and every unmatched block

For `o=L,R`, the checker independently constructs

\[
j_o:\mathbb Q^{10}\to\mathbb Q^{16},\qquad
u_o:\mathbb Q^6\to\mathbb Q^{16}
\]

with `j_o^Tj_o=I`, `u_o^Tu_o=I`, `j_o^Tu_o=0`, and
`j_oj_o^T+u_ou_o^T=I_16`.  The complements split by parent as `0+2+4`, and
`rank(j_Lj_L^T-j_Rj_R^T)=6`.

For each individual branch, the active ranks of image compression, leakage, and complement action
are:

| branch | `j^*Fj` | `u^*Fj` | `u^*Fu` |
|---|---:|---:|---:|
| common | 4 | 4 | 4 |
| residual | 4 | 4 | 4 |
| `beta_T` | 16 | 0 | 8 |
| `beta_M` | 10 | 0 | 4 |
| `beta_B` | 16 | 0 | 8 |

These ranks are the same for both orientation bases at the individual-branch level.  For the full
queried-side sum they are `20/4/12` when orientation and queried side agree and `24/8/16` when they
are crossed.  Full-space ranks multiply by four.  Both leakage directions are exact metric
adjoints.  The complement has genuine heavy action and singleton/residual leakage; it is not a
zero-padding sector.

## 4. Covariance, child completeness, and the transfer boundary

Let `K=S_63` fix `z0`.  A literal fixed-mark effect `A_t=F_(t,z0)^s` is `K`-invariant.  For
`g_zK in S_64/K`, covariance gives

\[
F_{t,z}^s=\rho_t(g_z)A_t\rho_t(g_z)^*.
\]

The all-mark native transfer on `Hom(E_0,E_1)` has vectorized kernel

\[
\sum_{gK}(F_{0,gz0}^s)^T\otimes F_{1,gz0}^s
=\sum_{gK}W(g)(A_0^T\otimes A_1)W(g)^*,
\quad W(g)=\overline{\rho_0(g)}\otimes\rho_1(g).
\]

The same coset occurs on source and target.  It is not `64` times one representative and not the
product of two independent coset sums.  Representative independence follows from `K` invariance.
Both the proposer and independent checkers give exact small-group counterguards to the two wrong
substitutions; the physical formula itself is verified analytically here.

The complete multiplicity-free `S_64 -> S_63` inventory is:

| parent | parent dimension | children and dimensions |
|---|---:|---|
| `(62,2)` | `1952` | `(61,2):1890`, `(62,1):62` |
| `(61,3)` | `39648` | `(61,2):1890`, `(60,3):37758` |
| `(61,2,1)` | `79360` | `(61,2):1890`, `(60,2,1):75579`, `(61,1,1):1891` |

Consequently common `tau=(61,2)` is a proper child in all three parents.  Its reduced fixed-mark
tables are one positive block of the literal effect, not the literal `F`.  On an arbitrary
rectangular matrix, the full transfer also includes every target/source child pair; a
`(tau,tau)` filtered contribution is only one component.

The proposer's stronger two-completion guard is exact.  Inside parent `(61,2,1)`, place the same
missing central marginal on either private child `chi`.  The required seed scale is

\[
a_\chi={f^{(61,2,1)}\over64f^\chi},
\]

so the single-effect central sum is one in both completions, while the equality-transfer
coefficient on a common scalar multiplicity line is `a_chi`.  This gives

\[
a_{(60,2,1)}={1240\over75579},
\qquad
a_{(61,1,1)}={40\over61}.
\]

They are unequal, while the reviewed common-child block is unchanged.  This proves genuine
nonuniqueness; it does not claim either artificial completion is the physical k-Sum row.

For the common-child orbit itself, the transported cross-parent carrier map is

\[
\rho_{\nu'}(g_z)\iota_{\nu',\tau}\iota_{\nu,\tau}^*\rho_\nu(g_z)^*:
S^\nu\to S^{\nu'}.
\]

The reduced `40 by 40` and `64 by 64` effects contain none of these matrices.  Their correlated
four-parent vectorized sum is the missing carrier/Wigner kernel.  Separate Schur traces
`64 f^tau/f^nu` determine only central marginals, not this full kernel.  Therefore a full-HS rank,
kernel, or spectrum genuinely cannot be inferred from the reviewed multiplicity tables.

## 5. Rule-7(a): display-by-display type audit

| target object/display | domain and codomain | exact dimension audit and verdict |
|---|---|---|
| `Y_(0,tau),Y_(1,tau)` | alphabet multiplicity spaces | `Q^10=Q^(1+3+6)`, `Q^16=Q^(1+5+10)`; PASS |
| `Z_L,Z_R,G` | each occurrence space `Q^4`; `G:Z->Z^*` | positive diagonal `4 by 4`; PASS |
| `H_(kappa,eta)` | bilinear form `Z x Z -> Q` | symmetric `4 by 4`; PASS |
| `O=G^-1H` | `Z->Z` | `4 by 4`, `G`-self-adjoint; PASS |
| each `D_chi` | `Y_(1,tau)->Y_(1,tau)` | `16 by 16`, ranks `1,1,1,1,5,1,5,1`; PASS |
| active `F_i` | `Y_(1,tau) tensor Z_s ->` itself | `64 by 64`; all 16 alphabet columns retained; PASS |
| `Gamma_64` | active source Gram | `64 by 64=I_16 tensor G`; PASS |
| full left/right effect | `Y_(1,tau) tensor Z_L tensor Z_R ->` itself | `256 by 256`; effect lift uses `I`, form lift uses passive `G`; PASS |
| full fixed-mark cross-side product | endomorphism of the same `256`-space | common/common rank 16; other 24 zero; PASS |
| `j_o,u_o` | `Q^10->Q^16`, `Q^6->Q^16` | exact orthogonal `16x10` and `16x6`; PASS |
| orientation effect blocks | image/complement endomorphisms or rectangular leakage maps | active image `40`, complement `24`; induced Grams `I_10 tensor G`, `I_6 tensor G`; PASS |
| literal `A_t,F_(t,z)` | endomorphisms of the complete physical selected source `E_t` | NO and YES ranks unequal; `rho_t(g)` acts within its own `E_t`; PASS conditionally on the missing complete seed |
| native transfer | `Hom(E_0,E_1)->Hom(E_0,E_1)` | rectangular HS dimension `dim(E_1)dim(E_0)`; no PSD order is asserted on rectangular matrices themselves; PASS |
| vectorized kernel | endomorphism of `bar(E_0) tensor E_1` | each summand `(F_0)^T tensor F_1` has the same square type; PASS |
| branching `iota_(nu,tau)` | `S^tau->S^nu` | carrier sizes are the hook dimensions in Section 4; PASS |
| cross-parent carrier block | `S^nu->S^(nu')` | composition `rho_(nu') iota_(nu') iota_nu^* rho_nu^*` is well defined; PASS |
| correlated Wigner kernel | vectorized four-parent carrier block | target/source parent indices retained; absent computationally and therefore no rank claimed; PASS boundary |
| completion seed `a_chi P_chi` | endomorphism of `S^(61,2,1)` | `P_chi` has rank `f^chi`; both scales are positive contractions; PASS |

The `40960=256*160` number in the target is explicitly carrier-suppressed.  The actual unmarked
source is a direct sum of `S_64` parent carriers whose `S_63` child embeddings carry the reduced
blocks; `S^tau` is embedded inside those parent carriers, not an additional independently tensorable
copy.  The target uses the number only as a warning and makes no dense-dimension claim from it.

## 6. Rule-7(b): regime-complete identity gates

| qualitative regime in the finite claim | identity-level evidence | result |
|---|---|---|
| occurrence multiplicity `C_r=4` | all four columns of all six `G^-1H` effects | PASS exact |
| YES parent multiplicities `1,5,10` | full `16 by 16` gauge and every parent block | PASS exact |
| eta `1,V15` | separate contributions, ranks, resolution, and commutator relation | PASS exact |
| common/residual/heavy | all five queried branches on left and right | PASS exact |
| all legal transported paths | all seven YES triples, including both two-path top sums | PASS exact |
| all within-side pairs | all ten commutators | PASS exact |
| fixed-mark cross-side pairs | all 25 support products and both orders | PASS exact |
| active/full | exact `64` effects and passive-factor consequences on `256` | PASS exact |
| orientation `L,R` | both images, both complete six-column complements | PASS exact |
| individual complement action/leakage | every branch, both orientations, both queried sides | PASS in independent checker |
| all `S_63` children | all seven branching edges and five distinct shapes | PASS exact |
| common child versus literal seed | two same-central-marginal completions | PASS exact nonuniqueness |
| same-coset versus representative/independent twirls | analytic formula plus exact synthetic guards | PASS |
| full physical Wigner kernel | deliberately absent; no rank/spectrum claim | UNTESTED / WITHHELD |
| private-child physical effects | absent and named | UNTESTED / WITHHELD |
| other `s` or asymptotic family | outside claim | UNTESTED / WITHHELD |

No untested regime is used to upgrade the finite component to a full transfer conclusion.

## 7. Rule-7(c)--(g)

### 7(c): anchoring ban

**PASS.**  Section 2 records the pre-target baseline, its hash, and independent output.  The five
effect digests later matched the proposer exactly, but they were derived before the proposer was
opened.  Coincident notation is limited to project-standard shapes, branch labels, and canonical
form/effect conventions.

### 7(d): no frozen-input immunity

**PASS.**  The review reopened every predecessor at the granularity newly used:

1. all occurrence effects were regenerated from raw forms as `G^-1H`;
2. both NO and YES parent gauges were checked as exact orthogonal changes of basis;
3. all eight YES projectors and the unequal-cell failure guard were reconstructed;
4. all legal transported Pieri paths were resummed, not read from branch totals;
5. both orientation maps and their complete complements were independently rebuilt;
6. the NO assembly was used only as an unequal source and reconstruction check;
7. the direct-coset/typing reviews supplied only the native space and covariance boundary, while
   the same-coset formula and nonuniqueness were rederived.

No earlier common-child review is used to immunize the missing private children or carrier kernel.

### 7(e): failure-mode diversity

| hostile attack | result |
|---|---|
| dropped/extra normalization | status, eta, unequal-cell, and transported `p^2` factors each occur once; both resolutions pass |
| form/effect mismatch | every product uses `G^-1H`; raw-form multiplication is separately identified as wrong |
| type/dimension mismatch | Section 5 types every displayed map, including unequal answers and cross-parent carriers |
| undefined term/range | `common tau`, `fixed mark`, `filtered`, `literal`, `full`, `central`, `native`, and `Wigner kernel` are resolved here and in the target; the quantifier is one finite point |
| colored representative substituted for a full sum | rejected: the same-coset sum has 64 transported terms and differs exactly from `64` times one seed |
| independent target/source twirls | rejected analytically and by exact counterguard |
| values right while formula broken | component values, printed formulas, and carrier/twirl inference are audited in separate evidence layers |
| omitted YES complement | all six columns and their branchwise action/leakage are explicit |
| parent pinch | the full `1|5|10` codiagonal common-child gauge is retained |
| common child called literal `F` | refuted by the complete five-shape child inventory |
| pullback or zero padding | excluded; native target dimension 256 and source dimension 160 remain unequal |
| same-mark sold as distinct-mark enumeration | excluded; covariance is formula-level, and no explicit distinct-mark value table is claimed |
| Schur trace sold as a Wigner kernel | excluded; scalar `64 f^tau/f^nu` does not determine the four-parent correlated kernel |
| finite component sold as a spectrum/resolvent | explicitly withheld |

### 7(f): value versus formula

The proposer rerun exercises the proposer's own assembly and proves only reproducibility.  The
blind checker independently reconstructs the exact forms, effects, gauges, paths, ranks,
commutators, orientation blocks, and branching inventory without importing the proposer.  Its five
effect digests agree entry by entry with the target.

Separately, the review proves the covariance type, correlated same-coset order, Schur-average
coefficients, and two-completion guard analytically.  The target's `S_3` gate is an inference guard;
it does not evaluate the physical `S_64` carrier kernel, and neither the proposer nor this review
claims that it does.  Thus values and printed formulas are not conflated.

### 7(g): quantifier hygiene

**PASS with the strict scope below.**

- **Complete YES assembly** means every branch and all sixteen multiplicity columns inside the
  single fixed-mark `tau=(61,2)` component.  It does not mean every point child or literal `F`.
- **Full `256`** means both four-dimensional occurrence multiplicities are retained after common
  carriers are suppressed.  It does not mean a dense Specht carrier.
- **Common mark** means one `S_63` stabilizer.  It does not enumerate effects for two distinct raw
  marks.
- **Correlated central orbit** means the same coset representative transports source and target.
- **Native transfer** acts on `Hom(E_0,E_1)` and uses the entire YES target.  It is not an
  orientation pullback.
- **Wigner kernel required** means required for the full-HS matrix/rank/spectrum; a smaller
  separately proved equivariant restriction could require less data, but it is not this reviewed
  claim.

## 8. Exact licensed and withheld scope

### Licensed

1. The finite common-`tau` YES fixed-mark source effects, their forms, all branch/sum ranks, all
   within-side commutator ranks, and fixed-mark cross-side products.
2. Both orientation images and the entire unmatched complement, including every individual
   branch's action and leakage ranks.
3. The exact `S_64/S_63` covariance formula and correlated same-coset transfer type.
4. The complete child inventory and the conclusion that common `tau` is not literal `F`.
5. The exact same-central-marginal completion coefficients `1240/75579` and `40/61` and the
   resulting insufficiency theorem.
6. The necessity of omitted private-child effects and the carrier/Wigner kernel before any
   full-HS transfer rank or spectrum.

### Explicitly withheld

1. Every private-child physical fixed-mark table and the literal complete fixed-mark effect.
2. The literal native transfer matrix, rank, kernel, spectrum, or numerator-active block.
3. Any orientation pullback or zero-padded substitute.
4. Any explicit distinct-mark product enumeration.
5. Any resolvent, Sylvester, taper, regularization, coefficient-norm, query-attenuation, incidence,
   remainder, numerator, adversary lower-bound, or exponent conclusion.
6. Any uniform-in-`s` or asymptotic inference.

The proposer result therefore receives **MINOR / STRICTLY SCOPED PASS**.  This review is not a
completion review of the controlling resolvent node and licenses no status change.  No canonical
or shared DAG file was edited by this reviewer.
