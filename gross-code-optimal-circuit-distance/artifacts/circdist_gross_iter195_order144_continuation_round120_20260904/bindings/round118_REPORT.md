# CIRCDIST.gross iteration-194 order-144 continuation — Round 118 proposer report

## Exact verdict

The exact reviewed iteration-194 order-144 quotient is **SAT**. The retained assignment sets each of all 4,353,203 DIMACS variables exactly once and satisfies every one of 21,323,127 clauses. It decodes to a legal frozen-family schedule with 864 named edges, 648 MC overlaps, 310 used layers (0 through 309), no resource conflict, no MC violation, global interleaving, no hit in 814,392 installed blocks, and no hit in 50,832 installed selectors.

Both complete unrestricted direct-360 adversaries at canonical threshold W=10 are also **SAT**. The Xerr query has 6,154 variables and 23,196 clauses; the Zerr query has 6,179 variables and 23,296 clauses. Each complete assignment was checked variable-by-variable and clause-by-clause. Independent standard-library reconstruction of all 360 physical columns per sector proves exact fault count ten, empty detector syndrome, nonzero logical action, and nonstabilizer status in both canonical and physical coordinates. Thus this schedule is killed. The protocol forbids repair/gap adjudication because that branch is entered only after both complete direct queries prove UNSAT.

This does not close either root branch. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, and `D*_Gross` remains `{11,12}`. Branch A still lacks a legal schedule surviving both direct sectors plus repair/gap. Branch B still lacks a universal proof that every legal frozen schedule has distance at most 11. Fresh review is required before any canonical claim.

## Dispatch and immutable inputs

The sole scheduler winner was `CIRCDIST.gross@dstar-residual`, score `0.001373516289473971`. The bound SHA-256 values are:

- scheduler: `9053f6d7de5acfccfed840381681991ad88f068b5f250f92b1e266ec2b936591`
- ProofPilot: `165edab1701c04e1ac79e3b5eb7d5634c5a8f20d99332d552878164565296525`
- canonical node: `792c2db47abbb62fa1db07c1d3ebf780501fb1c8356d33e371c3c6ad80d19f5b`
- Round117 exact review: `26fd4c8c39910dae235348efc30e237c7f9ea3d93146076f3580b8c4459cf925`
- reviewed Round116 package root manifest: `2d214dc846b5cf8e7ef329e0baf9ed5204ad6340bcb9e93ac495e8e9e7a87143`

The solved source is `f4aafe384ae0a626671b95400f66727007942241cb6988ec9b68bb1a77893091` with semantic source `b1e7b4677de2549e3802b0e91af35d91f9d735218cd7630b5d9f9b284b15d9cc`, state `522848f50de5f9d7015ca326be4a8f0a69e1342bf7c5e27886c6b4dcdaf25c4f`, selector state `a0bf27750c0cf74196c2bb161ed70ad879b3bb7e117172adc34c13d8f02236d1`, base CNF `2e72b7bdd8702340fcac7cc706ebb777d5d2a10cc6e670bbd196565e0ece725f`, and exact quotient `7fade55daeabb8e2a6702552ce8fc9f0c899091cba64bc1d6806f6f93e7af8db`. The reviewed quotient adds 143 lex roots for the complete 144-element translation/CSS action and is equisatisfiable with the full base without assuming free orbits.

## Proof-first solve and assignment checks

All scientific children ran in the foreground under `source/serial_exec.py` with a nonblocking exclusive lock. Each process record contains exact argv, wrapper/child PID, UTC timestamps, return code, streams, and reap state. There was never more than one active scientific child.

The pinned solver is CaDiCaL 1.9.5, SHA-256 `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. The exact logical commands were:

```text
cadical -t 21600 --no-binary input/iter194/order144_quotient/outer.cnf output/iter194/solver/outer.drat
cadical -t 21600 --no-binary output/iter194/direct/direct360/Xerr.cnf output/iter194/direct/solver/Xerr.drat
cadical -t 21600 --no-binary output/iter194/direct/direct360/Zerr.cnf output/iter194/direct/solver/Zerr.drat
```

All returned rc=10 and were reaped. Durations were 992.393032 s outer, 6874.935513 s Xerr, and 656.566918 s Zerr. Proof output was enabled from byte zero. Because the results are SAT, these streams are search traces and receive no DRAT/LRAT UNSAT credit. Deterministic gzip retained all 33,456,766,269 raw bytes as 6,685,262,605 compressed bytes; a full decompression rehash matched raw SHA-256, byte count, LF count, and zero empty-clause lines for every stream.

For the outer model, the assignment SHA-256 is `74bd8ff5cba097380359e7b6d61fc75749758068df559fda97d378927cd06f98`. The independent orbit-control audit also rechecked the 3,117,683-variable / 11,438,824-clause base prefix, 8,640 primary time bits, 1,235,520 recurrence values, all 143 edge-map hashes and lex roots, and the complete 144-image schedule orbit. This particular schedule has trivial stabilizer and 143 strict nonidentity roots. Corrupt, truncated, reversed-lex, and missing-root controls were rejected.

## Direct adversary derivation

For each sector the query selects from all 360 named physical columns. If `s_j` is the selection bit, the exact threshold constraint is `sum_j s_j <= 10`. For each detector row `h`, the CNF enforces `XOR_j(s_j * h_j)=0`; twelve independently reconstructed logical rows produce `ell`, and the query enforces `ell != 0`. No pool, residual pattern, check count, within-check family, sampling, or partial-result restriction is present.

Xerr selects `D:33, D:36, D:81, D:114, D:119, D:137, R:28:0, R:37:2, R:46:2, R:52:2`. Its physical support is `[29, 33, 36, 38, 42, 46, 53, 55, 70, 81, 97, 106, 114, 119, 130, 137]`, detector syndrome is empty, and logical vector is `[1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0]`.

Zerr selects `D:115, D:116, D:118, D:119, D:127, D:130, R:55:1, R:58:1, R:62:0, R:65:0`. Its physical support is `[43, 52, 55, 62, 65, 109, 115, 118, 126, 127, 128, 130, 132, 133, 135, 136]`, detector syndrome is empty, and logical vector is `[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.

The independent auditor rebuilt incidence, 720 sector columns, syndromes, logical rows, canonical/physical supports and stabilizer spans without importing the frozen model implementation. Flipping one selected primary variable caused clause failures in each negative control.

## Sound exclusion closure

Translations form `G = Z_12 x Z_6`, so `|G|=72`. For any selector mechanism `m`, orbit-stabilizer gives `|Orb(m)| = 72/|Stab(m)|`. Xerr has stabilizer `{(0,0)}`, hence orbit size 72. Zerr has stabilizer `{(0,0),(0,3)}`, hence orbit size 36. The CSS involution `D` swaps Xerr and Zerr and satisfies `D^2=1` and `D T_delta D = T_-delta`; its two dual translation orbits again have sizes 72 and 36. Exact semantic keys prove the four orbits pairwise disjoint and collision-free against all 50,832 installed selectors.

Every one of the 72 group elements was physically replayed for each original and CSS-dual representative: 288 replays total. All preserve legal scheduling, weight at most ten, zero syndrome, and nonstabilizer action. Therefore exactly 216 distinct selectors are soundly installed, giving 51,048 selectors. No blocks are added, leaving 814,392. The full registry is closed under translations and CSS, including the nonfree size-36 orbits.

## Fresh iteration-195 frontier

The deterministic next source is `e32f3e98e8c7b1a73a59a2e75b963abf080abcf23457aeb90bf25f17bcfdc16a`, semantic SHA-256 `fa3a1b80b6b33a6ef14fa314aba2fd8acc394af588bb670a36d8bcffb44cb55b`, state `4ad41e85dcb37973caec6ac8cc9939f3e3b9aa842ba2ff00e1c8c0007bd44be0`, and selector state `231a37783821b049e50f3f9920413010bd497382f4c02f4beee7637757124857`. It has 814,392 blocks, 51,048 selectors, and 869,838 assertions.

The checked base is 3,124,223 variables / 11,459,291 clauses, SHA-256 `952b2dc06d859cb8fa30a51ce3a6e32cd47ac6ffc310e6465ab205a0b084c099`. The checked order-144 quotient is 4,359,743 variables / 21,343,594 clauses with 143 roots, SHA-256 `cbab91a2bd7ba5e89db0e6cf52f8b5d3daaa9d6d1a33b1388b1db423e11cdbd6`. The quotient checker reconstructed all 9,884,303 appended clauses, established unique extension, checked all 144 group permutations, and rejected corrupt/truncated primitive controls.

Iteration 195 is genuinely **UNSTARTED**: state `started=false`, no SAT/UNSAT status, zero solver invocation in the session ledger referencing this frontier, and no solver/model/assignment/proof artifact anywhere beneath `frontier/iter195`. Its mandatory next action is to solve exactly this retained quotient proof-first.

## Failed attempts and controls

Nine wrapped rc=1 false starts are retained: an inherited order-72 orbit checker on 143 roots; an initial attempt to edit its read-only scratch copy; an iter193 CSS count assertion on iter194 data; a non-scientific `len(int)` summary probe; the rejected novel iter195 schema label; a mistyped recovery tag; the gzip trace suffix mismatch; an unstarted auditor that initially required a state field absent from the established schema; and the first documentation writer using the wrong reviewed metadata-key name. One later administrative log-copy command used a misspelled lock pathname while no other child was active; it returned rc=0, created no concurrency, and was corrected under the canonical lock. Each affected scientific check was rerun from the beginning after a narrow correction and passed. `FAILURE_LEDGER.md` gives paths and consequences. None is used as positive evidence.

## Reviewed parent documentation defects

The Round116 sealed parent is preserved byte-for-byte and was not edited. This package copies its original inventory and REPORT under `bindings/`. As Round117 found, the parent inventory has one non-load-bearing temporal self-prefix row for `FILE_INVENTORY.jsonl`; its root manifest still binds the final 66,305-byte inventory. The parent REPORT also says two corrected rc=1 attempts although the sealed process/failure ledgers show four. These are disclosed here and are not silently rewritten.

## Replay

The preseal solver-free science replay passed 20 serialized checker/builder runs and 35 exact or runtime-normalized comparisons; all children were reaped and iteration 195 remained unstarted. All eight ordinary zero-exit repository gates passed. Evidence closure returned rc=1 with 493 unique unlinked-evidence diagnostics, all and only beneath this single new unreviewed package; the retained interpreter classified that as the permitted pre-review condition.

After sealing, run:

```text
./replay.sh /private/tmp/circdist-round118-replay
```

The replay writes only to the requested external directory, never invokes a SAT solver, verifies the seal and result, rechecks all three complete assignments and clauses, replays schedule/orbit/direct evidence, regenerates and checks the fresh source outside the package, checks base and quotient encodings, fully decompresses and rehashes all SAT traces, and confirms iteration 195 remains unstarted.
