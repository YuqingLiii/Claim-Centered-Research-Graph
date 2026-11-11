# CIRCDIST.gross Round122 exact iter196 continuation

## Verdict

The exact reviewed iteration-196 order-144 quotient is **SAT**. Its complete assignment satisfies all 21,362,300 clauses and decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are also **SAT** at exact fault weight 10. Either sector alone kills the candidate; both were independently reconstructed, so repair was forbidden and not attempted.

The only scientific advance after the kill is sound registry growth: four exact generalized-dihedral selector orbits of sizes `36,72,36,72` add 216 distinct selectors. Iteration 197 is sealed **CHECKED_UNSTARTED** and has never been solved.

## Dispatch and mandatory starting frontier

The live scheduler, ProofPilot dispatch, canonical Gross node, Round121 exact review, and reviewed Round120 root manifest match the five dispatch SHA256 values in `INPUT_BINDINGS.json`. The independent preflight rehashed the sealed starting frontier:

- source `31256761866d464eba48c278e2247d6f396a1372ad0508886e06e3f24ea6f51a`, semantic source `f93cd8e600e1b02db801d84a5b6b2eb0def408f3bca65528c8b0a6b5b0e0b73d`;
- state `ab064886695d712b62fddadb8639a75e9d230faa9e8e2d870605ebaf72946da9`, selector state `a960134b6315978cd800261ab5dd6ce287a3fd96c7dda5c33abd19c8671527c9`;
- 814,392 blocks, 51,336 selectors, 870,126 assertions;
- base `cf190...e639`, 3,130,306 variables / 11,477,997 clauses;
- quotient `12d86...593`, 4,365,826 variables / 21,362,300 clauses / 143 roots.

No solver/model/assignment/proof artifact existed in that frontier, and the Round122 ledger had zero prior starts targeting it.

## Exact outer solve and schedule replay

Pinned CaDiCaL SHA256 is `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. The exact sealed quotient was supplied directly, with ASCII proof output enabled from byte zero. The solver returned 10 and was reaped. `output/iter196/solver/assignment_check.json` verifies all 4,365,826 variables exactly once and every clause.

Physical replay reports 356 used layers (`0..355`), 864 edges, 0 resource conflicts, 648 overlap relations, 0 MC violations, global interleaving, 100 overlap-interleaved pairs, 378 whole-check-interleaved pairs, and zero inherited block/selector hits. Raw schedule SHA256 is `aff437a3dea42fcb043590df0b99f1e39c7c91954f0eaec93a1db88feaabd70b` and compressed schedule SHA256 is `32ed7de5031979c256cc085819f168e11e5a0b7adc22ef52229fbd6598e332a3`. All 143 roots and 144 images, including stabilizer cases and corrupt/truncated/reversed/missing-root controls, pass in the orbit audit.

## Complete direct-360 results

The direct queries are outside the outer encoding and use every one of the 360 physical columns. They impose only complete `W<=10`, 72 exact syndrome equations, and a nonzero disjunction over 12 logical rows. No pool, residual pattern, check count, within-check family, sample, or partial restriction appears.

### Xerr

- CNF `8368f46f95e2a2d5960348e66bb1a3dc46fc24dec54d38f6199022788f1c93b2`, 6,124 variables / 23,076 clauses; all checked.
- Selected faults: `D:16, D:24, D:52, D:60, D:76, D:98, D:112, D:134, R:0:2, R:36:2`.
- Exact weight 10; physical net support `[2, 16, 24, 38, 52, 60, 76, 84, 98, 112, 120, 134]`; syndrome empty; logical vector `[0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1]`.
- Canonical and physical nonstabilizer checks pass. Flipping selected variable 17 fails 5 clauses.

### Zerr

- CNF `c91b4367d97cf9ba928e8b106f15be2ed1c945995515fffdc04ba5cfc39cc812`, 6,126 variables / 23,084 clauses; all checked.
- Selected faults: `D:48, D:53, D:55, D:122, R:17:0, R:27:1, R:33:0, R:34:1, R:36:1, R:58:1`.
- Exact weight 10; physical net support `[11, 14, 24, 27, 28, 46, 48, 53, 55, 90, 97, 103, 105, 112, 113, 122, 129, 143]`; syndrome empty; logical vector `[0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0]`.
- Canonical and physical nonstabilizer checks pass. Flipping selected variable 49 fails 6 clauses.

An independent standard-library implementation reconstructs all 720 columns, all clauses, both 72-row syndromes, both 12-row logical systems, stabilizer ranks 66, cross-pairing rank 12, and schedule/resource semantics. The vendored verifier agrees.

## Exact selector closure and iteration 197

All 72 physical translations were replayed for each original and CSS-dual mechanism. Xerr has a size-36 orbit with stabilizer `(0,0),(6,0)`; Zerr is free of size 72. Their CSS images have the same respective sizes. Pairwise collision and inherited-registry checks are zero. The advance installs 108 Xerr and 108 Zerr selectors atomically.

Fresh iter197 identities:

- source `6ce8b8593fabc80ce0917f342126e351da30114802765a46773da348115aec44`, semantic `bee49435279caa3fb6cc02e0f1b145e3568eb54e6d3ac02c49e5bae3c5fa42f4`;
- state `cd005e436ff92c66badefb5a30e83531d81d9339bfbc047ebbdbb32627eb1ed0`, selector state `2b5d1178c5532d62f8e6266d627aaa4c228fa18526e7f79156cc667b1e207608`;
- 814,392 blocks / 51,552 selectors / 870,342 assertions;
- base `f46bc3862e2c4db10570d73d5a364750fa1892d90ecd0fa3d08fe411c3755ef3`, 3,140,244 variables / 11,511,680 clauses;
- order-144 quotient `fe73a93b7a171fd2afcffe210729f165684297d3d85f4260d883e5ed69ffd334`, 4,375,764 variables / 21,395,983 clauses / 143 roots;
- `CHECKED_UNSTARTED.json` `68e06e13c5242beb3d0170565968b911ba68e2b0715d8c3b91a33c4a8f8761b5`, zero iter197 solver invocations and no forbidden artifacts.

## Trace disposition, failures, and limits

All three proof-output streams are retained losslessly as deterministic gzip files and independently round-trip checked. They are SAT search traces, contain no empty-clause line, and receive zero UNSAT-certificate credit. See `proof_streams/*.stream.json`.

`FAILURE_LEDGER.md` records every failed administrative/checker branch and its clean correction. None contributes positive evidence. `PROCESS_LEDGER_CHECK.json` proves exact STARTED/REAPED pairing, no interval overlap, three serial SAT solver runs, no detached/background children, and zero solver invocation targeting iter197.

The replay is solver-free, strictly serial, read-only, and accepts an arbitrary external output directory. Scientific status remains: `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross = {11,12}`.
