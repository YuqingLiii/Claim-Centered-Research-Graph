import Lake
open Lake DSL

/-!
Tier-1 formalization of the conditional assembly of
`se/paper/se_explicit_witness.tex` (Theorem B).

DAG node: `SE.formal.t1` (`se/proof-dag/nodes/SE.formal.t1.yaml`).

Mathlib is pinned to the same revision as the machine-local prebuilt cache used by
`ksum/lean`, so that `.lake/packages` can be reused directly (see `README.md`).
-/

package seAudit where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.31.0"

@[default_target]
lean_lib SE where
