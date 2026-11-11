# External audit #2 (ChatGPT Pro, via lead) — the PAPER draft itself — 2026-07-29

Provenance: the lead submitted the paper draft (main.pdf v1.1) for a hostile audit; verdict
pasted back as a screenshot, transcribed here.

## Verdict

- **Mathematics: PASS, high confidence.** The auditor re-derived from definitions — complement
  channel, lift, the full 27×27 defect Choi — with SYMBOLIC (not floating-point) spot checks:
  intertwining equations correct; both negative-square forcing identities correct; the three
  eigenvalue branches with multiplicities 19/5/3 correct; x=1/2 degenerates to the Zhu–Wang
  rank-3 certificate; x<1/2 negative eigenvalue confirmed; the theorem-invocation direction
  (CP defect ⇒ P^(1)=Q^(1)=0 at all blocklengths) correct; the x=1 self-complementarity
  argument correct. No counterexample found. Supports the main theorem on [1/2,1].
- **As a manuscript: Major Revision.** Core criticism (verbatim gist): "'定理大概率是真的'与
  '论文已经给出了合格证明'是两回事。最核心的新计算几乎是直接宣告的,而不是证明出来的" — the
  central new computations (uniqueness forcing, the closed-form spectrum) are DECLARED with a
  pointer to the verification statement, not PROVEN in the text. A math venue requires the
  derivations to be present and human-checkable.

## Decision-layer assessment

The criticism is correct and was a deliberate but wrong trade-off in v1 (letter-style
compression + "verified symbolically, see §6"). The proof CONTENT exists across the campaign
artifacts (R2/R3 reviews, Fable audit, block data); it must be moved INTO the paper:

Revision plan (paper v2, registered as the P5 work item):
1. **Appendix A (entrywise defect formula):** derive and PRINT the closed-form general-x
   entrywise formula for Delta_x(tau) — the analog of Zhu–Wang's Eq. (A.2) — from which
   Prop. 3.2's forcing identities become displayed hand computations.
2. **Appendix B (spectrum proof):** spin-adapted reduction (multiplicities 1,3,2,1), the four
   reduced blocks as explicit small matrices, the elimination to the unique point, explicit
   closed-form eigenvectors for the multiplicity-5 and multiplicity-3 branches, plus the
   annihilating-polynomial + trace-multiplicity argument — every step displayable and
   checkable without trusting any script.
3. **§4 expansion:** inline the support/tensorization details (the P4 note's O1–O7, already
   R3-reviewed) instead of "exactly as in [ZW]".
4. Keep the verification statement as a supplement, but the paper must stand alone.

This is the FIFTH independent verification layer to confirm the mathematics with zero errors;
the gap is purely proof-presentation.

