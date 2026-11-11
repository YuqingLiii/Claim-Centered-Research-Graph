# Round112 failure ledger

All items below are harness or invocation corrections. None produced a scientific SAT/UNSAT/UNKNOWN discrepancy.

- **F112-001.** The copied process runner retained read-only mode; its first attempted update failed before science. Corrected only the scratch copy's mode.
- **F112-002.** The first reconstruction comparison required metadata byte identity and rejected nondeterministic `compile_seconds`; load-bearing files were exact. The retry ignored only measured runtime fields and passed.
- **F112-003.** The first cumulative direct-CNF builder assumed the DIMACS header was line 1; the formula has three leading comments. It failed before solver launch. The retry located the unique `p cnf` header and passed.
- **F112-004.** A zsh variable containing eight `--audit` pairs was passed as one argument. `argparse` returned 2 before frontier output. The explicit-argument retry passed.
- **F112-005.** The first explicit retry omitted the wrapper's required `--timeout`; wrapper `argparse` returned 2 before any child or frontier output. The corrected invocation passed.
- **F112-006.** The first iter192 quotient checker clean environment omitted vendored `PYTHONPATH`; Python raised `ModuleNotFoundError: z3` before a verdict. The same command with the sealed vendored path passed.
- **F112-007.** The first metadata preparation tried to overwrite a read-only file cloned from the sealed source tree. It failed before package metadata generation; the scratch destination mode was corrected.
- **F112-008.** The first mode correction handled an existing file but not the inherited read-only parent directory. The retry failed before metadata generation; the scratch-only directory was made writable and the next retry passed.
- **F112-009.** The first preseal replay regenerated identical iter192 source and state bytes but passed absolute audit paths, so only provenance path strings changed in `orbit_audit.json`. It stopped before later checks. The driver was corrected to pass package-relative paths; the full clean-environment retry passed.
- **F112-010.** A preseal static assertion initially treated the intentionally retained DRAT control fixtures as forbidden raw SAT streams. The check and seal scope were corrected to forbid raw `.drat` only under `solver/` and `batch/`; the control fixtures remain required.
