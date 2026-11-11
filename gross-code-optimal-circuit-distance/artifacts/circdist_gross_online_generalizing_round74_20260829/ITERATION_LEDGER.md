# Iteration ledger

Every row is a complete online transaction. The next outer did not start until the row's exact blocks, generalized validation, deduplication, retained install, and after-state snapshots completed. `X/Z weight` is elementary fault count; support weight is not the direct bound.

| iter | blocks before | outer | X/Z weight | direct X/Z | raw terms | dup-new | dom-new | retained | literal pair tuples | symbolic multi tuples | blocks after |
|---:|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 42 | 6850 | SAT | 10 / 9 | SAT / SAT | 16 | 2 | 1 | 13 | 100,224 | 2,985,984 | 6865 |
| 43 | 6865 | SAT | 10 / 10 | SAT / SAT | 14 | 2 | 2 | 10 | 78,624 | 0 | 6877 |
| 44 | 6877 | SAT | 10 / 10 | SAT / SAT | 14 | 2 | 2 | 10 | 72,000 | 0 | 6889 |
| 45 | 6889 | SAT | 10 / 7 | SAT / SAT | 26 | 2 | 2 | 22 | 196,704 | 0 | 6913 |
| 46 | 6913 | SAT | 10 / 10 | SAT / SAT | 34 | 3 | 2 | 29 | 288,576 | 0 | 6944 |
| 47 | 6944 | SAT | 10 / 10 | SAT / SAT | 8 | 3 | 2 | 3 | 24,768 | 0 | 6949 |
| 48 | 6949 | SAT | 10 / 10 | SAT / SAT | 8 | 3 | 2 | 3 | 19,008 | 0 | 6954 |
| 49 | 6954 | SAT | 10 / 10 | SAT / SAT | 10 | 3 | 2 | 5 | 40,896 | 0 | 6961 |
| 50 | 6961 | SAT | 10 / 10 | SAT / SAT | 12 | 3 | 2 | 7 | 50,472 | 0 | 6970 |
| 51 | 6970 | SAT | 10 / 9 | SAT / SAT | 18 | 3 | 2 | 13 | 114,336 | 0 | 6985 |
| 52 | 6985 | SAT | 10 / 10 | SAT / SAT | 12 | 2 | 2 | 8 | 57,600 | 0 | 6995 |
| 53 | 6995 | SAT | 10 / 10 | SAT / SAT | 16 | 3 | 2 | 11 | 93,888 | 0 | 7008 |

Totals: 12 outer SAT schedules, 24 unrestricted direct SAT assignments, 24 candidate-exact blocks, 188 raw generalized candidates, 31 duplicate-new, 23 dominated-new, zero duplicate-old, zero dominated-old, and 134 retained terms. The retained validation covers 1,137,096 literal pair tuples and 2,985,984 multi tuples through the symbolic universal proof described in `MATH_DERIVATION.md`.

There was no direct UNSAT, UNKNOWN, timeout, accepted absence, repair entry, or branch closure. Iteration 54 is frozen and unstarted.
