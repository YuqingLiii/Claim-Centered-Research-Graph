# CIRCDIST Gross exact outer/direct continuation — Round98 proposer report

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** All twelve exact outer queries at iterations 160--171 are SAT. Both complete unrestricted direct-360 sectors are SAT for every candidate. No actual Gross UNSAT occurred, repair was never entered, and no distance-12 witness or universal distance-11 ceiling was proved. `CIRCDIST.gross` and `gap-via-lift` remain **CONJECTURED** and the exact residual remains `D*_Gross in {11,12}`.

## Exact campaign

The reviewed iteration-160 formula was reconstructed exactly: 19,162 assertions, 411,526 variables and 1,396,722 clauses, CNF `aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59`. Each SAT model satisfies every DIMACS clause and decodes to a legal frozen schedule. Every direct assignment satisfies its complete unrestricted formula; canonical and physical syndrome are zero, logical action is nonzero and agrees, and the next two selectors are appended atomically.

| iteration | source selectors | outer | X named/canonical/physical | Z named/canonical/physical | next selectors |
|---:|---:|---|---:|---:|---:|
| 160 | 280 | SAT | 10/12/12 | 10/14/14 | 282 |
| 161 | 282 | SAT | 9/14/22 | 10/18/32 | 284 |
| 162 | 284 | SAT | 10/12/12 | 10/12/14 | 286 |
| 163 | 286 | SAT | 10/12/14 | 10/16/24 | 288 |
| 164 | 288 | SAT | 10/12/14 | 10/12/16 | 290 |
| 165 | 290 | SAT | 10/12/12 | 10/12/16 | 292 |
| 166 | 292 | SAT | 10/16/22 | 10/12/14 | 294 |
| 167 | 294 | SAT | 10/12/14 | 10/12/16 | 296 |
| 168 | 296 | SAT | 10/14/18 | 10/14/18 | 298 |
| 169 | 298 | SAT | 10/14/16 | 10/16/18 | 300 |
| 170 | 300 | SAT | 10/16/22 | 10/12/16 | 302 |
| 171 | 302 | SAT | 10/16/20 | 10/12/12 | 304 |

## Exact same-sector order-5 theorem

The C++ streaming enumerator visits the unique strict representation `a<b<c<d<e` for every five-distinct-selector tuple. It enumerates `C(125,5)=234,531,275` X tuples and `C(109,5)=116,828,271` Z tuples, total **351,359,546**, with complete histograms summing to those closed forms. Full six-word equality, not hash identity, decides result equality. The independent Python validator reconstructs all 38,382 X and 1,771 Z unique named-weight-1..10 results from their five witnesses and replays their canonical and physical effects. Neither sector has a syndrome-zero result; therefore there is no source-schedule-valid same-sector order-5 EFSSC in this exact domain and zero selectors are retained. This theorem excludes neither mixed sectors, repeated indices, order six or higher, other schedules/frontiers, nor arbitrary mechanisms.

## Fresh frontier and scope

Iteration 172 is compiled and encoding-checked but deliberately unstarted/unsolved: 304 selectors, selector state `a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1`, 19,186 assertions, 413,646 variables, 1,406,245 clauses, CNF `f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342`. No solver/model/proof disposition is inherited.

## Failures and recovery

The retained failures are: a C++ mixed-`auto` declaration compile error corrected before use; an X input-header `magic` abort corrected by regenerating the exact input; a wrong vendor-directory audit invocation corrected before the accepted audit; three post-science GPT model-capacity interruptions during packaging; and one dispatcher attempt to check protected bindings before `INPUT_BINDINGS.json` existed. Every incident is non-scientific, disclosed, and excluded from positive evidence. Accepted science is backed by successful corrected runs and independent audits.

## Reproducibility

`replay.sh` verifies both manifests, reconstructs all thirteen formulas, regenerates all twelve direct formulas and all twelve atomic transitions, reruns the independent assignment/physical audit and exact order-5 validator, and checks result, process, proof controls and protected bindings. Canonical state is read-only. See `SYNTHESIS_PROOF.md`, `FAILURE_LEDGER.md`, `PROCESS_LEDGER.json`, `RESULT.json` and `FIX-2.md`.
