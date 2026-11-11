# CIRCDIST.gross Round126 exact iteration-198 continuation

## Verdict and safe boundary

The exact reviewed iteration-198 order-144 quotient is **SAT**. Its complete assignment covers all 4,387,647 variables exactly once and satisfies all 21,434,596 clauses. It decodes to a legal frozen 864-edge schedule. Both mandatory complete unrestricted direct-360 sectors are **SAT** at exact fault weight 10. Either checked sector kills the candidate; both were adjudicated. Repair and gap analysis were therefore forbidden and not attempted.

Four free generalized-dihedral selector orbits of size 72 add 288 distinct sound exclusions. Iteration 199 is sealed **CHECKED_UNSTARTED** and was never solved. Root status is unchanged: `CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, and `D*_Gross = {11,12}`.

## Dispatch and exact reviewed input

The scheduler, ProofPilot record, canonical Gross node, Round125 review, and Round124 parent seal match `INPUT_BINDINGS.json`. A 608-file independent parent rehash passed before use. The mandatory frontier has source `dd0e4f55943381e265b174a0360f2ee2dc0e9c93326b71c315632ffbda6d95a2`, semantic `d41be17da8e398e13b94cf38807d78187247e7318d61ebbeb6d21bc2e7f43f9d`, state `a60e1e378283153a3f24611a9e33cbb97df19bcbe231a9fa515b13fae0ff7287`, selector-state `e25d5ad244f42075e6e4c3f884bb33300c50dbfbdf1bfa74324b1dd964438f53`, 814,392 blocks, 51,840 selectors, and 870,630 assertions. Its base has 3,152,127 variables and 11,550,293 clauses; the exact quotient has 4,387,647 variables, 21,434,596 clauses, and 143 nonidentity roots. Receipt `894686dbda1bb6c8da578aad828cb1122e5fe68c8b2e7ec47341c0fabdf8d03c` records zero prior solver starts and no forbidden artifacts.

## Proof-first outer solve and independent controls

Pinned CaDiCaL SHA-256 is `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9`. The exact sealed quotient was passed directly, with the proof-output pathname present in the initial argv and binary proof mode disabled. Child PID 85987 ran from `2026-09-05T21:34:58.253689Z` to `2026-09-05T21:50:41.698362Z`, returned 10, produced 37,956,205 stdout bytes and zero stderr bytes, and was reaped without timeout or detachment.

The assignment checker covers every variable and clause. Independent semantic replay gives schedule SHA-256 `f4fd87d669c4c5ecfe83dd03a871071208add4cace69b3b963fc74bc13e526f9` with 343 layers `0..342`, zero conflicts, all 648 MC overlaps satisfied, global interleaving, 108 overlap-interleaved pairs, 375 whole-check-interleaved pairs, and zero block or selector hits. A separate orbit control enumerates all 144 schedule images, proves identity stabilizer and lexicographic minimality, checks 1,235,520 recurrence values and all 143 roots, and rejects constant-bit mutation, assignment truncation, reversed lex direction, and omitted-root controls.

The exact equivalence derivation is in `THEOREM_NOTES.md`: byte-exact base prefix plus finite-orbit least representatives proves `SAT(Q198) iff SAT(B198)` without assuming freeness.

## Complete unrestricted direct-360 adjudication

Both formulas sit outside the outer encoding and use every one of 360 physical columns. Their only semantic constraints are `W<=10`, all 72 detector parities zero, and a nonzero vector among all 12 logical rows.

### Xerr

- CNF `310e7c32f4decd001184b6288d3ef8005da67d2f09686412c3f1c71a698023b8`, 6,130 variables / 23,100 clauses; every clause checked.
- Selected faults: `D:26, D:32, D:45, D:48, D:130, R:5:2, R:34:0, R:35:0, R:36:0, R:51:1`.
- Canonical support `[23, 26, 30, 32, 38, 45, 48, 54, 74, 103, 112, 120, 129, 130]`; physical support `[23, 26, 30, 31, 32, 35, 37, 45, 48, 52, 53, 74, 104, 111, 113, 114, 118, 119, 129, 130]`.
- Syndrome `[]`; logical vector `[1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0]`; both canonical and physical supports are outside the stabilizer span.
- Flipping selected variable 27 fails 7 clauses, first at 2826.

### Zerr

- CNF `fa235f94898c9eabac37209e5e2aa5663d3beb8fa847f2083e1a7144c1048a69`, 6,151 variables / 23,184 clauses; every clause checked.
- Selected faults: `D:4, D:6, D:72, D:137, D:139, D:143, R:4:1, R:5:2, R:8:1, R:10:2`.
- Canonical and physical support `[2, 4, 6, 64, 68, 71, 72, 75, 79, 80, 130, 134, 136, 137, 139, 143]`.
- Syndrome `[]`; logical vector `[1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]`; both canonical and physical supports are outside the stabilizer span.
- Flipping selected variable 5 fails 10 clauses, first at 191.

The vendored physical replay and an independent standard-library reconstruction agree. Because both complete sectors are SAT, the candidate is rejected and the protocol forbids a repair attempt.

## Exact orbit accounting and fresh iteration 199

The four translation orbits have sizes `[72,72,72,72]`, stabilizer `{(0,0)}` in each case, 288 distinct selector tuples, no pairwise collision, and no collision with the inherited registry. Every original and CSS-dual translated schedule is legal and every translated mechanism remains weight at most 10, zero-syndrome, and nonstabilizer. The full registry is closed under translations and the CSS involution.

Fresh identities are source `ceb91b607e6434f9ef20c6177ba1ee5792b8688790f88f5ec89ee5b75d8f715f`, semantic `bb10d914be3f18a885513b482dee2573dba4b1e3123d84e2cc1ffb1682a5ec2b`, state `ba0795e0f82282193e6fe5c6566127fb69b680803cf50a216bcdb859933e39ab`, selector-state `faa8d3745780c593b5e4e430c8c49c8bb223beb28f8b0d8ecbf384636e75a049`. Counts are 814,392 blocks, 52,128 selectors, and 870,918 assertions. The independently checked base is `c08af6fc567c6d8554428eac5873c276ee4b89137d7c6bff192baca4608a1f9d` with 3,162,788 variables / 11,584,428 clauses. The independently checked order-144 quotient is `602f91c302883ec3ad6a1d9c4cc6b31b450d00feba059707fdc5c37a69aa71e1` with 4,398,308 variables / 21,468,731 clauses / 143 roots. Receipt `6b421a829cec5b07b63b8208443301f60d3e482735f6d20f722fe78563019f71` records zero iteration-199 solver invocations and no forbidden artifact.

## Streams, failures, and limits

Before sealing, the solver-free replay completed 20 strict-serial child runs and 35 byte-exact or runtime-normalized semantic comparisons. It regenerated iteration 199, reconstructed and checked every base and quotient clause, replayed all outer/direct/orbit/CSS evidence, and reconfirmed the never-solved boundary. Nine repository gates passed, including both proof-DAG scopes, migration/contracts/self-test checks, duplicate-YAML scan, `git diff --check`, and evidence closure. Their exact logs and run records are retained under `recovery_state/recovery`.

All three proof-output streams were enabled from byte zero. Because every solver result is SAT, they are search histories rather than UNSAT certificates. The complete streams contain 23,837,572,292 raw bytes and 4,763,053,464 deterministic-gzip bytes. Each compressed file was decompressed in full and matched on byte count, LF count, and SHA-256. They receive zero UNSAT-certificate credit.

`FAILURE_LEDGER.md` discloses recovery, adapter, and first-assembly failures. They changed no scientific conclusion and receive no credit. The original interrupted-worker ledger history is preserved. All scientific children were foreground, strict-serial, non-detached, and reaped, with no solver timeout.

This package supplies a checked candidate kill and 288 additional sound CEGAR exclusions. It supplies neither a distance-12 witness nor a universal `<=11` theorem, so it does not close the root or narrow the interval.
