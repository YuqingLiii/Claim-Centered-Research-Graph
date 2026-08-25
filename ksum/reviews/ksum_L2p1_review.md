# Independent hostile review — KSUM.B4b.L2 phase 1

Date: 2026-07-19  
Reviewer: fresh independent completing reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Scope: the phase-1 invariant framework, frozen P2 projection gate, exact P3 LPs, and stated P4 lemma/proof plan

## Pre-action reload and provenance

Before analyzing or changing status I reloaded from disk the research-structure and DAG protocols (including completion rule 6), the KSUM node index, KSUM.B4b.L2 and parent KSUM.B4b, the complete phase-1 report and both drivers, every text/JSON/log artifact in ksum/artifacts/logs_ksum_L2p1_20260719, the optimizer manifests and relevant JSON/NPZ data in ksum/artifacts/logs_ksum_expL_20260719, and the cited passages of Tani's local main.tex. I also read KSUM.L2d, KSUM.B4b.U1, its completed hostile review, the relevant legacy-DAG cap passages, and the optimizer extractor/reconstruction code. No network or git commit was used.

The preregistration is genuinely earlier than the measurement on the available record. predictions.txt was created and last modified at 18:45:13.801Z; projection_test.log was created at 18:46:19.818Z and records the measurement starting at 18:46:30.158Z; projection_results.json was created at 18:46:34.626Z. The executor transcript states the threshold and exact subspaces before writing predictions.txt, records that optimizer arrays remained unopened, and only afterward builds/runs the measurement. This proves disk/transcript ordering, not the unknowable stronger claim that a human had never seen similar data in another session.

Independent verification code, importing neither phase-1 driver:

- ksum/tools/ksum_l2p1_review_projection_verify.py; output ksum/artifacts/logs_ksum_L2p1_20260719/independent_review_projection.log.
- ksum/tools/ksum_l2p1_review_verify.py; output ksum/artifacts/logs_ksum_L2p1_20260719/independent_review_verify.log.

## Ruling

**OPEN — independent review completed; finite LP optima verified, but the asymptotic lemma is false as stated and must be repaired.**

The exact rational P3 optimum table is correct as a statement about sign approximate degree at approximation error (1/3). The joint and single LPs use the same normalization and moment constraints. P2 validly detects a 25–27 percentage-point deficit of the chosen shell coarsening at two optimizer blocks. It does not nontrivially establish 100% “joint capture”: that value is forced by how the invariant optimizer and full orbital space are constructed.

Two defects prevent confirmation of the route at CONJECTURED. First, with (F\in\{-1,+1\}), a quantum algorithm of error (1/3) yields a degree-(2T) sign polynomial with uniform error (2/3), so a direct (Q_{1/3}\ge d/2) dual certificate needs correlation strictly greater than (2/3), not (1/3). Second, the P4 lemma quantifies uniformly through (q=N) while demanding (d=\Omega(\sqrt N q^\eta)) for (\eta>1/6); at (q=N) this exceeds (N^{2/3}), contradicting the proved range-independent Johnson/Tani walk upper bound and the polynomial method. The broad joint-histogram route is repairable and therefore is not REFUTED: a cap-compatible target such as (\Omega(\min\{\sqrt N q^\eta,N^{2/3}\})), or the range (q\le N^{1/(6\eta)}), remains logically possible.

## S1 — P2 is partly tautological

### S1(a): exact subspace spanned by “joint”

For an ordered input pair ((x,y)), full_joint_codes stores:

1. the distinguished ordered symbol pair ((x_0,y_0));
2. the complete table (J_{ab}=|\{r>0:(x_r,y_r)=(a,b)\}|);
3. the lexicographically minimal encoding under simultaneous (C(\sigma)) relabeling; and
4. the minimum of the encoding and its transpose, because the saved matrix is symmetric.

The complete table labels the orbit under simultaneous permutation of positions (1,\ldots,N-1). Canonicalization adds (C(\sigma)), and transposition passes from directed orbitals to symmetric orbitals. Therefore the indicator matrices of the resulting 4,108 and 6,944 classes span exactly the real symmetric (S_{N-1}\times C(\sigma))-invariant matrix space. They are disjoint-support indicator matrices, so projection is simply within-class averaging; there is no Gram–Schmidt or ill-conditioned basis orthogonalization.

### S1(b): why 100% is forced

The extractor optimizes symmetric multiplicity blocks for the same stabilizer representation and reconstructs natural_A as a sum of aligned invariant block embeddings, then explicitly symmetrizes it. Consequently every such reconstructed optimizer lies in the full symmetric orbital space, regardless of its numerical optimum or uniqueness. “Joint capture = 100%” is therefore a construction check, not evidence favoring the route.

Independent stable within-class SSE recomputation found full-space relative residuals (3.86\times10^{-14}) and (7.14\times10^{-14}), with maximum within-class deviations (6.45\times10^{-14}) and (3.15\times10^{-13}). The original code instead computes residual as total minus projected mass and clamps negative roundoff to zero; that is numerically fragile near exact capture, but the stable recomputation shows no material error.

The nonautomatic result is the shell deficit:

| Case | shell capture | full capture | full minus shell |
|---|---:|---:|---:|
| (5,4,1) | 0.729571578447623 | 1 within roundoff | 0.270428421552377 |
| (7,3,0) | 0.747543015864284 | 1 within roundoff | 0.252456984135716 |

### S1(c): fairness and re-grading

The 10-point discriminator was frozen before measurement and is fair for its narrow operational question: does this particular invariant optimizer lie close to the explicitly defined label/distinguished-pair/Hamming-distance coarsening? It decisively says no at both selected points.

It is strictly weaker than the qualitative frozen wording that “joint-histogram duals genuinely exceed” shell resolution, and weaker than the route-level risk if “collapse to BS Hamming shells” means the entire Belovs–Špalek algebra. Reasons:

- the full-space projection is guaranteed, so the test is algebraically identical to asking whether shell capture is at most 90%;
- the measured object is a two-input HLS optimizer matrix under the stabilizer (S_{N-1}\), whereas P3/P4 use one-input signed measures under (S_N);
- the script defines one coarse shell proxy but does not prove that proxy equals every BS/Hamming-shell construction relevant to the route; and
- two selected finite optimizers do not address optimizer nonuniqueness or asymptotic collapse.

**Re-graded P2 meaning:** PROVED finite numerical fact after independent recomputation: the two archived invariant matrices have 27.04 and 25.25 percentage points of squared Frobenius mass outside the specified shell coarsening. P2 supplies no independent evidence from the 100% column and does not establish dual-polynomial or asymptotic expressiveness.

## S2 — P3 correctness and meaning

### Dual derivation

Let (F=-1) on NO inputs and (F=+1) on YES inputs. For a joint input orbit (h), let (w_h) be its total signed mass and lift it uniformly to inputs in that orbit. Then (\|\mu\|_1=\sum_h|w_h|).

A nonzero query monomial of degree (m) selects (m) distinct positions and has a symbol-multiplicity vector (\alpha\) with (|\alpha|=m). Averaging over (S_N) gives

\[
  \frac{\prod_a(n_a)_{\underline{\alpha_a}}}{(N)_{\underline m}}.
\]

For a (C(\sigma))-invariant measure, averaging this expression over the alphabet orbit of the occupancy vector loses no constraint. The nonzero denominator is irrelevant to a zero equation. Hence pure high degree at least (d) is exactly

\[
 \sum_h w_h M_{\alpha,h}=0\qquad (|\alpha|<d),
\]

with (M) the class average used in the driver. Repeated one-hot variables reduce by idempotence; incompatible same-position symbols give the zero monomial. Thus these rows cover the full one-hot query basis, not merely a selected generator list.

The split-variable LP with (\sum_h(w_h^++w_h^-)\le1) is equivalent to (\|w\|_1\le1). At every positive logged optimum the recovered witness has exact norm one. Joint classes average over (C(\sigma)); single classes average over (S_q). Alphabet permutations preserve multinomial orbit sizes, so the unweighted average over occupancy vectors is the correct input-class average in both cases. Correlation, moment degree, and norm conventions are otherwise identical, making the comparison genuinely nested.

Tani's cited passages support row multisymmetry, degree-preserving power-sum generation over (\mathbb Q), and domain symmetrization into occupancy polynomials. They do not state the (C_2\wr S_r\) centralizer specialization verbatim. That specialization is nonetheless correct: symmetrized pair power sums generate the wreath-product invariant ring over (\mathbb Q), fixed points contribute an independent symmetric factor, and the direct all-(\alpha) moment implementation does not rely on an unproved choice of generators.

### Exact witness and optimum verification

The independent verifier rebuilt all joint/single occupancy orbits, all falling-factorial rows, and all class-averaged signs without importing the submitted solver. Across all 24 logged bands it found:

- exact (\ell_1=1);
- exact correlation equal to the logged rational value;
- every exact rational moment residual equal to zero;
- independent HiGHS optima agreeing within (1.12\times10^{-16}); and
- rationalized LP-dual upper certificates satisfying every inequality exactly and attaining each logged rational optimum.

Thus the entire P3 rational optimum table, including the equal (1/11) endpoint at (5,4,1), is **PROVED as a finite LP claim by this completed review**.

### Error convention and corrected finite interpretation

For sign approximate degree, the submitted test “correlation (>1/3)” correctly certifies (\widetilde{\deg}_{1/3}(F)\ge d). It does **not** directly imply (Q_{1/3}(F)\ge d/2). A (T)-query algorithm with output error (e) has a degree-(2T) expected-sign polynomial of uniform error (2e), so direct error-(1/3) exclusion requires correlation (>2/3). At that threshold the logged table re-grades to:

| Case | single degree certified for direct error-1/3 polynomial test | joint degree certified |
|---|---:|---:|
| (3,3,0) | 0 | 2 |
| (4,3,0) | 0 | 2 |
| (5,4,1) | 2 | 3 |

Degree zero means only that this LP supplies no positive-degree certificate at the strict (>2/3) threshold; it is not a claim that the function has degree zero. The original degrees 3,4,4 still yield an asymptotic quantum lower bound up to a larger constant by first amplifying a (1/3)-error algorithm to error below (1/6); they do not carry the claimed direct factor (1/2).

### Evidential weight

The small instances show that the orbit/moment machinery runs and that fine pairing can improve finite correlations. They do not support an exponent trend. Degrees 3 and 4 occur at (N\le5), the tested alphabets and cycle types are sparse, and no cross-(N) witness family or uniform norm estimate appears. G11 therefore limits P3's route-level weight to “machinery and finite separation demonstrated.”

## S3 — additional attacks

### Projection numerics

**PASS after independent recomputation.** There is no basis-orthogonalization error because class indicators are orthogonal. The submitted total-minus-projected residual and zero clamp can conceal only roundoff at full capture; stable SSE reproduces both shell deficits to approximately (6\times10^{-15}). It does not repair P2's conceptual tautology.

### The (5,4,1) no-degree-gain point

**Mixed but not a refutation.** At the submitted (1/3) approximation threshold, both bases top out at degree 4, so the phrase “strict joint-over-single gains” refers to objective values at (d=3,4), not to the maximum integer degree. Both fail at (d=5). This weakens any claim that fine pairing automatically raises degree. It is plausibly size-limited because (N=5) leaves only one higher band, and under the corrected direct quantum threshold the same point actually separates degree 3 from degree 2. With one point, “size-explicable” is a plausible interpretation, not evidence of asymptotic growth.

### P4 statement and proof plan

**The statement is syntactically well quantified but mathematically false as written.** Fixed constants (\eta,c_0,\delta), all (3\le q\le N), all targets, and one witness per ((N,q,t)) give a meaningful family and make “pure high degree (\Omega(\sqrt Nq^\eta))” precise up to integer rounding. The missing restriction (0<\delta<2/3) is minor because correlation is at most one.

The fatal cap contradiction is immediate. At (q=N), the demanded degree is (\Omega(N^{1/2+\eta})), strictly larger than (N^{2/3}) for every (\eta>1/6). The range-independent Johnson/Tani walk gives (Q=O(N^{2/3})), and every (T)-query algorithm yields a degree-(2T) approximant after choosing a fixed error convention. This conflicts with the reviewed walk cap, independently of U1. For the target (\eta=1/4), the uncapped formula is compatible only through (q\le N^{2/3}). A corrected uniform statement must include (\min\{\sqrt Nq^\eta,N^{2/3}\}), or explicitly restrict (q\le N^{1/(6\eta)}).

The proof plan is coherent as a list of the right obstacles—pair-lattice kernel, conditioning, fixed-point factor, norm/correlation control, full-basis lift—but it is not yet a constructive argument. Conditioning on total occupancy is exactly where low-degree cancellation can fail, and no kernel or Christoffel estimate is supplied. After the cap repair it is a plausible research program, not an argument sketch strong enough for CONJECTURED.

### Consistency with L2d and U1

L2d is formulated for the (k\ge3) donor campaign, so it is not literally the governing node for this (k=2) dual. Its endpoint logic is the same cap: a range-independent walk upper bound forbids a lower-bound exponent beyond the walk. The phase-1 P4 statement violates that logic at (q=N).

U1's reviewed certificate is consistent with a cap-corrected L2 target: it says one charged sample–compress model approaches a (q^{1/4}) upper exponent and does not prove an all-algorithms lower bound. A lower witness targeting (q^{1/4}) only in the active middle range and saturating at (N^{2/3}) would not contradict U1. The submitted uncapped (q^{1/4}) family does contradict the actual walk upper bound.

## Defects

| ID | Severity | Defect | Effect / required repair |
|---|---|---|---|
| D1 | MAJOR | P2's full joint capture is forced by invariant reconstruction and full-orbital projection. | Re-grade P2 to the shell deficit only; do not cite 100% as route evidence. |
| D2 | MODERATE | P2 measures a two-input stabilizer optimizer and one chosen shell proxy, not the one-input dual space or a proved complete BS algebra. | Treat it as narrow structural evidence; add a one-input/held-out discriminator if desired. |
| D3 | MAJOR | The sign encoding uses correlation (>1/3) but the intended direct error-(1/3) quantum bound via degree/2 requires (>2/3). | Relabel as sign approximate degree at error (1/3), use amplification with the correct constant, or rerun/report the (2/3) threshold. |
| D4 | FATAL to P4 as stated; route-repairable | Uniform (\eta>1/6) through (q=N) exceeds the (N^{2/3}) walk cap. | Add the (N^{2/3}) minimum or restrict the q-range; do not leave the false lemma as the next obligation. |
| D5 | MINOR | Original projection residual uses cancellation plus a zero clamp. | Stable SSE independently confirms the values; use it in future runs. |
| D6 | MINOR | “Strict gains” can be read as degree gains at every point, but (5,4,1) has equal maximum degree 4 under the submitted threshold. | Say strict objective gains at selected bands and list maximum-degree ties explicitly. |

## Status action

KSUM.B4b.L2 is demoted from CONJECTURED · pending-review to **OPEN — independent review completed**. This is not an over-kill: the exact finite LPs pass, the joint-histogram framework is mathematically legitimate, and a cap-corrected asymptotic route remains possible. The specific uncapped P4 lemma is refuted by a proved upper bound. No node is promoted to PROVED; only the finite rational LP optimum claims are marked proved within this review. KSUM.B4b, KSUM.B4, and the root remain OPEN.

## What I did not check

- I did not rerun the expensive MOSEK optimizer extraction or prove optimizer uniqueness; I checked its archived feasibility diagnostics, hashes, symmetry construction, and the two saved matrices used by P2.
- I did not independently re-prove the reviewed Johnson/Tani quantum walk theorem or the full L2d/U1 reviews; I checked their on-disk statements and the cap arithmetic used here.
- I did not construct the repaired asymptotic witness, prove conditioning preserves moments, or prove uniform (\ell_1)/correlation estimates.
- I did not exhaust all BS adversary algebras or show that the submitted shell proxy is maximal.
- I did not test additional ((N,q,t)), held-out optimizers, or cycle types.
- I did not use the network.

## Closeout validations

- Independent verifier syntax compilation: PASS.
- python tools/proof_dag_check.py --problem ksum: PASS (38 nodes; existing native-migration semantic warnings only).
- python tools/literature_check.py: PASS (24 papers, schema v1).
- git diff --check: PASS; stderr contains only pre-existing permission/line-ending warnings.
- Full outputs: ksum/artifacts/logs_ksum_L2p1_20260719/REVIEW_VALIDATION.txt.
