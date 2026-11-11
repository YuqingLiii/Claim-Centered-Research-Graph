# Holevo additivity equality

This folder owns the first question: whether the Holevo additivity equality is universal, and how
pair additivity, self-additivity, tensor-power additivity and the regularized classical capacity are
logically related.

- [`proof-dag/NODE_INDEX.md`](../../proof-dag/NODE_INDEX.md) is the generated claim index.
- [`proof-dag/GRAPH.mmd`](../../proof-dag/GRAPH.mmd) is the generated graph view.
- [`proof-dag/nodes/`](../../proof-dag/nodes) contains the canonical node records.
- [`reviews/`](../../reviews/holevo-additivity-equality) contains project-level independent reviews.
- [`artifacts/`](.) contains the linked proofs, source audits, and retained research output.

Begin with node `HAEQ.goal`, then follow its structured route, evidence, and review links. This
directory is self-contained; repository-level `tools/` contains the shared structural validators.

This is a **classical-information-through-a-quantum-channel** problem. The transmitted messages are
classical, but the physical channel, code states and measurements are quantum, and codewords may
be entangled across several channel uses. Thus the appearance of entanglement is expected and does
not turn the question into quantum capacity `Q` or private capacity `P`. The one-shot quantity is
`chi`; the unassisted classical capacity is its regularization
`C(N)=sup_n chi(N^tensor n)/n`.

The canonical state is in `proof-dag/nodes/*.yaml`. The index and graph are generated views.
Historical web research is retained only as source material under `artifacts/`; no continuing work
is dispatched to the web.

Current answer: universal equality is false, while many special channel classes remain additive.
The migrated dossier is intentionally capped at CONJECTURED until the exact new-format claims and
route implications receive hash-bound independent review.

The root route now uses Shor's explicit finite Weyl-labelled construction, which preserves the
numerical MOE pair defect exactly as a Holevo pair defect. Shor's universal equivalence remains a
correct background theorem but is no longer the load-bearing transfer step.

Boss-facing frozen verdict: `artifacts/BOSS_QUESTION_1_VERDICT_20260830.md`.

## Validation

```sh
python3 tools/proof_dag_check.py --problem holevo-additivity-equality --write-generated
python3 tools/evidence_closure_check.py --problem holevo-additivity-equality
```
