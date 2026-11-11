# Werner–Holevo capacity threshold

This folder owns the qutrit one-parameter channel problem

`Lambda_x(X) = (1-x)X + (x/2)(Tr(X)I-X^T)`.

It is separate from the Holevo/classical-capacity additivity questions. This project studies the
quantum capacity `Q` and private capacity `P` thresholds.

Current organized state:

- `Q(Lambda_x) > 0` is supported on `0 < x < 2/5`;
- `Q(Lambda_x) = P(Lambda_x) = 0` is supported on `1/2 <= x < 1`;
- `P(Lambda_x) > 0` is supported on `0 < x < 1/2`;
- the remaining quantum-capacity problem is `2/5 <= x < 1/2`.

Legacy dossiers, proof notes, reviews and Lean sources are preserved under `artifacts/legacy-*`.
Because the new canonical claim wording has not yet been rebound to exact review hashes, migrated
positive results are conservatively capped at CONJECTURED rather than silently inheriting old
completion stamps.

The current Zhu--Wang arXiv v2 theorem numbering and the external HRSF tensorization interface are
rebound in `artifacts/PRIMARY_SOURCE_AUDIT_20260829.md`. The relationship to the three classical-
capacity projects is isolated in `artifacts/RELATION_TO_HOLEVO_ADDITIVITY_20260829.md`.

New local progress on the remaining strip:

- the complete one-copy input optimization has an exact five-real-parameter `O(3)` normal form;
- every real qutrit input has nonpositive one-copy coherent information on `[2/5,1/2]`;
- at every blocklength, every state diagonal in a real product basis, with arbitrary classical
  correlations across copies, has nonpositive coherent information; and
- a fresh rank-stratified numerical scan found only the exact pure-state zero floor on the strip.

These advances do not close the root: complex one-copy coherences and genuinely coherent/entangled
multi-copy inputs remain uncontrolled.

## Validation

```sh
python3 tools/proof_dag_check.py --problem werner-holevo-capacity-threshold --write-generated
python3 tools/evidence_closure_check.py --problem werner-holevo-capacity-threshold
```
