# Attack and rejected-branch ledger

## A1. Exploratory 15,874 pair-pattern clauses

**Decision:** rejected for candidate selection and every absence inference.

**Reason:** round 63 did not retain the ten source schedules, exact clause bodies, or later-schedule exclusion replay. Reproducible source and aggregate counts do not repair a missing verdict ledger. Usage count in round 68 is exactly zero.

## A2. Static single-residual clauses treated as complete direct absence

**Decision:** rejected.

**Reason:** the 1,440 clauses are complete only for a suffix-three residual plus nine singleton completion to a frozen weight-12 logical. The primary Zerr witness uses four two-suffix hooks; the Xerr witness uses seven residuals. The static library is a sound outer filter, not a complete adversary.

## A3. Round-63 live verifier failure

**Observation:** `verify.py --repo-root ...` rejects the current Gross node hash, and `--full-static --repo-root ...` rejects for the same reason.

**Disposition:** expected binding drift, not a seal failure. Both round-63 manifest checks pass. `verify.py --full-static` with sealed inputs passes and reconstructs the complete static certificate. `BINDING_DRIFT.json` shows that only the later-updated Gross node and scheduler differ among round-63 bindings; current bytes are rebound in `SOURCE_BINDINGS.json`, and normalized load-bearing statements are unchanged.

## A4. First build-script assertions

Two external-scratch development attempts stopped before candidate selection:

1. strict equality against `global_single_clauses.json` failed because the sealed JSON includes the non-mathematical `replay_wall_seconds` field while the deterministic generator does not;
2. the first round-62 replay expected `raw_selected_indices`, but inherited witnesses use `selected`.

Repairs were narrow and explicit: ignore only the timing key, and accept the inherited canonical `selected` field. The final verifier independently regenerates and compares every mathematical clause record and replays all selected columns.

## A5. C1 direct control solve

A complete C1/Zerr DIMACS control was generated, but the foreground CaDiCaL run was interrupted with SIGINT after 61.43 real seconds, exit 130, while still undecided. Its 693,145,600-byte non-verdict SAT trace was deleted from scratch; the solver log, exact run record, formula summary, and independently raw-valid expected C1 witness remain. No solver verdict is assigned.

This branch was unnecessary after both primary formulas returned SAT and an independent Glucose42 run produced a second raw-valid primary Zerr model.

## A6. Weak proof corruption that remained valid

Deleting only the final `0` line from the PHP(6,5) DRAT file still yielded `s VERIFIED`. Backward checking found a sufficient conflict in the remaining proof, so the removed line was redundant. This is not counted as a negative control.

The repaired negative controls retain only the first 10 of 219 DRAT lines and only the first 10 LRAT lines. They are rejected with exit 1 and `NOT VERIFIED` by the separate checkers.

## A7. Checking SAT traces as UNSAT proofs

**Decision:** rejected as meaningless. CaDiCaL wrote trace streams because a proof filename was supplied, but both direct runs ended SAT. The compressed streams are retained only to bind the proof-logging execution. They are not DRAT certificates and carry no checker claim.

## A8. Arbitrary-round repair

**Decision:** not entered.

**Reason:** the commission permits repair only after independently checked direct absence in both sectors. Both sectors are SAT, so running repair would violate the gate and could not rescue this candidate.

## A9. Universal D*=11 inference from blocks

**Decision:** rejected.

**Reason:** 1,472 total retained blocks after the primary and five-step continuation do not constitute a checked exhaustion of the unrestricted interleaved outer space. The continuation outer calls remain SAT.

## A10. D*=12 inference from candidate legality

**Decision:** rejected.

**Reason:** legality and MC are necessary only. Complete direct queries exhibit effective logicals below 11 in both sectors, so the candidate is killed before the completion-gap criterion.
