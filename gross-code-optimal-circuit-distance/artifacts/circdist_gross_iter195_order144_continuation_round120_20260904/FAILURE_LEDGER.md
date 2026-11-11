# Failure ledger — Round 120

No failed run contributes positive evidence. Expected solver rc=10 is not a failure.

| ID | event / process tag | rc | defect | correction and consequence |
|---|---|---:|---|---|
| F120-001 | initial `sysctl` and unprivileged `ps` probes | blocked | The restricted host denied system/process inspection; a chained command prevented its second read-only probe. | An approved focused process query found no competing solver before science. No formula or evidence changed. |
| F120-002 | first direct-formula build | 1 | Clean environment omitted the reviewed vendored z3 module. | Reran the whole builder with the exact parent `python/site-packages`; both formulas were regenerated and passed. |
| F120-003 | first Xerr CaDiCaL start | 1 | The target proof directory did not yet exist, so CaDiCaL failed before search/output. | Created the directory through the serial wrapper; reran proof-first from byte zero with a new output and obtained the checked SAT result. |
| F120-004 | first vendor direct replay | 1 | The vendor interface expected retained `Xerr.solver.log` and `Zerr.solver.log` filenames. | Copied the exact solver stdout streams under those names; the full vendor replay passed. |
| F120-005 | first process-ledger self-check | 1 | It read the live ledger after its own STARTED row and before its REAPED row. | Final validation uses an atomic cutpoint produced by the self-excluding snapshot tool. |
| F120-006 | inherited iteration-195 quotient check prose | n/a | The conclusion says “iteration-194” although all input hashes/counts/invocation bind iteration 195. | Classified as non-load-bearing; the parent package was not edited. The iteration-196 checker was adapted, corrected, and fully rerun. |
| F120-007 | copied source edit attempts | n/a | Sealed parent modes initially made scratch copies read-only; one patch therefore failed. | Changed permissions only on scratch copies, then applied and syntax-checked adaptations. |
| F120-008 | `/dev/stdout` wrapper inspection | 1 before child start | The serial wrapper could not reopen `/dev/stdout` on this host. | Used retained-file reads for administration only; scientific children stayed under the lock. |
| F120-009 | initial compiler-source lookup | 2 | The first path omitted the inherited `round116_reviewed/` directory. | Located and used the exact reviewed compiler; compilation and independent checking passed. |
| F120-010 | syntax-check warnings | 0 | Clean `/usr/bin/python3` reported `confstr()` fallback warnings for its temp directory. | All syntax checks returned zero; runtime commands explicitly pinned `TMPDIR` to the unique scratch tree. |
| F120-011 | administrative interface boundary | n/a | Initial read-only discovery, tool-host wrapper launches, `apply_patch` scratch writes, and the approved repository copy are outside the inner child ledger. | Disclosed in `ADMIN_INTERFACE_OPERATIONS.json`; none invoked a solver/checker or supplied positive science. |
| F120-012 | first final cutpoint-ledger audit | 1 | The initial checker classified the earlier `cadical --version` identity probe as a query process. | Corrected the classifier to report one rc=0 identity probe separately from four query invocations; the unchanged 228-row cutpoint then passed. |
| F120-013 | first post-cutpoint documentation rewrite | 2 | The administrative invocation omitted the writer's required `--session-ledger` argument, so argparse exited before reading or writing package evidence. | Reran the writer with the immutable package cutpoint ledger; regenerated documents were then independently rechecked. |

All recorded scientific and construction children were foreground and serialized. No process was killed, detached, timed out, or left unreaped. Exact scratch cleanup and postseal survivor checks are recorded outside the immutable cutpoint at completion.
