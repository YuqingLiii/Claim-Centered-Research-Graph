---
id: "WHGAP.zero-capacity-application"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.zero-capacity-application.md"
aliases: ["P4"]
kind: AND
role: proof
status: PROVED
status_source: "artifacts/whgap_p4_review_20260728.md (R3 licensing statement 1, PROVED tier) applied by the decision layer 2026-07-28; proof note channel-capacity/werner-holevo-gap/notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md (post-R3 revision); edge-normalized 2026-07-30 (kind LEAF -> AND, child P2) with the composition block below"
disposition: null
parents: ["WHGAP.goal"]
children: ["WHGAP.signed-lift-extension"]
related: ["WHGAP.order-boundary", "WHGAP.private-boundary"]
---

# WHGAP.zero-capacity-application — Q = P = 0 on [1/2, 1) via the extended lift family

## Claim

For every x in [1/2, 1), Q(Lambda_x) = P(Lambda_x) = 0 — assembled from the R2-PROVED covariant
lift family (defect-PSD on [1/2,1), unique residual point) through the generic Zhu–Wang
machinery (Theorem 3.3, Lemma 3.2, Corollary 3.7) and HRSF22 hybrid tensorization, explicitly
discharging the seven obligations enumerated in R2 review claim 9. **[PROVED — R3 licensing
statement 1; provenance note: HRSF22 tensorization verified through the local Zhu–Wang
statement, no local HRSF22 copy audited. The [1/2,1] Corollary sits at CERTIFIED\* (RK24
endpoint cite-only); the (1/2,4/7) gap-closure substatement is inside the PROVED scope.]**

## Role in DAG

Capstone application node registered 2026-07-28 when the R2 review split the P2 claim: the
certificate core went to PROVED scope while the capacity conclusion required this separate
write-up. Closing this node (with review) closes the original gap x in (1/2, 4/7) of WHGAP.goal
— and more: the whole [1/2, 1). **Edge-normalized 2026-07-30:** kind LEAF → AND with child
[[WHGAP.signed-lift-extension]] — the assembly note has always been exactly this node's
composition proof; the protocol update merely names it as such.

## Composition proof

```yaml
composition:
  claim: >
    (P2, R2-PROVED-scope subclaim) the covariant signed-lift family J_x intertwines,
    is unique in the ansatz, and has completely positive defect exactly on [1/2, 1);
    together with the cited external interfaces
    [ZW Thm 3.3 + Lem 3.2 + Cor 3.7 (signed-lift criterion)],
    [BGSW25 (cBKM -> cRE bridge)], [HRSF22 Lem 3.1 via the local ZW statement
    (hybrid tensorization)], and [Llo97/Dev05 (regularization)],
    imply Q(Lambda_x) = P(Lambda_x) = 0 for every x in [1/2, 1) at every blocklength.
  proof: "channel-capacity/werner-holevo-gap/notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md (post-R3 revision); full written form: paper/main.tex section 4"
  review: "artifacts/whgap_p4_review_20260728.md (R3, licensing statement 1)"
  status: PROVED
  rel:
    - "consumes ONLY the R2-PROVED-scope subclaim of P2 (feasible region + uniqueness +
       certificates), not P2's node-level CERTIFIED* (whose star reflects the delegated
       capacity clause = this very node, and the ansatz-scope caveat, which is displayed)"
    - "HRSF22 tensorization verified through the local ZW statement (provenance note)"
    - "the [1/2,1] closed-interval Corollary adds the RK24 cite-only endpoint and sits at
       CERTIFIED*; alternatively paper Lemma 4.1 (self-complementarity at x=1) at
       written-proof/external-review tier"
```

Status arithmetic: status(P4) = min(status(composition) = PROVED [R3], scoped-input tier
of P2's consumed subclaim = PROVED [R2 statement]) = **PROVED**, with the two relative
notes displayed above. The naive node-level min(P2 = CERTIFIED\*) does NOT apply because
the star on P2 marks exactly the clause that THIS node discharges plus an ansatz-scope
caveat that the composition claim quotes; per §1 the unresolved-hypothesis display rule is
satisfied by the rel list.

## Current status

PROVED (single fresh-session R3 review; decision layer applied its licensing verbatim).
**Theorem:** P^(1)(Lambda_x^{⊗n}) = Q^(1)(Lambda_x^{⊗n}) = 0 for every x in [1/2, 1) and every
n >= 1, hence Q(Lambda_x) = P(Lambda_x) = 0 on [1/2, 1) — R3 claims 1/4/5/7/8/9 PASS, claims
2/3/6 MINOR (wording/attribution; fixed in the note's post-R3 revision, no mathematical change).
Provenance note carried with the status: the HRSF22 tensorization input is verified through the
local Zhu–Wang statement (no local HRSF22 copy audited). **Corollary at CERTIFIED\*:**
{x : Q(Lambda_x)=0} ⊇ [1/2, 1], with the x=1 endpoint resting on cite-only RK24. R3 states
explicitly that the (1/2, 4/7) gap-closure substatement lies within the PROVED Theorem scope
with no RK24 dependency — **the original open question of WHGAP.goal is closed.**

## Dependencies

- [`WHGAP.signed-lift-extension`](WHGAP.signed-lift-extension.md) (CERTIFIED\*; certificate core
  PROVED-licensed by R2) — supplies J_x and the CP defect on [1/2, 1).
- Zhu–Wang arXiv:2607.24693 (local PDF): Theorem 3.3, Lemma 3.2, Corollary 3.1/3.7, Theorem 4.3
  proof pattern — generic theorems, cited not re-proved.
- HRSF22 (Hirche–Rouzé–Stilck França, Quantum 6:862): hybrid tensorization Lemma 3.1 — cited via
  the Zhu–Wang statement; no independent local copy yet (flagged by R2 as an untested regime).

## Seven obligations to discharge (R2 review claim 9, verbatim scope)

1. Kraus family CPTP for every x in [1/2, 1); the displayed complement is its chosen complement.
2. N^{⊗n} is a complement of M^{⊗n} up to the standard environment isometry.
3. Complete-relative-entropy quantifier covers all finite references and admissible support pairs.
4. Private-information step: zero-probability ensemble terms discarded; supp rho_u ⊆ supp rho-bar.
5. Coherent-information step: purification support inclusion used in Corollary 3.1 holds.
6. Tensorization orientation (Lambda_x^c)^{⊗n} ⪰_cRE Lambda_x^{⊗n}, then one-shot optimizations
   and regularizations.
7. x = 1 excluded because N(1) is not faithful there.

## Work record

- 2026-07-28 — node registered (rule 8a/8b) at R2-outcome application time; write-up not yet
  produced. See the R2 licensing statement 4 for why this is a separate obligation:
  [whgap_p2_review_20260728.md](../../../../artifacts/whgap_p2_review_20260728.md).
- 2026-07-28 — decision-layer write-up authored:
  [WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md](../../notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md)
  — Theorem + Corollary, (H1)-(H3) hypothesis check from R2-PROVED facts (F1)-(F4), obligations
  (O1)-(O7) discharged (Stinespring construction for O1/O2; support-inclusion arguments for
  O4/O5; tensorization orientation O6; endpoint exclusion O7). Status raised OPEN -> CONJECTURED
  (proposer tier) with pending-review. R3 review commission to follow.
- 2026-07-28 — R3 review commission authored by the decision layer (fresh-session reviewer,
  7a–7g embedded and adapted to a prose-proof review: pre-reading outline frozen to disk before
  opening the note, PDF statement-level cross-checks required, R2-license scope enforcement,
  orientation-drift named as the top failure mode):
  [WHGAP_REVIEW_COMMISSION_R3_20260728.md](../../notes/WHGAP_REVIEW_COMMISSION_R3_20260728.md).
  pypdf 6.14.2 installed into the pinned interpreter for the PDF cross-checks. Dispatched to a
  fresh codex reviewer session.

## Evidence

- 2026-07-28 — proposer write-up (unreviewed):
  [theorem note](../../notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md).

## Adversarial reviews

- 2026-07-28 — EXTERNAL cross-vendor hostile-referee review (ChatGPT Pro, via lead): Claim 5
  (the assembly) **PASS** — "no support, orientation, tensorization, or tensor-complement gap";
  plus the x=1 strengthening: the padded 4-dim complement's faithfulness failure is a
  representation artifact — the minimal 3-dim complement gives Λ_{1,min}^c = Λ_1
  (self-complementary), J = id, zero defect, so Q(Λ_1)=P(Λ_1)=0 by the SAME theorem and the
  result extends to the CLOSED interval [1/2,1] without RK24. Decision-layer machine
  verification: all items CONFIRMED. Archive:
  [whgap_external_review_chatgpt_20260728.md](../../../../artifacts/whgap_external_review_chatgpt_20260728.md).
- 2026-07-28 — decision-layer audit pass (Fable 5, lead-commissioned; SELF-audit for this node
  since the note is decision-layer-authored — opens no gate, recorded as evidence only):
  [whgap_fable_audit_20260728.md](../../../../artifacts/whgap_fable_audit_20260728.md) —
  re-derived the assembly identities (I(R;B)−I(R;E) = 2·Ic on pure tripartite states;
  admissibility inclusions; orientation), audited Zhu–Wang Theorem 3.3's own proof (Lemmas
  3.5/3.6 sound via the variational characterization of A^{-1}), and machine-verified the
  (F1)-(F4) inputs plus the max-mixed Ic ≈ 0.39 crossing consistency check.
- 2026-07-28 — fresh independent R3 rule-7 review completed:
  [whgap_p4_review_20260728.md](../../../../artifacts/whgap_p4_review_20260728.md).
  Claims 1, 4, 5, 7, 8, and 9 PASS; claims 2, 3, and 6 MINOR (F4's exact R2 license wording,
  real- versus complex-linearity wording, and the O5 reference-state attribution). The review
  opens the Theorem completion gate at PROVED scope on `[1/2,1)` and the full `[1/2,1]`
  Corollary gate at CERTIFIED* scope with a cite-only RK24 endpoint caveat. **No status applied
  by the reviewer.**

## Open obligations

Completion gate satisfied. Optional upgrades only: (1) ~~audit a local HRSF22 copy~~ —
PARTIALLY DISCHARGED 2026-07-29: HRSF22 fetched into the field library
(`channel-capacity/literature/papers/hirche-rouze-stilckfranca-2022-contraction-partial-orders/`)
and Lemma 3.1 (complete less-noisy tensorizes) verified at STATEMENT level against the use
made here; the proof remains cited, not re-derived — the provenance note weakens from
"no local copy" to "statement-checked, proof cited"; (2) locally verify RK24's x >= 4/7
antidegradability to lift the Corollary from CERTIFIED\* to PROVED at the x = 1 endpoint.
Neither blocks the gap-closure result.

## Status history

- 2026-07-28 — created OPEN (decision-layer registration following the R2 licensing split).
- 2026-07-28 — OPEN -> CONJECTURED (proposer tier; pending-review): full assembly write-up on
  disk. Cite: `channel-capacity/werner-holevo-gap/notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md`.
- 2026-07-28 — CONJECTURED -> PROVED (decision layer applying the completed fresh-session R3
  review's licensing statement 1 verbatim; pending-review marker removed; three MINORs fixed in
  the note's dated post-R3 revision). Corollary scope recorded at CERTIFIED\* (RK24 endpoint
  cite-only). Cite: `artifacts/whgap_p4_review_20260728.md` and
  `artifacts/logs_whgap_p4_review_20260728/SHA256SUMS.txt`.

## Lean

```yaml
lean:
  module: "WHGAP.«zero-capacity-application»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/zero-capacity-application.lean"
  claim: "Claim"
  composition: "composition"
  state: "composition-checked"
  tier: "T1"
  rel: []
  build: "artifacts/logs_whgap_lean_20260730/"
  claim_hash: "sha256:8be43283510eb60ce3f617da0df2fec2832c5b8e4f6f6b5a6ce52bd5973326da"
  synced: "2026-07-30"
```

Mechanization notes (LEAN-1, 2026-07-30, NUMERICAL `pending-review:` — the §7.10
statement-fidelity review is the completion gate): composition (P2 ⟹ P4) checked; blocklength quantifier lives inside the cited zw_hrsf_zero interface field (composition_one_shot records the one-shot half); closed interval deliberately not stated.
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

