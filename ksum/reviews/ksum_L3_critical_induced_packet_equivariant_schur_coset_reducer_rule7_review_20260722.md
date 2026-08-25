# Fresh hostile Rule-7 review: finite equivariant Schur--coset reducer

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the proposer proof or proposer checker  
Controlling node, read only and not edited:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law`

Reviewed proposer artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_equivariant_schur_coset_reducer_proof_20260722.md`

## 1. Verdict

**Overall verdict: PASS / STRICTLY SCOPED.**

The proposer formula is correct.  An independent pre-target derivation and exact rational
`S_3/S_2` construction establish the following finite statement for either `s=L` or `s=R`.
With

\[
G=S_{64},\quad K=S_{63},\quad |G/K|=64,\quad
\tau=(61,2),
\]

and parent set

\[
P=\{(62,2),(61,3),(61,2,1)\},
\]

let the common-child fixed-mark coefficient blocks be

\[
A^{t,s}_{\mu\nu}:M_{t,\nu}\longrightarrow M_{t,\mu}.
\]

On the carrier-suppressed `G`-equivariant rectangular coefficient subspace,

\[
B=\bigoplus_{\nu\in P}I_{S^\nu}\otimes B_\nu,
\qquad B_\nu:M_{0,\nu}\to M_{1,\nu},
\]

the correlated common-child coset transfer is exactly

\[
\boxed{
(\mathcal E_{s,\tau}B)_\mu
=\frac{64f^\tau}{f^\mu}
 \sum_{\nu\in P}A^{1,s}_{\mu\nu}B_\nu A^{0,s}_{\nu\mu}.}
\tag{R1.1}
\]

The output-parent coefficients in the stated parent order are

\[
\boxed{{3780\over61},\quad {180\over59},\quad {189\over124}},
\tag{R1.2}
\]

and the reviewed carrier-suppressed coefficient-space dimension is

\[
\boxed{19456=1216\cdot16}.
\tag{R1.3}
\]

The right/source effect acts first.  Schur parent pinching is applied only after forming
`A^1 B A^0`; the intermediate-parent sum is compulsory.  The NO and YES cosets are correlated,
not independently averaged.

This pass banks a **common-child plus `G`-equivariant-subspace formula only**.  It is not a
private-child completion, literal native transfer, full-Hilbert--Schmidt carrier kernel, physical
matrix spectrum, resolvent, numerator, lower bound, or exponent.  The controlling node therefore
remains **OPEN**.

One scope lock must remain attached to every use of `19456`: it is the dimension after the fixed
position Specht carriers have already been suppressed, as the proposer repeatedly states.  It is
not the dimension of `Hom_(S_64)` on an unsuppressed physical source containing those spectator
carriers.  This is a boundary, not a defect in the stated carrier-suppressed claim.

## 2. Anchoring record and manifest-first gate

Both repository protocols were read in full.  Before the rectangular-transfer scope audit, target
proof, target checksum ledger, target checker/output, or canonical reducer values were opened or
grepped, the reviewer used only the already-reviewed direct-coset and YES
common-child/central-insufficiency reviews to seal

`ksum/artifacts/ksum_L3_critical_induced_packet_equivariant_schur_coset_reducer_rule7_blind_baseline_20260722.md`,

SHA-256
`49102CA17F6695397C4282ABF8D0560CE2D2CBB7B60A3434EF1B0100CB4788DF`.

The baseline independently fixed:

- the correlated coset identity and multiplication order;
- Schur pinching after, not before, the reference sandwich;
- all nine NO/YES rectangular Hom types;
- all four hook dimensions and three output-parent coefficients;
- the `1216` active, `16` passive, and `19456` total coefficient dimensions;
- separate `L` and `R` untouched-factor formulas;
- exact hostile gates and the withheld scope.

The pre-target checker is

`ksum/tools/ksum_l3_equivariant_schur_coset_reducer_rule7_independent.py`, SHA-256
`CAD98648741DDE0EB271D38866ABBDD139F198CD67CAEDBF2BC010B1791DFF9E`.

Its output and log are

- `ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_rule7_review_20260722/independent.json`,
  SHA-256 `B6E4FC490434E89D0A865E654B5C507F1088913087A7FEA76B84A6E426E78091`;
- `ksum/artifacts/logs_ksum_L3_equivariant_schur_coset_reducer_rule7_review_20260722/independent.log`,
  SHA-256 `05AE21B8AABB89843D8CBA47053F2794FF0B96DCB42F47DB82869CB1BFEB1820`.

It reports `ALL_EQUIVARIANT_SCHUR_COSET_RULE7_GATES_PASS`.  Those four objects were pinned in the
pre-target manifest, SHA-256
`6726D2EBC4C572B0E17B1D1DD96F2BDE30CD7CC9647EFA4828E79F6702214734`.

Only after this seal was written was the proposer checksum ledger opened.  Its SHA-256 is
`A31FF706FE5E0F44AF881DDA12A2073345A522B949D2E71A3256A35C5A215D5F`, and all four entries match
the current bytes:

| proposer object | manifest SHA-256 | observed result |
|---|---|---|
| proof | `C385DDC597A534D478A7024FFD4053A16E61C0E3425095C35A4268B1F3FA9105` | exact |
| checker | `418FDE6FCEB6DC0D80A23C449861F256BD8EE44BF9CE9317548DD47350D892F5` | exact |
| JSON | `DBC19C6E51AE40B2FDCE2BFFD75E31F794F1CA34B33C5569F53F65269AE813F9` | exact |
| log | `C5D4BF94D7FCEA1AED70F944D04F9CCD9B0694DCF88C643AF3A2071053FC6F59` | exact |

The proposer checker was rerun only after inspection.  It again printed
`ALL_EQUIVARIANT_SCHUR_COSET_REDUCER_GATES_PASS`, and both generated files remained byte-identical
to the archive.

The post-seal comparison script imports neither checker.  It pins both manifests and reports
`ALL_EQUIVARIANT_SCHUR_COSET_TARGET_COMPARISON_GATES_PASS`; all six legitimately comparable
formula/type fields agree exactly.

## 3. Independent first-principles derivation

Write the carrier-suppressed three-parent sources as

\[
E_t^P=\bigoplus_{\nu\in P}V_\nu\otimes M_{t,\nu},
\qquad V_\nu=S^\nu.
\tag{R3.1}
\]

Choose an isometric multiplicity-free branching map
`J_nu:V_tau->V_nu`.  A `K`-intertwining fixed-mark seed supported on the common child has blocks

\[
Q_t^s[\alpha,\beta]
=(J_\alpha J_\beta^*)\otimes A^{t,s}_{\alpha\beta}.
\tag{R3.2}
\]

For `B in Hom_G(E_0^P,E_1^P)`, Schur's lemma gives
`B=direct-sum_nu I_(V_nu) tensor B_nu`.  The reference sandwich has outer block

\[
(Q_1^sBQ_0^s)[\mu,\alpha]
=J_\mu J_\alpha^*\otimes
 \sum_\nu A^{1,s}_{\mu\nu}B_\nu A^{0,s}_{\nu\alpha}.
\tag{R3.3}
\]

This proves the source-side order before any averaging.  Every term has type

\[
M_{0,\alpha}\xrightarrow{A^{0,s}_{\nu\alpha}}M_{0,\nu}
\xrightarrow{B_\nu}M_{1,\nu}
\xrightarrow{A^{1,s}_{\mu\nu}}M_{1,\mu}.
\tag{R3.4}
\]

For a `K`-intertwiner `C:E_0^P->E_1^P`, the unnormalized coset sum is

\[
\sum_{gK}\rho_1(g)C\rho_0(g)^*
=\frac1{|K|}\sum_{g\in G}\rho_1(g)C\rho_0(g)^*.
\tag{R3.5}
\]

Therefore its outer `mu,alpha` block is zero for `mu!=alpha`.  On the diagonal,

\[
\sum_{gK}\rho_\mu(g)J_\mu J_\mu^*\rho_\mu(g)^*
=\frac{|G/K|f^\tau}{f^\mu}I_{V_\mu},
\tag{R3.6}
\]

because the left side is scalar by Schur and has trace `|G/K| f^tau`.  Applying (R3.6) to
(R3.3) gives (R1.1).  This derivation uses no target notation or target code.

With column-stacking vectorization, the reducer block from input parent `nu` to output parent
`mu` is

\[
[\mathsf R_s]_{\mu\leftarrow\nu}
=\frac{64f^\tau}{f^\mu}
 \bigl(A^{0,s}_{\nu\mu}\bigr)^{\mathsf T}\otimes
 A^{1,s}_{\mu\nu}.
\tag{R3.7}
\]

The transpose here is the vectorization transpose.  It does not reverse the physical right
multiplication or silently replace the source block by its opposite block.

## 4. Rule-7(a): display-by-display type audit

In parent order `(62,2),(61,3),(61,2,1)`, put

\[
f=(1952,39648,79360),\quad
m_0=(16,48,96),\quad m_1=(16,80,160).
\]

Within the stated carrier-suppressed model,

\[
\dim E_0^P=9,552,896,qquad
\dim E_1^P=15,900,672.
\]

| proposer display | independent domain/codomain and dimension audit | result |
|---|---|---|
| (0.1) | Input/output is `direct-sum_mu Hom(M0_mu,M1_mu)`, dimension `19456`.  For each output `mu`, every summand maps `M0_mu->M1_mu`; the scalar depends on the output parent. | PASS |
| (0.2) | Three dimensionless rational scalars in the same order as the three output parents. | PASS |
| (0.3) | `256+3840+15360=19456`; this is the coefficient space, not full `Hom(E0,E1)`. | PASS |
| (1.1) | `E_t^P` is the orthogonal direct sum of `V_nu tensor M_t,nu`; dimensions above. | PASS in the explicitly carrier-suppressed model |
| (1.2) | `rho_t(g)` is an endomorphism of `E_t^P`; each summand is `f^nu m_t,nu` square. | PASS |
| (1.3) | `J_(nu,tau):C^1890->C^(f^nu)` and its adjoint compose to `I_1890`. | PASS |
| (1.4)--(1.5) | Block `[mu,nu]` maps `V_nu tensor M_t,nu -> V_mu tensor M_t,mu`; `J_mu J_nu^*` is `f^mu x f^nu`, and `A_mu,nu` is `m_t,mu x m_t,nu`. | PASS |
| (1.6)--(1.7) | `B:E_0^P->E_1^P`; its parent block is `I_(f^nu) tensor B_nu` with `B_nu` of shape `m1_nu x m0_nu`.  No padding is present. | PASS |
| (2.1) | Outer block maps `V_alpha tensor M0_alpha -> V_mu tensor M1_mu`.  The carrier contraction is `J_nu^*J_nu=I_1890`; all factors share the inner parent `nu`. | PASS |
| (2.2) | The three arrows are respectively `m0_nu x m0_alpha`, `m1_nu x m0_nu`, and `m1_mu x m1_nu`. | PASS |
| (2.3) | All nine products were audited individually below and by both checkers. | PASS |
| (3.1) | `Q_t,z;tau` is an endomorphism of `E_t^P`; conjugation uses `rho_t` on that same answer space. | PASS |
| (3.2) | Each term `Q_1 B Q_0` maps `E_0^P->E_1^P`; the sum preserves `Hom_G` but is also a typed map on the full rectangular Hom space. | PASS |
| (3.3) | Both sides map `E_0^P->E_1^P`; it is exactly the intertwining identity. | PASS |
| (3.4)--(3.5) | `T_(mu,alpha):V_alpha->V_mu`, hence it is `f^mu x f^alpha`.  Coset representative independence follows from `K`-intertwining. | PASS |
| (3.6) | Zero is the unique `G`-map between unequal irreducibles `V_alpha` and `V_mu`. | PASS |
| (3.7) | Both sides are endomorphisms of `V_mu`; trace on the left is `64 f^tau`, fixing the scalar. | PASS |
| (4.1)--(4.2) | Hook dimensions, branching sums, and reduced fractions all rederive exactly. | PASS |
| (5.1) | `M0` and `M1` dimensions are respectively `16(1,3,6)` and `16(1,5,10)`. | PASS |
| (5.2) | Schur identifies the equivariant Hom with exactly three rectangular coefficient blocks. | PASS |
| (5.3) | Dimension arithmetic is exact and does not claim the full-HS dimension. | PASS |

The complete nine-term rectangular audit is:

| output `mu` | inner `nu` | `A1_(mu,nu)` | `B_nu` | `A0_(nu,mu)` | output |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | `16 x 16` | `16 x 16` | `16 x 16` | `16 x 16` |
| 1 | 2 | `16 x 80` | `80 x 48` | `48 x 16` | `16 x 16` |
| 1 | 3 | `16 x 160` | `160 x 96` | `96 x 16` | `16 x 16` |
| 2 | 1 | `80 x 16` | `16 x 16` | `16 x 48` | `80 x 48` |
| 2 | 2 | `80 x 80` | `80 x 48` | `48 x 48` | `80 x 48` |
| 2 | 3 | `80 x 160` | `160 x 96` | `96 x 48` | `80 x 48` |
| 3 | 1 | `160 x 16` | `16 x 16` | `16 x 96` | `160 x 96` |
| 3 | 2 | `160 x 80` | `80 x 48` | `48 x 96` | `160 x 96` |
| 3 | 3 | `160 x 160` | `160 x 96` | `96 x 96` | `160 x 96` |

The literal full rectangular space in this already position-carrier-suppressed alphabet model has
dimension `9,552,896 * 15,900,672 = 151,897,465,946,112`, before restoring any further spectator
carriers.  This is deliberately not `19456` and is not represented by the reducer.

## 5. Hook dimensions, coefficients, and parent pinching

The independent hook calculation gives

\[
f^{(61,2)}=1890,quad f^{(62,2)}=1952,quad
f^{(61,3)}=39648,quad f^{(61,2,1)}=79360.
\]

Therefore

\[
{64f^\tau\over f^{(62,2)}}={3780\over61},\quad
{64f^\tau\over f^{(61,3)}}={180\over59},\quad
{64f^\tau\over f^{(61,2,1)}}={189\over124}.
\]

The coefficient cannot depend on the inner parent: Schur averaging sees the outer diagonal block
and divides by its carrier dimension.  Conversely, the inner parent cannot be pinched away before
the sandwich.  In (R3.3), every `nu` contributes to the already-diagonal outer block after
`J_nu^*J_nu=I`; deleting off-diagonal seed blocks would change the transfer.

The independent `S_3/S_2` model makes both errors concrete.  Its two `S_3` parents have dimensions
`1,2` and share a one-dimensional `S_2` child, so the exact coefficients are `3,3/2`.  The direct
three-coset sum matches (R1.1) entry by entry.  Premature parent pinching changes entry `(0,0)` by
`192`, and omitting the coset index changes entry `(0,0)` by `148`.

## 6. Correlated twirl, multiplication order, and exact counterguards

For equivariant `B`, the physical summand is

\[
\rho_1(g)A_1\rho_1(g)^*B\rho_0(g)A_0\rho_0(g)^*
=\rho_1(g)(A_1BA_0)\rho_0(g)^*.
\]

The same `gK` occurs on both answers.  In the independent exact model:

- replacing the sum by `3 A_1BA_0` changes entry `(0,1)` by `-33/2`;
- multiplying independent target/source coset sums changes entry `(0,0)` by `132`;
- using the wrong Schur normalization changes entry `(0,0)` by `148`;
- prematurely pinching seed parent blocks changes entry `(0,0)` by `192`.

An independent nonsymmetric matrix gate gives

\[
\operatorname{vec}(A_1BA_0)
=(A_0^{\mathsf T}\otimes A_1)\operatorname{vec}(B),
\]

while a missing transpose, swapped seeds, and moving the source seed left of `B` give nonzero
first errors `-66,-133,-30`, respectively.  Thus the printed order is verified as a formula, not
merely accepted because the final dimensions happen to agree.

The proposer checker supplies a separate exact `S_4/S_3` model with positive-semidefinite seed
effects.  It obtains direct residual rank zero and reversed-order residual rank eight.  The two
models are distinct: the blind model uses rational `S_3` carriers, unequal parent multiplicities,
and additional normalization/twirl/pinch guards; the proposer uses a PSD `S_4` construction.

## 7. Both query sides and coefficient dimension

For `s=L`, write

\[
M_{t,\nu}=(Y_{t,\nu}\otimes Z_L)\otimes Z_R,
\qquad A^{t,L}_{\mu\nu}=\widehat A^{t,L}_{\mu\nu}\otimes I_{Z_R}.
\]

The active coefficient-space dimension is

\[
(4\cdot4)+(20\cdot12)+(40\cdot24)=1216,
\]

and the passive `Hom(Z_R,Z_R)` dimension is `4^2=16`.  Hence the full coefficient dimension is
`1216*16=19456`, and the left reducer is the active reducer tensored with the identity on the
passive Hom factor.

For `s=R`, interchange `Z_L` and `Z_R`; the passive factor is `Hom(Z_L,Z_L)`.  The proof and
normalization do not identify the two physical gauges, but apply to their respective matrices.
Exact tensor-product gates verify both orders separately.  This is the precise sense in which the
same representation-theoretic reducer applies to both sides.

## 8. Rule-7(b): regime-complete gates

| qualitative regime | identity-level evidence | result |
|---|---|---|
| NO versus YES | `m0=(16,48,96)` and `m1=(16,80,160)`; all nine unequal products audited | PASS |
| parent multiplicity one and greater than one | Physical type table contains `1,3,6` and `1,5,10`; blind `S_3` model uses unequal multiplicities `1,2` at identity level | PASS |
| every outer parent | Three distinct hook coefficients independently recomputed | PASS |
| every intermediate parent | Nine formula blocks typed; exact toy has nonzero cross-parent blocks | PASS |
| common child shared by all three parents | Multiplicity-free branching embeddings and trace `f^tau=1890` | PASS |
| private children | Deliberately absent and not used | WITHHELD |
| correlated same-coset twirl | Analytic equality and exact `S_3/S_2` enumeration | PASS |
| one representative or independent twirls | Exact nonzero counterguards | REJECTED substitutions |
| Schur parent pinch | Outer unequal parents killed only after the sandwich; premature seed pinch exact counterguard | PASS |
| source multiplication/vectorization | Direct composition plus three distinct wrong-order counterguards | PASS |
| `L` and `R` | Separate exact passive-factor tensor gates | PASS |
| equivariant versus general full-HS modes | Formula proved only on `Hom_G`; full-HS dimension and Wigner need stated | PASS boundary |
| spectrum/resolvent/exponent | No calculation and no inference | WITHHELD |

No untested regime is used in the favorable verdict.

## 9. Rule-7(c)--(g)

### 9.1 Anchoring ban

**PASS.**  The baseline and independent checker were hashed before target inspection.  The blind
derivation used a full group average and partial carrier trace; it did not reproduce a proposer
display.  The eventual formulas coincide because both compute the same Schur projection.

### 9.2 No frozen-input immunity

**PASS at the granularity used.**  The direct-coset review is used only for native unequal-answer
typing, exact covariance, and the existence of side-local fixed-mark effects.  The YES
common-child/central-insufficiency review is used only for the finite parent/multiplicity inventory
and the strict fact that the common child is not literal completion.  The new correlated coset
restriction, parent pinch, normalization, all Hom types, hook coefficients, and L/R factorization
were independently rederived.  No private-child table or full carrier kernel is declared frozen or
known.

### 9.3 Failure-mode diversity

| attack | result |
|---|---|
| dropped/extra `64` or carrier dimension | independent coefficients and exact wrong-normalization guard; PASS |
| type/dimension mismatch | all displayed maps and nine rectangular products audited; PASS |
| undefined carrier suppression | locked to the archived position-carrier-suppressed model; PASS with explicit scope |
| same-coset replaced by a colored representative | exact nonzero guard; rejected |
| same-coset replaced by independent twirls | exact nonzero guard; rejected |
| source effect moved to the wrong side/order | direct arrows, vectorization, and exact errors; rejected |
| parent cross-blocks silently deleted | premature-pinch guard; rejected |
| values agree while printed derivation is broken | analytic derivation, blind finite group, proposer finite group, and field comparison kept separate; PASS |
| common child called literal native effect | explicitly withheld; PASS |
| `19456` called full-HS dimension | explicitly refuted by the dimension audit; PASS |
| L matrix silently reused as R matrix | formulas apply separately and gauges are not identified; PASS |
| finite reducer sold as spectrum/exponent | explicitly withheld; PASS |

### 9.4 Value versus formula

The proposer rerun establishes reproducibility of proposer code.  Its `S_4/S_3` gate exercises the
printed formula with synthetic PSD seeds; it does not construct physical k-Sum fixed-child
matrices.  The blind checker independently exercises the formula in an `S_3/S_2` representation
and independently computes the finite hook/type data.  The post-seal comparison verifies that
both constructions report the same dimensions and coefficients.

The physical parent multiplicities and common-child seed blocks remain inputs at exactly the scope
of the cited prior reviews.  This review verifies the **reducer formula**, not the numerical entries
of those seed blocks and not a numerical `19456 by 19456` spectrum.

### 9.5 Quantifier hygiene

- **Finite** means only `(s,a,d,r,q)=(4,16,17,4,64)` for the physical input data.
- **Common child** means only `tau=(61,2)` in the stated three-parent sector.
- **Equivariant coefficient subspace** means the `G`-intertwiner blocks after the archived fixed
  position carriers have already been suppressed.
- **Correlated coset twirl** means one common representative `gK` transports both answers.
- **Parent pinching** means Schur projection of the completed outer sandwich, not deletion of seed
  cross-parent blocks.
- **Both sides** means the same theorem applied separately to the actual `L` matrices and actual
  `R` matrices; it does not identify them.
- **Reducer** means the restriction (R1.1), not a literal native transfer or any spectrum.

## 10. Exact license and stopping point

### Licensed

1. The finite common-`tau` fixed-mark seed, once supplied in the reviewed coefficient gauge,
   determines the correlated coset transfer on the carrier-suppressed `G`-equivariant subspace by
   (R1.1).
2. The source-side order is exactly `A^1 B A^0`, and the vectorized block is exactly (R3.7).
3. Schur parent pinching retains all three intermediate parents and supplies output factors
   `3780/61,180/59,189/124`.
4. All nine NO-to-YES Hom compositions are typed, and the coefficient-space dimension is `19456`.
5. The representation-theoretic formula applies separately to `L` and `R`, with active dimension
   `1216` and passive Hom dimension `16`.

### Explicitly withheld

1. All four private-child physical effects and any completion of the literal fixed-mark seed.
2. The literal native transfer on the full unequal-answer Hilbert--Schmidt space.
3. Every nontrivial carrier/Wigner block and every off-equivariant mode.
4. Any orientation pullback, padding, or claim that the common child is the native effect.
5. Any numerical reducer matrix built from unreviewed physical values, and every rank, kernel,
   eigenvalue, joint spectrum, or singular value of a physical transfer.
6. Any resolvent, taper, optimizer, coefficient norm, query attenuation, incidence, remainder,
   numerator, adversary lower bound, asymptotic statement, or exponent.

The proposer proof therefore receives **PASS / STRICTLY SCOPED**.  It supplies a correct finite
formula-level diagnostic and no completion of the controlling resolvent node.  No canonical or
shared DAG file was edited by this reviewer.
