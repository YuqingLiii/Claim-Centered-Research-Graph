# Fable-5 decision-layer cross-stack audit of the WHGAP core proof (2026-07-28)

**Auditor:** the decision layer itself (Claude Fable 5) — a DIFFERENT model/vendor stack from the
two codex (gpt-5.6-sol) implementations it audits. Commissioned directly by the lead
("你再自己对核心证明做一个审计"). Scope: the P2 certificate core (codex-authored, R2-reviewed)
and the P4 assembly (decision-layer-authored, R3-reviewed — for P4 this is a self-audit and is
labeled as such; it opens no gate).

**Verdict: ALL PARTS PASS.** Every load-bearing claim of the core proof was reproduced by (i)
hand-derivation and (ii) a third, independently written implementation
([tools/whgap_fable_audit.py](../tools/whgap_fable_audit.py); log
[fable_audit.log](logs_whgap_fable_audit_20260728/fable_audit.log)) that shares no code or basis
choices with either codex implementation.

## Hand-derivation results (in-context, no CAS)

1. **Intertwining equations re-derived from scratch** via the decomposition
   Y = (t/3)I + S + T: scalar 3(1-x)p + x(3c1+c2+c3) = 1; quint -(x/2)(c2+c3) = 1-3x/2;
   vector 4qk + (x/2)(c2-c3) = 1-x/2 — identical to the executor's displayed system. The naive
   coefficient-matching pitfall ({t·I, Y, Y^T} are not independent) was identified and resolved;
   the executor's system is the correct one.
2. **Forced-point formulas verified by hand:** p = 1/3 identically; c2 = (7x-4)/(3x);
   q = (1/3)sqrt(2(1-x)/x); Zhu–Wang's (1/3, sqrt2/3, 2/3, -1/3, -2/3) recovered at x = 1/2.
3. **Theorem 3.3's own proof audited** (the paper is one day old — the largest external risk):
   Lemma 3.5's block quadratic-form expansion checks out; Lemma 3.6 follows by the variational
   characterization <W, A^{-1}W> = sup_V [2Re<W,V> - <V,AV>] plus congruence domination — sound.
   The BKM bridge (Lemma 3.2, published [BGSW25]) and tensorization (published [HRSF22]) are
   peer-reviewed citations.
4. **Assembly identities re-derived:** I(R;B) - I(R;E) = 2·Ic on a pure tripartite state;
   admissibility supp(ω_RB) ⊆ supp(ω_R ⊗ ω_B); orientation environment-over-receiver throughout.

## Machine audit (tools/whgap_fable_audit.py, store-python sympy, 75 s total)

- **A (construction):** Kraus identities exact; Λ_x from Kraus = closed form on all matrix
  units; intertwining residual ≡ 0 symbolically in x at the forced point; the 27×27 defect Choi
  is real symmetric and k-free (even powers only).
- **B (uniqueness, auditor's own route — different from both codex proofs):** for v in
  ker C(forced), g_v(s1,s2) = v^T C(s1,s2) v must be ≥ 0 under PSD; 17 of the kernel quadratics
  are concave with max 0 at the forced point, so PSD forces their max loci; the joint gradient
  system has the UNIQUE solution (s1,s2) = (2(1-x)/(3x), (5x-2)/(3x)) — verified at
  x = 5/9, 4/7, 3/4.
- **C (region):** symbolic kernel dimension 19; 8×8 range compression computed; exact PSD grid:
  NOT-PSD at x = 2/5, 49/100, 499/1000; PSD at x = 1/2 (rank 3), 501/1000, 26/51, 13/25, 5/9,
  4/7, 3/5, 2/3, 3/4, 9/10, 99/100 (rank 8) — boundary bracketed at 1/2 ± 10^-3 exactly;
  explicit exact negative eigenvalue -102/1225 at x = 49/100.
- **D (Zhu–Wang anchor):** the x = 1/2 Choi equals (2/9)·Σ_μ Choi(G_μ·G_μ†) ENTRYWISE (my own
  G_μ construction from their Eq. (4.19)); rank exactly 3; the three certificate points
  x = 26/51, 4/7, 3/4 are exact-PSD rank 8.
- **E (assembly-side):** Kraus completeness; Λ_x(I) = I; Λ_x^c(I) = diag(3(1-x),x,x,x);
  physics cross-check: max-mixed-input coherent information crosses zero near x ≈ 0.39
  (+0.0667 at 0.35, -0.0138 at 0.40) — so Q > 0 for x ≲ 0.39, consistent with (and independent
  of) the theorem; the certificate's failure below 1/2 is necessary at least below ~0.39.

## What this audit does and does not change

- P2's certificate core: now verified by a third independent stack (hand + Fable-authored CAS
  route with different bases and a different uniqueness argument). This addresses the R2-listed
  untested regime "no second independent exact-algebra stack beyond SymPy" only partially (same
  CAS library, different author/model/route).
- P4's assembly: my re-derivations corroborate it, but I authored the note — this section is
  self-audit and opens no completion gate (rule 2/6). The R3 review remains P4's gate.
- No status changes are made on the basis of this audit; it is additional evidence recorded on
  the nodes.

## Provenance

- Script: `tools/whgap_fable_audit.py` (one auditor-bug fixed mid-run and documented: `.H` on
  symbolic sqrt matrices produced unresolved conjugates; replaced by `.T`, valid since all
  Kraus matrices are real on 0 < x < 1; and the first uniqueness strategy — raw-basis
  negative-square minors — found none, exposing that the negative-square structure lives in
  reduced bases; replaced by the concave-kernel-quadratic route above).
- Log: `artifacts/logs_whgap_fable_audit_20260728/fable_audit.log` (ALL PARTS PASS).
- SHA-256 manifest: `artifacts/logs_whgap_fable_audit_20260728/SHA256SUMS.txt`.

