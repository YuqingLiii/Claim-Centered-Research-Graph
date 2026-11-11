# Proposed canonical delta for independent review

This file is a proposal only.  Round 102 did not edit
`circdist/proof-dag/nodes/CIRCDIST.gross.yaml`, the scheduler, any protocol, or
any review.  A reviewer may translate the following evidence update into the
live schema after checking this package seal.

## Status fields

Leave unchanged:

```yaml
status: CONJECTURED
gap_via_lift_status: CONJECTURED
distance_bound:
  lower: 11
  upper: 12
```

Neither root-completing branch is proved.  Do not promote the node or
`gap-via-lift`.

## Proposed evidence entry

```yaml
- id: circdist-gross-global-translation-quotient-round102
  kind: exact_finite_symmetry_and_cegar_frontier
  artifact: circdist/artifacts/circdist_gross_global_closure_round102_20260901
  result: MATERIAL-CHECKED-GLOBAL-PROGRESS-NOT-CLOSED
  root_branch_A_legal_distance_12_witness: false
  root_branch_B_all_legal_schedules_distance_at_most_11: false
  theorem_scope:
    group: Z_12_x_Z_6
    group_order: 72
    schedule_action: exact_bijection_on_all_864_frozen_edges
    direct_action: exact_bijection_on_all_360_named_columns_per_sector
    invariant_blocks: 517140
    invariant_selectors_iter186: 23868
    quotient_equisatisfiable_with_invariant_base: true
  corrected_quotient:
    cnf_sha256: f6dec16c6ee19ee1a041d3eb78786171558f54805c3038ce9c311c62b82d7c13
    variables: 2447800
    clauses: 11774686
    result: SATISFIABLE
    schedule_sha256: f6a806a1b90535d497da63b154960f9ebf172c6c740356470cdeda56866bd5cf
    complete_unrestricted_direct_360:
      Xerr: SATISFIABLE
      Zerr: SATISFIABLE
  fresh_unstarted_frontier:
    iteration: 187
    source_sha256: d7a1f6bf63b328627362a70518f5beb77d3b4b32241ccaaab83d6d5d5c122124
    source_semantic_sha256: 88c726321144b782ce7fb72d8b1ed0d361473ab6587bb7f3ba8ec6cd0079dfa3
    state_sha256: b7fa430f67bdcb8fdb034c8e42174ee219d0d77ecdbe57f99576de1518de9bea
    selector_state_sha256: 7667fc8230b67224b1895180764680c5000dcef34b3c67352f904e5998e8879b
    invariant_blocks: 517140
    invariant_selectors: 24012
    quotient_cnf_sha256: e415b4c2c5b4923a47348a06ea9ebb06bbc85cea2c9c32bd3a9b25a1ce198234
    started: false
  exclusions:
    iteration184_exact_selectors_added: 2
    corrected_candidate_translation_orbit_selectors_added: 144
    all_new_selectors_source_schedule_valid_and_physically_replayed: true
  limitations:
    - no Gross UNSAT proof occurred
    - no circuit-distance-12 witness occurred
    - exploratory unclosed quotient has no global coverage status
    - fixed-basis span and mixed-sector results retain their prior limited scope
```

## Reviewer checks before adoption

The reviewer should verify `SHA256SUMS.txt`, `PAYLOAD_SHA256SUMS.txt`, and
`FILE_INVENTORY.jsonl`; run `source/check_manifests.py`; inspect `RESULT.json`,
`GLOBAL_TRANSLATION_THEOREM.md`, and `verification/preseal_replay.json`; and
confirm that repository-gate diagnostics are confined to this unlinked package.
