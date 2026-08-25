import Lake
open Lake DSL

/-!
Formal audit of the k-Sum small-alphabet paper (`ksum/paper/ksum_small_alphabet.tex`)
and the DAG-mirroring composition layer of `ksum/proof-dag/`.

Mathlib is pinned to the same revision as the machine-local prebuilt cache so that
`.lake/packages` can be reused directly (see `README.md`).

Two libraries are deliberately separated:

* `KsumAudit` — the manuscript-facing formalization (tiers T1/T3).  Module names are Lean names.
* `KSUM`      — the DAG-mirroring layer.  **Module name = proof-DAG node id**, file path = module
  path, plus the non-node modules `KSUM.Interface`, `KSUM.Support.*`, `KSUM.Trust`,
  `KSUM.SelfTest`.
-/

package ksumAudit where
  version := v!"0.1.0"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.31.0"

@[default_target]
lean_lib KsumAudit where

/-- The DAG-mirroring layer.  `globs := .submodules` because node ids such as `KSUM.A1a` are
module names in their own right and there is no single mathematical root module: the roots are
the DAG's own roots (`KSUM.goal`, and the aggregators `KSUM.Trust` / `KSUM.SelfTest`). -/
@[default_target]
lean_lib KSUM where
  globs := #[.submodules `KSUM]
