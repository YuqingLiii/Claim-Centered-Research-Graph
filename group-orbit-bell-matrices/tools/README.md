# Group-orbit tools

Run from the repository root with Python 3 standard-library dependencies:

```text
python3 grothendieck-group-orbit/tools/check_balance_rigidity.py
python3 grothendieck-group-orbit/tools/check_spectral_stability.py
python3 grothendieck-group-orbit/tools/check_clifford_generators.py
```

The first two replay this round's exact finite examples. The third is the
existing Clifford-construction checker. These runs corroborate the linked
proofs; finite sample checks do not establish universal theorems by themselves.
Canonical evidence levels and review scopes live in the node YAML files.
