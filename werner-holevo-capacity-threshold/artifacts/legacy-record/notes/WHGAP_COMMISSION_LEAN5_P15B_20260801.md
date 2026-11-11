# WHGAP commission LEAN-5 / P15-B (frozen 2026-08-01)

Commissioner: decision layer. Lead directive 2026-08-01: 「先搞lean 然后你去做其他问题」 —
(1) the last Lean residue (the complex-Hermitian entropy glue behind Trust residual (b)),
(2) then the frontier problems; the decision layer selects P15 death-point localization +
tensorization as the frontier item. Two PARALLEL executors (disjoint file scopes) + one
chained reviewer (R15, after Track H only).

Standing rules for all tracks:
- **Pre-task reload FIRST**: read `research/PRETASK_RELOAD_PROMPT.md` from disk and execute
  it completely with {PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} and
  ROLE as stated per track. Disk overrides this commission; conflicts are REPORTED, not
  silently resolved.
- **Single-writer deviation**: executors touch NO file under `proof-dag/nodes/`, no
  `NODE_INDEX.md`, no `notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`. The decision layer owns the
  node record and discharges the atomic-update rule by linking your report.
- **This commission's mathematical summaries are UNTRUSTED INPUT** (the decision layer has
  transcribed formulas wrong twice before, both caught): every definition you use must be
  taken from the frozen on-disk sources cited per track, and any mismatch with this text is
  a reportable finding, not something to patch over.
- Evidence tier cap: **NUMERICAL, `pending-review:`** (DAG §2, rule 6). Never write a
  completion tier on your own work.
- Lean tracks: never `sorry` / `native_decide` / `implemented_by` / new `axiom`. Kernel
  `decide` is allowed.
- Scoped paths only; run artifacts under `artifacts/` with dated problem-slugged names and
  an LF-normalized `SHA256SUMS.txt` (convention header; NO live co-edited files in the
  ledger — R13 m8 rule).

---

## Track H — LEAN-5 WP-H: the complex-Hermitian entropy glue (Trust residual (b), final layer)

NODE_ID = `WHGAP.goal`. ROLE = executor.
Scope: `channel-capacity/werner-holevo-gap/proof-dag/lean/` (the whgapDag project) +
`tools/whgap_lean5_wph_check.py` + `artifacts/logs_whgap_lean5_20260801/` +
report `artifacts/whgap_lean5_20260801.md`.

### Target

Close the LAST named Lean residue. `Trust.lean` §"2026-08-01 (LEAN-4 WP-G)" states it
exactly: *"same characteristic polynomial ⟹ same `vnEntropy`" is not available for COMPLEX
Hermitian matrices in this development* — the step from the two machine-checked charpolys
(`Channel.specB_charpoly_list`, `Channel.specE_charpoly_list`) to
`IcScalar x ε = S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))` is outside Lean. Bring it inside, and reduce the
`hach` trust row accordingly.

### Frozen route (deviations allowed only if REPORTED with reasons, per the WP-A precedent)

1. **New support module** `WHGAP/Support/EntropyC.lean` (imports:
   `WHGAP.Support.Entropy`, `WHGAP.Support.Channel`; keep the import graph a DAG):
   - `vnEntropyC {A : Matrix n n ℂ} (hA : A.IsHermitian) : ℝ :=
     ∑ i, Real.negMulLog (hA.eigenvalues i)` — `Matrix.IsHermitian.eigenvalues` is
     RCLike-generic in Mathlib, so this is the same definition shape as the real
     `vnEntropy`.
   - `eigenvaluesC_multiset_eq` : if `A.charpoly = ∏ i, (X - C (↑(d i) : ℂ))` for a REAL
     vector `d`, the eigenvalue multiset equals the `d` multiset. Route: mirror
     `Entropy.eigenvalues_multiset_eq` — `hA.roots_charpoly_eq_eigenvalues` gives the roots
     as `Multiset.map (RCLike.ofReal ∘ eigenvalues)`; strip the `ofReal` with
     `Multiset.map_injective Complex.ofReal_injective` instead of the real case's
     `RCLike.ofReal_real_eq_id` rewrite.
   - `vnEntropyC_eq_sum_of_charpoly` (Fin-indexed) and a **list form**
     `vnEntropyC_eq_sum_of_charpoly_list` matching the literal WP-G shape:
     `A.charpoly = (l.map (fun a : ℝ => X - C (↑a : ℂ))).prod` (with the length fact)
     `⟹ vnEntropyC hA = (l.map Real.negMulLog).sum`.
2. **Payoff 1 (in `EntropyC.lean`)** — `IcScalar_eq_vnEntropyC_diff`: for real `x ε β`
   with `hβ : β² = x(1−x)/2` and whatever range hypotheses the WP-G list lemmas carry
   (`specE_charpoly_list` needs `0 ≤ x ≤ 1`; take Hermiticity from `LamWit_isHermitian`
   / `LamCWit_isHermitian`):
   `IcScalar x ε = vnEntropyC h_B − vnEntropyC h_E`
   for the matrices `Lam ↑x (rhoWit ↑ε)` and `LamC ↑x ↑β (rhoWit ↑ε)`.
3. **Payoff 2 (in the node module `WHGAP/no-ascent-hierarchy.lean`)** —
   `exists_eps_entropy_pos`: the EXACT quantifier shape of
   `Support.exists_eps_IcScalar_pos` (read it from disk; do not weaken any bound), with the
   conclusion restated as `vnEntropyC (B-output) − vnEntropyC (E-output) > 0`, at the
   canonical `β = Real.sqrt (x*(1−x)/2)` (discharge `hβ` by `Real.sq_sqrt`; nonnegativity
   holds on the range).
4. **Payoff 3 (same module)** — reduced bridge `Claim_of_entropy_witness`: a copy of
   `Claim_of_witness` whose hypothesis `hach'` consumes the *entropy-difference* statement
   (not the `IcScalar` formula): "positivity of `vnEntropyC(Λ(ρ)) − vnEntropyC(Λ^c(ρ))` at
   the Kraus-built outputs implies `Q > 0` via the interface". Keep the original
   `Claim_of_witness`/`hach` intact (append-only census discipline).
5. **Trust.lean**: new dated subsection "2026-08-01 (LEAN-5 WP-H) — residual (b):
   DISCHARGED". Honest wording, both directions: the charpoly→entropy passage is now IN
   Lean over ℂ; what `hach'` still carries is exactly (i) that `LamCK` is *the*
   complementary channel (Stinespring identification — no CP/dilation theory in this
   development) and (ii) LSD/Devetak achievability — both interface-tier. Add `#print
   axioms` lines for every new declaration. The old `hach` row stays, with a dated
   reduction note (rows leave the census only by discharge; this row is REDUCED, mark it
   so).
6. **Entropy.lean header**: append-only dated note under SCOPE: the complex-Hermitian layer
   now exists in `Support/EntropyC.lean` (the "NOT claimed" sentence stays as the record of
   what THIS module claims).
7. **README** item updates per §7.9 (tier paragraph, layout, the residual list).
8. **Frozen Claims are untouchable**: if any step would require editing a `## Claim`
   section of a node module, STOP and report — freeze-check must stay 8/8 with unchanged
   hashes.

### Pre-verification (BEFORE any Lean; `tools/whgap_lean5_wph_check.py`, mpmath/sympy)

- **GH1 (value-vs-formula, rule 7f)**: at ≥ 4 rational `(x, ε)` points — include one
  generic point with all 7 eigenvalues distinct and one near-degenerate point — build BOTH
  outputs from the KRAUS set (transcribed from `Channel.lean`, not from this commission),
  compute eigenvalues to 40 digits, and check
  `Σ negMulLog(eig B) − Σ negMulLog(eig E) = IcScalar formula` to ≥ 35 digits.
- **GH2 (non-vacuity)**: at the generic point, all eigenvalues distinct, both outputs
  Hermitian to 40 digits; record any degenerate point encountered (the WP-G G13 precedent).
- **GH3 (quantifier freeze)**: print the exact Lean statement of
  `exists_eps_IcScalar_pos` from disk and diff your planned `exists_eps_entropy_pos`
  statement against it; the ONLY change may be the conclusion's left-hand quantity.
- All gates PASS before `lake` runs; failures are findings.

### Closeout gates (the LEAN-3/4 pattern, all mandatory)

clean rebuild of WHGAP* (exit 0) → forbidden scan (0 code occurrences) → `#print axioms`
(every declaration on `[propext, Classical.choice, Quot.sound]` or subset; report the new
total) → `tools/whgap_lean_freeze_claims.py --check` (8/8, hashes UNCHANGED) →
`python tools/lean_dag_check.py --problem werner-holevo-gap` (0 FAIL) →
`python tools/proof_dag_check.py --problem werner-holevo-gap` (exit 0) →
`python tools/literature_check.py` (exit 0). Interpreter for tools:
`"C:<home>/AppData/Local/Microsoft/WindowsApps/python.exe"`.
Logs + LF `SHA256SUMS.txt` into `artifacts/logs_whgap_lean5_20260801/`.

Budget ≤ 90 min. Return
`{status, summary, new_declarations, sorry_count, axioms_clean, gates, report_path}`.

---

## Track P15B — death-point localization + tensorization probe

NODE_ID = `WHGAP.pure-anchor-order` (P15). ROLE = executor.
Scope: `tools/whgap_p15b_*.py` + `artifacts/logs_whgap_p15b_20260801/` +
note `channel-capacity/werner-holevo-gap/notes/WHGAP_P15B_DEATHPOINT_20260801.md`.

### Frozen inputs (read from DISK; this commission's formulas are untrusted)

- The property `P_b2`, the functional `G(ψ, σ)`, and the decomposition identity: take their
  DEFINITIONS from `notes/WHGAP_P15A_STRICTNESS_20260730.md` and the R9 report
  `artifacts/whgap_r9_review_20260801.md`. R9's corrected state of knowledge is the frozen
  baseline: **violations of `P_b2` exist at x = 2/5 and x = 41/100** (R9-verified, interior
  full-rank violators, 9-digit agreement); **bounded null at x = 9/20 and x = 49/100**.
  Hence the death point x_d sits in **(0.41, 0.45)**.
- R9's optimizer protocol and hit-rate observations (≈97% of restarts negative at 41/100)
  are the calibration reference.

### Protocol (pre-registered; boundary-stop discipline applies)

- **Phase 0 — calibration gate G-P15B-1**: with YOUR OWN optimizer (fresh implementation
  or a from-disk tool with provenance recorded), reproduce a `P_b2` violation at
  x = 41/100; sharpen the found minimum with mpmath to ≥ 40 digits and record the pair.
  **If this gate fails, STOP the track and report** — no bisection on an uncalibrated
  instrument.
- **Phase 1 — localization**: coarse scan x ∈ {0.415, 0.42, 0.425, 0.43, 0.435, 0.44,
  0.445} with a restart count N chosen from the Phase-0 hit rate (state the detection-power
  reasoning in the note), then bisect to a bracket **[x_viol, x_null] of width ≤ 5·10⁻³**:
  x_viol = largest x with a certified violation (40-digit sharpened G < 0), x_null =
  smallest x with bounded null at the calibrated N. Deliverables: the bracket, every
  violation certificate (pair + G value), and the min-G-vs-x curve data. Gate G-P15B-2 =
  bracket achieved (else report the partial bracket honestly).
- **Phase 2 — tensorization probe** at 2 points on the surviving side (suggest 0.46 and
  0.48): for Λ_x ⊗ Λ_x, pure anchors in the 9-dim input (BOTH product and entangled
  starts), σ over 9×9 states (product and correlated starts), test whether 2-copy `P_b2`
  violations appear where the 1-copy property holds. Any confirmed 2-copy violation
  (40-digit sharpened) ⟹ `P_b2` does NOT tensorize — record as evidence AGAINST the
  P15 route to Q = 0 on the upper strip. Bounded null ⟹ the route survives (NUMERICAL
  only; say so). Gate G-P15B-3 = a verdict (or documented infeasibility) at ≥ 2 points.
- **Batch discipline**: this commission is batch 1 of ≤ 2. Do not launch extensions beyond
  the three phases; register follow-ups as proposals in the note.
- Numerical hygiene (standing failure-mode list): double-precision scan values are
  LOCATORS only — every certificate is mpmath-sharpened; near-boundary optima must be
  checked for support/rank degeneracy (R5a's exact-zero-mode trap); no verdict from a
  resolution the instrument cannot support; record negative-control runs.
- Compute: local `tools/pypinned.cmd` python is fine for 1-copy; for the 2-copy phase the
  Mac Studio (ssh, `~/qdisc/.venv`) MAY be used under the recorded etiquette (venv python,
  `OMP_NUM_THREADS=1`, `nice -19`, background + logs pulled back into the artifacts dir;
  NEVER commit credentials). State which was used.

Budget ≤ 120 min wall. Return
`{status, summary, bracket, tensorization_verdict, gates, report_path}`.

---

## R15 (chained after Track H only): review of WP-H

NODE_ID = `WHGAP.goal`. ROLE = reviewer (fresh instance; you did not author WP-H and are
told no desired outcome). Scope: report `artifacts/whgap_r15_review_20260801.md` +
`tools/whgap_r15_*.py` + logs prefixed `r15_` in `artifacts/logs_whgap_lean5_20260801/`
(additive).

1. **Own-route verification (7c anchoring ban)**: WITHOUT reading
   `tools/whgap_lean5_wph_check.py`, rebuild both witness outputs from the Kraus set and
   check `S(B) − S(E) = IcScalar` at ≥ 3 rational points of your own choosing, ≥ 40 digits.
2. **Definition audit**: `vnEntropyC` is the standard von Neumann entropy (nats) of the
   Hermitian eigenvalue enumeration; the multiset-strip step uses `ofReal` injectivity and
   assumes NO ordering; the list-form lemma's length hypothesis is not vacuous.
3. **Statement fidelity**: `exists_eps_entropy_pos` quantifier-congruent to
   `exists_eps_IcScalar_pos` (only the conclusion's quantity may differ); `hach'` in
   `Claim_of_entropy_witness` is genuinely WEAKER than `hach` (or exactly the reduction
   claimed), and a satisfiability instance exists or is added to `Model.lean` per §7.10.5.
4. **Trust/README wording**: residual (b) "DISCHARGED" must be accompanied by the explicit
   named remainder (complementary-channel identification + achievability interface);
   over-claim and under-claim both reportable.
5. **Standard §7.10**: clean rebuild reproduction, `#print axioms` on every new
   declaration, forbidden scan, freeze-check (8/8 unchanged), `lean_dag_check` 0 FAIL.
6. Rule-7 embedded set: type audit; c ≥ 2 identity gates on the central identity (charpoly
   route AND direct eigendecomposition route); anchoring ban (item 1); frozen-input scopes;
   standing failure-mode list; value-vs-formula statement.

Menu: **(A)** "WP-H is licensed as recorded; the residual display is accurate" /
**(B)** FINDINGS (MAJORs itemized). Budget ≤ 60 min.
Return `{verdict, summary, majors, minors, report_path}`.

