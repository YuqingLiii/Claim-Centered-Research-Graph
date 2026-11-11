# WHGAP commission P12-A — the private-capacity boundary and the restricted-order no-go
Frozen 2026-07-30. Node (rule 8a): `WHGAP.restricted-order` (P12); cross-nodes
`WHGAP.order-boundary` (P6), `WHGAP.more-capable-route` (P8), `WHGAP.order-converse` (P11).

Executor: one fresh Opus instance. Paired review R8: a second fresh instance, dispatched
after the executor note lands. Interpreter `C:<home>/cpython3119/python.exe`;
scripts `tools/whgap_p12a_*.py` / `tools/whgap_r8_*.py`; logs
`artifacts/logs_whgap_p12a_20260730/` (per-role `SHA256SUMS_*.txt`, LF).

**Mandatory first step:** `research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.restricted-order`, ROLE as
assigned; PRE-ACTION REPORT at the top of your note/report.

**Inherited frozen material:** §1–§3 of
[WHGAP_REVIEW_COMMISSION_R5_20260729.md](WHGAP_REVIEW_COMMISSION_R5_20260729.md)
(conventions, standing failure modes, rule-7 embeds) + the P13-A/P13-B tooling additions
(radical-free rational charts; Berkowitz/Newton charpolys; **never** `nsimplify` on exact
rationals; `Symbol('x')` needs a reality assumption for Hermiticity gates; **ambient
rationalization is VOID as a verification step on a positive-codimension set — use
chart-aware rationalization**). Single-writer deviation binding (no node/index/DAG edits).

**Reviewed inputs you may rely on (7d):** paper §5 necessity package incl.
ε_c(x) = 2(1−2x)/(2−3x) (R5b LICENSE A); P2/P4 (P = Q = 0 on [1/2,1]); P3+R5d
(Q > 0 on (0, 2/5)); P13-A (R6). Everything else carries only its node status.

**Design input (decision-layer authorship, NOT frozen, NOT to be trusted):**
[WHGAP_DESIGN_MEMO_P12_20260730.md](WHGAP_DESIGN_MEMO_P12_20260730.md). Treat every
claim in it as a CONJECTURE to be independently derived or refuted. Refuting it is a
first-class outcome: report it, do not repair it silently.

## Deliverable

`channel-capacity/werner-holevo-gap/notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md` —
a rigorous, self-contained proof note, plus scripts/logs. Cap: authorship licenses
nothing; end at NUMERICAL/CONJECTURED with `pending-review:` for R8.

## Stage S0 — literature check FIRST (bounded, ≤ 25 min)

Local library `channel-capacity/literature/` first (catalog + papers), then a targeted
external search only if the local copies are silent:
1. Is "less noisy ⟺ relative-entropy domination for all pairs" stated in HRSF22 (local
   PDF), Watanabe 2012, or elsewhere? Record the exact statement + reference, or record
   that you must prove it yourself.
2. Do RK24 / RK25 / ZW state ANY private-capacity result for the noisy Werner–Holevo
   family (bounds, positivity, thresholds)? This decides whether S1's theorem is new.
3. HHHO 2008 (local: `hhho-2008-secure-key-bound-entanglement`) for the P > 0 = Q
   phenomenon — one paragraph of context only.
Record findings in the note's §1; do not let them alter the gates.

## Stage S1 — the private-capacity theorem (the main prize)

**S1a (the order equivalence).** State and PROVE (or refute): for channels M, N with a
common input, N ⪰_less-noisy M ⟺ D(N(ρ)‖N(σ)) ≥ D(M(ρ)‖M(σ)) for all states ρ, σ with
supp ρ ⊆ supp σ. The ⟸ direction is immediate; for ⟹ use the two-point ensemble
{p, ρ; 1−p, σ} and the p → 0⁺ limit — make the limit rigorous (continuity of D in the
second argument at a faithful point; the O(p²) second term). If it fails, say exactly
where and fall back to S1b, which does not need it.

**S1b (the explicit ensemble — the theorem's core, INDEPENDENT of S1a).** For the
symmetric two-point ensemble E(ε,t) = {½ : ρ_ε + tX, ½ : ρ_ε − tX} with the frozen
witness pair (ρ_ε, X) of paper §5:
1. prove both states are valid for |t| ≤ √2 ε;
2. prove the commutation and derive the EXACT closed forms
   χ_B = b·f(u/b), χ_E = e·f(v/e), with f(s) = (1+s)log(1+s) + (1−s)log(1−s),
   b = x/2 + (1−3x/2)ε, u = t(1−3x/2)/√2, e = (x/2)(1−ε), v = tx/(2√2)
   — derive these yourself from the frozen conventions (the memo's values are conjectural);
3. prove Δ(x,ε,t) := χ_B − χ_E > 0 for explicit rational (ε,t) at every x ∈ (0,1/2),
   with an EXPLICIT threshold (e.g. via f(s) ≥ s² and f(s) ≤ s² + s⁴/(6(1−s²))), and give
   a closed-form admissible choice (ε(x), t(x));
4. conclude P^{(1)}(Λ_x) ≥ Δ > 0; then P(Λ_x) ≥ P^{(1)}(Λ_x) via superadditivity of
   P^{(1)} under tensor powers (prove the superadditivity step or cite it precisely);
5. conclude **{x : P(Λ_x) = 0} = [1/2, 1]** with P4 for the other side.

**S1c (exact certificates).** Exact rational (x, ε, t) certificates of Δ > 0 at
x ∈ {2/5, 21/50, 9/20, 12/25, 49/100, 499/1000} — positivity established rigorously
(rational series bound, or ≥ 60-digit directed interval arithmetic; state which).

**S1d (quantitative bonus, if cheap).** Numerically optimize Δ over (ε,t) at those x to
report a lower-bound curve for P(Λ_x); confirm it → 0 as x → 1/2⁻.

**Gates.**
- **G-cal (HARD, run before any strip claim):** at x ∈ {11/20, 3/5} — where P = 0 is
  PROVED — Δ(x,ε,t) ≤ 0 for every tested (ε,t) over a dense scan (≥ 500 pairs) AND, if
  feasible, symbolically. A positive value means your closed forms are wrong: STOP and
  diagnose before proceeding.
- **G-ind (independence):** verify the closed forms against a direct, independently coded
  numerical Holevo computation (build the ensemble, apply the channel/complement, compute
  von Neumann entropies) at ≥ 3 triples (x,ε,t), agreement ≥ 10 digits.
- **G-cont:** exhibit Δ_max(x) → 0 as x → 1/2⁻ (consistency with ε_c(x) → 0).

## Stage S2 — the purity-knob hierarchy

Prove (or refute), from the definitions:
1. for a PURE-state ensemble {p_u, ψ_u}, χ_B − χ_E = I_c(ρ̄, Λ) exactly (use isospectrality
   of the two outputs at pure inputs), hence sup over pure ensembles = Q^{(1)};
2. sup over all ensembles = P^{(1)} (Devetak's formula — cite precisely);
3. therefore the ensemble-class knob interpolates exactly between Q^{(1)} = 0
   (more capable) and P^{(1)} = 0 (less noisy).
Verify numerically at ≥ 2 strip x that a pure two-point ensemble gives χ_B − χ_E ≤ 0
while the S1b mixed ensemble gives > 0 — the two regimes must separate as predicted.

## Stage S3 — the restricted-order no-go map

For each candidate order class below, decide (i) does it imply P^{(1)} = 0? (ii) does it
contain the S1b witness ensembles? (iii) verdict = DEAD below 1/2 / survives:
- (a) less noisy / complete less noisy / cRE / cBKM / any signed-lift CP-defect
  certificate / criterion (W) / sandwiched-Rényi orders with α ≥ 1;
- (b) the P12 node's own "anchored less-noisy" (anchors σ = ψ_R ⊗ ρ_A, reference R
  allowed trivial) — check the trivial-R specialization;
- (c) marginal-matched purification pairs (σ = ψ_R ⊗ ρ_A with ρ_A = Tr_R ψ_RA) — show
  this equals more capable = Q^{(1)} = 0 for complement pairs (cite HRSF22 Prop 3.3 as a
  frozen literature input; verify the pure-input identity yourself);
- (d) any class containing states within trace distance δ of a pure state, for arbitrarily
  small δ > 0 — use that ρ_ε ± tX → |0⟩⟨0| as ε, t → 0 with ε < ε_c(x), and give the
  explicit δ(x) below which the class is dead.
Deliverable: a table + the honest statement of what survives. State explicitly whether
the memo's "P12 no-go" claim is established, weakened, or refuted, and what exactly the
surviving frontier is.

**Scoping honesty (binding):** nothing in this commission may claim anything about Q on
[2/5, 1/2). If S1 succeeds, the correct reading is "P > 0 there; Q unknown; if Q = 0 the
family exhibits P > 0 = Q".

**Budget:** ≤ 100 min compute. Document resistance append-only; do not force. Return
{status: DONE|BLOCKED, outcome: THEOREM|PARTIAL|REFUTED, summary, note_path,
p_boundary_verdict}.

## R8 — paired fresh review (after the note lands)

Full rule-7 review: re-derive the closed forms by an OWN route (own Kraus/complement
assembly, own entropy computation — do NOT start from the executor's f-form); re-verify
S1a's limit argument and S1b's explicit threshold line by line; reproduce G-cal and G-ind
with your own script at ≥ 2 points each; audit the superadditivity citation; audit S2/S3
for over-claim (especially any leakage of a Q-statement on the strip, and the exact scope
of the no-go). Licensing menu:
- (A) "P^{(1)}(Λ_x) > 0 for every x ∈ (0,1/2) and hence P(Λ_x) > 0 — PROVED; with P4,
  {x : P(Λ_x) = 0} = [1/2,1] exactly — PROVED. The purity-knob hierarchy (S2) is PROVED.
  The S3 no-go map holds at the stated scope."
- (B) FINDINGS (itemized MAJOR/minor).
Report `artifacts/whgap_r8_review_20260730.md`.

