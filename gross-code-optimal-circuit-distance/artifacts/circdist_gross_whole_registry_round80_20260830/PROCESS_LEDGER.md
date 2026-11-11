# Process ledger

Accepted synthesis wrappers: 2; accepted CEGAR child processes: 96; iteration driver wrappers: 12; proof-control runs: 7.

Accepted process wall total: 4731.729s; maximum sampled RSS: 3,261,661,184 bytes. No accepted process timed out or received SIGTERM/SIGKILL.

## FIX-2 development incidents

- **whole_v1** — FAILED_NO_STATE_MUTATION; wall=7.563s, maxRSS=1,953,562,624 B, exit=1. missing non-raw catalog-mask handling; assertion before mutation
- **whole_v2** — FAILED_NO_STATE_MUTATION; wall=7.591s, maxRSS=1,968,340,992 B, exit=1. Python 3.9 int.bit_count incompatibility before mutation
- **whole_v3** — EXTERNALLY_SIGTERM_NO_STATE_MUTATION; wall=238.798s, maxRSS=1,968,406,528 B, exit=-15. exact quadratic column scan was too slow; manual SIGTERM; replaced by bitset scan
- **whole_v4** — TEMPORARY_SCHEMA_ONLY_STATE_ROLLED_BACK; wall=9.657s, maxRSS=2,041,282,560 B, exit=0. synergy required at seed caused zero retained; schema-only semantic mutation rejected and rolled back exactly
- **whole_v5** — FAILED_NO_STATE_MUTATION; wall=199.932s, maxRSS=1,986,281,472 B, exit=1. complete provisional classification reached, then Python 3.9 replay bit_count incompatibility
- **whole_v6** — ACCEPTED_PASS; wall=398.521s, maxRSS=1,986,330,624 B, exit=0. bitset dominance, corrected synergy timing and portable popcount; 24 strict expansions
- **outer_iter90_v1** — FAILED_CANDIDATE_DISCARDED_NO_STATE_MUTATION; wall=28.604s, maxRSS=662,192,128 B, exit=1. outer SAT built, independent replay correctly rejected missing plain round62 source; candidate discarded and fresh iter90 restarted
- **verifier_v1_noop** — REJECTED_HARNESS_NO_STATE_MUTATION; wall=0.040s, maxRSS=26,542,080 B, exit=0. main invocation missing after source edit; zero-byte output rejected despite shell exit 0
- **verifier_v2_bad_live_path** — REJECTED_BINDING_METADATA_NO_STATE_MUTATION; wall=0.160s, maxRSS=115,539,968 B, exit=1. SOURCE_BINDINGS named nonexistent live Gross node path; corrected to canonical proof-dag node path

All failed/interrupted computations occurred in disposable staging. Tentative outputs were either never installed or explicitly rolled back. The accepted CEGAR chain contains only complete atomic commits.
