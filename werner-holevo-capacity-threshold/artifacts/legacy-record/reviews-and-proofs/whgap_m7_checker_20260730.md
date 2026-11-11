# WHGAP M7 — the §7.6 Lean↔DAG anti-drift checker: implementation report

**Date:** 2026-07-30 · **Role:** executor (fresh Opus 5 instance) · **Node (rule 8a):**
`WHGAP.goal` (Work record, LEAN-1.1 residual obligation "the §7.6 anti-drift checker
implementation (R11 m7)") · **Commission:**
[`WHGAP_COMMISSION_M7_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_M7_20260730.md)
· **Origin finding:** R11 m7 ([`whgap_r11_lean_review_20260730.md`](whgap_r11_lean_review_20260730.md)).
**Evidence tier: NUMERICAL** (tool runs = command + log + SHA); this report is executor
self-authored and licenses no completion status (rule 6).

---

## PRE-ACTION REPORT

- **Target node / status as read from disk:** `WHGAP.goal`, `status: OPEN`
  (`status_source: "problem-scaffold-2026-07-28"`), GOAL, children
  `WHGAP.qpositive-onset`, `WHGAP.zero-capacity-application`, `WHGAP.onset-two-fifths`.
- **Role:** executor. No status was written by me; no node/index/DAG markdown was edited
  (single-writer deviation binding).
- **Highest status my evidence could license (§2):** NUMERICAL — this is tooling, i.e. runs
  with command + log + SHA-256. Writable by the proposer; a completion tier would need a
  fresh independent review. The tool's *verdicts* license nothing by themselves.
- **Gates:** G-M7a `--selftest` 4/4; G-M7b real WHGAP tree exits 0; G-M7c an in-memory
  patched copy of the P9 node reproduces the MAJOR-2 detection against the real module.
- **Deliverables:** `tools/lean_dag_check.py`; WHGAP `proof-dag/README.md` run line; logs
  under `artifacts/logs_whgap_m7_20260730/` (+ `SHA256SUMS.txt`, LF); this report.
- **Conflict between the commission text and the disk:** **ONE, material — see §6
  (FINDING M7-F1).** The commission's premise "none of §7.6's seven checks is implemented
  anywhere" is **no longer true on disk**: `tools/proof_dag_check.py` acquired a partial
  §7.6 checker in commit `b9fa96b` (the ksum Lean T3 session). Reported, not resolved: the
  same commission forbids me to touch that file.

---

## 1. What was built

`tools/lean_dag_check.py` — read-only (it never writes to any tree), stdlib-only, driven by
a problem registry:

```python
REGISTRY = {"werner-holevo-gap": ProblemSpec(..., enabled=True),
            "se":   ProblemSpec(..., enabled=False),
            "ksum": ProblemSpec(..., enabled=False)}
```

Only `werner-holevo-gap` is enabled, per scope discipline; `se`/`ksum` are registered with
their would-be paths and `enabled=False`, so a later session self-enables by flipping one
flag (a disabled problem exits 2 with an explanatory line — it is never silently "green").
Non-node modules are `{Interface, Trust, SelfTest, Model}` plus everything under
`Support/`, exactly the §7.6 set the commission names.

Per node the tool parses the YAML front matter (`id`, `kind`, `status`, `parents`,
`children`), the `## Lean` block (`module`, `file`, `claim`, `composition`, `state`, `rel`,
`tier`, `build`, `claim_hash`, `synced`), and — for the status arithmetic — the prose
`## Composition proof` block (`status`, `rel`). Guillemet module identifiers
(`WHGAP.«no-ascent-hierarchy»`) are normalized to node ids. `lean: none` nodes are exempt
but WARN if the reason is bare or absent (§7.4 "silence is invalid").

### The seven checks, at the commissioned severities

| # | severity | what it does |
|---|---|---|
| 1 | **FAIL** | declared `file` exists; `def Claim` present; every theorem named in `composition` (string or list; `null # …` ignored) exists as `theorem`/`lemma`; declared `module` matches the module implied by the file path |
| 2 | **FAIL** | bijection: node-shaped `.lean` files (basename not in the non-node set) ↔ nodes carrying a `lean:` block, one-to-one, **and** module name = node id |
| 3 | **FAIL** | hash triple-agreement: recomputed == node `claim_hash` == the 64-hex digest embedded in the Lean docstring (multiple distinct digests → WARN + membership test) |
| 3b | WARN *(extra, beyond the commission — flagged as such in the tool docstring)* | the docstring's **frozen Claim body** equals the node's `## Claim` body. This closes the exact hole R11 m7 named in the authoring tool (`digest in src` passes an edited body with an intact hash line). Kept at WARN because the commission fixed the severities; the decision layer may promote it |
| 4 | **WARN** | AND coverage — the composition theorem's source text mentions each child (and flags mentions of non-children). Every emitted line carries the caveat `TEXTUAL APPROXIMATION: a sound check needs elaboration` |
| 5 | **FAIL** | OR/GOAL route match: if `composition_via_*` theorems exist, their suffix set must equal `children`; a single AND-style `composition` is accepted and reported at INFO (this is WHGAP.goal's shape) |
| 6 | **FAIL** | import graph: node-module imports (prefix-matching, minus non-node modules) == `children`, exactly |
| 7a | **FAIL** | **state-vs-content, the MAJOR-2 catcher.** `state` is tokenized (parentheticals stripped, split on `+`/`,`); tokens outside `{none, stated, composition-checked, proved, refuted}` FAIL. `stated` ⟹ `def Claim`; `composition-checked` ⟹ `composition` non-null **and** the named theorem(s) exist; `proved` ⟹ a declared composition theorem, or `theorem holds`, or a theorem named in the state's parenthetical (and every name mentioned there must exist); `refuted` ⟹ `theorem not_Claim` |
| 7b | **FAIL** / WARN | `composition-checked`/`proved` require the `rel` key (FAIL if absent). `rel: []` is accepted only when the composition signature's binders are all child `Claim`s or the interface; otherwise WARN with the binder list and the honest "cannot decide textually" caveat |
| 7c | **WARN** | epistemic recomputation: header status ≤ min(composition status, child statuses); if exceeded, the composition block's `rel` is required and **its text is printed** when the scoped-input exception is invoked |

Output ends with a **coverage block** (how many evaluations each check actually performed),
so a green run cannot hide a check that silently skipped everything.

### Hash normalization byte-matches the freeze tool

Check 3 recomputes with **exactly** `tools/whgap_lean_freeze_claims.py`'s normalization:
read UTF-8, `CRLF→LF`, `re.search(r"^## Claim\n(.*?)(?=^## )", raw, re.S|re.M)`,
`.strip("\n")`, SHA-256 of the UTF-8 bytes. Verified head-to-head by importing the freeze
tool and comparing **bytes**, not just digests:

```
result: 8/8 nodes byte-identical and hash-identical
```

(`logs_whgap_m7_20260730/hash_normalization_bytematch.log`; lengths 141/387/457/498/644/736/784/881 B.)

---

## 2. G-M7a — self-test: **4/4 PASS** (exit 0)

`--selftest` builds synthetic node+module fixtures in a `tempfile.TemporaryDirectory()`
(a synthetic `FIX` problem spec constructed in code — it is *not* in the registry, and no
real tree is read or written) and asserts:

| fixture | assertion | result |
|---|---|---|
| `clean` | no FAIL, exit 0 | PASS (0 FAIL, 0 WARN) |
| `major2_unbacked_state` | `state: "composition-checked"` with no composition theorem → FAIL | PASS — `FAIL [7a] … UNBACKED (the R11 MAJOR-2 class)` |
| `stale_hash` | Claim body edited, recorded hash left intact → FAIL | PASS — two `FAIL [3]` (node hash and docstring hash both ≠ recomputed) + the 3b body WARN |
| `import_mismatch` | import ≠ `children` → FAIL | PASS — `FAIL [6] … imports [] != children ['FIX.child']` |

`--selftest` exits 0 iff all four hold. Log: `logs_whgap_m7_20260730/selftest.log`.

## 3. G-M7b — real WHGAP tree: **exit 0**, no FAIL

```
$ python tools/lean_dag_check.py --problem werner-holevo-gap
INFO [5] WHGAP.goal: no composition_via_* theorems; single AND-style composition
         ['composition'] accepted (§7.6 note)
WARN [7c] WHGAP.order-boundary: header status PROVED exceeds min(composition=PROVED,
         WHGAP.signed-lift-extension=CERTIFIED*); scoped-input exception invoked,
         composition rel reads: consumes the R2-PROVED-scope region subclaim of P2 …
WARN [7c] WHGAP.zero-capacity-application: header status PROVED exceeds min(…,
         WHGAP.signed-lift-extension=CERTIFIED*); scoped-input exception invoked,
         composition rel reads: consumes ONLY the R2-PROVED-scope subclaim of P2 …
coverage: 1:8  2:16  3:8  4:3  5:1  6:8  7a:8  7b:6  7c:4  nodes:16  mechanized:8  lean-none:8
summary: 0 FAIL, 2 WARN, 1 INFO        exit status: 0
```

Both WARNs are the **expected, documented** scoped-input exceptions of P4 and P6 (the tool
prints the `rel` text that licenses them, so a reader can judge rather than trust); the INFO
records that `WHGAP.goal` legitimately uses one AND-style composition instead of
`composition_via_*`. The coverage line confirms all eight mechanized nodes were evaluated by
checks 1/3/6/7a, all sixteen nodes by the bijection and silence checks, the three AND nodes
by check 4, the one GOAL by check 5, six nodes by 7b and four by 7c.

**No genuine violation was found on the real tree**, i.e. nothing to report under the
"do not silently fix the tree" clause. (The tree had just been brought into compliance by
the LEAN-1.1 repair; this is an independent confirmation of that repair by a different
instrument.)

## 4. G-M7c — the MAJOR-2 detection, reproduced on the real module

Patched copies of the *node* directory (written to the session scratchpad — **the real tree
is untouched**, verified by `git status`) fed to the checker against the **real** Lean
modules. Two shapes of the pre-R11 P9 metadata were tried, because the archived record does
not fix which one it was:

| mutation | detection | exit |
|---|---|---|
| P9 `state → "composition-checked"`, `composition: null` (as the module actually is) | `FAIL [7a] WHGAP.no-ascent-hierarchy: state asserts 'composition-checked' but 'composition' is null -- UNBACKED (the R11 MAJOR-2 class)` | 1 |
| P9 `state → "composition-checked"`, `composition: "composition"` (a name the module does not define) | `FAIL [1] … declared composition theorem 'composition' not found in …/no-ascent-hierarchy.lean` **and** `FAIL [7a] … the named theorem(s) ['composition'] do not exist in the module -- UNBACKED (the R11 MAJOR-2 class)` | 1 |

So **both** readings of the R11 MAJOR-2 drift are caught. Two further mutation probes were
run on the real tree to show checks 3 and 6 bite on real (not just synthetic) data:

- edit `WHGAP.goal`'s `## Claim` body → `FAIL [3]` twice (node hash and docstring hash), exit 1;
- drop one child from `WHGAP.goal`'s `children` → `FAIL [6] … imports [3 modules] != children [2]`, exit 1.

Logs: `mutation_gm7c_major2_null_composition.log`, `mutation_gm7c_major2_named_missing.log`,
`mutation_probe_hash_drift.log`, `mutation_probe_import_drift.log`.

## 5. Artifacts and provenance

```
artifacts/logs_whgap_m7_20260730/
  selftest.log                                G-M7a, exit 0
  real_tree_run.log                           G-M7b, exit 0
  mutation_gm7c_major2_null_composition.log   G-M7c, exit 1 (detection)
  mutation_gm7c_major2_named_missing.log      G-M7c variant, exit 1 (detection)
  mutation_probe_hash_drift.log               check 3 bites on the real tree
  mutation_probe_import_drift.log             check 6 bites on the real tree
  hash_normalization_bytematch.log            8/8 byte-identical vs the freeze tool
  tool_sha256.txt                             SHA-256 of tools/lean_dag_check.py (LF bytes)
  SHA256SUMS.txt                              LF-normalized SHA-256 of every log above
```

Closeout validators (read-only, unchanged by me): `python tools/proof_dag_check.py --problem
werner-holevo-gap` → `Proof-DAG validation OK: 16 nodes`, exit 0; `python
tools/literature_check.py` → `Literature catalogs OK: 51 papers across 5 libraries`, exit 0.

Files touched this session (scope discipline): `tools/lean_dag_check.py` (new),
`channel-capacity/werner-holevo-gap/proof-dag/README.md` (run-line paragraph),
`artifacts/logs_whgap_m7_20260730/**` (new), this report. **Not** touched:
`tools/proof_dag_check.py`, any node/index/DAG markdown, the `se`/`ksum` trees (neither read
nor validated).

---

## 6. Findings for the decision layer

**M7-F1 (MATERIAL — commission-vs-disk conflict; reported, not resolved).**
The commission's premise, inherited from R11 m7, that "none of §7.6's seven checks is
implemented anywhere" is **false as of commit `b9fa96b`** ("… *proof_dag_check gains the
DAG-protocol 7.6 lean-block anti-drift checker (+169)*", the ksum Lean T3 landing).
`tools/proof_dag_check.py:199 check_lean()` now implements a *partial* §7.6: declared
file/`Claim`/composition-theorem existence (errors), docstring-vs-node hash, freeze-rule
hash drift, orphan modules, `composition_via_*` vs children, and imports-not-children —
**all six of those at WARNING**, by an explicit "v1 rollout … multiple problems share this
tool mid-migration" policy. Consequences the decision layer should adjudicate:

1. **The MAJOR-2 class remains uncaught by `proof_dag_check.py`**: it has no state-vs-content
   check at all, so `state: "composition-checked"` with `composition: null` passes it
   silently. That is precisely the gap `lean_dag_check.py` check 7a closes — the commission's
   *purpose* survives its factual premise being stale.
2. **Severity divergence.** Hash drift and import mismatch are WARNINGs there and FAILs here
   (as commissioned). Two tools with different severities for the same protocol clause is
   itself a drift risk; someone should decide whether `proof_dag_check.py` defers to
   `lean_dag_check.py` for WHGAP, or whether the checks merge. I could not act: the
   commission forbids touching that file, and it is shared with live se/ksum sessions.
3. **Duplicate implementations of §7.6 checks 1/2/3/5/6 now exist.** Recommend the decision
   layer either (a) fold `lean_dag_check.py` into `proof_dag_check.py` in a session that owns
   both, or (b) keep the two and record in `DAG_PROTOCOL.md` §7.6 which is authoritative.

**M7-F2 (minor, in `tools/proof_dag_check.py`, NOT fixed — out of scope).**
Its `LEAN_NON_NODE_BASENAMES = {"Interface", "Trust", "SelfTest", "Defs"}` omits `Model`,
so its check-2 pass emits a spurious
`WARNING: orphan lean module WHGAP/Model.lean (derived id WHGAP.Model matches no node)` on
every WHGAP run. `WHGAP/Model.lean` is R11's satisfiability model, shipped in-tree by the
LEAN-1.1 repair; §7.6/the M7 commission list `Model` as a non-node module, and
`lean_dag_check.py` treats it correctly. One-word fix, owned by whoever owns that file.

**M7-F3 (advisory, protocol).** §7.6's check 4 ("AND composition parameters cover exactly the
status-propagating children, plus only declared relative hypotheses/interfaces") cannot be
decided by text: it needs elaborated signatures. Everything this tool says about check 4 —
and about `rel: []` under 7b — is a textual approximation and is labelled as such in every
emitted line. A sound version would need `lake env lean` + `#check`/`elab` output; that is a
separate, larger commission, not smuggled in here.

**M7-F4 (advisory).** `tools/whgap_lean_freeze_claims.py --check` still only tests
`digest in src` (the R11 m7 hole). It is unchanged (single-writer discipline for the freeze
tool), but `lean_dag_check.py` check 3b now covers the same hole at WARN. If the decision
layer wants that hole closed at FAIL, promote 3b rather than editing the freeze tool.

---

## 7. Honest limits of this deliverable

- Everything here is **executor-authored and unreviewed**: NUMERICAL, `pending-review:`.
  A green `lean_dag_check.py` run is evidence about *metadata consistency only*; it says
  nothing about whether the Lean statements faithfully mirror the prose (that is R11's job)
  and nothing about whether the proofs are correct (that is `lake build` + §7.10).
- Checks 4 and 7b-empty-rel are textual approximations (M7-F3). Check 7c compares statuses on
  the §2 ladder and cannot judge whether an invoked scoped-input exception is *justified* —
  it prints the `rel` text so a human can.
- The parser is a purpose-built mini-YAML reader, not a YAML library; it handles the shapes
  present in the WHGAP tree (inline scalars/lists, `null # comment`, folded `>` blocks,
  multi-line `- ` item lists). A node using an unhandled YAML shape would be parsed as
  missing keys — which fails loudly (checks 1/7a), not silently.
- `se`/`ksum` were neither read nor validated this session; their registry rows are
  unexercised placeholders and their paths are guesses that a future enabling session must
  verify.

