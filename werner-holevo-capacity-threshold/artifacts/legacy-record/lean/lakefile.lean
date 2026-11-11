import Lake
open Lake DSL

/-!
DAG-mirroring Lean development for the noisy Werner–Holevo zero-capacity problem.

Root DAG node: `WHGAP.goal`
(`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md`).

Governed by `research/DAG_PROTOCOL.md` §7 and `research/RESEARCH_STRUCTURE_PROTOCOL.md`
§4 item 7: every node-shaped module name equals a DAG node id, and the import graph
equals the propagating DAG skeleton.

Mathlib is pinned to the same revision as the machine-local prebuilt cache reused by
`research/se/lean` and `research/ksum/lean`, so `.lake/packages` is shared (see `README.md`).
-/

package whgapDag where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.31.0"

@[default_target]
lean_lib WHGAP where

