# SE Lean tier-2 discharge — independent review (DAG_PROTOCOL §3/§5.5)

> **Provenance.** Date 2026-08-17. Reviewer: fresh Claude Opus 5 subagent, non-author (independence
> stated in its own PRE-ACTION REPORT: did not author the tier-2 work, given no wanted outcome).
> Commission: coordination layer, workflow `wf_073bc9f2-10f`, phase "Audit". Target node
> `SE.formal.t2`; frontier item `task-005` ("Independent review of the tier-2 discharge") is the
> item this review discharges. Archived VERBATIM by the coordination layer because the reviewer
> deliberately wrote nothing into the repository (it only re-ran the generated-view writer and
> rebuilt the `.lake/build` cache); a completion tier requires the review to be on disk and cited.
> The text below is the reviewer's final report, unedited.

---

## VERDICT: **PASS-WITH-FIXES** (7 fixes, none blocking; no mathematical or mechanization defect found)

Independence: I did not author any of the reviewed work, was given no wanted outcome, and wrote nothing to the repository except re-running the generated-view writer (byte-identical output) and deleting/rebuilding the `.lake/build` cache.

---

### PRE-ACTION REPORT (STEP -1 discharged)

- Read from disk, in order: `research/PRETASK_RELOAD_PROMPT.md`, `DAG_PROTOCOL.md` (all 8 sections), `FILE_PROTOCOL.md` (all 8 sections), `se/README.md`, `se/proof-dag/PROJECT.yaml` (`schema_version: 6`, root `SE.goal`), `se/proof-dag/NODE_INDEX.md` (generated; `SE.formal.t2` at line 70), then `se/proof-dag/nodes/SE.formal.t2.yaml` and the nodes it touches (`SE.formal.t1`, `SE.denom.taper`, `SE.denom.assembly.envelope`).
- **Target node / status on disk:** `SE.formal.t2`, `assessment.level: NUMERICAL`, caveat `pending-review`, frontier `task-005` = "Independent review of the tier-2 discharge". That frontier item is exactly this commission.
- **Role:** reviewer. I did not author the reviewed work and was given no desired outcome.
- **Highest level my evidence licenses:** my evidence is an independent re-execution + statement-level audit. Under §3/§5.5 that is the missing ingredient for a completion tier; it licenses at most **CERTIFIED\*** on `SE.formal.t2` (reviewed, but conditional on one un-Lean-ified external theorem — Frame–Robinson–Thrall). **`PROVED` is not licensed** and neither is any change to `SE.goal`/H1–H4. I wrote no level; recording is the coordinator's.
- **Conflicts between this commission and the disk:** the commission's own framing ("§7 governs formalization", node records are YAML with id/role/aliases/claim/assessment/frontier/events, NODE_INDEX generated) matches disk v6. `PRETASK_RELOAD_PROMPT.md` itself is **pre-v6** (it cites a `status` ladder, "the eight hard rules", `artifacts.work_record`, `{NODE_ID}.md`, and a Windows Python path) — none of which exist in schema v6. I followed the disk and report the conflict rather than resolving it. One commission item is unsatisfiable as written: V5 demands `tools/lean_dag_check.py` exit 0, which is impossible for `se` (see V5/F6).

---

### V1 BUILD — **PASS**

My own command, from `se/proof-dag/lean`:

```
rm -rf .lake/build && lake build
```

`REVIEWER_CLEAN_BUILD_EXIT=0`, `Build completed successfully (3059 jobs).` One cosmetic linter warning only (`SE/denom/taper.lean:132:4: try 'simp' instead of 'simpa'`), zero errors. The executor's claimed exit status and job count reproduce exactly. Toolchain `leanprover/lean4:v4.31.0`, mathlib pinned `v4.31.0` in `lakefile.lean`.

### V2 CENSUS — **PASS**

- Project-wide grep for `sorry` / `axiom ` / `native_decide` / `implemented_by` / `unsafe` / `opaque` / `extern` over `SE.lean`, `SE/`, `lakefile.lean`: **every hit is prose inside a docstring** (e.g. `SE/Support/Hook.lean:23`, `SE/Trust.lean:12`, `SE/denom/taper.lean:57`). No `sorry`, no `axiom` declaration, no `native_decide`.
- My clean build printed **79** `#print axioms` lines (`SE/Trust.lean:183`–`:266`), **all exactly** `[propext, Classical.choice, Quot.sound]`. My census is **byte-identical** to `se/artifacts/logs_se_lean_t2_20260817/print_axioms.txt` after normalization (diff empty).
- `theoremB` is not a declaration name; the report itself identifies it as `SE.goal.composition_via_br` (report line 33). I printed axioms on it independently: `[propext, Classical.choice, Quot.sound]`.
- **Unlisted-declaration check.** Seven top-level declarations added by tier 2 are *not* in `SE/Trust.lean`'s census: `SE.rise_den_pos`, `SE.hook_den_pos`, `SE.one_le_rise_factor`, `SE.one_le_hook_factor`, `SE.two_pow_pos`, `SE.SelfTest.modelRho_nonneg`, `SE.SelfTest.lt_of_lt_K`. I ran `#print axioms` on all seven plus every new `def` (`rtopHook`, `hookExponent`, `rhoConst`, `specialPathFactor`, `specialPathFactorLen`, `rowShape`, `modelRho`) via `lake env lean`: all standard-axioms-only, and each is a dependency of a listed theorem, so the census is transitively complete. Not a FAIL; listed as fix F7-adjacent housekeeping. Also verified `SE.rhoConst = 4` by `rfl`.

### V3 NO-WEAKENING — **PASS** (the critical check; two narrowings, both real, both non-weakening at the chain level, both declared)

Method: `git diff HEAD -- SE/Interface.lean` plus a programmatic field-statement extraction of `structure Cited` from `git:f0d686a:.../SE/Interface.lean` vs. the working tree.

**Field-by-field result.** 22 of the 25 tier-1 fields have **byte-identical statements** (`adv_ge, block_triangle, bthe_pos, cDiag_bound, cDiag_nonneg, cDiag_zero, cLower_nonneg, cLower_zero, csect_nonneg, defect_orth, maskNorm_pos, mask_from_D, mxi_nonneg, numerator, omega_le, omega_pos, rtop_le_rho, rtop_pos, xNorm_nonneg, x_bound, yNorm_nonneg, y_bound`). Zero fields survived with a *changed* statement. Removed: `rho_ge_one`, `rho_le`, `rhoConst_nonneg`. Added: `rho_hook` (`SE/Interface.lean:156-157`). `SEFrame` 20 → 19 (`rhoConst` removed).

| discharged field | tier-1 statement | tier-2 theorem | verdict |
|---|---|---|---|
| `rho_ge_one` | `∀ n d, 1 ≤ F.rho n d` | `SE/Support/RhoEnvelope.lean:44` — `∀ n d, d < K n → 1 ≤ F.rho n d` | **hypothesis added** (declared). Both — and only — call sites already carry it: `SE/denom.lean:120` (`hd : d < K n`) and `SE/denom/Phi/legal/tame.lean:180` (`by omega` from `hjK : j < K n - 1`). Conclusion verbatim. |
| `rho_le` | `∀ n d, d < K n → F.rho n d ≤ 1 + F.rhoConst/n^(1/3)` | `SE/Support/RhoEnvelope.lean:57` — same, with `SE.rhoConst` | scope identical; abstract constant replaced by a proved explicit one. |
| `rhoConst_nonneg` | `0 ≤ F.rhoConst` | `SE/Support/Hook.lean:397` — `0 ≤ (4:ℝ)` by `norm_num` | trivial; it existed only to constrain the carrier field that was deleted. |

**`theoremB` — explicit answer.** `SE.goal.Claim` (`SE/goal.lean:75-77`) still concludes, for the **same range** `∀ n, 27 ≤ n`, that `(SE.Cconst - SE.epsB c n) * n^(1/3) ≤ F.adv n` together with `Tendsto (epsB c) atTop (𝓝 0)`, with **`SE.Cconst` textually unchanged** = `9/(18 + 4√6 + 3√10)` (`SE/Support/Defs.lean:53`; `inv_two_one_add_Mconst` unchanged). The *only* change is `c`: the universally-carried `F.rhoConst` became the closed `SE.rhoConst = 4`. So: **same constant `9/(18+4√6+3√10)`, same range `n ≥ 27`, same `ε_n → 0`** — the asymptotic content of Theorem B is unchanged, and the conditional status (H1–H4 still hypotheses of `tame.composition`) is unchanged.

The one thing that *did* move is the finite-`n` size of `ε_n`, because `envBound` is increasing in `c`. My computation of `(n^{1/3}-1)/(2·envBound c n)` at 40-digit precision:

| n | bound at c=0 | bound at c=4 | ratio |
|---|---|---|---|
| 27 | 0.272476 | 0.116775 | 0.429 |
| 10³ | 1.575578 | 1.125413 | 0.714 |
| 10⁶ | 21.369578 | 20.547671 | 0.962 |

This is **not** a weakening of anything previously established: `c` was an unconstrained carrier datum at tier 1 (only `0 ≤ c` was assumed), and `c = 0` — the value the three tier-1 `SelfTest` models actually used — forces `ρ_d ≡ 1`, which is **false** for genuine hook values (I computed `r_top(2·343, 6, (6)) = 1.03125`). Tier 2 closes that hole: the models now carry `modelRho n d = rtopHook (2n) d d (rowShape d)` (`SE/SelfTest.lean`, new block), a real hook value, and `c = 0` is no longer available. I count this as a strengthening of the trust story. It must nevertheless be recorded (F2), because report line 132-134 ("strictly more informative") is true of `ρ_d` but not of the downstream `goal.Claim` relative to a smaller `c`.

Two further statement movements the report does not fully cover, both benign: `rho_hook` is an **equational** assumption, hence strictly stronger than the two inequalities it replaced — the admissible frame class shrank, so `Cited → X` theorems hold for fewer frames (F4); and `SE.denom.taper.Claim` gained a third conjunct (`SE/denom/taper.lean:243-249`), so `denom.composition`'s hypothesis is strictly stronger than tier-1's — harmless only because `taper.holds` proves the whole Claim unconditionally (F5).

### V4 MATH — **PASS** (independent re-derivation, `Fraction`/`Decimal(prec=60)`, no floats in any comparison)

1. **Hook-envelope log bound.** Exact rational verification of the two majorant steps over **218 698** `(q, d, θ)` triples (all `q ≤ 60`, all `2d < q`, all partitions of `d`, conjugates computed independently): `Σ_{i<d} i/(q−i) ≤ d(d−1)/(2(q−d+1))` and `Σ_c θ'_c/(q−d−c+1) ≤ d/(q−2d+1)`, hence `log r_top ≤ E(q,d)` — **PASS**, no exception. Independently, `log(rtopHook) ≤ E(q,d)` at 60-digit precision for all `q ≤ 40` — **PASS**. Downstream: `E(2n,d) ≤ 1/K(n)` for every `n < 3000, d < K(n)` — **PASS**; and `r_top(2n,d,θ) ≤ 1 + 4·n^{−1/3}` for every `n < 400, d < K(n)` and every partition, checked exactly as `(r−1)³·n ≤ 64` — **PASS**, with the smallest sufficient constant `sup (r_top−1)·n^{1/3} ≈ 0.2188` (attained at `n=343, d=6, θ=(6)`). So `4` is correct and comfortably loose; it is not tight, but it is not weaker than any established tier-1 value.
2. **One-defect identity `r_{j+1} = j·r_top`.** Exact rational equality at 960 points (`q ∈ {3, 7, 11/2, 101/7, 1000003/17}`, `j = 0..11`, `f^θ, f^λ` over four rationals) — **PASS**; and the cancellation `q^{j+1} − q^j(q−j) = j·q^j` — **PASS**. Matches `SE/Support/Hook.lean:201`.
3. **Special-path maximum.** `spf(s) = (s+1)/2^{max(0,s−2)}` over exact `Fraction`s: values `1, 2, 3, 2, 5/4, 3/4, 7/16, …`; `max = 3`; `{s : spf(s) = 3} = {2}`, i.e. **equality exactly at |P| = 4** — **PASS**. `|P|`-indexed form `≤ 3` for all even `|P| ≥ 2` and `= 3 ⟺ |P| = 4` — **PASS**; `spfLen(2s) = spf(s)` — **PASS**. Matches `SE/Support/BranchFactors.lean:82, 94, 118`.
4. **Bonus (taper conjunct 2, since it is a claimed R2 discharge).** `(K(n)−k)₊²·k ≤ n` for all `n < 4000` and all `k` — **PASS**; and the AM–GM identity `4(m+k)³ − 27m²k = (m−2k)²(4m+k)` verified on a 13×13 integer grid (conclusive for total-degree-3 polynomials) — **PASS**.
5. **Bonus (Theorem B constants).** `M = (4√6+3√10)/18` and `1/(2(1+M)) = 9/(18+4√6+3√10)` by exact radical normalization (`√(15/8) = √30/4`, `√90 = 3√10`), confirmed at 60 digits: `C = 0.2413852814754581733126…`, matching `Cconst_digits` in `SE/Support/Constants.lean:135`.

### V5 PROTOCOL — **PASS except one item that is impossible to satisfy**

My own commands from the repo root:

| command | exit | result |
|---|---|---|
| `python3 tools/proof_dag_check.py --problem se` | **0** | `se: 84 node files structurally valid` |
| `python3 tools/proof_dag_check.py --problem se --write-generated` | **0** | `NODE_INDEX.md` and `GRAPH.mmd` come back **byte-identical** (diff empty) ⇒ generated, not hand-edited |
| `python3 tools/check_event_append_only.py --base-ref HEAD` | **0** | no event deleted or rewritten |
| `python3 tools/literature_check.py` | **0** | `Literature catalogs OK: 52 papers across 5 libraries, schema v1` — **the file exists**, see F1 |
| `python3 tools/lean_dag_check.py --problem se` | **2** | `se` is `enabled=False` in the tool's `REGISTRY` (`tools/lean_dag_check.py:78-82`) |
| same tool, `enabled=True`, run from a scratch copy | **crash** | `ValueError: invalid front matter line: '- COR'` — I reproduced the executor's finding exactly; it loads nodes through the pre-v6 `parse_front_matter` and dies on the first v6 record |
| `git diff --check -- research/se se/artifacts/logs_se_lean_t2_20260817 se/artifacts/se_lean_t2_20260817.md` | **0** | only pre-existing repo-wide CRLF *warnings* |

Node record `SE.formal.t2.yaml`: valid v6 — `id`/`aliases`/`role: tool`/`claim`/`assessment{level,summary,basis,caveats}`/`frontier`/`events`; `caveats` is a documented `ASSESSMENT_KEYS` member (`tools/proof_dag_v6.py:31`); no `artifacts` block, no `routes` (direct-evidence node, permitted by §2); `level-change` event carries `from: OPEN`/`to: NUMERICAL` with sources; frontier holds only unfinished work (`task-003`, `task-004`, `task-005`).

Evidence directory complete and verified: `command.txt`, `lake_build_clean.txt`, `print_axioms.txt`, `grep_trust.txt`, `interface_field_census.txt`, `interface_diff.txt`, `lean_dag_check_se_trial.txt`, `SHA256SUMS.txt`. I re-verified all **37** ledger entries over LF-normalized bytes: **37 OK, 0 mismatch, 0 missing**. The `SE.denom.taper` claim hash resync is genuine: I recomputed `sha256` of the v6 claim line and got `d181c0bdb60c41fdfca5b888339302081d5908caf23350ecfd3c88d297ae8221`, matching `formalization.lean.claim_hash`.

I independently reproduced the field census: `SEFrame` 20 → 19, `Cited` 25 → 23, removed `{rho_ge_one, rho_le, rhoConst_nonneg}`, added `{rho_hook}` — identical to `interface_field_census.txt`.

Context note (not a finding against this session): HEAD is `f0d686a` = the **schema-v5** snapshot, so the entire v6 SE tree — including all 84 node records — is uncommitted working-tree state. The `git:f0d686a:…` baselines the report cites do resolve; the new evidence has no git object yet, and the `SHA256SUMS.txt` ledger is what substitutes for one.

### V6 HONESTY — **PASS on substance; two factual misstatements about a tool**

- The report and the node record **never** claim H1–H4 progress and **never** claim the root moved. `SE.formal.t2.yaml` says verbatim: "It establishes nothing about H1-H4 and does not change the conditional status of Theorem B." The claim field states the same. Correct.
- Level: `NUMERICAL` + `pending-review` caveat is exactly what §3 licenses for mechanized run evidence, and §5.5 bars the author from more. Verified that **no other node's level changed**: only four node files were touched (`SE.formal.t2`, `SE.denom.taper`, `SE.formal.t1`, `SE.denom.assembly.envelope`); the latter three received `provenance`/`repair-applied` events with levels held at NUMERICAL/PROVED(legacy-mirror)/NUMERICAL. The envelope node correctly refuses to absorb the result, noting its frozen claim (`ρ_{n,k} ≤ R_{n,k}`, in-spec max 16/15) is *sharper* than what tier 2 proves — consistent with my measured worst case 1.0313.
- Every quantitative claim in the node summary that I could check is true: 3059 jobs, exit 0, 79 axiom-clean declarations, 25 → 23 fields, all three `composition` theorems and `composition_via_br` still typechecking, three non-vacuity models still satisfying `Cited`.
- Defect: **the report twice asserts that `tools/literature_check.py` does not exist** (lines 52-54: "`ls tools/literature_check.py` → absent"; line 233: "the file does not exist in this tree"). It exists, is tracked at HEAD, and exits 0. See F1.

---

### FIXES (enumerated; none blocks acceptance of the tier-2 work)

- **F1 (accuracy, report only).** `se/artifacts/se_lean_t2_20260817.md` lines 52-54 and 233: `tools/literature_check.py` **does** exist (tracked at HEAD, last touched in `78399df`) and `python3 tools/literature_check.py` exits **0** — `Literature catalogs OK: 52 papers across 5 libraries, schema v1`. Correct both places and record the real status; PRE-ACTION conflict item 2's second half is withdrawn.
- **F2 (precision, report + node caveat).** Add the finite-`n` consequence of fixing `c = 4`: `C = 9/(18+4√6+3√10)`, the range `n ≥ 27` and `ε_n → 0` are unchanged, but the finite-`n` guarantee `(n^{1/3}−1)/(2·envBound c n)` is 0.43× / 0.71× / 0.96× the `c = 0` instance at `n = 27 / 10³ / 10⁶`. Report line 132-134's "strictly more informative" is true of `ρ_d`, not of `goal.Claim` against a smaller `c`. Also worth recording that the smallest constant the data support is ≈ 0.219, so `4` is valid but loose.
- **F3 (prose vs. statement).** `SE/Interface.lean:143-147` and report §3.1 say `rho_hook` asserts the maximum `ρ_d = max_{θ⊢d} r_top` **is attained**. The Lean statement (`SE/Interface.lean:156-157`) never mentions a maximum: it asserts only that `ρ_d` equals *some* `rtopHook` of some `IsColumnData`. That is weaker than described (so trust-safe), but the docstring should match the statement; `rtop_le_rho` remains the only field tying `ρ` to a maximum.
- **F4 (headline honesty).** Say explicitly that `rho_hook` is an **equational** assumption and therefore strictly stronger than the two inequalities it replaced: the admissible-frame class shrank, so every `Cited → X` theorem now covers fewer frames. This is the correct direction for a discharge and the paper's frame satisfies it (the three `SelfTest` models witness satisfiability), but "25 → 23 fields" alone hides it.
- **F5 (statement change not covered).** Report §3.5's "every `composition` theorem retains its exact tier-1 statement" omits that `taper.Claim` gained a conjunct, so `denom.composition`'s hypothesis is strictly stronger than tier-1's. Harmless (`taper.holds` is unconditional), but it is a statement change.
- **F6 (repo tool, not this node).** `tools/lean_dag_check.py` cannot exit 0 for `se`: `enabled=False` gives exit 2, and flipping it crashes with `ValueError: invalid front matter line: '- COR'` because the tool still loads nodes through `proof_dag_check.parse_front_matter` (pre-v6). Independently reproduced. File as a repo-level frontier item ("give `lean_dag_check.py` a v6 loader"), not on `SE.formal.t2`; the V5 requirement that it exit 0 is currently unsatisfiable and should be struck from future commissions until the loader lands.
- **F7 (cosmetic).** `specialPathFactor_eq_three_iff` (`SE/Support/BranchFactors.lean:94`) carries a needless `hs : 1 ≤ s`; `spf(0) = 1 ≠ 3`, so the `↔` holds at `s = 0` too. Also consider adding the seven transitively-covered auxiliary lemmas to the `SE/Trust.lean` census so the census is literally, not just transitively, complete.

### Corrected count of genuinely discharged fields

The executor's arithmetic is **correct**: `Cited` 25 → 23, three fields removed, one added, `SEFrame` 20 → 19. I reproduced it independently from `git:f0d686a`.

The count of fields discharged **with mathematical content is 2, not 3**: `rho_ge_one` and `rho_le`. The third, `rhoConst_nonneg`, was `0 ≤ F.rhoConst` on a carrier datum that this change deletes; its "proof" is `0 ≤ 4` by `norm_num`. The honest headline is therefore: **two quantitative analytic assumptions (plus one bookkeeping nonnegativity) replaced by one definitional/equational assumption that cites Frame–Robinson–Thrall — net −2 interface fields, with the added field strictly stronger than the ones removed.**

Recommendation on level (for the coordinator, not written by me): with this review archived and cited, `SE.formal.t2` is licensed for **CERTIFIED\*** — reviewed, with explicit caveats being (i) the cited FRT hook-length formula, (ii) the declared `d < K n` scope narrowing of `rho_ge_one`, and (iii) the fixed `c = 4` in `denom`/`br`/`goal.Claim`. `PROVED` is **not** licensed while the discharge rests on an external theorem absent from the Lean development, and nothing here licenses any movement on `SE.goal`, H1–H4, or `SE.denom.taper`'s legacy-mirrored PROVED.
