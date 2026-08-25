# Proof-DAG protocol

This protocol defines the public research state used by every proof-oriented project in the
repository. Its purpose is to make claims, alternative proof routes, dependencies, evidence,
reviews, failures, and remaining work auditable without reconstructing them from chat logs.

The protocol is general: it does not prescribe a model, agent role, wall-clock schedule, or
project-specific workflow.

## 1. Canonical object

Each project stores one YAML file per node under `<project>/proof-dag/nodes/`. A minimal
record has the following form; optional blocks are omitted rather than written as null values.

```yaml
id: PROJECT.unique-id
role: proof                    # optional: proof | obstruction | outcome | tool | constraint
aliases: [short-name]          # optional
claim: >-
  A precise, reviewable proposition or research outcome.

assumptions:                   # optional; only for route-free direct proofs
  cited-result:                # established external theorem or model fact used by the proof
    kind: external-theorem     # external-theorem | model-fact
    statement: Exact statement and scope.
    source:
      path: path/to/source
      kind: text
      locator: Theorem or section containing the imported statement

routes:                        # optional: alternative ways to establish the claim
  route-id:
    premises: [PROJECT.B, PROJECT.C]
    assumptions:               # optional; established interfaces only
      cited-result:
        kind: external-theorem # external-theorem | model-fact
        statement: Exact statement and scope.
        source:
          path: path/to/source
          kind: text
          locator: Theorem or section containing the imported statement
    implication: >-
      Explain why all listed premises, under the listed assumptions, imply this node's claim.
    proof:                     # optional until an argument exists
      sketch: Reviewable blueprint or completed argument.
      sources:
        - path: path/to/argument
          kind: text
    assessment:
      level: OPEN
      summary: What is and is not established about this implication.
      basis:                   # optional: evidence | reviews | runs | counterexamples
        evidence:
          - path: path/to/evidence
            kind: text

assessment:
  level: OPEN                  # OPEN | CONJECTURED | NUMERICAL | CERTIFIED* | PROVED | REFUTED
  summary: Current judgment of the node's own claim.
  basis:                       # optional
    routes: [route-id]
    reviews:                  # external-review records
      - path: project/reviews/review-report.md
        kind: review
        locator: Finding F1
        scope: What this finding checked and what it did not check.
        reviewed_hash: sha256:... # digest of this exact claim or route implication

disposition:                   # optional; operational, not evidential
  state: PARKED                # PARKED | DEAD
  reason: Why work stopped.
  revive: What new evidence would reopen a PARKED node.
  source:
    path: path/to/stopping-evidence
    kind: review

formalization:                 # optional; present only for a linked formalization
  lean:
    module: Project.Module
    file: path/to/Module.lean
    claim: Claim
    state: stated
    claim_hash: sha256:...
    source_claim_hash: sha256:...
    sync_state: current        # current | stale
    synced: YYYY-MM-DD
    theorems: [TheoremName]
    rel: [declared assumptions and correspondence notes]
    build: path/to/build-evidence

frontier:                      # optional; only unfinished actions
  task-id:
    task: A concrete next action.
    kind: task                 # task | gate | review
    since: YYYY-MM-DD

events:                        # optional; material changes to the research state
  event-id:
    date: YYYY-MM-DD
    type: level-change         # created | level-change | route-added | route-retired |
                               # route-refuted | review-completed | repair-applied
    from: OPEN                 # required only for level-change
    to: CONJECTURED            # required only for level-change
    summary: What changed and why.
    sources:
      - path: path/to/supporting-record
        kind: review
```

Closed-key validation is deliberate: a field with no protocol semantics is rejected instead of
silently becoming an undocumented second source of truth.

## 2. Nodes and routes

A node is the smallest independently auditable research object. It owns one claim, one assessment,
and the evidence needed to interpret that assessment. The protocol does not distinguish structural
types such as `goal`, `leaf`, or `kind`: a node may acquire or lose routes without changing its
identity.

A route is a directed AND-hyperedge stored in the node it seeks to establish. Its `premises` are
jointly required; the different routes of one node are alternatives. Thus premises are combined by
AND within a route and routes are combined by OR across the node. Reverse dependencies, roots,
indexes, and diagrams are derived views and are never copied into node files.

Every route contains two logically separate obligations:

1. the listed premise claims must be established to the level required by the parent; and
2. the route implication must itself be argued and reviewed.

These obligations may be completed in any order. A level never propagates automatically across a
route. A completed parent requires an assembled, reviewable argument containing every load-bearing
premise and the corresponding route implication.

A direct proof needs no artificial empty-premise route. It is recorded in the node's assessment
basis and linked evidence. An unresolved hypothesis is not an assumption: it becomes its own OPEN
node and is listed as a premise. `assumptions` is reserved for already established external theorems
and explicit model facts. Every assumption records its exact statement and scope together with a
locatable source, given as a repository path, a claim-node reference, or a precise bibliographic
note. A route-free node registers these inputs in a node-level `assumptions` block. A node with
routes instead registers each input under every route that uses it. This keeps every load-bearing
external input machine-visible and attaches it to the argument whose validity depends on it.

A `basis.evidence` entry may link another node only as a non-load-bearing cross-reference, using
`kind: node-evidence`. If the parent claim mathematically depends on that node, the dependency must
instead appear under `routes.<route-id>.premises`; generic evidence links do not participate in DAG
reachability or completion checks.

## 3. Project-level review records

An external review is a first-class project-level object, not a field owned by
one node. Its immutable report lives under `<project>/reviews/`
and may cover a whole graph, a connected subgraph, several nodes, or several
route implications. The report states the reviewer or model, independence,
inputs inspected, scope, findings, verdict, and limitations. Each finding has
a stable locator and identifies the claims or routes it affects.

Nodes and routes do not copy the report. Their assessment bases link only the
applicable finding, together with a scoped description and, for a completion
level, the `reviewed_hash` of the exact statement reviewed. Thus one broad
review remains one public object while its consequences can be located and
audited at claim level.

## 4. Evidence levels

The level describes the evidence for the object on which it is written. Route levels assess route
implications; node levels assess node claims.

| Level | Meaning |
|---|---|
| `OPEN` | Registered but no reviewable argument yet. |
| `CONJECTURED` | A substantive blueprint or argument sketch exists. |
| `NUMERICAL` | A reproducible computation or mechanized run supports the scoped claim; the node links the command/output record and states what the run established. |
| `CERTIFIED*` | An independently reviewed conditional result with explicit unresolved premises or scope caveats. |
| `PROVED` | A complete argument and all load-bearing inputs passed independent adversarial review. |
| `REFUTED` | A structured counterexample or decisive contradiction refutes the precise claim or implication. |

Higher positive levels require stronger evidence, but the ladder is not an automatic arithmetic on
the graph. The node's level is written only after examining its own assembled dossier. The validator
may block an impossible promotion; it does not promote nodes.

## 5. Failure and disposition

Failure must be scoped to the proposition actually refuted.

- A refuted premise disables every route that requires it; it does not by itself refute the route
  implication or the parent claim.
- A refuted route implication kills that route only.
- Even if every registered route is dead, the parent is `OPEN` or `PARKED` unless the parent claim
  itself has been refuted. Registered routes are not assumed exhaustive.
- `DEAD` and `PARKED` are dispositions, not confidence levels. `DEAD` records a reviewed route with
  no known repair. `PARKED` requires a concrete revival condition.

Failed routes remain public through their route assessments and linked counterexamples. They are
removed from the active frontier, not erased from the research record.

## 6. DAG update protocol

Every mutation follows the same sequence.

1. **Read the current state.** Inspect the target node, its routes and premises, relevant source
   artifacts, and the generated dependency view.
2. **Register before testing or relying.** Add every substantive proposed claim or route before
   testing it or allowing another node to depend on it, including alternatives not selected for
   immediate work. A new route includes its premises, implication statement, and at least an OPEN
   assessment. Before leaving an attempted route, record whether it succeeded, failed, or remains
   untested, together with the supporting evidence or reason; a route must not disappear silently.
3. **Make dependencies explicit.** Convert every unresolved load-bearing hypothesis into a node.
   Record only established interfaces under `assumptions`.
4. **Attach evidence locally.** Put evidence, reviews, runs, and counterexamples in the assessment
   of the node or route they support. A filename or chat transcript is not a verdict by itself.
5. **Review before promotion.** Completion-level promotion of either a node or a route requires a
   locatable finding in a project-level independent adversarial review of the assembled argument by a reviewer other than its
   author. The review is normally conducted in a fresh review context and must state the reviewer
   or model, independence declaration, materials inspected, scope, verdict, and limitations. A
   linked review's scope describes the work actually checked, not merely the target claim. The
   review link records `reviewed_hash`, the digest of the exact node claim or route implication
   reviewed, and a completion assessment becomes invalid if that statement later changes. The
   structural validator checks that the review is linked, reachable, and hash-bound; whether it is genuinely
   independent and mathematically adequate remains an audit question, not a filename check.
6. **Record material changes.** Append a scoped event when a claim or route is registered, a level
   changes, a route is retired or refuted, a review is completed, or a mathematical repair is applied.
   Events describe changes to the research state; repository maintenance and schema changes are not
   research events.
7. **Refresh derived views and validate.** Regenerate the index and graph, then run the repository
   checker before closing the update.

## 7. Node-level audit protocol

An auditor must be able to start from one node without reading an entire conversation. For every
audited node, check:

1. the claim is precise and does not embed its current status;
2. every route lists all and only its load-bearing unresolved premises;
3. every external assumption states its exact theorem, regime, and source;
4. the implication proves the parent claim actually written, not an older or stronger statement;
5. the assessment level is licensed by the attached basis and caveats;
   a `NUMERICAL` assessment has an explicit run record, a `REFUTED` assessment identifies the
   counterexample or contradiction, and a completion assessment links its independent review;
6. failures are scoped to a premise, implication, route, or claim without over-propagation;
7. linked formalizations quote the current claim hash, or are explicitly marked `stale`; and
8. the frontier contains only unfinished, actionable work.

The complete audit report remains a project-level object. The finding relevant to
each claim or route is linked from that object's assessment. This makes review
incremental: unchanged subgraphs need not be re-audited merely because a
different route changed.

## 8. Formalization

Formal proof is linked to the same public state rather than maintained as a separate graph. A
`formalization` block is present only when a real module, file, and claim declaration exist.
`claim_hash` binds the formalization to the current natural-language claim. Any claim rewrite sets
`sync_state: stale` and creates a frontier gate until the formal statement, imports, proof, and hash
are synchronized.

A successful build is run evidence. It promotes a mathematical claim only to the extent that the
formal theorem contains all required premises and the formal-to-natural-language correspondence has
been reviewed.

## 9. Project manifest and generated views

`proof-dag/PROJECT.yaml` declares `schema_version`, project name, and root node IDs.
`NODE_INDEX.md` and `GRAPH.mmd` are generated from canonical node files. They may be deleted and
rebuilt without losing research state.

The schema and semantic checks are implemented by `tools/proof_dag_check.py`. The repository's
pull-request workflow regenerates the derived views and validates both case studies.
