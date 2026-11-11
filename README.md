# Claim-Centered Research Graph

[![Proof DAG audit](https://github.com/YuqingLiii/Claim-Centered-Research-Graph/actions/workflows/proof-dag-audit.yml/badge.svg)](https://github.com/YuqingLiii/Claim-Centered-Research-Graph/actions/workflows/proof-dag-audit.yml)

This repository contains the claim-centered research state for ten research projects covering ten of the twelve problems listed in the [problem index](PROBLEM_INDEX.md): quantum query complexity (minimal-alphabet Set Equality, small-alphabet \(k\)-Sum), quantum channel capacity and additivity, circuit distance of quantum error-correcting codes, and Grothendieck-type Bell inequalities. Each project is represented as an AND/OR proof DAG. A node records one mathematical claim, its proof routes and dependencies, its current evidence level, and direct links to the evidence used to assess it.

## Paper

[A Claim-Centered Research Record for AI-Assisted Theoretical Research:
Examples in Quantum Query Complexity (PDF)](paper/claim-centered-research-record.pdf)

The paper is licensed under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
This license statement applies to the paper only.

## Start here

- [Problem index](PROBLEM_INDEX.md)
- [File protocol](FILE_PROTOCOL.md)
- [DAG protocol](DAG_PROTOCOL.md)
- [Evidence gaps](EVIDENCE_GAPS.yaml)

## Repository structure

```text
channel-additivity-violations/              P01 Channel additivity violations
werner-holevo-capacity-threshold/           P02 Werner–Holevo zero-capacity boundary
circuit-distance-stabilization/             P05 Circuit-distance stabilization
circuit-versus-effective-distance/          P06 Circuit versus effective distance
gross-code-optimal-circuit-distance/        P07 Optimal circuit distance of the Gross code
distance-preserving-schedule-complexity/    P08 Complexity of distance-preserving schedules
ksum/                                       P09 Quantum k-sum with small alphabets
se/                                         P10 Set equality and collision
finite-dimensional-grothendieck-bounds/     P11 Finite-dimensional Grothendieck bounds
group-orbit-bell-matrices/                  P12 Group-orbit Bell matrices
paper/
  claim-centered-research-record.pdf
tools/                                      shared DAG validators only
```

Every project directory has the same layout: `README.md`, `proof-dag/` (`PROJECT.yaml`, `nodes/`, generated `NODE_INDEX.md` and `GRAPH.mmd`), and, where present, `artifacts/`, `reviews/`, `lean/` and `tools/`.

Begin with a generated `NODE_INDEX.md`, open a claim node under
`<project>/proof-dag/nodes/`, and follow its structured links to the
relevant proof, computation, review finding, or Lean formalization. The
materials for each case study are kept inside its own project directory, so a
single case study can be exported without collecting evidence from elsewhere
in the repository. The repository is a snapshot of the current DAG and its
evidence. The public paper is included as a PDF; its LaTeX source, raw model
conversations, private accounting data, and unrelated projects are not included.
Linked evidence that is deliberately not included (third-party papers, raw logs, oversized solver output) is listed in `EVIDENCE_GAPS.yaml`; the validators report it as a declared gap, never as present. The snapshot preserves selected research events and failed claims, not a complete
event-by-event history. The protocols specify how subsequent updates should be recorded;
passing the static checks does not establish completeness of the historical record.

## Validate

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

make audit
make validate
```

For retention checks against a saved earlier snapshot, additionally run
`python tools/proof_dag_check.py --previous-state /path/to/earlier-snapshot`.
This checks that previously registered nodes, routes, and events have not disappeared
and that existing events have not been rewritten. It does not inspect old model sessions.

The evidence levels are repository-local assessments. A linked Lean
formalization checks its formal statement under its declared assumptions; it
does not imply that every natural-language claim in the graph has been
formalized or externally accepted.
