/-
`KSUM/Interface.lean` — the trust boundary of the node-linked formalization.

This module contains **no invented proofs**.  It re-exports the abstract query-model interface
of the manuscript audit (`KsumAudit.QueryModel`, written for tier T1 on 2026-07-30) under a
stable path so that every node module imports the interface from one place, and it records, per
field, the exact external result the field represents.

A theorem proved against this interface is **exactly as strong as the results the interface
cites, and not one notch stronger** (the current trust-boundary rule).  `lean-checked` is an evidence
attribute, never a status.

════════════════════════════════════════════════════════════════════════════════════════════════
                       WHAT EACH FIELD OF `QueryModel` CITES
════════════════════════════════════════════════════════════════════════════════════════════════

  field         manuscript object                                     kind
  ───────────   ───────────────────────────────────────────────────   ──────────────────────────
  `Q`           bounded-error quantum query complexity,               DEFINITION taken as given
                `sec:prelim`, paragraph "Query model"                 (position-dependent
                                                                      alphabets — see F5 below)
  `restrict`    `sec:prelim` fact (i): restricting the domain does    PRELIMINARY FACT, cited
                not increase `Q`
  `relabel`     `sec:prelim` fact (ii): a per-coordinate relabeling   PRELIMINARY FACT, cited
                costs at most the absolute factor `2`; the maps may
                differ per position and may change the alphabet
  `freeze`      `sec:prelim` facts **(i) + (iii)** composed at the    PRELIMINARY FACTS, cited
                last position: restrict to the product subdomain      (STATED IN THE MANUSCRIPT
                whose last factor is a singleton (fact (i)), then     in the reviewed manuscript)
                delete that now-singleton coordinate (fact (iii),
                *singleton-coordinate deletion*).  **Originally
                interface-only:** audit finding **F1** of the
                2026-07-30 T1 audit reported that no such principle
                was stated and that fact (i) as printed did not
                cover it, because deleting a coordinate changes the
                INPUT LENGTH.  The manuscript-repair batch of
                2026-07-31 (item M-1) added fact (iii) with exactly
                that not-an-instance-of-(i) note, so F1 is
                DISCHARGED and this field is now a cited fact, not
                an unstated one.
  `constQ`      `sec:prelim` fact **(iv)**: a constant function has   PRELIMINARY FACT, cited
                `Q = 0`; used by `thm:oabarrier` ("In both cases      PRELIMINARY FACT, cited
                `Q = 0`").  The external review identified this      and explicitly reviewed
                interface requirement as finding **F2**.
  `cABI`,       the absolute constant hidden in the `Ω(·)` of         BOOKKEEPING
  `cABI_pos`    `thm:abi` / `thm:tani`
  `abi`         `thm:abi` = Ambainis–Balodis–Iraids,                  EXTERNAL THEOREM, CITED —
                `Q(Claw_{n→κ}) = Ω(√n · κ^{1/6})` for `2 ≤ κ < n`     **not proved here**
  `tani`        `thm:tani` = Tani, same bound for `2 ≤ κ ≤ 2n-1`      EXTERNAL THEOREM, CITED —
                                                                      **not proved here**

`QueryModel.relabel_inj` (facts (i) and (ii) composed, for a per-coordinate *injection*) is a
THEOREM of the interface, not a field — finding **F5**: the load-bearing encoding lemma needs
nothing beyond the two stated facts, PROVIDED `Q` is given a position-dependent alphabet family,
which is what `sec:prelim` item (ii) already describes.

Design note (from `KSUM.LEAN`, scope clause 1): the cited results are STRUCTURE FIELDS rather
than `axiom`s.  A field carries zero soundness risk — `#print axioms` stays at Lean's three
standard axioms, so the citation manifest is machine-checked — whereas a bad `axiom` can
silently prove `False`.  Non-vacuity of the interface is witnessed by `KsumAudit.demoModel`,
which is a consistency witness only and is NOT a claim about quantum query complexity.
-/
import KsumAudit.MainLine

namespace KSUM

/-- The abstract query model of the manuscript audit, re-exported at the DAG-layer path.
See this module's header for what each field cites. -/
abbrev QueryModel := KsumAudit.QueryModel

end KSUM
