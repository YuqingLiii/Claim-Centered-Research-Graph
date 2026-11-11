# WHGAP commission M7 — implement the §7.6 Lean↔DAG anti-drift checker (frozen 2026-07-30)

Commissioner: decision layer. Executor: ONE fresh Opus 5 instance. Node (rule 8a): the
obligation is registered on `WHGAP.goal` (Work record, LEAN-1.1 entry: "Residual
registered obligations: ... the §7.6 anti-drift checker implementation (R11 m7)").
Origin finding: R11 m7 (`artifacts/whgap_r11_lean_review_20260730.md`) — none of §7.6's
seven checks is implemented anywhere; the R11 MAJOR-2 drift (a `lean.state:
"composition-checked"` with NO composition theorem in the module) went uncaught.

**Mandatory first step:** `research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.goal`, ROLE = executor. Read
`research/DAG_PROTOCOL.md` §7.1 + §7.6 in full — the checker implements §7.6 verbatim.
Single-writer deviation binding: no node/index/DAG markdown edits.

**SCOPE DISCIPLINE (binding):** touch ONLY: the new tool `tools/lean_dag_check.py`, the
WHGAP proof-dag README run-line addition, WHGAP-scoped artifacts, and your report. Do NOT
touch `tools/proof_dag_check.py` (shared with live se/ksum sessions), and do NOT read or
validate the se/ksum trees this session (design the registry so they can self-register
later, but only `werner-holevo-gap` is enabled now).

## Deliverable: `tools/lean_dag_check.py --problem werner-holevo-gap`

Problem registry maps problem → (nodes dir, lean dir, module prefix, non-node modules =
{Interface, Support/*, Trust, SelfTest, Model}). Parse each node file's front matter
(`kind`, `children`, `status`) and its `## Lean` yaml block (`module`, `file`, `claim`,
`composition`, `state`, `rel`, `claim_hash`); `lean: none` nodes are exempt but must
carry a reason (WARN if bare).

The seven §7.6 checks — severity as assigned:

1. **[FAIL] Existence.** Declared module file exists; `def Claim` present; every theorem
   named in `composition` (string or list; ignore `null # ...` comments) exists as a
   `theorem <name>` in the file.
2. **[FAIL] Bijection.** Node-shaped .lean files under the lean dir (basename not in the
   non-node set) ↔ nodes with a `lean:` block, one-to-one, names matching.
3. **[FAIL] Hash triple-agreement.** Recompute the Claim hash with EXACTLY the
   normalization of `tools/whgap_lean_freeze_claims.py` (CRLF→LF; `## Claim` section body
   up to the next `## `; strip edge newlines; SHA-256 of UTF-8) and require
   recomputed == node `claim_hash` == the hex digest embedded in the Lean docstring.
4. **[WARN] AND coverage (textual approximation, say so in the output).** For AND-kind
   nodes: the composition theorem's source text references each child's Claim (module
   name appears in the hypothesis block); report missing/extra at WARN with the honest
   caveat that a full check needs elaboration.
5. **[FAIL] OR route match.** If a GOAL/OR node's module declares `composition_via_*`
   theorems, their suffix set must equal `children` exactly; if it instead uses a single
   AND-style `composition` (as WHGAP.goal does, per its prose composition block), accept
   and note it.
6. **[FAIL] Import graph = edges.** The node-module imports of each node module
   (imports with the module prefix, minus non-node modules) must equal that node's
   `children` set exactly.
7. **State backing + status arithmetic.**
   - **[FAIL] State-vs-content (the MAJOR-2 catcher):** every §7.1 token asserted in
     `state` must be backed — `stated` ⟹ Claim def exists; `composition-checked` ⟹
     `composition` non-null AND the named theorem(s) exist; `proved` ⟹ the declared
     composition/named theorems exist (or a `theorem holds`); `refuted` ⟹ `not_Claim`
     exists. Unknown tokens outside the §7.1 vocabulary (allowing parenthetical
     qualifiers) → FAIL.
   - **[FAIL] Rel display:** `composition-checked`/`proved` require the `rel` key present
     (empty list allowed only if the module's composition takes no extra hypothesis
     parameters beyond child Claims — if you cannot determine this textually, WARN).
   - **[WARN] Epistemic recomputation:** for AND nodes with a prose composition block,
     header status must not exceed min(composition status, child statuses) UNLESS the
     composition block's `rel` documents a scoped-input exception — print the rel text
     when invoking the exception.

## Regression self-test (the gate that proves the tool catches what R11 caught)

`--selftest` mode: build synthetic fixtures in a temp dir (never touching real trees)
and assert: (a) a `state: "composition-checked"` with no composition theorem → FAIL
(the MAJOR-2 class); (b) an edited Claim body with a stale hash → FAIL; (c) an import
not matching `children` → FAIL; (d) a clean fixture → exit 0. Self-test must exit 0
iff all four assertions hold.

## Gates

- **G-M7a:** `--selftest` passes (4/4 assertions).
- **G-M7b:** `--problem werner-holevo-gap` runs on the REAL tree and exits 0 (the tree
  was just brought into compliance; if you find a genuine violation, that is a FINDING —
  report it, do not silently fix the tree).
- **G-M7c:** temporarily reverting (IN MEMORY ONLY, e.g. by feeding the checker a
  patched copy of the P9 node with the old "composition-checked" state) reproduces the
  MAJOR-2 detection on the real module. Show the output in the report.

Artifacts: run + selftest logs under `artifacts/logs_whgap_m7_20260730/` (SHA256SUMS.txt,
LF); report `artifacts/whgap_m7_checker_20260730.md`; add the run line to
`channel-capacity/werner-holevo-gap/proof-dag/README.md`. Budget ≤ 60 min. Cap NUMERICAL.
Return {status, summary, selftest_pass, real_tree_pass, major2_detected, report_path}.

