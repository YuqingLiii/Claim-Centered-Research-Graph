# G2 — induced-packet payload value test at `a=16, q=64`

**Status of this artifact: NUMERICAL — pending-review.** Finite diagnostic only.
Per the target node's G11 clause, no outcome here licenses an asymptotic exponent, and
nothing in this file may be read as a completion-tier (CERTIFIED*/PROVED/REFUTED) status.
No canonical node or existing repo file is edited by this work.

- Target node (rule-8a cite):
  `KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-payload-value-test`
  (`ksum/proof-dag/nodes/…induced-packet-payload-value-test.md`).
- Commission: G2 gate batch, 2026-07-23. "Does the packet route have a computable payload
  at finite scale?"
- Executor: Opus 4.8. Everything below is re-derived from the on-disk record; the
  commissioning text is context, not authority.

## 0. Outcome (one line)

**NOT ASSEMBLABLE.** The reviewed `a=16, q=64` components do **not** assemble end-to-end into
the compressed-model candidate adversary object. Its objective value therefore has no defined
number, and no packet-vs-baseline ratio is computed. The concrete missing-piece list (§4) is the
primary finding. All finite ingredients that *are* present were independently recomputed and pass
(§5); the missing pieces are precisely the ones the reviewed record itself withholds.

This is outcome class **"not assemblable"** of the three the target node pre-registers
(node lines 36-44); it is not a REFUTED and not a payload-empty signal.

---

## 1. Scope statement

Finite point (the reviewed first-target instance; matches the packet-kernel first gate `q=4a`):

```
(s, a, d, r, q, n, N) = (4, 16, 17, 4, 64, 288, 576),   tau_* = (61,2) |- 63.
```

Here `q = 4a = 64` and `q = 64 ≈ N^{2/3} = 576^{2/3} ≈ 69.2`, i.e. the critical endpoint scaling.
The question is whether the on-disk reviewed pieces at this point compose into the complete
candidate adversary object and, if so, its value against a matched baseline.

## 2. What the "complete compressed-model candidate adversary object" IS (per the record)

The record defines the object in three layers.

**(2a) The adversary functional it must realize.** The critical endpoint's missing object is an
invariant matrix `Gamma` between the two legal orbits `E_0` (NO) and `E_1` (YES) with

```
||Gamma|| >= c·N^{2/3}      and      max_i ||Gamma ∘ Delta_i|| <= 1,
```

i.e. objective value `Adv±(Gamma) = ||Gamma|| / max_i ||Gamma ∘ Delta_i||`, target `Theta(N^{2/3})`
(critical-endpoint node, work record 2026-07-21, `…critical-endpoint.md:226-230`; status
`…critical-endpoint.md:41-46`). The proved addressed construction already reaches `N^{11/18}`
(`…critical-endpoint.md:220-225`); the packet route exists to supply the missing `N^{1/18}`
address-erasure gain.

**(2b) The compressed-model realization of `Gamma`.** `Gamma` is an alphabet-`S_q`-equivariant
multiplier

```
B = ⊕_{nu |- q} I_{S^nu} ⊗ B_nu  ∈  Hom_{S_q}(E_0, E_1)          (Schur form)
```

restricted, in the "compressed model", to the **position-carrier-suppressed** coefficient space of
dimension `D = 19456` for the three reviewed alphabet parents `P = {(62,2),(61,3),(61,2,1)}`
(equivariant-sufficiency decision §1, eqns (1.2)-(1.3),(1.8),
`…equivariant_sufficiency_decision_20260722.md:44-113`; Schur–coset reducer proof §0,§5,
`…equivariant_schur_coset_reducer_proof_20260722.md:28-56,275-308`).

**(2c) The physical maps that turn `B` into a value.** Three of them:
- the native equality-transfer superoperator `E_s(B) = sum_z F^s_{1,z} B F^s_{0,z}` and its
  defect `B - E_s(B)` (the query side), vectorized as the correlated coset twirl
  `K_s = sum_z (F^s_{0,z})^T ⊗ F^s_{1,z}` (sufficiency decision §2 eq (2.2),
  `…:148-152`; YES central-transfer decision §6 eq (6.2),
  `…first_target_yes_physical_central_transfer_decision_a16_20260722.md:233-239`);
- the operator norm `||C|| = max_nu ||C_nu||` (Schur block norm, sufficiency §3 eq (3.2),
  `…:227-232`) — the numerator size;
- the outer incidence / numerator functional applied to `B` — the adversary numerator proper.

The packet cross-Gram that would carry a nontrivial coefficient is
`K = J_L^* J_R`, the normalized Bernoulli–Laplace/Johnson swap walk on `J(2a,a)`, with spectrum
`lambda_j = 1 - j(2a-j+1)/a^2`, `0<=j<=a`, and full-type refinement
`c_{nu,j} = [s_nu] s_{2a-j,j} s_{a-1,1}^2`
(packet-kernel node, `…three-row-induced-bicovariant-alphabet-packet-kernel.md:42-91`).

## 3. Frozen inputs relied on (every on-disk component, file cite)

Reviewed (rule-7 scoped passes) finite factors at `a=16, q=64`, all cited from the packet-kernel /
occurrence-pencil node evidence lists:

| # | Component (finite, `tau_*=(61,2)`) | Result | File |
|---|---|---|---|
| F1 | `s=4` occurrence algebra | `M_1(Q) ⊕ M_3(Q)` | `ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_20260722.md`; review SHA `1741AD66…` |
| F2 | NO `tau_*` alphabet point-child table | `C^6`, ranks `1,1,3,1,3,1`, char.poly `(x-61)(x-1)^3(x+2)^6` | `ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_20260722.md`; review SHA `4A8FEE28…` |
| F3 | YES `tau_*` alphabet point-child table | `C^8`, ranks `1,1,1,1,5,1,5,1` | `ksum_L3_critical_induced_packet_yes_alphabet_point_child_gate_a16_20260722.md`; review SHA `BE1B4BD6…` |
| F4 | corrected transported Pieri scalar table | scoped pass (`rho_lambda(g)` required) | `ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_20260722.md`; review SHA `DB65748C…` |
| F5 | NO one-side physical assembly | surviving `M_3` core, active/full ranks `8/32` | `ksum_L3_critical_induced_packet_first_target_no_physical_assembly_a16_20260722.md`; review SHA `24D68034…` |
| F6 | packet first gate (`J_L,J_R,K`) at `p=0,u=1,q=4a` | `MINOR/SCOPED PASS` | packet-kernel node; review SHA `CF1E853A…` |
| F7 | direct-coset cross-side factorization | `[E_L,E_R]=0`, `P_t=⊕_xi P_L(xi)⊗P_R(xi)` | review SHA `C3A7DFD2…` |
| F8 | equivariant Schur–coset reducer (`D=19456`, factors `3780/61,180/59,189/124`) | `PASS/STRICTLY SCOPED` | `ksum_L3_critical_induced_packet_equivariant_schur_coset_reducer_proof_20260722.md`; review SHA `E062009C…` |

Proposer-tier (pending review) inputs used only to locate the assembly gap, never as licence:

| # | Component | Tier | File |
|---|---|---|---|
| P1 | YES common-`tau_*` physical assembly + central-transfer decision | proposer, pending review | `ksum_L3_critical_induced_packet_first_target_yes_physical_central_transfer_decision_a16_20260722.md` |
| P2 | equivariant sufficiency decision | proposer (guards pass) | `ksum_L3_critical_induced_packet_equivariant_sufficiency_decision_20260722.md` |

Definitional frozen inputs: critical-endpoint node `…critical-endpoint.md` (Gamma constraints,
`11/18` baseline); packet-kernel node (`J_o`, `K`, `lambda_j`, `c_{nu,j}`); occurrence-pencil node
(pencil typing, uniform algebra unclassified, `…occurrence-pencil-classification.md:36-48`);
outer-incidence node (`…outer-incidence-numerator-interface.md:32-34,55-61`, no functional frozen).

## 4. Missing-piece list (PRIMARY FINDING)

The object is not assemblable. The following components/definitions/normalizations are absent from
the reviewed (and even the proposer-tier) record at file level. No difficulty is asserted for any —
only presence/absence.

**M1 — The four private point-children (both answers) are undefined; no construction exists.**
The three parents `P` restrict to five point-children `(61,2),(62,1),(60,3),(60,2,1),(61,1,1)`
(exact `S_64↓S_63` branching, verified §5). The reviewed NO/YES point-child tables (F2,F3) contain
**only the common mark `tau_* = (61,2)`**. The four private children `(62,1),(60,3),(60,2,1),(61,1,1)`
have no reviewed and no proposer table on disk. The literal effect `F_{t,z}` sums every point-child,
so without these the literal `F_{t,z}` and the transfer are undetermined.
Cite: P1 §1.3,§7 (`…yes_physical_central_transfer_decision_a16_20260722.md:40-43,254-331`, "four
missing private children"); §12 withholds "all private-child physical row values" (`:439`);
Schur reducer §6 boundary 1 (`…equivariant_schur_coset_reducer_proof_20260722.md:319-323`);
KSUM_PROVER_PROMPT names these four as the active gates.

**M2 — The correlated carrier/Wigner kernel `Omega_tau` (eq. 8.2) is defined but not evaluated.**
Expanding even the common-`tau_*` partial orbit into the full rectangular Hilbert–Schmidt transfer
requires `Omega_tau = sum_z (P^{nu'_0<-nu_0}_{0,tau,z})^T ⊗ P^{nu'_1<-nu_1}_{1,tau,z}` built from
the branching isometries `rho_nu((z,64)) iota_{nu,tau}` for 3 parents × 5 children × 64 marks,
contracted same-`z`. "No reviewed artifact evaluates it."
Cite: P1 §8 eqns (8.1)-(8.2) (`…yes_physical_central_transfer_decision_a16_20260722.md:334-367`),
§12 withheld "the evaluated carrier/Wigner kernel" (`:440`); Schur reducer §6 boundary 2 (`:324-328`).

**M3 — The literal native central transfer `K_s` (the objective operator) is not assembled.**
`K_s = sum_z (F^s_{0,z})^T ⊗ F^s_{1,z}`, its rank, kernel, and spectrum are all withheld; they
depend on M1+M2. There is no on-disk value, spectrum, or even a full `40960×…` matrix for it.
Cite: P1 §1.4 (`…:44-46`), §12 withheld "the literal native central transfer, its rank, kernel, or
spectrum … any joint spectrum" (`:441-442`).

**M4 — The literal marked-query / polar-norm interface (the adversary denominator) is unfixed.**
No frozen polar/range-reducing identity equates the compressed effect defect `||B - E_s(B)||` with
the literal physical query-mask norm `max_i ||Gamma ∘ Delta_i||`. The record proves they differ in
general: an exact guard gives `||Delta(B)||^2 = 1/2` while `||B - E_s(B)||^2 = 1/4` (strict gap).
Cite: P2 §4 eqns (4.1)-(4.5) (`…equivariant_sufficiency_decision_20260722.md:289-344`), ledger row
"Is `B-E_s(B)` already the literal physical query defect …? **BLOCKED**" (`:382`), §9 item 1
(`:444-445`). Registered OPEN carrier nodes for this map:
`…ALT.literal-marked-query-polar-norm-interface`, `…ALT.polar-offdiagonal-block-law`,
`…ALT.physical-range-reducing-equality-law`, `…ALT.hs-query-energy-law` (all OPEN, NODE_INDEX
lines 92-95).

**M5 — The outer incidence / numerator map (the adversary numerator) is undefined.**
"No exact outer incidence functional, normalization, or numerator-active subspace is currently
frozen." Equivariance does not determine it (underdetermination guard: `N_1(B)=e_1^*Be_1` and
`N_2(B)=e_1^*Be_2` are both `S_q`-invariant yet give `1` and `0` for `B=I_2`).
Cite: outer-incidence node Current status + Open obligations
(`…induced-packet-outer-incidence-numerator-interface.md:32-34,55-61`); P2 §5 (`:346-370`),
ledger row "Does the outer numerator close …? **BLOCKED**" (`:383`).

**M6 — The `D=19456` compressed model is not a norm-complete operator model (normalization
unlicensed).** It suppresses the two position Specht carriers `P = S^{lambda}_L ⊗ S^{lambda}_R`
(`lambda=(283,4,1)`, `dim P = p^2`; strict hierarchy `D < p^2 D < p^2 d_0 d_1`, verified §5).
Alphabet equivariance does **not** make that suppression norm-preserving: a fixed-coordinate query
branches the active position carrier through `beta_T,beta_M,beta_B`, so `||C|| = max_nu ||C_nu||` on
the `19456` slice is a coefficient diagnostic, not a licensed physical operator norm.
Cite: P2 §1 (eqns 1.9-1.12), §3 (eqns 3.4-3.6, `…:244-287`), ledger row "Does the `19456`
position-suppressed slice suffice …? **NO LICENSE**" (`:381`); Schur reducer §6 boundary 2/3 (`:324-335`).

**M7 — No adversary coefficient law `B_nu` / `b_{j,h,k}` is chosen or frozen.** Even given M1-M6,
the actual multiplier has no value. A constant/scalar `B_j` reduces exactly to the already-capped
`N^{11/18}` addressed-UIC baseline (packet-kernel node scope-collapse note,
`…packet-kernel.md:172-181`). The three nonseparable candidate laws are OPEN and untested —
Young-holonomy, joint-parent-content (total-energy/Cauchy–Sylvester resolvent), plaquette-flow — as
is the rectangular-transfer-resolvent law.
Cite: packet-kernel node work record "recorded but not tested" (`:182-195`); NODE_INDEX OPEN nodes
`…induced-packet-young-holonomy-law` (86), `…induced-packet-joint-parent-content-kernel` (87),
`…induced-packet-total-energy-resolvent-law` (89), `…induced-packet-rectangular-transfer-resolvent-law` (91),
`…induced-packet-plaquette-flow-law` (97).

**Assembly dependency summary.** Numerator side needs M3 (⇐ M1+M2) and M5; denominator side needs
M4; the norm model needs M6; and a specific number needs M7. Every one of the five layers in §2 has
at least one undefined or unevaluated input. Hence the object cannot be assembled or valued.

## 5. What IS present — independent finite verification (reproducible)

Because the object is not assemblable, no objective value is computed. Instead, every finite
quantity on which the §2 *definition* rests was re-derived from scratch (hook-length formula,
branching, exact rationals) and matched to the reviewed artifacts. All 30+ gates pass:

- Hook dimensions of all eight partitions: `(62,2)=1952, (61,3)=39648, (61,2,1)=79360`;
  `(61,2)=1890, (62,1)=62, (60,3)=37758, (60,2,1)=75579, (61,1,1)=1891`.
- Exact `S_64↓S_63` branchings and dimension resolutions
  `1952=1890+62`, `39648=1890+37758`, `79360=1890+75579+1891`; child sets reproduced.
- Reducer factors `64 f^{(61,2)}/f^mu = 3780/61, 180/59, 189/124`.
- `m_0=(16,48,96)`, `m_1=(16,80,160)`, `D = 16·16+48·80+96·160 = 19456`.
- Alphabet-module dims `d_0 = 9,552,896`, `d_1 = 15,900,672`; position carrier
  `f^{(283,4,1)} = 62,660,742,144`, `p^2 = 3,926,368,606,036,857,716,736`; strict hierarchy
  `D < p^2 D < p^2 d_0 d_1` holds.
- Johnson cross-Gram spectrum at `a=16`: `lambda_j` exact rationals from `1` (`j=0`) down to
  `-1/16` (`j=16`); contrast kills `j=0`; smallest nonzero contrast singular value `2/sqrt(a)=1/2`;
  `||J_L - J_R||^2 = 17/8`, `||J_L + J_R||^2 = 4`.

These confirm the reviewed finite ingredients (F1-F8, and the §2 definitional constants) are
present and correct. They do **not** constitute the object; they are the boundary against which
M1-M7 are the exact remainder.

## 6. Matched composition baseline (defined for context; no ratio computable)

**Definition.** The proved composition/claw structure in the record is the addressed
`UIC_a ∘ pSearch_{d+1}` construction (critical-endpoint node, `…:220-225`), giving
`Adv±  = Theta(a^{2/3}·sqrt(d+1)) = Theta(sqrt(N)·q^{1/6}) = Theta(N^{11/18})` at the endpoint.

**Matching choices (explicit).** Instance size `N=576`, alphabet `q=64`, promise = the exact
rare-singleton/heavy-decoy critical promise the packet route itself targets, with `a=16, d=17`
(same finite point as §1). The packet route is worth bridging to only if it **exceeds** this
baseline en route to the target `N^{2/3}`.

**Values at matched parameters (scaling forms).**
`a^{2/3}·sqrt(d+1) = 26.94`,  `sqrt(N)·q^{1/6} = 48.00`,  target `N^{2/3} = 69.23`.

**No ratio is computed**, for two independent reasons: (i) the packet object has no value (§4,
not assemblable); and (ii) the two baseline scaling forms disagree numerically at finite scale
(26.94 vs 48.00), so the multiplicative constant (from the ED unique-collision bound and the BHK
composition) is not pinned at finite scale in the record — the baseline itself is a scaling form,
not a single finite number. Reporting a ratio would be fabricated precision.

## 7. Commands, logs, and SHA-256

- Script: `ksum/artifacts/ksum_L3_payload_value_test_a16_20260723_finite_verify.py`
  SHA-256 `B1E68FD20592FE5FD9A66BA4F3D010901D9588E98F3C8991B62CAB83936AED57`.
- Command (Git Bash):
  ```
  "<machine-local-path-redacted>" \
    ksum/artifacts/ksum_L3_payload_value_test_a16_20260723_finite_verify.py \
    > ksum/artifacts/logs_ksum_L3_payload_value_test_a16_20260723/finite_verify.log 2>&1
  ```
- Log: `ksum/artifacts/logs_ksum_L3_payload_value_test_a16_20260723/finite_verify.log`
  SHA-256 `AC116562CCBA80A0C8C038785D486696A54AE4A4C44BF5F694DFFEB6ABD7F0BB`.
- Interpreter: CPython 3.11.9, numpy 1.26.4, sympy 1.13.1 (numpy/sympy not required by the script;
  arithmetic is exact Python big-ints / `fractions`).
- Terminal status line: `ALL_FINITE_VERIFICATION_GATES_PASS`.

## 8. What would change this outcome

- **M1+M2 supplied and reviewed** (the four private NO/YES point-child tables and an evaluated
  `Omega_tau`): then `K_s` (M3) becomes assemblable and the transfer spectrum could be computed —
  turning "not assemblable" into a value question, still gated by M4-M6.
- **A frozen polar/range-reducing identity (M4)** equating `||B - E_s(B)||` with the literal query
  mask norm on the active `beta` blocks: fixes the denominator; without it the query cost is
  undefined even if the numerator exists.
- **A frozen outer incidence/numerator map (M5)** with typed domain/codomain and nonvanishing on
  the equivariant coefficient: fixes the numerator; the underdetermination guard shows equivariance
  alone cannot supply it.
- **A norm-completeness theorem for the `19456` slice (M6)**, or a full `Hom_{S_q}` (unsuppressed
  position-carrier) computation: without one, any operator norm read off the `19456` slice is
  unlicensed as the physical `||Gamma||`.
- **A specific nonseparable coefficient law `B_nu` (M7)** from one of the registered OPEN nodes
  that survives its own query/numerator gates: only then does a concrete finite value exist to
  compare to the baseline.
- Conversely, a proof that any coefficient with `o(1)` compressed query defect also kills the outer
  numerator (a kill criterion already registered on the outer-incidence node) would push this toward
  the **payload-empty** outcome class — still NUMERICAL, still not a REFUTED (G11).

Any of these is itself a separate proof obligation requiring its own rule-8 node, proposer work,
and fresh rule-7 review before it could lift this artifact above NUMERICAL — pending-review.
