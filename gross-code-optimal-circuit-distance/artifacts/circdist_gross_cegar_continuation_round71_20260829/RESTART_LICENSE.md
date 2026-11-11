# Exact restart license

The only licensed continuation boundary is:

```text
next outer iteration: 30
round-63 unary blocks: 1,440
round-62 blocks: 20
round-69 generalized blocks: 4,740
dynamic blocks: 60 = 12 inherited + 48 round-71
next total: 6,260
exploratory round-63 pair clauses: 0
state: cegar/dynamic_blocks.json
```

No iteration-30 candidate has been built. Copy the state outside this sealed directory and run the local frozen source in a clean environment:

```bash
PKG=/absolute/path/to/circdist_gross_cegar_continuation_round71_20260829
OUT=/tmp/circdist-r71-iter30
STATE=/tmp/circdist-r71-dynamic-iter30.json
cp "$PKG/cegar/dynamic_blocks.json" "$STATE"
PYTHONDONTWRITEBYTECODE=1 "$PYTHON" "$PKG/src/build_cegar_candidate.py" \
  --iteration 30 --output "$OUT" --dynamic-blocks "$STATE" \
  --z3-timeout-ms 120000
```

Apply an external foreground 180-second process-group hard limit. Continue only for a verified outer SAT candidate. Run both unrestricted complete direct formulas even if the first is SAT. Give CaDiCaL an internal 600-second and external 660-second limit, preserve exact argv/exit/wall/timeout, then use `src/replay_direct_candidate.py`. Append blocks with `src/append_dynamic_blocks.py` only after complete assignment/clause/raw replay passes.

For an UNSAT sector, rerun proof-producing, retain complete DIMACS and DRAT, translate/check LRAT, and run valid plus corrupted/truncated controls. Missing proof, checker rejection, UNKNOWN, or timeout is not absence. Append a block only from a SAT sector. Enter repair only after both sectors of one candidate have accepted absence proofs. An outer UNSAT needs a proof-producing encoding and independent checker before exhaustion or `D*=11` may be claimed. Do not mutate this package.
