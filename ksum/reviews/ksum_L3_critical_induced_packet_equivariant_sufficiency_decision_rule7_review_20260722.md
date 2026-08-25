# Fresh hostile Rule-7 review: equivariant-sufficiency decision

Date: 2026-07-22  
Reviewer: independent instance; did not author the target decision or target checker  
Controlling node: read only; no canonical/shared DAG file edited  
Reviewed target:
`ksum/artifacts/ksum_L3_critical_induced_packet_equivariant_sufficiency_decision_20260722.md`

## 1. Verdict

**MINOR / STRICTLY SCOPED PASS for the stated PARTIAL theorem.**

The positive theorem is correct.  For the complete raw-value sum, covariance makes each native
transfer `mathcal E_s` preserve `Hom_(S_q)(E_0,E_1)`.  The defect `I-mathcal E_s`, the restrictions
of the commuting positive self-adjoint left/right transfers, and every defined joint functional
calculus remain on that equivariant space.  Schur's lemma gives the exact rectangular block norm

\[
 \left\|\bigoplus_\nu I_{S^\nu}\otimes B_\nu\right\|_{op}
 =\max_\nu\|B_\nu\|_{op}.
\tag{R1.1}
\]

This proves that the nontrivial alphabet-`S_q` Wigner complement is not needed for the **internal
calculation of this fixed equivariant multiplier architecture**.  It does not prove that an
arbitrary adversary may be averaged without loss, and the target correctly makes no such claim.

The target also correctly rejects a stronger inference: `19456` is not a norm-complete model of
the unsuppressed `Hom_(S_q)`.  It is the coefficient count after setting two enormous position
Specht carriers to spectator identities.  The target's exact position counterguard is valid, and
the independent blind checker supplies two additional exact guards: an omitted equivariant
position mode can have suppressed slice zero and norm one, and a nonreducing parent compression
can report residual norm `9/25` while the full Schur-block norm is `12/25`.

Two MINOR corrections/scopes are required.

1. In target (4.1), the physical projections must be written
   `Q_(1,z) W_1 B W_0^* Q_(0,z)`.  A single literal `Q_z` cannot act on both unequal raw answer
   spaces unless it is explicitly declared overloaded.  The target's subsequent toy has equal
   two-dimensional raw spaces and is correct; this is a physical-display typing repair.
2. “Exactly two missing interfaces” is correct only when **interface** means the two maps crossing
   from the equivariant multiplier calculation to (i) the literal marked-query norm and (ii) the
   physical outer numerator.  It is not a claim that only two mathematical obligations remain.
   The first interface package must include every active position branch, every physical
   common/private marked child and reached parent, and the full YES range.  Complete restricted
   transfer values/spectrum, a defined taper/resolvent parameter, coefficient bounds, and
   attenuation remain internal construction obligations after the interfaces are typed.  The
   target already lists these as withheld, so this is a scope-lock clarification rather than a
   change to its theorem.

With those readings, there is no third **Wigner-facing** interface hidden by the target.  Position
carriers are retained inside `K_(t,nu)` rather than suppressed, and complete marked rows belong to
the literal-query interface.  There are, however, more than two remaining tasks before an
adversary lower bound exists.

The target licenses no completion status for the controlling node, no exponent, and no launch of
either successor interface.

## 2. Hostile-blind seal and manifest-first comparison

Both repository protocols were read in full.  Before opening or grepping the target decision, its
checker, JSON/log, checksum, or the canonical current sufficiency conclusion, I read only the
already-reviewed complete-packet, direct-coset, and Schur--coset inputs and sealed

`ksum/artifacts/ksum_L3_critical_induced_packet_equivariant_sufficiency_decision_rule7_blind_baseline_20260722.md`

at SHA-256
`D246FB73BA591F5B0A1C3F7483212DB232AAC951BCB72ED1E4D86B3CFEEB8D33`.
The pre-target manifest has SHA-256
`1E08882B7C3635D7A3D9637B4342C4C9A2DA7469F6BE00A27A88AA823919E605`.

The independent pre-target checker is
`ksum/tools/ksum_l3_equivariant_sufficiency_rule7_independent.py`.  It imports no proposer object and
reports `ALL_EQUIVARIANT_SUFFICIENCY_RULE7_BLIND_GATES_PASS` in
`ksum/artifacts/logs_ksum_L3_equivariant_sufficiency_rule7_review_20260722/independent.log`.

Only after that seal was fixed did I open the proposer manifest.  Its five listed decision-object
hashes match the current bytes.  In particular:

| target object | SHA-256 |
|---|---|
| decision | `FD917A96001D8A4B869CF4BF8C2C634CCA365EF8D349754818454C1998C09792` |
| checker | `0E43247DD5C66CB93A8A9F5F91EB55B3CBA1926ABAC3633161E2B0993B8570C7` |
| JSON | `06FB00CDC83EC560861B8991060EE5505EE93C2247258FD3310ACCA698E8C068` |
| log | `E0F1D5328E407CFC80E4038516CBD9863C572C10D3634186940B28DCA1E86836` |
| manifest | `D71C855CF01595E37D7E5971F6455D7461A1F8164B61C43DDAB8133267BA1561` |

The proposer checker was rerun after inspection.  It again printed
`ALL_EQUIVARIANT_SUFFICIENCY_DECISION_GUARDS_PASS`; JSON and log remained byte-identical.

The post-seal comparison checker
`ksum/tools/ksum_l3_equivariant_sufficiency_rule7_target_compare.py` imports neither checker.  It pins
both manifests, independently recomputes all hook/dimension values, and independently reconstructs
the literal/compressed and position-suppression gaps.  It reports
`ALL_EQUIVARIANT_SUFFICIENCY_TARGET_COMPARISON_GATES_PASS`.

## 3. Independent derivation

Let `G=S_q`, let `rho_t:G->U(E_t)`, and equip
`H=Hom(E_0,E_1)` with the Hilbert--Schmidt inner product.  The unitary conjugation action is

\[
 U_g(B)=\rho_1(g)B\rho_0(g)^*,
 \qquad H^G=\operatorname{Hom}_G(E_0,E_1).
\tag{R3.1}
\]

For complete covariant effect families

\[
 F^s_{t,gz}=\rho_t(g)F^s_{t,z}\rho_t(g)^*,
\]

put

\[
 \mathcal E_s(B)=\sum_zF^s_{1,z}B F^s_{0,z}.
\tag{R3.2}
\]

Direct substitution and relabelling give

\[
 U_g\mathcal E_s(B)=\mathcal E_sU_g(B).
\tag{R3.3}
\]

Thus `H^G` is invariant.  Since `mathcal E_s` is self-adjoint on `H`, invariance makes `H^G`
reducing.  The reviewed full-space identity `[mathcal E_L,mathcal E_R]=0` descends to commuting
self-adjoint restrictions.  The joint spectral theorem proves closure of every function defined
on their restricted joint spectrum.  This derivation uses neither the target's `C_2` values nor
its printed proof.

For orthogonal isotypic decompositions

\[
 E_t=\bigoplus_\nu S^\nu\otimes K_{t,\nu},
\]

Schur's lemma gives

\[
 H^G=\bigoplus_\nu I_{S^\nu}\otimes
       \operatorname{Hom}(K_{0,\nu},K_{1,\nu}).
\tag{R3.4}
\]

Orthogonality of the direct sum and `||I tensor B_nu||=||B_nu||` prove (R1.1).  If
`K_(t,nu)=P tensor M_(t,nu)` and the particular candidate is literally
`I_P tensor b_nu`, its norm is `max_nu||b_nu||`.  Schur's lemma alone does not force the `I_P`.

At the reviewed finite target,

\[
 \dim P=(f^{(283,4,1)})^2
       =(62{,}660{,}742{,}144)^2,
\]

and

\[
 \sum_\nu m_{0,\nu}m_{1,\nu}
 =16^2+48\cdot80+96\cdot160=19456.
\tag{R3.5}
\]

Therefore the full three-parent `Hom_G` dimension retaining `P` on both source and target is
`(dim P)^2 19456`, exactly as the target states.  The number 19456 itself cannot control position
blocks.

## 4. Exact counterguards

### 4.1 Position suppression

Let `W=C^2` be an alphabet-trivial position carrier and `V` any nontrivial two-dimensional
`S_3`-module.  Then

\[
 X=\operatorname{diag}(1,-1)\otimes I_V
\]

is an `S_3`-intertwiner of norm one, while its normalized partial trace over `W` is zero.  Hence a
position-suppressed slice can miss norm-one operators even **inside** `Hom_G`.

The target's different fixed-mark counterguard is also exact.  Marking `B=I_2` by
`P_0=diag(1,0)` leaves true defect norm one, while replacing the marked block by its normalized
position trace gives defect norm `1/2`.  These constructions verify the logical and row-level
failure modes separately.

### 4.2 Parent-slice leakage

The exact positive self-adjoint contraction

\[
 T={1\over25}\begin{pmatrix}16&12\\12&9\end{pmatrix},
 \qquad T^2=T,
\]

maps the retained first block into the omitted second block.  For `b=(1,0)`,

\[
 (I-T)b=(9/25,-12/25).
\]

The compressed residual norm is `9/25`; the full Schur-block operator norm is `12/25`.  Thus a
19456-like parent slice is norm-complete only after it is proved reducing.  The target avoids this
error by moving the closure theorem to full `Hom_G`; it does not prove the three-parent 19456
slice reducing.

### 4.3 Literal versus compressed defect

For the target's exact isometries and projections,

\[
 W_0=(1,0)^T,quad W_1=2^{-1/2}(1,1)^T,quad
 Q_0=\operatorname{diag}(1,0),\quad Q_1=\operatorname{diag}(0,1),
\]

direct multiplication gives literal defect norm squared `1/2` but compressed effect-defect norm
squared `1/4`.  This independently proves that closure of `B-mathcal E(B)` is not a physical query
norm theorem.

### 4.4 Wigner modes and forbidden averaging inference

In the `S_3` permutation representation, `diag(1,-1,0)` has norm one and conjugation twirl zero.
The test numerator `X_(11)-X_(22)` changes from `2` to `0`.  Therefore no claim that arbitrary
adversaries can be averaged without loss is available.  This does not conflict with candidate-
specific closure: starting with a fixed intertwiner and applying an equivariant transfer generates
no such mode.

## 5. Rule-7(a): display-by-display type audit

Write `p=dim P`, `d_t=sum_nu f^nu m_(t,nu)`, and let `R_t` denote the physical raw answer space.

| target display | domain/codomain and dimensions | audit |
|---|---|---|
| (1.1) | `E_t=direct-sum S^nu tensor K_(t,nu)`; each summand has dimension `f^nu dim K_(t,nu)` | PASS; all nonalphabet factors are retained in `K` |
| (1.2)--(1.3) | each block maps `S^nu tensor K_(0,nu) -> S^nu tensor K_(1,nu)` and is `I_(f^nu) tensor B_nu` | PASS for unequal multiplicities and all `nu` |
| (1.4) | `I_P tensor b_nu:P tensor M_(0,nu)->P tensor M_(1,nu)` | PASS as a stronger ansatz, not a Schur consequence |
| (1.5)--(1.12) | scalar dimension identities; in the three-parent sector `dim E_t=p d_t`, `dim Hom_G=p^2D`, full HS `p^2d_0d_1` | PASS; independent hook calculation agrees exactly |
| (2.1) | `F_(t,z):E_t->E_t`; conjugation stays in `End(E_t)` | PASS |
| (2.2)--(2.5) | `mathcal E_s,D_s:Hom(E_0,E_1)->Hom(E_0,E_1)` | PASS; complete raw-value sum is load-bearing |
| (2.3) | every factor maps `E_0->E_1` after the adjacent endomorphisms; output is a rectangular intertwiner | PASS |
| (2.6) | Hilbert--Schmidt inner products on the same rectangular space | PASS; establishes reducing complement |
| (3.1)--(3.3) | `C:E_0->E_1`; `C_nu:K_(0,nu)->K_(1,nu)`; `c_nu:M_(0,nu)->M_(1,nu)` | PASS; operator and HS carrier factors are distinct and correct |
| (3.4) | `U,B,P_0` are `2 by 2` endomorphisms of the toy position carrier | PASS as counterguard, not physical value |
| (3.5)--(3.6) | finite carrier dimensions and scalar probability resolutions | PASS; sums and branch dimensions are exact |
| (4.1) | physical `W_t:E_t->R_t`; literal map `R_0->R_1` must be `Q_(1,z)W_1BW_0^*Q_(0,z)` | **MINOR notation repair**: one `Q_z` is overloaded across unequal spaces |
| (4.2) | `W_1^*:R_1->E_1`, literal map `R_0->R_1`, `W_0:E_0->R_0`; compression maps `E_0->E_1` | PASS after the preceding subscript repair |
| (4.3) | operator norms of maps `E_0->E_1` and `R_0->R_1` | PASS by isometric compression |
| (4.4)--(4.5) | toy has `E_0=E_1=C`, `R_0=R_1=C^2`; all products are typed | PASS; exact strict gap |
| (5.1) | `N_1,N_2:End(C^2)->C` | PASS as an underdetermination guard; not a proposed physical numerator |

## 6. Rule-7(b): regime-complete gates

| qualitative regime | evidence | result |
|---|---|---|
| complete raw sum versus one color | analytic covariance reindexing; target explicitly excludes colored term | PASS |
| NO/YES unequal ranks | target `C_2` gate uses multiplicities `(1,2)` versus `(2,1)`; physical dimensions are unequal | PASS |
| multiplicity one and greater than one | exact `C_2` identity gate and physical `(16,48,96)/(16,80,160)` | PASS |
| left/right | independently reviewed full-space commutation descends to the reducing restriction | PASS; target does not identify gauges |
| polynomial/resolvent/taper | exact restricted matrices plus analytic joint spectral theorem | PASS only when the function is defined |
| alphabet carrier versus coefficient | Schur norm proof and exact finite dimensions | PASS |
| position identity versus active mark | two distinct exact counterguards and physical three-branch inventory | PASS; 19456 rejected as full norm model |
| retained parent versus leakage | independent exact `9/25` versus `12/25` guard | PASS boundary; no three-parent invariance claimed |
| effect versus literal query | exact `1/4` versus `1/2` norm-square gap | PASS boundary |
| numerator | two invariant readouts give `1` and `0` on the same multiplier | PASS underdetermination boundary |
| common/private marked children | complete physical rows remain absent | WITHHELD inside interface 1 |
| restricted physical spectrum/taper parameter | no physical calculation | WITHHELD; not used in positive verdict |
| arbitrary-adversary symmetrization | exact twirl-loss guard; target disclaims it | REJECTED inference |

No untested regime is used to support the partial theorem.

## 7. Rule-7(c)--(g)

### 7.1 Anchoring ban

**PASS.**  The blind baseline, checker output, and manifest were hashed before any target object or
canonical conclusion was opened.  The independent proof used the fixed-point subspace of the
conjugation representation and an orthogonal Schur decomposition.  The eventual notation agrees
because the objects are standard; the target's `C_2` construction was not copied.

The sealed baseline initially treated position factorization and complete marked-parent closure as
separate candidate prerequisites.  The target answers the first by rejecting the 19456 reduction
and retaining position factors in `K_(t,nu)`; it packages the second into the complete literal-
query interface.  That is why the final finding is MINOR rather than the baseline's pre-registered
MAJOR branch for an unqualified “only two tasks” claim.

### 7.2 No frozen-input immunity

* The complete-packet review is used only for an actual full induced source and the explicit fact
  that query/numerator work remains open.
* The direct-coset review is used at its reviewed complete aggregate scope: covariance, unequal
  physical answers, self-adjoint positive transfers, and full-space L/R commutation.
* The Schur--coset review is used only for the three-parent coefficient inventory and the warning
  that 19456 suppresses fixed position carriers.  Its common-child formula is not called a full
  transfer and its private-child omissions are retained.
* The occurrence review was reopened for the literal/effect type distinction and polar boundary.
  It explicitly says deterministic marked rows and private-child values remain absent.
* The Pieri review was reopened only for the active position-branch warning.  Its corrected
  transporter statement is not promoted to a physical assembled effect.

Thus no old review is used beyond its audited granularity.

### 7.3 Standing failure-mode audit

| attack | result |
|---|---|
| dropped/extra carrier factor | operator norm has none; HS norm has `f^nu` and, under `I_P`, `p`; PASS |
| type/dimension mismatch | all displays audited; (4.1) needs `Q_(1,z),Q_(0,z)`; MINOR |
| undefined “equivariant” | fixed as alphabet `S_q`, with positions retained in multiplicity; PASS |
| colored orbit substituted for complete sum | target explicitly uses and requires complete `z` sum; PASS |
| value gate sold as formula proof | closure and norm are analytic; exact toys are counterguards only; PASS |
| 19456 sold as full `Hom_G` | explicitly rejected; PASS |
| carrier trace sold as norm isometry | exact strict counterguard rejects it; PASS |
| nonreducing parent compression | target does not claim three-parent closure; independent guard records danger; PASS boundary |
| common child sold as native transfer | target withholds private children and physical spectrum; PASS |
| compressed effect sold as literal query | exact strict-gap guard rejects it; PASS |
| representation type sold as numerator | exact underdetermination guard rejects it; PASS |
| arbitrary adversary group-averaged | expressly not claimed; independent twirl-loss guard; PASS |
| finite diagnostic sold as exponent | exponent and lower bound withheld; PASS |

### 7.4 Value versus formula

The target rerun verifies reproducibility of its own exact values.  Its `C_2` model exercises
closure and a defined rational functional calculus, but it does not construct physical k-Sum
marked rows.  The target's position and literal-query toys establish logical counterexamples, not
physical values.  Independent analytic arguments establish the printed covariance, reducing-
subspace, joint-functional-calculus, and Schur-norm formulas.  The post-seal comparison script
independently recomputes every displayed dimension and both exact target norm gaps.

No code here verifies a physical 19456-by-19456 transfer, private-child matrix, spectrum, taper,
query attenuation, or numerator; the verdict does not claim otherwise.

### 7.5 Quantifier hygiene

* **Equivariant** means fixed by the alphabet `S_q` conjugation action; it does not mean invariant
  under position permutations.
* **Complete raw-value transfer** means the full physical sum over every raw value and all marked
  branches, not the reviewed common child alone.
* **19456 slice** means the three-parent alphabet multiplicity coefficient space after both fixed
  position Specht carriers are set to identities.
* **Norm-complete** means exact for a specified operator family under the physical operator norm;
  19456 is not norm-complete for unsuppressed `Hom_(S_q)`.
* **Wigner complement** means the nontrivial isotypic complement of the alphabet-conjugation
  representation on the full rectangular Hilbert--Schmidt space.  It does not include arbitrary
  position endomorphisms, which already lie in the trivial alphabet sector.
* **Two interfaces** means the two cross-space packages described in Verdict item 2.  It does not
  mean two remaining calculations before a lower bound.
* **Defined functional calculus** means the function is defined on the restricted joint spectrum;
  no invertibility or taper parameter is inferred.
* **Partial theorem** means closure and diagnostic norm structure only, with no query bound,
  numerator, adversary lower bound, asymptotic statement, or exponent.

## 8. Exact license and stopping point

### Licensed

1. `Hom_(S_q)` is closed under the complete aggregate `mathcal E_s` and `I-mathcal E_s`.
2. The restricted left/right transfers are commuting self-adjoint operators; their defined joint
   functional calculus stays in `Hom_(S_q)`.
3. The Schur-block operator norm is the maximum coefficient-block norm, even with unequal ranks.
4. The nontrivial alphabet-Wigner complement need not be diagonalized for this candidate's
   internal restricted calculation.
5. The 19456 position-suppressed common-child coefficient slice is **not** a licensed full norm
   model.
6. The two missing Wigner-facing interfaces are the complete literal-query/polar norm package and
   the outer incidence/numerator package, with the scope locks above.

### Explicitly withheld

1. position-carrier suppression or three-parent reducing closure;
2. complete physical common/private marked rows and their values;
3. literal query norm equality;
4. complete restricted spectrum, resolvent/taper parameter, and attenuation;
5. outer incidence/numerator survival;
6. optimality or lossless symmetrization of arbitrary adversaries;
7. any lower bound or exponent.

The target therefore receives **MINOR / STRICTLY SCOPED PASS** as a Rule-7-quality PARTIAL theorem.
The controlling node remains OPEN.  This reviewer did not edit the canonical/shared DAG and did
not start either successor interface.
