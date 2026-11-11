# WHGAP commission LEAN-1 — DAG-mirroring Lean development, tier T1+T2 (frozen 2026-07-30)

Commissioner: decision layer (Fable 5 — statements and design below are mine).
Executor: ONE fresh Opus 5 instance. Node (rule 8a): the development mirrors the
propagating skeleton rooted at `WHGAP.goal`; build evidence lands on each mirrored node.
Governed by `research/DAG_PROTOCOL.md` §7 (READ IT FULLY FIRST — it is new) and
`RESEARCH_STRUCTURE_PROTOCOL.md` §4 item 7.

**Mandatory first step:** `research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.goal`, ROLE = executor.
Single-writer deviation binding: no node/index/DAG edits — you write ONLY the Lean
project, run artifacts, and your report note.

## Project shape (§7.2–7.3)

Location: `channel-capacity/werner-holevo-gap/proof-dag/lean/` — one lake project,
package name `whgapDag`. **Toolchain: `leanprover/lean4:v4.31.0` with Mathlib pinned to
tag `v4.31.0`** — copy the pattern of `research/se/lean/` (lakefile, lean-toolchain,
.gitignore) and REUSE its prebuilt `.lake/packages` cache (copy the directory, or follow
`research/se/lean/README.md`); do NOT rebuild Mathlib from scratch. Never commit `.lake/`.

Modules (node ids with hyphens use Lean's «guillemet» identifiers so module = node id
EXACTLY; file paths use the raw names):

    WHGAP/Interface.lean        -- cited external results as structures; NO invented proofs
    WHGAP/Support/Basic.lean    -- shared definitions (channel data as explicit matrices/scalars)
    WHGAP/«private-boundary».lean         -- P14  (T2 flagship: full core proof)
    WHGAP/«order-boundary».lean           -- P6   (T2: gap + threshold identities)
    WHGAP/«signed-lift-extension».lean    -- P2   (T2: forcing identities)
    WHGAP/«no-ascent-hierarchy».lean      -- P9   (T2: d1 sign; T1: expansion as hypothesis)
    WHGAP/«qpositive-onset».lean          -- P3   (T1: composition from P9 + interface)
    WHGAP/«zero-capacity-application».lean-- P4   (T1: composition from P2 + interfaces)
    WHGAP/«onset-two-fifths».lean         -- P13  (stated only: Claim def, no proof — it is a conjecture)
    WHGAP/goal.lean                       -- G    (T1: the union-assembly composition, PROVED outright)
    WHGAP/Trust.lean            -- #print axioms for every top theorem; sorry census
    WHGAP/SelfTest.lean         -- decidable/rational checks of definitions at known values

Every node module carries the §7.4 docstring: node id, dated epistemic status, the
VERBATIM frozen Claim text from its node file, and the SHA-256 of that frozen text
(compute it; LF bytes).

## Design (decision layer; derive-and-verify, do not blindly trust my algebra)

**Support/Basic.** Work over ℝ. Fixed scalars as functions of x (and ε, t where needed):
b(x,ε) = x/2 + (1−3x/2)ε; e(x,ε) = (x/2)(1−ε); u(x,t) = t(1−3x/2)/√2; v(x,t) = tx/(2√2);
ε_c(x) = 2(1−2x)/(2−3x); d₁(x) = (1−x)(2−5x)/(2−x); f(s) = (1+s)·Real.log(1+s) +
(1−s)·Real.log(1−s); Δ tuple per P14. For matrix-level facts use
`Matrix (Fin 2) (Fin 2) ℝ` with the sqrt-free parameterization: carry β as a variable
with hypothesis hβ : β^2 = x(1−x)/2 (NEVER Real.sqrt in identities).

**T2 statements (simple → hard; ALL must be sorry-free):**

1. (P6 module) `gap_identity`: for x ≠ 0,
   x/2 − (2/x)(1 − 3x/2)^2 = 2(1−x)(2x−1)/x.  [field_simp; ring]
   `threshold_factorization`: x·b(x,ε) − 2(1−3x/2)^2(1−ε) = 2(1−x)((2x−1) + (1−3x/2)ε).
   `gap_neg_below_half`: 0 < x → x < 1/2 → 2(1−x)(2x−1)/x < 0.
   `strict_violation_window`: 0 < x → x < 1/2 → 0 < ε → ε < ε_c(x) →
   x·b(x,ε) − 2(1−3x/2)^2(1−ε) < 0.  [sign analysis on the factorization]

2. (P2 module) the two forcing identities of paper Prop 3.2 as rational-function
   identities in (x,p,d), x ∉ {0}:
   `forcing_p`: (p−1)(x−1)(p+2x−1)/x + 4·(x−1)(2p²+px−2p+x)/(2x)
     + 2·(x−1)(p²−px−2x+1)/x + 2·(x−1)(p²−px+2x−1)/x = (3p−1)²(x−1)/x.
   `forcing_d`: 2·(−(9d²+4dx−8d+4x²−8x+4)/(2x)) + 2·(−2d(2x−1)/x) = −(3d+2x−2)²/x.
   `defect_eigenvalues_sign`: λ₅(x) = 4(1−x)(2x−1)/x satisfies (λ₅ ≥ 0 ↔ x ≥ 1/2) on
   0 < x < 1, and λ₃(x) = 16(1−x)(3x−1)/(9x) ≥ 0 ↔ x ≥ 1/3 on the same domain.
   Docstring honesty: these verify the DISPLAYED identities and sign analysis of the
   uniqueness/spectrum proofs, not the 27×27 construction itself.

3. (P14 module — the flagship; every step sorry-free):
   `f_pos`: ∀ s, 0 < s → s < 1 → 0 < f s.
     [Route: f 0 = 0 and StrictMonoOn via deriv f s = log(1+s) − log(1−s) > 0; or the
      direct convexity route — your choice, prove it, no axioms.]
   `argument_coincidence`: for 0 < x < 1/2 and ε = t = ε_c(x)/2:
     u(x,t)/b(x,ε) = (1−2x)/(√2(1−x)) ∧ v(x,t)/e(x,ε) = (1−2x)/(√2(1−x)).
     [Rational identities; keep √2 as a variable r with hr : r^2 = 2, r > 0.]
   `prefactor_pos`: b(x,ε) − e(x,ε) = ε(1−x), positive for 0 < ε, x < 1.
   `Delta_closed_form_pos` (MAIN): for 0 < x < 1/2, with ε = ε_c(x)/2 and
     s* = (1−2x)/(√2(1−x)): 0 < s* < 1 (needs (1−2x)² < 2(1−x)², i.e. ring+positivity)
     and Δ := (b−e)·f(s*) = ((1−2x)(1−x)/(2−3x))·f(s*) > 0.
   `Delta_lower_bound` (bonus if cheap): f s ≥ s² on [0,1) ⟹ Δ ≥ (1−2x)³/(2(1−x)(2−3x)).
   Matrix layer (supports paper Lemma 7.1): on `Matrix (Fin 2) (Fin 2) ℝ`
   `blockA_trace_det`: for A = !![1−x, −β(1−2ε); −β(1−2ε), x/2] with hβ : β^2 = x(1−x)/2:
     trace A = 1 − x/2 ∧ det A = 2x(1−x)ε(1−ε).
   (Real symmetric stand-in for the Hermitian block — the entries' moduli are what enter;
    state this honestly in the docstring.)

4. (P9 module) `d1_sign`: on 0 < x < 1, 0 < d₁(x) ↔ x < 2/5; `d1_at_2_5`: d₁(2/5) = 0.
   T1 hypothesis-form expansion: given hexp : ∀ ε ∈ Ioo 0 ε₀, |Ic ε − d₁·ε·Real.log (1/ε)|
   ≤ C·ε (Ic : ℝ → ℝ abstract, C ≥ 0, ε₀ > 0), and d₁ > 0, conclude ∃ ε ∈ Ioo 0 ε₀,
   0 < Ic ε.  [choose ε < min(ε₀, exp(−(C+1)/d₁)); Mathlib: Real.exp_log etc.]

5. (Interface) structure `CapacityInterface` with fields: state space placeholder,
   Q P Qone Pone : ℝ → ℝ (index = x); axioms-as-fields with EXACT citations in
   docstrings: `lsd_devetak : ∀ x, Qone x ≤ Q x ∧ Pone x ≤ P x` (LSD/Devetak via
   superadditivity — cite ZW eq. 2.6/2.7); `zw_hrsf_zero : ∀ x, (SignedLiftCP x) →
   Qone x = 0 ∧ Pone x = 0 ∧ Q x = 0 ∧ P x = 0` with `SignedLiftCP : ℝ → Prop` a field
   (cite ZW Thm 3.3 + BGSW25 + HRSF22 Lem 3.1); `q_pos_of_ic_pos : ∀ x c, 0 < c →
   IcLB x c → 0 < Q x` with `IcLB : ℝ → ℝ → Prop` a field. Keep the interface MINIMAL
   and honest — it is the trust boundary, and the README must say so in the §7.9 words.

6. (T1 composition layer — §7.4 exactly):
   - P2/P6/P9/P13/P14 modules: `def Claim (I : CapacityInterface) : Prop := ...`
     matching the frozen node Claims at the granularity the interface allows (e.g.
     P14.Claim := ∀ x, 0 < x → x < 1/2 → 0 < I.P x; P13.Claim := the determination of
     {x ∈ [2/5,1/2) | I.Q x = 0} as a given set S — parameterize: Claim S).
   - P4 module: `theorem composition (I) (h2 : «signed-lift-extension».Claim I) :
     Claim I` — where P2.Claim supplies SignedLiftCP on [1/2,1) and the interface field
     discharges the capacities. The Lean proof IS the R3 note's assembly logic.
   - P3 module: `theorem composition (I) (h9 : «no-ascent-hierarchy».Claim I) : Claim I`
     via the interface's q_pos field + d1_sign.
   - goal module: `theorem composition (I) (S) (h3 : P3.Claim I) (h4 : P4.Claim I)
     (h13 : P13.Claim I S) : Claim I S` where goal.Claim I S :=
     {x ∈ Ioo (0:ℝ) 1 | I.Q x = 0} = (Ico (1/2) 1) ∪ S — prove the set equality
     OUTRIGHT from the three pieces (my inline union assembly; Set.ext + interval
     case analysis; this one is a genuine complete Lean proof of the G composition).
   The import graph must equal the DAG skeleton: goal imports P3, P4, P13; P3 imports
   P9; P4 imports P2; «order-boundary» imports P2. §7.6 check 5/6 compliance.

7. `SelfTest.lean`: `example : d₁ (2/5) = 0 := by norm_num [d₁]`; ε_c(9/20) = 1/13... 
   compute: ε_c(9/20) = 2(1−9/10)/(2−27/20) = (1/5)/(13/20) = 4/13 — VERIFY yourself with
   norm_num, do not trust my arithmetic; b, e, d₁ at two rational points against
   independently computed rationals; the forcing identities at (x,p,d) = (2/5, 1/3, 2/5).

8. `Trust.lean`: `#print axioms` for every top theorem (expect: `propext`,
   `Classical.choice`, `Quot.sound` ONLY); assert no `sorry`, no `native_decide`.

## Gates (pre-registered)

- **G-L1:** `lake build` exit 0, full transcript captured.
- **G-L2:** zero `sorry` anywhere; `#print axioms` on every top theorem shows only the
  three standard axioms; grep for `native_decide`/`implemented_by` clean.
- **G-L3:** SelfTest compiles with all examples closed by `norm_num`/`decide`.
- **G-L4:** import graph = DAG skeleton (list the imports in the report and check).
- **G-L5 (statement fidelity, self-check tier):** for each module, quote the frozen
  prose Claim and your Lean `Claim` side by side in the report and state the
  correspondence and any granularity loss (e.g. "Q as an interface field, not defined").
  A separate fresh statement-fidelity review is the completion gate — NOT yours.

## Deliverables

Project as above; run artifacts per §7.7 under `artifacts/logs_whgap_lean_20260730/`
(command + exit status + full transcript + #print axioms output + SHA256SUMS.txt, LF);
report `artifacts/whgap_lean_t1t2_20260730.md` (with the §7.9 scope sentences verbatim +
the G-L5 side-by-side table); README in the project with the §7.9 language.
Cap: NUMERICAL (`pending-review:`) — a green build is a run, not a status.
Budget: ≤ 150 min. If a T2 item resists, leave it as an explicit hypothesis parameter
(NEVER sorry), document append-only, and continue — the flagship P14 core and the goal
composition are the two MUST-LAND items.
Return {status, summary, built: bool, sorry_count, axioms_clean: bool, report_path,
project_path, must_land_ok: bool}.

