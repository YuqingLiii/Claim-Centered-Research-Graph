# WHGAP review commission R4 — independent adjudication of the P3 Q>0-onset work (2026-07-29)

**Node (rule 8a):** `WHGAP.qpositive-onset`. **This review is the rule-6 completion gate** for
that node. **Runs ONLY after** `WHGAP_COMMISSION_P3_20260729.md` has produced its artifact
`artifacts/whgap_p3_qonset_20260729.md`.

**Reviewer identity (rules 2/6):** a FRESH codex session that did not author the reviewed work
and is given no desired outcome. Mandate: adjudicate correctness, completeness, and licensing.
The reviewer writes NO node statuses; it produces an immutable report. Status application is a
separate decision-layer step citing the report.

## Step -1 — mandatory pre-task reload

Execute `research/PRETASK_RELOAD_PROMPT.md` FIRST with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.qpositive-onset`, ROLE = reviewer.
No work before its PRE-ACTION REPORT (including your independence statement). Disk overrides
this commission on any conflict.

## Reviewed objects (frozen scope)

- Artifact: `artifacts/whgap_p3_qonset_20260729.md`
- Scripts: `tools/whgap_p3_*.py`
- Logs: `artifacts/logs_whgap_p3_20260729/` (+ SHA256SUMS.txt)
- Node: `channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.qpositive-onset.md`
- Spec: `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P3_20260729.md` may be read
  as the problem spec; every mathematical claim in it must be independently re-verified (7d).
- Literature (context): local RK24 PDF
  `channel-capacity/literature/papers/roofeh-karimipour-2024-noisy-werner-holevo/arxiv_2310.15353.pdf`
  (§5.3–5.4). RK24's own numerics are a CLAIM, not ground truth.

## Claims under adjudication (verdict each: PASS / MINOR / MAJOR / GAP)

1. **D1 closed form:** `Lambda_x(pi) = pi`; `Lambda_x^c(pi) = diag(1-x, x/3, x/3, x/3)`;
   `Ic(pi,x) = log2 3 + (1-x)log2(1-x) + x log2(x/3)` (bits). Re-derive from the frozen Kraus
   family yourself.
2. **D2 monotonicity lemma:** `d/dx Ic(pi,x) = log2(x/(3(1-x)))`, strictly negative for
   x < 3/4; uniqueness of the root x_1 on (0, 3/4). Check the derivative computation and the
   sign argument exactly.
3. **D3 certified root bracket:** the interval-arithmetic bracketing of x_1 (width <= 1e-30):
   verify the endpoint sign evaluations with YOUR OWN independent high-precision computation
   (different code path; state precision and rounding discipline), and confirm the printed
   30-digit value.
4. **D4 positivity certificates:** the three interval certificates at x = 1/4, 1/3, 39/100 —
   re-evaluate independently; confirm each rational lower bound is valid.
5. **The lower-bound principle usage:** `Q >= sup_rho Ic` applied pointwise — confirm the
   citation scope (single-letter coherent information as a capacity lower bound) and that no
   step confuses bits/nats.
6. **S1 ceiling scan methodology:** parameterization covers ALL density matrices (no silent
   restriction of rank or realness); restart counts and structured starts as commissioned;
   the pure-state floor Ic = 0 handled correctly (outputs isospectral for pure inputs —
   verify this fact yourself); the reported maxima and argmax characters are reproducible at
   spot-check level (rerun at >= 2 grid points with your own optimizer).
7. **S2 Hessian threshold:** the local-maximality analysis at pi and the comparison x_H vs
   x_1 — verify the second-variation computation at one rational x on each side.
8. **S3 two-letter probe:** families searched as commissioned; the superadditivity comparison
   baseline correct (2x best single-letter at the SAME x); any claimed positive re-verified
   exactly, any null bounded honestly (report restart counts and time cap adherence).
9. **G2 interpretation licensing:** does the artifact's chosen interpretation follow from the
   pre-registered cases? Separately license: (i) the EXACT package — closed form + lemma +
   root bracket + certificates ("Q > 0 on (0, x_1)" with certified x_1); (ii) the NUMERICAL
   package — the single-letter ceiling picture above x_1 and the two-letter null; state for
   each: "this review does / does not open the completion gate for <statement>, at tier
   <CERTIFIED* / PROVED>, with scope <...>".

## Mandatory review-quality checklist (rule 7, embed-and-execute; a review missing any item opens NO gate)

- **(7a) Type audit.** Every displayed identity: domains, codomains, dimensions; entropy
  conventions (base, sign); density-matrix parameterization well-defined (positivity, trace);
  interval-arithmetic objects (what exactly is bounded, with what rounding guarantees).
- **(7b) Regime-complete identity gates.** With YOUR OWN implementation: check Ic(pi,x) at
  x in {1/4, 39/100, x just below and above the bracket, 49/100}; verify the pure-state
  Ic = 0 fact at 3 random pure states at 2 different x; test the optimizer floor at one x
  above x_1 and confirm D4 at one point below. Name every untested regime (e.g. blocklengths
  >= 3, x outside (0, 1/2), non-covariant multi-letter ansätze).
- **(7c) Anchoring ban.** BEFORE opening the proposer's scripts, artifact tables, or logs:
  derive the closed form, the derivative, and your own root bracket from the frozen
  conventions; freeze them to disk with hashes; only then compare.
- **(7d) No frozen-input immunity.** The P1/P2-reviewed facts are in scope only as reviewed
  (x=1/2..1 side); everything on (0, 1/2) is NEW. The commission's displayed formulas are
  hypotheses to check.
- **(7e) Standing failure-mode list (check every one):** dropped/extra normalization
  (log base slips are THE standing risk here); type/dimension mismatch; undefined terms
  ("certified", "floor", "restart"); partial objects for full ones (a restricted input
  parameterization silently standing in for all states — check rank coverage); numerics
  validating values while the printed derivation is broken; sign/orientation drift (Ic vs
  -Ic in minimizers); solver-status laundering (optimizer non-convergence counted as
  evidence); rounding-then-asserting exactness (floating point presented as interval-certified).
- **(7f) Value-vs-formula decoupling.** Your numbers from YOUR implementation = verification;
  redirected reruns of proposer scripts = reproduction; label which established what.
- **(7g) Quantifier hygiene.** "onset", "certified region", "ceiling", "floor", "null",
  "sup over all inputs" — each resolves to a definition in the reviewed documents; the final
  statements' quantifiers (for every x in ..., there exists rho ...) are exactly what the
  evidence supports.

## Deliverables

1. Immutable report `artifacts/whgap_p3_review_20260729.md`: per-claim verdicts 1–9; your
   frozen pre-reading derivations (or hash + link); untested-regime list; the two licensing
   statements of claim 9 in the required form.
2. Reviewer scripts + logs under `artifacts/logs_whgap_p3_review_20260729/` with
   SHA256SUMS.txt (including the anchoring-boundary hash file); redirected proposer
   reproduction included.
3. Append a dated entry to the node's `Adversarial reviews` section linking the report. NO
   status writes anywhere.
4. Run `tools/proof_dag_check.py --problem werner-holevo-gap` and
   `tools/literature_check.py` with the pinned interpreter (both must exit 0).
5. Print `FINAL: REVIEW-COMPLETE` or `FINAL: FAILED — <reasons>`.

**Executor:** codex CLI, one sequential session, workspace-write, NO network; Python
`"C:<home>/cpython3119/python.exe"` (CPython 3.11.9; pinned stack + mpmath 1.3.0 +
pypdf 6.14.2). Budget <= 60 min; stop-loss on two info-free cycles or budget breach.

