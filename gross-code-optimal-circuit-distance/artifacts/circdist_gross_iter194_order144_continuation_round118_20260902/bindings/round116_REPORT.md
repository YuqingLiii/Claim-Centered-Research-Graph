# Round 116 proposer report — Gross iter193 invariant-quotient continuation

## Verdict

The mandatory iteration-193 translation quotient is **SAT**. Its complete assignment satisfies all **16,301,485** clauses and decodes to a legal **864-edge, 460-layer** frozen `S_Gross` schedule. Both required complete unrestricted direct-360 queries are also **SAT** at weight at most 10. Independent reconstruction proves that each selected ten-fault mechanism has zero detector syndrome, nonzero logical action, and canonical and physical supports outside the stabilizer span. Therefore this candidate is not a distance-12 witness. Neither exact root branch closes. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, with `D*_Gross in {11,12}`; no narrowing or promotion is proposed.

The strongest sound continuation is a deterministic, checked, **unstarted** iteration-194 frontier. It closes the previously skipped nonfree CSS images, installs four collision-free candidate/CSS selector orbits, compiles an exact base, and adds an independently checked quotient under the complete order-144 translation/CSS action. Iter194 has not been sent to a solver and receives no SAT or UNSAT label.

## Dispatch and immutable bindings

All five required dispatch hashes matched before science:

| object | SHA-256 | bytes |
|---|---|---:|
| canonical Gross YAML | `5fe0aebccc3b97757b0c2560ca18db8fbdbe1c4468ea49153382fbe0fbc51df0` | 143873 |
| scheduler | `e47e27cef7ef026edca8e0cb73eeb3ba969a17212de922f6c29b7a8029c029a4` | 363737 |
| Round115 exact review | `15c31086b2aa8c7f6eaa6bbdd2a4c4b7d61bfaba55b60a142c07e0ac6801f9b5` | 178954 |
| Round114 root manifest | `b041e4919cdd21e834d6bf8bd252302ef7d9449af7bf10a70bf20ff0d01f9b58` | 56689 |
| Round116 ProofPilot record | `1571799f7532a85026a38d32f0596543e98207a3a4d202c9f65028bcd3fb5c67` | 40912 |

The authorized action is `CIRCDIST.gross@dstar-residual`, score `0.00078784493684339`, `P=.10`, `v=100`, `D=4`, `s=32.25`. Budget was observed authorized/pending at 141/142 and is not settled here. The canonical task prose is stale at iter192; the independently installed Round115 evidence/event, exact review, scheduler, and reviewed Round114 package bind iter193. This is disclosed as F116-006 and no canonical file was modified.

## Mandatory iter193 solve

The exact reviewed source has 814,068 blocks, 50,580 selectors, and 869,046 assertions. Base CNF: `f6500190...aa76`, 3,104,384 variables / 11,393,894 clauses. Quotient CNF: `cf9545d5...9f1`, 3,717,824 variables / 16,301,485 clauses. CaDiCaL 1.9.5 (`fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`) ran first with the reviewed clean environment and exact `-t 21600 --no-binary CNF DRAT` binding. It returned 10/SAT in 1469.018411s; the configured cutoff was not reached.

The independent assignment checker required all 3,717,824 variables exactly once and streamed every clause. Semantic replay then checked all primary times, all 648 MC constraints, every resource occupancy, global interleaving, 814,068 exact blocks, all 50,580 selectors, rank compression, all 71 quotient roots, base/quotient projection, and frozen-model replay. Negative controls flipped the constant, truncated the final variable, reversed lex direction, and demonstrated a schedule failing exactly the `(11,0)` root; all were rejected as expected. Candidate hash: `8b4a811074b4442ab875ab17e405120943393f9c8400163e6e7d7d386aac1089`; compressed schedule hash: `433c2edc9ceacf3237be8c768089f746e7f63165c4c587a522663dfb7d4a858b`.

## Complete direct adjudication

The direct formulas retain all 360 columns per sector and no auxiliary search restriction. Xerr is 6,128 variables / 23,092 clauses, CNF `8c8c866d685f1b85e6e922e11aab38a577f1ac88d9186dbabfdcf93e94d0ee26`. Zerr is 6,142 / 23,148, CNF `aae36a930c1f0b1276288b41a30266c50aa237046b9bb3854bcf95a1dbdb5887`. They ran serially after outer replay and returned SAT in 1753.669068s and 2791.716634s.

Xerr selected `D:55, D:58, D:102, D:104, D:105, D:107, D:121, D:124, R:31:0, R:34:0`. Its physical net support is `[30, 32, 33, 35, 55, 58, 102, 104, 105, 107, 109, 112, 115, 118, 121, 124]` and logical parity vector is `[0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1]`. Zerr selected `R:3:1, R:3:2, R:28:1, R:44:0, R:54:0, R:61:1, R:62:0, R:62:1, R:66:0, R:69:2`. Its physical support is `[16, 22, 42, 47, 48, 49, 55, 60, 65, 69, 73, 98, 99, 114, 115, 120, 130, 132, 139, 143]` and logical vector is `[1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]`. Both physical syndromes are empty; both logical vectors are nonzero; both canonical and physical supports are nonstabilizers. Selected-variable flip controls fail formula clauses. Arbitrary-round repair was forbidden because both sectors were SAT.

The three solver proof-output streams contain 30,567,956,303 raw bytes and are retained losslessly as 5,769,292,375 deterministic gzip bytes. They contain zero empty-clause lines and are SAT search traces, not DRAT/LRAT UNSAT certificates. They receive no absence credit.

## Sound exclusions and CSS closure

The direct Xerr selector has a nonfree 36-element translation orbit with stabilizer `[(0,0),(0,3)]`; the direct Zerr selector has a free 72-element orbit. All 144 translated schedule/mechanism pairs were physically replayed. Their CSS images are disjoint orbits of sizes 36 and 72, and all 144 dual translated pairs were replayed. No candidate orbit collides with the installed iter193 registry or another new orbit.

An independent full CSS audit found the exact inherited closure deficit identified by Round115: nine size-36 block orbits (324 blocks) and one size-36 selector orbit (36 selectors). Every member carries parent/source provenance, complete realizing-delta and stabilizer accounting, generator invariance, and physical replay where applicable. Final iter194 counts are 814,392 blocks, 50,832 selectors, and 869,622 assertions. Translation audit checked 1,628,784 block generator images, 101,664 selector generator images, and 4,478,976 group composition cases. The CSS audit found zero missing D images.

## Fresh iter194 base and order-144 quotient

The final source is `f4aafe384ae0a626671b95400f66727007942241cb6988ec9b68bb1a77893091` with semantic payload `b1e7b4677de2549e3802b0e91af35d91f9d735218cd7630b5d9f9b284b15d9cc`. The exact base is `2e72b7bdd8702340fcac7cc706ebb777d5d2a10cc6e670bbd196565e0ece725f`, 3,117,683 variables / 11,438,824 clauses. Its independent encoding checker reconstructed all source roots and definitions, checked 1,048,576 comparison truth cases and 4,354,560 local rank-membership/order cases, and passed five mutation/truncation/direction/bound controls.

The order-144 quotient is `7fade55daeabb8e2a6702552ce8fc9f0c899091cba64bc1d6806f6f93e7af8db`, 4,353,203 variables / 21,323,127 clauses, with 143 nonidentity lex roots. Its checker verified 144 distinct concrete edge permutations, 17,915,904 composition cases, the full geometry, closure bindings, every base-prefix byte, and all 9,884,303 appended clauses. The non-strict lex theorem explicitly permits nonfree orbits. See `THEOREM_NOTES.md` for the proof. A recursive scan finds no iter194 solver log, assignment, DRAT, LRAT, or result; `solver_invocations=0`.

## Process, failures, and scope

All scientific children ran serially. Each wrapped child has exact argv, clean environment, wrapper/child PID, UTC start/end, return code, and stdout/stderr paths in `logs/process/session_process.jsonl`. Exit 10 is the expected SAT code for the three solver calls. Two exit-1 attempts are retained and corrected: the free-only orbit auditor and provisional schema mismatch. There was no detach, wrapper timeout, killed child, or concurrent scientific solver/checker. Early interface operations without PID capture are disclosed in F116-007.

`FAILURE_LEDGER.md` records every known false start. `RESULT.json` is the machine-readable verdict, `FRESH_FRONTIER.json` binds the next frontier, and `THEOREM_NOTES.md` separates the proved claims from the remaining root gap. This package does not claim that its finite registry is an exhaustive characterization of every distance-<12 schedule, does not claim any iter194 solver result, and does not self-award a canonical level.
