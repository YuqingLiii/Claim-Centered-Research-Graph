# Circdist Gross Round110: iteration-190 invariant-quotient continuation

## Verdict

**MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED.** The exact reviewed iteration-190 quotient is SAT. Its complete assignment satisfies all 11,827,887 clauses. The decoded 864-edge schedule is legal, but both unrestricted direct-360 sectors are SAT and exhibit independently checked named weight-10 undetected nonstabilizer mechanisms. This candidate is excluded. Neither root branch closes; `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`, and the exact licensed interval remains `D*_Gross in {11,12}`.

After both sectors completed, the two complete free `Z_12 x Z_6` orbits were appended atomically: 72 Xerr selectors plus 72 Zerr selectors, zero collisions, changing 24,444 selectors to 24,588. The retained iteration-191 base and 71-root quotient are fresh, checked, and unstarted. Iteration 191 was not solved.

## Bound reviewed start

The scheduler, canonical Gross node, Round109 fresh review, and entire sealed Round108 predecessor were hashed before science. Their SHA-256 values are respectively `beefafeee1608dda1eadfe0e82b920f7148bd2dfc12e93c52c6b48ff69e74aed`, `7302da9e4726bd2c62a9e335d75d6a9098780888ed91a87a66d503b5938f607b`, `0d31152bc03ca8066a7ffeaf885730b51ff2c55a3634819fc68d9fcbcd26dd82`, and root manifest `6c7f94706744ec7e11dcae7616d56ac3cc816025c72c25d4dc7396f981666cc0`. Full predecessor manifest verification passed.

The unique allowed quotient has SHA-256 `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`, 2,464,197 variables, 11,827,887 clauses, and 546,053 assertions. Before and after solving, independent streaming checks established the 517,140-block/24,444-selector registry invariance, the exact source/base bijection, all 71 lex roots, unique extension, and finite-orbit quotient/base equisatisfiability.

## Exact quotient result and legal candidate

CaDiCaL PID 14419 returned 10 (SAT) after 823.558288 seconds. It was foreground, attached, not timed out, and reaped. The assignment SHA-256 is `975dbb72397674377b2ef7a5c81156701b04e0667d6ac744e0238ebd9f7e2429`; every variable 1 through 2,464,197 appears exactly once and every clause is satisfied. The independent model serialization has SHA-256 `8a1f06b58914930b2ba3480392f25f8070aacf9cccca617f41f94f1e279f9a4f` and reconstructs the same model.

The schedule uses 477 layers, times 0 through 476, with zero conflicts, errors, or MC violations. It has 648 overlap pairs, 75 pair-interleaving witnesses, 321 whole-check-interleaving witnesses, and satisfies the global interleaving condition. Its compressed semantic SHA-256 is `843f3a156476027bce38d9bdd97a7d9bdc496d9d3e4d0acfcedb0f6014210d58`. All 72 orbit vectors are distinct, the stabilizer is exactly `{(0,0)}`, and all 71 nonidentity lex roots are strict. Flip, truncation, reversed-lex, and missing-root negative controls were rejected as specified.

## Complete unrestricted direct adjudication

Each direct formula contains all 360 primary fault columns, exact weight at most 10, zero detector syndrome, and nonzero logical class. No pool, residual-pattern, check-count, or within-check-order restriction was used. Xerr ran first to a terminal SAT result; only then did Zerr start.

### Xerr

- CNF: 6,130 variables, 23,100 clauses, SHA-256 `8bbe080ff3e6eadf65f7da0180daa686386237f4b64a23f05e9fe41dd932ff67`
- solver PID 14843: SAT in 1067.949165 seconds; complete assignment SHA-256 `9cca8da6aa23024ab343fe8c591f339f75e52297be3610c4b94c8910d4376d67`
- selected names: `D:14 D:29 D:35 D:78 D:88 D:103 D:120 R:5:1 R:26:0 R:67:2`
- canonical support: `[1, 14, 29, 35, 69, 74, 78, 79, 88, 89, 101, 103, 104, 120]`
- physical support: `[1, 14, 27, 28, 29, 35, 44, 69, 74, 78, 79, 88, 89, 103, 110, 120]`
- syndrome: empty canonically and physically
- logical parity: `[1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]`; canonical and physical nonstabilizer checks pass

### Zerr

- CNF: 6,088 variables, 22,932 clauses, SHA-256 `ddec622ceef752c73696c327a09c50768a331a9ff78e7fbcd5d1445afe8c0006`
- solver PID 15147: SAT in 766.880087 seconds; complete assignment SHA-256 `f13cf3e68cbf8278a7b29dd94bce8c537182e77603d16596ecbe72ed628bf8e1`
- selected names: `D:0 D:65 D:75 D:131 D:133 D:137 D:138 D:140 R:2:0 R:7:2`
- canonical support: `[0, 1, 5, 65, 67, 72, 75, 131, 133, 137, 138, 140]`
- physical support: `[0, 1, 62, 65, 67, 68, 73, 75, 128, 131, 133, 137, 138, 140]`
- syndrome: empty canonically and physically
- logical parity: `[0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]`; canonical and physical nonstabilizer checks pass

Vendor-backed physical replay and a separate Python-standard-library implementation both reconstruct every column, clause assignment, schedule-dependent hook, syndrome, logical parity, physical support, and stabilizer test. Either mechanism excludes the candidate; retaining both discharges the required serial two-sector adjudication. Repair was not entered because direct absence was false.

## Orbit update and fresh frontier

Both mechanism stabilizers are trivial, hence orbit-stabilizer gives 72 translated selectors per parent. Normalized semantic tuples show no old-registry, cross-sector, or within-orbit collision. Audits replay all 72 translated legal schedules and all 144 translated physical mechanisms; each mechanism retains named weight 10, empty syndrome, and nonstabilizer logical action. Generator closure checks cover 1,034,280 block cases and 49,176 selector cases. Therefore the atomic count is `24,444 + 72 + 72 = 24,588`.

The fresh iteration-191 source SHA-256 is `0b0ac7e6daa69d8d3ab1b98b7228c43690a5406c52defe57e46027b185984a47`, semantic payload `02da1bcb87a45637afa8434a8dfa4e4c8092489ace7f5a7fd1ba3266f9615532`, state `6059554d307e7c503bd1792dd77718a205346f5dce243e719ae057f402cf6c9f`, and selector state `41bb458a1b9a31aba7d70f063165221a9ae9c989421682320826dbc5d166f9e6`. Its base is 1,853,886 variables / 6,929,888 clauses / 546,126 assertions, SHA-256 `d1e68e88eb4c22ffda58d3a1c73cb7dbf6082690c594e8c538f8cc70c432e223`. Its quotient is 2,467,326 variables / 11,837,479 clauses / 546,197 assertions, SHA-256 `30ce7d14d96349e61d7105255cddc8899b8927ce728dfd147b641c75c97fe10f`. Both independent checks pass. Exact file allowlists exclude solver, model, assignment, and proof outputs; `started=false`, `stop=null`.

## Proof and process disposition

All three solver results are SAT. Their proof-side outputs are retained only as losslessly verified deterministic-gzip search traces: 10,443,528,805 raw bytes, 2,406,711,083 gzip bytes, zero empty-clause lines. They are not DRAT/LRAT certificates and carry no UNSAT credit. Separate tool controls accept valid DRAT, convert it to accepted LRAT, and reject corrupt/truncated DRAT and LRAT. Those controls do not certify Gross.

All scientific children were foreground and serial; each record includes argv, cwd, environment, PID/PPID, UTC interval, return code, timeout/signal/reap/detach status, stream paths, sizes, and hashes. Ten harness/interface/adaptation/packaging failures are disclosed in `FAILURE_LEDGER.md`; none produced an accepted scientific result or UNKNOWN outcome.

## Root branches and scope

Branch A does not close: this legal candidate has explicit weight-10 mechanisms in both sectors, so it is not a distance-12 witness. Branch B does not close: the mandatory quotient is SAT, so no Gross UNSAT certificate or universal `d_circ <= 11` theorem is available. Candidate exclusion does not narrow the campaign interval.

This package proves only the checked iteration-190 candidate exclusion, its complete two-orbit exclusion update, and construction of the fresh iteration-191 frontier. It does not install canonical state, claim an explicit distance-12 circuit, or claim universal distance at most 11. The next exact task is: Solve the exact fresh iteration-191 71-root quotient proof-first; if SAT, replay the legal schedule and adjudicate unrestricted Xerr then Zerr strictly serially.
