# File protocol

This protocol governs placement, naming, linking, generated views, and preservation. Mathematical
meaning, evidence levels, route semantics, and promotion are governed by
[`DAG_PROTOCOL.md`](DAG_PROTOCOL.md).

The objective is simple: a reader or a new worker must be able to start from one canonical node and
reach every artifact needed to inspect or continue that part of the research.

## 1. Canonical project layout

```text
<project>/
  README.md
  proof-dag/
    PROJECT.yaml              # schema version, project id, and roots
    NODE_INDEX.md             # generated
    GRAPH.mmd                 # generated
    nodes/
      <stable-node-id>.yaml   # one canonical file per node
  lean/                       # optional linked Lean formalization
  reviews/                    # reviews covering this project or a subgraph
  artifacts/                  # proofs, runs, certificates, and other evidence
  tools/                      # optional project-specific checkers
```

This release contains exactly two projects, `se` and `ksum`. Each project is
self-contained: its node-linked proofs, runs, certificates, reviews, Lean
files, and project-specific checkers remain under the same
`<project>/` directory. A review is a project-level object rather
than a child of one node, so a single report may cover a whole graph, a
connected subgraph, several nodes, or several route implications. Only the
validators shared by both projects live in the repository-level `tools/`
directory.
Manuscripts, raw conversations, private accounting data, unrelated projects,
and unlinked exploratory output are outside the public release.

## 2. Source of truth

Each fact has one canonical owner.

| Information | Canonical owner |
|---|---|
| Node claim, routes, assessment, disposition, frontier, and research events | node YAML file |
| Project roots | `PROJECT.yaml` |
| Alias lookup, reverse dependencies, and graph drawing | generated files |
| External review scope, findings, verdict, and limitations | immutable report under `<project>/reviews/` |
| Long proof, run, certificate, or dataset | linked file under `<project>/artifacts/` |
| Placement and preservation rules | this protocol |
| Mathematical update and audit rules | `DAG_PROTOCOL.md` |

Do not maintain a second authoritative copy of a claim, dependency list, or level. A prose summary
may explain the state, but it must point back to canonical node IDs.

## 3. One node, one file

Every node has exactly one file:

```text
<project>/proof-dag/nodes/<stable-node-id>.yaml
```

The filename equals the node ID. Node files use the schema in `DAG_PROTOCOL.md`; they do not store
parents, paths to themselves, structural kinds, or generated index content. Reverse dependencies
are derived by scanning route premises.

Node IDs are stable. If a correction preserves the same proposition, revise the claim in place. If
the proposition changes materially, create a new node rather than silently reusing the old identity.

## 4. Where material goes

- A claim, route, evidence pointer, claim-level assessment, failure, or next action goes in the
  affected canonical node.
- A long derivation or synthesis note goes in `<project>/artifacts/` and is linked from the relevant assessment
  or route proof.
- An independent review is an immutable project-level report under
  `<project>/reviews/`, not a child of any node.
  The report records reviewer/model identity, independence, inspected materials, scope, findings,
  verdict, and limitations. Each affected node or route links the applicable finding by report path
  and locator; a completion-level link also binds the exact reviewed statement with
  `reviewed_hash`. A link's `scope` summarizes what the review actually checked and any relevant
  boundary of that check. It must not merely restate the claim under review.
- A machine run, certificate, generated table, or large output goes in
  `<project>/artifacts/`. A
  `NUMERICAL` assessment links it under `basis.runs` and records the result and scope;
  the node also links its checker, records the command and dependencies, and gives a locator or
  checksum when needed for unambiguous reproduction. A fresh rerun is dated as such and must not
  be presented as a recovered historical log. A historical output without an available checker
  is identified as an archived result, not as a directly reproducible run.
- A linked Lean development goes under `<project>/lean/`. Build
  products such as `.lake/` and `.olean` are caches, not research records.
- A mathematical checker used by only one case study goes under
  `<project>/tools/`; only shared structural validators belong in the
  repository-level `tools/` directory.
- A verified reference note used by a claim goes under
  `<project>/artifacts/` and is linked from the precise assumption or
  evidence entry that uses it.
- A disposable experiment may remain in `tmp/`, but it cannot support a level change until its
  durable inputs, outputs, and command are placed in a stable linked location.

Large bodies of text are linked rather than copied into every node. Reachability from the node is
mandatory; physical co-location is not.

## 5. Naming and links

- Use stable descriptive names, not `final`, `new`, `latest`, or agent names.
- Use `YYYYMMDD` or `YYYY-MM-DD` for dates.
- Prefer project and node/purpose slugs for artifacts.
- Store repository-relative paths in structured sources.
- Before adding a new artifact, search for an existing canonical object that should own the work.
- Before moving a cited file, update all structured references in the same change.

## 6. Atomic update protocol

A research update is complete only when all applicable steps have been performed:

1. read the target node and the routes and premises in scope;
2. write the proof, run, or counterexample to a stable artifact location, or write an independent
   review as a project-level report under `<project>/reviews/`;
3. link the applicable object or review finding from each precise node or route assessment it supports;
4. update the level, caveats, disposition, frontier, and applicable research event under the DAG protocol;
5. update a linked formalization and claim hash, or mark it `stale` with a synchronization gate;
6. regenerate `NODE_INDEX.md` and `GRAPH.mmd`; and
7. run the structural and semantic validator.

An unlinked artifact is orphaned work and does not complete the update.

## 7. Preservation

Do not delete a proof attempt, counterexample, negative route, or completed project-level review that
remains part of the public research state. A superseded route may leave the active frontier, but it
remains in its parent node with its assessment and linked evidence.

## 8. Closeout checks

From the repository root, run:

```text
python3 tools/proof_dag_check.py --problem ksum --write-generated
python3 tools/proof_dag_check.py --problem se --write-generated
```

Then confirm that every changed claim has a reason, every assessment has sufficient basis, every
new artifact is reachable, failed routes were not erased or over-propagated, and no generated file
has become a competing source of truth.
