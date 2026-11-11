# Failure ledger

All failures were foreground, bounded, and reaped. Neither failure mutated selector state or produced accepted scientific evidence.

1. **Bootstrap command rejected before process creation.** An initial command combined scratch removal with setup. The tool safety layer rejected it, with no filesystem effect and no OS child. Setup was retried only after asserting the target absent. This is recorded in `logs/bootstrap-processes.tsv`.
2. **Order-4 attempt 1, rc=1, 2.904381 s.** The script incorrectly required inherited `selected_names` to be lexically sorted. Reviewed selectors preserve direct-column order; GF(2) set algebra requires uniqueness, not lexical order. The assertion was corrected. See `logs/process/order4_exact_synthesis.json` and its stderr.
3. **Order-4 repair 1, rc=1, 3.056889 s.** Python 3.9 lacks `int.bit_count`. It was replaced by the frozen model's `popcount`, preserving exact semantics. See `logs/process/order4_exact_synthesis_repair1.json`.
4. **Order-4 repair 2, rc=0, 60.963179 s wrapper / 60.838360 s census.** The full 15,254,626-element run passed. See `logs/process/order4_exact_synthesis_repair2.json`.
5. **Transient model-capacity interruption, orchestration only.** The proposing agent turn was interrupted after the foreground preseal replay had already exited rc=0 and written its complete 116-child record. No OS science process remained live, no file was rolled back or mutated by the interruption, and work resumed from the retained disk state without repeating candidate solving or the order-4 census. This has no mathematical disposition.

No timeout, unknown solver disposition, detached process, repair branch, proof-checker failure, or weight<=8 event occurred.
