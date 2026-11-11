# CIRCDIST Gross cross-registry proposer — round 78

**Verdict:** `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`.

This sealed proposer begins only from the exact reviewed, unstarted iteration-78 state (`G=5,743`, `D=156`, registry/raw `72`, total `7,359`). Before the first outer call it performs a separate cross-registry synthesis over all 72 reviewed raw mechanisms and retains 2,826 exhaustively validated pair regions, giving first-outer state `G=8,569`, total `10,185`. It then closes 12 candidates, iterations 78–89, with a fresh outer process and both unrestricted direct-360 sectors for each candidate. Every one of the 24 direct sectors is SAT and passes complete-assignment, every-clause, canonical and physical replay. No UNSAT, UNKNOWN, timeout, repair, or absence conclusion occurs.

The final exact restart is unstarted iteration 90: `G=10,595`, `D=180`, registry/raw `96`, total `12,235`. The round contributes 4,852 generalized terms: 2,826 pre-outer cross-registry, 62 online, and 1,964 post-candidate cross-registry. Candidate-exact blocks are preserved. `D*_Gross` remains in `{11,12}`.

## Audit map

- `SOURCE_BINDINGS.json` binds the source seal, exact review, reviewed restart, live snapshots, environment, engine, and R77-F1 final compressor.
- `cross_registry/` contains every catalog, option registry, completion attempt, 720×720 relation, raw candidate, semantic classification, retained term, selector replay and state transition.
- `cegar/iter78` … `iter89` contain the actual outer SMT, candidate, both direct-360 formulae and assignments, raw mechanisms, online catalogs/relations/DP, cross-registry synthesis, and four-state commit journals.
- `classification/`, `cegar/summary.json`, and `restart/restart_state.json` are aggregate and restart ledgers.
- `controls/` contains fresh valid, corrupt, and truncated DRAT/LRAT controls. They test only the proof toolchain and are not Gross proofs.
- `FIX-2.md` and `development/` disclose every interrupted or failed development attempt, including memory incidents and the temporary v6 staging rollback.
- `verify.py --quick` verifies the seal, compression, bindings, state chain, ledgers and controls. `verify.py --full` additionally rebuilds every outer/direct formula in fresh processes, replays all 96 raw mechanisms, all local catalogs, every retained pair tuple, and every multi-check DP/product.

Fresh independent exact review is required before any continuation or node mutation.
