# Post-audit cleanup — additivity-equality project

Date: 2026-09-07

Status: structural and locator cleanup after the V6 adversarial audit. No claim, implication or
evidence level is changed.

## Repairs

1. Verified that the project-local Hastings PDF is present and matches the registered SHA-256
   `b303560e5794e9b12b7c7f4145b4cd7958a6dd8ab83b61eb7947befca3348b98`; the post-audit package
   includes it under the HAEQ project rather than relying on the duplicate in another project.
2. Connected `HAEQ.fixed-channel-regularization` as the fourth root-route premise. This replaces a
   duplicated route-local HSW assumption and makes the separately reviewed capacity lemma visible
   in the dependency graph.
3. Standardized the Fukuda--Wolf Proposition 1(4) locator as statement on PDF p. 1 and proof on
   PDF p. 2.

The conclusion remains exactly: there is a finite channel `T` with
`chi(T tensor T)>2chi(T)` and hence `C(T)>chi(T)`.
