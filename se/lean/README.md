# Set Equality linked Lean development

This Lean 4 + Mathlib development is linked to the Set Equality claim graph. The canonical records
for its two main layers are [`SE.formal.t1`](../proof-dag/nodes/SE.formal.t1.yaml) and
[`SE.formal.t2`](../proof-dag/nodes/SE.formal.t2.yaml). The node files, rather than this README, are the
authority for current evidence levels, caveats, and review links.

## Current coverage

The development machine-checks the conditional composition from four named obligations to the
target adversary bound. It also proves selected analytic and combinatorial components, including
the taper inequalities, discrete envelope bounds, closed constants, hook-product estimates, and
the two-sided range used for the parameter `omega`.

The four representation-theoretic obligations H1--H4 remain explicit hypotheses. In particular,
the development does not prove the missing minimal-alphabet witness, the exhaustive sectorization
of the legal lower block, or the full representation-theoretic interfaces. These boundaries are
recorded by the corresponding claim nodes and by the linked external reviews.

## Trust boundary

A successful build checks the Lean statements under the assumptions declared in
`SE/Interface.lean`. It is run evidence, not an automatic promotion of any mathematical claim.
The node assessment determines the current level and links the review that licenses it.

The archived build records report no `sorry`, no project-specific axioms, and no use of
`native_decide`. They do not validate imported mathematical results or establish that every Lean
statement captures the intended natural-language claim; that correspondence remains a review
obligation.

## Layout

- `SE/Interface.lean` declares the explicit trust interface.
- `SE/denom/Phi/legal/` contains the linked shadows of H1--H4 and their conditional composition.
- `SE/denom.lean`, `SE/br.lean`, and `SE/goal.lean` assemble the conditional route.
- `SE/Support/` contains reusable analytic and combinatorial lemmas.
- `SE/SelfTest.lean` supplies non-vacuity and definition checks.
- `SE/Trust.lean` records the formal trust boundary and axiom census.

## Build

```bash
lake exe cache get
lake build
```

The project pins Lean and Mathlib through `lean-toolchain` and `lake-manifest.json`. Generated
`.lake/` directories and `.olean` files are caches and are not research records.

## Contribution rules

- Do not commit a theorem containing `sorry` or introduce a project-specific `axiom`.
- Record imported assumptions explicitly in the interface and in the applicable claim node.
- Keep the node claim hash and Lean synchronization metadata current.
- Link build output and independent review from the exact node or route they support.
- If a step cannot be formalized faithfully, leave the obligation explicit rather than weakening
  the statement.
