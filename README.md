# Claim-Centered Research Graph

[![Proof DAG audit](https://github.com/YuqingLiii/Claim-Centered-Research-Graph/actions/workflows/proof-dag-audit.yml/badge.svg)](https://github.com/YuqingLiii/Claim-Centered-Research-Graph/actions/workflows/proof-dag-audit.yml)

This repository contains the current claim-centered research state for two
case studies in quantum query complexity: minimal-alphabet Set Equality and
small-alphabet \(k\)-Sum. Each project is represented as an AND/OR proof DAG.
A node records one mathematical claim, its proof routes and dependencies, its
current evidence level, and direct links to the evidence used to assess it.

## Start here

- [File protocol](FILE_PROTOCOL.md)
- [DAG protocol](DAG_PROTOCOL.md)
- [Set Equality node index](se/proof-dag/NODE_INDEX.md)
- [Small-alphabet k-Sum node index](ksum/proof-dag/NODE_INDEX.md)

## Repository structure

```text
se/
  proof-dag/                   Set Equality nodes and generated graph views
  lean/                        linked Lean development
  reviews/                     project-level external reviews
  artifacts/                   proofs, runs, and counterexamples
ksum/
  proof-dag/                   k-Sum nodes and generated graph views
  lean/                        linked Lean development
  reviews/                     project-level external reviews
  artifacts/                   proofs, runs, and counterexamples
  tools/                       project-specific mathematical checkers
tools/                         shared DAG validators only
```

Begin with a generated `NODE_INDEX.md`, open a claim node under
`<project>/proof-dag/nodes/`, and follow its structured links to the
relevant proof, computation, review finding, or Lean formalization. The
materials for each case study are kept inside its own project directory, so a
single case study can be exported without collecting evidence from elsewhere
in the repository. The repository is a snapshot of the current DAG and its evidence. Manuscripts,
raw model conversations, private accounting data, and unrelated projects are
not included.

## Validate

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

make audit
make validate
```

The evidence levels are repository-local assessments. A linked Lean
formalization checks its formal statement under its declared assumptions; it
does not imply that every natural-language claim in the graph has been
formalized or externally accepted.
