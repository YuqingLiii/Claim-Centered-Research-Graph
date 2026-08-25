# frontier task-008 / task-010 / task-011 clearance — independent review (discharges task-013)

> **Provenance.** Date 2026-08-17. Reviewer: fresh Claude Opus 5 subagent, non-author (authored no
> commit, node, Lean file, artifact or tool edit under review; given no wanted outcome; wrote NOTHING
> into the repository — every mutation was made in throwaway scratchpad copies, verified by a
> byte-identical `git status` at the end). Commission: coordination layer, workflow `wf_b390a146-5f0`,
> phase "Audit". It was required to re-run the previous review's six adversarial probes AND to invent
> at least two new ones. It ran five new probes and found two new soft spots (NEW-1, NEW-4, NEW-5),
> including the fundamental one: a MEANING change can be laundered past the entire hash machinery if
> all four records are updated consistently. Archived VERBATIM by the coordination layer.

---

PRE-ACTION REPORT

- Read completely, in order: `research/PRETASK_RELOAD_PROMPT.md`, `DAG_PROTOCOL.md` (schema v6, all 8 sections), `FILE_PROTOCOL.md`, `se/README.md`, `se/proof-dag/NODE_INDEX.md`, then `se/proof-dag/nodes/SE.formal.t2.yaml` in full and every node/module/artifact it touches.
- Target node: `SE.formal.t2`, read from disk as level **CERTIFIED\***, role `tool`, open frontier `task-012` (check-4 elaboration) and `task-013` (this review, registered before the work).
- ROLE: **reviewer**. Independence: I authored no commit, node, Lean file, artifact or tool edit under review; I was given no wanted outcome; I wrote **nothing** into the repository — every mutation was made in throwaway copies under my scratchpad (verified at the end: `git status` for `research/se`, `tools/`, `se/artifacts/` is byte-identical to the state at session start). The only repo-side effect is the `.lake/build` cache, which FILE_PROTOCOL §4 declares a cache and which I rebuilt green.
- Highest LEVEL my evidence could license per §3: `NUMERICAL` for the mechanized parts I reproduced. As an independent reviewer my report may *license* a completion tier for others to write; I write no level myself.
- Gates: V1 re-run the six probes myself; V2 invent ≥2 new probes; V3 no-weakening diff vs `9f92ff8` + F1 margin on the 26 real declarations; V4 re-derive the ω tightness claim and judge task-010; V5 own clean rebuild + census + regression; V6 protocol validators/events/views/levels.
- Conflict between commission text and disk: **none.**

---

# VERDICT: PASS-WITH-FIXES — no blocking finding

The central question — *was any FAIL cleared, or any residual hidden, by weakening the checker?* — answer: **NO.** Nine non-blocking fixes are enumerated at the end; two of them are new soft spots my own probes found.

## V1 — the six probes, re-run by me in throwaway copies

Method: `rsync`'d `se/proof-dag` (minus `.lake`) + `tools/` into a scratch root and drove the checker with `--root <scratch>` (never `--nodes-dir/--lean-dir` alone — the prior review is right that `src_of()` ignores `--lean-dir`). Baseline reproduces the cited log exactly: **0 FAIL / 17 WARN / 9 INFO, exit 0**; `--selftest` **23/23**. My harness is written from scratch (`probes.py`), not `22_probes_harness.py`. Each probe was run against **both** a pristine `git show HEAD:tools/lean_dag_check.py` and the hardened tool.

| probe | mutation | HEAD tool | hardened tool | verdict |
|---|---|---|---|---|
| **P1** F1 junk mechanism | `SE.br.num` mechanism → 26 literal `q` | 0 FAIL, exit 0 | **2 FAIL, exit 1** (`rel` gate + check 6 undeclared-mismatch fallback) | now FAILs |
| **P2** F2 false-but-plausible | `` `Cited.numerator` `` → `` `Cited.maskNorm_pos` `` on `SE.br` | 0 FAIL | 0 FAIL | by-design residual, **disclosed** |
| **P3** F3 import across mechanized intermediate | `import SE.denom` in `goal.lean` + well-formed `import-not-child` | 0 FAIL, exit 0 | **1 FAIL, exit 1** (`skipped: ['SE.br']`) | now FAILs |
| **P4** F4 un-imported mechanized premise | comment out `import SE.denom` in `br.lean` + declaration | 0 FAIL, exit 0 | **1 FAIL, exit 1** | now FAILs |
| **P5** F5 REFUTED silences check 5 | `SE.jz` → `REFUTED`, delete its `route-not-formalized` | 0 FAIL | 0 FAIL | by-design residual, **disclosed** |
| **P6** F6 `sync_state` over-read | none possible | 0 FAIL | 0 FAIL + `INFO [3]` disclosure printed | by-design residual, **disclosed** |

No probe passes *silently*: P2/P5/P6 each produce a gated INFO line and/or a docstring sentinel that three selftest fixtures fail if deleted. My FAIL counts and messages match `21_probes_AFTER.txt` byte-for-byte in substance. **No blocking finding in V1.**

## V2 — five probes of my own (two find new soft spots)

| probe | what it attacks | result |
|---|---|---|
| **NEW-1** | Is the F1 anchor gate substance or syntax? Mechanism = `` `q` `q` `q` `q` `q` `q` `q` `q` `` — exactly 24 non-space chars, 8 words, 8 backtick anchors | **0 FAIL, exit 0 — PASSES.** New soft spot (fix R2) |
| **NEW-2** | Import a great-grandchild (`trace.t6`) into `denom.lean` with a well-formed declaration | **1 FAIL** — the union-over-paths logic finds the mechanized intermediate `tame`. Checker survives; the F3 fix is genuinely path-complete, not one-path |
| **NEW-3** | Subject/mechanism incoherence: retarget a real `import-not-child` onto another real non-child import | **2 FAIL** (duplicate + undeclared). Checker survives |
| **NEW-4** | Launder a **meaning** change with a fully self-consistent re-sync: narrow `SE.br`'s claim to `n ≥ 10^6`, then update `claim_hash`, `source_claim_hash`, the module's FROZEN CLAIM text **and** its header digest | **0 FAIL, exit 0 — PASSES.** New soft spot (fix R4) |
| **NEW-5** | Declare and perform an `import-not-child` for a node reachable only across a **§4-DISABLED** route (`trace.r1`, REFUTED/DEAD) | **0 FAIL, exit 0 — PASSES.** New soft spot (fix R3); latent only, no live instance today |

## V3 — no weakening

Mechanical section-by-section comparison of `run_checks` against `9f92ff8`:

- **byte-identical:** checks 1, 2, 3/3b, 4, 5, 7a/7b, 7c, the §7.4 silence check, and the `run_checks` preamble.
- **changed, additive only:** check 6 **+28/−0** lines; the declaration-parsing section **+17/−0**. `parse_rel_declarations` keeps the original `MIN_MECHANISM_CHARS` condition verbatim and *adds* two more into a `deficits` list — strictly stricter. `drift_note` change is message text only (appends the F6 clarifier).
- **severity census:** `rep.fail` 39 → **41** (check 6: 6 → 8); `rep.warn` **15 → 15**; `rep.info` 5 → 7. **No FAIL removed, no severity lowered, no output suppressed.**
- **F1 margin on the real tree, measured by me** (26 declarations parsed): minima **110 non-space chars** (gate 24), **21 words** (gate 4), **≥1 anchor** (gate 1); 0 declarations fail. Smallest-char row is `SE.denom → SE.denom.Y` (anchor `` `Cited.y_bound` ``); smallest-word rows are the 21-word `familysplit`/`gram.interface`/`omega.interface`/`t6` entries. Margins of 4.6× and 5.25× — admitted **for the right reason**, not by accident.
- **fixture honesty:** the pre-existing `v6_import_mismatch*` fixtures were re-pointed at an *unmechanized* child (the case §1 actually licenses) and the old scenario is now covered by a new fixture that must FAIL, plus a **negative control** (`v6_import_not_child_unmechanized` must NOT fail). Stricter, not looser.
- **other trees:** whgap old-tool vs new-tool output **byte-identical**, 0 FAIL / 2 WARN. ksum **22 FAIL → 22 FAIL**, zero `(check,node)` pairs lost or gained; the only line-level delta is the appended F6 clarifier inside 8 `drift_note` messages, plus 2 → 3 INFO. The executor's disclosure is exact.

## V4 — task-008 / task-010, re-derived independently

**ω tightness, from scratch.** I did not use `se_hook_definition_crosscheck.py`. I computed ω from the **branching rule** — ω = Σ_{corners c of θ} f^{(q−j,θ−c)} / f^{(q−j−1,θ)}, with f^λ from the hook-length formula — over the whole window `1 ≤ j`, `6j ≤ q`, `q ≤ 90`: **11 219 triples, 0 range violations.**

- **Upper bound attained: YES**, 85 cases, every one at `j = 1`, `θ = (1)`, where ω = 1/(q−2) = j/(q−2j) **exactly** (checked symbolically: f^{(q−1,1)} = q−1, f^{(q−2,1)} = q−2 ⇒ p₀ = (q−2)/(q−1) ⇒ ω = 1/(q−2)).
- **Lower bound `j/q` attained: 0 cases.** Closest approach ω/(j/q) = **45/44** at q = 90, j = 1. The task-008 wording is **TRUE**.
- Their 1782-check sweep is a strict subset of mine (q ≤ 60); I confirm it and extend it.
- Nuance behind fix R6: the ratio at j = 1 is exactly q/(q−2) → 1, so the lower bound is never attained but **asymptotically sharp**; "SAFE BUT LOOSE floor" reads as quantitatively loose, which it is not.
- Scope note in the executor's favour: the tightness discussion is **comment only**; the Lean theorem proves the two-sided range, so no wording here can affect soundness.

**Comment-only proof, reproduced.** With block and line comments stripped, `SE/Support/Omega.lean`, `SE/Trust.lean` and `SE/denom/taper.lean` are **byte-identical to HEAD** (raw bytes differ, as expected). `goal.lean`, `Interface.lean`, `SelfTest.lean`, `Support/Defs.lean`, `Support/Constants.lean` are byte-identical to HEAD. The linter warning moving `taper.lean:132 → :137` is itself corroboration of a 5-line comment insertion.

**task-010(a), judged independently.** Recovered `git:f0d686a:se/proof-dag/nodes/SE.denom.taper.yaml` (v5 `claim.statement`, len 100) and ran difflib against the current claim (len 91): **exactly one non-equal opcode, deletion of `" [PROVED]"` at offset 14.** `sha256(v5) = a79e1c59…` (the digest formerly in the module header), `sha256(v6) = d181c0bd… = claim_hash = source_claim_hash`, and `taper.lean` now carries **exactly one** 64-hex digest. **I independently reach the same judgement: WORDING ONLY** — `[PROVED]` inside a claim is what DAG_PROTOCOL §6.1 forbids; no proposition changed, so `taper.Claim` needed no restatement.

**task-010(b), judged independently.** I count **15** check-4 WARNs (and 2 check-7c), confirming the executor's corrected count against the task text's 16. Check 4 is byte-identical to HEAD and self-labels as a textual approximation; a premise arriving as an `Interface.Cited` field has no child name to find, so WARN is the correct severity and no textual patch would be honest. Registering the real work as `task-012` instead of closing it silently is what §6.8 requires. **I agree with the call.**

## V5 — my own clean rebuild, census, regression

- Deleted every SE build product (`.lake/build/lib/lean/SE*`, `.lake/build/ir/SE`) — verified the directory was empty, so nothing was "Replayed" — then `lake build SE`: **exit 0, 3061 jobs, 57.8 s wall.**
- `#print axioms`: **124 declarations, 124/124 exactly `[propext, Classical.choice, Quot.sound]`**, zero non-standard, `sorryAx` absent. One cosmetic linter warning (`taper.lean:137: try 'simp' instead of 'simpa'`).
- Zero `sorry`, zero `axiom`, zero `native_decide` — every grep hit in the tree is inside a comment.
- **`goal.Claim` unchanged**: `goal.lean` byte-identical to HEAD; still `Tendsto (epsB rhoConst) atTop (𝓝 0) ∧ ∀ n ≥ 27, (Cconst − epsB rhoConst n)·n^(1/3) ≤ F.adv n`.
- **ksum / whgap not regressed** (numbers in V3).
- Evidence ledger `se/artifacts/logs_se_frontier_20260817/SHA256SUMS.txt`: **22/22 entries verify** over LF-normalized bytes, 0 mismatched, 0 missing; 23 files on disk = 22 + the ledger.

## V6 — protocol

- `proof_dag_check.py --problem se --verify-git` → **exit 0**, 84 node files valid. `--problem ksum --verify-git` → exit 0, 142 nodes.
- `literature_check.py` → exit 0 (52 papers, 5 libraries). `check_event_append_only.py --base-ref HEAD` → **exit 0**.
- `lean_dag_check.py --problem se` → exit 0; `--selftest` → 23/23.
- **Levels unchanged:** I diffed all 84 node levels and every route level against HEAD — **NONE** changed. Nothing was promoted.
- **Generated views fresh:** regenerating `NODE_INDEX.md` and `GRAPH.mmd` in a scratch copy reproduces both **byte-for-byte**.
- **Events append-only:** confirmed; three new events (`task011-…`, `task008-…`, `task010-…`) plus `taper-source-hash-aligned-…`, no existing event edited or deleted.
- Frontier hygiene: task-008/010/011 removed, task-012/013 registered with dated `since` — §6.8 satisfied. One gap, fix R5.

## FIXES (none blocking; R1, R3, R5 are the ones I would gate the next promotion on)

- **R1 — "two independent exact-rational sweeps" is FALSE.** `se/artifacts/logs_se_lean_t2b_20260817/definition_crosscheck.txt` and `se/artifacts/logs_se_frontier_20260817/30_hook_definition_crosscheck_rerun.txt` are **byte-identical transcripts of the same deterministic script**, and "1782 range checks" and "the 35183-check run" are two counts *from that same run* (16530+379+1782+16492 = 35183). Re-running a deterministic script proves reproducibility, not independence. Appears in `SE/Support/Omega.lean`'s header, `SE/Trust.lean` §C, the node's `task008-wording-applied-2026-08-17` event, and `assessment.summary`. The underlying fact is TRUE; only the epistemic label is wrong. My branching-rule sweep (q ≤ 90, 11 219 triples, independent implementation) **is** a genuine second sweep and agrees — cite it, or say "one exact-rational sweep, re-run and reproduced".
- **R2 — the F1 gate is a syntax tax, not a substance gate.** Probe NEW-1: `` `q` `q` `q` `q` `q` `q` `q` `q` `` clears all three conditions (24 chars / 8 words / 8 anchors) at **0 FAIL**. The hardening is a real improvement against *accidental* junk and against the exact 26-`q` probe, but the executor's headline "F1 junk mechanism … now FAIL" should be scoped: junk of that specific shape fails; adversarial junk still passes, which is F2 restated. Fold NEW-1 into the F2 disclosure rather than pretending F1 closed it.
- **R3 — NEW soft spot: the `import-not-child` descendancy licence counts paths through §4-DISABLED routes.** `descendants_of()` walks all route premises without consulting `route_disabled_reason()`, so probe NEW-5 (import `SE.denom.Phi.legal.trace.r1`, a REFUTED/DEAD node reachable only across a disabled route, with a well-formed declaration) passes at **0 FAIL**. There is no live instance today (Lean would also refuse the missing module), but the same predicate the tool already factored out for checks 5/7c should gate this licence, or the check should FAIL when the imported subject is `REFUTED`. Cheap, and exactly the class of drift check 6 exists to catch.
- **R4 — NEW soft spot (and a scope statement the node should carry): a MEANING change is invisible when re-synced consistently.** Probe NEW-4 narrows `SE.br`'s claim to `n ≥ 10^6` and updates `claim_hash`, `source_claim_hash`, the module's quoted claim and its header digest — **0 FAIL**. Nothing in `lean_dag_check.py` anchors a claim to git. Consequence worth writing down beside the F6 disclosure: the Class-A and task-010(a) "wording only" judgements rest entirely on a **human** comparison against `git:f0d686a`, not on any checker. Setting `source_claim_hash := claim_hash` (correct per `drift_note`'s definition) is precisely what removes the machine-readable pointer to the prior text; history survives only because the v5 digest was moved into the node event.
- **R5 — the four shadow nodes gained a caveat with NO event.** `SE.denom.Phi.legal.gram.interface`, `…omega.interface`, `…sect`, `…tame` each went 1→2 (tame 2→3) caveats with **zero new events**, while `SE.denom.taper` in the same session correctly received `taper-source-hash-aligned-2026-08-17`. DAG_PROTOCOL §5.6 / FILE_PROTOCOL §6.4 want repairs to caveats logged, and §6's node-level audit premise ("start from one node") breaks: an auditor at `sect` sees new text with no dated event or source on that node. Fix: append a dated `repair-applied` event to each of the four citing `se/artifacts/se_frontier_20260817.md`. (The caveats themselves are TRUE — I verified `sect`'s Lean `Claim` is only the ≤ direction on the re-scoped window.)
- **R6 — "SAFE BUT LOOSE floor" understates the lower bound.** It is never attained but asymptotically sharp: ω/(j/q) = q/(q−2) at j = 1, minimum 45/44 ≈ 1.023 at q = 90. Reword to "attained nowhere, though asymptotically sharp; only its positivity is load-bearing".
- **R7 — self-report imprecision (artifact is correct).** "smallest: 110 chars, 21 words, anchor `` `Cited.mask_from_D` ``" conflates two different declarations: 110 chars is `SE.denom → SE.denom.Y` (anchor `` `Cited.y_bound` ``); 21 words is `familysplit` and three others. `23_declaration_audit.txt` reports both correctly.
- **R8 — standing reproducibility hole, now broader.** `tools/lean_dag_check.py` is uncommitted (`M`) and `tools/proof_dag_v6.py`, `tools/check_event_append_only.py`, `tools/migrate_node_schema_v6.py` are **untracked**, so HEAD cannot run its own documented closeout and **cannot reproduce this verdict**. Flagged by the previous review; it now covers the hardened checker too. Not this session's doing; it will bite the next reviewer.
- **R9 — probe log ordering.** `21_probes_AFTER.txt` reports 18 WARN throughout, i.e. the probes were executed *before* the task-010(a) taper fix took the tree to 17 WARN. I re-ran all six against the final tree and obtained the same FAIL sets, so nothing is wrong — but the log should be regenerated or annotated so the counts reconcile with `14_lean_dag_check_se_after.txt`.

## Level judgement

Nothing in this session's frontier clearance changes what `SE.formal.t2` may claim: it is checker hardening, comment wording, and one bookkeeping re-sync. **CERTIFIED\* remains licensed and PROVED remains withheld**, for the unchanged reason — the discharge rests on the cited Frame–Robinson–Thrall hook-length formula, absent from Mathlib v4.31.0. My evidence licenses `NUMERICAL` for the mechanized parts I reproduced; I wrote no level.

Files most relevant to a re-audit (absolute paths): `<machine-local-path-redacted>`, `.../se/artifacts/se_frontier_20260817.md`, `.../se/artifacts/logs_se_frontier_20260817/`, `.../se/artifacts/se_task006_review_20260817.md`, `.../se/proof-dag/nodes/SE.formal.t2.yaml`, `.../se/proof-dag/nodes/SE.denom.taper.yaml`, the four shadow nodes `.../se/proof-dag/nodes/SE.denom.Phi.legal.{gram.interface,omega.interface,sect,tame}.yaml`, and `.../se/lean/SE/{Support/Omega.lean,Trust.lean,denom/taper.lean}`. My probe harness and ω re-derivation are at `<machine-local-path-redacted>}` (scratchpad only; nothing was written into the repository).
