# CIRCDIST.gross iteration-195 order-144 continuation — Round 120 proposer report

## Exact root verdict

The exact reviewed iteration-195 order-144 quotient is **SAT**. Its retained assignment covers all 4,359,743 DIMACS variables exactly once and satisfies all 21,343,594 clauses. The decoded frozen schedule has 864 edges, 325 used layers (0 through 324), no resource conflict, all 648 MC overlaps accepted, no MC violation, global interleaving, zero hits among 814,392 installed blocks, and zero hits among 51,048 installed selectors.

Both complete unrestricted direct-360 sectors at `W=10` are independently **SAT**. Xerr has 6,142 variables and 23,148 clauses; Zerr has 6,135 variables and 23,120 clauses. Every variable and every clause was checked. Independent physical reconstruction establishes weight ten, zero detector syndrome, nonzero logical action, and nonstabilizer status in canonical and physical coordinates for both mechanisms. The schedule is therefore killed. Repair was not entered because the protocol permits it only if both complete sectors prove UNSAT.

Neither root branch closes. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED**, and `D*_Gross={11,12}`. There is no certified distance-12 schedule and no universal proof that all legal frozen schedules have distance at most 11.

## Dispatch and immutable input

The sole authorized winner was `CIRCDIST.gross@dstar-residual`, score `0.0010998258664973192`. Bound SHA-256 values are scheduler `0614734c7b1e4227935a0ec82e973d43e46be761baba6e3d5a706b01b0473177`, canonical node `0b30330901d01b6eec2bb7dae69bf7aa9c4cc4530060cbed55382313ec9cbe96`, Round119 exact review `d79e9ca01e43f646bf1fdd2bcfd7fa05c3845da4d7d4e8f7cd75b37d3bdbdd46`, Round118 root manifest `c4e089e3daaebccca09a4ba12b338e751321b62054b997440837c8b6d905d329`, and Round120 ProofPilot `10b4cb531ff91bc13cbf926329a1a367baf71874f011d68b0132751f057bfcdd`.

The independently reviewed source is `e32f3e98e8c7b1a73a59a2e75b963abf080abcf23457aeb90bf25f17bcfdc16a` (semantic `fa3a1b80b6b33a6ef14fa314aba2fd8acc394af588bb670a36d8bcffb44cb55b`), state `4ad41e85dcb37973caec6ac8cc9939f3e3b9aa842ba2ff00e1c8c0007bd44be0`, selector state `231a37783821b049e50f3f9920413010bd497382f4c02f4beee7637757124857`, base CNF `952b2dc06d859cb8fa30a51ce3a6e32cd47ac6ffc310e6465ab205a0b084c099`, and order-144 quotient `cbab91a2bd7ba5e89db0e6cf52f8b5d3daaa9d6d1a33b1388b1db423e11cdbd6`. Before science, `CHECKED_UNSTARTED` was independently replayed: 15 precursor files, state `started=false`, zero solver invocations, and no assignment/model/proof artifact.

## Quotient and proof-first solve

For the generalized-dihedral action `H=(Z_12 x Z_6) semidirect C_2`, `|H|=144`. The quotient is

`Q = B and AND_{g in H, g != e} [t <=_lex g.t]`.

The lex inequalities are non-strict. Every finite orbit has a lex-minimal element; stabilizer-equal images satisfy equality, so equisatisfiability never assumes a free orbit. The checker reconstructed the byte-exact 11,459,291-clause base prefix, all 9,884,303 appended clauses, the unique extension, 143 roots, the full action, and corrupt/truncated controls.

Pinned CaDiCaL 1.9.5 is `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. No timeout was set. Solver child PIDs/times/rc were outer `28251` / `823.576569` s / 10, Xerr `28678` / `2849.984073` s / 10, and Zerr `32274` / `512.411197` s / 10. All were foreground, nonoverlapping, and reaped. Proof output was enabled from byte zero.

Because all outcomes are SAT, the three retained proof-output streams receive zero UNSAT-certificate credit. They contain 20,645,231,426 raw bytes and 3,924,456,936 deterministic-gzip bytes. Independent decompression reproduced each raw SHA-256, byte count, LF count, and zero empty-clause lines.

The schedule assignment is `32c26d5a7a91cb69a79e42fd14327abb72ad9184df0786260eb32c9052206f3d`; raw schedule `c08fec75579ef0eb10a9bb496678dfcc61bcffff126f935e14e4d9b63b48b270`; compressed schedule `764e04ea49c6be4704f53bb4e2cbf275bd81c99d8fec6723c3379b4da20c4e4d`. The full 144-image audit found orbit size 144 and trivial stabilizer, checked 8,640 primary time bits, 1,235,520 recurrence values, and all roots. Flipped, truncated, reversed-lex, and missing-root controls were rejected.

## Complete direct sectors

For each sector, all 360 physical columns are available. With selection bits `s_j`, the query enforces `sum_j s_j <= 10`, all 72 detector XOR equations equal zero, 12 logical parity equations, and a nonzero logical vector. No pool, residual-pattern, check-count, within-check-family, sampling, or partial-result restriction is present.

Xerr selects `D:49, D:60, D:69, D:74, D:78, D:83, D:134, R:22:1, R:57:0, R:63:2`. Its physical support is `[9, 40, 49, 59, 60, 64, 69, 74, 78, 83, 91, 100, 126, 134, 135, 141]` and logical vector is `[1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1]`.

Zerr selects `D:36, D:58, D:59, D:73, D:84, D:93, D:143, R:2:0, R:8:2, R:10:1`. Its physical support is `[4, 7, 36, 58, 59, 62, 72, 78, 80, 84, 93, 128, 134, 143]` and logical vector is `[0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0]`.

The vendor replay and an independent stdlib auditor rebuilt all 720 sector columns, both syndromes, logical rows, canonical/physical supports, and stabilizer spans. Flipping one selected variable caused clause failures in each negative control.

## Sound selector closure

Translations form `G=Z_12 x Z_6`, `|G|=72`. For each mechanism `m`, `|Orb(m)| |Stab(m)|=72`. The original Xerr and Zerr mechanisms and their CSS-dual mechanisms each have orbit size 72 and stabilizer `{(0,0)}`. The CSS involution swaps sectors, maps data qubits by `D`, checks by negation, preserves the residual-kind convention, and satisfies `D^2=1` and `D T_delta D=T_-delta`.

The four exact selector-tuple orbits are pairwise disjoint and collision-free against the inherited CSS-closed registry. Every translation was replayed physically for every original/dual mechanism: 288 replays. Exactly 288 selectors, 144 per sector, were added, giving 51,336 selectors; blocks remain 814,392. Tuple identities, realizing deltas, stabilizers, source schedule hashes, and provenance live in `frontier/iter196/source.json.gz` and the orbit audits.

## Fresh iteration-196 frontier

The deterministic source is `31256761866d464eba48c278e2247d6f396a1372ad0508886e06e3f24ea6f51a`, semantic `f93cd8e600e1b02db801d84a5b6b2eb0def408f3bca65528c8b0a6b5b0e0b73d`, state `ab064886695d712b62fddadb8639a75e9d230faa9e8e2d870605ebaf72946da9`, selector state `a960134b6315978cd800261ab5dd6ce287a3fd96c7dda5c33abd19c8671527c9`. It has 814,392 blocks, 51,336 selectors, and 870,126 assertions.

The checked base is 3,130,306 variables / 11,477,997 clauses, SHA-256 `cf1907663bca93d838d85ba7a4eb8f682f3939b601d4a0295905699f1118e639`. The checked order-144 quotient is 4,365,826 variables / 21,362,300 clauses with 143 roots, SHA-256 `12d86dfec0d588760a42edc7a8d43ac6f0172415956384bce461da592e08a593`. Iteration 196 is **CHECKED_UNSTARTED**: zero solver invocation and no assignment/model/proof artifact. It must receive fresh independent review before its exact retained quotient is solved proof-first.

## Controls, defects, and replay

`FAILURE_LEDGER.md` retains every failed branch and correction. The inherited iteration-195 quotient checker’s prose says “iteration-194”; its machine hashes, counts, schema inputs, and invocation bind iteration 195, so this is classified as non-load-bearing documentation. The new iteration-196 checker corrects the prose and was fully rerun.

The preseal solver-free replay passed 18 serialized runs and 35 comparisons with zero solver invocations. Eight ordinary repository gates passed. Evidence closure returned rc=1 with 498 unique diagnostics, all under this single new unreviewed package; the retained interpreter classifies that as the expected pre-review condition. `replay.sh` writes only to an explicit external directory and never invokes a solver.
