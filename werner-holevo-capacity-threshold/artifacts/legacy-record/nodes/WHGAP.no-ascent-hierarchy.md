---
id: "WHGAP.no-ascent-hierarchy"
node_file: "channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.no-ascent-hierarchy.md"
aliases: ["P9"]
kind: LEAF
role: proof
status: CERTIFIED*
status_source: "R5c + R5d reviews 2026-07-29 (artifacts/whgap_r5c_review_20260729.md, whgap_r5d_review_20260729.md, both LICENSE A) applied by the decision layer 2026-07-30: the n=1 isotropic layer (N1'-a closed form, expansion lemma, Q>0 on (0,2/5)) is PROVED; the full hierarchy (n>=2, non-isotropic strata, balanced layer) stays CONJECTURED"
disposition: null
parents: ["WHGAP.qpositive-onset"]
children: []
related: ["WHGAP.goal", "WHGAP.order-boundary", "WHGAP.choi-distillation-necessary"]
---

# WHGAP.no-ascent-hierarchy — Necessary conditions for Q = 0 from first-order no-ascent at the pure manifold

## Claim

**(No-ascent hierarchy, necessity):** If Q(N) = 0 then, for every blocklength n, every pure
input psi on A^n, and every state phi on A^n with
supp (N^c)^{⊗n}(phi) ⊆ supp (N^c)^{⊗n}(psi),
\[ Tr[(N^c)^{⊗n}(phi) · log (N^c)^{⊗n}(psi)] ≤ Tr[N^{⊗n}(phi) · log N^{⊗n}(psi)] . \]
(The n = 1 instance for our family: for every pure qutrit psi and every kernel-avoiding phi,
Tr[Λ^c(phi) log Λ^c(psi)] ≤ Tr[Λ(phi) log Λ(psi)].) **[CERTIFIED\* — the repaired n = 1
isotropic layer is PROVED after two completed fresh-instance reviews (R5c: closed form +
orbit transport; R5d: expansion lemma + Theorem Q > 0 on (0, 2/5)); the general hierarchy
(n ≥ 2, non-isotropic strata, balanced layer N1'-b) remains CONJECTURED.]**

## Role in DAG

Decision-layer answer opener to the lead's 2026-07-29 question "find NECESSARY conditions"
(everything so far — signed lift, criterion W — is sufficient-side). Derivation sketch
(in-context): pure inputs have isospectral receiver/environment outputs, so Ic vanishes
identically on the pure manifold, which is therefore a critical level set at the global
maximum whenever Q^{(1)} = 0; Q = 0 forces Ic(ρ_ε) ≤ 0 for ρ_ε = (1−ε)ψ + εφ at every
blocklength. Directions whose E-side output hits ker (N^c)^{⊗n}(psi) give S(E) a
+ε log(1/ε) gain (Ic plummets — non-binding); on kernel-avoiding directions both entropies
are differentiable and the linear coefficient is
c₁ = −Tr[Λφ log Λψ] + Tr[Λ^cφ log Λ^cψ] (using S(Λψ) = S(Λ^cψ)); Q = 0 ⟹ c₁ ≤ 0, which is
the displayed inequality. For our family Λψ is full rank while Λ^cψ has a one-dimensional
kernel (spectra {x/2, x/2, 1−x} and {1−x, x/2, x/2, 0} for real ψ), so the support condition
is one linear constraint on phi per psi. The n ≥ 2 layers use entangled pure ψ_n and the
tensor/mixed kernel structure of (Λ^c)^{⊗n} — they probe exactly the superactivation
directions and are cheap spectral computations. VALUE: an ascent violation at some n in the
strip (x_1, 1/2) would PROVE Q > 0 there; the hierarchy holding is structured evidence for
Q = 0 and a target for an eventual matching sufficiency proof.

## Current status

CONJECTURED unchanged after P9-E1. The pre-registered G0 gate failed before S1/S2:
the fixed spectrum is false for generic complex pure inputs, and four generic
support tests left only \(\phi=\psi\). The kernel-hitting entropy plunge passed.
`pending-review:` this executor finding has not received an independent rule-7
review. The pre-run obligations below are retained as history.

CONJECTURED (proposer = decision layer; pending-review). Needs: (i) a written derivation
with the ε log ε bookkeeping made rigorous (Fréchet differentiability of entropy on the
support, uniformity of the kernel-avoidance condition); (ii) verification that at n = 1 the
condition is equivalent to the KKT first-order content of Q^{(1)} = 0 at pure maximizers
(sanity: it must HOLD on the strip where Q^{(1)} = 0 numerically); (iii) the n = 2
closed-form layer and its scan over the strip — commissioned as P9-E1 in
[WHGAP_COMMISSION_P9_20260729.md](../../notes/WHGAP_COMMISSION_P9_20260729.md) (queued
behind P6; codex sequential).

## Dependencies

P3 (strip picture; the near-pure optimal inputs are exactly the boundary objects of this
hierarchy); P4 (Q = 0 on [1/2,1] — the hierarchy must hold there, a calibration regime).

## Work record

- 2026-07-29 — P9-E1 stopped at the pre-registered G0 gate. Exact evaluation at
  \(x=9/20\) confirms the frozen spectra for real \(\psi\), but the generic complex input
  \((1,i,1)/\sqrt3\) has receiver spectrum
  \(\{9/40,(31-3\sqrt{97})/80,(31+3\sqrt{97})/80\}\), not
  \(\{9/40,9/40,11/20\}\). Four random generic pure inputs also left a
  one-dimensional allowed input support under
  \(\operatorname{supp}\Lambda^c(\phi)\subseteq\operatorname{supp}\Lambda^c(\psi)\);
  hence the only allowed state was \(\phi=\psi\), so the commissioned distinct
  kernel-avoiding epsilon fits and the S1/S2 optimizations could not be formed. The
  kernel-hitting \(-\epsilon\log(1/\epsilon)\) plunge passed. Status remains
  CONJECTURED as commissioned; this is an unreviewed executor finding.

- 2026-07-29 — node registered (rule 8b) with the derivation sketch above; commission P9
  authored the same day (queued).

## Evidence

- 2026-07-29 — P9-E1 G0 FAIL:
  [P9 execution artifact](../../../../artifacts/whgap_p9_necessary_20260729.md),
  [machine JSON](../../../../artifacts/logs_whgap_p9_20260729/g0_derivation_check.json),
  [raw log](../../../../artifacts/logs_whgap_p9_20260729/g0_derivation_check.log), and
  [script](../../../../tools/whgap_p9_g0.py). Script SHA-256
  `f1939dca5f0efb027603f89995529eb78169143fcde801b4a0d14acffa575d7d`;
  JSON SHA-256
  `a8b4398048ae7b3e52d86915652a76e833d73df82cefbf11d2b00dbb1a7f7c55`.
  `pending-review:` the fixed-spectrum and nontrivial-support failures require an
  independent rule-7 review before any completion-tier interpretation.

## Cross-reference (2026-07-30): the n = 1 first-order landscape is now COMPLETE

The P13-A stratum-exhaustion Theorem (PROVED, R6 review — recorded on
[[WHGAP.onset-two-fifths]]) settles the tau != 0 strata: for every pure psi with
tau(psi) > 0 and every phi != P_psi, w_E = (x/2)(1 - <psi|phi|psi>) > 0 strictly and the
leading coefficient is -w_E < 0 (exceptional set empty; kernel-avoiding set = {P_psi}).
Combined with the R5c closed form on the isotropic stratum, the ENTIRE n = 1 pure-base
first-order landscape is characterized: ascent exists exactly on the isotropic stratum
for x < 2/5.

## Adversarial reviews

- 2026-07-29 — **R5c (fresh Opus instance, rule-7 complete): LICENSE A — NO MAJOR, 6
  minors.** The isotropic weight-operator closed form is PROVED SYMBOLICALLY IN x by the
  reviewer's own route (w_B/w_E as linear functionals on a 9-element Hermitian basis; HS
  duality M_E = sum_ab (Pi_E)_ab K_a^T K_b derived, not read; three independent routes —
  conjugate-free (a,b)-parameterized sympy, 60-digit mpmath at 6 rational x incl. 9/20 and
  499/1000, and a projector-algebra hand proof D = (1-x-4k)P_psibar - k P_e3 with
  k = x(1-x)/(2-x), the d_2 = 0 cancellation from iA_2 = P_psibar - P_psi). Supersession
  adjudicated with an UNCONDITIONAL defect localization (below). The load-bearing orbit
  claim 4(iii) now has a PROOF: psi isotropic iff {sqrt2 u, sqrt2 v} is a real orthonormal
  pair, so O = [sqrt2 u, sqrt2 v, 2 u x v] ∈ SO(3) maps the canonical psi_0 to psi (SO(3)
  ALONE is transitive; no U(1) needed); covariance gives O^T K_i O = sum_j V_ij K_j with
  V = 1 ⊕ det(O)·O REAL ORTHOGONAL (det factor required on the det = -1 branch), hence
  Pi_E(O psi) = V Pi_E(psi) V^T and D_{O psi} = O D_psi O^T — verified symbolically on both
  det branches + numerically at 10 random isotropic psi to 1e-61. Report:
  [whgap_r5c_review_20260729.md](../../../../artifacts/whgap_r5c_review_20260729.md).
- 2026-07-29 — **R5d (fresh Opus instance, rule-7 complete): LICENSE A — NO MAJOR, 8
  minors.** Verdict verbatim: "the expansion Lemma is PROVED; the Theorem
  Q(Lambda_x) > 0 for all x in (0, 2/5) is PROVED" — and UNCONDITIONALLY: the Theorem
  imports nothing from R5c (the note derives w_B - w_E = (1-x)(2-5x)/(2-x) from the
  definitions in its own §7.3). Every inequality and remainder constant re-derived by hand
  (Weyl; Ostrowski congruence comparison, all four sign cases; the kernel-cluster bound
  with its Schur block-diagonalization and constant 40/9 <= 6; the mu-uniform eps-log-eps
  bookkeeping; C(x) arithmetic; Theorem 8.1's explicit threshold; Proposition 9.1). B-side
  diagonalization verified symbolically in an own basis order; sanity table reproduced at
  ALL FOUR x-values (21 entries, worst rel err 4.5e-10); crossover eps* = 1.775878e-8 at
  x = 0.395 independently computed. Falsification beyond the note's gates: Prop 3.3 at
  kernel multiplicities m = 1,2,3; Ostrowski on 20 random pairs; Lemma 5.1 uniformity over
  6 x-values x 5 random isotropic psi x 3 random phi x 4 eps incl. eps = x/8 exactly (360
  tests, no violation). Report:
  [whgap_r5d_review_20260729.md](../../../../artifacts/whgap_r5d_review_20260729.md).

## Post-review corrections (decision layer, 2026-07-30, applying R5c minors — append-only)

- **R5c m2 — the supersession rationale is now UNCONDITIONAL** (replacing the earlier
  conditional "impossible given the expansion lemma pattern" argument, which leaned on the
  then-unreviewed lemma): the superseded `tools/whgap_p6b_v2_isotropic.py` works at
  psi' = (0, 1, -i)/sqrt2 where u x v = -e_1 but passes third = +e_1 while asserting
  "third_is_u_cross_v": true, so its analytic kernel vector has the wrong sign and its
  Pi_E FAILS the defining property Pi_E Λ^c(P_psi) = 0 (its own gate
  annihilates_environment_output = false). R5c reproduced its published wrong diagonal
  exactly under that convention and restored diag(-99/620, -11/124, 0) by flipping only
  that sign. The defect is intrinsic to the superseded script; no appeal to any unreviewed
  result is needed.
- **R5c m3 — a VOID audit is ANNULLED:** the field
  `p9b_pi_e_audit.raw_sum_equals_true_projector = false` in
  `artifacts/logs_whgap_p6b_20260729/v2_isotropic.json` compares P9b's Pi_E against the
  DEFECTIVE projector of the same superseded script and is meaningless; its neighbouring
  field raw_basis_mutually_orthogonal = true already implies P9b's sum IS the orthogonal
  projector, and R5c's independent computation confirms P9b's diag(-99/620, -11/124, 0).
  No doubt about the P9b datum survives.
- **R5c m4 — scope of "the balanced layer is empty":** correct at x = 9/20 and, as a
  formula, on x ∈ (2/5, 1) only. At x = 2/5 exactly ker D = span{psi, psibar}; for
  x < 2/5, D is indefinite and the balanced set is a nontrivial face. Earlier bare
  statements on this node are to be read with this range.
- **R5c m5 — wording:** SO(3) alone is transitive on the isotropic stratum (drop
  "x U(1)"); the transport is ORTHOGONAL with environment index carried by
  V = 1 ⊕ det(O)·O (the det factor is required); P9b's "by continuity" chart hand-wave is
  replaced by R5c's constructive transitivity proof (report §3).

## Work record (continued)

- 2026-07-29 — repaired commission authored by the decision layer after the G0 failure:
  [WHGAP_COMMISSION_P9B_20260729.md](../../notes/WHGAP_COMMISSION_P9B_20260729.md) —
  parameterized-isotropic G0 gate, (N1-prime-a) scans with anchors, balanced layer, n=2
  isotropic layer. Dispatched.

## Decision-layer digestion of P9b — 2026-07-29 (late)

The G0' "failure" is a structural POSITIVE in disguise: the exact operator
D_psi(9/20) = diag(-99/620, -11/124, 0) <= 0 with kernel exactly span{psi} IS the
first-order no-ascent condition (N1'-a) HOLDING at x = 9/20 with an exact certificate —
what failed is only the decision layer's assumption that a nontrivial balanced layer
exists (it is empty: balance forces phi = P_psi). Reformulation **N1''**: by O(3)
transitivity on the isotropic orbit, the entire first-order landscape is ONE closed-form
3x3 operator inequality `D_psi(x) <= 0`; its x-threshold (where the largest eigenvalue
crosses 0) is an ANALYTIC necessary-condition curve, commissioned in P6b alongside the
lead's tau=1 BKM witness. Complementary-strata picture: cBKM necessity witnesses live at
tau = 1 (real stratum, spin-2 directions — the lead's rho_eps/X pair); single-letter
ascent structure lives at tau = 0 (isotropic stratum).

## P6b-V2 outcome — 2026-07-29 (night): the isotropic weight operator is now EXACT

The repaired-formulation weights admit a closed-form weight operator: at the isotropic
psi = (e1 + i e2)/sqrt2 (all isotropic psi equivalent under covariance, pending the orbit
write-up), D = M_B - M_E is exactly diagonal in (e3, psi-bar, psi) with
d_0 = -x(1-x)/(2-x) < 0, **d_1 = (1-x)(2-5x)/(2-x)**, d_2 = 0
(tools/whgap_p6b_v2_fable.py, all gates PASS; independent numeric arbitration at x = 9/20;
matches the earlier P9b datum diag(-99/620, -11/124, 0); the interrupted executor script
whose assembly disagreed is superseded, defect recorded append-only). Hence
max_phi (w_B - w_E) = max(d_1, 0): **the first-order isotropic ascent exists iff x < 2/5 —
candidate EXACT single-letter onset x_D = 2/5**, implying (pending review of the N1-prime
expansion lemma) Q > 0 on (0, 2/5) and a strip shrunk to [2/5, 1/2). Status stays
CONJECTURED; the expansion lemma + this closed form are the R-review package.

## Repaired formulation N1' — 2026-07-29 (decision layer, superseding the broken generic-psi N1)

The G0 failure localizes the conjecture to the right stratum. Stratify pure inputs by the
O(3)-invariant **isotropy parameter** `tau(psi) = |psi^T psi| in [0,1]` (real psi: tau = 1;
the broken claims were the tau = 1 case overgeneralized). On the **isotropic stratum
tau = 0** (psi-bar ⊥ psi):

- Output spectra (derivation: Lambda(P)|psi> = (1-x/2)|psi>, Lambda(P)|psi-bar> = 0,
  Lambda(P)|z> = (x/2)|z> for z ⊥ both): spec Lambda(P) = {1-x/2, x/2, 0} — rank 2 with
  ONE-dim kernel spanned by psi-bar; by isospectrality spec Lambda^c(P) = {1-x/2, x/2, 0, 0}
  — rank 2 with TWO-dim kernel K_E(psi). BOTH sides now have kernels, so the epsilon log
  epsilon terms can compete instead of the E-side always winning.
- For rho_eps = (1-eps)P + eps*phi with UNRESTRICTED phi, define the kernel weights
  `w_B(psi,phi) = <psi-bar| Lambda(phi) |psi-bar>` and
  `w_E(psi,phi) = Tr[Pi_E(psi) Lambda^c(phi)]` (Pi_E = projector onto K_E). Then
  `Ic(rho_eps) = (w_B - w_E) * eps*log(1/eps) + O(eps)`.
- **(N1'-a, sharp layer):** Q^{(1)} = 0 forces, for every isotropic pure psi and EVERY state
  phi: `w_B(psi,phi) <= w_E(psi,phi)` — a closed-form, genuinely nontrivial inequality
  family (any violation gives an infinite-slope ascent, hence Ic > 0 nearby, hence Q > 0).
- **(N1'-b, balanced layer):** on directions with w_B = w_E the leading term cancels and the
  eps-linear coefficient (support-block Frechet terms plus the kernel-block h(eps w) pieces)
  must be <= 0 — to be derived exactly in the renewed commission.
- n-copy layers: isotropic-entangled psi_n (tau computed with the global transpose), tensor
  kernel bookkeeping — the superactivation probes.
- **Consistency check that the repair is right:** P3's optimal near-pure witnesses have base
  vector v = (0, 1/sqrt2, -i/sqrt2)-type with v^T v = 0 — exactly the isotropic stratum, as
  N1' predicts; and its spectrum family (0, eps, 1-eps) matches the balanced-perturbation
  geometry.

## Open obligations

The n = 1 isotropic layer is CLOSED (lemma + closed form + reviews; Q > 0 export recorded
on [[WHGAP.qpositive-onset]]). Remaining for the full hierarchy claim: (a) optimality of
the isotropic stratum — non-isotropic psi (tau ≠ 0) for x ∈ [2/5, 1/2); (b) the balanced
layer (N1'-b) on x < 2/5 where the balanced set is a nontrivial face; (c) the n ≥ 2
entangled layers (superactivation directions); (d) the onset conjecture itself, now
registered separately per rule 8b on [[WHGAP.onset-two-fifths]] (E-N1 note §13 item 4 +
R5d request: 2/5 must never be read off the lemma note as an onset).

## Status history

- 2026-07-29 — created CONJECTURED (decision-layer derivation; pending-review).
- 2026-07-30 — CONJECTURED -> CERTIFIED\* (decision layer, applying the completed R5c +
  R5d reviews' licensing statements verbatim; pending-review markers on the P9/P9b/P6b-V2
  entries discharged). PROVED tier opened for: the isotropic weight-operator closed form
  (symbolic, with orbit transport), the eps-log-eps expansion Lemma 5.1 with explicit
  remainder, Corollary 5.3 (the (N1'-a) necessity layer), and Theorem 8.1
  (Q(Lambda_x) > 0 for all x in (0, 2/5), exported to WHGAP.qpositive-onset). The general
  hierarchy (n >= 2, tau ≠ 0 strata, balanced layer) remains CONJECTURED — tracked in
  Open obligations.

## Work record (continued — P9b)

- 2026-07-29 — P9b stopped at the pre-registered G0' repaired-derivation gate.
  The parameterized isotropic spectra, three random isotropic checks, the
  \(\tau\in\{1,1/2,0\}\) interpolation (including the prior P9 sample at
  \(\tau=1/3\)), and all five unbalanced epsilon fits passed. The required
  nontrivial balanced-pair construction failed exactly: at \(x=9/20\), in the
  basis \((e_0,\bar\psi,\psi)\), the weight operator
  \(D_\psi=M_B-M_E\) is
  \(\operatorname{diag}(-99/620,-11/124,0)\). Therefore
  \(w_B-w_E=\operatorname{Tr}(D_\psi\phi)=0\) forces
  \(\phi=|\psi\rangle\langle\psi|\); \(O(3)\) covariance transports this
  statement across the single isotropic orbit. Convex mixing reaches balance
  only at that trivial endpoint, so zero of the commissioned three distinct
  balanced pairs exist. Under pre-registered interpretation G2(c), S1'/S2'/S3' were not
  entered. This falsifies the decision layer's assumed nontrivial balanced layer
  at the \(x=9/20\) calibration point, not the repaired isotropic spectra or the
  leading unbalanced asymptotic. Status remains CONJECTURED and untouched.
  `pending-review:` this executor finding has not received an independent
  rule-7 review.

## Evidence (continued — P9b)

- 2026-07-29 — P9b G0' FAIL:
  [execution artifact](../../../../artifacts/whgap_p9b_noascent_20260729.md),
  [machine JSON](../../../../artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.json),
  [raw log](../../../../artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.log),
  and [script](../../../../tools/whgap_p9b_g0.py). Exact hashes are archived in
  [SHA256SUMS.txt](../../../../artifacts/logs_whgap_p9b_20260729/SHA256SUMS.txt).
  `pending-review:` no completion-tier interpretation is licensed.

## Evidence (continued — E-N1 lemma note + R5 batch, 2026-07-29/30)

- 2026-07-29 — **E-N1 (fresh Opus executor, commissioned in
  [WHGAP_REVIEW_COMMISSION_R5_20260729.md](../../notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md)):
  the written expansion-lemma proof note**
  [WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md](../../notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md)
  — self-contained: own degenerate-perturbation bound (Weyl + Ostrowski congruence
  comparison + kernel-cluster Proposition with explicit constant 40/9 <= 6), mu-uniform
  eps-log-eps bookkeeping, Lemma 5.1 |Ic(rho_eps) - (w_B - w_E) eps log(1/eps)| <= C(x) eps
  for 0 < eps <= x/8 with C(x) explicit and uniform in phi AND psi (proved pointwise on the
  stratum — the orbit claim is NOT a dependency), §7 exact B-side diagonalization
  diag((1-eps)(1-x/2), eps(1-x/2), x/2) and exact E-side 2x2 block split, §7.3 own
  definition-based derivation w_B = 1-x/2, w_E = 4x(1-x)/(2-x) + x/2, Theorem 8.1
  (Q > 0 on (0, 2/5) with explicit eps_1(x)), Proposition 9.1 (two-term expansion with
  crossover eps* = exp(c_1/d_1) — at x = 0.395 the sign only turns positive below
  eps ~ 1.8e-8, explaining why P3's numerics missed the ridge). Sanity: own
  `tools/whgap_n1p_sanity.py`, 75 gates ALL PASS; logs + SHA256SUMS_n1p.txt (LF) under
  `artifacts/logs_whgap_r5_20260729/`. Executor-honesty note: the commissioned sign
  pattern (+, +, -) at eps in {1e-3..1e-5} is WRONG at x = 0.395 (negative at all three;
  flips only below eps* ~ 1.8e-8) — a genuine finding, predicted by Prop 9.1.

## Lean

```yaml
lean:
  module: "WHGAP.«no-ascent-hierarchy»"
  file: "channel-capacity/werner-holevo-gap/proof-dag/lean/WHGAP/no-ascent-hierarchy.lean"
  claim: "Claim"
  composition: null  # leaf — NO composition theorem exists in this module
  state: "proved (core lemmas: d1_sign, d1_at_two_fifths, exists_pos_of_expansion, blockA_trace_det) + stated (Claim, a substituted tier-1 shadow)"
  tier: "T2 (core) / T1 (shadow Claim)"
  rel: ["hexp — retained ONLY for the general arbitrary-Ic lemma exists_pos_of_expansion; the §6 witness family no longer needs it (WP-B carries its own proof exists_eps_IcScalar_pos)", "hach (Claim_of_witness wiring): the achievability reading that IcScalar is an achievable coherent-information value — the entropy/channel identification layer, sympy-checked, outside Lean"]
  build: "artifacts/logs_whgap_lean3_20260801/"  # LEAN-3/3.2 batch; earlier evidence dirs retained
  claim_hash: "sha256:542edac65af8d29b3bf7a10c14298e587d9422dd87d80ccd24cad3ec65363d37"
  synced: "2026-08-01 (post LEAN-3.2, R13 m2)"
```

Mechanization notes (LEAN-1 + R11 corrections, 2026-07-30): the Lean Claim is a
SUBSTITUTED tier-1 shadow — the statement Theorem 8.1 of the N1' note produces and P3
consumes — NOT the node's frozen operator-inequality Claim (unrepresentable at this
tier); **no implication from the prose Claim is asserted** (R11 m2 wording adopted; the
earlier "via the contrapositive" justification was invalid and is withdrawn). PROVED
outright in Lean: d1_sign, d1_at_two_fifths, exists_pos_of_expansion, and — moved here
from the P14 module per **R11 MAJOR-1** — blockA_trace_det (the trace/det invariants of
paper Lemma 6.1's E-side block A(ε), an ingredient of THIS node's positivity layer; the
original filing under P14/"Lemma 7.1" was a misattribution). The initial metadata state
"composition-checked" was UNBACKED (no composition theorem exists in the module) —
corrected to proved+stated per R11 MAJOR-2; a decision-layer transcription of an
executor-report error, exactly the drift class the not-yet-implemented §7.6 checker
should catch.
Report: [whgap_lean_t1t2_20260730.md](../../../../artifacts/whgap_lean_t1t2_20260730.md)
(G-L5 fidelity self-table row for this node; granularity losses stated there).

