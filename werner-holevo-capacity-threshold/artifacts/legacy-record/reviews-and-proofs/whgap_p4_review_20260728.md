# WHGAP P4 independent review - 2026-07-28

Node: `WHGAP.zero-capacity-application`

Reviewed object: `channel-capacity/werner-holevo-gap/notes/WHGAP_P4_ZERO_CAPACITY_NOTE_20260728.md`

Role: fresh independent reviewer

## PRE-ACTION REPORT

- Target node and disk status: `WHGAP.zero-capacity-application`, `CONJECTURED` with
  `pending-review:`.
- Independence: I did not author the reviewed work and was given no desired outcome.
- Highest licensable evidence tier: `PROVED`; the protocol permits an independent checker to
  write it, but the commission reserves status application to a later decision-layer step, so
  this review writes no status.
- Gate: adjudicate claims 1-9 and demonstrably execute rule 7a-7g, including a pre-reading
  hash-frozen assembly outline.
- Deliverables: this immutable report; scripts, logs, outline, and hashes under
  `artifacts/logs_whgap_p4_review_20260728/`; one dated node-review link; two green validators.
- Protocol conflict reported before work: `research/PRETASK_RELOAD_PROMPT.md` names the
  WindowsApps Python for closeout, while the disk commission and user instruction require
  `C:<home>/cpython3119/python.exe` for every Python invocation. I used the latter pinned
  CPython 3.11.9. No other conflict was found.

## Executive verdict

The Theorem is mathematically complete on \(1/2\le x<1\). The note has three minor
provenance/exposition defects, none of which creates a mathematical gap:

1. (F4) was passed in R2 claims 1, 6, and 9 but is not literally named in the exact scopes of R2
   licensing statements 1-3; I therefore reopened and verified it rather than granting frozen
   input immunity.
2. (F1) calls the lift "real-linear," while Zhu-Wang Theorem 3.3 requires a complex-linear map.
   The displayed formula is complex-linear, and the exact matrix-unit audit verifies
   \(J(iE_{jk})=iJ(E_{jk})\) for all nine units, but the sentence should say "complex-linear."
3. O5 names a full-rank \(\pi_R\), whereas Zhu-Wang Corollary 3.1 uses the purification marginal
   \(\psi_R\). The note's support pair is still valid and yields the same cancellation if the
   same \(\pi_R\) is used on both outputs, but "the pair used by [ZW]" is imprecise. O4 likewise
   introduces an unnecessary reference \(R\); setting \(R\) trivial recovers the exact
   private-information convention.

The Corollary's \(x=1\) endpoint is not locally adjudicated: RK24 has no local PDF and was
required by the commission to be treated as cite-only. Thus the full closed-interval Corollary
is capped at `CERTIFIED*`, with that endpoint caveat. The actual historical gap
\((1/2,4/7)\) is already closed by the PROVED-tier Theorem and does not depend on RK24.

## Anchoring-ban execution (7c)

Before opening the reviewed note, I read only Zhu-Wang Theorem 3.3 and the R2 claim-9 obligation
list, wrote my own required-assembly outline, and froze it:

- Outline:
  [`FROZEN_PRE_READING_OUTLINE.md`](logs_whgap_p4_review_20260728/FROZEN_PRE_READING_OUTLINE.md)
- SHA-256:
  `d601a830e25043b8e785e45f5b82e6512572ef8be665f76e755771c1c2cf8934`
- Boundary record:
  [`ANCHORING_BOUNDARY_SHA256.txt`](logs_whgap_p4_review_20260728/ANCHORING_BOUNDARY_SHA256.txt)

Item-by-item comparison:

| Independent demand | Note location | Result |
|---|---|---|
| State \(x\)-range, all \(n\), one-shot conventions, regularizations | Theorem and O6 | Met |
| Establish CPTP pair and both partial traces | O1 | Met; independent all-nine-unit check passed |
| Establish tensor-power complement | O2 | Met by explicit reordered Stinespring isometry |
| Check every Theorem 3.3 hypothesis | H1-H3 | Met, with the real-/complex-linearity wording defect above |
| Resolve complete-reference/support quantifier | O3 | Met |
| Tensorize with environment-over-receiver orientation | O6 | Met |
| Private-information support, termwise comparison, zero floor | O4 | Met; unnecessary \(R\) is harmless when taken trivial |
| Coherent-information support, comparison, pure-input floor | O5 | Met; \(\pi_R\)/\(\psi_R\) attribution is imprecise |
| Regularize and exclude \(x=1\) from this theorem | O6-O7 | Met |
| Keep \(x=1\) and \(x<1/2\) outside the assembly | Corollary/caveats | Met |

The outline additionally demanded an explicit all-unit check that the stated Kraus family acts as
the printed \(\Lambda_x\), and an explicit coherent-information relative-entropy identity. The
note treats the former as a frozen channel formula and cites Zhu-Wang Corollary 3.1 for the
latter. I independently checked the Kraus action and verified the cited corollary's complete
argument. The note contains no substantive step that the outline would forbid or fail to
license.

## Claim-by-claim adjudication

1. **PASS - Theorem statement well-posedness.** The theorem uses Zhu-Wang's
   \(P^{(1)}(\Lambda^{\otimes n})\) and \(Q^{(1)}(\Lambda^{\otimes n})\) conventions, quantifies
   every integer \(n\ge1\), and states \(x\in[1/2,1)\) unambiguously. The PDF's Theorems 1.1 and
   4.3 use exactly the same all-blocklength formulation and then regularize.

2. **MINOR - (F1)-(F4) quotes and R2 scope.** F1-F3 occur in the P2 artifact and are within R2
   licensing statement 1's scope:
   "within the frozen five-parameter real \(O(3)\)-equivariant adjoint-preserving ansatz, the
   defect Choi is PSD exactly for \(1/2\le x<1\), at the unique displayed residual point."
   The three exact gates are within statement 2's scope:
   "\(x=26/51,4/7,3/4\): exact lift parameters, all four spin blocks, solver-free PSD
   congruences, and direct-\(27\times27\)/block spectrum linkage." No use is made of statement
   3 beyond its narrow twirling scope. F4 is established in P2 and expressly passed by R2 claims
   1, 6, and 9, but the final licensing statements 1-3 do not literally name the faithfulness
   formula. Under 7d I treated the note's "R2-licensed PROVED" label for F4 as too broad and
   reopened it. Exact symbolic computation gives
   \(\Lambda_x(I_3)=I_3\) and
   \(\Lambda_x^c(I_3)=\operatorname{diag}(3(1-x),x,x,x)\). The same computation verifies the
   displayed forced \((p,q,c_1,c_2,c_3)\), complex linearity, adjoint preservation, and all 81
   entries of \(J_x^\dagger\Lambda_x^c-\Lambda_x\) as zero.

3. **MINOR - (H1)-(H3) hypothesis check.** The local PDF's Theorem 3.3 requires
   finite-dimensional quantum channels, \(M(I)\succ0\), \(N(I)\succ0\), a linear
   adjoint-preserving \(J:L(H_B)\to L(H_E)\), \(J^\dagger N=M\), and complete positivity of the
   outer defect. H1-H3 cover every item, with no range weakening. The only defect is that F1
   says "real-linear"; the displayed formula and independent audit establish the required
   complex linearity. Remark 3.4 confirms that the required CP is the outer map
   \(L(H_A)\to L(K_B)\), not merely pointwise positivity.

4. **PASS - O1.** Exact computation verifies
   \(\sum_aK_a^\dagger K_a=I_3\), equality of the Kraus action with the printed
   \(\Lambda_x\) on all nine matrix units, \(V_x^\dagger V_x=I_3\), and both partial traces on
   all nine matrix units. The resulting \(N\) is exactly the displayed chosen complement.

5. **PASS - O2.** After the canonical permutation
   \((B\otimes E)^{\otimes n}\simeq B^{\otimes n}\otimes E^{\otimes n}\), the constructed
   isometry has receiver channel \(M^{\otimes n}\) and environment channel \(N^{\otimes n}\).
   This is an exact chosen complement, so no uniqueness theorem is needed. The note's additional
   "unique up to environment isometry" sentence invokes the standard complementary-channel
   freedom; Zhu-Wang Corollary 3.1 only requires a complementary channel and is insensitive to
   an isometric environment relabeling. There is no gap between "a complement" and "the
   complement" in the chain.

6. **MINOR - O3-O5.** O3 preserves every finite reference and every support-admissible pair.
   O4 correctly discards \(p_u=0\), derives \(p_u\rho_u\preceq\bar\rho\), compares Holevo terms
   in the environment-over-receiver orientation, and uses the singleton floor. The added
   reference \(R\) is unnecessary; taking it trivial gives exactly the PDF proof and the
   definition of \(P^{(1)}\). O5 correctly handles rank-deficient inputs by choosing the
   purification reference on the Schmidt support and supplies the pure-input \(I_c=0\) floor.
   Zhu-Wang Corollary 3.1 uses
   \((\psi_{RA^n},\psi_R\otimes\rho_{A^n})\), not the note's named
   \((\phi_{RA^n},\pi_R\otimes\rho_{A^n})\); either full-rank second reference factor gives the
   support inclusion and cancels from the relative-entropy difference, so this is a citation/
   notation defect rather than a logical gap.

7. **PASS - O6.** The PDF's Section 3.1 states
   \(M_1\succeq_{\rm cRE}N_1,\ M_2\succeq_{\rm cRE}N_2\Rightarrow
   M_1\otimes M_2\succeq_{\rm cRE}N_1\otimes N_2\). The note preserves the required
   orientation
   \((\Lambda_x^c)^{\otimes n}\succeq_{\rm cRE}\Lambda_x^{\otimes n}\).
   Its displayed regularizations are the private and quantum capacity regularizations cited in
   Zhu-Wang.

8. **PASS with cite-only endpoint - O7 and Corollary.** Exact F4 gives loss of faithfulness at
   \(x=1\), so Theorem 3.3 hypothesis 1 and Lemma 3.2 fail there. The note does not smuggle
   \(x=1\) into the Theorem. It clearly labels RK24 as used only for the endpoint remark. Because
   RK24 has no local PDF, the statements "antidegradable for \(x\ge4/7\)" and hence \(Q=0\) at
   \(x=1\) are cite-only and were not independently verified here. Conditional on that citation,
   the Theorem plus the endpoint gives \(\{x:Q(\Lambda_x)=0\}\supseteq[1/2,1]\).

9. **PASS - no-overclaim audit.** The caveats correctly say that there is no licensed full
   averaging/WLOG lemma, HRSF22 has no locally audited copy, and \(x<1/2\) is untouched. The note
   does not infer non-equivariant infeasibility, positivity immediately below \(1/2\), or a
   local audit of HRSF22/RK24.

## 7a - type audit of every displayed identity

Let \(H_A=H_B=\mathbb C^3\), \(H_E=\mathbb C^4\),
\(A_n=H_A^{\otimes n}\), \(B_n=H_B^{\otimes n}\), and
\(E_n=H_E^{\otimes n}\). Dimensions are independent of \(x\).

| Display/objects | Domain and codomain | Dimension check |
|---|---|---|
| \(\Lambda_x\) | \(L(H_A)\to L(H_B)\) | \(9\to9\); every term is \(3\times3\) |
| \(\Lambda_x^c\) | \(L(H_A)\to L(H_E)\) | \(9\to16\); output is \(4\times4\) |
| \(J_x\) block form | \(L(H_B)\to L(H_E)\) | \(9\to16\); block sizes \(1+(3)\) by \(1+(3)\) |
| \(J_x^\dagger\Lambda_x^c=\Lambda_x\) | \(L(H_A)\to L(H_B)\) | \(9\to9\); \(J^\dagger\) is \(16\to9\) |
| \(L_{\Lambda_x(\tau)}\) | \(K_B=L(H_B)\to K_B\) | \(9\times9\) superoperator |
| \(L_{\Lambda_x^c(\tau)}\) | \(K_E=L(H_E)\to K_E\) | \(16\times16\) superoperator |
| \(\Delta_x\) | \(L(H_A)\to L(K_B)\) | \(9\to81\); each value is \(9\times9\), outer Choi \(27\times27\) |
| \(V_x\) | \(H_A\to H_B\otimes H_E\) | \(12\times3\); \(V^\dagger V\) is \(3\times3\) |
| two one-copy partial traces | \(L(H_B\otimes H_E)\to L(H_B)\) or \(L(H_E)\) | \(144\to9\) and \(144\to16\) as linear maps |
| \(W_nV_x^{\otimes n}\) | \(A_n\to B_n\otimes E_n\) | \(12^n\times3^n\) isometry |
| tensor partial traces | \(L(B_n\otimes E_n)\to L(B_n)\) or \(L(E_n)\) | \(144^n\to9^n\) and \(144^n\to16^n\) |
| \(M_n,N_n\) | \(L(A_n)\to L(B_n),L(E_n)\) | \(9^n\to9^n\), \(9^n\to16^n\) |
| cRE input pair with finite \(R\), \(\dim R=r\) | states on \(R\otimes A_n\) | matrices \(r3^n\times r3^n\) |
| cRE output pair | states on \(R\otimes B_n\) and \(R\otimes E_n\) | matrices \(r3^n\times r3^n\) and \(r4^n\times r4^n\) |
| each \(D(\cdot\|\cdot)\), Holevo sum, and \(I_c\) | scalar | paired arguments have identical spaces; sums are real scalars |
| purification support pair | \(R\otimes A_n\), \(r=\operatorname{rank}\rho\le3^n\) | both operators are \(r3^n\times r3^n\) |
| \(P^{(1)},Q^{(1)},P,Q\) | channel functionals | real scalars; \(n^{-1}\) regularizations are dimensionless |

Thus every displayed identity is typed at arbitrary \(n\), not just \(n=1\). The lift and defect
are one-copy inputs to the cited order theorem; only the resulting cRE order, complement, and
information expressions are tensorized.

## 7b - regime-complete gates

### Tested

- \(x=1/2,26/51,4/7,3/4\): exact forced parameters, exact F4 values, all-nine-unit
  intertwining, and exact defect-Choi spectra/ranks. At \(x=1/2\), the spectrum is
  \(\{8/9\}^{\times3}\cup\{0\}^{\times24}\). At the three interior points, ranks are eight and
  every printed exact eigenvalue is nonnegative; see `verify_whgap_p4_attempt2.log`.
- Symbolic \(x\): Kraus normalization/action, both partial traces, F4, adjoint preservation,
  complex linearity, and all 81 intertwining residual entries.
- Rank-deficient O4/O5 inputs: tested logically by
  \(p_u\rho_u\preceq\bar\rho\) and by taking the purification reference on its Schmidt support.
- Sign/orientation at \(n=1\) and arbitrary \(n\): checked directly against the PDF displays.

### Inherited

- All \(x\in[1/2,1)\), including \(x\) arbitrarily near 1: full-interval CP-defect positivity is
  inherited from R2 licensing statement 1; strict faithfulness is independently symbolic.
- Every finite reference: inherited from Theorem 3.3, Lemma 3.2, and the definition of cRE in
  the local PDF, after their channel-specific hypotheses were tested.
- Large \(n\): inherited from the Section 3.1 tensorization display and Corollaries 3.1/3.7 in
  the local Zhu-Wang PDF. The underlying HRSF22 proof is not locally audited.
- The all-input private/coherent optimizations and regularizations: inherited from Zhu-Wang
  Corollaries 3.1/3.7, with their support steps independently checked here.

### Untested

- RK24's endpoint result at \(x=1\): no local PDF; cite-only.
- The proof internal to HRSF22 Lemma 3.1: no local copy; only Zhu-Wang's statement and use were
  checked.
- \(x<1/2\), a non-equivariant WLOG theorem, and positivity/onset below \(1/2\): outside scope.

## 7d - no frozen-input immunity

R2 licensing statement 1 was used only for the covariant five-parameter exact region and unique
residual point; statement 2 only for the three exact certificates; statement 3 was not expanded
into a WLOG theorem. F4 fell outside the literal final scope lines even though R2's body passed
it, so it was reopened symbolically. The tensor-power complement, supports, information steps,
and capacities were not imported from P2/R2; they were reviewed as the new P4 assembly.

## 7e - standing failure-mode audit

- Dropped/extra normalization: none; the \(x/2\), Kraus sum, and both capacity \(1/n\) factors
  are consistent.
- Type/dimension mismatch: none; see 7a.
- Undefined terms: "admissible pair," "complement," and regularization resolve locally;
  \(P^{(1)}\)/\(Q^{(1)}\) resolve to the cited PDF. The symbol \(\pi_R\) in O5 is underdefined
  beyond "full rank" and is a MINOR notation/citation finding.
- Partial objects for full ones: none. One-copy lift/defect establish a one-copy order which is
  explicitly tensorized; every finite reference and every \(n\) remain quantified.
- Values standing in for formulas: none. Four exact values are gates for, not substitutes for,
  the R2-licensed symbolic interval theorem.
- Sign/orientation drift: none. Environment dominates receiver throughout.
- Citation laundering: no theorem is credited with a conclusion absent from its PDF statement.
  The exact O5 support pair is imprecisely attributed, and RK24 is explicitly cite-only.

## 7f - value/formula/logical decoupling

- Formula verification: `verify_whgap_p4.py` directly exercises the printed \(J_x\), channel,
  complement, defect, and forced-parameter formulas. It checks symbolic identities and exact
  spectra; it does not purport to re-prove R2's full symbolic elimination.
- Independent construction: the same script constructs the Kraus channels and Stinespring
  isometry independently and compares them on every matrix unit. Agreement corroborates the
  objects and also verifies the printed one-copy identities.
- Statement verification: the decrypted local PDF was cross-checked at Theorem 3.3, Remark 3.4,
  Lemma 3.2, Corollaries 3.1/3.7, Lemma 4.1, Proposition 4.2, Theorem 4.3, and the Section 3.1
  tensorization display.
- Logical assembly: established by the pre-reading outline comparison, not by the numerical
  values or by reproducing the proposer's order of exposition.

## 7g - quantifier hygiene

- Theorem: every \(x\in[1/2,1)\) and every integer \(n\ge1\); neither endpoint nor
  blocklength is narrowed later.
- O3: every finite-dimensional \(R\) and every state pair with
  \(\operatorname{supp}\rho\subseteq\operatorname{supp}\sigma\), exactly the PDF definition.
- O4: every finite ensemble after deletion of zero-weight terms; the support condition is proved
  per retained term. The usual private-information case is \(R\) trivial.
- O5: every input \(\rho\), including rank-deficient inputs; the reference dimension is its
  finite Schmidt rank. The optimization is over all inputs and the pure-input floor is included.
- O6: every \(n\ge1\), followed by the cited one-shot suprema and capacity regularizations.
- No quantifier is narrowed from arbitrary finite reference to one fixed reference, from all
  inputs to faithful inputs, or from all \(n\) to sampled \(n\).

## Licensing statements

1. **this review does open the completion gate for the Theorem, at tier PROVED, with scope
   \(P^{(1)}(\Lambda_x^{\otimes n})=Q^{(1)}(\Lambda_x^{\otimes n})=0\) for every
   \(x\in[1/2,1)\) and every integer \(n\ge1\), hence
   \(P(\Lambda_x)=Q(\Lambda_x)=0\) on \([1/2,1)\), subject to the explicit literature
   provenance that HRSF22 tensorization is verified here through the local Zhu-Wang statement
   rather than a local HRSF22 copy.**

2. **this review does open the completion gate for the gap-closure Corollary, at tier
   CERTIFIED*, with scope
   \(\{x:Q(\Lambda_x)=0\}\supseteq[1/2,1]\), caveated that the \(x=1\) endpoint depends on the
   cite-only RK24 antidegradability result and was not locally independently verified. The
   substatement closing \((1/2,4/7)\) is within the PROVED scope of the Theorem and has no RK24
   dependency.**

No node status is written by this review.

## Provenance

- Exact verification:
  [`verify_whgap_p4.py`](logs_whgap_p4_review_20260728/verify_whgap_p4.py) and successful
  [`verify_whgap_p4_attempt2.log`](logs_whgap_p4_review_20260728/verify_whgap_p4_attempt2.log).
  The failed first attempt is retained append-only in
  [`verify_whgap_p4.log`](logs_whgap_p4_review_20260728/verify_whgap_p4.log).
- PDF extraction:
  [`extract_zw_pdf.py`](logs_whgap_p4_review_20260728/extract_zw_pdf.py),
  [`extract_zw_pdf.log`](logs_whgap_p4_review_20260728/extract_zw_pdf.log), and
  [`zhu_wang_extracted.txt`](logs_whgap_p4_review_20260728/zhu_wang_extracted.txt).
- Checksums:
  [`SHA256SUMS.txt`](logs_whgap_p4_review_20260728/SHA256SUMS.txt).

## Closeout

- `C:<home>/cpython3119/python.exe tools/proof_dag_check.py --problem
  werner-holevo-gap`: exit 0, five node files structurally valid.
- `C:<home>/cpython3119/python.exe tools/literature_check.py`: exit 0, 42 papers across
  five libraries.
- Review-scope trailing-whitespace and link-target check: PASS.
- Repository-wide `git diff --check` reports only unrelated pre-existing whitespace in
  `artifacts/quantum_query_progress_note.aux` and `.log`; those user-owned files were not
  modified by this review.
- The review stayed within the commissioned 60-minute budget box, and no two consecutive
  information-free cycles occurred.

