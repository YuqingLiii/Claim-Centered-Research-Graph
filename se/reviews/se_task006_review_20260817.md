# task-006 clearance (12 lean_dag_check FAILs → 0) — independent review

> **Provenance.** Date 2026-08-17. Reviewer: fresh Claude Opus 5 subagent, non-author (authored no
> commit, node, Lean file, artifact or tool edit under review; given no wanted outcome; wrote nothing
> into the repository — every mutation was made in throwaway scratchpad copies). Commission:
> coordination layer, workflow `wf_67f8daa7-fac`, phase "Audit"; it discharges frontier `task-009`.
> The commission's central question was whether any FAIL had been cleared by weakening the checker
> instead of fixing the underlying fact. Archived VERBATIM by the coordination layer.

---

PRE-ACTION REPORT (as required by `research/PRETASK_RELOAD_PROMPT.md`)

- Read completely, in order: `DAG_PROTOCOL.md` (schema v6, all 8 sections), `FILE_PROTOCOL.md`, `se/README.md`, `se/proof-dag/NODE_INDEX.md`, then `se/proof-dag/nodes/SE.formal.t2.yaml` and every node it touches.
- Target node: `SE.formal.t2`, read from disk as **level `CERTIFIED*`**, role `tool`, with `frontier.task-009` already open and describing exactly this review (it names the three attacks: Class-A byte judgement, the 26 `lean.rel` declarations, the two `lean_dag_check.py` edits).
- ROLE: **reviewer**. Independence: I authored none of the reviewed work (no commit, node, Lean file, artifact or tool edit under review is mine), I was given no wanted outcome, and I wrote nothing into the repository — every mutation in this review was made in throwaway copies under my scratchpad.
- Highest LEVEL my evidence could license per §3: `NUMERICAL` for the mechanized parts (reproduced build + checker runs). As an independent reviewer my report may *license* a completion tier for others to write; I write no level myself.
- Gates/deliverables (one line each): V1 tool-diff adversarial re-test; V2 Class-A honesty (claim vs `Claim : Prop`); V3 truth/specificity of Class-B/C declarations; V4 own clean rebuild + axiom census; V5 regression on `goal.Claim`/`Cited`/SelfTest; V6 protocol validators, generated views, ksum/whgap unchanged.
- Conflict between commission text and disk: **none.** The v6-refreshed PRETASK template matches the disk (v6 has no numbered "hard rules" list, `sync_state`/`source_claim_hash` are real `LEAN_KEYS`, `lean_dag_check.py` is not required to exit 0). One item to report per the template's own instruction: the executor's own declared commission/disk conflict (`SE.denom.taper`'s `source_claim_hash` residual) is real and still on disk, correctly left for its owner as `frontier.task-010(a)`.

---

# VERDICT: PASS-WITH-FIXES — no blocking defect

The single most important question — **was any FAIL cleared by weakening the checker rather than by fixing the underlying fact?** — answer: **NO.** I established this with a 2×2 cross-matrix that the executor did not run, comparing both tool versions against both trees (HEAD = `5a92115`, working tree = the work under review):

| | HEAD tree | working tree |
|---|---|---|
| **HEAD tool** | 12 FAIL / 25 WARN / 1 INFO, exit 1 | 5 FAIL / 18 WARN / 1 INFO, exit 1 |
| **new tool** | **12 FAIL** / 25 WARN / 2 INFO, exit 1 | 0 FAIL / 18 WARN / 7 INFO, exit 0 |

The decisive cell is the top-right→bottom-left pair: **the tool edit applied to the un-fixed tree clears zero FAILs (12 → 12).** Seven FAILs are cleared by data alone (old tool on new tree: 12 → 5). The remaining five are cleared jointly by the declaration channel plus the tool edit — i.e. the edit is load-bearing for those five, which is why V1 and V3 below carry the weight of this verdict.

Note for the record: my true BEFORE reproduction required a full HEAD snapshot, because `src_of()` resolves Lean modules through `root / node.lean.file` and ignores `--lean-dir`; running the old tool with `--nodes-dir/--lean-dir` alone silently reads the *current* modules and under-reports check 3 (5 FAIL instead of 12). Anyone re-verifying must use `--root` on a full tree.

## V1 TOOL DIFF — every edit re-tested adversarially

`git diff tools/lean_dag_check.py` = 398 insertions. Scope audit: I extracted and compared the bodies of every check between HEAD and the working tree. **Checks 1, 2, 3, 3b, 4, 7a, 7b, 7c and the §7.4 silence check are byte-identical.** Only check 5, check 6, and a new check id `rel` (severity FAIL) exist as changes, plus fixtures/docstring. No severity was lowered for undeclared drift; no output was suppressed. `route_disabled_reason()` is a genuine factoring of the predicate check 7c *already* applied (I diffed 7c and confirmed it contained the same REFUTED-implication/REFUTED-premise exclusion before the edit), so justification (b) in the executor's §2 is accurate, not ad hoc.

Adversarial tests, all against a scratch copy of the **real** SE tree (not the synthetic fixtures), repo never touched:

**(a) undeclared import mismatch — still FAILs.** Three variants:
- delete the single `premise-not-imported: SE.br.num` entry → `1 FAIL, exit 1`: `FAIL [6] SE.br: ... UNDECLARED children not imported: ['SE.br.num (no formal mirror)']`
- add a real new premise to `SE.br`'s live route, declare nothing → `3 FAIL, exit 1` (the mismatch plus two false-declaration FAILs)
- import `SE.goal` from `br.lean` (an ancestor) and declare it `import-not-child` with a well-formed 100-char mechanism → `1 FAIL, exit 1`: the descendant rule fires.

**(b) silently dropped formalized route — still FAILs.** Four variants:
- rename route `SE.br`→`SE.brX` on the node, keep `composition_via_br` → `2 FAIL` (new "correspond to no live routes — a renamed or silently dropped route", plus undeclared unrendered route)
- rename the theorem (`theorem composition_via_br` → `..._brZZ`), node untouched → `4 FAIL` across checks 1, 5, 5, 7a
- delete the whole `br` route block from the node, theorem stays → `2 FAIL` (checks 5 and 6)
- declare `route-not-formalized: SE.br` while `composition_via_br` exists → `1 FAIL` (false record).

**(c) docstring digest that does not match a claim — still FAILs.** Three variants:
- append a real strengthening ("the constant may be taken to be 1") to `SE.goal`'s claim, leave both hashes intact → `2 FAIL [3]`
- corrupt the 64-hex digest in `goal.lean`'s docstring → `1 FAIL [3]`
- edit the claim **and** recompute the node's `claim_hash`, leaving the module stale → `1 FAIL [3]`.

All three targets are still caught. **No check can any longer fail to catch its target**, so no V1 FAIL verdict. Fixes F1–F5 below are residual holes I found beyond the three required tests.

## V2 CLASS A HONESTY — confirmed, and confirmed independently

I did not take the executor's word or their `40_classA_wording_proof.txt`. I recomputed from `git:f0d686a` (v5 records were `*.yaml` with `claim.statement`, not `*.md`):

- For all **7/7** nodes: deleting the first ` [<LEVEL>]` from the v5 statement yields the v6 claim **byte for byte**. Tokens recovered independently and they match the executor's table exactly (`[OPEN]` ×5 for `br`, `denom`, `sect`, `tame`, `goal`; `[CONJECTURED]` ×2 for `gram.interface` (H2), `omega.interface` (H3)).
- `sha256(v5 text) == source_claim_hash` recorded at HEAD: **7/7 True**.
- HEAD module frozen-claim body `==` v5 text: **6/7**; the one exception is `omega.interface`, differing in exactly the line the executor disclosed unprompted (`belong to the PARENT node` vs `belong to the consuming node`). Their disclosure is accurate and the repair is correct.
- Current module frozen body `==` current node claim: **7/7**. Recorded `claim_hash == sha256(current claim)`: **7/7**.
- No `Claim : Prop` was restated: `goal.Claim` is byte-identical to HEAD; `Interface.lean` and `SelfTest.lean` have a **0-line** diff vs HEAD.

My own meaning judgment, node by node, against the Lean `Claim : Prop`:

- `SE.goal` — node claim `Adv± ≥ ‖Γ‖/max‖Γ∘Δ_i‖ = Ω(n^{1/3})`; Lean `Tendsto (epsB rhoConst) atTop (𝓝 0) ∧ ∀ n ≥ 27, (Cconst − epsB rhoConst n)·n^{1/3} ≤ F.adv n`. Faithful and explicit. **Same meaning.**
- `SE.denom` — `max_i ‖Γ∘Δ_i‖ = O(1)`; Lean `∀ n ≥ 27, maskNorm n ≤ 2·envBound rhoConst n`. Faithful quantitative rendering. **Same.**
- `SE.br` — the claim is a *scope label* ("Branch A: BR tapered witness restricted to legal q=2n (AND)"), not a proposition; the mathematics is in the route implication and in `br.Claim` (`K n /(2·envBound) ≤ gammaNorm/maskNorm`). Nothing was papered over, but see F6.
- `gram.interface` (H2) — node claim is the **typed, Schur-lifted operator identity** with the `I_{V_κ⊗V_ν}` lift and "no lost factor c"; Lean `Claim` is the **scalar shadow** `gcanS = rtopS/(btheS²·omegaS)·mxiS`. The module's own header says so explicitly and names what is lost ("the Schur lift … is INVISIBLE in this shadow … a MIS-TYPED H2 would therefore NOT be caught").
- `omega.interface` (H3) — node claim asserts the **exact sandwich equality**; Lean part (i) is the **inequality** `csectS² ≤ cnprobS · gcanS`. Declared in-module as "an INEQUALITY, weaker than the frozen identity … the implication runs the safe way".
- `sect` (H4) — node claim is the **exhaustive orthogonal decomposition ⇒ ‖C‖ = max‖C̃‖ uniformly for c ≥ 1**; Lean `Claim` is only the ≤ direction on the re-scoped window. Declared: "'orthogonal, exhaustive, no residual sectors' degenerates to that one-directional bound … the missing-sector failure mode survives this development untouched".
- `tame` — node claim is a status line (refuted 1(a) + three OPEN routes); Lean `Claim` is the uniform-O(1) reading `cLower ≤ √(15/8)·ρ_j·√(j/(n−j))` on `1 ≤ j`, `3j ≤ n`, `j < K−1`. Declared in-module as a place where "the Lean statement must differ in FORM from the frozen prose".

**Judgment: no re-sync papered over a meaning change.** Every node↔Lean divergence above is an admitted tier-1 shadow, loudly declared *in the module*, present unchanged at `f0d686a`, and untouched by this session. V2 = PASS. The one thing worth a fix is where those declarations are *not* repeated (F6).

## V3 CLASS B/C DECLARATIONS — specific and true, with two soft findings

26 declarations parsed by the tool (`rel: 26` in coverage), inside 39 total `rel` entries. I checked every one against the graph, the modules and `Interface.lean`, not just for well-formedness:

- **Every "carries no formalization block" assertion is true.** Verified for `SE.denom.Phi`, `Phi.legal`, `trace`, `gram`, `omega`, `found`, `jz`, `mdh`, `sdp`, `ros`, `goal.hyp.se-jz.01` — all `formalization` absent.
- **Every `Cited.<field>` named exists and carries the right content.** `SE.br.num` → `numerator : ∀ n, (K n:ℝ) ≤ F.gammaNorm n` is exactly `‖Γ‖ ≥ K`. `SE.denom.X` → `x_bound` exact. `SE.denom.Y` → `y_bound : yNorm ≤ rho·(√2·√(d/n))` matches the node's `ρ √2 √(k/n)` exactly. `crossk` → `defect_orth`, and the declaration's own hedge ("only the ≤ half is used") matches the field's docstring verbatim. `Phi` → `cDiag_bound`/`cDiag_zero`/`cLower_zero` (matched-defect half) + `tame.Claim` (open half) — correct split.
- **Every `route-not-formalized` reason is true.** `SE.jz`, `SE.mdh`, `SE.sdp`, `SE.ros` all have no `proof:` key on the route (verified from the YAML); `SE.jz`'s route really does carry the second premise `SE.goal.hyp.se-jz.01`, whose node claim really is the unproved multiplicative→additive transfer.
- **`SE.denom.assembly` → `SE/Support/Envelope.lean`**: `denom.lean` really imports `SE.Support.Envelope`.
- **No blanket text, no wildcards, no duplicates, one subject per entry.** The four longest are 200+ characters of specific mechanism. This is the opposite of boilerplate.

Two soft findings, folded into F8 below: `Cited.block_triangle` and `Cited.mask_from_D` are the only two named fields whose own docstrings cite paper equations but **no node**, while the other five (`numerator`, `maskNorm_pos`, `x_bound`, `y_bound`, `cDiag_bound`) carry explicit node attributions. The `decomp → block_triangle` and `familysplit → mask_from_D` mappings are therefore the executor's defensible interpretation rather than a labelled correspondence.

## V4 BUILD + CENSUS — my own clean rebuild

I deleted every SE build product (`.lake/build/lib/lean/SE*`, `.lake/build/ir/SE*`) and ran `lake build SE`:

- **exit 0, 3061 jobs** (matches the report's count exactly). One cosmetic linter warning only: `SE/denom/taper.lean:132: try 'simp' instead of 'simpa'`.
- **`#print axioms`: 124 declarations, 124/124 exactly `[propext, Classical.choice, Quot.sound]`**, zero non-standard axioms, `sorryAx` absent from the log. (My regex first matched 121 — the three missing are `SE.prod_Ico_ratio'`, `SE.prod_range_ratio'`, `SE.sq_alpha_mul_le'`, whose primes broke the pattern; a `grep -c` on the raw lines confirms 124 emitted and 124 exactly-three.)
- Census includes everything required: **`SE.goal.composition_via_br`**, `SE.br.composition`, `SE.denom.composition`, `SE.denom.Phi.legal.tame.composition`, plus 34 `SelfTest` declarations.
- **Zero `sorry`, zero `axiom` declarations, zero `native_decide`** — every grep hit in the tree is inside a comment.

## V5 REGRESSION — clean

- **`goal.Claim` unchanged**: byte-identical to HEAD. Against tier-1 `f0d686a` it differs only by `F.rhoConst → SE.rhoConst`, the already-reviewed tier-2a change. **Same constant** `SE.Cconst = 9/(18+4√6+3√10)` (untouched `Support/Constants.lean`), **same range** `27 ≤ n`.
- **Surviving `Cited` fields unchanged**: `SE/Interface.lean` diff vs HEAD is **0 lines**. This session did not touch the trust interface at all.
- **The three SelfTest models**: `SE/SelfTest.lean` diff vs HEAD is **0 lines**; `emptySectorFrame_cited`, `liveSectorFrame_cited`, `channelFrame_cited` all rebuild and are all axiom-clean; `hypotheses_consistent` still exhibits `Cited ∧ H1 ∧ H2 ∧ H3 ∧ H4`. Non-vacuity is genuine, not degenerate: `liveSectorFrame` has admissible sectors at every `(n,j)` with `1 ≤ j ∧ 3j ≤ n`, and `defect_orth` is deliberately scoped `1 ≤ n` precisely to prevent the vacuous-premise collapse the interface docstring warns about.

## V6 PROTOCOL

- `python3 tools/proof_dag_check.py --problem se --verify-git` → **exit 0**, "84 node files structurally valid".
- `python3 tools/literature_check.py` → **exit 0** (52 papers, 5 libraries).
- `python3 tools/check_event_append_only.py --base-ref HEAD` → **exit 0**. **No node or route level changed anywhere**: I diffed all 84 node levels and every route level against HEAD — `NONE`. Nothing was promoted.
- **Generated views fresh**: regenerating `NODE_INDEX.md` and `GRAPH.mmd` in a scratch copy reproduces the on-disk files byte-for-byte, and both are also unmodified vs HEAD (levels didn't change, so the index shouldn't).
- `python3 tools/lean_dag_check.py --problem se` → **exit 0**, full summary `0 FAIL, 18 WARN, 7 INFO`; coverage `1:9 2:18 3:9 4:3 5:1 6:9 7a:9 7b:5 7c:16 rel:26 nodes:84 mechanized:9 lean-none:75`. `--selftest` → **16/16 assertions passed**, `0 FAIL, 0 WARN, 3 INFO`.
- **whgap**: old tool vs new tool, both `--root` the repo → output **byte-identical**, `0 FAIL, 2 WARN, exit 0`. Unchanged.
- **ksum**: **21 FAIL → 22 FAIL** (17 WARN both, 1 → 2 INFO). I diffed the FAIL sets: **the "OLD-only" set is empty of anything genuinely lost** — each of the 5 old lines has a 1:1 reworded NEW counterpart; the extra is the new `FAIL [5] KSUM.B1: composition_via_* theorem(s) ['A1','A1_inputs'] correspond to no live routes of this node — a renamed or silently dropped route`. **No ksum FAIL disappeared; the tool got strictly stricter on ksum.** The executor's disclosure is exact.
- **ksum side effect verified, not just accepted**: `find research -newermt '2026-08-17 16:20'` lists exactly two ksum paths, `proof-dag/NODE_INDEX.md` and `proof-dag/GRAPH.mmd`, and **no ksum node file**; regenerating both from the unchanged ksum node files reproduces them byte-for-byte (idempotent). The many other `M ksum/...` entries in `git status` predate 16:20 and belong to the earlier uncommitted v6 migration, not this session.
- **Evidence ledger**: `se/artifacts/logs_se_task006_20260817/SHA256SUMS.txt` — I verified **38/38 entries, 0 mismatched, 0 missing** over LF-normalized bytes.

## True counts I measure myself

| run | FAIL | WARN | INFO | exit |
|---|---|---|---|---|
| `lean_dag_check.py --problem se` BEFORE (HEAD tool, HEAD tree) | **12** | 25 | 1 | 1 |
| `lean_dag_check.py --problem se` AFTER (working tree) | **0** | 18 | 7 | 0 |
| `--selftest` | 16/16 | — | 3 | 0 |

All of the executor's headline numbers reproduce: 12→0 FAIL, 25→18 WARN, 1→7 INFO, 8/8→16/16 selftest, 3061 jobs, 124/124 axiom-clean, whgap identical, ksum 21→22.

## FIXES (none blocking; F1, F3, F4 are the ones I'd gate the next promotion on)

- **F1 — `MIN_MECHANISM_CHARS = 24` is a pure length gate, and junk clears it.** I replaced `SE.br.num`'s real mechanism with 26 literal `q` characters: **0 FAIL, exit 0**. The tool's own docstring promises "a substantive mechanism"; length alone does not deliver that. Fix: additionally require e.g. ≥ 4 words *and* at least one backticked identifier, node id, or ruling reference — every one of the 26 real declarations would still pass.
- **F2 — a plausible but FALSE mechanism naming a *real* field passes.** Substituting `Cited.maskNorm_pos` for `Cited.numerator` on `SE.br.num`: **0 FAIL**. The tool checks field *existence*, never *relevance*. This is disclosed honestly in the tool and in report §4, and it is exactly why `SE.formal.t2 frontier task-009` exists; I have now discharged that obligation for all 26 (V3 above). Keep it a standing review obligation, and record in the node that it was checked by this review.
- **F3 — `import-not-child` requires only DAG descendancy, not that the skipped intermediates are unmechanized.** Adding `import SE.denom` to `goal.lean` (a descendant reached across the **mechanized** node `SE.br`) with a well-formed declaration: **0 FAIL**, where HEAD FAILed. All four real declarations actually assert the stronger property ("neither of which carries a formalization block"), so tighten the check to match the prose: every skipped intermediate must lack a `formalization` block.
- **F4 — `premise-not-imported` accepts a *mechanized* child.** Commenting out `import SE.denom` in `br.lean` plus one declaration: **0 FAIL**, where HEAD FAILed. Mitigated in practice because Lean itself refuses to elaborate a composition whose `Claim` parameter's module is absent (so V4 is the real backstop) — but the checker should not be silent. Fix: FAIL when an un-imported premise *has* a `formalization` block, since then a module demonstrably exists to import.
- **F5 — the §4 disabled-route exemption is a laundering path worth naming.** Setting `SE.jz` to `REFUTED` and deleting its `route-not-formalized` entry silences check 5's rendering obligation entirely: **0 FAIL**. This is correct per §4, matches check 7c's pre-existing predicate, and is reported as INFO rather than hidden; a `REFUTED` write is separately policed by the append-only checker and `proof_dag_check`. Fix is documentation only: name this consequence in the tool docstring so no future session discovers it as a trick.
- **F6 — `sync_state: current` over-reads on four nodes.** For `gram.interface`, `omega.interface`, `sect` and `tame`, `current` means "the module quotes the current claim text and the digests agree", **not** "the Lean `Claim : Prop` expresses the node claim" — which DAG_PROTOCOL §7's wording ("until the formal statement, imports, proof, and hash are synchronized") invites a reader to assume. The *modules* declare their shadows superbly; the *nodes* do not repeat it in the new sync caveat. Fix: one clause in each of those four `formalization` caveats, e.g. "synchronized at the level of the quoted claim text and digest; the Lean `Claim` is the declared tier-1 shadow (see module header)".
- **F7 — five nodes now have a completely empty `frontier`**, including the project goal `SE.goal`, because the discharged `resync-formalization` gate was the last entry. Not a protocol violation (§1 makes `frontier` optional, §6.8 only forbids finished work), but the goal node now advertises no actionable next step. Fix: restate the real next action on `SE.goal` (or point it at `SE.denom.Phi.legal.tame`).
- **F8 — add node attribution to `Cited.block_triangle` and `Cited.mask_from_D`** docstrings (the only two of the seven named fields lacking it), so the `decomp`/`familysplit` mappings stop being an interpretation the next reviewer must re-derive.
- **F9 — trivial:** the report says "verified all 37 SHA ledger entries"; the ledger has 38 and all 38 verify.

## Two things the next session should know that are not this executor's doing

- `src_of()` in `lean_dag_check.py` resolves modules through `root / node.lean.file` and **ignores `--lean-dir`**, so `--nodes-dir/--lean-dir` overrides silently mix a patched node set with the live modules (this is what makes checks 1/3/3b/4/7a unreliable under those flags). Anyone reproducing a "before" state must snapshot a full tree and use `--root`. Worth a `--lean-dir`-aware fix or an explicit warning.
- `tools/proof_dag_v6.py`, `tools/check_event_append_only.py` and `tools/migrate_node_schema_v6.py` are **untracked** (`??`) while `DAG_PROTOCOL.md` v6 and `FILE_PROTOCOL.md` §8 both depend on them, and `tools/proof_dag_check.py`'s v6 dispatch is uncommitted. The repository as committed at HEAD cannot run its own documented closeout. This is a scoped-commit miss from the migration session (the same failure mode as commit `57e2989`), not from task-006, but it will bite the next reviewer who tries to reproduce from a clean clone.

Files most relevant to a re-audit (absolute paths): `<machine-local-path-redacted>`, `.../se/artifacts/se_task006_20260817.md`, `.../se/artifacts/logs_se_task006_20260817/`, `.../se/proof-dag/nodes/SE.formal.t2.yaml`, and the seven re-synced nodes plus their modules under `.../se/lean/SE/`.
