# Iteration ledger

Every row is a fully closed dual-sector candidate. `SAT / w / a / s` means a complete unrestricted direct-360 formula was SAT, the retained raw mechanism has fault count `w`, its exact order antecedent has `a` atoms, and the foreground solver wall time was `s`. Both sectors were run before state mutation.

| iter | blocks before | outer solve s | schedule SHA prefix | Xerr status / weight / atoms / solver | Zerr status / weight / atoms / solver | dynamic after |
|---:|---:|---:|---|---|---|---:|
| 6 | 6212 | 1.561436 | `a3ece9e83274` | SAT / 10 / 60 / 6.230s | SAT / 10 / 63 / 1.048s | 14 |
| 7 | 6214 | 1.589435 | `d80a5e38e088` | SAT / 9 / 62 / 5.621s | SAT / 10 / 76 / 4.807s | 16 |
| 8 | 6216 | 1.560153 | `bf63a98fb894` | SAT / 10 / 25 / 19.560s | SAT / 10 / 34 / 1.226s | 18 |
| 9 | 6218 | 1.564680 | `9f82f85ca258` | SAT / 10 / 57 / 1.222s | SAT / 10 / 35 / 0.382s | 20 |
| 10 | 6220 | 1.572012 | `1d68123ed413` | SAT / 10 / 16 / 10.254s | SAT / 10 / 66 / 0.270s | 22 |
| 11 | 6222 | 1.587800 | `ba17537b08e0` | SAT / 10 / 46 / 38.285s | SAT / 10 / 41 / 4.079s | 24 |
| 12 | 6224 | 1.564014 | `dd8fd6e2c71f` | SAT / 10 / 76 / 6.109s | SAT / 10 / 48 / 0.382s | 26 |
| 13 | 6226 | 1.569643 | `3d839f4eb410` | SAT / 10 / 72 / 0.390s | SAT / 10 / 53 / 4.566s | 28 |
| 14 | 6228 | 1.568905 | `4efa33f3edc3` | SAT / 9 / 72 / 30.632s | SAT / 9 / 40 / 0.323s | 30 |
| 15 | 6230 | 2.352556 | `acf5002ba902` | SAT / 10 / 25 / 5.952s | SAT / 10 / 76 / 0.862s | 32 |
| 16 | 6232 | 2.085667 | `b850a77d1c85` | SAT / 10 / 53 / 6.369s | SAT / 9 / 52 / 5.167s | 34 |
| 17 | 6234 | 1.659442 | `01a1335b2c30` | SAT / 10 / 34 / 17.999s | SAT / 10 / 61 / 0.330s | 36 |
| 18 | 6236 | 1.584655 | `0554da646bd7` | SAT / 10 / 16 / 2.651s | SAT / 9 / 42 / 0.330s | 38 |
| 19 | 6238 | 1.552923 | `21359c37e405` | SAT / 10 / 25 / 19.201s | SAT / 10 / 66 / 0.330s | 40 |
| 20 | 6240 | 2.068738 | `03c00ae93c5e` | SAT / 10 / 64 / 1.406s | SAT / 10 / 16 / 3.984s | 42 |
| 21 | 6242 | 1.566043 | `bcb48f242bcd` | SAT / 10 / 70 / 23.519s | SAT / 10 / 16 / 5.166s | 44 |
| 22 | 6244 | 1.638892 | `24fff64a28b7` | SAT / 9 / 55 / 5.429s | SAT / 10 / 72 / 0.383s | 46 |
| 23 | 6246 | 2.053768 | `df92bde4cd78` | SAT / 10 / 51 / 23.474s | SAT / 10 / 48 / 4.244s | 48 |
| 24 | 6248 | 1.675329 | `7e3bafebadb5` | SAT / 10 / 35 / 32.069s | SAT / 10 / 16 / 0.083s | 50 |
| 25 | 6250 | 1.599703 | `9a125c1c3cda` | SAT / 10 / 66 / 18.827s | SAT / 10 / 68 / 5.289s | 52 |
| 26 | 6252 | 1.563932 | `cbed3bd2fe40` | SAT / 9 / 52 / 5.601s | SAT / 10 / 68 / 4.800s | 54 |
| 27 | 6254 | 1.553120 | `51e324ec92e0` | SAT / 9 / 64 / 32.466s | SAT / 10 / 48 / 3.991s | 56 |
| 28 | 6256 | 1.593964 | `90dcae848dcd` | SAT / 10 / 44 / 22.696s | SAT / 10 / 76 / 3.219s | 58 |
| 29 | 6258 | 1.927507 | `f9091946b336` | SAT / 10 / 41 / 47.345s | SAT / 10 / 54 / 4.223s | 60 |

All 24 outer candidates passed the separate `outer_independent_replay.json`: 864 named edges, 72+72 weight-six checks, 648 MC relations, complete edge set, no qubit/time conflict, idle compression, global X/Z interleaving, all inherited blocks false on the candidate, exact SMT-LIB byte reconstruction, and SAT after fixing every serialized edge variable to the recorded schedule.

All 48 direct results have complete assignments for every DIMACS variable. Every clause was evaluated, then the selected canonical columns and actual physical hook suffixes were replayed. Every resulting physical support had zero opposite-check syndrome and a nonzero logical quotient.
