# Holevo counterexample prevalence

This folder owns the second question: in what precise senses are additivity counterexamples
"many"? The project separates existence, random-model probability, topology/measure,
genericity, explicitness and dimension thresholds.

- [`proof-dag/NODE_INDEX.md`](../../proof-dag/NODE_INDEX.md) is the generated claim index.
- [`proof-dag/GRAPH.mmd`](../../proof-dag/GRAPH.mmd) is the generated graph view.
- [`proof-dag/nodes/`](../../proof-dag/nodes) contains the canonical node records.
- [`reviews/`](../../reviews/holevo-counterexample-prevalence) contains project-level independent reviews.
- [`artifacts/`](.) contains the linked proofs, source audits, runs, and retained output.

Begin with node `HCPREV.goal`, then follow its structured route, evidence, and review links. This
directory is self-contained; repository-level `tools/` contains the shared structural validators.

Canonical claims live in `proof-dag/nodes/*.yaml`; historical web output is retained only under
`artifacts/` and is not an active research surface.

Current answer: strict counterexamples form relative-open positive-measure sets at every fixed
dimension where a witness exists, and some named high-dimensional random ensembles produce them
with probability tending to one or almost-sure eventual occurrence. A new proposer-side
product-Haar construction strengthens this: for every target gap, after fixing a sufficiently large
finite depth, the probability of a finite-dimensional gap above that target tends to one with the
per-leg matrix dimension. This is model-specific abundance, not genericity in the whole channel
space.

At fixed dimensions there is also a separate qualitative probability bridge, registered as
`HCPREV.full-support-probability-dichotomy`: under any Borel sampling law with support equal to the
entire relevant CPTP ambient space, a nonempty strict-violation set has probability strictly
between zero and one. Full support alone supplies no dimension-uniform numerical bound.

Counterexamples are not dense, residual, or full-measure in the whole fixed-dimensional CPTP space
because entanglement-breaking channels contain an open strongly additive region. The reported
`182/183` thresholds are model/Bell-witness thresholds, not universal minimum dimensions; a
compact deterministic certified `p=1` witness remains an open frontier. Openness and density of
Gaussian-rational unitaries do imply that algebraic witnesses exist and that an exhaustive
certified search must terminate in principle, but no remotely practical dimension/runtime bound or
printed tuple is presently supplied.

Boss-facing frozen verdict: `artifacts/BOSS_QUESTION_2_VERDICT_20260830.md`.

## Validation

```sh
python3 tools/proof_dag_check.py --problem holevo-counterexample-prevalence --write-generated
python3 tools/evidence_closure_check.py --problem holevo-counterexample-prevalence
```
