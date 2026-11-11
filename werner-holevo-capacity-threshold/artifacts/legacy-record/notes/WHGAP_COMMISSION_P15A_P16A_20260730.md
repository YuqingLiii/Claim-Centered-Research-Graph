# WHGAP commission P15-A / P16-A — the two surviving restricted-order candidates
Frozen 2026-07-30. Nodes (rule 8a): Track A = `WHGAP.pure-anchor-order` (P15, obligation 1);
Track B = `WHGAP.direction-restricted-order` (P16, design question 1). Two independent
executors, each followed by its own fresh reviewer (R9 for A, R10 for B).

Interpreter `C:<home>/cpython3119/python.exe`; scripts `tools/whgap_p15a_*.py`,
`tools/whgap_p16a_*.py`, `tools/whgap_r9_*.py`, `tools/whgap_r10_*.py`; logs
`artifacts/logs_whgap_p15a_20260730/` and `.../logs_whgap_p16a_20260730/` (per-role
`SHA256SUMS_*.txt`, LF).

**Mandatory first step:** `research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = your track's node, ROLE as assigned.

**Inherited frozen material:** §1–§3 of
[WHGAP_REVIEW_COMMISSION_R5_20260729.md](WHGAP_REVIEW_COMMISSION_R5_20260729.md) plus the
P13/P12 tooling additions (radical-free charts; Berkowitz/Newton charpolys; never
`nsimplify` on exact rationals; `Symbol('x')` needs a reality assumption; **ambient
rationalization is VOID on a positive-codimension set — use chart-aware rationalization**).
Single-writer deviation binding (no node/index/DAG edits).

**Reviewed inputs you may rely on (7d):** P2/P4; P3 + R5d (**Q > 0 PROVED on (0, 2/5)**);
R5b necessity package; R5c/R6 (P13 weight operator, stratum exhaustion); R7 (n = 2 exact
package); R8 (private boundary PROVED; purity knob PROVED; the pure-ensemble identity
χ_B − χ_E = I_c(ρ̄); R8's first-order law
G((1−s)P_χ + sφ) = s(w_E − w_B)(χ,φ) + o(s)).

**Definition (frozen for both tracks).** For a pure state ψ and any state σ,
  G(ψ, σ) := D( Λ^c(P_ψ) ‖ Λ^c(σ) ) − D( Λ(P_ψ) ‖ Λ(σ) ).
P_b2 ("pure-anchor order") is the statement G(ψ, σ) ≥ 0 for all pure ψ and all σ.

---

# TRACK A — P15-A: is P_b2 strictly stronger than Q^{(1)} = 0?

Deliverable: `channel-capacity/werner-holevo-gap/notes/WHGAP_P15A_STRICTNESS_20260730.md`.

**Decision-layer conjecture (INPUT, NOT TRUTH — derive or refute it yourself; refuting it
is a first-class outcome).** For every state σ and EVERY pure decomposition
σ = Σ_u p_u P_{ψ_u},
  **Σ_u p_u G(ψ_u, σ) = − I_c(σ, Λ)**,
so the average of G over a pure decomposition is decomposition-INDEPENDENT. If true:
(i) P_b2 ⟹ Q^{(1)} = 0 is immediate (each term ≥ 0 ⟹ average ≥ 0 ⟹ I_c ≤ 0); (ii) the
converse fails in general, because Q^{(1)} = 0 forces only the AVERAGE to be ≥ 0 — a single
negative term may be compensated by the others. Strictness is then decided by an explicit
example rather than by a general theorem.

**A1 (the identity).** State and prove it, or refute it. Derive from the frozen
pure-ensemble identity or from scratch; verify symbolically where possible and at ≥ 3
(σ, decomposition) instances with DIFFERENT decompositions of the SAME σ (the
decomposition-independence is the sharp part). Report the exact support/faithfulness
hypotheses it needs.

**A2 (the x = 2/5 test — the decisive computation).** Recover the R8 violating pair
(ψ*, σ*) at x = 2/5 from `artifacts/logs_whgap_r8_20260730/r8_b2probe.json` (or find your
own violation with your own optimizer — preferred, then compare). Then:
 1. verify the violation independently at ≥ 50 digits and check it is NOT a support
    artifact (report min spec Λ(σ*), min spec Λ^c(σ*));
 2. check whether ψ* ∈ range(σ*);
 3. **compute I_c(σ*, Λ_{2/5}) to ≥ 40 digits**, and locally maximize I_c over states near
    σ* (≥ 100 restarts).
**Pre-registered gates:**
 - **G-A+ (a new Q witness):** if any rank-unambiguous state τ near σ* has I_c(τ) > 10^{-8}
   at x = 2/5 — or at any x ≥ 2/5 — then Q^{(1)}(Λ_x) > 0 there. Rationalize CHART-AWARELY,
   re-verify exactly/at 80 digits, and REPORT IMMEDIATELY. This would refute the
   candidate-onset conjecture `WHGAP.onset-two-fifths` and extend the PROVED Q > 0 region.
 - **G-A0 (strictness demonstrated):** if instead I_c(σ*) ≤ 0 while G(ψ*, σ*) < 0, then at
   x = 2/5 the pair (ψ*, σ*) demonstrates P_b2 ⊋ {Q^{(1)} = 0} — state exactly what this
   licenses and what it does NOT (it is a statement at one x, about one pair).
 - **G-Acal (hard calibration, run FIRST):** at x = 11/20 (where P = Q = 0 is PROVED)
   your G-computation must find NO violation over ≥ 300 (ψ, σ) samples, and your
   I_c-computation must return ≤ 0 everywhere. A violation there means your code is wrong:
   stop and diagnose.

**A3 (general strictness).** Either prove P_b2 ⊋ {Q^{(1)} = 0} for a general channel (a
construction or a clean argument from A1), or state honestly that only pointwise
demonstrations are available. Do NOT overstate: R8's MAJOR 3 was raised precisely because
this was asserted without proof.

**A4 (strip viability).** Given A1–A3, restate what the bounded searches at x = 9/20 and
49/100 mean for P_b2 as a candidate Q = 0 mechanism. Use R8's first-order law: the
first-order layer of a P_b2 violation is the P13 weight operator, which is PROVED ≤ 0 on
the strip — so any strip violation must be NON-PERTURBATIVE; search accordingly (≥ 200
restarts per point at x ∈ {2/5, 41/100, 9/20, 49/100}, with the rank discipline of P13-B:
accept a kernel dimension only when the spectral gap exceeds 10^6 × the zero-cluster).
Report inf G honestly (R8 m1: the previous "positive minima" were optimizer stalls toward
the degenerate corner σ → P_ψ, where G → 0⁺).

**Budget ≤ 90 min.** Cap NUMERICAL/CONJECTURED with `pending-review:` for R9.

---

# TRACK B — P16-A: is a direction-restricted order even usable?

Deliverable: `channel-capacity/werner-holevo-gap/notes/WHGAP_P16A_DIRECTION_20260730.md`.

The idea under test (registered on the node): restrict the order so that it EXCLUDES the
spin-2 perturbation directions in which the necessity witness breaks cBKM, while RETAINING
the pairs the coherent-information proof consumes. R8 MAJOR 1 established that the existing
no-go does not reach this class; nothing else is known.

**Decision-layer prediction (INPUT, NOT TRUTH — refuting it is a first-class outcome):**
the class dies at B2, because the purification pairs generically HAVE spin-2 content, so
excluding spin-2 excludes exactly what the proof needs.

**B1 (make it a definition).** Write down at least two precise candidate definitions of a
direction-restricted domination (e.g. (i) RE domination only for pairs (ρ,σ) whose
difference has zero spin-2 component in the A-sector; (ii) BKM domination only in
non-spin-2 tangent directions at each base point). For each, state whether it is a
statement about state PAIRS or about a cone field of directions, and what its complete
(reference-assisted) version would mean.

**B2 (consistency test — cheap and decisive).** For each definition, decide whether the
pairs the coherent-information step consumes — (ψ_{RA}, ψ_R ⊗ ρ_A), and their n-copy
versions — lie inside the restricted class. Concretely: decompose
ψ_{RA} − ψ_R ⊗ ρ_A under the O(3) action on the A factor and compute the spin-2 isotypic
component for ≥ 20 random purifications and ≥ 3 structured ones (isotropic ψ, real ψ,
maximally entangled). If the spin-2 component is generically nonzero, the class CANNOT
imply Q = 0 and the definition is DEAD — record it with that reason.

**B3 (stability, only if B2 leaves survivors).** Test whether the restriction survives
(i) attaching an arbitrary reference and (ii) tensoring: in the isotypic decomposition of
the two-copy space, does "no spin-2" on each factor imply "no spin-2" on the tensor? Give
the explicit obstruction or the explicit stability statement.

**B4 (verdict).** Either: DEAD with the reason (and then note that the P12 no-go becomes
exhaustive for the classes considered so far), or: a precise surviving formulation plus
what a feasibility probe would need.

**Budget ≤ 60 min.** Cap NUMERICAL/CONJECTURED with `pending-review:` for R10.

---

# Reviews R9 (Track A) and R10 (Track B)

Fresh instances, full rule-7. Re-derive the identity A1 by an own route; re-verify the
x = 2/5 datum with your own optimizer and your own I_c code; audit every gate verdict; for
Track B, redo the spin-2 decomposition independently (own isotypic projectors). Licensing
menus:
- R9-(A): "the decomposition identity is PROVED; the x = 2/5 verdict [G-A+ or G-A0] is
  licensed at the stated scope; A3's strictness claim is licensed exactly as stated."
- R10-(A): "the B2 verdict is licensed; the direction-restricted class is DEAD for the
  definitions considered / survives in the stated form."
- (B) FINDINGS in both cases.
Reports: `artifacts/whgap_r9_review_20260730.md`, `artifacts/whgap_r10_review_20260730.md`.

