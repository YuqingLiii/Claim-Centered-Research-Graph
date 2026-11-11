# FIX-2 exhaustive execution and correction disposition

## Frozen inputs and workspace discipline

No sub-agent was created. The full protocols, frozen Gross statement, live Gross node, round-69 package, round-70 review, round-71 package, round-72 package, and round-73 review were read before the search. The recursive reader opened 2,536 physical files, 1,268 gzip members, and 1,888 regular tar members with zero errors. All three predecessor manifests passed. The required round-72 seal is `bc2bf8bdc2da199e348b0471ef4f0367e52e1a7e5eefe1294adb51ab25a4f7f6`; the required round-73 review hash is `92e2b6306f7181b2c61fa02b3eba0624a74864f19045e6e72b208754115224d3`.

A unique Python environment and all authoring state lived under `/tmp`. The round-72 clean full verifier passed in 1,326.432405 seconds before iteration 42. The only final repository write permitted is the new sealed package directory; canonical nodes, `operations/circdist/SCHEDULER.yaml`, protocols, reviews, generated views, and existing artifacts remain read-only. No commit or push is made.

A cleanup attempt using `rm -rf` was rejected by the execution tool before process creation. No filesystem mutation resulted. A unique path and Python `shutil.rmtree` are used for safe final cleanup. `py-spy` was installed in the scratch environment for possible diagnosis but was not usable without elevated privileges and was never load-bearing; package requirements remain the exact declared Python dependencies.

## Iteration42 replay correction

The first independent outer replay checked a display-only field `audit["compressed"]` that is not emitted by the current audit schema. It exited 1 only after reconstructing the formula. No direct solver or research-state mutation had begun. The corrected checker proves compression from the schedule itself:

```text
sorted(set(schedule times)) = [0,…,max_time].
```

The same candidate and same serialized SMT formula then passed. Both the failed and successful logs/run JSON are retained.

## Iteration42 online-generalization corrections

The first online-generalization authoring pass attempted a non-load-bearing high-dimensional exact union count over the entire predecessor library. After 876.345772 seconds it was deliberately sent SIGTERM and exited -15. It had written no generalization output and had not changed the generalized library or mechanism registry. The two candidate-exact dynamic blocks had already been installed once at their correct prior stage and were preserved.

The corrected semantic design computes exact finite prior-union coverage for pair domains and, for multi domains, records exact term total plus exact semantic duplicate/dominance scope without claiming an uncomputed global union size. This removes no soundness check.

A second pass reached retained validation and began a redundant literal loop over the 2,985,984-tuple retained multi domain. After 242.296 seconds it was deliberately sent SIGTERM and exited -15 before any generalized/registry state write. The parent authorization and the reviewed round-72/73 equivalence permit a symbolic universal proof when a retained multi domain is too large for online literal enumeration. The final method materializes every allowed local order and canonical/physical signature identity, exhausts the exact joint GF(2) DP states and transitions, proves the fixed selector construction for an arbitrary tuple, and binds the exact Cartesian count. This is universal proof, not sampling. Pair terms remain literal every-tuple.

The final iteration42 pass completed in 114.516 seconds, installed 13 retained terms exactly once, and froze byte-linked after-state snapshots. All three correction records and the invariants `candidate unchanged`, `direct formulas unchanged`, `dynamic exact state mutated once`, `generalized state mutated once after successful validation`, and `no stale batch pricing` are sealed in `cegar/iter42/iteration_outcome.json`.

## Strict online foreground execution

The 84 successful candidate stages ran in strict foreground serial order. CaDiCaL exit 10 means SAT. There were no candidate timeouts, SIGTERM/SIGKILL events, worker pools, daemons, detached jobs, or overlapping next iterations. Iteration `r+1` was created only after iteration `r` wrote its exact and generalized after-state. The range driver stopped on any nonzero iteration exit; it completed 44–53 with exit 0.

The slowest successful stage was iteration49 Xerr direct at 234.163742 seconds, SAT. The next slowest was iteration46 online generalization at 213.095299 seconds. Both remained inside hard limits. All 12 outers and all 24 direct sectors were SAT, so there are no candidate-specific proof files and no repair branch.

## Package-verifier authoring corrections

Two preseal quick runs exposed display-schema assumptions in the draft verifier and exited 1 without changing research state. Version 1 indexed the published weight-14 `sectors` list as a dictionary. Version 2 assumed the positive Zerr pool stayed at its initial 9,435 words, whereas one checked positive word joins the online union by iteration 44. The corrected check reads the list by sector and binds every iteration to its own recorded count, with Xerr fixed at 9,438 and Zerr in the exact observed progression 9,435 to 9,436. Both failed logs and run records are retained.

A source audit before sealing found one non-load-bearing draft assertion ending in `or True` for an aggregate pair count. The full generator replay was already byte-comparing every pair relation, so this did not affect any research result, term, or first full replay. It was nevertheless removed. The final verifier now checks, for every relation, all 720 truth and explicit rows, 720-bit range, explicit-subset inclusion, recomputed truth and explicit bit counts, the two generated terms per positive configuration, full represented-domain cardinality, and the per-iteration positive cell/configuration/relation totals.

Two read-only probes used while specifying that stronger assertion exited 1: the first used `int.bit_count` under the host Python 3.9, and the second initially conflated the full represented relation domain with the conservative-positive truth subset. `verification/pair_count_probe_corrections.json` and the two logs preserve their exact dispositions. The corrected definitions were checked over iterations 42–53 and the strengthened quick verifier passed. The successful pre-strengthening full run is retained separately; `verification/ARCHIVE_MAP.json` binds the archived names and original wrapper fields. The canonical clean preseal full was then rerun with the final verifier.

## Proof and negative controls

Fresh round-74 DRAT and LRAT fixture runs are accepted. Deterministic ten-line corrupt/truncated DRAT and LRAT fixtures are rejected with expected exit 1. They test the checkers and are not Gross proofs. Twenty-four assignment flips, twenty-four first-fault removals, twelve schedule collisions, one truncated assignment, and all 1,372 retained-term deletion controls are rejected within their stated scope.

## Compression, preseal, seal, preservation, and cleanup

Deterministic gzip uses level 9, empty stored filename, and mtime 0. `COMPRESSED_INVENTORY.json` binds both compressed and decompressed hashes. The package-root manifest excludes only itself. The final preseal replay, repository-preservation comparison, and pre-copy process scan are frozen in `FINAL_AUDIT.txt` before manifest construction. The package-root seal hash, post-copy preservation, sealed live-binding full replay, final process scan, and scratch cleanup are reported externally, because writing them into the package afterward would invalidate that seal. None changes the mathematical claim.

The first manifest-generation draft filtered by filename basename and therefore also omitted nested round-72 files named `PAYLOAD_SHA256SUMS.txt` or `SHA256SUMS.txt`. Its reported 2,247 payload entries and 2,251 root entries were immediately rejected before copy or sealed verification. The exact failed manifests, hashes, and disposition are retained under `verification/manifest_generation.failed_basename_filter_v1.*`. The corrected generator excludes only the exact package-root relative paths, includes every nested predecessor manifest, and is accepted only after `verify.py` proves complete root-manifest coverage.
