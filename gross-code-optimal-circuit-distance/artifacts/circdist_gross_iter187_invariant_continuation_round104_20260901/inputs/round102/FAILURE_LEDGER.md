# Round102 failure and correction ledger

No failed attempt below is used as positive evidence.  Corrected attempts have
new process records and outputs; superseded artifacts remain labeled so a
reviewer can reconstruct the chronology.

| ID | phase | failure or correction | disposition |
|---|---|---|---|
| F001 | iteration-184 SAT replay | `outer_iter184_verify_sat` used the base Python, which could not import `z3`; child exited 1. | Retained.  Reran with the explicitly bound vendored Python path; the complete SAT replay passed. |
| F002 | environment binding | First `bind_vendored_z3` command had malformed shell quoting and raised `SyntaxError`; child exited 1. | Retained.  Corrected quoting, bound Z3 5.1.0, and ran an import/solve smoke test. |
| F003 | exploratory closure plan | First block-closure script asserted that all 14,484 inherited records had unique semantics.  Seven historical records are semantic duplicates. | Retained.  Identity now uses full normalized tuples; the corrected plan reports 14,477 input semantics and all multiplicities. |
| F004 | exploratory quotient checker | First `check_iter186_orbit_quotient` invocation omitted the package `PYTHONPATH`; child exited 1. | Retained.  Reran in the bound environment and passed. |
| F005 | exploratory SAT-orbit control | First control invocation pointed to a compressed file where raw quotient bits were required; child exited 1. | Retained.  Corrected path and reran all positive and negative model controls. |
| F006 | proof negative control | Removing only the last DRAT line was accepted: the retained prefix already contained a complete refutation, so that mutation was not a valid truncation control. | Retained as a failed control design.  The corrected half-byte truncation was rejected; corrupt DRAT/LRAT and truncated LRAT were also rejected. |
| F007 | scientific scope | The first 330-selector lex quotient appended leaders to a registry that was not closed under translation.  SAT point evidence was valid, but global equisatisfiability had not been proved. | The global claim was retracted immediately.  All 14,484 block and 474 selector parent orbits were closed exactly, invariance was independently checked, and a new quotient was compiled and solved. |
| F008 | full-closure builder | First build coerced historical `source_iteration: "pre-124"` to an integer and exited 1. | Retained.  Corrected the builder to preserve historical provenance values verbatim; complete rebuild and independent closure check passed. |
| F009 | corrected candidate Xerr direct query | Default-profile proof-mode CaDiCaL reached its 890-second internal bound and returned 0/UNKNOWN.  The 6,101,477,668-byte output is an incomplete trace, not an absence certificate. | Solver and wrapper were reaped.  Trace retained losslessly and labeled UNKNOWN.  A documented `--unsat`-profile retry on the unchanged CNF returned SAT and its complete assignment and physical effects were checked. |
| F010 | corrected candidate Zerr direct query | Default-profile proof-mode CaDiCaL reached its 890-second internal bound and returned 0/UNKNOWN.  The 6,379,134,538-byte output is an incomplete trace, not an absence certificate. | Solver and wrapper were reaped.  Trace retained losslessly and labeled UNKNOWN.  A later documented retry on the unchanged CNF returned SAT; its interval did not overlap X and its complete assignment and physical effects were checked. |
| F011 | fresh frontier compilation | The first iteration-187 frontier writer used a descriptive schema without the compiler-required `-finite-source-v1` suffix; compilation rejected it before writing a formula. | Retained as an exited/reaped rc=1 process.  The package-local writer was corrected, iteration 187 was regenerated, and its base CNF and lex quotient both passed independent reconstruction.  The frontier remains unstarted. |
| F012 | preseal replay | The first replay reached the last child after twelve successful checks, then the proof-control wrapper requested nonexistent `php6_5.fresh.drat` instead of retained `php6_5.drat`; the wrapper exited 1. | Retained as an exited/reaped failure.  The package-local path was corrected; no scientific evidence changed, and the complete replay was rerun from the beginning. |
| F013 | final cleanup audit | The first cleanup audit correctly found an empty package-local `scratch/` directory left by bootstrap; the checker exited 1. | The empty directory was removed with a separately recorded and reaped child.  The corrected cleanup audit found no package or system Round-102 temporary survivor and no raw corrected solver stream. |

## Non-failures that remain non-certificates

SAT-side CaDiCaL proof-output streams are retained because proof production was
enabled from launch, but they are not UNSAT certificates.  An UNKNOWN prefix,
even if it contains billions of derived/deleted clauses, proves no absence.
The exploratory non-invariant quotient's SAT schedule and its two physically
replayed mechanisms are legal point evidence only.  Fixed-schedule basis/span
results inherited from Round100 retain their reviewed scope and are not
globalized here.

## Process-record limitation disclosed

Two initial bootstrap records used a synchronous `subprocess.run` wrapper and
therefore have `child_pid: null`; their commands, return codes, stdout, stderr,
and wall intervals are retained.  All subsequent scientific compilers,
solvers, replayers, and checkers use PID-bearing `run_logged.py` records.  Shell
inspection commands issued by the orchestration host are not detached compute
and are not claimed as package-owned scientific children.
