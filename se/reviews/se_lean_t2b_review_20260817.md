# SE Lean tier-2b + `lean_dag_check` v6 loader — independent review

> **Provenance.** Date 2026-08-17. Reviewer: fresh Claude Opus 5 subagent, non-author of BOTH tracks
> (independence stated in its own PRE-ACTION REPORT; told explicitly that no outcome was preferred).
> Commission: coordination layer, workflow `wf_6732ae6e-d60`, phase "Audit". Scope: the tier-2b
> discharge (`omega_le`, `omega_pos`, `rtop_le_rho`, `rtop_pos` + the θ-carrier rework + review fixes
> F1-F5/F7) AND the `tools/lean_dag_check.py` v6-loader track. This review is what closes frontier
> `task-007` ("the tier-2b increment is executor-authored and unreviewed") and what extends the
> CERTIFIED* basis from tier-2a to tier-2b. Archived VERBATIM by the coordination layer because the
> reviewer deliberately wrote nothing under `research/`.

---

All seven checks complete. Final verdict.

**VERDICT: PASS-WITH-FIXES** (4 fixes, none blocking; no mathematical or mechanization defect found in either track)

---

## PRE-ACTION REPORT (STEP −1)

**Target node / level on disk:** `se/proof-dag/nodes/SE.formal.t2.yaml`, `assessment.level: CERTIFIED*`, basis `se/artifacts/se_lean_t2_review_20260817.md`; frontier `task-006`, `task-007`.
**Role: reviewer.** Independence statement: I authored neither the math track nor the tool track, I was given no wanted outcome, and I was told explicitly that no outcome is preferred. All commands below are my own.
**Highest level my evidence licenses:** none. A review licenses nothing by itself; it is an input the coordination layer may cite. I wrote no level and modified no file under `research/`.

**Conflicts found (reported, not resolved):**
1. `research/PRETASK_RELOAD_PROMPT.md` is PRE-v6, exactly as the commission warned. It cites a "§2 status ladder", "the eight hard rules" (§3), `{NODE_ID}.md` node files, `artifacts.work_record`, a Windows python path, and `tools/literature_check.py` as a mandatory exit-0 closeout gate. **None of that exists in schema v6**: `DAG_PROTOCOL.md` has 8 sections, §2 is "Nodes and routes", §3 is the six-level evidence table, there is no numbered hard-rules list, node records are YAML with `id/role/aliases/claim/assessment/frontier/events`, and `FILE_PROTOCOL.md` §8 names only `proof_dag_check.py`, `check_event_append_only.py`, `git diff --check`. **The disk wins**; I followed `DAG_PROTOCOL.md` + `FILE_PROTOCOL.md`. This is the **third consecutive session** to report it — it should now be fixed rather than re-reported.
2. The template's step 5 says "KSUM and SE use `{NODE_ID}.yaml`; legacy problem trees may still use `{NODE_ID}.md`" — this half is consistent with `FILE_PROTOCOL.md` §1 and with what I found (WHGAP is still legacy-md and still loads). No conflict there.

---

## V1 BUILD — **PASS**

`rm -rf .lake/build && lake build` in `se/proof-dag/lean`. True exit **0**, **3061 jobs**. All 24 SE modules genuinely recompiled (`v1_build.log:1–25`: `SE.Support.Defs` … `SE.Trust` … `SE`). Zero errors. One pre-existing style warning only: `SE/denom/taper.lean:132:4: try 'simp' instead of 'simpa'`. No "declaration uses sorry".

## V2 CENSUS — **PASS**

- `grep` over `SE/**.lean`: **0** `sorry`, **0** `axiom` declarations, **0** `native_decide`, **0** `implemented_by`/`extern`/`unsafe`/`partial def`, **0** `Lean.ofReduceBool`. Every hit is prose inside a docstring.
- **124 declarations** printed by `#print axioms`; **124/124** are exactly `[propext, Classical.choice, Quot.sound]`. Zero non-standard.
- `SE.goal.composition_via_br` — `v1_build.log:26`, clean.
- Coverage: I enumerated all 179 top-level `theorem`/`lemma` declarations and diffed against `SE/Trust.lean`'s 124 `#print axioms` entries. **`Hook.lean`, `Omega.lean`, `Telescope.lean`, `RhoEnvelope.lean`, `BranchFactors.lean` are 100% censused — zero uncensused new declarations.** The 55 uncensused names are all pre-existing tier-1 auxiliaries (`Cbrt`, `Constants`, `Envelope`, `Limits`, `taper`) plus 4 `private lemma`s in `SelfTest.lean` (`one_le_K`, `live_window`, `live_omega_pos`, `live_rtop_pos`), every one transitively covered by a censused top-level theorem. `SE.SelfTest.is` in my first pass was a regex artifact from the prose "theorem is about" at `SelfTest.lean:375`.

## V3 NO-WEAKENING — **PASS** (critical check)

Field-by-field diff of `SE/Interface.lean` against `git:f0d686a`:

| | count |
|---|---|
| tier-1 `Cited` assumption fields | **25** |
| removed | **7** — `rho_ge_one`, `rho_le`, `rhoConst_nonneg`, `rtop_le_rho`, `omega_le`, `omega_pos`, `rtop_pos` |
| added | **3** — `rho_isGreatest`, `admissible_window`, `sector_hook` |
| surviving | **18**, statements **byte-verbatim** (machine-diffed modulo line-wrap: zero differences) |
| tier-2b `Cited` | **21** |

Carrier `SEFrame`: `rhoConst` removed, `shapeLen`/`shapeCol` added (20 → 21).

**Discharged-field statements vs the old assumed fields** (`SE/Support/RhoEnvelope.lean:94,105,119,137`):
- `rtop_le_rho`, `rtop_pos`, `omega_le`, `omega_pos` — binders `∀ n j s, F.admissible n j s →` and conclusions **identical character-for-character** to tier 1, including `omega_le`'s RHS `(j:ℝ)/(2*((n:ℝ)-(j:ℝ)))`. **No narrowing, no added hypothesis, no flipped strictness.**
- `rho_ge_one` — narrowed to `d < K n` (tier-2a, already reviewed). I verified **both** call sites carry it: `denom.lean:120` has `hd : d < K n`; `tame.lean:180` derives it by `omega` from `hjK`. Harmless.
- `rho_le` — abstract `F.rhoConst` → fixed `SE.rhoConst = 4` (`Hook.lean:573`). Declared caveat F2.

**`goal.Claim`: YES, it still concludes 9/(18+4√6+3√10) over the same range.** `SE/Support/Defs.lean` is **byte-unchanged** from tier 1 — `Cconst := 9 / (18 + 4*√6 + 3*√10)`, `envBound`, `epsB` all untouched. The entire `goal.lean` diff is the mechanical substitution `F.rhoConst → SE.rhoConst`; `27 ≤ n` and `Tendsto (epsB ·) atTop (𝓝 0)` are unchanged. Asymptotics identical; the only cost is that the finite-`n` guarantee is now pinned at `c = 4` instead of being frame-dependent — the already-recorded F2 caveat.

**`SelfTest` non-vacuity: YES, all three models still satisfy `Cited` non-vacuously after the θ-carrier rework.** `emptySectorFrame_cited`, `liveSectorFrame_cited`, `channelFrame_cited` all typecheck and are axiom-clean. `channelFrame` is genuinely non-degenerate: `channelFrame_channels_pos` (`SelfTest.lean:549`) proves `xNorm, yNorm, cDiag, cLower, csectS` all `> 0` at `(n,d) = (100,7)`, and its `cLower` now equals `modelCsect` whose positivity comes from the **proved** lower half `j/q ≤ ω` rather than tier-2a's fiat. `liveSectorFrame_goal` and `channelFrame_goal` compose `tame → denom → br → goal` end-to-end.

**The honest headline, which the node states correctly:** the three added fields are *equational/definitional*, hence **strictly stronger** than the inequalities they replace — the admissible-frame class shrank twice. Net −4 fields purchased with three definitional fields citing Frame–Robinson–Thrall. That is a declared change of assumption strength, not a weakening of any statement. One further declared statement change: `taper.Claim` gained conjunct 2, making `denom.composition`'s hypothesis *stronger* than tier 1 — harmless because `taper.holds` is unconditional.

## V4 MATH — **PASS**

I wrote my own exact-rational checker (`fractions.Fraction`, no float), computing `f^λ` from the **actual Young diagram** by FRT rather than reusing the conjugate-coordinate shortcut. **3375 shapes, 0 failures.**

- `rtopHook` **is** `q^j f^θ/(j! f^{(q-j,θ)})` — 0 mismatches.
- `p0Hook` **is** `f^{(q-j-1,θ)}/f^{(q-j,θ)}` — 0 mismatches.
- **Two-sided ω range** `j/q ≤ ω ≤ j/(q-2j)` — 0 violations. I re-derived it by hand: `h_{q-j}=1` kills the top factor; the `c>θ₁` factors telescope over `Ico θ₁ (q-j-1)` to `1/(A-θ₁)`; `θ'_c ≥ 1` gives `∏(1-1/h_c) ≥ (A-θ₁+1)/(A+1)`, `θ'_c ≤ θ'_1 = a` gives `≤ (A+a-θ₁)/(A+a)`. Cross-multiplying, I get **exactly** the two reduced cores Lean proves: lower `q²(s+1) ≥ (q+j)(A+1)s` ⇔ `q² ≥ s(q+j-j²)`; upper, after full expansion, `A(j² - aθ₁) ≥ j²(θ₁ - a)` — character-for-character `omega_upper_core`'s docstring. Both hold with room via `a+θ₁ ≤ j+1` and `A ≥ 5j`. 0 violations of either core over the sweep.
- **`rtop` bound / single-row maximality** — verified independently: the single row `θ=(j)` maximizes `r_top` in **every** case. I also checked the telescoping majorant `1+θ'_{i+1}/(A-i) ≤ (A-S_i+1)/(A-S_{i+1}+1)` reduces to `S_{i+1} ≥ i+1`, which is exactly "every column inside the first row is nonempty". Correct, and equality iff `θ'_c ≡ 1`, i.e. the single row.
- **Equality case at j=1: CONFIRMED.** At `j=1`, `θ=(1)`, `a=L=1`, so `A(j²-aL)=0=j²(L-a)` — the upper reduction is an identity. Closed form: `ω = 1/(q-2) = j/(q-2j)` exactly, verified at `n = 3, 5, 10, 27, 100`. **38 attaining cases in my sweep, all at j=1** (their crosscheck reports 55 over its wider `q≤60` sweep — consistent). Both majorant steps are exact at `j=1`, so no `∏(1-x) ≤ exp(-Σx)` step is admissible. Their worked example (`q=10, j=2, θ=(2)`: `f^(8,2)=35`, `f^(7,2)=27`, `p₀=27/35`, `ω=8/27`) I recomputed from the hook diagram by hand — correct.

## V5 TOOL — **PASS**

Diff of `tools/lean_dag_check.py` (+507/−51): **all seven checks present at their original severities.** Base vs current, identical assignment — 1 FAIL, 2 FAIL, 3 FAIL / 3b WARN, 4 WARN, 5 FAIL, 6 FAIL, 7a FAIL, 7b FAIL+WARN, 7c WARN. The additions are a schema-v6 loader (`detect_schema`, `load_v6_records`, `V6Node`, `build_v6_fixture`) and a `drift_note` diagnostic whose own docstring states *"Severity is unaffected: check 3 still FAILs"* — I confirmed it only appends explanatory text to an existing FAIL message. **The legacy-md loader was retained**, so WHGAP's 16 pre-v6 records still load (this honors `FILE_PROTOCOL.md` §1 against the commission wording the tool track flagged). **No check was weakened; no green was bought.**

My runs:

| target | exit | findings |
|---|---|---|
| `--problem se` | **1** | 12 FAIL, 25 WARN. 7× check-3 (v6 claim-hash resync, every one carrying `sync_state: stale` — the open §7 gate, **not** tier-2b), 1× check-5 (`SE.goal` routes), 4× check-6 (import≠children). All pre-existing, all the declared deviations D2–D6 in `SE/Trust.lean`. Notably `SE.denom.taper` is **not** among the check-3 failures — tier 2 resynchronized its hash. |
| `--problem ksum` | **2** | "registered but NOT enabled" |
| ksum, dirs forced | **1** | 21 FAIL, 17 WARN (e.g. `FAIL [7b] KSUM.A1c: state 'proved' requires the 'rel' key`) |
| `--problem werner-holevo-gap` | **0** | 0 FAIL, 2 WARN, 16 legacy-md nodes loaded |
| `--selftest` | **0** | **8/8 assertions passed**, including "v6: import not matching the route premises must FAIL → PASS" |

## V6 PROTOCOL — **PASS**

- `SE.formal.t2.yaml` valid schema v6: `proof_dag_check.py --problem se` → **exit 0**, 84 nodes; `--verify-git` → exit 0; `--problem ksum` → exit 0, 142 nodes.
- `check_event_append_only.py --base-ref HEAD` → **exit 0**, "Append-only event check OK". No level-change event was written for tier 2b (the increment is a `provenance` event) — correct, since the level did not move.
- **Generated views fresh**: I backed up `NODE_INDEX.md`/`GRAPH.mmd`, re-ran `--write-generated`, and both came back **byte-identical**.
- `git diff --check` → clean (output is CRLF advisories only).
- **SHA ledger complete**: I independently verified `se/artifacts/logs_se_lean_t2b_20260817/SHA256SUMS.txt` — **39/39 entries OK, 0 mismatch, 0 missing**, under the declared LF-normalization (`open(p,'rb').read().replace(b'\r\n',b'\n')`). Evidence dir has all 11 files incl. `command.txt`.
- Level licensed: see Fix 1.

## V7 HONESTY — **PASS**

No wording anywhere suggests H1–H4 progress or root movement. On disk **right now**: `SE.goal` **OPEN**; H1 `trace.t6` **OPEN**; H2 `gram.interface` **CONJECTURED**; H3 `omega.interface` **CONJECTURED**; H4 `sect` **OPEN** — identical to `SE/Trust.lean` §A's tier-1 table. **Not one of those five node files contains a 2026-08-17 event or any mention of `formal.t2`.** The node claim states "does not close any of the four hypotheses H1–H4 and does not change the conditional status of Theorem B"; the report at `se_lean_t2b_20260817.md:244` states "The conditional status of Theorem B is untouched: H1–H4 are still hypotheses"; `Trust.lean:58` keeps "Nothing in this development proves, or even evidences, any of them." The one phrase that could be misread — "H1 and H2 still hold with equality" — is about the **SelfTest models**, and `SelfTest.lean:591` disclaims it: "This checks the PLUMBING on models; it says nothing about the real Set Equality data."

---

## CORRECTED FIELD COUNT

**The math track's claim is correct.** `SE.SEFrame.Cited`: **25 (tier 1) → 23 (tier 2a) → 21 (tier 2b)**, and **21** is what I count in the working tree. The four fields discharged at tier 2b became theorems with their tier-1 binders and conclusions **verbatim** — confirmed, not merely asserted. No correction needed.

## FIXES (enumerated, none blocking)

1. **The level's scope is invisible in the generated views.** `NODE_INDEX.md:70` and `GRAPH.mmd:66` render a bare `CERTIFIED*`. The archived review covers **tier 2a only**; the tier-2b increment (4 fields, 2 new modules, 3 reworked models) is executor-authored and unreviewed, which `DAG_PROTOCOL.md` §3 caps at NUMERICAL. The executor did the right thing — wrote no level, added two caveats and frontier `task-007` — but a reader of the derived view cannot see the split. Fix: either demote to `NUMERICAL` with a `pending-review:` marker until `task-007` closes, or move the qualifier into the **first sentence** of `assessment.summary` so it survives generation. (This is the coordination layer's call, not the executor's; the commissioning instruction to "keep CERTIFIED*" is the conflict both tracks correctly reported rather than resolved.)
2. **`SE.formal.t2.yaml` frontier `task-006` is factually stale.** It says `lean_dag_check.py` "crashes with `ValueError: invalid front matter line: '- COR'` because the tool still loads nodes through the pre-v6 `parse_front_matter`." I independently reproduce that **this is no longer true** — the v6 loader exists and `se` loads all 84 records. It exits 1 for entirely different, pre-existing reasons (the D2–D6 declared deviations and the 7 open §7 hash-resync gates). Rewrite the task text; the "no commission may require it to exit 0" instruction should stand, but on the correct grounds.
3. **Overstated non-lossiness of the lower bound.** `SE/Support/Omega.lean:38` and `SE/Trust.lean:136` say the two majorants have "equality at `j = 1`, so neither is lossy." True of the **majorant steps** (both are exact at `j=1`) but a reader will infer the *lower bound* `j/q ≤ ω` is tight — it is not: **0 attaining cases** in both my sweep and theirs; at `j=1` the exact value is `1/(q-2) > 1/q`. Add half a sentence distinguishing the two.
4. **The "counting note" is itself incomplete.** `SE/Trust.lean:38` and the node offer a conjunct-level count "23 − 4 + 4 = 23" on the grounds that `sector_hook` bundles three conjuncts — but `rho_isGreatest` (`IsGreatest` = membership ∧ upper bound) and `admissible_window` (`1 ≤ j ∧ 3j ≤ n`) each bundle two as well, so the offered conjunct count is not the conjunct count either. Since nothing hinges on it, the cleanest fix is to drop the conjunct arithmetic and state only the field count (21) plus the qualitative fact that no added conjunct is quantitative — which I verified independently against the paper (`se_explicit_witness.tex` ~line 977: `q=2n, j=k-1≥1, λ=(q-j,θ), θ⊢j`, admissibility requires `n≥3j` — so `admissible_window` is verbatim the manuscript's standing setup, carrying no estimate).

**Files:** `<machine-local-path-redacted>`, `.../lean/SE/Interface.lean`, `.../lean/SE/Support/{Hook,Omega,RhoEnvelope,Telescope}.lean`, `.../lean/SE/{Trust,SelfTest,goal}.lean`, `.../tools/lean_dag_check.py`. My audit scratch (independent re-derivation + build log) is at `<machine-local-path-redacted>/` (`v4_independent.py`, `v1_build.log`). I wrote nothing into the repository.
