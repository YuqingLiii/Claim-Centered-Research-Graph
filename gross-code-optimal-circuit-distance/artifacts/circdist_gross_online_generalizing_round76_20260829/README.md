# Gross exact online-generalizing CEGAR — round 76

Date: 2026-08-29  
Verdict: **MATERIAL-CHECKED-PROGRESS-NOT-CLOSED**

This sealed proposer package continues the exact unrestricted Gross-code search from the round-75 reviewed, unstarted iteration-54 frontier. It completes twenty-four online iterations, 54 through 77, in strict serial foreground processes. It modifies no canonical claim, scheduler, protocol, generated view, review, or predecessor artifact. It supplies positive checked progress and freezes iteration 78; it does not prove physical absence, outer exhaustion, or either branch of the Gross root.

## Bound start

- round-74 package `SHA256SUMS.txt` SHA-256: `321eb6ccaae3795e866b0cad409571b35dff7b7b17a84c614c8ab1a23b8e498c`;
- round-75 exact review SHA-256: `a6ee9d2c18291f3474672fb13682e6720a0f2d313da138da26397e67ccd48cc8`;
- exact reviewed unstarted state: `1,440 + 20 + 4,740 + 566 + 134 + 108 = 7,008` blocks, `G=5,440`, `D=108`, registry `24`;
- exploratory round-63 pair clauses installed: **0**.

## Result

All 24 fresh unrestricted outer queries are SAT. Every stored schedule has all 864 named CNOT edges, all 648 measurement-collision constraints, one edge once, one gate per qubit-time, compressed idle layers, and global X/Z interleaving. Each formula and fixed schedule has a separate independent reconstruction.

Both direct sectors were generated unconditionally for every candidate. All 48 formulas are SAT. Their actual primary domain is exactly **360 elementary columns = 144 data singletons + 216 residual elementary-fault columns** per sector. The 1,884-member weight-12 pool is not the primary domain; it binds quotient representatives and positive completions. Every complete assignment satisfies every DIMACS clause and raw-reconstructs canonical and physical zero-detector-syndrome, stabilizer-nonmember mechanisms of nonzero logical quotient and at most ten elementary faults.

The run preserves 48 candidate-exact blocks. Immediate online generalization constructs all participating `6!=720` local-order catalogs, exact positive pair completions, and exact joint GF(2) relations. From 420 raw candidates, semantic filtering against the full current library retains 303. Every retained pair tuple was literally visited and physically replayed (2,637,648 tuples). The two retained multi-check domains cover 55,037,740,032 tuples by universal factorization over every allowed local record, explicit canonical=physical signature identity, all exact DP states/transitions, fixed selector construction, and exact product counts.

The unstarted restart is iteration 78:

```text
1,440 unary + 20 round-62 + 4,740 round-69 + 566 round-72
+ 134 round-74 + 303 round-76 generalized + 156 dynamic exact
= 7,359 installed blocks; G=5,743; D=156; registry=72.
```

No direct sector was UNSAT, so no candidate-specific Gross DRAT/LRAT absence proof exists and repair was never licensed. No outer UNSAT proof exists. `D*_Gross` remains in `{11,12}`.

## Audit map

- `RESULT.json`: machine-readable claim boundary and restart hashes.
- `MATH_DERIVATION.md`: definitions, formulas, direct completeness, catalogs, selectors, DP proof, and limitations.
- `ITERATION_LEDGER.md`: all 24 online transactions.
- `CLASSIFICATION_LEDGER.md`: aggregate catalog/relation/term/tuple counts.
- `cegar/iter*/`: outer formulas, schedules, complete direct CNFs/assignments, raw mechanisms, and online objects.
- `classification/round76_retained_terms.json.gz`: all retained terms and deletion controls.
- `classification/installed_generalized_terms.json.gz`: complete iteration-78 generalized library.
- `cegar/dynamic_blocks.json.gz`: complete iteration-78 dynamic state.
- `restart/`: exact reviewed iteration-54 and proposer iteration-78 restart files.
- `controls/round76_proof_checker/`: fresh valid and corrupt DRAT/LRAT toolchain controls; not Gross proofs.
- `SOURCE_BINDINGS.json`, `PROCESS_LEDGER.json`, `FIX-2.md`: source, process, and incident audit.
- `COMPRESSED_INVENTORY.json`: deterministic gzip compressed/uncompressed dual hashes.
- `verify.py`: quick and full self-contained replay.
- `SHA256SUMS.txt`: external non-self package seal.

## Verification

```bash
python3 -m venv /tmp/circdist-r76-review-venv
/tmp/circdist-r76-review-venv/bin/pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r76-review-venv/bin/python verify.py --quick
PYTHONDONTWRITEBYTECODE=1 /tmp/circdist-r76-review-venv/bin/python verify.py --full
```

Add `--repo-root /absolute/path/to/Claim-Centered-Research-Graph` to verify live source-package, review, protocol, scheduler, and node bindings. The proposer verifier is reproducibility evidence, not independent review. **Fresh independent exact review is required before canonical use or restart.**

## Release-verification stages

The package distinguishes three stages. `development_precompression_full` is an engineering replay on uncompressed staging content; its sealed log and run record are reproducibility evidence but are not the accepted release gate. `accepted_preseal_full` is run after deterministic gzip and `COMPRESSED_INVENTORY.json` are final, before seal creation; it must exit zero with `status=PASS` and it directly checks every final gzip member through compressed/uncompressed dual hashes plus transparent materialization. `post_copy_sealed_full_live` is run only after atomic installation with `--repo-root`; it additionally verifies the root seal and live source/review/protocol/scheduler/node bindings. A final sealed quick replay is also required.

Accepted-preseal and post-copy stdout stay outside the immutable package: inserting a run log after the run would change the tree that run certified. `verification/RELEASE_GATES.json` gives the exact commands and acceptance predicates. The release operator may atomically install this directory only after the accepted-preseal quick and FULL both pass. The package remains a proposer artifact; these self-replays do not replace fresh independent exact review.
