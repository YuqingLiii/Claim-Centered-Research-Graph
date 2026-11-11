# Rebuttal and attack ledger

| proposed shortcut or inference | disposition | sealed evidence |
|---|---|---|
| Treat a zero pair truth cell as physical absence | rejected; the relation is conservative positive only | pair relations and deletion controls |
| Treat no weight-12/14 completion as absence | rejected; finder misses are not negative certificates | every `w14_positive_pool.json.gz` and aggregate summary |
| Multiply independent pair probabilities for multi-check soundness | rejected; every mechanism uses one joint GF(2) DP | 24 `multi_check_relations.json.gz` objects |
| Infer all-tuples validity from three samples | rejected; the proof quantifies over every catalog class and DP transition | factorized universal basis in `tuple_raw_replay.json.gz` and `MATH_DERIVATION.md` |
| Reprice the old 314,668,800 cells every round | unnecessary; exact semantic masks are cached/indexed and new mechanisms are evaluated incrementally | per-iteration dedup ledgers; final sequential recomputation |
| Claim high-dimensional prior-union cardinality without computing it | rejected; multi coverage difference is deliberately `null` with explicit scope | iter42 dedup/tuple ledgers |
| Use deletion countertuples as physical absence | rejected; controls are library-relative or selected-mechanism-relative | 1,372 embedded controls |
| Install exact blocks but defer generalization to a stale batch | rejected; after-state equals next before-state for every iteration | iteration outcomes and snapshots |
| Accept partial SAT assignment | rejected by a one-literal truncation | `controls/truncated_assignment_iter42_Xerr.solver.log.gz` |
| Accept corrupted proof | rejected by both DRAT and LRAT checkers | `controls/round74_proof_checker/` |
| Enter repair after one sector or unproved absence | rejected; dual checked absence is mandatory | all direct gate policy and RESULT |
| Treat twelve SAT iterations as exhaustion | rejected | frozen iteration54 restart and verdict |
