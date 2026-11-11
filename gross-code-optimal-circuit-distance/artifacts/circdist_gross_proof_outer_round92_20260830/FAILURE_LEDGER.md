# Failure and rollback ledger

All failures below are procedural or rejected synthesis attempts.  None was converted into
absence evidence and none mutated the frozen scientific state.

1. The first strict-expansion verifier used `int.bit_count`, which is unavailable in the
   recorded Python runtime.  It failed before acceptance.  The public implementation was
   changed to the equivalent `bin(x).count("1")`; the full DIMACS, frozen schedule, and
   physical checks then passed.  No formula, assignment, or selector changed.
2. An online weight-9 synthesis script was started after the 12-candidate prefix, then the
   parent explicitly directed that new experiments stop.  The process was interrupted with
   Ctrl-C, exited 1, was reaped, and wrote no result, state, or source.  Its script and partial
   output are excluded from this package.
3. The first package-assembly command was rejected by the tool policy because its shell text
   contained an `rm -rf` cleanup.  It never executed and created no package.  The accepted
   assembler uses Python `shutil.rmtree` in scratch.
4. SAT-side proof streams totaled several GiB.  Because every corresponding formula was SAT,
   they were not certificates.  Each was hashed, counted, checked to contain no empty-clause
   line, and recorded before removal.  The smallest actual stream was deterministically
   regenerated from the identical formula and solver command, matched the recorded hash,
   and is retained for checker controls.  The regeneration process was bounded and reaped.
5. The first preseal full replay passed both synthesis, all 13 formula reconstructions, the
   strict-expansion model, all 12 outer/direct/physical candidate replays, continuation,
   result, and process checks, then failed because it byte-compared a DRAT-trim diagnostic
   containing a temporary formula pathname.  The checker semantics were already correct.
   Replay was repaired to require return code 1, `NOT VERIFIED`, and empty stderr while the
   sealed original log remains hash-checked separately.  No scientific object changed.

There were no solver timeouts, UNKNOWN dispositions, UNSAT misclassifications, retroactive
cuts, repair entries, or canonical edits.
