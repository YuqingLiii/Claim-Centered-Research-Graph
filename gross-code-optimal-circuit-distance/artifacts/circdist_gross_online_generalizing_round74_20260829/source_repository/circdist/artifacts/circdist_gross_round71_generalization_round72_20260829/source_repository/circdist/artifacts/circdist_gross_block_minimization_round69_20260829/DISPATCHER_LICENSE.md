# Exact continuation license

## Frozen restart state

- next iteration: 6
- inherited blocks: 1,460
- round-69 generalized blocks: 4,740
- installed dynamic blocks: 12
- next outer total: 6,212
- dynamic state: `cegar/dynamic_blocks.json`
- forbidden exploratory round-63 pair clauses: 0 installed

No iteration-6 candidate has been created. The restart therefore has no candidate awaiting a direct query.

## Build the next outer candidate

Use a clean environment containing `requirements.txt`. Write continuation output outside the repository:

```bash
PKG=/absolute/path/to/circdist_gross_block_minimization_round69_20260829
OUT=/tmp/circdist_round69_iter6
"$PYTHON" "$PKG/src/build_cegar_candidate.py" \
  --iteration 6 \
  --output "$OUT" \
  --dynamic-blocks "$PKG/cegar/dynamic_blocks.json" \
  --z3-timeout-ms 120000
```

Apply an external 180-second foreground timeout. If the outer result is UNKNOWN or times out, preserve the files and stop with no verdict. If outer is UNSAT, do not claim `D*=11` until the complete outer exhaustion object has an independently checked proof appropriate to the SMT encoding.

## Query both complete direct sectors

If outer is SAT, run both commands even if the first one is SAT:

```bash
"$PKG/tooling/cadical-1.9.5-arm64-macos" -t 600 --no-binary \
  "$OUT/direct360/Xerr.cnf" "$OUT/solver/Xerr.drat" \
  > "$OUT/solver/Xerr.solver.log" 2>&1

"$PKG/tooling/cadical-1.9.5-arm64-macos" -t 600 --no-binary \
  "$OUT/direct360/Zerr.cnf" "$OUT/solver/Zerr.drat" \
  > "$OUT/solver/Zerr.solver.log" 2>&1
```

Each needs a 660-second external hard timeout and a run JSON containing exact argv, exit code, wall time, and timeout flag.

If both are SAT, replay them:

```bash
"$PYTHON" "$PKG/src/replay_direct_candidate.py" --root "$OUT"
```

Only after that replay passes may a copied dynamic-state file be extended:

```bash
cp "$PKG/cegar/dynamic_blocks.json" /tmp/round69_dynamic_blocks_iter6.json
"$PYTHON" "$PKG/src/append_dynamic_blocks.py" \
  --verification "$OUT/direct_verification.json" \
  --dynamic-blocks /tmp/round69_dynamic_blocks_iter6.json \
  --iteration 6
```

Do not mutate this sealed package.

## If a sector is UNSAT

Retain the complete DIMACS and proof. Independently run DRAT and LRAT checks, with positive/corrupted checker controls in the same environment. A missing/rejected proof, UNKNOWN, timeout, or solver exit other than checked UNSAT is no absence verdict. Do not append a SAT block for an UNSAT sector.

## Repair gate

Enter arbitrary-round repair only if Xerr and Zerr for the same candidate both have independently accepted candidate-specific absence proofs. This package provides no precedent for bypassing that gate.
