# File protocol

This protocol governs placement, naming, linking, generated views, and preservation. Mathematical
meaning, evidence levels, route semantics, and promotion are governed by
[`DAG_PROTOCOL.md`](DAG_PROTOCOL.md).

The objective is simple: a reader or a new worker must be able to start from one canonical node and
reach every artifact needed to inspect or continue that part of the research.

## 1. Canonical project layout

```text
research/<project>/
  README.md
  proof-dag/
    PROJECT.yaml              # schema version, project id, and roots
    REDIRECTS.yaml            # retired-id redirects only
    NODE_INDEX.md             # generated
    GRAPH.mmd                 # generated
    nodes/
      <stable-node-id>.yaml   # one canonical file per node
    lean/                     # optional node-mirrored formalization
  notes/                      # long derivations and synthesis notes
  paper/                      # project-specific manuscript material
  data/                       # reusable input data
  logs/                       # project-local run logs
```

Existing repository-level `artifacts/`, `logs/`, `results/`, `tools/`, and `paper/` remain valid.
This protocol does not move an existing cited artifact merely to make the directory tree uniform.
Research projects outside `research/<project>/proof-dag/` remain on their documented legacy layout
and schema until a separate migration is performed. Their previous placement rules are preserved at
`git:f0d686a:research/RESEARCH_STRUCTURE_PROTOCOL.md`; the current validator continues to read those
projects without treating them as canonical schema-v6 records.

## 2. Source of truth

Each fact has one canonical owner.

| Information | Canonical owner |
|---|---|
| Node claim, routes, assessment, disposition, frontier, and events | node YAML file |
| Project roots | `PROJECT.yaml` |
| Retired identifier redirects | `REDIRECTS.yaml` |
| Alias lookup, reverse dependencies, and graph drawing | generated files |
| Long proof, review, run, certificate, or dataset | linked artifact |
| Placement and preservation rules | this protocol |
| Mathematical update and audit rules | `DAG_PROTOCOL.md` |

Do not maintain a second authoritative copy of a claim, dependency list, or level. A prose summary
may explain the state, but it must point back to canonical node IDs.

## 3. One node, one file

Every node has exactly one file:

```text
research/<project>/proof-dag/nodes/<stable-node-id>.yaml
```

The filename equals the node ID. Node files use schema v6 from `DAG_PROTOCOL.md`; they do not store
parents, paths to themselves, structural kinds, or generated index content. Reverse dependencies
are derived by scanning route premises.

Node IDs are stable. If a correction preserves the same proposition, revise the claim and append an
event. If the proposition changes materially, create a new node and add an explicit redirect or
supersession record rather than silently reusing the old identity.

## 4. Where material goes

- A claim, route, evidence pointer, review judgment, failure, or next action goes in the affected
  canonical node.
- A long derivation or synthesis note goes in the project `notes/` directory and is linked from the
  relevant assessment or route proof.
- An independent review remains a separate immutable artifact and is linked from the exact node or
  route it reviewed. The artifact records reviewer/model identity, independence, inspected
  materials, scope, verdict, and limitations; a review filename alone is not a completed gate. A
  review link's `scope`, when present, summarizes what the review actually checked and any relevant
  boundary of that check. It must not merely restate the claim under review.
- A machine run, certificate, generated table, or large output goes in an established artifact/log
  directory. A `NUMERICAL` assessment links it under `basis.runs` and records the result and scope;
  the node also records a locator or checksum when needed for unambiguous reproduction.
- A node-mirrored Lean development goes under `proof-dag/lean/`; standalone formal projects may use
  another clearly documented project-local directory. Build products such as `.lake/` and `.olean`
  are caches, not research records.
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
- Before moving a cited file, update all references atomically and provide a redirect when a stable
  historical path may still be used.

## 6. Atomic update protocol

A research update is complete only when all applicable steps have been performed:

1. read the target node and the routes and premises in scope;
2. write the proof, run, review, or counterexample to a stable location;
3. link that object from the precise node or route assessment it supports;
4. update the level, caveats, disposition, frontier, and append-only event under the DAG protocol;
5. update a formal mirror and claim hash, or mark it `stale` with a synchronization gate;
6. regenerate `NODE_INDEX.md` and `GRAPH.mmd`; and
7. run the structural and semantic validator.

The update is also compared with its git base. Existing event entries may not be deleted or edited,
and every node- or route-level change requires a new matching `level-change` event. This turns the
append-only requirement into an automatically checked repository invariant.

An unlinked artifact is orphaned work and does not complete the update.

## 7. Preservation and migration

Do not delete a proof attempt, counterexample, negative route, completed review, or status-changing
event. A superseded object may leave the active frontier, but its content must remain reachable
through the node event history or an immutable repository snapshot.

Schema migration must:

1. create an immutable baseline;
2. preserve that baseline in every migrated node's event record;
3. distinguish mechanical normalization from new mathematical judgment;
4. validate all references and cycles before declaring success; and
5. keep generated views reproducible from canonical files.

## 8. Closeout checks

From the repository root, run:

```text
python3 tools/proof_dag_check.py --problem ksum --write-generated --verify-git
python3 tools/proof_dag_check.py --problem se --write-generated --verify-git
python3 tools/check_event_append_only.py --base-ref HEAD
git diff --check
```

Then confirm that every changed claim has a reason, every assessment has sufficient basis, every
new artifact is reachable, failed routes were not erased or over-propagated, and no generated file
has become a competing source of truth.
