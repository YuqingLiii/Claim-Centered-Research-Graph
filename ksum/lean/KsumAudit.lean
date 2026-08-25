/-
Root of the manuscript-facing library `KsumAudit`.

`Smoke`        — the gate G-L1 environment probe (not paper content).
`MainLine`     — tier T1, the `k = 2` lower-bound main line, ADOPTED
                 (node `KSUM.LEAN.T1.k2-main-line`, NUMERICAL · pending-review).
`T2KFloor`     — tier T2, the `k`-floor combinatorial cores (`lem:core`, `prop:core-even`,
                 `lem:core-odd`, and the combinatorial half of `lem:transl-cover`), and
`RosmanisBarrier` — tier T2, `prop:rosmanis` (the negative-set orbit parametrization).
                 Node `KSUM.LEAN.T2.rosmanis-kfloor`; both carry **no `QueryModel`**, so their
                 theorems are unconditional.
`Obstructions` — tier T3, the obstruction group, **AUDITED and ADOPTED 2026-07-30**
                 (report `ksum/artifacts/ksum_lean_T3_obstructions_20260730.md`, evidence
                 `ksum/artifacts/logs_ksum_lean_T3_20260730/`).  Node
                 `KSUM.LEAN.T3.obstruction-theorems` is **NUMERICAL · pending-review:
                 KSUM.LEAN.statement-fidelity** — a green build is evidence, never a status; see
                 `KSUM/Trust.lean` §(d).  Four of the ten formalized (target, node) pairs
                 are recorded as NARROWER on the node, and two labels are not formalized at all.

The DAG-mirroring layer is the separate library `KSUM` (see `lakefile.lean`).
-/
import KsumAudit.Smoke
import KsumAudit.MainLine
import KsumAudit.T2KFloor
import KsumAudit.RosmanisBarrier
import KsumAudit.Obstructions
