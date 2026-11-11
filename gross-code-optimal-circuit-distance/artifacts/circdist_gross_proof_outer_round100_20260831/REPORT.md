# Gross proof outer Round100 report

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** The frozen Gross root and gap-via-lift route remain **CONJECTURED**. The exact interval remains

\[
D^*_{\mathrm{Gross}}\in\{11,12\}.
\]

No outer or direct query was UNSAT, no repair gate opened, no universal `D*=11` ceiling was proved, and no explicit certified `D*=12` witness was found. Canonical, scheduler, review, and protocol files were not edited.

## Exact campaign

Iteration 172 was solved first from the commissioned unstarted frontier: 14,484 inherited order blocks, 304 selectors, 19,186 assertions, 413,646 variables, 1,406,245 clauses, and CNF `f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342`. It was SAT. Both complete unrestricted direct-360 sectors were then SAT and independently clause-checked and physically replayed. Only after both results settled were `r100-i172-Xerr` and `r100-i172-Zerr` appended atomically.

The same serial protocol completed iterations 173 through 183. Totals: **12 outer SAT**, **24 direct SAT**, **36 complete assignments**, **36 SAT proof streams summarized and deleted as non-certificates**, **24 accepted exact mechanisms**, and **12 atomic two-selector transitions**. Every schedule passed the frozen 864-edge audit; every direct mechanism had empty canonical and raw physical detector syndrome, equal nonzero canonical/physical logical action, and weight 1..10. No solver intervals overlapped.

The fresh unstarted frontier is iteration 184 with 328 selectors, selector-state `7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d`, state-file `3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b`, source-file `5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0`, semantic source `d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268`, 19,210 assertions, 415,793 variables, 1,416,404 clauses, and CNF `2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62`.

## New exact synthesis results

The exact six-distinct same-sector domain contains

\[
\binom{125}{6}+\binom{109}{6}=4,690,625,500+2,025,023,364=6,715,648,864.
\]

The MITM reduction enumerated 317,750 X triples and 209,934 Z triples and found no canonical-syndrome-zero six-set in either sector, hence no combined-syndrome-zero or eligible result. This is an exact reduced-domain theorem, not sampling; the proof of coverage and uniqueness is in `SYNTHESIS_PROOF.md`.

A stronger all-orders GF(2)-span query was UNSAT in both sectors after quotienting every existing full named mask. X: 12,949 variables, 43,827 clauses, CNF `c689883518b2abbf28aadbc9f13025d032f6f1e792e469b7a584517cfc4f48e5`. Z: 12,089 variables, 40,443 clauses, CNF `ce2113182676ab6063006a60d0fb4a6fc60447056ea2449b351eb6e9024c01b9`. Both DRATs were accepted, generated LRATs were accepted, corrupt/truncated DRAT and LRAT controls were rejected, and an independent direct-semantics Z3 encoding returned UNSAT in both sectors.

For CSS mixed-sector mechanisms of total named weight at most 10, an undetected nontrivial mixed action has an undetected nontrivial component of named weight at most 10. Thus mixed composition cannot evade the two component direct queries. This is a reduction theorem, not additional global closure.

## Scope and limitations

The order-six and span theorems bind the reviewed post-iteration-136 schedule and the 125 Xerr / 109 Zerr bases. The six-distinct theorem does not cover repeated indices, order at least seven, mixed sectors, other schedules/frontiers, or mechanisms outside those bases. The span theorem covers all GF(2) combinations of the reviewed bases but explicitly quotients existing masks and says nothing about arbitrary outside-span mechanisms. A positive direct result excludes only its source schedule after its selector is installed.

Round98 had three post-science model-capacity interruptions. They are disclosed, but none is inherited as a Round100 failure. Round100 failures and corrections are complete in `FAILURE_LEDGER.md`.
