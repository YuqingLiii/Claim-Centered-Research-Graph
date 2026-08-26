# k-Sum linked Lean development

This Lean 4 + Mathlib development is linked to the small-alphabet k-Sum claim graph. The canonical
node files under [`../proof-dag/nodes/`](../proof-dag/nodes/) are the authority for current evidence levels, caveats,
and review links.

## Current coverage

The development checks the principal lower-bound reductions used by the k-Sum case study and a
collection of obstruction arguments. It includes the cyclic 2-Sum encoding and target-shift chain,
the fixed-k frozen-core construction, selected orbit and filtration statements, and exact
certificates for several finite linear programs.

Some statements are proved unconditionally, while others are proved only relative to the explicit
`QueryModel` interface. Imported Claw and query-model bounds are not reproved here. The recursive
quantum upper-bound algorithm, its correctness proof, and its query-complexity analysis are not
formalized. The statement-fidelity review linked from the relevant nodes records where the Lean
statements are faithful to, narrower than, or conditional on the natural-language claims.

## Trust boundary

A successful build is evidence for the exact Lean statements under their declared assumptions; it
does not by itself set a node's evidence level. Completion-level assessments require the independent
reviews linked from the corresponding nodes. Consistency examples show that interfaces are
inhabited, but they are not quantum query lower bounds.

The archived build and axiom census report no `sorry` and no project-specific axioms. The trusted
base remains Lean, Mathlib, the declared interfaces, and the reviewer-checked correspondence between
formal and natural-language statements.

## Layout

- `KsumAudit/` contains the mathematical reductions, obstruction lemmas, and exact certificates.
- `KSUM/Interface.lean` declares the imported query-model interface.
- `KSUM/Support/` contains shared constructions used by multiple claim nodes.
- `KSUM/*.lean` contains the node-linked claims and composition theorems.
- `KSUM/SelfTest.lean` contains definition and non-vacuity checks.
- `KSUM/Trust.lean` records the formal trust boundary and axiom census.

## Build

```bash
lake exe cache get
lake build
```

The project pins Lean and Mathlib through `lean-toolchain` and `lake-manifest.json`. On Windows,
long path support may be needed because some claim-node filenames are descriptive. Generated
`.lake/` directories and `.olean` files are caches and are not research records.

## Contribution rules

- Do not commit a theorem containing `sorry` or introduce a project-specific `axiom`.
- Keep imported assumptions explicit in `QueryModel` and in the applicable claim node.
- Use explicit quantified constants in formal statements instead of asymptotic notation.
- Keep the node claim hash and Lean synchronization metadata current.
- Link build output and independent review from the exact node or route they support.
- If a step cannot be formalized faithfully, preserve the unresolved obligation instead of
  weakening the statement.
