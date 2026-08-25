/-
# Tier 3 of the k-Sum Lean audit — the obstruction / negative-result group

DAG node: `KSUM.LEAN.T3.obstruction-theorems`
(`ksum/proof-dag/nodes/KSUM.LEAN.T3.obstruction-theorems.yaml`).

Aggregator for the §`sec:proof-search` obstruction theorems of
`ksum/paper/ksum_small_alphabet.tex`.  Nothing in this tier imports a `QueryModel` or
any other interface hypothesis: every theorem below is UNCONDITIONAL finite linear algebra and
combinatorics.

| Module | LaTeX label | DAG node(s) |
|---|---|---|
| `ObstructionsCore`        | (substrate; eq. (38))         | — |
| `ObstructionsPairTensor`  | `thm:pair-tensor`             | `KSUM.B4b.L2.M1` |
| `ObstructionsProduct`     | `thm:product-obstruction`     | `KSUM.B4b.L2.M2` |
| `ObstructionsBlock`       | `thm:block-obstruction`       | `KSUM.B4b.L2.T4`, `KSUM.B4b.L2.VBUD` |
| `ObstructionsOrientation` | `thm:orientation-obstruction` | `KSUM.B4b.L2.ORIENT` |
| `ObstructionsTransfer`    | `prop:transfer-facts`         | `KSUM.B4b.L2.G1/G2/G3` |
| `ObstructionsBandMult`    | `lem:band-multiplication`     | `KSUM.B4b.L2.BANDMULT` |
| `ObstructionsTiltedBand`  | `thm:tilted-log-band` (PARTIAL) | `KSUM.B4b.L2.L2P3` |
| `FactorialFiltration`     | `lem:factorial-filtration`    | `KSUM.B4b.L2.FILT` |
| `JointLP`                 | `prop:joint-lp`               | `KSUM.B4b.L2.JOINTLP` |

**2026-07-31 (gap-closure batch 1, item L-1).**  `lem:factorial-filtration` is now formalized, in
both directions, in `KsumAudit/FactorialFiltration.lean` — together with the uniform orbit lift
that carries an occupancy-level measure to an `S_N`-invariant measure on `A^N` with the same `ℓ¹`
norm.  Its node `KSUM.B4b.L2.FILT` was registered 2026-07-30.  `prop:joint-lp`
(node `KSUM.B4b.L2.JOINTLP`) remains unformalized: it is an exact finite LP computation delegated
to an ancillary script, with no dual certificates on disk.

**Audit status (2026-07-30):** all eight modules AUDITED and ADOPTED (44 draft statements ADOPT,
0 REPAIR, 0 REJECT, 14 added), 58 declarations axiom-clean, zero `sorry`/`axiom`, zero build
warnings.  Of the ten formalized (LaTeX target, node) pairs six are FAITHFUL and four are
**NARROWER**: `thm:orientation-obstruction` clause (b) — the only one on an obstruction —
`thm:pair-tensor`, `thm:tilted-log-band`, and `lem:band-multiplication` clauses (a),(d).

`lean-checked` is an evidence attribute, never a status (see `KSUM.LEAN`).
-/
import KsumAudit.ObstructionsCore
import KsumAudit.ObstructionsPairTensor
import KsumAudit.ObstructionsProduct
import KsumAudit.ObstructionsBlock
import KsumAudit.ObstructionsOrientation
import KsumAudit.ObstructionsTransfer
import KsumAudit.ObstructionsBandMult
import KsumAudit.ObstructionsTiltedBand
import KsumAudit.FactorialFiltration
import KsumAudit.JointLP
