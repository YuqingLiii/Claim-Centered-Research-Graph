# Gross round 72: strict generalization plus exact CEGAR

## Result

`MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`

This sealed proposer package does two load-bearing things.

1. It independently reconstructs all 48 exact mechanisms added in round 71 from the sealed unrestricted DIMACS formulas, complete solver assignments, schedules, and raw witnesses. It enumerates all 720 local orders in every one of 113 participating check catalogs, constructs 607 conservative factorized pair relations, and constructs an exact selected-mechanism GF(2) relation for each of the 48 mechanisms. After semantic deduplication and dominance against the reviewed 4,740-term round-69 library, 566 new generalized terms remain. Every source mechanism is covered by at least one retained term, while its original candidate-exact block remains preserved.
2. Starting from the licensed iteration-30 state (6,260 inherited blocks), it installs those 566 sound terms and runs 12 fresh-process outer candidates, iterations 30 through 41. Every outer query is SAT. Both unrestricted direct-360 sectors are SAT for every candidate, and all 24 complete assignments pass every DIMACS clause and raw physical replay. They add 24 exact blocks. There is no accepted absence proof, repair entry, branch closure, or outer exhaustion proof.

The exact restart boundary is iteration 42 with 6,850 blocks: 1,440 unary + 20 round-62 + 4,740 reviewed round-69 generalized + 566 round-72 generalized + 84 dynamic exact. No round-63 exploratory pair clause is installed.

## Claim boundary

The 566-term library is conservative and positive. A zero entry in a pair truth table, a failed positive completion search, an atom-deletion countertuple, or any prior negative observation is not physical absence. The package does not claim a complete classification of all weight-at-most-10 failures. `ROOT-11-CANDIDATE-PROOF` and `ROOT-12-CANDIDATE` are not licensed.

## Verification

Create a fresh Python environment from `requirements.txt`, then run:

```bash
PYTHONDONTWRITEBYTECODE=1 python verify.py --quick
PYTHONDONTWRITEBYTECODE=1 python verify.py --full
```

`--full` is self-contained. It re-runs the complete 48-mechanism classification from the nested sealed round-69/71 source packages, compares every output byte, reconstructs all 12 outer formulas in fresh child processes, reconstructs all 24 direct formulas byte-for-byte, and replays every complete assignment and raw mechanism. `--repo-root` additionally compares frozen bindings to a live checkout.

The package is proposer evidence and still requires a fresh independent review before any canonical link or claim change.
