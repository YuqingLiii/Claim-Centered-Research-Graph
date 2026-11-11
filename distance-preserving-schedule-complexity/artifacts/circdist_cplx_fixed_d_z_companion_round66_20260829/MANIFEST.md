# Round-66 sealed-package manifest

## Verdict-bearing proof material

| file | role |
|---|---|
| `README.md` | Self-contained proposer proof, exact theorem, hook algebra, counterexample, transform, case split, constants, and Karp reduction. |
| `THEOREM.txt` | Exact 999-character proposed full fixed-`d` theorem. |
| `LICENSED_X_THEOREM.txt` | Exact 883-character independently cleared X-EFF3 premise. |
| `DISPATCHER_LICENSE.txt` | Exact review license and conditional post-review installation boundary. |
| `ATTACK_LEDGER.md` | Public attack results, rejected branches, exact residual, and review targets. |
| `COUNTEREXAMPLE.json` | Complete raw matrices and GF(2) certificates for the smallest nonempty source-family increasing-block obstruction. |

## Clean-room implementation and outputs

| file | role |
|---|---|
| `construction.py` | Exact deterministic round-64 CSS/X builder copied from its sealed package. |
| `z_companion.py` | R3 hook model, private-sentinel transform, explicit orders, rank/quotient helpers, and exact terminal-column audit. |
| `make_counterexample.py` | Deterministic generator for `COUNTEREXAMPLE.json`. |
| `verify.py` | Standard-library checker with positive, adversarial, and real negative controls. |
| `verifier_output.json` | Genuine Python-3.9.6 foreground output: 20/20 PASS. |
| `requirements.txt` | Runtime boundary. |
| `COMMANDS.txt` | Copyable clean-room reproduction commands. |

## Governance and audit material

| file | role |
|---|---|
| `SOURCE_BINDINGS.txt` | Raw source-file hashes and exact theorem/claim hashes. |
| `PROCESS_LEDGER.txt` | Strict-serial foreground process declaration and FIX-2 accounting. |
| `FINAL_AUDIT.txt` | Pre-seal replay, repository-write, process, and scratch audit. |
| `SHA256SUMS.txt` | Internal payload seal; excludes itself. Its external SHA-256 is reported by the dispatcher. |

## Evidence boundary

The universal proof is in `README.md`. Finite output is corroboration and implementation checking,
not inductive evidence. The package is proposer-level and licenses no canonical promotion without
a fresh independent exact review.

## Minimal replay

From this directory:

```text
sha256sum -c SHA256SUMS.txt
PYTHONDONTWRITEBYTECODE=1 python3 verify.py > /tmp/circdist_round66_replay.json
python3 -m json.tool /tmp/circdist_round66_replay.json >/dev/null
```

The expected semantic result is `verdict=PASS`, `checks=20`, and 20 individual `PASS` entries.
See `COMMANDS.txt` for theorem-hash, raw-counterexample, compile, and cleanup commands.
