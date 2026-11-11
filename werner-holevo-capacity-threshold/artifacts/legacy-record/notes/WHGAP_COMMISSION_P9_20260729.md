# WHGAP commission P9 — necessary-condition scans: no-ascent hierarchy (E1) + one-way Choi distillation (E2) (2026-07-29)

**STATUS: DISPATCHED 2026-07-29 (P6 completed; codex slot free).**

**Nodes (rule 8a):** primary `WHGAP.no-ascent-hierarchy` (E1); secondary
`WHGAP.choi-distillation-necessary` (E2). Both may receive AT MOST `NUMERICAL` +
`pending-review:` (E2 node) — `WHGAP.no-ascent-hierarchy`'s CONJECTURED status is
decision-layer-owned: append Work-record/Evidence lines only, do not change its status
field. Parent `WHGAP.goal` untouched.
**Executor:** codex CLI, ONE sequential session, workspace-write, NO network.
**Python:** `"C:<home>/cpython3119/python.exe"`.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.no-ascent-hierarchy`,
ROLE = executor. PRE-ACTION REPORT before any work; disk overrides on conflict.

## Frozen conventions

- Family, Kraus, complement: the WHGAP standard. Entropies/logs NATURAL unless a bits
  conversion is stated. x_1 = 0.390910232076... (P3). Strip = (x_1, 1/2).
- **Pure-input structure (verify exactly first):** for a pure qutrit psi (take real psi and
  generic complex psi), spec Λ_x(psi) = {x/2, x/2, 1-x} and
  spec Λ_x^c(psi) = {1-x, x/2, x/2, 0} — B-side full rank, E-side one-dimensional kernel.
- **The claimed first-order necessary condition (from the node; treat as a CLAIM to verify,
  not truth):** Q = 0 forces, for every pure psi and every state phi with
  supp Λ^c(phi) ⊆ supp Λ^c(psi):
  `Tr[Λ^c(phi) log Λ^c(psi)] ≤ Tr[Λ(phi) log Λ(psi)]`   (N1)
  with the n-copy analog on (Λ^{⊗n}, (Λ^c)^{⊗n}) and entangled pure psi_n.
- Distillation reduction (cite, do not re-prove): D_→(omega_x) ≤ Q(Λ_x) via one channel use +
  one-way LOCC; hashing: D_→(rho) ≥ -S(A|B)_rho; local filtering maps rho to
  (F_A⊗F_B) rho (F_A⊗F_B)† / p with success probability p, and one-way rates multiply by p.

## E1 — no-ascent hierarchy (node `WHGAP.no-ascent-hierarchy`)

- D1 (derivation check, exact): verify the pure-output spectra claims symbolically; verify
  the epsilon-expansion bookkeeping NUMERICALLY at high precision: for random (psi, phi)
  kernel-avoiding pairs at x = 9/20, fit Ic((1-eps)psi + eps phi) against
  c1*eps + O(eps^2 log eps) and confirm the fitted c1 matches
  `-Tr[Λ(phi-psi) log Λ(psi)] + Tr[Λ^c(phi-psi) log Λ^c(psi)]` to >= 8 digits; also confirm
  kernel-HITTING phi produce the -eps log(1/eps) plunge. GATE G0.
- S1 (n = 1 layer, strip scan): at x in {2/5, 21/50, 11/25, 23/50, 12/25, 49/100} and the
  calibration points {77/200 (< x_1: violation MUST exist — cross-check against P3),
  11/20 (> 1/2: must hold)}: maximize
  `A_1(psi, phi) = Tr[Λ^c(phi) log Λ^c(psi)] - Tr[Λ(phi) log Λ(psi)]`
  over pure psi and kernel-avoiding states phi (parameterize phi on the 3-dim support
  constraint; >= 150 restarts). A_1 > 0 anywhere = first-order ascent = Q^{(1)} > 0 nearby —
  must be consistent with P3 (violations only below/near x_1). Record max A_1 per x.
- S2 (n = 2 layer — the new territory): on two copies, psi_2 entangled pure (Schmidt-rank 2
  and 3 families + random), phi_2 constrained to supp (Λ^c)^{⊗2}(psi_2) (derive the support
  projector exactly per psi_2 — the E-side kernel is now psi_2-dependent and richer);
  maximize A_2(psi_2, phi_2) analogously (>= 200 restarts per x; x in
  {21/50, 11/25, 23/50, 12/25, 49/100}). **Pre-registered interpretations (G2-E1):**
  (a) A_2 > 1e-8 with clean convergence at some strip x -> MAJOR-positive: rationalize,
  interval-certify (this implies Ic > 0 on two copies near pure ⇒ Q > 0 at that x — a
  strip-resolving finding; certify with the same rigor as P3's witness);
  (b) all A_2 at the numerical floor (<= 0 + 1e-9) -> bounded-null: "no first-order
  two-copy ascent found; hierarchy consistent with Q = 0 in the strip";
  (c) mixed -> per-point report.

## E2 — one-way distillation attack on the Choi (node `WHGAP.choi-distillation-necessary`)

- D2 (calibration): hashing on omega_x directly = Ic(pi) — must go positive exactly below
  x_1 (cross-check); at x in [1/2, 11/20] every attack below MUST fail (Q = 0 proved).
- S3 (filtered hashing scan): local filters F_A, F_B in small parameterized families
  (diagonal rank-<=3 filters + O(3)-adapted projectors + >= 100 random low-rank filters),
  compute the one-way filtered-hashing rate p * max(0, -S(A|B)) on the filtered state at
  x in {21/50, 11/25, 23/50, 12/25, 49/100}; also try two-copy filtered hashing on
  omega_x^{⊗2} with correlated filters (budget-capped). **Pre-registered (G2-E2):** any
  certified positive one-way rate in the strip -> MAJOR-positive (Q > 0 there);
  all floors -> bounded-null with the searched-family inventory listed.

## Artifact and closeout

1. Artifact `artifacts/whgap_p9_necessary_20260729.md`: derivation-check results, S1/S2
   tables (x, max ascent, argmax character, certified?), S3 filter-scan tables, the
   pre-registered interpretations, runtimes. Scripts `tools/whgap_p9_*.py`; logs + JSON +
   SHA256SUMS.txt under `artifacts/logs_whgap_p9_20260729/`.
2. Node closeouts: `WHGAP.choi-distillation-necessary` -> at most NUMERICAL +
   `pending-review:`; `WHGAP.no-ascent-hierarchy` -> Work record/Evidence appends only;
   sync NODE_INDEX prose, mermaid, outline, "Most recent change".
3. Both validators exit 0 with the pinned interpreter.
4. Print `FINAL: DONE` or `FINAL: FAILED — <reasons>`.

**Budget box:** <= 90 min compute; 20-min single-step rule; S2 and the two-copy part of S3
each hard-capped at 30 min. Two info-free cycles -> STOP and report.

