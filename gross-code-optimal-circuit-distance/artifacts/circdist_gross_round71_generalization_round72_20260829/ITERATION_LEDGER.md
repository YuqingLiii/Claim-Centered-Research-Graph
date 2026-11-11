# Exact CEGAR iteration ledger

| iter | candidate SHA-256 | blocks before | X w/atoms/seconds | Z w/atoms/seconds | result |
|---:|---|---:|---:|---:|---|
| 30 | `23c6b85b2c33e886d430ba59ea064b7b137f1b90d7bf8633ff46fd893131a68e` | 6826 | 10/47/18.144 | 10/70/0.374 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 31 | `7cd759cb93fd3f1b0a1a2a5a0487f432c12f9cf00b8263862abba6e83193f6cf` | 6828 | 10/76/31.901 | 10/41/0.503 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 32 | `79cb7a43363722b5fe7e3c977dfac59396b4bc17cddc6971e9f56b890e3bc28e` | 6830 | 10/66/68.906 | 10/76/5.243 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 33 | `2f52a7d44c821db6229f907fb6ec03d3f96f1afb5117f0d8cab7f85333f5ce54` | 6832 | 10/16/64.123 | 10/67/21.969 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 34 | `9074090085e287580a7e3430b3b50452cea1b24e9187b45a25e524d3655bf7fb` | 6834 | 10/16/11.862 | 10/72/0.264 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 35 | `2ef491a93653e7e0d5024a67dfaee269c676828e933233109f1fd77c47190603` | 6836 | 10/41/21.525 | 10/41/28.614 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 36 | `83e4904227d466dfeab6e957023711fe03bfdbc49f2b309289b006fbbbd63790` | 6838 | 10/16/16.996 | 9/64/4.988 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 37 | `3b6513cc8d7ae6080f19993756de3d8a68a8ec62d0fd47f1cd3797e684a0c6bc` | 6840 | 10/34/16.399 | 10/66/0.384 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 38 | `6dd6d535c64160a6f84ddb91d7b2f3f8aed67451e220f8949a7edca8c369f141` | 6842 | 10/50/23.226 | 10/69/6.242 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 39 | `fce5dd538b0954f47b3dda16a472ff10391e696476f4e981ea349090056e2a6f` | 6844 | 10/67/0.330 | 10/25/15.613 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 40 | `c799b9399c8bc419f7d92556f3932168dfa13ab38d6c68e156a2feb9369202fb` | 6846 | 10/57/19.925 | 10/50/0.384 | outer SAT; X/Z SAT; clause+raw replay PASS |
| 41 | `28c123cce2a7579a3145b9224efb54ea4cff54745381f6290e55f772c3a1507e` | 6848 | 10/32/103.007 | 10/74/6.085 | outer SAT; X/Z SAT; clause+raw replay PASS |

All 72 material candidate processes appear individually in `PROCESS_LEDGER.json`. No query timed out or returned UNKNOWN/UNSAT. No DRAT/LRAT object is therefore Gross absence evidence. Iteration 41 Xerr was the slowest direct query at 103.007 seconds under a 600-second solver and 660-second hard limit.

Exact next state: iteration 42, 84 dynamic exact blocks, 6,850 total blocks.
