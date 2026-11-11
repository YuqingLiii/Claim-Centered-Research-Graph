# CIRCDIST.gross Round124 exact iter197 continuation

## Verdict and safe boundary

The exact reviewed iteration-197 order-144 quotient is **SAT**. Its complete assignment covers all 4,375,764 variables exactly once and satisfies all 21,395,983 clauses. It decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are also **SAT** at exact fault weight 10. Either checked sector kills the candidate; both were adjudicated for the symmetric ledger. Repair and gap analysis were therefore forbidden and not attempted.

The only scientific advance after the kill is sound registry growth: four free generalized-dihedral selector orbits of size 72 add 288 distinct selectors. Iteration 198 is sealed **CHECKED_UNSTARTED** and has never been solved. Root status is unchanged.

## Dispatch and reviewed starting frontier

The scheduler, ProofPilot record, canonical Gross node, Round123 exact review, and reviewed Round122 root manifest match the SHA256 values in `INPUT_BINDINGS.json`. Before science, an independent preflight rehashed the sealed input:

- source `6ce8b8593fabc80ce0917f342126e351da30114802765a46773da348115aec44`, semantic `bee49435279caa3fb6cc02e0f1b145e3568eb54e6d3ac02c49e5bae3c5fa42f4`;
- state `cd005e436ff92c66badefb5a30e83531d81d9339bfbc047ebbdbb32627eb1ed0`, selector state `2b5d1178c5532d62f8e6266d627aaa4c228fa18526e7f79156cc667b1e207608`;
- 814,392 blocks, 51,552 selectors, 870,342 assertions;
- base `f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3`, 3,140,244 variables / 11,511,680 clauses;
- quotient `fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334`, 4,375,764 variables / 21,395,983 clauses / 143 nonidentity roots;
- checked-unstarted receipt `68e06e13c5242beb3d0170565968b911ba68e2b0715d8c3b91a33c4a8f8761b5`, state `started=false`, forbidden artifacts empty, solver starts targeting iter197 zero.

The quotient is used only through its checked equisatisfiability with that exact base. Its 143 non-strict lex leaders permit stabilizers and make no free-orbit assumption.

## Mandatory proof-first outer solve

Pinned CaDiCaL SHA256 is `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. The exact sealed quotient was passed directly; proof output was enabled from byte zero. The solver returned 10 and reaped normally. Exact argv, PIDs, UTC start/end, byte counts, stderr, and return code are in `RESULT.json` and the JSONL process ledger.

`output/iter197/solver/assignment_check.json` verifies every variable exactly once and all clauses. The decoded schedule has 864 edges, 228 used layers `0..227`, no resource conflict, all 648 MC overlaps satisfied, global interleaving, 102 overlap-interleaved pairs, 351 whole-check-interleaved pairs, and zero reviewed block/selector hits. Candidate schedule SHA256 is `46633e0c3b8073783d1aaf86fe4dea581e300be3152b3c2661b272efb3f87151`. The independent orbit audit checks all 144 schedules, all 143 roots, identity stabilizer, lex minimality, base-prefix and quotient clause satisfaction, plus flipped-variable, truncated-assignment, reversed-lex, and omitted-root controls.

Because the solve is SAT, its proof stream is evidence of the proof-enabled search only. It is not a DRAT/LRAT UNSAT certificate.

## Complete unrestricted direct-360 adjudication

The two formulas are outside the outer encoding and use every one of 360 physical columns, with only complete `W<=10`, 72 detector equations, and a nonzero 12-logical-row condition. There is no pool, residual-pattern, check-count, within-check-family, sample, or partial restriction.

### Xerr

- CNF `8cb4e48da6bae2912452143fd938cee9db67d77624204c73a89ff1e9fbd99e7e`, 6,119 variables / 23,056 clauses; every clause checked.
- Selected faults: `D:2, D:56, D:63, D:71, D:128, D:129, D:133, R:59:0, R:65:0, R:71:1`.
- Exact weight 10; canonical support `[2, 5, 11, 54, 56, 60, 63, 67, 71, 77, 128, 129, 133, 140]`; physical support `[2, 55, 56, 61, 63, 67, 71, 129, 133, 134, 137, 140]`.
- Detector syndrome `[]`; logical vector `[1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]`.
- Canonical and physical nonstabilizer tests pass. Flipping selected variable 3 fails 6 clauses.

### Zerr

- CNF `44d5c6a0ab07076f844398d684a3a4c027283462b169ae1a9348d2434cb675ef`, 6,125 variables / 23,080 clauses; every clause checked.
- Selected faults: `D:117, D:119, D:131, R:57:1, R:59:0, R:66:1, R:67:2, R:68:1, R:69:0, R:71:2`.
- Exact weight 10; canonical support `[45, 53, 56, 57, 61, 70, 111, 117, 119, 120, 122, 125, 128, 131, 138, 143]`; physical support `[45, 47, 61, 63, 66, 70, 111, 113, 117, 119, 120, 122, 123, 125, 128, 129, 130, 131, 138, 139, 140, 143]`.
- Detector syndrome `[]`; logical vector `[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.
- Canonical and physical nonstabilizer tests pass. Flipping selected variable 118 fails 4 clauses.

The independent implementation uses only the Python standard library and reconstructs all 720 sector columns, both CNFs and assignments, exact physical hooks, both 72-row syndromes, both 12-row logical systems, stabilizer rank 66 in each sector, and cross-pairing rank 12. The vendored verifier agrees.

## Orbit lineage and iter198 frontier

For translations `T_delta` and CSS involution `D`, the audits enumerate stabilizers rather than assuming freeness. Here Xerr, Zerr, and both CSS-dual selector orbits each have identity stabilizer and size 72. All 288 physical group-element replays preserve schedule legality, exact weight, zero syndrome, logical action, and nonstabilizer status. Full selector tuples establish pairwise disjointness and no inherited collision. The source registry is closed under translations and CSS duality before and after atomic insertion.

Fresh iter198 identities:

- source `dd0e4f55943381e265b174a0360f2ee2dc0e9c93326b71c315632ffbda6d95a2`, semantic `d41be17da8e398e13b94cf38807d78187247e7318d61ebbeb6d21bc2e7f43f9d`;
- state `a60e1e378283153a3f24611a9e33cbb97df19bcbe231a9fa515b13fae0ff7287`, selector state `e25d5ad244f42075e6e4c3f884bb33300c50dbfbdf1bfa74324b1dd964438f53`;
- 814,392 blocks / 51,840 selectors / 870,630 assertions;
- base `4dc712e335bd3d22c753aaa61e8603026c514a070522a94aa2e239714e185f8f`, 3,152,127 variables / 11,550,293 clauses;
- order-144 quotient `ee72ce86b4191f6e2602d500e2dc157ea4aca9565028fa7c07073d8b8d19bd08`, 4,387,647 variables / 21,434,596 clauses / 143 roots;
- checked-unstarted `894686dbda1bb6c8da578aad828cb1122e5fe68c8b2e7ec47341c0fabdf8d03c`, zero iter198 solver invocations and no forbidden artifacts.

The base checker binds every compiled definition and clause. The quotient checker reconstructs the byte-exact base prefix and every appended recurrence/root clause, verifies the concrete order-144 action and group law, and states only equisatisfiability with the exact invariant base. Iter198 was not solved.

## Streams, controls, failures, and limits

The three complete proof-output streams contain 15,199,582,159 raw bytes total. Each is retained as deterministic gzip, re-expanded in a streaming pass, and matched on byte count, LF count, and SHA256. All are classified `SAT_SEARCH_TRACE` with zero UNSAT-certificate credit. Raw scratch streams were deleted only after those checks; `verification/raw_sat_trace_cleanup.json` records the transition.

`FAILURE_LEDGER.md` records the lost unified-session handle, both lead census outcomes, and the first quotient-check extension mistake. None contributes scientific credit. All scientific children were foreground, lock-serialized, non-detached, and reaped; no solver timeout was configured.

Scientific status remains `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross = {11,12}`. This package gives a candidate kill and 288 additional sound CEGAR exclusions, not a root proof, witness, exhaustion claim, or interval narrowing.
