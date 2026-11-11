# WHGAP commission LEAN-4 / R9 / M6 — clearing the registered obligations (frozen 2026-08-01)

Commissioner: decision layer. Lead directive 2026-08-01: complete the four registered
items (rank_Cmat_half review debt; residual (b); m6 BGSW25 ingestion; R9 on P15-A;
checker harmonization — the last is decision-layer-executed separately). Three PARALLEL
executors (disjoint file scopes) + one chained reviewer.

Standing rules for all: pre-task reload ({PROBLEM_DIR} = channel-capacity/werner-holevo-gap,
{NODE_ID} as stated, ROLE as stated); single-writer deviation (no node/index/DAG
markdown); scoped paths only; never sorry / native_decide (Lean tracks); evidence tier
NUMERICAL, pending-review.

---

## Track G — LEAN-4 WP-G: residual (b), the complex-spectra identification
NODE_ID = WHGAP.goal. Scope: the Lean project + artifacts/logs_whgap_lean4_20260801/ +
a new dated section in artifacts/whgap_lean3_20260801.md (or a new whgap_lean4 report).

Target: close Trust.lean residual (b). The §6 witness outputs are explicit COMPLEX
matrices: ρ_ε = (1−ε)P_ψ + εP_ψ̄ with ψ = (e₁+ie₂)/√2 (entries of P_ψ are ±1/2, ±i/2);
Λ(ρ_ε) is the explicit 3×3 complex Hermitian matrix; Λ^c(ρ_ε) the explicit 4×4 (β under
hβ : β² = x(1−x)/2). Prove over ℂ:
- `specB_charpoly` : (Λ(ρ_ε)).charpoly = (X − ((1−ε)(1−x/2)))·(X − (ε(1−x/2)))·(X − x/2)
  — matching IcScalar's B-list;
- `specE_charpoly` : (Λ^c(ρ_ε)).charpoly = the quartic Π over IcScalar's E-list, i.e.
  (X² − (1−x/2)X + 2x(1−x)ε(1−ε))·(X − x(1−ε)/2)·(X − xε/2) — state it with the
  QUADRATIC factor (the λ± roots involve a square root; the charpoly-level statement
  needs none, which is exactly why this level was chosen).
Use the channel definitions from Support/Channel.lean where they apply over ℂ (LamK is
R-generic — check; if it is real-scalar-bound, define the complex instance minimally and
verify against the closed form). Then update Trust.lean's residual block: (b) CLOSED AT
CHARPOLY LEVEL, with the remaining glue named explicitly — "same charpoly ⟹ same
vnEntropy" for complex Hermitian matrices is STILL not in Lean (the real-symmetric
entropy layer does not apply verbatim); README updated to match, per §7.9. sympy
pre-verification first (both charpolys symbolically in (x, ε, β)). Budget ≤ 90 min.
Return {status, summary, built, sorry_count, axioms_clean, report_path}.

## Track R9 — the owed rule-7 review of P15-A
NODE_ID = WHGAP.pure-anchor-order. ROLE = reviewer (fresh; you did not author P15-A).
Scope: your report artifacts/whgap_r9_review_20260801.md + tools/whgap_r9_*.py + logs
into artifacts/logs_whgap_p15a_20260730/ prefixed r9_ (additive).

Execute the R9 section of
[WHGAP_COMMISSION_P15A_P16A_20260730.md](WHGAP_COMMISSION_P15A_P16A_20260730.md)
against the COMPLETE on-disk package: note
notes/WHGAP_P15A_STRICTNESS_20260730.md (638 lines, all gates run), logs under
artifacts/logs_whgap_p15a_20260730/ (post-hoc manifest
SHA256SUMS_posthoc_decision_layer.txt — the run died at closeout; treat the manifest
gap as a recorded closeout defect, not fresh suspicion). Key items per the frozen menu:
re-derive the decomposition identity Σ p_u G(ψ_u, σ) = −I_c(σ) by your OWN route; re-find
or re-verify the x = 2/5 violating pair with your OWN optimizer and your OWN I_c code
(≥ 40 digits); audit the G-A0 verdict (strictness demonstrated: G < 0 while I_c(σ*) < 0
and local max ≈ 0) and the G-A+ non-trigger; audit A3 for the exact over-claim R8
MAJOR-3 flagged; audit A4's strip statements and the calibration gate. Licensing menu as
frozen there. Budget ≤ 90 min. Return {verdict, summary, majors, minors, report_path}.

## Track M6 — BGSW25 literature ingestion
NODE_ID = WHGAP.goal (obligation registered in the LEAN-1.1/R11 record). ROLE = executor.
Scope: channel-capacity/literature/ ONLY (catalog.json + a new
papers/belzig-gao-smith-wu-2025-reverse-dpi/ directory) + a one-line report.

The paper: P. Belzig, L. Gao, G. Smith, P. Wu, "Reverse-type data processing
inequality," Commun. Math. Phys. 406, 295 (2025) — the sole source of the cBKM ⟹ cRE
bridge (cited as ZW Lemma 3.2's origin; load-bearing for the zw_hrsf_zero interface).
Find the arXiv version (search; verify authors/title match), download the PDF into the
paper directory, write the README.md page following the shape of the existing entries
(e.g. papers/hirche-rouze-stilckfranca-2022-*/README.md): bibliographic block, one-para
summary, THE SPECIFIC RESULT WE USE (the reverse-type DPI / bridge statement — quote its
number and statement from the PDF), and local-role notes (which WHGAP nodes lean on it).
Add the catalog.json entry (schema v1 — copy an existing entry's fields exactly).
Closeout: tools/literature_check.py exit 0. Budget ≤ 30 min.
Return {status, summary, arxiv_id, report_path}.

---

## R14 (chained after Track G): review of rank_Cmat_half + WP-G
NODE_ID = WHGAP.goal. ROLE = reviewer (fresh). Scope: report
artifacts/whgap_r14_review_20260801.md + tools/whgap_r14_*.py + logs prefixed r14_.

1. **rank_Cmat_half** (LEAN-3.2, flagged as unreviewed executor work): re-derive the
   factorization route yourself (Cmat(1/2) = ((1/18)V3R)·V3Rᵀ; rank bounds via
   rank_mul_le + rank_of_isUnit on V3Rᵀ·Cmat(1/2)·V3R = (128/9)·𝟙₃); verify the three
   new declarations' statements against the paper's Thm 3.3(2) rank claim; check the
   glosses in all four places match what is proved; independently compute
   rank(Cmat(1/2)) with your own exact code.
2. **WP-G**: reproduce the build; verify both charpoly statements against IcScalar's
   lists symbol by symbol; own sympy re-derivation of both charpolys; audit the updated
   Trust/README residual wording for over/under-claim (the complex-entropy glue must
   still be named as open).
3. Standard §7.10: axioms, forbidden scan, freeze-check, lean_dag_check.
Menu: (A) "rank_Cmat_half and the WP-G package are licensed as recorded; the residual
display is accurate" / (B) FINDINGS. Budget ≤ 60 min.
Return {verdict, summary, majors, minors, report_path}.

