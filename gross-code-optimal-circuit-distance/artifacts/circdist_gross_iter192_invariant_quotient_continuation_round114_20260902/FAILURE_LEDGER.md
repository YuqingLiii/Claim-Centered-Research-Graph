# Round114 failure ledger

Every item is retained and classified. None produced a scientific SAT, UNSAT, or UNKNOWN discrepancy.

- **F114-001.** The copied `source/` directory inherited mode 0555, so the first attempt to create the reconstruction verifier failed with permission denied before output. Only the scratch directory mode was changed; source bytes/metadata in the sealed Round112 package were untouched.
- **F114-002.** The first outer-model replay omitted the copied z3 site-packages. Python raised `ModuleNotFoundError: z3` before a verdict. The full replay with the explicit bundled `PYTHONPATH` passed.
- **F114-003.** An inspection grep included nonexistent `source/build_invariant_quotient_round110.py`; grep returned 2 after emitting matches from the existing files. No scientific program ran; the actual quotient tool name was then read.
- **F114-004.** A read-only schema probe used the wrong scratch source path and raised `FileNotFoundError`. The corrected path was inspected; no state changed.
- **F114-005.** The first CSS audit used `int.bit_count`, unavailable in the system Python 3.9, and stopped at that compatibility call before registry conclusions. It was replaced by `bin(x).count('1')`; the entire retained audit then passed.
- **F114-006.** The first iter193 quotient-check invocation passed `vendor/` instead of `vendor/round80` and stopped at `ModuleNotFoundError: model`. No formula verdict was accepted.
- **F114-007.** The next quotient-check invocation bound `vendor/round80` but omitted z3 site-packages, stopping at `ModuleNotFoundError: z3`. The entire third invocation with both reviewed bindings passed.
- **F114-008.** A repository-status wrapper was invoked from the repository with a scratch-relative runner path and failed before launching git. The corrected absolute-target invocation from scratch passed.
- **F114-009.** The first package-finalizer invocation stopped before sealing or installation when `shutil.copy2` attempted to overwrite a read-only staged source file and raised `PermissionError`. The retained scratch-only finalizer was made idempotent by granting owner-write permission only to an existing destination immediately before ordinary-copy replacement; every replacement also checks distinct source/destination inode identities and destination link count one. Source metadata was not changed, and the complete finalization was rerun.
- **F114-010.** A report-inspection command used the nonexistent absolute path `/usr/bin/rg` and exited 127 before inspecting files. The bundled `rg` path was discovered and the same read-only inspection succeeded; no scientific or package state was changed.
- **F114-011.** The first preinstall evidence-closure wrapper invocation again used the scratch-relative process-runner path from the repository working directory, so Python exited 2 before launching the checker. The corrected invocation used the absolute scratch runner path; the retained preinstall baseline then passed with exit 0.
