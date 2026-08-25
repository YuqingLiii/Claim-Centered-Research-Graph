# Fresh Rule-7 review: first finite NO one-side physical assembly

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the target mathematics or code  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

Reviewed target:
`ksum/artifacts/ksum_L3_critical_induced_packet_first_target_no_physical_assembly_a16_20260722.md`

## 1. Verdict and exact license

**Overall verdict: MINOR / SCOPED PASS.**

The following statement passes fresh independent exact review:

> At the single finite point
> `(s,a,d,r,q,t,tau)=(4,16,17,4,64,NO,(61,2))`, on the complete `1+3+6`
> all-parent multiplicity closure and for one fixed common raw mark, the reviewed occurrence,
> alphabet, and corrected transported Pieri tables assemble into the four left NO source effects
> `rare A,beta_T,beta_M,beta_B` on the `40`-dimensional active occurrence-multiplicity source and
> their lifts to the `160`-dimensional two-occurrence-multiplicity source.  The branch ranks are
> `4,16,10,16` actively and `16,64,40,64` after the untouched factor.  Every unordered pair of
> heavy beta effects has active commutator rank eight and full rank thirty-two.  The complete left
> unital algebra has dimension twenty-two and represented commutant dimensions `436` actively and
> `6976` after the passive factor.  The right mirror is identical.  All sixteen same-mark
> left/right branch products vanish in both orders, and the complete two-side algebra on dimension
> `160` is `Q^6 direct-sum M_3(Q)^4`, of dimension `42`, with commutant dimension `1152`.

The target explicitly prints the `beta_M,beta_B` commutator.  The reviewer's blind exact model
additionally verifies the `beta_T,beta_M` and `beta_T,beta_B` pairs; the heavy resolution makes
their commutators respectively equal to and the negative of the printed one.  This is an exact
reviewer-side strengthening within the identical finite scope, not a new asymptotic claim.

The `MINOR` qualification is nonmathematical.

1. In target Section 3, the displayed `p^2` line contains three plain `quad` tokens where
   `\quad` was intended.
2. The multiline reproduction commands use POSIX backslash continuation.  They are not directly
   executable in the repository's stated PowerShell shell; use one line or PowerShell backticks.

There is also one scope clarification: dimensions `40` and `160` are the complete
**occurrence-multiplicity** dimensions after the common Specht carrier factors are suppressed.
They are not literal dense Specht-carrier dimensions or literal marked-row codomain ranks.  The
target's Section 2 constructs exactly these multiplicity spaces, so this clarification changes no
calculation.

The broad canonical node remains **OPEN**.  This review licenses no YES object, no distinct-mark
relation, no other `s`, no uniform critical-family formula, no transfer feasibility, no query
bound or attenuation, no numerator, and no exponent.

## 2. Manifest-first provenance

The strengthened manifest was opened before the target artifact, tool, JSON, or log.  Every
manifest entry matched current disk bytes.

| target object | observed SHA-256 | manifest result |
|---|---|---|
| target artifact | `12991C331D593BA576B35A31791174AF64CCD5DBFF86E665396A148EFE3A3434` | exact |
| target tool | `B31EE99618772CC38DB8FDD705002C31370C52F63A490F70DF7A8F7A7699D770` | exact |
| archived target JSON | `428F8D33A60563A1F99787C98A78C5833CD2275A1C41975598284B553B17E009` | exact |
| archived target log | `4CA8972B9841A424FA3D376B861A618FBE441814187DA982A4A750BD7A42C5E9` | exact |
| strengthened manifest | `6E575D2F5AD665D7F5752D559D611E45E14C522B5AC3F76C81038E95DA232366` | recorded |

The manifest also pins the three reviewed JSON inputs and their three Rule-7 reviews.  All six
hashes match current bytes.

## 3. Rule-7(c) blind freeze and independent evidence

Before opening any target-named file or the canonical node's newest paragraphs, the reviewer
archived

`ksum/artifacts/ksum_L3_critical_induced_packet_finite_no_one_side_assembly_a16_rule7_blind_baseline_20260722.md`,

SHA-256
`CD300002E945E0A018F18BB000FDCE89BFE6F2DC91C13D5C7709AC12C27FB127`.

The baseline independently fixed:

- the `10 x 4` active and `10 x 4 x 4` full multiplicity spaces;
- the source Grams and form-to-endomorphism convention;
- the rare/heavy, eta, status, Pieri, and passive-factor weights;
- every branch rank and support relation;
- all three heavy-pair commutator ranks, kernels, and images;
- the complete left/right inventory, all sixteen cross-side products, and the left/full algebra
  decompositions;
- hostile failures for raw-form multiplication, no transport, old-parent pinching, absorbed
  normalizations, and a missing untouched factor;
- the complete scope exclusions.

The blind model was sealed before comparison:

| independent evidence | SHA-256 | result |
|---|---|---|
| `ksum/artifacts/logs_ksum_L3_finite_no_one_side_assembly_rule7_review_20260722/independent_model.py` | `D09C4D81F43C1AB74DF145E0FECC2ABCED7BB3B95806EC70D97FBF0F0A1BFC00` | does not import proposer assembly |
| `.../blind_model.json` | `1FB57BB03525AD4DB76C648DAD8A4B240B0B6041E10D1EE76F2C2A648BAC91BC` | `ALL_BLIND_EXACT_MODEL_GATES_PASS` |
| `.../blind_model.log` | `CA9AFC80ADD0ACF8CB3B1FDA4154B1244C1CAE16600DBCDFAC552148AD6E5992` | exact concise log |
| `.../independent_target_comparison.py` | `4A13A1745527CD19AB0C739B1A9099E6A7C6F2A41A616E5A954778166F9512A5` | manifest and frozen-model comparison |
| `.../independent_target_comparison.json` | `EF227D1FC93A992835EE25437183018064FAE6CE1D6FEEE07E865E89C1FDEA82` | `ALL_INDEPENDENT_TARGET_COMPARISON_GATES_PASS` |
| `.../independent_target_comparison.log` | `DE90AE93F48330331D50B6E1CDB6FC8571095F0F076F7563968A36FACB6A5479` | exact concise log |

Only after those independent gates passed was the proposer rerun.  Fresh proposer JSON and log
are byte-identical to the archived outputs, with hashes `428F8D...E009` and `4CA897...5E9`, and
`--verify-log` returns `ARCHIVED_NO_PHYSICAL_ASSEMBLY_RESULT_VERIFIED`.  This is a secondary
reproducibility result, not the independent proof.

## 4. Independent construction and normalization

### 4.1 Alphabet and occurrence coordinates

Let `P` be the ten-dimensional all-parent alphabet multiplicity space.  The one-mark reviewed
orthogonal gauge gives

\[
 I_P=P_A+P_B+P_{L,1}+P_{L,V}+P_{R,1}+P_{R,V}
\]

with ranks `1,1,3,1,3,1`.  All products between different projectors vanish.  This is a common
orthogonal change of gauge, not an old-parent pinch: each parent-gauge projector has nonzero blocks
across every pair of the parent blocks of sizes `1,3,6`.

The two occurrence spaces `Z_L,Z_R` each have dimension four.  In the rational source basis their
Gram is

\[
 G=\operatorname{diag}\left(
 {233245657600\over39},
 {37699701339916525\over14836},
 {252885664381001925\over1388384},
 {130423121542000\over93351}
 \right).
\]

For each `kappa in {T,M,B}` and `eta in {1,V15}`, the reviewed symmetric occurrence form is
`H_(kappa,eta)`.  Its endomorphism is

\[
 O_{\kappa,\eta}=G^{-1}H_{\kappa,\eta},
 \qquad O_{\kappa,\eta}^{\dagger_G}=O_{\kappa,\eta}.
\]

The independent model reconstructs all six `O` matrices from the actual archived forms and
matches the archived occurrence operators entrywise.  It does not use their printed ranks as
inputs.

### 4.2 Corrected transported position and coevaluation factors

The only legal NO heavy paths and transported squares are

\[
 p^2_{T,T}=1,quad p^2_{T,M}={2\over9275},quad
 p^2_{T,B}={4\over19099},quad
 p^2_{M,M}={9273\over9275},quad
 p^2_{B,B}={19095\over19099}.
\]

These are the values of the corrected operator identities containing `rho_lambda(g)`.  The
untransported planning equations do not produce them.  Rare has only `beta_T` and square one.

The independent assembly keeps separate

\[
 w_A={1\over18},qquad w_H={17\over18},qquad
 {d_1\over D}={1\over15},qquad {d_V\over D}={14\over15}.
\]

No status weight, coevaluation dimension, or Pieri square is absorbed into another table.

### 4.3 Assembly and source Gram

On

\[
 \mathcal S_L^{\rm act}=P\otimes Z_L,qquad \dim=40,qquad
 \Gamma_{40}=I_{10}\otimes G_L,
\]

put

\[
 X_{\beta,\eta}
 ={17\over18}{d_\eta\over15}
 \sum_{\kappa\leadsto\beta}p_{\beta,\kappa}^2O_{\kappa,\eta}.
\]

The left effects are

\[
 F_A={1\over18}P_A\otimes I_L,
\]

\[
 F_\beta=P_{L,1}\otimes X_{\beta,1}
          +P_{L,V}\otimes X_{\beta,V},
 \qquad \beta=T,M,B.
\]

The corresponding forms are `mathcal H_i=Gamma_40 F_i`; in particular the rare form is
`(1/18)P_A tensor G_L`.  On the full occurrence-multiplicity source

\[
 \mathcal S=P\otimes Z_L\otimes Z_R,qquad \dim=160,
\]

\[
 \Gamma_{160}=I_{10}\otimes G_L\otimes G_R,
\]

the left effect is `F_i tensor I_R`, while its form is `mathcal H_i tensor G_R`.  The right mirror
uses `P_B,P_R1,P_RV`, makes `Z_R` active, and has `I_L` at effect level or `G_L` at form level.

The beta resolution is

\[
 F_T+F_M+F_B
 ={17\over18}\left({1\over15}P_{L,1}+{14\over15}P_{L,V}\right)\otimes I_L.
\]

This is a fixed-mark, fixed-child sector identity.  It is not the full query sum over raw marks,
point children, or answers.

## 5. Rule-7(a) display-by-display type audit

| target display/object | exact domain, codomain, and audit | result |
|---|---|---|
| finite parameter tuple | `s=4,a=16,d=17,r=4,q=64,n=288,N=576,t=0,tau |-63`; no free asymptotic parameter | PASS |
| active source | `P tensor Z_L`, dimension `10*4=40`; multiplicity space with common carriers suppressed | PASS |
| full source | `P tensor Z_L tensor Z_R`, dimension `10*4*4=160`; complete two-occurrence multiplicity source, not a dense Specht carrier | PASS with stated clarification |
| alphabet `E` and `D_chi` | `E:R^10_parent -> R^10_Mackey` is orthogonal; each `D_chi in End(R^10)` has rank `1,1,3,1,3,1` | PASS entrywise |
| `G_occ` | positive diagonal form on each `Z congruent Q^4` | PASS |
| `H_(kappa,eta)` | symmetric bilinear form `Z x Z -> Q`; matrix `4 x 4` | PASS |
| `A=G^-1 H` | endomorphism `Z -> Z`, `4 x 4`, self-adjoint for `G`; raw `H` is not multiplied as an operator | PASS entrywise |
| `Gamma_40` | positive basis Gram on `P tensor Z_L`, `40 x 40` | PASS |
| `Gamma_160` | positive basis Gram on `P tensor Z_L tensor Z_R`, `160 x 160` | PASS |
| transported `rho_lambda(g)` | endomorphism of `S^lambda`, fixing the required `S_271` subgroup and aligning the old heavy coordinate before branching | PASS; no-transport excluded |
| `H_T,H_M,H_B` | bilinear forms on the active `40`-space; each eta term is `10x10 tensor 4x4` | PASS |
| rare `H,F` | `(1/18)D_A tensor G` is a form and `(1/18)D_A tensor I_4` is its effect | PASS |
| `F=Gamma^-1 H` | endomorphism `40 ->40`; every target branch conversion checked entrywise | PASS |
| eta commutators | `[O_M,eta,O_B,eta] in End(Z)`, `4 x 4`, rank two and kernel/image dimension two | PASS both eta sectors |
| active commutator | `[F_M,F_B] in End(P tensor Z_L)`, `40 x 40`; eta packet-copy ranks `3*2` and `1*2` | PASS rank `8` |
| active kernel/image | subspaces of the same `40`-space, dimensions `32` and `8`; target bases have the stated rational occurrence coordinates | PASS |
| metric adjoint | `C^dagger_Gamma=Gamma^-1 C^T Gamma=-C`, equivalently `Gamma C+C^T Gamma=0` | PASS exact |
| full commutator | active commutator tensored with `I_R`, an endomorphism `160 ->160` | PASS rank `32` |
| branch resolution | equality in `End(P tensor Z_L)`; it is not an identity on all of `P` | PASS |
| generated algebras | unital subalgebras of `End_Q(Q^40)` or `End_Q(Q^160)` with the displayed central supports | PASS exact word closure/block audit |

Literal marked rows have their own codomains and are not commuted here.  The reviewed objects are
positive source effects.  No conjugator is asserted to normalize an unrelated subgroup.

## 6. Exact ranks, kernels, images, and supports

### 6.1 Complete left inventory

| branch | eta contribution ranks on active `40` | active rank/kernel | full rank/kernel |
|---|---:|---:|---:|
| rare `A` | not applicable | `4 / 36` | `16 / 144` |
| heavy `beta_T` | `12 + 4` | `16 / 24` | `64 / 96` |
| heavy `beta_M` | `6 + 4` | `10 / 30` | `40 / 120` |
| heavy `beta_B` | `12 + 4` | `16 / 24` | `64 / 96` |

The eta-sector full ranks for `T,M,B` are `48+16`, `24+16`, and `48+16`.  Rare plus all heavy
branches has active rank twenty and full rank eighty.  The right mirror has exactly the same
table.

The rare support has active dimension four.  The heavy support

\[
 \mathcal S_H=(\operatorname{im}P_{L,1}\oplus\operatorname{im}P_{L,V})\otimes Z_L
\]

has dimension sixteen.  `F_T` and `F_B` are invertible on `mathcal S_H`, while `F_M` has rank ten
there.  Rare/heavy products vanish in both orders, as do products between the two eta
contributions.

### 6.2 All heavy-pair commutators

Let

\[
 K=[O_{M,1},O_{B,1}],qquad \operatorname{rank}K=2.
\]

The exact occurrence relation is

\[
 [O_{M,V},O_{B,V}]={1\over196}K,
\]

so the two eta commutators have the same kernel and image.  The target's two displayed kernel
vectors are scalar-normalized versions of the blind model's two vectors, and its image bases span
the exact blind images.

Because the heavy sum is scalar on each eta support,

\[
 [F_T,F_M]=[F_M,F_B],qquad
 [F_T,F_B]=-[F_M,F_B].
\]

Thus all three unordered pairs have:

| level | eta ranks | rank | kernel dimension | image dimension |
|---|---:|---:|---:|---:|
| active `40` | `6+2` | `8` | `32` | `8` |
| full `160` | `24+8` | `32` | `128` | `32` |

For any pair, actively,

\[
 \ker C=
 \left(\operatorname{im}(P_A+P_B+P_{R,1}+P_{R,V})\otimes Z_L\right)
 \oplus\left(\operatorname{im}P_{L,1}\otimes\ker K\right)
 \oplus\left(\operatorname{im}P_{L,V}\otimes\ker K\right),
\]

\[
 \operatorname{im}C=
 \left(\operatorname{im}P_{L,1}\otimes\operatorname{im}K\right)
 \oplus\left(\operatorname{im}P_{L,V}\otimes\operatorname{im}K\right).
\]

The full kernel and image tensor with `Z_R`.  For the commutator form `Gamma C`, the kernel and
rank are unchanged but the coordinate image is `Gamma im(C)`.

## 7. Algebra and commutant audit

For either eta, the exact `M,B` occurrence operators generate

\[
 M_1(\mathbb Q)\oplus M_3(\mathbb Q),
 \qquad \dim=10,
\]

and their commutant has dimension two.  The common invariant line is

\[
 \operatorname{span}\left(1,{1839664\over39414687},0,0\right).
\]

The differing eta aggregate eigenvalues `1/15` and `14/15` separate the two eta supports, rather
than linking them diagonally.

### 7.1 Active one-side algebras

For `M,B` plus the identity, the zero packet complement has multiplicity twenty-four.  The two
occurrence representations have multiplicities `3,3` and `1,1`.  Therefore

\[
 \mathcal A_{M,B}\cong\mathbb Q^3\oplus M_3(\mathbb Q)^2,
 \quad \dim=21,
\]

\[
 \dim\mathcal A_{M,B}'=24^2+3^2+3^2+1^2+1^2=596.
\]

Adding rare `A` and the complete heavy inventory separates an inactive twenty-dimensional block
from the four-dimensional rare block.  Hence

\[
 \mathcal A_L\cong\mathbb Q^4\oplus M_3(\mathbb Q)^2,
 \quad \boxed{\dim\mathcal A_L=22},
\]

with carrier blocks `20,4,3,9,1,3`, and

\[
 \mathcal A_L'\cong M_{20}\oplus M_4\oplus M_3\oplus M_3\oplus M_1\oplus M_1,
 \quad \boxed{\dim\mathcal A_L'=436}.
\]

### 7.2 Passive lift and complete two-side algebra

Tensoring the left effects by `I_R` does not change their abstract algebra dimension.  It
multiplies all representation multiplicities by four, giving full carrier blocks
`80,16,12,36,4,12` and

\[
 \dim\mathcal A_{L,160}'
 =80^2+16^2+12^2+12^2+4^2+4^2
 =\boxed{6976}.
\]

The right mirror is identical.  With both inventories present, all six alphabet sectors are
separate central supports.  The representation multiplicities are

\[
 16,16,12,12,4,4,12,12,4,4
\]

for simple sizes

\[
 1,1,1,3,1,3,1,3,1,3.
\]

Therefore

\[
 \boxed{\mathcal A_{L,R}\cong\mathbb Q^6\oplus M_3(\mathbb Q)^4},
 \qquad \boxed{\dim\mathcal A_{L,R}=42},
\]

\[
 \boxed{\dim\mathcal A_{L,R}'=1152}.
\]

These are exact rational-algebra statements and remain valid after complexification.  They were
not inferred from commutator ranks alone.

## 8. Complete right mirror and same-mark cross-side products

The right inventory is rare `B` and heavy `beta_T,beta_M,beta_B` on packet supports
`P_B,P_R1,P_RV`.  The left supports are `P_A,P_L1,P_LV`.  At one fixed common raw mark all six are
members of the same orthogonal alphabet resolution.  Hence every one of the sixteen products

\[
 F_i^L F_j^R=F_j^R F_i^L=0
\]

for `i,j in {rare,T,M,B}`.  All same-mark cross-side commutators vanish, and the left/right total
has rank `80+80=160`.

This exact product result is consistent with the separately reviewed direct-coset same-mark
theorem.  It cannot be transferred to two distinct raw marks, where the two point-stabilizer
resolutions are conjugate rather than common.

## 9. Rule-7(b): regime-complete identity gates

| regime within the claim | independent identity-level gate | result |
|---|---|---|
| parent multiplicities `1,3,6` | all ten columns retained; exact common `E`, every projector, and every cross-parent block | PASS |
| old-parent off-diagonal coupling | all three unordered parent-block pairs are nonzero in every alphabet table | PASS; no pinch |
| eta `1` | actual occurrence matrices, all three beta branches, rank-two core commutator, three packet copies | PASS |
| eta `V15` | actual occurrence matrices, all three beta branches, rank-two core commutator, one packet copy | PASS |
| rare/heavy | rare `A/B` and all `T,M,B` heavy branches | PASS |
| active/full | exact `40` effects/forms and passive-factor consequences on `160` | PASS |
| left/right | independent side support audit and mirror typing | PASS |
| all heavy commutator pairs | `TM,TB,MB`, not merely the printed `MB` value | PASS exact |
| same-mark cross-side inventory | all sixteen products, both orders | PASS exact |
| distinct marks | outside claim; no common-projector gate | UNTESTED / NOT LICENSED |
| YES | outside claim | UNTESTED / NOT LICENSED |
| any other `s` | outside claim | UNTESTED / NOT LICENSED |

Thus no qualitative finite branch in the stated claim is left behind a trace-only or numerical
gate.

## 10. Rule-7(d): no frozen-input immunity

The three reviewed inputs were reopened at the operator granularity used by this assembly.

1. Every occurrence endomorphism was reconstructed from the actual archived symmetric form and
   positive source Gram as `G^-1 H`; its `G`-adjoint identity and both eta resolutions were checked.
2. The actual radical alphabet matrix `E` was parsed exactly, its orthogonality was checked, and
   every archived parent-gauge table was independently regenerated as `E^T D E`.  The review did
   not accept the target's Boolean summaries or replace the codiagonal table by an old-parent
   diagonal one.
3. The Pieri JSON was checked against the corrected transported inventory and exact square
   resolutions.  The invalid literal no-transport equations were not granted immunity merely
   because the desired values appear in a reviewed table.

The planning interface was used only for the typed assembly formula.  Its uncorrected heavy
operator displays remain superseded by the reviewed formulas containing `rho_lambda(g)`.

## 11. Rule-7(e): standing and assembly-specific failure attacks

| attack | independent result |
|---|---|
| dropped/extra normalization | `w_A=1/18`, `w_H=17/18`, `d_eta/D=1/15,14/15`, and each transported `p^2` occur exactly once; both beta resolutions pass |
| type/dimension mismatch | every form, endomorphism, Gram, commutator, kernel, image, and passive lift is typed in Sections 5--6 |
| undefined terminology/stability | `first target`, `same mark`, `active`, `full`, `rare`, `heavy`, and carrier suppression are resolved here; no hidden stability or admissibility range is invoked |
| colored/fixed sector substituted for a full sum | the review calls this one mark and one child throughout; it does not call the beta resolution a full raw-value query resolution |
| values right while derivation broken | the exact values do not excuse omitted `rho_lambda(g)`, raw-form multiplication, or a missing passive Gram; each formula is separately audited |
| naive raw-form multiplication | the blind exact model gets wrong ranks `10,16,10` for raw-form `TM,TB,MB`, versus correctly typed effect rank `8` for all three |
| omitted transporter | the no-transport table kills middle/bottom fixed Pieri lines and fails their resolution; only the corrected transported table is assembled |
| absorbed `d_eta/D`, status, or Pieri factors | all three factor types remain separate; in particular `14/15` is not hidden in normalized `O_(kappa,V15)` |
| old-parent pinching | rejected by exact nonzero cross-parent blocks; common-gauge orthogonality does not make parent pinching physical |
| missing untouched factor | effect lift uses `I`, form lift uses `G`; ranks multiply by four and commutant multiplicities change accordingly |
| form/effect commutator confusion | typed form is `H_i Gamma^-1 H_j-H_j Gamma^-1 H_i=Gamma[F_i,F_j]`; raw `[H_i,H_j]` is a different matrix |
| numerics presented as proof | every positive conclusion uses rational/algebraic equality; numerical residuals would license none of the exact ranks or algebra types |

## 12. Rule-7(f): formula versus independent construction

The evidence layers are deliberately separate.

1. The blind checker is an independent assembly from the three reviewed upstream JSONs.  It
   reconstructs `G^-1H`, the common alphabet gauge, the transported `p^2` combinations, all
   branch effects, all three heavy commutators, and the algebra dimensions.  It imports no target
   tool and was sealed before the target was opened.
2. The target-comparison checker pins the strengthened manifest and compares the target JSON with
   the frozen blind output.  Target Boolean fields are not treated as independent proof.
3. The target tool rerun exercises the proposer's own implementation and is byte-identical to the
   archive.  It proves reproducibility only.
4. The printed derivation is audited analytically in Sections 4--8.  In particular, matching
   values would not repair an omitted transporter or an ill-typed raw-form product.

Thus both the corrected printed formulas and an independent construction of their finite object
have been checked.

## 13. Rule-7(g): quantifier hygiene and stopping point

The licensed quantifier is literal and finite:

- answer `NO` only;
- `s=4,a=16,d=17,r=4,q=64,n=288,N=576` only;
- point child `tau=(61,2)` only;
- complete parent multiplicities `1+3+6`;
- both eta sectors and both four-dimensional occurrence factors;
- all three NO heavy position children and the physical rare status;
- one fixed common raw mark;
- carrier-suppressed occurrence-multiplicity ranks, with passive occurrence restored as stated.

`Same mark` means the left and right projectors belong to one common `S_63` marked resolution.
`Active` means the queried occurrence factor is retained and the opposite occurrence factor is
suppressed.  `Full` in the licensed statement means both occurrence multiplicities are retained;
it does not mean a dense Specht carrier or literal row codomain.

Explicitly not licensed:

1. YES or a NO-to-YES transfer;
2. two distinct raw marks;
3. any other finite `s`, or a formula uniform for `s>=4`;
4. transfer, resolvent, or Sylvester feasibility;
5. query attenuation, coefficient norm, or query bound;
6. numerator or adversary lower bound;
7. exponent improvement;
8. completion of the broad occurrence-pencil classification node.

The canonical node had already recorded this proposer result with `pending fresh Rule-7 review`
before the commission.  It remains OPEN after this finite favorable review because its YES,
distinct-mark, uniform-family, and downstream obligations are not discharged.  No canonical or
shared DAG file was edited by this reviewer.
