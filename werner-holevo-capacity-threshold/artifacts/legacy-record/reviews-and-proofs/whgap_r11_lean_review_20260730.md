# WHGAP R11 — independent §7.10 review of the DAG-mirroring Lean development (2026-07-30)

Reviewer: fresh Opus 5 instance, R11 REVIEWER role.
Reviewed project: `channel-capacity/werner-holevo-gap/proof-dag/lean/` (package `whgapDag`).
Reviewed report: `artifacts/whgap_lean_t1t2_20260730.md` (LEAN-1 executor).
Governing protocols: `research/DAG_PROTOCOL.md` §7 (mandate = §7.10), rules 6–7; rule-7 embeds
from `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §§1–3.
Run artifacts: `artifacts/logs_whgap_lean_20260730/r11_*` + `SHA256SUMS_r11.txt`.

**VERDICT: (B) FINDINGS — 2 MAJOR, 15 minor.**
Neither MAJOR is a soundness defect. The build, the axiom evidence, the frozen-Claim
integrity, the import graph, the satisfiability of every composition, and every machine-checked
scalar identity all reproduce and hold. Both MAJORs are **attribution/metadata** defects that
make the licensing sentence "the `lean:` states on the nodes are licensed as recorded" false
*as recorded*, which is why licence (A) cannot be granted as written.

---

## 0. PRE-ACTION REPORT (`research/PRETASK_RELOAD_PROMPT.md`)

Read from disk, complete and in order, before any work: `research/DAG_PROTOCOL.md` (whole
file, §7 in full), `research/RESEARCH_STRUCTURE_PROTOCOL.md` (incl. §4 item 7 and §10),
`channel-capacity/werner-holevo-gap/README.md`,
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`,
`.../notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §§1–3, and the node files `WHGAP.goal`,
`WHGAP.qpositive-onset`, `WHGAP.zero-capacity-application`, `WHGAP.signed-lift-extension`,
`WHGAP.order-boundary`, `WHGAP.no-ascent-hierarchy`, `WHGAP.onset-two-fifths`,
`WHGAP.private-boundary`.
(Note: there is no repo-root `AGENTS.md`; the chain resolves through `research/`. Reported here
rather than resolved silently.)

* **Target node and status as read from disk:** `WHGAP.goal` — **OPEN**
  (`status_source: problem-scaffold-2026-07-28`; displayed "resolved except on `[2/5, 1/2)`",
  capped by the CONJECTURED child `WHGAP.onset-two-fifths`).
  Its Lean block reads `state: composition-checked`, `rel: ["P13 unresolved", "hS : S ⊆ [2/5,1/2)"]`,
  evidence tier **NUMERICAL, `pending-review:`** — this review is that pending gate.
* **Role: reviewer. Independence statement:** I did not author any part of the Lean
  development, its report, the node files, or the manuscript, and I was given no desired
  outcome. The licensing menu was presented to me as alternatives.
* **Highest status my evidence could license (§2):** my completed, archived review is what
  opens the **CERTIFIED\*/PROVED** gate for the `lean:` attributes under rules 6–7; the
  *writer* of any resulting status is the decision layer, not me. Note §7.1: a Lean attribute
  never promotes a node by itself, so nothing here moves an epistemic status.
* **Gates/deliverables (one line each):** reproduce the build from deleted outputs and report
  the true exit status; rerun `#print axioms` on every top declaration and scan for
  `sorry`/`axiom`/`native_decide`/`implemented_by`; recompute every frozen-Claim SHA-256 with
  my own code *and* by hand for ≥3 nodes and compare each Lean `Claim` with the prose;
  compare the goal conclusion with `paper/main.tex` and with the node's composition block;
  check satisfiability/non-vacuity and the interface citations against the local PDFs; check
  README/report scope honesty; audit the two executor deviations and the P14 flagship's
  unconditionality. Single deliverable: this report (+ `tools/whgap_r11_claim_audit.py` and
  `artifacts/logs_whgap_lean_20260730/r11_*`).
* **Conflicts between commission text and disk protocols:** **none.** The single-writer
  deviation (no node/index/DAG edits) is commissioned and is narrower than §5/§6 of the DAG
  protocol; consequently the atomic-update obligation (`RESEARCH_STRUCTURE_PROTOCOL.md` §6
  step 3 — linking this report from `WHGAP.goal` and from each mirrored node) is **owed by the
  decision layer** and is listed in §9 below rather than performed by me.

**Anchoring discipline (7c).** §5 of the executor report — the author's fidelity self-table —
was read **only after** §§1–6 of this report were derived. My Claim-vs-prose comparison (§4)
was written from the node files and `paper/main.tex` alone; every scalar identity in §5 was
re-derived by hand before any of the author's arithmetic was read. §6 records the diff.

**Rule-7 screening actually performed** (R5 §2 standing failure-mode list, item by item):
(1) no sympy `.H` use in my path — I re-derived symbolically by hand; (2) interpreter: I used
the WindowsApps python only for my own scripts, which need no third-party packages, plus
`cpython3119`'s `pypdf` for the ZW PDF; (3) complement-convention drift — checked where the
Lean scalars come from (paper Lemma 7.1 and Lemma 6.1) and found the mis-citation of MAJOR-1;
(4) transpose vs conjugate-transpose — checked in `blockA_trace_det` (real-symmetric stand-in
vs Hermitian block; invariants agree, see §5.6); (5) no symbolic sorting used;
(6) **CRLF/LF in the checksum ledger — this is minor m1**; (7) degeneracy bookkeeping —
checked the self-test degenerate point (§7); (8) `ε log ε` bookkeeping — checked the shape of
`hexp` against the manuscript's `O(ε)` (§4.6); (9) anchoring — see above.

---

## 1. Checklist item 1 — build reproduction

`.lake/build` was deleted in full (104 files, 30 MB); `.lake/packages` (the junction to the
shared prebuilt Mathlib cache) was left untouched, as the README instructs.

| | |
|---|---|
| command | `lake build` |
| cwd | `channel-capacity/werner-holevo-gap/proof-dag/lean` |
| lake / lean | `Lake 5.0.0-src+68218e8 (Lean 4.31.0)` / `Lean 4.31.0, x86_64-w64-windows-gnu, commit 68218e876d2a…` |
| toolchain file | `leanprover/lean4:v4.31.0` (elan switched correctly: the ambient lake is 4.32.2, the project build ran 4.31.0) |
| **true exit status** | **0** |
| wall time | **491 s** (8 min 11 s) |
| jobs | `Build completed successfully (3051 jobs)` — identical job count to the executor's log |
| transcript | `artifacts/logs_whgap_lean_20260730/r11_lake_build.log` |

Non-fatal warnings, all cosmetic and all present in the executor's log too: 6 `push_neg`
deprecations, 1 `<;>`-style linter note, 2 "`all_goals ring` does nothing" notes, 1 unused-binder
note (`order-boundary.lean:76:5`, see minor m12). No errors, no `sorry` warnings, no
"declaration uses sorry".

**Result: PASS — the build reproduces from a clean WHGAP tree, exit 0.**

---

## 2. Checklist item 2 — axioms and forbidden constructs

`#print axioms` fires for all **44** declarations listed in `WHGAP/Trust.lean` during the
build. I re-read all 44 lines of my own transcript:

```
grep -c "depends on axioms"                                        -> 44
grep "depends on axioms" | grep -v "[propext, Classical.choice, Quot.sound]"  -> (empty)
```

Every one of the 44 reports exactly `[propext, Classical.choice, Quot.sound]`. Coverage check:
the 44 cover the interface structure, all 8 node `Claim`s, all 4 `composition*` theorems, the
P14 bridge, and every T2 core lemma. `Support.Basic`'s helper lemmas and the 29 `SelfTest`
`example`s are not separately printed, but `#print axioms` is transitive over the whole proof
term, so anything they could have smuggled in would appear in the 44 — nothing did.

Forbidden-construct scan (`r11_forbidden_scan.log`), over every `.lean` outside `.lake/`, for
`sorry`, `sorryAx`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `partial`,
`opaque`, `decide`: **every single hit is prose inside a docstring or one of the 44
`#print axioms` command lines.** There is no `sorry`, no `axiom` declaration, no
`native_decide`, no `implemented_by`, no `unsafe`/`partial` declaration anywhere.
`sorryAx` appears in **zero** proof terms (confirmed twice: by the scan and by the 44 axiom
lines).

**Result: PASS. `Trust.lean`'s "sorry census: Zero" is accurate, and its five-row hypothesis
table matches the elaborated signatures I printed independently (§3).**

---

## 3. Checklist item 3a — frozen-Claim integrity (hash + verbatim text)

Three independent instruments, deliberately not sharing code:

1. the authoring tool, `tools/whgap_lean_freeze_claims.py --check` → 8/8 `ok`
   (`r11_freeze_check.log`);
2. **my own from-scratch implementation**, `tools/whgap_r11_claim_audit.py` — a *line-based*
   (not regex) section scanner, which additionally extracts the verbatim frozen block from
   each Lean docstring and compares it **character by character** against the node file
   → **8/8 PASS on hash AND on verbatim text** (`r11_claim_audit.log`);
3. **a by-hand, shell-only computation** (`awk` section extraction + blank-edge stripping +
   `sha256sum`, no Python at all) for four nodes — `WHGAP.goal`, `WHGAP.private-boundary`,
   `WHGAP.order-boundary`, `WHGAP.onset-two-fifths` — all four digests reproduce exactly
   (`r11_manual_hash.log`).

| node | recomputed SHA-256 | docstring | verbatim text |
|---|---|---|---|
| `WHGAP.goal` | `f3a95693…39ce99` | match | match (141 chars) |
| `WHGAP.qpositive-onset` | `a3f1e418…568cfa` | match | match (492) |
| `WHGAP.zero-capacity-application` | `8be43283…73326da` | match | match (636) |
| `WHGAP.signed-lift-extension` | `6283cddf…149cf757` | match | match (385) |
| `WHGAP.order-boundary` | `db030127…c69e611` | match | match (450) |
| `WHGAP.no-ascent-hierarchy` | `542edac6…65363d37` | match | match (708) |
| `WHGAP.onset-two-fifths` | `502ef4a9…8cefe5a04` | match | match (355) |
| `WHGAP.private-boundary` | `415bdc11…172a30aa9` | match | match (783) |

Note (minor m7): the authoring tool's `--check` mode tests only `digest in src` — it would
pass an *edited* docstring body whose hash line was left intact. Instrument 2 closes that hole
and reports clean.

**Result: PASS — no drift between the node `## Claim` sections and the Lean docstrings.**

---

## 4. Checklist item 3b — Claim vs prose, module by module (derived before reading §5)

Legend: **F** = faithful in scope; **F(w)** = faithful but weaker (disclosed granularity loss);
**S** = a *substituted* statement, not a weakening of the node Claim.

### 4.1 `WHGAP.goal` (G) — **F**

Lean `Claim I S := {x | x ∈ Ioo 0 1 ∧ I.Q x = 0} = Ico (1/2) 1 ∪ S`.
This is verbatim the node's `composition:` block (`{x ∈ (0,1) : Q = 0} = [1/2,1) ∪ {x ∈ [2/5,1/2) : Q = 0}`)
with the strip set promoted to a parameter `S` plus `hS : S ⊆ [2/5,1/2)`.
Endpoints checked one by one: domain `(0,1)` **open at both ends**; `[1/2,1)` **closed at
1/2, open at 1**; `x = 1` **excluded** — correct, since on disk the endpoint is CERTIFIED\*
via cite-only RK24 / paper Lemma 4.1, and the module says exactly that. `Q`, not `Q^{(1)}` —
correct for the determination. Clause 2 of the prose ("close the gap `x ∈ (1/2,4/7)`") is a
substatement of `[1/2,1) ⊆` the set; not stating it separately is right.

I checked the composition proof term by hand, both inclusions:
`⊆` splits on `x < 1/2` then `x < 2/5`, killing the first piece with `(h3 …).ne'` and mapping
the strip through `h13 .mp`; `⊇` uses `h4` on `[1/2,1)` and `hS`+`h13 .mpr` on `S`. No premise
beyond `hS, h3, h4, h13` is used (confirmed from the elaborated signature, §4.9). **Genuine,
complete, unconditional proof of the assembly logic.**

`composition_conjectured` yields `= Ico (2/5) 1`, i.e. `[2/5,1)`. The prose P13 says "with P4,
give `{x : Q=0} = [2/5,1]`"; the Lean drops the `x = 1` endpoint, consistently with everything
else. Correct.

### 4.2 `WHGAP.qpositive-onset` (P3) — **F(w)**

`Claim I := ∀ x, 0 < x → x < 2/5 → 0 < I.Q x`. Exactly the node's PROVED content
(`Q(Λ_x) > 0 for ALL x ∈ (0, 2/5)`), open interval, strict inequality, regularized `Q` as the
prose writes it. Loss (the "determine the threshold" task, `x_1`/`x_H`, the two-letter null,
the 783/2000 witness) is real and is disclosed. `composition` consumes exactly
`«no-ascent-hierarchy».Claim` + `I.q_pos_of_ic_pos`, nothing else.

### 4.3 `WHGAP.zero-capacity-application` (P4) — **F**

`Claim I := ∀ x, 1/2 ≤ x → x < 1 → I.Q x = 0 ∧ I.P x = 0`. Interval and both capacities match
the prose exactly. The "at every blocklength" quantifier sits inside `zw_hrsf_zero`, which is
the honest place (ZW Cor 3.7 states precisely `P^{(1)}(M^⊗n) = Q^{(1)}(M^⊗n) = 0 (n≥1)` and
`P(M) = Q(M) = 0`; verified against the local PDF, §5.8). `composition_one_shot` records the
`Qone/Pone` half separately — good practice, and the reason minor m4 below is a *consistency*
complaint about P14 rather than a soundness one. The closed interval `[1/2,1]` is deliberately
not stated. Correct.

### 4.4 `WHGAP.signed-lift-extension` (P2) — **F**

`Claim I := ∀ x, 1/2 ≤ x → x < 1 → I.SignedLiftCP x`. The prose headline says "extends to
`[1/2, x_max]`, `x_max > 1/2`"; the frozen bracket pins the R2-licensed region as `[1/2,1)`,
which is what Lean states. Since the bracket is inside the frozen Claim, this is faithful (and
the Claim is only ever a *hypothesis*, never proved, so no over-claim can propagate).

### 4.5 `WHGAP.order-boundary` (P6) — **F**

`Claim cBKM := ∀ x, 0 < x → x < 1 → (cBKM x ↔ 1/2 ≤ x)` — i.e. "the cBKM domination set
within `(0,1)` is `[1/2,1)`", exactly the node's ANSWER. `cBKM` is an abstract predicate; both
order directions are explicit hypotheses (`hHolds`, `hFails`) and both are displayed in the
node's `rel`. The manuscript's `cor:phase` writes the set as `[1/2,1]` (its domain is `(0,1]`,
with `x = 1` read through Lemma 4.1); the node writes `[1/2,1)` (domain `(0,1)`). Lean follows
the node. Consistent, no silent endpoint change.

### 4.6 `WHGAP.no-ascent-hierarchy` (P9) — **S**

The node's frozen Claim is the no-ascent operator inequality
`Tr[(N^c)^{⊗n}(φ) log (N^c)^{⊗n}(ψ)] ≤ Tr[N^{⊗n}(φ) log N^{⊗n}(ψ)]` at every blocklength.
The Lean `Claim I := ∀ x ∈ (0,2/5), ∃ c > 0, I.IcLB x c` is **a different proposition**, not a
weakening of it. The module says so plainly, and so does the node's mechanization note; the
substitution is therefore *disclosed*, and it is harmless in the graph because the Lean `Claim`
is only ever a hypothesis of `«qpositive-onset».composition`.

Two problems remain: the justification offered for the substitution is invalid (minor m2), and
the recorded mechanization **state** is unbacked (MAJOR-2).

`hexp` faithfully encodes the manuscript's `I_c(ρ_ε) = d₁(x) ε log(1/ε) + O(ε)` (eq:iclead):
a uniform `C` on a punctured window `(0,ε₀)`, which is exactly what `O(ε)` as `ε → 0⁺` means.
No dropped uniformity.

### 4.7 `WHGAP.onset-two-fifths` (P13) — **S**, and see minor m3

`Claim I S := ∀ x, 2/5 ≤ x → x < 1/2 → (I.Q x = 0 ↔ x ∈ S)`. This is the parent's composition
input ("a determination of `{x ∈ [2/5,1/2) : Q = 0}`"), not the node's conjecture. Restricting
to `[2/5,1/2)` rather than the prose's `[2/5,1)` is right (the upper half is P4's). `conjecturedS`
is defined and — I verified by grep across the whole tree — **asserted nowhere**: its only
occurrences are as an instantiation argument in `goal.composition_conjectured`. Correct and
important.

The **`Q^{(1)} → Q` substitution** is the one flagged in my mandate. Verdict: the Lean is
right and the prose is loose. The node's frozen conjecture asserts `Q^{(1)}` statements and
says only "*ideally* also `Q = 0` there"; the parent's composition block asks for a **`Q`**
determination. Lean mirrors the parent. But the module docstring and the executor's §5 both
say "the conjecture asserts both", which the frozen text does not support — see m3 for the
concrete downstream risk.

### 4.8 `WHGAP.private-boundary` (P14) — **F(w)**

`Claim I := ∀ x, 0 < x → x < 1/2 → 0 < I.P x` is **verbatim the last sentence of the node's
frozen Claim** ("Hence P(Λ_x) > 0 there"). The quantitative `≥ Δ(x) ≥ (1-2x)³/(2(1-x)(2-3x))`
half is the scalar core (proved) plus the bridge (hypothesised). Faithful; see m4 for the
undisclosed `P^{(1)} → P` inside `hbridge`.

### 4.9 Mechanically confirmed signatures

Rather than trust the sources, I elaborated the signatures out-of-tree
(`r11_audit_lean.log`, exit 0):

```
f_pos                 : ∀ {s}, 0 < s → s < 1 → 0 < Support.f s
argument_coincidence  : ∀ {x r}, 0 < x → x < 1/2 → 0 < r → (u/b = … ∧ v/e = …)
Delta_closed_form_pos : ∀ {x}, 0 < x → x < 1/2 → (0 < sStar x ∧ sStar x < 1) ∧ 0 < Delta x
Delta_lower_bound     : ∀ {x}, 0 < x → x < 1/2 → (∀ s, 0 ≤ s → s < 1 → s^2 ≤ f s) → …
goal.composition      : ∀ I, ∀ S ⊆ Ico (2/5) (1/2), P3.Claim I → P4.Claim I → P13.Claim I S → goal.Claim I S
order-boundary.composition : ∀ cBKM I, P2.Claim I → (∀ x, I.SignedLiftCP x → cBKM x)
                              → (∀ x, 0 < x → x < 1/2 → ¬cBKM x) → Claim cBKM
```

**The P14 flagship is genuinely unconditional.** `f_pos`, `argument_coincidence` and
`Delta_closed_form_pos` carry no hypothesis beyond `0 < s < 1` / `0 < x < 1/2` (`hr : 0 < r`
for the third). `hsq` appears in `Delta_lower_bound` **and nowhere else** — I confirmed this
from the elaborated types, not from the source comments. `argument_coincidence` does not even
need `r² = 2`: it is a rational identity in `r`, strictly stronger than commissioned.
`goal.composition` takes exactly the three child Claims plus `hS`; no hidden premise.

---

## 5. Checklist items 4 & 5 — manuscript comparison, satisfiability, interface citations

### 5.1 Goal conclusion vs manuscript vs node composition block

The node's inline assembly and `goal.Claim` agree exactly (§4.1). Against `paper/main.tex`:
`rem:strip` states "on `(0,2/5)` both capacities are positive, on `[1/2,1]` both vanish, and on
the strip `[2/5,1/2)` we now know `P > 0` while `Q` is undetermined" — which is precisely
`goal.Claim` with `S` unknown, modulo the `x = 1` endpoint the Lean drops on purpose.
`thm:main` (`P^{(1)}(Λ_x^{⊗n}) = Q^{(1)}(Λ_x^{⊗n}) = 0` for `x ∈ [1/2,1]`, `n ≥ 1`; hence
`P = Q = 0`) is P4's Claim **plus** the `x = 1` endpoint and the blocklength quantifier; the
Lean carries `[1/2,1)` and pushes the blocklength into the interface. Honest, and stated as
such in both the module and the README.

### 5.2 Every T2 identity re-derived by hand, then matched to the manuscript

I derived each of the following independently before opening the executor's arithmetic:

* `forcing_p` — expanding the four terms and clearing `x/(x-1)` gives
  `9p² − 6p + 1 = (3p−1)²`. **Matches `prop:unique` (paper §3.2) term for term**, including
  the RHS orientation `(3p−1)²(x−1)/x`.
* `forcing_d` — clearing `x`: `−9d² − 12dx + 12d − 4x² + 8x − 4 = −(3d+2x−2)²`. **Matches
  `prop:unique`**; note `3d − 2(1−x) = 3d + 2x − 2`, so the paper's `eq:forcing` form and the
  Lean form are the same object.
* `lam5 = 4(1−x)(2x−1)/x`, `lam3 = 16(1−x)(3x−1)/(9x)` — **exactly the two nonzero roots of
  `eq:charpoly` in `thm:spectrum`**; the sign iffs (`≥ 1/2`, `≥ 1/3`) and the binding-branch
  conclusion reproduce `thm:spectrum` claim (1).
* `gap_identity`: `x/2 − (2/x)(1−3x/2)² = 6 − 2/x − 4x = 2(1−x)(2x−1)/x`. **Matches paper §5**,
  and is exactly `lam5/2`, corroborating `rem:obstruction`'s "the local BKM gap equals
  `λ₅(x)/2`" across two independent Lean modules.
* `threshold_factorization`: `ε⁰` coefficient `−4x²+6x−2 = 2(1−x)(2x−1)`; `ε¹` coefficient
  `(1−3x/2)(x + 2 − 3x) = 2(1−x)(1−3x/2)`. Identity confirmed.
  `strict_violation_window` is the correct algebraic shadow of the violation
  `g_E < g_B ⟺ x·b_ε < 2(1−3x/2)²(1−ε)` from the R5b witness data, with the exact threshold
  `ε_c(x) = 2(1−2x)/(2−3x)`.
* `b, e, u, v` — **all four match `lem:holevo` (paper Lemma 7.1) verbatim**:
  `b = x/2 + (1−3x/2)ε`, `u = (t/√2)(1−3x/2)`, `e = (x/2)(1−ε)`, `v = tx/(2√2)`.
* Frozen point `ε = t = ε_c/2 = (1−2x)/(2−3x)`: `b = (1−x)/2`, `e = x(1−x)/(2(2−3x))`,
  `u = (1−2x)/(2r)`, `v = x(1−2x)/(2r(2−3x))`, and **both ratios collapse to `(1−2x)/(r(1−x))`**.
  Reproduced by hand; matches `thm:private` exactly.
* `prefactor_eq`: `b − e = ε(1−x)` ✓ (paper's own one-liner).
  `Delta_eq_prefactor_mul`: `(b−e)·f(s*) = Δ(x)` at the frozen point ✓ — the paper's
  `Δ(x) := (b−e) f(s*(x))` and its closed form are the same object.
* `sStar_lt_one`: `(1−2x)² < 2(1−x)² ⟺ 1 − 2x² > 0` ✓ (true on `(0,1/2)`, in fact to `1/√2`).
* `Delta_lower_bound` under `hsq`: `K·s*² = (1−2x)³/(2(1−x)(2−3x))` ✓ — the paper's second
  inequality exactly.
* `blockA_trace_det`: `tr = 1 − x/2`, `det = (1−x)(x/2) − β²(1−2ε)² = 2x(1−x)ε(1−ε)` ✓.

**Value-vs-formula statement (7f):** every item above I verified as a **FORMULA** (a symbolic
identity in the free parameters), by my own hand derivation, not by evaluating the author's
script or re-running the author's `sympy` file. The `SelfTest` examples are additionally
**VALUE** checks at rational points; I confirmed the two non-degenerate forcing points by hand
(`forcing_p(1/4,1/2) = −3/4`, `forcing_d(1/4,1/3) = −1`). What remains unverified by anyone in
Lean: that these displayed scalars really *are* the Choi entries / Holevo quantities /
eigenvalues they are named after — the 27×27 construction, the char-poly factorization
`eq:charpoly`, the Gram factors `4/25` and `1/3`, Appendix A's entrywise table, and the
`lem:holevo` collapse itself are all outside the development, correctly and explicitly.

**c ≥ 2 gates (7b):** every identity above was checked **fully symbolically** (formula level),
which subsumes the two-point requirement; in addition the `SelfTest` layer exercises each at
≥ 1 non-degenerate rational point and I re-evaluated two of those by hand.

**Type audit (7a).** Domains/codomains of everything in scope: `Q, P, Qone, Pone : ℝ → ℝ`
(opaque scalars, *not* channel functionals); `SignedLiftCP : ℝ → Prop`; `IcLB : ℝ → ℝ → Prop`;
`cBKM : ℝ → Prop` (a theorem *parameter*, quantified per-theorem, so no global consistency
obligation); `S : Set ℝ`; `b, e, epsC, dOne, f, sStar, Delta : ℝ → ℝ` and `u, v : ℝ → ℝ → ℝ → ℝ`
(the third argument `r` standing for `√2`); `blockA` is `Matrix (Fin 2) (Fin 2) ℝ`.
Every constituent map is well defined on its stated domain: the four `Support` denominators
(`x`, `2−3x`, `1−x`, `2−x`, `r`) are each guarded by a named nonvanishing lemma or an explicit
hypothesis at every use site — I checked each `field_simp` call site for an unguarded division
and found none. The one type-level *stand-in* is `blockA_trace_det`: the paper's `A(ε)` is
**Hermitian** with off-diagonals `∓iβ(1−2ε)`, the Lean matrix is **real symmetric** with
`−β(1−2ε)`. Trace is identical; determinant agrees because
`|iβ(1−2ε)|² = β²(1−2ε)²`. So the two invariants transfer, the matrix does not — disclosed in
the module. (This is the item of MAJOR-1, for a different reason.)

**Quantifier hygiene (7g).** Every term of art in a reviewed Lean statement resolves:
`SignedLiftCP`, `IcLB`, `cBKM` resolve to interface fields / explicit parameters with
docstrings; `f`, `s*`, `Δ`, `ε_c`, `d₁`, `b/e/u/v` resolve to `Support.Basic` definitions that
match the manuscript symbol for symbol. No undefined term of art appears in any `Claim`.

### 5.3 Satisfiability / non-vacuity — a machine-checked certificate

§7.10.5 needs more than an argument, so I built one. `artifacts/logs_whgap_lean_20260730/r11_audit_source.lean`
(compiled out-of-tree with `lake env lean`, **exit 0**) constructs an explicit, **non-trivial**
`CapacityInterface`:

```
Q := fun x => if x < 2/5 then 1 else 0      P := fun x => if x < 1/2 then 1 else 0
Qone := 0   Pone := 0   SignedLiftCP x := 1/2 ≤ x   IcLB x c := 0 < x ∧ x < 2/5 ∧ 0 < c
```

with all three assumption fields discharged, and then proves **in one model, simultaneously**:
`R11_P2` (P2.Claim), `R11_P9` (P9.Claim), `R11_P3`, `R11_P4`, `R11_P13` (at `S = conjecturedS`),
`R11_goal := goal.composition …`, `R11_goal_conj := goal.composition_conjectured …`
(concluding the *non-trivial* set equality `{x ∈ (0,1) : Q x = 0} = [2/5,1)`), and `R11_P6`
via `order-boundary.composition` with the **non-trivial** predicate `cBKM x := 1/2 ≤ x`
(neither `True` nor `False`). All four reviewer theorems print
`[propext, Classical.choice, Quot.sound]`.

Consequences: the interface is inhabited (no contradictory-hypothesis vacuity); each
composition theorem's hypotheses are **jointly satisfiable**, and satisfiable *together across
theorems*; and no composition's conclusion is trivially true. The P14 bridge shape is likewise
inhabited (`Δ(x) ≤ 1` on `(0,1/2)`: `Δ` is bounded by ≈ 0.277 there), and `hsq` is a true fact
about `f` (the manuscript's own series `eq:fdef` gives `f(s) = s² + s⁴/6 + …`), so
`Delta_lower_bound` is not conditional on a falsehood.

**Result: PASS — nothing in this development is vacuous.**

### 5.4–5.8 Interface citations against the local PDFs

I extracted the ZW text from
`channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf`
(encrypted with an empty password, per the local README) and read the cited statements:

| interface field | docstring citation | what the PDF says | verdict |
|---|---|---|---|
| `zw_hrsf_zero` | ZW **Thm 3.3** | "Theorem 3.3 (Signed-lift CP-defect criterion)": hypotheses (1) `M(1)≻0, N(1)≻0`, (2) adjoint-preserving `J` with `J†∘N = M`, (3) `Δ_J` completely positive ⟹ `N ⪰cBKM M` | **exact** |
| `zw_hrsf_zero` | ZW **Lem 3.2**, "BGSW25 (cBKM → cRE bridge)" | "Lemma 3.2 ([BGSW25]) … `M ⪰cBKM N ⟹ M ⪰cRE N`" | **exact**, incl. the BGSW25 attribution |
| `zw_hrsf_zero` | ZW **Cor 3.7** | "Corollary 3.7 … `P^{(1)}(M^{⊗n}) = Q^{(1)}(M^{⊗n}) = 0 (n≥1)`, `P(M) = Q(M) = 0`" | **exact** — and note this is *literally* the four-fold conjunction the field states |
| `zw_hrsf_zero` | **HRSF22 Lem 3.1** (hybrid tensorization) via ZW | ZW eq. (3.4)+text: "This is the hybrid tensorization lemma from [HRSF22, Lemma 3.1]"; the local HRSF22 page records the same statement as locally checked | **exact** |
| `lsd_devetak` | "ZW eq. (2.6)/(2.7)"; Llo97, Dev05 | (2.6) defines `P^{(1)}`, (2.7) gives `P = lim = sup_n (1/n)P^{(1)}(N^{⊗n})`. The **quantum** half is (2.3)/(2.4), and (2.4) displays only the limit | **incomplete** — minor m5 |
| `q_pos_of_ic_pos` | same LSD/Devetak interface, as used by Thm 8.1 of the N1' note | consistent with ZW (2.4)/`thm:positivity`'s `Q ≥ Q^{(1)} > 0` | ok |

**Frozen-input scope (7d).** I relied on the *statements* of ZW Thm 3.3 / Lem 3.2 / Cor 3.7
and HRSF22 Lem 3.1 only to check that the interface *cites what it says it cites*; I did not
re-derive them and this review licenses nothing about them. The R2/R3/R5b/R5c/R5d/R8 prose
reviews are outside my scope; where I compared a Lean scalar to the manuscript, the manuscript
display is the object I compared to, not those reviews' verdicts.

---

## 6. Checklist item 6 — scope language and over-claiming; and the diff against §5 of the report

**§7.9 verbatim sentences.** Both appear, verbatim, in `proof-dag/lean/README.md` (lines 32–35)
and in the executor report §1:

> A theorem proved against an abstract interface is exactly as strong as the results that
> interface cites, and not one notch stronger.

> `lean-checked` is an evidence attribute, never a status.

The `RESEARCH_STRUCTURE_PROTOCOL.md` §4 item 7 sentence ("a formalization is *evidence*, not a
status…") is also quoted verbatim in both. The README's "What a green build here does NOT
establish" section (7 items) and the report's identical list are, in my judgement, **accurate
and if anything conservative**: item 1 disowns the capacities, item 2 disowns the goal, item 3
disowns `P^{(1)} ≥ Δ`, items 4–6 disown the lift, the BKM order and the external results, item
7 disowns review status. **Nowhere in the README, the report, the module docstrings or the
node mechanization notes is a green build described as proving an original theorem.** Every
node's mechanization note carries "NUMERICAL `pending-review:` — the §7.10 statement-fidelity
review is the completion gate". The one wording risk is m13.

**Diff against the executor's §5 self-table** (read only at this point). Rows for `goal`,
`qpositive-onset`, `zero-capacity-application`, `signed-lift-extension`, `order-boundary` and
`private-boundary` agree with my independently derived §4 in substance and in the granularity
losses named. Three divergences:

1. `no-ascent-hierarchy` row: "Direction: prose ⟹ (via the first-order mechanism) this" — I do
   not accept this (minor m2).
2. `onset-two-fifths` row: "prose asserts both [`Q^{(1)}` and `Q`]" — the frozen prose does not
   (minor m3).
3. `private-boundary` row: does not disclose that `hbridge` is stated with the **regularized**
   `I.P`, not `I.Pone` (minor m4).

The self-table does **not** mention `blockA_trace_det`'s provenance beyond "the Hermitian
block"; the module docstring's "paper Lemma 7.1" is where MAJOR-1 lives. Everything else in
§§1–4, 6–8 of the report that I could check (12 modules, 44 declarations, 29 `SelfTest`
examples, exit 0, the import table, the eleven re-derived identities, the `ε_c(9/20) = 4/13`
correction) is accurate.

---

## 7. The two executor deviations, audited

**Deviation 1 — the degenerate self-test point.** The commission's proposed point
`(x,p,d) = (2/5, 1/3, 2/5)` gives `3p − 1 = 0` and `3d + 2x − 2 = 0`, so both forcing
identities read `0 = 0` there. **I confirm the finding independently**: at `p = 1/3` the
right-hand side `(3p−1)²(x−1)/x` vanishes identically in `x`, and at `(x,d) = (2/5,2/5)`,
`3d + 2x − 2 = 6/5 + 4/5 − 2 = 0`. A mis-transcribed left-hand side would indeed pass. The
executor's remedy is correct and sufficient: the degenerate point is retained and *labelled*
as a zero-locus check, and non-degenerate points were added — `forcing_p(1/4,1/2)` with both
sides `−3/4` and `forcing_d(1/4,1/3)` with both sides `−1`, each as a *pair* of `norm_num`
examples (LHS and RHS separately against the same rational, which is the right design: a
single `example : LHS = RHS` would close by `norm_num` even if both sides were wrong in the
same way). I re-evaluated both pairs by hand and confirm the values.
**Verdict on deviation 1: correct finding, correct remedy, correctly recorded append-only.**

**Deviation 2 — `Delta_lower_bound` conditional on `hsq`.** Confirmed from the elaborated
signature: `hsq : ∀ s, 0 ≤ s → s < 1 → s^2 ≤ f s` appears in `Delta_lower_bound` and in **no
other declaration** in the development (verified by type inspection, not by reading comments).
`Delta_closed_form_pos` — the MUST-LAND item and the one that carries `Δ(x) > 0` — is
**unconditional**. Nothing depends on `Delta_lower_bound`: it is a leaf declaration.
The hypothesis is *true* (m15), so no vacuity. Per §7.5 an unclosable obligation becoming an
explicit parameter rather than a `sorry` is exactly right.
**Verdict on deviation 2: correctly handled and correctly scoped; nothing over-claimed.**

**P14 flagship chain unconditional?** Yes — established mechanically in §4.9 from the
elaborated types of `f_pos`, `argument_coincidence` and `Delta_closed_form_pos`, and
corroborated by re-proving `0 < Delta x` from `0 < x` and `x < 1/2` alone in my out-of-tree
file. The chain `mul_log_gt → f_pos`, `b_at/e_at/u_at/v_at → argument_coincidence`,
`sStar_pos + sStar_lt_one + f_pos → Delta_closed_form_pos` uses only Mathlib and
`Support.Basic`; no interface field, no `hsq`, no `hbridge`.

---

## 8. FINDINGS

### MAJOR-1 — `blockA_trace_det` is attributed to the wrong manuscript lemma and filed under the wrong node

`WHGAP/private-boundary.lean` heads the theorem "Step 4 — the 2×2 block invariants (supports
paper **Lemma 7.1**)" and its fidelity note calls it "a real symmetric stand-in for the
Hermitian block of paper **Lemma 7.1**". Paper Lemma 7.1 is `lem:holevo` (§7, "Both Holevo
quantities collapse to `f`") and contains **no 2×2 block**. The matrix
`A(ε) = [[1−x, −iβ(1−2ε)], [iβ(1−2ε), x/2]]` with `β = √(x(1−x)/2)`, `tr A = 1 − x/2`,
`det A = 2x(1−x)ε(1−ε)` is `eq:Eexact` of **Lemma 6.1 (`lem:exactspec`, §6 "Positive capacity
below 2/5")** — an ingredient of the *positivity* layer, i.e. of nodes `WHGAP.no-ascent-hierarchy`
(P9) / `WHGAP.qpositive-onset` (P3), not of `WHGAP.private-boundary` (P14). Its `ρ_ε` is the
isotropic `(1−ε)P + εP̄`, not the `diag(1−2ε,ε,ε)` witness of §5/§7.

Consequences: (i) `WHGAP.private-boundary`'s on-disk mechanization note lists
`blockA_trace_det` inside "the FLAGSHIP scalar core … PROVED UNCONDITIONALLY", crediting P14
with machine-checked content that belongs to P9/P3; (ii) `WHGAP.no-ascent-hierarchy`'s note
under-credits by the same amount; (iii) §7.3's placement rule ("anything used by only one node
belongs in that node's module") is violated; (iv) a wrong manuscript cross-reference sits
inside a frozen-Claim-bearing docstring, which is precisely the drift surface §7.6 exists to
protect.

The identity itself is **correct** (I re-derived trace and determinant, and confirmed the
real-symmetric stand-in carries the same two invariants as the Hermitian block). Nothing is
unsound. Fix: move the theorem to `WHGAP/no-ascent-hierarchy.lean`, change "Lemma 7.1" to
"Lemma 6.1 (`lem:exactspec`)", and correct both nodes' `lean:` mechanization notes.

### MAJOR-2 — `WHGAP.no-ascent-hierarchy`'s recorded `lean.state: "composition-checked"` is unbacked

The node file records

```yaml
  composition: null  # leaf
  state: "composition-checked"
```

and `NODE_INDEX.md` row P9 reads `composition-checked rel {hexp}`. **There is no composition
theorem in `WHGAP/no-ascent-hierarchy.lean`** — I read the module and the `Trust.lean` census:
the module declares `d1_at_two_fifths`, `d1_sign`, `exists_pos_of_expansion` and `Claim`, and
nothing else. The block is self-contradictory (`composition: null` vs
`state: "composition-checked"`), and the `rel: hexp` names a hypothesis of a *lemma*, not of a
composition. Compounding it, this module's `Claim` is (by the author's own explicit statement)
**not** the node's frozen Claim but a substituted tier-1 shadow (§4.6) — so "composition-checked"
would be misleading even if a composition existed, on a node that carries **CERTIFIED\***.

Under §7.1 the mechanization state must be displayed accurately with its `rel`; under the
licensing menu, statement (A) asserts "the `lean:` states on the nodes are licensed as
recorded", and for P9 that statement is false as recorded. Fix: set P9's state to `proved`
(for `d1_sign`/`d1_at_two_fifths`/`exists_pos_of_expansion`) + `stated` (for the shadow
`Claim`), keep `rel: [hexp]`, and add one sentence saying the Lean `Claim` is a substituted
shadow, not the node's Claim — the module docstring already says this; the metadata must too.

### Minor findings

**m1 — the shipped checksum ledger does not verify.** `sha256sum -c artifacts/logs_whgap_lean_20260730/SHA256SUMS.txt`
from the repo root reports **24 OK, 1 FAILED** (`sympy_identity_check.log`). Diagnosis: the
ledger header says "SHA-256 over LF-normalized bytes", but all files on disk are CRLF and
**24 of 25 entries are raw-byte hashes**; only `sympy_identity_check.log` was hashed after
LF-normalization. I verified `tr -d '\r' < sympy_identity_check.log | sha256sum` reproduces the
recorded digest exactly, so **no content is altered** — the ledger's convention is simply
mixed, and its header describes the convention only one entry follows. This is R5 §2 standing
failure mode 6. Fix: rewrite the ledger under one stated convention (§7.7 says LF).

**m2 — invalid justification for the P9 Claim substitution.** The module docstring (and the
executor's §5) assert "prose ⟹ (via the contrapositive first-order mechanism) this". The
contrapositive of the node's Claim yields at most `Q(Λ_x) ≠ 0`; turning that into
`∃ c > 0, I.IcLB x c` needs the N1' expansion *and* a converse-to-LSD step (positive capacity ⟹
a positive achievable coherent information), which is in neither the interface nor the module.
The substitution is fine — the justification is not. Say instead: "the Lean `Claim` is the
tier-1 shadow that Theorem 8.1 of the N1' note *produces*, and is what P3 consumes; no
implication from the prose Claim is asserted."

**m3 — `Q^{(1)}` vs `Q` at P13, with a live downstream risk.** The node's frozen conjecture
asserts `Q^{(1)}` statements and says only "*ideally* also `Q = 0` there"; the module docstring
and the executor's §5 both say "the conjecture asserts both". The **Lean is correct** (it
mirrors the parent's composition block, which is a `Q`-determination). The actionable risk:
should someone later prove P13's actual conjecture (`Q^{(1)} = 0` on `[2/5,1)`), that would
**not** discharge `goal.composition`'s `h13`, because `Q^{(1)} = 0` at one blocklength does not
give `Q = 0`. Recommend reconciling P13's frozen Claim with the parent's block, and deleting
"the conjecture asserts both".

**m4 — an undisclosed `P^{(1)} → P` substitution inside the P14 bridge, and a dead interface
field.** `Claim_of_delta_le` takes `hbridge : ∀ x ∈ (0,1/2), Δ x ≤ I.P x`, whereas the prose
and `thm:private` prove `P^{(1)}(Λ_x) ≥ Δ(x)` and then invoke superadditivity for `P ≥ P^{(1)}`.
The honest shape is `hbridge : Δ x ≤ I.Pone x` followed by `I.lsd_devetak`. As written the
theorem is *stronger* (weaker hypothesis), so nothing is unsound — but (i) the §5 table does
not disclose the substitution while the P4 module went out of its way to add
`composition_one_shot` for exactly this distinction, and (ii) **`lsd_devetak` is consequently
consumed by no declaration anywhere** (verified by grep: its only occurrences are its own
definition and a prose mention in `Trust.lean`). An interface field that nothing uses is a
trust-boundary line item with no counterpart in the checked content.

**m5 — `lsd_devetak`'s citation covers only half the field.** "Zhu–Wang eq. (2.6)/(2.7)" are
the *private* definitions; the quantum half is ZW (2.3)/(2.4), and (2.4) displays only the
limit form, so `Qone x ≤ Q x` additionally rests on superadditivity of the coherent information
(which the docstring's parenthetical does mention). Fix the equation numbers to "(2.3)/(2.4)
and (2.6)/(2.7)".

**m6 — `BGSW25` has no local literature record.** It is cited in `Interface.lean` (and is the
sole source of ZW Lemma 3.2, the cBKM→cRE bridge) but has no entry in
`channel-capacity/literature/` — no catalog record, no local PDF. Only the manuscript
bibliography (`main.tex:1220`, Belzig–Gao–Smith–Wu) identifies it. Given that the bridge is
load-bearing for `zw_hrsf_zero`, it should be ingested.

**m7 — the anti-drift checker of §7.6 does not exist.** `tools/whgap_lean_freeze_claims.py --check`
tests only `digest in src` — it would pass an edited docstring body with an intact hash line.
None of §7.6's seven checks (module/file/`Claim`/composition existence; node↔module bijection;
composition parameters covering exactly the propagating children; `composition_via_*` matching
for OR nodes; import graph vs `parents`/`children`; status recomputation) is implemented
anywhere: `tools/proof_dag_check.py` is Lean-unaware (it exits 0 with 16 nodes valid and
mentions `lean:` only to say those blocks are "validated semantically elsewhere" — they are
not). `tools/whgap_r11_claim_audit.py`, written for this review, closes the verbatim-text half
only. Note that MAJOR-2 is precisely a §7.6-check-1/4 failure that an implemented checker would
have caught.

**m8 — mechanization tier not recorded on the nodes.** §7.8: "The tier is recorded in the
project README **and on each mechanized node**." The README declares T1+T2; none of the eight
`lean:` blocks carries a tier field or the words T1/T2.

**m9 — the eight unmechanized nodes are silent, and §7.4 forbids silence.** `WHGAP.antideg-boundary`,
`.relaxed-lift`, `.more-capable-route`, `.choi-distillation-necessary`, `.order-converse`,
`.restricted-order`, `.pure-anchor-order`, `.direction-restricted-order` have **no `## Lean`
section at all**. §7.4: "A non-formalized node records `lean: none` with a reason. Silence is
invalid." `NODE_INDEX.md`'s Lean column carries "none" for them, but with no reason and not on
the canonical node file.

**m10 — `lake-manifest.json` still declares `"name": "ksumAudit"`** while `lakefile.lean`
declares `package whgapDag`. A copied-manifest provenance artifact; harmless to the build
(lake keys off the lakefile) but it misidentifies the project in a committed file that is
itself in the SHA ledger.

**m11 — docstring/name slips.** The doc comment above `prefactor_eq` is headed
"**`prefactor_pos`**"; the P14 module header lists `prefactor_pos` where the README lists
`prefactor_eq`; the README's `WHGAP/Support/Basic.lean` bullet list omits `sqrt_two_spec`.
Cosmetic.

**m12 — `strict_violation_window` carries an unused hypothesis.** `hε0 : 0 < ε` is never used
(build warning, `order-boundary.lean:76:5`); the statement is in fact true for every
`ε < ε_c(x)`. This *strengthens* the theorem, but the docstring's "strict violation window
`0 < ε < ε_c(x)`" describes a hypothesis the proof does not need. Either drop `hε0` and say so,
or keep it and note that it is carried for readability.

**m13 — one README sentence risks reading as full coverage.** "every scalar identity the prose
proofs display — the P14 coincidence and closed form, the P6 threshold, the P2 forcing
identities, the P9 weight sign — is exactly true as written". The apposition bounds it, but the
opening quantifier invites the wrong reading: `eq:charpoly`, the Gram factors `4/25` and `1/3`,
Appendix A's entrywise table and `lem:holevo`'s collapse are all displayed scalar content that
is **not** checked. Suggest "every scalar identity listed below".

**m14 — no satisfiability witness ships with the project.** The executor's own §8.4 flags this.
I supplied and compiled one out-of-tree (§5.3); recommend adding it to `SelfTest.lean` so that
§7.10.5 has an in-tree artifact for the next reviewer.

**m15 — `hsq` is not a genuine gap in the mathematics.** The deviation record says every short
proof of `f(s) ≥ s²` "needs a power series or a two-level derivative-monotonicity argument".
That is fair about Lean's difficulty, but the manuscript already *displays* the series
(`eq:fdef`: `f(s) = Σ_{k≥1} s^{2k}/(k(2k−1))`), whose `k = 1` term is exactly `s²` — so the
paper does not treat this as an open step, and the node's `rel` entry
"`Delta_lower_bound` additionally rel `hsq`" should say the obligation is a *formalization*
gap, not a mathematical one.

---

## 9. Summary of what is and is not licensed

**Established by this review (reproduced, not taken on trust):**

* the build reproduces from deleted WHGAP outputs, `lake build` exit **0**, 491 s, Lean 4.31.0;
* **44/44** top declarations depend on exactly `[propext, Classical.choice, Quot.sound]`;
  zero `sorry`, zero `axiom` declarations, zero `native_decide`/`implemented_by`/`unsafe`/`partial`;
* **8/8** frozen Claims match their node `## Claim` sections in **both hash and verbatim text**,
  by two independent implementations plus a shell-only hand computation on four nodes;
* the import graph equals the propagating skeleton `G ⟸ {P3 ⟸ P9, P4 ⟸ P2, P13}`, `P6 ⟸ P2`;
* every composition theorem's hypotheses are **jointly satisfiable in one explicit non-trivial
  model**, machine-checked; no vacuity anywhere; `conjecturedS` is asserted nowhere;
* every machine-checked scalar identity is **exactly right** and matches its manuscript display
  (`prop:unique`, `thm:spectrum`, §5, `lem:exactspec`, `lem:holevo`, `thm:private`), verified by
  my own hand derivation before reading the author's;
* the **P14 flagship chain is genuinely unconditional** (from elaborated signatures);
  `hsq` is confined to `Delta_lower_bound`; `hbridge` to `Claim_of_delta_le`;
* both executor deviations are correct findings, correctly remedied, correctly recorded;
* the README and report carry the §7.9 sentences verbatim and **nowhere describe a green build
  as proving an original theorem**;
* the ZW/HRSF22 interface citations (Thm 3.3, Lem 3.2 = BGSW25, Cor 3.7, HRSF22 Lem 3.1) match
  the local PDFs statement for statement.

**Not licensed, and blocking licence (A) as worded:** the two MAJORs. `WHGAP.private-boundary`'s
and `WHGAP.no-ascent-hierarchy`'s `lean:` mechanization notes mis-credit `blockA_trace_det`
(MAJOR-1), and P9's recorded `state: "composition-checked"` has no declaration behind it
(MAJOR-2). Once both are corrected — a metadata edit plus, for MAJOR-1, moving one theorem —
the licence sentence "the Lean development is a faithful machine-checked mirror at the stated
tiers; statement fidelity holds for all 8 modules at the granularity losses tabulated; the
build/axiom evidence is sound" would in my judgement be **fully supported**, with the minors
above as non-blocking corrections. The evidence tier of the development itself remains, per
§7.9 and the project's own README, **NUMERICAL** — a green build is a run, and this review
licenses the *fidelity and evidence*, never a capacity theorem.

**Owed by the decision layer (single-writer deviation):** link this report from `WHGAP.goal` and
from each mirrored node (`RESEARCH_STRUCTURE_PROTOCOL.md` §6 step 3, rule 8c); apply the two
MAJOR corrections; then decide the `lean:` attribute statuses. I wrote no node, index, or DAG
file.

---

## 10. Run artifacts

All under `artifacts/logs_whgap_lean_20260730/`, hashed in `SHA256SUMS_r11.txt` (LF):

* `r11_lake_build.log` — command, environment header, full transcript, true exit status, elapsed;
* `r11_forbidden_scan.log` — the 13-pattern forbidden-construct scan;
* `r11_freeze_check.log` — the authoring tool's `--check` output;
* `r11_claim_audit.log` — my independent hash **and verbatim-text** audit;
* `r11_manual_hash.log` — shell-only by-hand SHA-256 of four Claim sections;
* `r11_import_graph.log` — extracted import graph;
* `r11_audit_source.lean` / `r11_audit_lean.log` — the satisfiability model and signature
  audit, and its `lake env lean` output (exit 0);
* `r11_sha_verify.log` — verification of the executor's `SHA256SUMS.txt` (24 OK / 1 FAILED, m1).

Script: `tools/whgap_r11_claim_audit.py`.

