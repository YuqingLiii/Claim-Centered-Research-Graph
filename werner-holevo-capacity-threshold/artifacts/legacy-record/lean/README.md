# WHGAP — DAG-mirroring Lean 4 development (tier T1 + T2 + a minimal T3 layer)

Root DAG node: [`WHGAP.goal`](../nodes/WHGAP.goal.md).
Read that node, [`research/DAG_PROTOCOL.md` §7](../../../../research/DAG_PROTOCOL.md) and
[`research/RESEARCH_STRUCTURE_PROTOCOL.md` §4 item 7](../../../../research/RESEARCH_STRUCTURE_PROTOCOL.md)
**before** touching anything here — they carry the scope clauses that say what a green build in
this directory does and does not license.

This project is a *sibling of* `nodes/`, by the 2026-07-30 location amendment: a node's prose
claim and its formal claim are the same kind of object at different precision, so they are
filed together.

## Tier declaration (DAG protocol §7.8)

**T1 (conditional composition) + T2 (analytic/algebraic cores) + a deliberately MINIMAL T3
layer (von Neumann entropy of real symmetric matrices), lead-authorized 2026-07-31.**

* **T1** — the DAG's composition proofs are machine-checked against an abstract
  `CapacityInterface`: `«zero-capacity-application».composition` (P2 ⟹ P4),
  `«qpositive-onset».composition` (P9 ⟹ P3), `«order-boundary».composition` (P2 + two explicit
  hypotheses ⟹ `x_B = 1/2`), and `goal.composition` (P3 + P4 + P13 ⟹ the determination of
  `{x ∈ (0,1) : Q = 0}`).
* **T2** — the self-contained scalar cores are proved outright: the P14 flagship
  (`f_pos`, `argument_coincidence`, `prefactor_eq`/`prefactor_pos`, `Delta_closed_form_pos`),
  the P6 gap/threshold identities, the P2 forcing identities and defect eigenvalue sign
  analysis, and the P9 `d₁` sign analysis + `ε log(1/ε)` witness extraction + the 2×2 block
  invariants of paper Lemma 6.1 (`blockA_trace_det`); LEAN-2 added the basis-free core of
  paper Thm 3.3 (`WHGAP/Support/DefectChoi.lean`) and the §6 witness expansion theorem
  (`WHGAP/Support/IcScalar.lean`); LEAN-3 added paper Lemma 4.1's `x = 1` display
  (`WHGAP/Support/SelfComplement.lean`) and paper `eq:charpoly` itself
  (`DefectChoi.charpoly_Cmat`, unconditional in `x`); LEAN-3 WP-D added the **channel
  layer** `WHGAP/Support/Channel.lean` — the Kraus set, the padded complement, the
  forced-point lift with its HS adjoint, the defect superoperator, and the two
  identification theorems `choi_defect_eq_Cmat` and `outB_eq`/`outE_eq` that close
  residuals (a) and (c) of `Trust.lean`; LEAN-4 WP-G added §8 of the same file — the §6
  witness state and its two outputs over `ℂ`, with `specB_charpoly`/`specE_charpoly`
  closing residual (b) at characteristic-polynomial level; LEAN-5 WP-H then added
  `WHGAP/Support/EntropyC.lean` — the complex-Hermitian entropy layer that carries those
  charpolys to `IcScalar x ε = S(Λ_x(ρ_ε)) − S(Λ^c_x(ρ_ε))`, **discharging residual (b)**
  (see "What a green build here does NOT establish", item 10, for what remains).
* **T3 (opened 2026-07-31, lead directive quoted verbatim in
  `notes/WHGAP_COMMISSION_LEAN2_20260731.md`) — `WHGAP/Support/Entropy.lean` and, since
  2026-08-01 (LEAN-5 WP-H), its sibling `WHGAP/Support/EntropyC.lean`.**  `Entropy.lean`
  develops `vnEntropy` for **real symmetric** matrices (`∑ negMulLog λᵢ` over
  `Matrix.IsHermitian.eigenvalues`), the eigenvalue-multiset/charpoly bridge, the diagonal
  case, similarity invariance and block-diagonal additivity — just enough to *compute* the
  two Holevo quantities of paper Lemma 7.1 from explicit matrices.  `EntropyC.lean` re-runs
  the definition and the multiset bridge over `ℂ` (`vnEntropyC`,
  `eigenvaluesC_multiset_eq`, `vnEntropyC_eq_sum_of_charpoly(_list)`) for the §6 witness,
  whose outputs are genuinely complex Hermitian.  **Neither is a channel library:** there
  are no Choi matrices as channel objects, no complete positivity, no coherent information
  as a channel functional and no blocklength anywhere in this development, and neither
  module presupposes eigenvalue positivity or normalization.

## Scope clauses (DAG protocol §7.9 — verbatim)

> A theorem proved against an abstract interface is exactly as strong as the results that
> interface cites, and not one notch stronger.

> `lean-checked` is an evidence attribute, never a status.

Per `RESEARCH_STRUCTURE_PROTOCOL.md` §4 item 7 and `DAG_PROTOCOL.md` §2:

> a formalization is *evidence*, not a status. A green build is a run (command + log + SHA) and
> therefore caps at NUMERICAL under `DAG_PROTOCOL.md` §2; it licenses a completion tier only
> through the normal rule-6/rule-7 review gate, and it can never raise a node above what its own
> imported hypotheses allow.

### What a green build here does NOT establish

1. **It does not prove that `Q`, `P`, `Qone`, `Pone` are the capacities of `Λ_x`.**  They are
   four opaque `ℝ → ℝ` fields of `WHGAP.CapacityInterface`.  **Amended 2026-08-01 (LEAN-3
   WP-D):** there *is* now a channel layer — `WHGAP/Support/Channel.lean` builds the Kraus
   set `K₀ = t·1`, `K_{μ+1} = s·A_μ`, the Kraus sum, the padded complement
   `(Λ^c(X))_{ab} = Tr(K_a X K_bᵀ)`, the forced-point lift and its HS adjoint, and the defect
   superoperator, and it proves the two identification theorems named in item 11 below.  What
   is still **absent** is everything that would make it a *channel* in the
   information-theoretic sense: complete positivity, the Stinespring dilation, the theorem
   that `LamCK` is *the* complementary channel, coherent information as a channel functional,
   and any blocklength or coding theorem.  (Since
   2026-07-31 there *is* an entropy — `WHGAP.Support.vnEntropy` — and the two Holevo quantities
   of the §7 witness ensemble are computed from explicit matrices; but they are attached to
   matrices posited by hand, not to any channel, and none of it touches `Q`, `P`, `Qone`,
   `Pone`.)  Every statement about the four capacity fields is conditional on the interface.
2. **It does not prove the WHGAP goal.**  `WHGAP.goal.composition` takes
   `«onset-two-fifths».Claim I S` as a hypothesis, and that node is **CONJECTURED** on disk.
   The goal is OPEN for exactly that reason, and the Lean type shows it.
3. **It does not prove `P(Λ_x) > 0` below `1/2`** (the P14 theorem).  Proved outright: the
   closed-form scalar `Δ(x)` is strictly positive on `(0, 1/2)`; the two Holevo arguments
   coincide at `ε = t = ε_c(x)/2`; and — **new, LEAN-2 WP-C 2026-07-31** — paper Lemma 7.1
   itself, i.e. `χ(E,B) = b f(u/b)`, `χ(E,E) = e f(v/e)` and `Δ(x) = χ(E,B) - χ(E,E)`, with
   both `χ`'s *computed* as `S(avg) - ½S(out₊) - ½S(out₋)` from the explicit output matrices
   by the T3 entropy layer.  **The trust boundary of P14 is correspondingly smaller.**
   **Amended 2026-08-01 (LEAN-3 WP-D, correction R13 m1):** the identification step — that
   the explicit matrices `outB`/`outE` really are `Λ_x(ρ_ε ± tX)` and `Λ^c_x(ρ_ε ± tX)` — is
   **no longer outside Lean**; it is `«private-boundary».outB_eq`/`outE_eq`, proved entrywise
   against the Kraus-built channel of `WHGAP/Support/Channel.lean` (residual (c) of
   `Trust.lean`, CLOSED — see item 10 below).  The exact-sympy gate G1 of
   `tools/whgap_lean2_wpc_check.py` is now a cross-check, not the evidence of record.  What
   remains outside Lean, and is exactly the hypothesis `hdev` of
   `«private-boundary».Claim_of_devetak`, is (i) Devetak's formula
   `P^{(1)} = max_ensembles [χ(·,B) - χ(·,E)]`, the cited external interface, and (ii) the
   **validity of the ensemble** it is applied to: that `ρ_ε ± tX` are states (PSD, trace one)
   and satisfy `eq:ens`'s `|t| ≤ √2 ε`.  Positivity of the inputs is checked nowhere here
   (`outB_trace`/`outE_trace` check trace-one of the two *averages* only) and `|t| ≤ √2 ε` is
   nowhere represented; both are manuscript obligations.  The older, strictly stronger
   hypothesis `hbridge` of `«private-boundary».Claim_of_delta_le` is retained as the general
   bridge.
4. **It does not check the signed-lift construction.**  `SignedLiftCP` is an opaque predicate.
   The 27×27 covariant ansatz, its uniqueness, and the exact rational certificates are invisible
   here; only the *displayed* forcing identities and eigenvalue sign conditions are checked.
5. **It does not check the BKM order.**  `cBKM` in `«order-boundary»` is an abstract predicate
   parameter; the necessity theorem enters as the hypothesis `hFails`.
6. **The entropy layer is not a quantum-information library.**  `vnEntropy hA` is a number
   attached to a symmetric matrix through `Real.negMulLog`; it presupposes no positivity and
   no normalization, so for a non-state it has no information-theoretic reading.  Only
   `outB_trace`/`outE_trace` (trace one for the two averages) tie the payoff matrices to
   states at all, and the eigenvalue POSITIVITY that would make `vnEntropy` an entropy in the
   usual sense is nowhere required — the collapse theorems are algebraic identities valid
   under only the non-degeneracy conditions `b, b±u ≠ 0` (resp. `e, e±v ≠ 0`).
   **Extended 2026-08-01 (LEAN-5 WP-H):** the same sentence applies verbatim to
   `Support.vnEntropyC` over `ℂ` — it is `∑ negMulLog λᵢ` of the Hermitian eigenvalue
   enumeration, with no positivity, no normalization and no state structure assumed.  That
   the §6 witness `ρ_ε` happens to be a state is checked only to the extent of
   `Channel.rhoWit_trace` (trace one); PSD-ness of `ρ_ε` is nowhere represented.
7. **It does not validate the cited external results.**  `lsd_devetak`, `zw_hrsf_zero` and
   `q_pos_of_ic_pos` are assumptions with citations, not theorems.  If one of them is wrong, the
   build is unaffected.
8. **The `x = 1` self-complementarity module proves the DISPLAY, not the capacity claim.**
   (LEAN-3 WP-F, 2026-08-01.)  `WHGAP/Support/SelfComplement.lean` machine-checks the
   entrywise identity of paper Lemma 4.1 — `½ Tr(A_μ X A_νᵀ) = (Λ₁(X))_{μν}` for the minimal
   three-dimensional Kraus set `A_μ/√2` — and nothing else.  The Lemma's payoff
   (`P(Λ₁) = Q(Λ₁) = 0` via Theorem `thm:zw`) remains the cited Zhu–Wang interface; complete
   positivity, minimality of the Stinespring representation and the very notion of
   complementary channel are still absent here.
9. **The characteristic polynomial is proved, the *identification* still is not.**
   (LEAN-3 WP-E, 2026-08-01.)  `WHGAP.DefectChoi.charpoly_Cmat` machine-checks the paper's
   `eq:charpoly` — `det(z·1 − C_x) = z¹⁹(z − λ₅)⁵(z − λ₃)³` — **for every real `x`, with no
   side condition**, superseding the earlier `annihilator + Cmat_symm + multiplicity_unique`
   route (which needed an unformalized diagonalizability step and excluded
   `x ∈ {1/3, 1/2, 5/6}`).  What that does **not** do is identify `Cmat x` with the defect
   Choi matrix of the residual family: residual (a) of `Trust.lean` is untouched, so this is
   a theorem about the Appendix A display, not yet about the channel construction.  The
   `SO(3)` spin-reduction narrative of the paper's proof (the pencil identity `eq:pencil`,
   the Gram factors `4/25` and `1/3`) is still **not** formalized — the Lean proof reaches
   the same polynomial by an unrelated road (a rank-8 Weinstein–Aronszajn reduction), so a
   defect in that narrative would not be caught here.  *(Scope note, 2026-08-01: "residual (a)
   is untouched" describes what **`charpoly_Cmat` alone** does; residual (a) itself was closed
   later the same day by WP-D — item 10 below.)*  Note also that a characteristic polynomial
   does **not** determine a rank; the paper's `rank C_{1/2} = 3` is a separate theorem,
   `WHGAP.DefectChoi.rank_Cmat_half`, added 2026-08-01 (LEAN-3.2, R13 MAJOR-2) and proved from
   the factorization `A₃ = V₃V₃ᵀ` with `V₃ᵀV₃ = 16·1₃` — it is **not** an inference from
   `charpoly_half`.
10. **The identification layer is closed for (a) and (c), not for (b).**  (LEAN-3 WP-D,
   2026-08-01.)  `WHGAP.Support.Channel.choi_defect_eq_Cmat` proves that `DefectChoi.Cmat x`
   **is** the Choi matrix of the residual-family defect `Δ_J(τ)(Y) = Λ(τ)Y − J†(Λ^c(τ)J(Y))`
   at the forced point (all 729 entries, every `x`, `q` on the chart `9xq² = 2(1−x)`), and
   `«private-boundary».outB_eq`/`outE_eq` prove that `outB`/`outE` **are** `Λ_x(ρ_ε ± θX)` and
   `Λ^c_x(ρ_ε ± θX)`.  Residuals (a) and (c) of `Trust.lean` are therefore CLOSED.
   **Amended 2026-08-01 (LEAN-4 WP-G): residual (b) is now CLOSED AT CHARPOLY LEVEL, and
   only there.**  This item previously read "*Residual (b) is not [closed]*: the §6 witness
   outputs are complex Hermitian, and `charpoly Λ(ρ_ε) = ∏(X − specBᵢ)`,
   `charpoly Λ^c(ρ_ε) = ∏(X − specEᵢ)` remain exact-sympy results only
   (`tools/whgap_lean3_wpd_check.py`, gates D9a–D9e) — they were not reached in Lean."
   They are reached now: `WHGAP/Support/Channel.lean` §8 builds `ρ_ε` over `ℂ` from
   `ψ = (e₁ + i e₂)/√2` and proves `Channel.specB_charpoly`, `Channel.specE_charpoly`
   (the latter square-root free, with the `λ±` pair kept as a quadratic factor), their
   `IcScalar`-list forms and their Kraus-level corollaries.
   **Amended again 2026-08-01 (LEAN-5 WP-H): residual (b) is DISCHARGED.**  This item
   previously read "*What remains is named explicitly and is not small: 'same
   characteristic polynomial ⟹ same `vnEntropy`' is NOT in Lean for complex Hermitian
   matrices … nothing here yet turns the two charpolys into `S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))`*".
   `WHGAP/Support/EntropyC.lean` now supplies exactly that glue over `ℂ`, and
   `Support.IcScalar_eq_vnEntropyC_diff` proves
   `IcScalar x ε = vnEntropyC (Λ_x(ρ_ε)) − vnEntropyC (Λ^c_x(ρ_ε))` on `0 ≤ x ≤ 1` for any
   `β` with `β² = x(1−x)/2`.  **What remains after the discharge, named exactly:** the
   achievability hypothesis is still there, now available in the entropy-level form
   `hach'` of `«no-ascent-hierarchy».Claim_of_entropy_witness`, and what it carries is
   **(i)** the Stinespring identification — that `LamCK` is *the* complementary channel of
   `Lam` (no complete positivity and no dilation theory exist here) — and **(ii)** LSD/
   Devetak achievability.  Both are interface-tier (item 7).  `hach'` is *equivalent* to
   the older `hach`, not weaker (`«no-ascent-hierarchy».entropy_witness_eq_IcScalar` proves
   the two quantities equal); the gain is that the charpoly→entropy identification is a
   Lean theorem instead of an exact-sympy gate.
   Note also what closing (a)/(c) does **not** buy: no complete positivity, no
   Zhu–Wang certificate, and **the coding-theorem interfaces remain entirely outside this
   development** — `lsd_devetak`, `zw_hrsf_zero`, `q_pos_of_ic_pos` are still assumptions
   (item 7).  **Corrected 2026-08-01 (R13 m6):** this item previously bracketed `hach` with
   "the §4 entropy assembly".  It is two different things.  `hach` is the **achievability
   reading of the §6 `IcScalar`** — that the number computed from the explicit §6 output
   spectra is an achievable coherent information of `Λ_x` (P9 ⟹ P3); it is the missing
   channel/entropy reading of `IcScalar`, not a §4 statement.  The paper's **§4 assembly**
   sits inside the `zw_hrsf_zero` interface (P4) and is covered by item 7.

11. **It is not an independent review.**  Per `DAG_PROTOCOL.md` rules 6–7 and §7.10 this
   development must itself be reviewed by a fresh instance before any completion-tier status
   cites it.  Its own cap is **NUMERICAL, `pending-review:`**.

### What it does mean

The *shape* of the DAG is machine-checked: the import graph equals the propagating skeleton, the
three tier-1 child Claims really do compose to the goal set equality with no extra premise, and
every scalar identity listed below — the P14 coincidence and closed form, the P6
threshold, the P2 forcing identities, the P9 weight sign and Lemma 6.1 block invariants — is
exactly true as written, at a level of rigour no numerical run can give.  (Displayed scalar
content that is **not** checked anywhere here includes the pencil identity `eq:pencil` and
the Gram factors
`4/25` and `1/3`; Appendix A's entrywise table entered `WHGAP/Support/DefectChoi.lean` as a
*definition*, so its transcription is a sympy gate, not a Lean theorem.  `eq:charpoly`,
listed here as unchecked until 2026-08-01, **is now proved** —
`WHGAP.DefectChoi.charpoly_Cmat`, unconditionally in `x`.  The `lem:holevo`
collapse, listed here as unchecked until 2026-07-30, **is now proved** —
`«private-boundary».chiB_collapse`/`chiE_collapse`/`Delta_eq_chi_diff`.  **Both parenthetical
caveats that used to stand here — "the identification of that display with the defect Choi
matrix of the residual family remains outside Lean" and "the identification of `outB`/`outE`
with the channel outputs remains outside Lean" — were removed on 2026-08-01 (R13 m1): LEAN-3
WP-D closed both, by `Support.Channel.choi_defect_eq_Cmat` and by
`«private-boundary».outB_eq`/`outE_eq` respectively (item 10 above).**  Residual (b), the §6
complex `specB`/`specE` identification, was closed later the same day by LEAN-4 WP-G at
characteristic-polynomial granularity, and the complex-Hermitian entropy glue that carries
it to `IcScalar` landed the same day with LEAN-5 WP-H
(`WHGAP/Support/EntropyC.lean`, `Support.IcScalar_eq_vnEntropyC_diff`), see item 10.)  Two real
defects would be caught by this
development that prose review has historically missed: a *false* displayed identity (would fail
to compile) and a *missing* premise in a composition (would fail to close the goal).

## Layout (DAG protocol §7.3)

    WHGAP/Interface.lean                 -- the trust boundary; no invented proofs
    WHGAP/Support/Basic.lean             -- shared scalar definitions
    WHGAP/Support/Entropy.lean           -- T3: vnEntropy of real symmetric matrices
    WHGAP/Support/EntropyC.lean          -- LEAN-5 WP-H: vnEntropyC over C; residual (b) glue
    WHGAP/Support/DefectChoi.lean        -- LEAN-2 WP-A: the 27x27 defect Choi core
    WHGAP/Support/IcScalar.lean          -- LEAN-2 WP-B: the scalar coherent information
    WHGAP/Support/SelfComplement.lean    -- LEAN-3 WP-F: paper Lemma 4.1 (x = 1) entrywise
    WHGAP/Support/Channel.lean           -- LEAN-3 WP-D: Kraus set, complement, lift, defect
                                         --   + LEAN-4 WP-G §8: the §6 witness spectra over C
    WHGAP/signed-lift-extension.lean     -- node WHGAP.signed-lift-extension  (P2)
    WHGAP/order-boundary.lean            -- node WHGAP.order-boundary         (P6)
    WHGAP/private-boundary.lean          -- node WHGAP.private-boundary       (P14, flagship)
    WHGAP/no-ascent-hierarchy.lean       -- node WHGAP.no-ascent-hierarchy    (P9)
    WHGAP/qpositive-onset.lean           -- node WHGAP.qpositive-onset        (P3)
    WHGAP/zero-capacity-application.lean -- node WHGAP.zero-capacity-application (P4)
    WHGAP/onset-two-fifths.lean          -- node WHGAP.onset-two-fifths       (P13, stated only)
    WHGAP/goal.lean                      -- node WHGAP.goal                   (G)
    WHGAP/SelfTest.lean                  -- rational checks of the definitions
    WHGAP/Trust.lean                     -- sorry census + #print axioms
    WHGAP/Model.lean                     -- in-tree satisfiability witness (§7.10.5)

`WHGAP/Support/Basic.lean` contains the shared scalar definitions `b`, `e`, `u`, `v`, `epsC`,
`dOne`, `f`, `sStar`, `Delta`, the denominator non-vanishing lemmas (`two_sub_three_x_pos/ne`,
`one_sub_x_pos/ne`, `one_sub_two_x_pos`, `two_sub_x_three_ne`, `epsC_mul_denom`) and
`sqrt_two_spec` (`0 < √2 ∧ (√2)² = 2`, the only bridge between the `r`-parameterized identities
and the two concrete `Real.sqrt 2` definitions).

Module name = node id exactly, using Lean's `«guillemet»` identifiers for the hyphenated ids;
the file path uses the raw name.  Import graph (= the propagating DAG skeleton):

    goal  ->  qpositive-onset  ->  no-ascent-hierarchy
          ->  zero-capacity-application  ->  signed-lift-extension
          ->  onset-two-fifths
    order-boundary  ->  signed-lift-extension        (root-level companion theorem)

## Building

Toolchain `leanprover/lean4:v4.31.0`, Mathlib pinned to tag `v4.31.0`.  `.lake/packages` is a
junction to the machine-local prebuilt cache shared with `research/se/lean` and
`research/ksum/lean` — do not re-download or rebuild Mathlib.  `.lake/` is never committed.

    cd channel-capacity/werner-holevo-gap/proof-dag/lean
    lake build

Build evidence for the run of 2026-07-30: `artifacts/logs_whgap_lean_20260730/`
(command + exit status + full transcript + `#print axioms` output + `SHA256SUMS.txt`).
Report: `artifacts/whgap_lean_t1t2_20260730.md`.

Most recent build evidence (LEAN-4 WP-G): `artifacts/logs_whgap_lean4_20260801/`, log
prefix `wpg_`.  Report: `artifacts/whgap_lean4_20260801.md`.  Preceding evidence (LEAN-3 and
the 2026-08-01 LEAN-3.2 repair of the R13 review's source-side findings):
`artifacts/logs_whgap_lean3_20260801/`, log prefixes `wpf_`, `wpe_`, `wpd_` (LEAN-3), `r13_`
(the independent review) and `r32_` (LEAN-3.2).  Report:
`artifacts/whgap_lean3_20260801.md`.  Review of record:
`artifacts/whgap_r13_lean3_review_20260801.md`.

## Frozen Claims

Every node module's docstring carries the **verbatim** `## Claim` section of its node file and
the SHA-256 of that text (LF bytes, leading/trailing blank lines stripped).  Those two things
are written by `tools/whgap_lean_freeze_claims.py`; run it with `--check` to detect drift after
any node-file edit.  If a Claim changes, the prose, the Lean statement, the hash, the node
metadata and the synchronized views must all change in the same session (§7.6).

## `sorry`

There is none, anywhere.  Every unclosed obligation is an explicit hypothesis parameter and is
listed in `WHGAP/Trust.lean`.

