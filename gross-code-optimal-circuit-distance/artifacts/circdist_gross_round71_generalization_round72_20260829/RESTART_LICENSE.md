# Exact restart license

The sole licensed boundary is:

```text
next outer iteration: 42
round-63 unary blocks: 1,440
round-62 blocks: 20
reviewed round-69 generalized blocks: 4,740
round-72 generalized blocks: 566
dynamic exact blocks: 84 = 60 inherited + 24 round-72
next total: 6,850
exploratory round-63 pair clauses: 0
state: cegar/dynamic_blocks.json
```

Copy the dynamic state outside the sealed package. Run `src/build_cegar_candidate.py --iteration 42` in a fresh process with a 120,000 ms Z3 limit and 180-second process-group hard limit. Continue only after independent outer replay. Generate both direct sectors unconditionally, give CaDiCaL a 600-second internal and 660-second hard limit, and append exact blocks only after complete clause and raw physical replay.

For a direct UNSAT, use the proof path described in `DIRECT360_AND_PROOF_POLICY.md`. For outer UNSAT, stop without an exhaustion claim unless an equivalent proof-producing encoding and independent accepted proof are supplied. Do not mutate this sealed package.
