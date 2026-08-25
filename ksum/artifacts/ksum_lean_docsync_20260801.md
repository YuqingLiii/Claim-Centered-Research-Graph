# k-Sum Lean audit — DOCS-SYNC batch (honesty defects D-1 … D-6 + the new manuscript finding)

**Date:** 2026-08-01 · **Role:** executor (fresh Opus 5 instance) · **Scope:** documentation and
docstring level only · **Source of the work order:**
[`ksum/artifacts/ksum_lean_delta_fidelity_review_20260801.md`](ksum_lean_delta_fidelity_review_20260801.md)
§7.2 (honesty defects) and §12.7 (the new manuscript finding).

**No theorem statement was changed. No status field was written anywhere. No `git` command was
run.**

---

## 0. PRE-ACTION REPORT

**Files read from disk, completely, before any edit**, in the order prescribed by
`research/PRETASK_RELOAD_PROMPT.md`: that template; `DAG_PROTOCOL.md` (whole file, §1–§7
including all of §7.10); `research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10);
`ksum/README.md`; `ksum/notes/KSUM_PROOF_DAG.md` (header + "Most recent change");
`ksum/proof-dag/NODE_INDEX.md` (Lean rows); the target node
`ksum/proof-dag/nodes/KSUM.LEAN.statement-fidelity.yaml`; its parent
`KSUM.LEAN.yaml`; the neighbouring nodes touched by the work order (`KSUM.LEAN.T3.obstruction-theorems`,
`KSUM.B1`, `KSUM.A1`); the campaign ledger
`ksum/notes/ksum_lean_campaign_state_20260730.md`; and the delta-fidelity review in full
(837 lines).

- **Target node and status as read from disk:** `KSUM.LEAN.statement-fidelity` — **CERTIFIED\***
  (`status_source`: the 2026-07-31 consolidated review; the 2026-08-01 delta review is applied on
  the node), LEAF, role `tool`, parent `KSUM.LEAN` (**CERTIFIED\***, recomputed 2026-08-01), no
  children.
- **ROLE: executor.** Every item below implements a fix that an **independent** reviewer prescribed;
  I authored none of the reviewed work and I adjudicate none of it.
- **Highest status my evidence could license (§2 ladder):** **none.** A documentation sync produces
  no mathematical evidence. The `lake build` re-run is a *run* and caps at NUMERICAL, which is
  strictly below every status already on these nodes, so it licenses nothing and I wrote nothing.
  The one place where a status *number* is at issue (D-4) is recorded as text and left for the lead.
- **Gates / deliverables, one line each.** D-1 seven Lean files must stop asserting that
  `freeze`/`constQ` are not in the manuscript; D-2 `Trust.lean` must stop saying no `EmbedData`
  field is proved; D-3 the `KSUM.LEAN.T3` frontmatter caveat must be re-graded on rows 8/9/14/29;
  D-3′ the paper's M-10 sentence must stop calling (51) a hypothesis; D-4 `KSUM.B1`'s
  `status_source` and Current status must stop saying the route proof is unwritten, and must record
  the one-rung inconsistency; D-5 `lean/README.md`'s census denominators must be corrected to the
  disk figures with the coverage arithmetic stated unambiguously; D-6 the ledger's CAMPAIGN-CLOSED
  obligations list must be annotated for what batches 1–2 closed; plus the one-sentence manuscript
  justification of `C_h \le 25/19`; then `latexmk`, `lake build`, evidence, records, validators.
- **Conflicts between commission text and disk: three, reported not resolved.**
  1. `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists `git diff --check` among the required closeout
     checks; the commission forbids `git`. **No `git` command was run** — the same standing conflict
     every executor and both reviewers in this campaign have reported. Consequence for this report:
     the change excerpts in §2 are exact before/after pairs captured at edit time, not `git diff`
     output.
  2. **The commission numbers the defects `D-1 … D-7`; the review numbers them
     `D-1, D-2, D-3, D-3′, D-4, D-5, D-6`** — seven items, but with a primed rather than a seventh
     integer label. I have implemented **all seven review items** and mapped them explicitly in the
     table below rather than guessing which one "D-7" meant.
  3. **D-5's prescribed repair figure is itself slightly over-favourable.** The review's
     "~133 unprinted" is formed as `401 − 268`, which subtracts a count of *distinct printed names*
     (268, of which **28 are `def`s**) from a count of *`theorem`+`lemma` declarations* (401). The
     honest split is **240 of 401 theorem/lemmas printed, ~161 unprinted**. Since D-5 is the one
     defect in the delta that errs toward over-stating coverage, writing "~133" would have repeated
     the defect in smaller form. I wrote the split figures and recorded the provenance of both in
     the file itself. **Reported here rather than resolved silently.**

---

## 1. RESULT TABLE

| Item | Review § | Files touched | Verdict |
|---|---|---|---|
| **D-1** freeze/constQ still "NOT IN THE MANUSCRIPT" | §7.2 D-1 | **7 Lean files** (+2 node `rel` fields, see note) | **DONE** |
| **D-2** `Trust.lean`: "none of them is proved here" for `EmbedData` | §7.2 D-2 | `KSUM/Trust.lean` | **DONE** |
| **D-3** `KSUM.LEAN.T3` frontmatter caveat stale in four places | §7.2 D-3 | `KSUM.LEAN.T3.obstruction-theorems.yaml` | **DONE** |
| **D-3′** paper M-10 sentence still calls (51) a hypothesis | §7.2 D-3′, §4.1(4) | `paper/ksum_small_alphabet.tex` | **DONE** |
| **D-4** `KSUM.B1` says the route proof is unwritten; one-rung inconsistency | §7.2 D-4, §9 | `KSUM.B1.yaml` | **DONE (text); status left to the lead)** |
| **D-5** README census denominators stale AND over-stating | §2.3, §7.2 D-5 | `lean/README.md`, `KSUM/Trust.lean` | **DONE, sharpened** |
| **D-6** ledger CAMPAIGN-CLOSED list un-annotated | §7.2 D-6 | `notes/ksum_lean_campaign_state_20260730.md` | **DONE** |
| **Manuscript finding** `C_h \le 25/19` justification | §3.B row 6, §12.7 | `paper/ksum_small_alphabet.tex` | **DONE** |
| `latexmk -pdf -interaction=nonstopmode` | — | — | **exit 0**, warnings delta **0**, 37 pages |
| `lake build` | — | — | **exit 0**, **3017 jobs**, **0** warnings |
| `#print axioms` | — | — | **283 records / 268 distinct names, 0 non-standard** |
| validators | — | — | `proof_dag_check --problem ksum` **0**, `--problem all` **0** (293 nodes), `literature_check` **0** |

---

## 2. PER-ITEM DETAIL, WITH THE EXACT TEXT CHANGED

### D-1 — `freeze` and `constQ` are facts (iii) and (iv), not unstated principles

The review's location list is seven Lean files. All seven were edited. The replacement wording is
uniform in substance: **stated in the manuscript as facts (iii)/(iv) since v5.2 (2026-07-31
manuscript-repair batch, items M-1/M-2, discharging audit findings F1/F2), originally
interface-only**; and, per §3.B of the review, `freeze` is rendered precisely as **facts (i)+(iii)
composed at the last position** (restrict to the singleton product subdomain, then delete the
now-singleton coordinate), not as fact (iii) alone.

Verification that the false assertion is gone: `grep -rni "unstated|NOT IN THE MANUSCRIPT|NOT
STATED IN|does not state|but does not state"` over all 37 `.lean` sources outside `.lake/` now
returns **six hits, every one of them in the historically-correct frame** ("originally the unstated
principle F1, stated in the manuscript since v5.2" / "an unstated one"). Zero hits assert present
absence from the manuscript.

**1. `KSUM/Interface.lean` L27, L34** — the per-field citation table.

> before
> ```
>   `freeze`      **NOT STATED IN THE MANUSCRIPT** — finding **F1** of  UNSTATED FACT, carried as
>                 the 2026-07-30 T1 audit.  `lem:oddN` freezes a        an interface field until
>                 coordinate, which changes the INPUT LENGTH and is     `sec:prelim` is repaired
>                 therefore not an instance of fact (i) as printed.
>                 Manuscript repair: one sentence in `sec:prelim`.
>                 …
>   `constQ`      **NOT STATED IN THE MANUSCRIPT** — finding **F2**.    UNSTATED FACT, same status
> ```
> after
> ```
>   `freeze`      `sec:prelim` facts **(i) + (iii)** composed at the    PRELIMINARY FACTS, cited
>                 last position: restrict to the product subdomain      (STATED IN THE MANUSCRIPT
>                 whose last factor is a singleton (fact (i)), then     since v5.2)
>                 delete that now-singleton coordinate (fact (iii),
>                 *singleton-coordinate deletion*).  **Originally
>                 interface-only:** audit finding **F1** … The
>                 manuscript-repair batch of 2026-07-31 (item M-1)
>                 added fact (iii) with exactly that
>                 not-an-instance-of-(i) note, so F1 is DISCHARGED …
>   `constQ`      `sec:prelim` fact **(iv)**: a constant function has   PRELIMINARY FACT, cited
>                 `Q = 0` … **Originally interface-only** — audit       (STATED IN THE MANUSCRIPT
>                 finding **F2** — until the 2026-07-31                 since v5.2)
>                 manuscript-repair batch (item M-2) …
> ```

**2. `KSUM/Trust.lean` L53, L55** — the §(b) trust table.

> before: `freeze … **NOT IN THE MANUSCRIPT** (audit finding F1)` / `constQ … **NOT IN THE
> MANUSCRIPT** (audit finding F2)`
> after: `freeze   coordinate freezing = facts (i) + (iii) composed at the last position` →
> `sec:prelim — CITED (STATED since paper v5.2; originally interface-only, audit finding F1,
> discharged by manuscript repair M-1)`; `constQ … sec:prelim fact (iv) — CITED (STATED since paper
> v5.2; originally interface-only, audit finding F2, discharged by manuscript repair M-2)`

**3. `KsumAudit/QueryModel.lean`** — the structure docstring and both field docstrings.

> before (structure): `Fields `freeze` and `constQ` are two further elementary facts that the paper
> *uses* but does not *state*; … reported as a finding of the audit.`
> after: `… **originally interface-only** — they were findings F1 and F2 of this audit, facts the
> paper used but did not state — and **stated in the manuscript as facts (iii) and (iv) since
> v5.2** (2026-07-31 manuscript-repair batch, items M-1/M-2).`
>
> before (`freeze` field): `**Frozen coordinate.**  NOT stated in `sec:prelim`. …`
> after: `**Frozen coordinate.**  `sec:prelim` facts **(i) + (iii)** composed at the last position:
> restrict to the product subdomain whose last factor is the singleton `{a}` (fact (i)), then
> delete that now-singleton coordinate (fact (iii), *singleton-coordinate deletion*). … **Originally
> interface-only:** … Paper v5.2 states fact (iii) with exactly that not-an-instance-of-(i) note …
> so F1 is DISCHARGED …`
>
> before (`constQ` field): `**A constant function has query complexity `0`.**  NOT stated in
> `sec:prelim`; …`
> after: `… `sec:prelim` fact **(iv)**; used by `thm:oabarrier` …, whose proof now cites it.
> **Originally interface-only:** finding **F2** …; F2 is DISCHARGED.`

**4. `KSUM/A1.lean` L19, L50, L133, L267** *(pre-edit line numbers, as listed by the review)* —
the `rel` display in the header, the gate-G-R3 hypothesis table, the `composition` docstring, and
the `holds` docstring.

> before (×4, in substance): `QueryModel.freeze (= the UNSTATED coordinate-freezing principle, F1)`
> / `the unstated freezing principle` / `and the unstated coordinate-freezing principle F1` /
> `` `M.freeze` is the unstated coordinate-freezing principle F1``
> after (×4): `QueryModel.freeze (= sec:prelim facts (i)+(iii) composed at the last position —
> coordinate freezing; STATED in the manuscript since v5.2, originally interface-only as audit
> finding F1)` and the three corresponding prose forms.

**5. `KSUM/B1.lean` L16, L138, L198** *(pre-edit)* — same three shapes.

**6. `KSUM/Support/Freeze.lean` L13** — the module header.

> before: `That field is **finding F1** of the 2026-07-30 T1 audit: the manuscript does not state a
> coordinate-freezing principle, and fact (i) as printed does not cover it …`
> after: `That field is `sec:prelim` facts **(i) + (iii)** composed at the last position … .
> **Originally interface-only.**  It was **finding F1** … the manuscript *then* stated no
> coordinate-freezing principle … — and paper v5.2 supplies it: the 2026-07-31 manuscript-repair
> batch (item M-1) added fact (iii) with the explicit "this is *not* an instance of (i)" note, so F1
> is DISCHARGED.  The dependence is still carried visibly, in the type of every theorem that uses
> it, and never hidden.`

**7. `KsumAudit/MainLine.lean` L14** *(pre-edit)* — the module header's conditionality sentence.

> before: `(`Q` itself, `sec:prelim` facts (i)/(ii), the two extra elementary facts F1/F2 the paper
> uses but does not state, and the imported bounds …)`
> after: `(`Q` itself, `sec:prelim` facts (i)–(iv) — the last two, `freeze` = (i)+(iii) and
> `constQ` = (iv), were **originally interface-only**, audit findings F1/F2, and are STATED in the
> manuscript since v5.2 — and the imported bounds …)`

**Extension beyond the seven files, and why.** The review's *consequence* paragraph and its
recommendation 2 ask for the standing conditionality statement to be restated **repo-wide**.
`grep` found the same false assertion in the current-state `rel` displays of two node files, where
leaving it would have created a fresh Lean-vs-node inconsistency the moment the seven files were
fixed. Both were updated:

- `KSUM.A1.yaml` — `composition.rel[3]` and `lean.rel[3]`;
- `KSUM.B1.yaml` — `lean.rel[2]`.

**Deliberately NOT touched:** the same phrasing inside *dated Work-record / Status-history entries*
(`KSUM.A1.yaml` L167 and L209, `KSUM.B1.yaml` L120, `KSUM.LEAN.yaml` L158, `notes/KSUM_PROOF_DAG.md`
L283). Those are append-only history recording what was believed on the date written, and
`RESEARCH_STRUCTURE_PROTOCOL.md` §7 forbids overwriting cited history. The conditionality display
that a reader *acts* on is the frontmatter `rel`, and that is now correct everywhere.

**Net effect on the record.** The development's standing conditionality now reads, consistently in
Lean and on the nodes: **conditional on ABI21 + Tani24 + `sec:prelim` facts (i)–(iv), all four
stated** — a strictly better position than the record previously claimed, which is why the review
graded D-1 conservative.

### D-2 — `Trust.lean` §(b): `EmbedData` fields are no longer all unproved

> before
> ```
> Its fields `enc`, `enc_inj`, `k_dvd_P`, `two_mul_Mv`, `cP_pos`, `P_lower`,
> `P_upper` are properties of the manuscript's explicit payload/tag formulas, each cited in its
> docstring, and none of them is proved here.
> ```
> after
> ```
> … each cited in its docstring.
> **Since gap-closure batch 2 (2026-08-01) the structure is no longer trust-only:**
> `KSUM.Support.genEmbed` CONSTRUCTS an `EmbedData` from the manuscript's own parameter display for
> every `k ≥ 3`, `n ≥ 1`, `R ≥ 2`, discharging `enc_inj`, `k_dvd_P`, `two_mul_Mv`, `cP_pos`,
> `P_lower` and `P_upper` as theorems (`embed_enc_inj`, `embed_two_mul_M`, `embed_P_lower`,
> `embed_P_upper`, …), with `c_P = k(k-1)2^{k-2}` depending only on `k`; `demoEmbed` is the earlier
> single instance.  What is STILL NOT proved anywhere is the **encoding identity** of `prop:embed`
> (`kSum_{Z_q,0,kn}(encoded) = Coll_{k,n→R}(g)`): that is `KSUM.A2a.Claim`/`KSUM.A2b.Claim`, and
> both remain `def Claim : Prop` with no proving theorem in this development.
> ```

The second half is deliberate: the review's **C-1** is precisely that the census credited
`genEmbed` to `prop:embed` when the encoding identity is unformalized, so the corrected sentence
states what *is* proved and what is not in the same breath.

### D-3 — `KSUM.LEAN.T3` frontmatter caveat, re-graded on rows 8/9/14/29

Four clauses of the 2026-07-31 caveat were withdrawn with their replacement grounds named, and the
live residuals were restated. Withdrawn: `(iii) rho<=4/5 ASSUMED` (row 9: derived via the
manuscript's own three-weight step, both weight ratios now theorems); `transfer (G2)
satellite-replaced-by-augmentation-submodule (Maschke granted)` (row 29: the bridge is proved,
Maschke granted nowhere, and the Lean hypothesis is *weaker* than (52)'s summand form so the
theorem is stronger); `kernel does NOT confirm the orientation obstruction` (row 14: the step
producing (51) is proved and the derived exponent `1−r(m−1)−m` equals the paper's `r+1−m(r+1)`);
`or the tilted-band witness` (row 8: the outer half is hypothesis-free, both displayed bounds
included). Retained as the live caveat: still NARROWER at 6 labels / 9 clauses; the residuals are
the inner pair tensor as a measure on `ℤ_q^N`, the `genPoly`↔phase identification, `hident`, block
clause (i)'s `m`-fold multivariate Vandermonde, and the `S_N`-average operator.

**The node's `status:` field was not touched** — CERTIFIED\* before and after. The caveat is the
honesty display attached to it, and the review explicitly made this re-grading call itself
("*I make it here*"), which is what licenses an executor to type it.

### D-3′ — the paper's M-10 sentence

> before
> ```
> it does \emph{not} confirm the orientation obstruction, the
> block degree and $\rho_j$ clauses, or the tilted-band witness, whose analytic inputs --- among
> them the bound~(51) in the proof of Theorem~\ref{thm:orientation-obstruction} --- enter the
> formalization as hypotheses, not as proved content.
> ```
> after
> ```
> it does \emph{not} confirm the orientation obstruction, the
> block degree and $\rho_j$ clauses, or the tilted-band witness as whole statements. Their
> \emph{analytic} inputs are, however, now proved rather than assumed: the step producing the
> bound~(51) …, the derivation of $\rho_j\le4/5$ from the tilted inner weights, and the outer
> functional of Theorem~\ref{thm:tilted-log-band} together with both displayed constants
> $C_h\le25/19$ and $\sum_jA_j\le29/23$. What those clauses still take as hypotheses is
> \emph{structural} rather than analytic --- which measure a block carries, the identification of
> the constructed generating polynomial with the phase function, and the inner pair tensor as a
> measure on $\Zq^N$ --- and it is only for want of these that the named clauses are not confirmed
> end to end.
> ```

The negative claim ("does not confirm …") is **retained**, only re-scoped to *whole statements*,
which is what the review's §4.1(4) says is true; the analytic/structural split is the review's own
distinction.

### D-4 — `KSUM.B1`: the route proof is written

`status_source` and `## Current status` both asserted that the route proof "is statable and
near-trivial, but unwritten and unreviewed", four lines above a `lean.note` recording that it was
written. Both were corrected to state that `composition_via_A1_inputs` + `holds` exist and deliver
the absolute `C = 4`, that the route is nonetheless **unreviewed** (which is why the composition
entry sits at NUMERICAL with `review: null`), and that §1 therefore computes
`min(A1 = PROVED, route = NUMERICAL) = NUMERICAL · pending-review` — **one rung above the displayed
CONJECTURED**.

**The `status:` field was left at CONJECTURED.** The discrepancy is conservative (nothing
downstream can be over-claimed by a value that is too low), the recompute would have to propagate
to `KSUM.goal`, `NODE_INDEX.md`, the Mermaid and the outline in one diff, and my commission forbids
status writes. The inconsistency is now visible on the node instead of implicit.

### D-5 — census denominators (the one non-conservative defect)

Counts were recomputed from disk by a comment-stripping parse of all 37 `.lean` sources outside
`.lake/`, and the `#print axioms` records were counted from **my own build log** (§3), not from any
report:

| quantity | old README text | **disk, 2026-08-01** |
|---|---|---|
| `#print axioms` directives → printed lines | "283 declarations" | **283 directives → 283 lines** |
| distinct declaration names printed | *(absent)* | **268** (15 printed twice: owning module + `Trust.lean`) |
| of those, `theorem`/`lemma` | *(absent)* | **240** |
| of those, `def` | *(absent)* | **28** (the `Claim`s, `demoModel`, `sandwichModel`, `genEmbed`, `demoEmbed`, …) |
| `theorem` + `lemma` in the sources | "276" | **401** (294 + 107) |
| all named declarations | "377" | **569** |
| `example` witnesses | "96" | **127** |
| unprinted | "~80" | **~161 theorem/lemmas** |

Both `lean/README.md` L123 and `KSUM/Trust.lean`'s header carried this arithmetic; **both** were
corrected (the review flagged only the README, but the header is a second copy of the same claim
and was stale by a wider margin: 237/318/438/105 and "36 files"). The README row now states
explicitly: *"Do not compare 283 against the theorem count: 283 counts lines, 268 counts names, 240
counts theorems"*, so the "283 > 276 ⇒ total coverage" misreading is closed at the source.

**Deviation from the prescribed repair, disclosed.** The review's own figure "~133 unprinted"
is `401 − 268` and mixes kinds; the honest split is 240/401 printed, ~161 unprinted. I wrote the
split and recorded the provenance of both figures in each file, because writing "~133" would have
reproduced D-5's defect in smaller form. This is a change **in the conservative direction** — it
claims *less* coverage than the review's repair would have.

**Soundness of the census is unaffected and is restated in both files:** every unprinted
declaration is a helper that some printed result transitively depends on, and `#print axioms`
reports the axioms of the whole dependency closure.

### D-6 — ledger CAMPAIGN-CLOSED obligations list

Strikethroughs were added in place for the items batches 1 and 2 closed (matching the convention
already used there for the manuscript-repair item), and a boxed **ANNOTATION** table was appended
immediately below the list giving the 2026-08-01 state of every item: census table **DONE**; FILT
**DONE**; JOINTLP duals **DONE** (18 still not kernel-checked, `(5,4,1)`-single bounded not
decided); tilted-band **OUTER HALF DONE**; orientation (51) **DONE**; block (iii) `ρ` **DONE**;
block (i) **STILL OPEN**; `prop:embed` **PARTIAL** (encoding identity still unformalized); B2
`k`-uniformity **DONE**; B1 route **WRITTEN, unreviewed**; rosmanis **STILL OPEN**; the three prose
items **STILL OPEN**. The original list text is preserved — nothing was deleted.

### Manuscript finding — the `C_h \le 25/19` justification

The review's §3.B row 6 established that the printed one-liner does not deliver the constant:
applied flat to `d = 1,…,h`, `∏(1−x_i) ≥ 1−∑x_i` gives only `∏(1−5^{−d}) ≥ 1 − 1/4 = 3/4`, i.e.
`C_h ≤ 4/3 = 1.3333 > 25/19 = 1.31578`. The bound is true (`C_∞ ≈ 1.31520`) and the Lean proof
(`KsumAudit.Obstructions.TiltedBand.Cfac_le`, via `tail_geom`/`tail_geom_le`) gets it by peeling the
`d = 1` factor exactly and bounding only the tail. That step is now printed, in the paper's voice:

> before
> ```
> The elementary inequality $\prod_i(1-x_i)\ge1-\sum_i x_i$ gives $C_h\le25/19$, while
> ```
> after
> ```
> The elementary inequality $\prod_i(1-x_i)\ge1-\sum_i x_i$ gives $C_h\le25/19$, but only after the
> $d=1$ factor is peeled off exactly and the inequality applied to the tail alone: this yields
> $\prod_{d=1}^h(1-5^{-d})\ge\tfrac45\bigl(1-\sum_{d\ge2}5^{-d}\bigr)=\tfrac45\cdot\tfrac{19}{20}
> =\tfrac{19}{25}$, whereas applying it flat to all of $d=1,\dots,h$ would give only
> $\prod_{d=1}^h(1-5^{-d})\ge\tfrac34$, i.e.\ the weaker $C_h\le4/3$.  Meanwhile
> ```

Arithmetic re-derived here before writing: `∑_{d≥2}5^{−d} = (1/25)/(1−1/5) = 1/20`;
`(4/5)(19/20) = 19/25`; `(19/25)^{−1} = 25/19`. The theorem statement, the constant, and every
subsequent display (`437/581`, `437/581 − 3/4 = 5/2324`) are **unchanged**.

### View sync (DAG protocol §5.4 — obligatory, not optional, in this same change)

Fixing D-1 and D-3 on the canonical node files would have left the whole-graph views asserting the
opposite, which §5.4 forbids ("the canonical node files, `NODE_INDEX.md`, Mermaid and text outline
describe the SAME graph; edit all affected views in the same diff"). Three views carried the same
stale text and were synced:

- `notes/KSUM_PROOF_DAG.md` **Mermaid** — `LeanT1`'s label said *"two UNSTATED paper facts (freeze,
  constQ)"* and *"conditional on ABI/Tani + facts (i)/(ii) + F1/F2"*; `LeanT3`'s label carried the
  four withdrawn clauses. Both relabelled. **No `class`, no status word, no edge changed** — the
  Mermaid graph is byte-for-byte the same graph.
- `notes/KSUM_PROOF_DAG.md` **nested outline** — the `LeanT1` bracket and the `LeanT3` fidelity
  paragraph, the latter now carrying the 2026-08-01 re-grading with the analytic/structural split.
- `proof-dag/NODE_INDEX.md` **`LeanT3` note** — it listed only batch 1's closures and still named
  `thm:block-obstruction` (iii) and the convolution reduction as open; both were closed by batch 2.

`notes/KSUM_PROOF_DAG.md`'s **"Most recent change"** header was updated to describe this batch, with
the gap-closure-batch-2 header demoted to "Previous change" rather than deleted. Both explicitly
record **NO STATUS MOVED and the graph unchanged**.

---

## 3. BUILD AND COMPILE EVIDENCE

### 3.1 `lake build`, run from `ksum/lean/`

- **True exit status `0`** (captured as `EXIT_STATUS=0`, not inferred from the last line).
- Final line: **`Build completed successfully (3017 jobs).`** — identical to the batch-2 and
  delta-review figure, as expected for a docstring-only change.
- `grep -c '^warning' → 0`; `'^error' → 0`; `sorry`/`sorryAx` → **0**.
- Transcript: [`logs_ksum_lean_docsync_20260801/build.log`](logs_ksum_lean_docsync_20260801/build.log).

### 3.2 `#print axioms`, counted from this build's own log

**283 records**, **268 distinct declaration names**, **0 outside Lean's three standard axioms**:

| axiom set | records |
|---|---|
| `[propext, Classical.choice, Quot.sound]` | 257 |
| `[propext, Quot.sound]` | 15 |
| *does not depend on any axioms* | 6 |
| `[propext]` | 4 |
| `[Quot.sound]` | 1 |
| **total** | **283** |

Per-source directive counts (comment-stripped parse, matching the log line-for-line):
`KSUM/Trust.lean` 117, `KsumAudit/MainLine.lean` 29, `ObstructionsTransfer` 21,
`FactorialFiltration` 19, `ObstructionsTiltedBand` 17, `ObstructionsBandMult` 15,
`ObstructionsOrientation` 13, `ObstructionsBlock` 13, `ObstructionsPairTensor` 9, `JointLP` 8,
`ObstructionsProduct` 7, `KSUM/Support/Embed.lean` 6, `KSUM/B2.lean` 5, `KSUM/B1.lean` 4 = **283**.

*Minor correction to the delta review, for the record and not affecting its verdict:* its §2.2
breakdown lists the three-axiom set ×235, and its five categories sum to 261 rather than 283 — a
parse artifact from records that wrap across log lines. Its headline figures (283 lines / 268
distinct names / all standard) are exactly reproduced here; only the per-set split differs (257,
not 235).

### 3.3 `latexmk -pdf -interaction=nonstopmode ksum_small_alphabet.tex`

Baseline captured **before** any edit, in the same session
([`latex_baseline.log`](logs_ksum_lean_docsync_20260801/latex_baseline.log)), and re-run after
([`latex_after.log`](logs_ksum_lean_docsync_20260801/latex_after.log)):

| | baseline | after |
|---|---|---|
| exit status | **0** | **0** |
| `Warning` (final pass) | 0 | **0** |
| `Overfull \hbox` | 3 | **3** |
| `Underfull` | 0 | **0** |
| undefined references | 0 | **0** |
| pages | 37 | **37** |

**Warnings delta 0.** The three `Overfull \hbox`es are the pre-existing ones and are
**byte-identical in magnitude** — 13.64317pt (lines 350–352), 15.30252pt (403–412), 35.55777pt
(1404–1407 → **1415–1418**, shifted only by the 11 lines this batch added above them). `latexmk`
ran `pdflatex` twice because the added text moved a label; the transient
`LaTeX Warning: Label(s) may have changed` is resolved by that rerun and is absent from the final
pass.

---

## 4. WHAT WAS DELIBERATELY NOT DONE

- **No status field anywhere.** In particular `KSUM.B1` stays CONJECTURED though §1 computes
  NUMERICAL·pending-review (D-4), and `KSUM.LEAN.T3` stays CERTIFIED\* with a re-graded caveat.
- **No theorem, definition, or proof term was edited.** Every Lean change is inside `/- … -/`
  or `/-- … -/`. The unchanged 3017-job build with unchanged axiom census is the check.
- **No frozen Claim text and no `claim_hash` was touched**; the validator's hash-drift check (an
  ERROR since the 2026-07-31 closeout batch) passes at 0 drift.
- **No `git` command** (see §0 conflict 1).
- **The census table `ksum/artifacts/ksum_lean_census_20260731.md` was not edited** — the review's
  C-1…C-4 corrections were applied by the lead on 2026-08-01 and are outside this commission.
- **Review recommendations 6 and 8 were not attempted** (the two cheap Lean closures
  `opt_s541_single_d2` + LP monotonicity, and `oabarrier_kSum_Q`): they are *theorem* work, which
  this commission excludes.

---

## 5. FILES CHANGED

| File | Item(s) |
|---|---|
| `ksum/lean/KSUM/Interface.lean` | D-1 |
| `ksum/lean/KSUM/Trust.lean` | D-1, D-2, D-5 |
| `ksum/lean/KsumAudit/QueryModel.lean` | D-1 |
| `ksum/lean/KSUM/A1.lean` | D-1 |
| `ksum/lean/KSUM/B1.lean` | D-1 |
| `ksum/lean/KSUM/Support/Freeze.lean` | D-1 |
| `ksum/lean/KsumAudit/MainLine.lean` | D-1 |
| `ksum/lean/README.md` | D-5 |
| `ksum/proof-dag/nodes/KSUM.A1.yaml` | D-1 (`rel` displays) |
| `ksum/proof-dag/nodes/KSUM.B1.yaml` | D-1 (`rel`), D-4 |
| `ksum/proof-dag/nodes/KSUM.LEAN.T3.obstruction-theorems.yaml` | D-3 |
| `ksum/proof-dag/nodes/KSUM.LEAN.statement-fidelity.yaml` | Work record (this batch) |
| `ksum/proof-dag/nodes/KSUM.LEAN.yaml` | Work record (this batch) |
| `ksum/notes/ksum_lean_campaign_state_20260730.md` | D-6, campaign-ledger line |
| `ksum/notes/KSUM_PROOF_DAG.md` | view sync (Mermaid `LeanT1`/`LeanT3` labels, outline, "Most recent change") |
| `ksum/proof-dag/NODE_INDEX.md` | view sync (`LeanT3` note) |
| `ksum/paper/ksum_small_alphabet.tex` | D-3′, `C_h ≤ 25/19` justification |
| `ksum/paper/ksum_small_alphabet.pdf` | regenerated |

Hashes (LF and RAW) for all of the above and for the three logs:
[`logs_ksum_lean_docsync_20260801/SHA256SUMS.txt`](logs_ksum_lean_docsync_20260801/SHA256SUMS.txt).

---

`DOCSYNC RESULT: D-1 7 files fixed (+2 node rel displays) | D-2..D-7 done: D-2 Trust EmbedData, D-3 T3 caveat re-graded on rows 8/9/14/29, D-3' paper M-10 (51) sentence, D-4 B1 route-proof text + one-rung inconsistency recorded (status untouched), D-5 README+Trust denominators corrected and sharpened (240/401 printed, ~161 unprinted, not the review's ~133), D-6 ledger CAMPAIGN-CLOSED list annotated | paper sentence applied, latexmk exit 0, warnings delta 0, 37 pages, 3 pre-existing Overfull hboxes byte-identical | build exit 0 / 3017 jobs / 0 warnings / 283 axiom records, 268 distinct names, 0 non-standard | validators 0,0,0`
