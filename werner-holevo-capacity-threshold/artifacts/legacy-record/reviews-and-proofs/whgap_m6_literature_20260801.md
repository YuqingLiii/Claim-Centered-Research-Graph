# WHGAP M6 — BGSW25 literature ingestion (2026-08-01)

One line: R11 minor **m6** is discharged — Belzig–Gao–Smith–Wu, "Reverse-type Data Processing
Inequality" (arXiv:2411.19890v3; Commun. Math. Phys. **406**, 295 (2025)) is now in the
channel-capacity library at
[`channel-capacity/literature/papers/belzig-gao-smith-wu-2025-reverse-dpi/`](../channel-capacity/literature/papers/belzig-gao-smith-wu-2025-reverse-dpi/README.md)
(local PDF `arxiv_2411.19890.pdf`, 32 pp., SHA-256 below) with the catalog entry added, and the
cBKM ⟹ cRE bridge is identified in the source as **Lemma 4.1** (§4.1, p. 9), quoted on the page.

Provenance and checks:

- Identity verified against the commission: title, all four authors (Belzig, Gao, Smith, Wu), and
  the journal reference CMP 406:295 (2025) all match the arXiv listing and the PDF title page.
- Statement read from the LOCAL PDF (not from the abstract page): Lemma 4.1 is the two-sided
  equivalence between relative-entropy domination `c₁D(N(ρ)‖N(σ)) ≤ D(M(ρ)‖M(σ)) ≤ c₂D(N(ρ)‖N(σ))`
  and BKM-form domination `c₁g_{N(σ)}(N(X)) ≤ g_{M(σ)}(M(X)) ≤ c₂g_{N(σ)}(N(X))`, proved via the
  integral representation `D(ρ‖σ) = ∫₀¹∫₀^s g_{ρ_t}(ρ−σ)dt ds` (their eq. (15)).
- Three scope gaps between the displayed lemma and the form WHGAP consumes are recorded on the page
  rather than glossed: (1) we use only the `c₁ = 1`, (ii) ⟹ (i) direction; (2) **the displayed lemma
  has no reference system** — the *complete* orders follow by applying it to `(id_R ⊗ N, id_R ⊗ M)`
  for each finite `R`, which is why our chain cites ZW Lemma 3.2 (the complete form) rather than
  this lemma directly; (3) support-condition vs. the "both outputs faithful" hypothesis in `thm:zw`.
- Non-load-bearing context also recorded: §3 (impossibility of an absolute reverse DPI), Lemma 4.2
  (`ρ ≤ cσ ⟹ g_ρ ≥ g_σ/c`, explicitly NOT on our path), §6 (their own less-noisy/non-degradable
  construction).
- Local roles listed: node `WHGAP.zero-capacity-application` (P4), `WHGAP.goal` (the m6 obligation),
  Lean `Interface.lean` field `zw_hrsf_zero` and `zero-capacity-application.lean`, and the five
  `\cite{BGSW25}` sites in `paper/main.tex`.
- Closeout: `tools/literature_check.py` exit 0 (52 papers across 5 libraries, schema v1);
  `tools/proof_dag_check.py --problem all` exit 0. `catalog.json` diff is +31 lines only (no
  reformatting of existing entries).
- No node, index, or DAG markdown was edited (single-writer deviation respected). Evidence tier:
  this is a literature ingestion, not a mathematical status change; nothing is promoted.

SHA-256 (LF-irrelevant, binary):

```
6c59944e6a037d283c0a4a6ad6a48e3bce044e4cd077b5d769ac8a3b6c9948db  channel-capacity/literature/papers/belzig-gao-smith-wu-2025-reverse-dpi/arxiv_2411.19890.pdf
```

