# Gross whole-registry exact proposer, Round 80

This is a self-contained proposer package. It binds the freshly reviewed, unstarted iteration-90 state and adds a broader exact multi-mechanism whole-registry construction before running twelve strict-serial CEGAR candidates (iterations 90 through 101).

## Verdict

**MATERIAL-CHECKED-PROGRESS-NOT-CLOSED.** No load-bearing branch closed; no candidate-specific or outer UNSAT certificate was accepted; `D*_Gross` remains in `{11,12}` and did not change. Fresh independent review is required. No canonical node, scheduler, protocol, review, or generated view was edited by this proposer.

## Exact transition

- Licensed start: G=10,595, D=180, registry/raw=96, installed blocks=12,235, next iteration 90.
- Pre-outer whole-registry synthesis: +24 strict installed-union expansions, G=10,619, first outer total=12,259.
- CEGAR: 12 outer SAT schedules, 24 complete direct-360 SAT assignments, +94 online terms, +2107 cross-registry terms, +24 candidate-exact blocks.
- Frozen restart: G=12,820, D=204, registry/raw=120, installed blocks=14,484, fresh unstarted iteration 102.

Run `python verify.py --quick --repo-root /path/to/Claim-Centered-Research-Graph` for structure, hashes, ledgers, controls, and live bindings. Run `python verify.py --full --repo-root ...` for fresh outer formula reconstruction, complete direct formula/assignment replay, every raw mechanism replay, all retained literal/factorized term domains, and independent whole-registry selector replay.
