# WHGAP review commission R3 — independent adjudication of the P4 zero-capacity assembly note (2026-07-28)

**Node (rule 8a):** `WHGAP.zero-capacity-application`. **This review is the rule-6 completion
gate** for that node: no CERTIFIED*/PROVED/REFUTED may be written anywhere without citing THIS
review, completed and archived.

**Reviewer identity (rules 2/6):** a FRESH codex session. The reviewed note was authored by the
DECISION LAYER (a different model and session lineage from you); you did not author it and are
given no desired outcome. The mandate is to adjudicate correctness, completeness, citation
accuracy, and licensing — nothing else. You write NO node statuses; you produce an immutable
report. Status application is a separate decision-layer step citing the report.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.zero-capacity-application`,
ROLE = reviewer. No work before its PRE-ACTION REPORT (including your independence statement).
Disk overrides this commission on any conflict.

## Reviewed object and frozen inputs

- **The note under review (a PROSE PROOF):**
  `channel-capacity/werner-holevo-gap/notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md`.
- Frozen inputs it builds on (verify quotes and licensed scopes, do not re-review their
  internals): the R2 review `artifacts/whgap_p2_review_20260728.md` (its licensing statements
  1–4 and claim-9 obligation list are the contract this note must satisfy) and the P2 artifact
  `artifacts/whgap_signed_lift_extension_20260728.md` (formula source for the lift family).
- Literature ground truth: the local Zhu–Wang PDF
  `channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf` —
  encrypted with an EMPTY password; `pypdf` IS installed for
  `"C:<home>/cpython3119/python.exe"`: use `PdfReader(path)`, `.decrypt('')`, then
  per-page `.extract_text()`. Statement-level cross-checks against Theorem 3.3, Remark 3.4,
  Lemma 3.2, Corollary 3.1, Corollary 3.7, Lemma 4.1, Proposition 4.2, Theorem 4.3, and the
  §3.1 tensorization quote are REQUIRED. RK24 has no local PDF: treat every RK24-dependent
  statement as cite-only and say so in the verdict.

## Claims under adjudication (verdict each: PASS / MINOR / MAJOR / GAP)

1. **Theorem statement well-posedness:** P^(1)/Q^(1) conventions match Zhu–Wang Theorem 1.1/4.3;
   the claimed range x in [1/2, 1) and the blocklength quantifier are stated unambiguously.
2. **(F1)-(F4) quoting:** each quoted fact is (i) actually established in the P2 artifact and
   (ii) within the PROVED scope licensed by R2 statements 1–3 — no quote exceeds its license.
   Independently re-verify (F4) and the explicit (p,q,c1,c2,c3) forced-point formulas by a short
   exact sympy computation (intertwining residual on all nine matrix units at symbolic x, and
   Lambda_x(1), Lambda_x^c(1)).
3. **(H1)-(H3) hypothesis check** against the PDF's Theorem 3.3 as stated (all hypotheses named
   there are covered; none is silently weakened).
4. **Obligation O1** (CPTP + chosen complement): verify the Kraus-sum identity exactly (sympy)
   and the Stinespring construction's two partial traces.
5. **Obligation O2** (tensor powers): the reordering-isometry argument and the
   uniqueness-up-to-environment-isometry step — is the freedom invoked actually the one the
   PDF's §3 machinery uses? Name any gap between "a complement" and "the complement" anywhere
   in the chain.
6. **Obligations O3–O5** (complete quantifier; private step; coherent step): the support
   inclusion arguments (p_u rho_u ⪯ rho-bar; purification with full-rank reference), the
   term-by-term Holevo comparison, and the pure-input floor I_c = 0. Check each against the
   PDF's own Corollary 3.7 / Theorem 4.3 proof pattern — does the note's argument match what
   those statements actually require, with no borrowed step left uncited?
7. **Obligation O6** (tensorization orientation + regularization): the orientation matches the
   PDF's §3.1 display; the capacity limits are the cited regularizations.
8. **Obligation O7 + Corollary:** endpoint exclusion at x=1 is forced by (H1)/Lemma 3.2; the
   Corollary's use of RK24 for x=1 is clearly flagged as cite-only; the gap-closure sentence
   ({x: Q=0} ⊇ [1/2,1]) follows from the Theorem + that endpoint remark.
9. **No-overclaim audit:** the note's caveats (no WLOG lemma; HRSF22 not locally audited;
   x < 1/2 untouched) are consistent with R2's licensing; nothing in the note asserts beyond
   them.

## Mandatory review-quality checklist (rule 7, embed-and-execute; a review missing any item opens NO gate)

- **(7a) Type audit.** For every displayed identity IN THE NOTE (J_x block form, the Stinespring
  isometry and both partial traces, the defect definition, the Holevo/coherent-information
  expressions): domain, codomain, dimensions as functions of x and n. Verify the note's objects
  are well typed at tensor power n, not only n=1.
- **(7b) Regime-complete gates.** Exact spot-checks at x in {1/2, 26/51, 4/7, 3/4} and a symbolic-x
  check of (F4) and the intertwining residual; state which regimes of the ASSEMBLY (large n,
  x near 1, rank-deficient inputs in O4/O5) are argued purely by cited theorems and therefore
  inherit their hypotheses — name each explicitly as tested/inherited/untested.
- **(7c) Anchoring ban.** BEFORE opening the note: from the PDF's Theorem 3.3 + the R2 review's
  claim-9 obligation list alone, write your OWN outline of what a complete assembly must
  establish (the checklist you would demand). Freeze it to disk (hash it), then read the note
  and compare item by item. Flag anything your outline demands that the note lacks, and
  anything the note contains that your outline would not license.
- **(7d) No frozen-input immunity.** R2's licenses are scoped — quote their scope lines when
  checking (F1)-(F4). Any use of a P2/R2 fact outside its licensed scope is a finding, not a
  footnote.
- **(7e) Standing failure-mode list (check every one):** dropped/extra normalization; type or
  dimension mismatch; undefined terms ("admissible pair", "optimized private information",
  "complement", "regularization"); partial objects for full ones (n=1 statements silently used
  at tensor power n; a single reference where "every finite reference" is needed); values
  standing in for formulas; sign/orientation drift in the ⪰ orders (which channel dominates
  which — the single most dangerous flip in this note); citation laundering (a claim attributed
  to a theorem whose PDF statement does not contain it).
- **(7f) Value-vs-formula decoupling.** Your sympy spot-checks verify formulas; your PDF
  cross-checks verify statements; the note's logical assembly is verified by your own outline
  comparison. Say which of the three established each verdict.
- **(7g) Quantifier hygiene.** Every quantifier in the Theorem and in O3-O6 (every n, every
  finite reference, every admissible pair, every ensemble, sup over inputs) resolves to a
  definition in the note or the PDF; check resolvability and that no quantifier is narrowed
  mid-proof.

## Deliverables

1. Immutable report `artifacts/whgap_p4_review_20260728.md`: per-claim verdicts for 1–9; your
   frozen pre-reading outline (or its hash + file link); the tested/inherited/untested regime
   list; and a licensing statement in the exact form: "this review does / does not open the
   completion gate for <statement>, at tier <CERTIFIED* / PROVED>, with scope <...>" — covering
   separately (i) the Theorem (Q=P=0 on [1/2,1)) and (ii) the gap-closure Corollary.
2. Your scripts + logs under `artifacts/logs_whgap_p4_review_20260728/` with SHA256SUMS.txt
   (including the frozen outline file).
3. Append a dated entry to the node's `Adversarial reviews` section linking the report. No
   status writes anywhere.
4. Run `tools/proof_dag_check.py --problem werner-holevo-gap` and `tools/literature_check.py`
   with the pinned interpreter (both must exit 0).
5. Print `FINAL: REVIEW-COMPLETE` or `FINAL: FAILED — <reasons>`.

**Executor:** codex CLI, one sequential session, workspace-write, NO network; Python
`"C:<home>/cpython3119/python.exe"` (CPython 3.11.9; pinned stack + pypdf 6.14.2).
Budget <= 60 min; stop-loss on two info-free cycles or budget breach.

