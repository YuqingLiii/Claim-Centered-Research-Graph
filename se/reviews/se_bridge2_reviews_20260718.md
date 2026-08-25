# Rule-6 review archive — Bridge II write-ups (Tasks B, C, D), 2026-07-17/18

**Reviewer:** a Fable 5 checker instance that authored none of the reviewed mathematics (all three
work products authored by codex gpt-5.6-sol under written commissions). Method: line-cite
spot-verification against primary sources + independent re-derivation of every load-bearing step.
This file is the completed-review artifact required by `DAG_PROTOCOL.md` §3 rule 6 for the
status writes listed below.

## Review 1 — `se/artifacts/se_bridge2_writeups_20260717.md` (L1 degree, L2 J_Y, L3 commutation)
**Verdict: PROVED, all three lemmas.**
- Mathematics re-derived by the reviewer: L1 weight additivity over disjoint leg groups + projector
  containments + the self-adjointness step for the coimage; L2's normalized-delta arithmetic (2.2)
  recomputed by hand (`⟨v_z, R_n u_x⟩ = √(q^n/(q)_n)·1{z=x}`); L3's equivariance + central
  character-sum averaging.
- All cited anchors verified verbatim on disk: BR:353-363 (e-basis, Π_0), BR:371-375 (exact-weight
  H^{(m)}_k), BR:326-333 (illegality), BR:353-354 ((μ,z) row identification), BR:653-657 (X̄
  definition), `se_legal_diamond_query_norm_audit.md:55-71` ((1.1)),
  `se_symbolic_k2_channels.md:147-154` (isotypic projector formula),
  `exact_band_descent_analysis.md:346-354` (defect convention).

## Review 2 — `se/artifacts/se_bridge2_md_inst_20260718.md` (matched-degree lemma at d=k)
**Verdict: PROVED (statement (1.3), equality at m=q, k=0 endpoint).**
- Source regions verified verbatim: `:7-15` (premise `j≥1`, `d=j+1` — confirms the k=0 endpoint gap
  the note found and separately closed); `:102-158` ((2.3)-(2.7) chain); `:162-237` ((3.1)-(3.8) —
  the source's own (3.8) is stated at matched degree d=j; only the boxed theorem is d=j+1);
  `:240-273` ((3.9)-(3.10) one-defect-only, unused; single full-position copy); `:295+` (BR
  one-defect application, unused).
- Equality construction §5 re-derived (Gram attaining vector `u = P_kR_q^*w/(√r‖w‖)`).

## Review 3 — `se/artifacts/se_bridge2_ytransfer_20260718.md` (Y-transfer)
**Verdict: ACCEPTED AS WRITTEN — the GAP FOUND verdict is CORRECT.** Component review:
- PROVED items confirmed: the A_{≤k} three-factor sandwich (3.4), middle contraction (3.5), NO-side
  commutation reuse, and the new **Sub-lemma 3.1** (YES-side commutation: diagonal S_q preserves
  injectivity; same averaging argument) — each re-derived by the reviewer.
- The gap analysis is genuine and material: (†) yields alphabet defect `j ≤ k` only; MD (matched
  degree) applies to blocks with degree = defect; on a weight-k, defect-j<k block the correct
  full-permutation scalar is the mismatched `r_k(λ)` of `se_bridge2_md_inst_20260718.md:168-175`,
  which is NOT `r_top`. The note's example `r_2((q)) = q/2` was recomputed by the reviewer from that
  formula: `C(q,2) − q(q−1) + q²/2 = q/2`. ✓
- **Knock-on found by the reviewer (recorded in the DAG header (8)):** the same `j<k` issue
  invalidates the earlier "X-line closes analytically" accounting (Stage-1 link 7 / verdict §4's
  `j≤k` envelope implicitly substitutes matched `r_top` per defect); the X-line also closes only
  modulo the pinning statement below.
- **Closure sketch (reviewer's own contribution — CONJECTURED, NOT self-promotable under rule 6;
  lives on DAG node `SE.denom.bridge2.pin` pending write-up + independent review):** the carrier's
  position types have exactly k boxes below the first row (barΠ' definition; across the two halves
  via the LR first-row inequality `τ_1 ≤ σ_1 + σ'_1`); completion to the full-permutation space adds
  a single-row (Pieri) strip, so the completed position type τ satisfies
  `below(τ) = q − τ_1 ≥ m − ρ_1 = k`; the legal-NO Peter–Weyl pairing forces alphabet λ = position
  τ, hence alphabet defect ≥ k; with (†)'s ≤ k this pins defect = k on the legal restriction, which
  is exactly the note's missing (4.5); S_q-equivariance of Ȳ transports the pinning to the YES side.
  Note this rehabilitates the "LR first-row" fact that `se_leakage_lemma_verdict.md` §4 had declared
  dead code — it is load-bearing for the sandwich route, as Stage-1 HOLE 3(a) originally recorded.

## Review 4 — `se/artifacts/se_familysplit_20260718.md` (family-split declaration)
**Verdict: PROVED — `SE.denom.familysplit` discharged.** Component review by the Fable checker:
- The declaration `P_k := Π̄_{se,k}` + (1.4) = BR's own eqn:decomposition (BR:502-508, read verbatim);
  IDENT-1 derivation (incl. `Φ_0^{(n)} = 0` closing the ℓ=k term) re-derived; IDENT-2 immediate.
- The `Z̄_k ↦ −X̄_{k−1}` diamond check re-derived by the reviewer: both operators share the tail
  `S^μ_{k−1}`, the `e_0^*` partner slot and the block scale; domain projectors absorb idempotently;
  only the query leg differs (Π₁ vs Π₀), and `Δ₁∘Π₁ = −Δ₁∘Π₀` since `Δ₁∘I = 0`.
- Spot-checks against BR, all PASS: :202-225 (diamond definition, γ₂(Δ)≤2 factor-2 estimate,
  "always choose Δ⋄A = A", linearity — exactly as quoted); :338-340 (submatrix mechanism);
  :502-508, :526-532, :616-663, :665-676 (previously read verbatim by the reviewer).
- The note's numerical correction VERIFIED: `ybar_norms_fresh.log:58` gives IDENT1 = 3.373e-15 at
  (4,2) — the DAG's earlier "≤ 1.4e-15" relay was based on the (3,1)-(4,1) rows only; corrected.
- Honest scoping confirmed: Φ.legal and legal cross-k explicitly NOT claimed; Q1 shown not to be a
  premise (the declaration is projector algebra).

## Same-day reviews archived elsewhere
- Φ.ambient promotion: blind clean-room line-read, `se/artifacts/se_phi_blind_lineread_codex_20260717.md`
  (incl. BR:1307 / BR:914 errata, verified against the tex by the promoting checker).
- X̄/Ȳ ambient promotions: chains on the DAG nodes; underlying artifacts
  `se_phi_xbar_qfree_audit_20260717.md` (§6 blind checker) and `logs_se_py_reverify_20260717/`.
