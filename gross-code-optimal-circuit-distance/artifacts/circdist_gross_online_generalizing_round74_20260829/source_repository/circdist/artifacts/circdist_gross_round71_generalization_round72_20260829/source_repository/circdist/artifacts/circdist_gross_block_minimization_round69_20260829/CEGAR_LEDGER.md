# Continued unrestricted CEGAR ledger

## Installed constraint sets

Iteration 0 began with 6,200 sound blocks:

| source | count | load-bearing basis |
|---|---:|---|
| round-63 unary | 1,440 | 103,680 local-order replays and 7,200 deletion controls in sealed round 63 |
| round-62 raw blocks | 20 | raw schedule/witness replay in sealed round 62 |
| round-69 generalized | 4,740 | positive local-order mechanisms and rectangle inclusion |
| round-63 exploratory pair patterns | 0 | forbidden because retention gaps remain |

After each SAT candidate, its raw-replayed Xerr and Zerr exact blocks were added. Thus iteration `i` installed `6200+2i` blocks.

## Candidate ledger

| iter | installed | outer | candidate SHA-256 | Xerr | X atoms | Zerr | Z atoms | repair |
|---:|---:|---|---|---|---:|---|---:|---|
| 0 | 6,200 | SAT | `c8da557fa5f6470cb40fd0d0f48008a02add7b02f1e434b8d608fa64a69dd209` | SAT, w=10 | 80 | SAT, w=10 | 53 | gated off |
| 1 | 6,202 | SAT | `3de87c3ab911752591a51c9cb61c0ab3a472a2162470f8f248419881dde13d0d` | SAT, w=10 | 60 | SAT, w=10 | 64 | gated off |
| 2 | 6,204 | SAT | `05131a24589c1ed96fbdb9455ff4f0e1ba2d9a6bc8ca13f40f3a6f76eac12446` | SAT, w=10 | 57 | SAT, w=10 | 57 | gated off |
| 3 | 6,206 | SAT | `3a1248b695865680e354f54a02c2ce49cfb5d9574875df099c99bb6e49178083` | SAT, w=7 | 52 | SAT, w=10 | 64 | gated off |
| 4 | 6,208 | SAT | `c6fde2e505b528bc86deba59d9bad8a68a5e63a8c29cf469ba4bb35d62303dc4` | SAT, w=10 | 60 | SAT, w=10 | 25 | gated off |
| 5 | 6,210 | SAT | `81d6d668f8f1c0a56822402ddc7fff167df266babe220f448a31b87ee675fa6b` | SAT, w=10 | 63 | SAT, w=7 | 52 | gated off |

All six schedules pass:

- exact set of 864 named edges;
- nonnegative compressed integer layers;
- no same-ancilla or same-data conflict;
- all 648 MC equalities;
- global X/Z interleaving.

Every sector label in the table means the complete direct-360 formula was SAT, the full assignment satisfied every DIMACS clause, and the physical mechanism replay passed. The compact counts above do not replace the raw evidence under `cegar/iter*/`.

## Stop condition and live frontier

This round's explicit stop-loss was six complete dual-sector candidates, producing twelve new blocks. It was reached after iteration 5. There was no trend toward a direct-absence candidate and no root-closing outer result, so the calculation stopped before consuming an open-ended settlement round.

`cegar/dynamic_blocks.json` includes both iteration-5 blocks. The next exact outer problem is iteration 6 with 6,212 installed blocks. No iteration-6 candidate was generated, so there is no unqueried candidate in the package. `DISPATCHER_LICENSE.md` gives the continuation commands.
