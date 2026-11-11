# WHGAP review commission R1 — independent adjudication of the antidegradability-boundary work (2026-07-28)

**Node (rule 8a):** `WHGAP.antideg-boundary`. **This review is the rule-6 completion gate** for that
node: no CERTIFIED*/PROVED/REFUTED may be written anywhere without citing THIS review, completed and
archived. **Runs ONLY after** `WHGAP_COMMISSION_P1_20260728.md` has produced its artifact.

**Reviewer identity (rule 2/6):** a FRESH codex session that did not author any of the reviewed
work. This prompt states no desired outcome; the mandate is to adjudicate correctness, completeness,
and licensing — nothing else. The reviewer writes NO node statuses; it produces an immutable report.
Status application is a separate decision-layer step that cites the report (DAG protocol §2).

## Step -1 — mandatory pre-task reload

Execute the standalone rules-reload prompt `research/PRETASK_RELOAD_PROMPT.md` FIRST, with
{PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.antideg-boundary`,
ROLE = reviewer. No work before its PRE-ACTION REPORT (including your independence statement) is
produced; its folder-and-DAG maintenance obligations bind this entire commission. Disk overrides
this commission on any conflict.

## Reviewed objects (frozen scope)

- Artifact: `artifacts/whgap_antideg_boundary_20260728.md`
- Scripts: `tools/whgap_p0_calibration.py`, `tools/whgap_p1_antideg_boundary.py`
- Logs: `artifacts/logs_whgap_20260728/` (+ SHA256SUMS)
- Node: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.antideg-boundary.md`
- Spec: the frozen-conventions block of `WHGAP_COMMISSION_P1_20260728.md` may be read as the
  problem spec, but every mathematical claim in it must be independently re-verified, not trusted
  (see 7d below — the spec's ground truths are exactly what to check).

## Mandatory review-quality checklist (rule 7, embed-and-execute; a review missing any item opens NO gate)

- **(7a) Type audit.** For EVERY displayed operator identity in the artifact and scripts — channel
  action, Kraus/CPTP identities, complementary channel, Choi construction, partial transpose,
  symmetric-extension constraints — state domain, codomain, and dimensions as functions of x, and
  verify every constituent map is well defined. Specifically verify: the swap S_12 acts on the
  correct tensor factors of the 27-dim space; Tr_{B2} is taken in the SAME basis ordering used to
  build eta (basis-ordering bugs are the standing failure mode here); the Choi normalization (1/3)
  is consistent between construction and constraint. A review with no per-display type audit
  licenses nothing.
- **(7b) Regime-complete identity gates.** With the reviewer's OWN implementation (see 7c): re-run
  feasibility at BOTH endpoints (x=1/2, x=4/7) and at >= 3 interior points on EACH side of the
  claimed boundary; treat degenerate eigenvalue multiplicities (the Choi spectra here have
  multiplicity >= 2) explicitly at the identity level, not only through aggregate solver output.
  Every regime the proposer did not exercise (e.g. the exact-certificate branches, extreme
  accuracy settings) must be NAMED as untested in the verdict; licensing then caps at CERTIFIED*
  with that regime in the caveat.
- **(7c) Anchoring ban.** BEFORE opening the proposer's scripts or artifact tables: implement the
  channel family, Choi, and symmetric-extension feasibility test from the frozen conventions in
  your OWN construction (your own basis bookkeeping and, where possible, your own SDP formulation),
  and compute your own t*(x) values and boundary bracket. Only then read the proposer's material
  and compare. If your derivation ends up notationally coinciding with theirs, flag the coincidence.
- **(7d) No frozen-input immunity.** The six calibration ground truths (CPTP identities, Lambda^c(1)
  spectrum, Choi^{T_A} spectrum, lift identity, defect factorization, witness values) are used
  load-bearingly; re-verify each with your own exact computation. Any input leaned on outside the
  scope of an archived review must be re-opened for the uncovered aspect.
- **(7e) Standing failure-mode list (check every one, not only the last war):** dropped/extra
  normalization factors; type/dimension mismatches; undefined terms of art ("antidegradable",
  "feasible", tolerance semantics) and missing stability ranges; partial objects silently
  substituted for full ones (a subset of constraints, a subspace of the extension); numerics
  validating VALUES while the printed derivation is broken; sign/transpose convention drift
  (T_A vs T_B, S_12 direction); solver-status laundering (`inaccurate`/`unbounded` treated as
  clean); rounding-then-asserting exactness without an exact PSD check.
- **(7f) Value-vs-formula decoupling.** The verdict must state explicitly that your numbers come
  from an INDEPENDENT implementation (verification), not from re-running the proposer's scripts
  (reproduction). Do both, but label which established what.
- **(7g) Quantifier hygiene.** Every term of art in the reviewed claims ("boundary", "tight",
  "certificate", "feasible at tolerance") must resolve to a definition in the reviewed documents or
  an explicitly cited one; check resolvability, not mere consistency.

## Deliverables

1. Immutable report `artifacts/whgap_p1_review_20260728.md`: per-claim verdicts
   (PASS / MINOR / MAJOR / GAP) covering (i) the six calibration ground truths, (ii) the endpoint
   gates, (iii) the boundary value and bracket, (iv) any exactness/certificate claims; the
   reviewer's OWN x* value and bracket; the explicit untested-regime list; and a licensing
   statement: "this review does / does not open the completion gate for <exact claims>, at tier
   <CERTIFIED* / PROVED>, with scope <...>".
2. Reviewer's own scripts + logs under `artifacts/logs_whgap_review_20260728/` with SHA256SUMS.
3. Append a dated entry to the node's `Adversarial reviews` section linking the report. No status
   writes.
4. Run `python tools/proof_dag_check.py --problem werner-holevo-gap` (must exit 0).
5. Print `FINAL: REVIEW-COMPLETE` or `FINAL: FAILED — <reasons>`.

**Executor:** codex CLI, one sequential session, workspace-write, NO network; Python
`"C:<home>/cpython3119/python.exe"` (CPython 3.11.9; pinned: numpy 1.26.4,
scipy 1.14.1, sympy 1.13.1, mpmath 1.3.0, cvxpy 1.6.0, scs 3.2.7). Budget <= 60 min; stop-loss on
two info-free cycles or budget breach.

## Provenance addendum — 2026-07-28 (decision layer, pre-dispatch)

This review prompt was drafted by the run-1 executor session as the paired completion gate, then
AUDITED AND ADOPTED by the decision layer before dispatch: neutrality checked (no desired outcome
stated; reviewer writes no statuses; anchoring ban intact), rule-7 items verified present, and the
interpreter line above replaced — the originally pinned WindowsApps path is unresolvable under the
codex sandbox token (see the Environment addendum in `WHGAP_COMMISSION_P1_20260728.md`, same date;
identical pinned package versions verified under the replacement interpreter). The reviewer is a
fresh session that did not author any reviewed object; independence per rules 2/6 is preserved.

