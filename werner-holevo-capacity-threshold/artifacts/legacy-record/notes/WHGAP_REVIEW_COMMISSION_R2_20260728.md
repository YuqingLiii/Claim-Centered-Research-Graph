# WHGAP review commission R2 — independent adjudication of the signed-lift extension work (2026-07-28)

**Node (rule 8a):** `WHGAP.signed-lift-extension`. **This review is the rule-6 completion gate** for
that node: no CERTIFIED*/PROVED/REFUTED may be written anywhere without citing THIS review,
completed and archived.

**Reviewer identity (rules 2/6):** a FRESH codex session that did not author any of the reviewed
work. This prompt states no desired outcome; the mandate is to adjudicate correctness,
completeness, and licensing — nothing else. The reviewer writes NO node statuses; it produces an
immutable report. Status application is a separate decision-layer step citing the report.

**Authorship note:** this commission was authored by the decision layer (which also authored the
execution commission but none of the executor's mathematics, scripts, or artifact).

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.signed-lift-extension`, ROLE = reviewer.
No work before its PRE-ACTION REPORT (including your independence statement). Disk overrides this
commission on any conflict.

## Reviewed objects (frozen scope)

- Artifact: `artifacts/whgap_signed_lift_extension_20260728.md`
- Scripts: `tools/whgap_p2_exact.py`, `tools/whgap_p2_feasibility.py`, `tools/whgap_p2_twirling.py`
- Logs/JSON: `artifacts/logs_whgap_p2_20260728/` (+ SHA256SUMS)
- Node: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.signed-lift-extension.md`
- Spec: the frozen-conventions and gates of
  `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P2_20260728.md` may be read as the
  problem spec, but every mathematical claim in it must be independently re-verified (7d).
- Literature (read-only context): the local Zhu–Wang PDF
  `channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/arxiv_2607.24693.pdf`
  (empty-password encrypted: extract text with pypdf `PdfReader(...).decrypt('')`). Their
  Theorem 3.3 / Lemma 3.2 / Corollary 3.7 and the HRSF22 tensorization are CITED generic theorems:
  you re-verify their HYPOTHESES for this application, not their proofs.

## Claims under adjudication (verdict each: PASS / MINOR / MAJOR / GAP)

1. The general-x complementary channel and its Hilbert–Schmidt adjoint as displayed in the
   artifact (block form with `k = sqrt(x(1-x)/2)`).
2. The five-parameter real equivariant ansatz is adjoint-preserving, and the three displayed
   Schur-sector intertwining equations are exactly the constraint `J^dag ∘ Lambda_x^c = Lambda_x`
   (no lost equations, no lost solutions; coefficient-matrix rank 3 for ALL x in (0,1), or the
   exceptional set named).
3. The residual parameterization (p, q, c1, c2, c3 as displayed functions of (x, s1, s2)) and the
   x=1/2 recovery of the Zhu–Wang lift.
4. The 27×27 defect Choi construction; the spin-block reduction (multiplicity spaces of sizes
   1, 3, 2, 1); and the displayed exact principal-minor characterization, INCLUDING the three
   spin-1 negative-square minors, the spin-0 factorization, det B2, and B3 = 0.
5. The elimination logic: PSD of the full Choi forces the unique
   `s1 = 2(1-x)/(3x)`, `s2 = (5x-2)/(3x)` (no other solution branches survive; the vanishing
   system is consistent and its solution unique), and the reduced blocks
   `B1 ∝ 4(1-x)(3x-1)/(9x)`, `B2 ∝ 4(1-x)(2x-1)/(3x)` (rank-one forms) are correct.
6. The exact feasible region claim: defect Choi PSD on the forced point exactly for
   `1/2 <= x < 1` within (0,1); infeasibility strictly below 1/2; behavior at both endpoints
   (x = 1/2 rank structure; x -> 1 faithfulness degeneration).
7. The three solver-free certificates (x = 26/51, 4/7, 3/4) and the direct-27×27 vs
   spin-block spectrum linkage.
8. The twirling ingredients: the covariance identities with `V(O) = diag(1, det(O) O)` (attend to
   the epsilon-tensor det twist) and the congruence-convexity identity — state precisely what
   these DO and DO NOT establish (the full averaging/WLOG lemma is NOT claimed by the executor).
9. The generic-theorem application chain for x in [1/2, 1): verify from the local PDF that
   Theorem 3.3's hypotheses (faithful outputs; adjoint-preserving intertwining; CP defect) are
   exactly what the executor established at general x, and name every additional hypothesis of
   Lemma 3.2 / Corollary 3.7 / the tensorization step (e.g. support or faithfulness conditions)
   that a full write-up must still discharge. This is a hypothesis audit, not a re-proof.

## Mandatory review-quality checklist (rule 7, embed-and-execute; a review missing any item opens NO gate)

- **(7a) Type audit.** For EVERY displayed identity in the artifact and scripts: state domain,
  codomain, and dimensions as functions of x; verify every constituent map is well defined
  (J: L(H_B) -> L(H_E) 9->16; Delta's Choi on H_A ⊗ H_B ⊗ H_B' 27-dim; the U_j column bases and
  Gram pencils; the k-branch `k = +sqrt(x(1-x)/2)` and where 1/k appears). Basis-ordering and
  Choi-leg conventions are the standing failure mode: state YOUR convention, verify THEIRS, and
  check conclusions (not notations) match.
- **(7b) Regime-complete identity gates.** With your OWN implementation: test x = 1/2 (boundary,
  rank drop), one point in (1/2, 4/7), x = 4/7, one point in (4/7, 1), x = 2/3 (the channel's
  quint eigenvalue 1 - 3x/2 crosses zero — name any derivation step that could degenerate there),
  a point near 1 (faithfulness degeneration), and at least two points strictly below 1/2
  (infeasibility side). Identity level (matrix residuals), not aggregates. Name every untested
  regime in the verdict.
- **(7c) Anchoring ban.** BEFORE opening the proposer's scripts, artifact tables, or JSON: derive
  from the frozen conventions your OWN general-x complement, ansatz, intertwining solution,
  defect Choi, block reduction (your own basis construction), elimination, and feasible region.
  Only then read the proposer's material and compare. Flag any notational coincidence.
- **(7d) No frozen-input immunity.** The P1-reviewed calibration facts (C1-C6) are reviewed scope
  for x = 1/2 values only; every general-x statement is NEW and must be re-verified. The
  commission's own displayed formulas (e.g. the expected complement block form) are hypotheses to
  check, not truths.
- **(7e) Standing failure-mode list (check every one):** dropped/extra normalization factors;
  type/dimension mismatches; undefined terms of art; partial objects silently substituted for
  full ones (a PROPER subset of PSD constraints, a subspace of the Choi, leading-minor-only PSD
  tests); numerics validating values while the printed derivation is broken; sign/transpose/
  Choi-leg convention drift; solver-status laundering (should be moot — the work claims to be
  solver-free; verify that claim); rounding-then-asserting exactness; branch loss in symbolic
  `solve`/elimination (the failure the executor's own aborted runs hint at).
- **(7f) Value-vs-formula decoupling.** Your numbers must come from an INDEPENDENT
  implementation (verification); additionally reproduce the proposer's scripts unchanged with
  writes redirected (reproduction); label which established what.
- **(7g) Quantifier hygiene.** Every term in the reviewed claims resolves to a definition:
  "feasible region", "forced/unique", "rank-one form", "solver-free certificate", "x_max = sup",
  "covariant/equivariant", "adjoint preserving". Check resolvability in the reviewed documents.

## Deliverables

1. Immutable report `artifacts/whgap_p2_review_20260728.md`: per-claim verdicts for 1-9 above;
   your OWN derivation results (residual family, blocks, region); the explicit untested-regime
   list; and a licensing statement of the exact form: "this review does / does not open the
   completion gate for <statement>, at tier <CERTIFIED* / PROVED>, with scope <...>" — including
   separately (i) the exact feasible-region theorem for the covariant family, (ii) the
   three-point exact certificates, (iii) the twirling ingredients, and (iv) the generic-theorem
   application (which the executor did NOT claim; list its remaining obligations).
2. Reviewer's own scripts + logs under `artifacts/logs_whgap_p2_review_20260728/` with
   SHA256SUMS.txt; proposer reproduction with writes redirected into that directory.
3. Append a dated entry to the node's `Adversarial reviews` section linking the report. No
   status writes anywhere.
4. Run `tools/proof_dag_check.py --problem werner-holevo-gap` and `tools/literature_check.py`
   with the pinned interpreter (both must exit 0).
5. Print `FINAL: REVIEW-COMPLETE` or `FINAL: FAILED — <reasons>`.

**Executor:** codex CLI, one sequential session, workspace-write, NO network; Python
`"C:<home>/cpython3119/python.exe"` (CPython 3.11.9; pinned: numpy 1.26.4, scipy 1.14.1,
sympy 1.13.1, mpmath 1.3.0, cvxpy 1.6.0, scs 3.2.7). Budget <= 75 min; stop-loss on two
info-free cycles or budget breach.

