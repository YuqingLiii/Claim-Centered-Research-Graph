# Independent hostile review — k-SUM major-revision pass (2026-07-19)

## Pre-action note

Fresh reviewer: authored none of the reviewed revision and was given no wanted verdict. Before inspection, the reviewer reloaded in full the research structure protocol, DAG protocol, k-SUM README, node index, and full k-SUM proof DAG.

Scope was the six implemented items in ksum/paper/ksum_small_alphabet.tex, the executor claims in ksum/artifacts/logs_ksum_rev2_20260719/codex_run.log, statement/DAG synchronization, and the requested build and repository checks. No git commit was made.

## Per-item ruling

| Item | Ruling | Independent check |
|---|---|---|
| I1 — lower-cutoff quantifier | **DISCHARGED** | For k=3, q=3, t=0, N>=7, pigeonhole forces a value to occur three times and 3a=0 in Z_3; exhaustive enumeration of all 3^7=2187 inputs found no exception, so the function is constant 1 and Q=0. The arithmetic is exact: K=floor((q-2k+1)/(k^2-2))>=2 iff q>=2(k^2-2)+2k-1=2k^2+2k-5. Abstract, informal theorem, Theorem 4.1, scope/priority paragraph, A1d, and active DAG wording agree on q0(k)<=q<=C_kN. The plateau is separately justified by K=m-1=Theta(N), which is in the claw donor range and needs only q>=(k^2-2)(m-1)+2k-1; hence c_k=k^2 supports every q>=c_kN. No live affirmative “every/all q up to Theta_k(N)” statement remains. The committed W3 closeout retains its historical wording only because history is append-only; its dated erratum explicitly supersedes it. The DAG’s other match says “former false” and is not a claim. |
| I2 — Lemma A.7 replacement | **DISCHARGED** | The old composite-modulus fiber/union count is absent. From P=k(R-1)(omega^(k-1)-1)/(omega-1), k divides P, so every prime p dividing k misses P+1. Also M+1=((2k+1)^(k-1)+1)/2: for odd p dividing k, the numerator is 2 mod p and division by 2 is legitimate, giving M+1=1 mod p; if 2 divides k, then 2k+1=1 mod 4, so M+1 is odd. Thus gcd(k,(P+1)(M+1))=1. Multiplication by k is a bijection on Z_q, and kSum_0(x)=kSum_ka(x+a1) covers the unique a with ka=t. The lemma’s exact-modulus hypothesis matches this proof, and downstream citations use the translation lemma rather than the deleted count. |
| I3 — coherent virtual oracle | **DISCHARGED** | A capped adaptive evaluator admits a fixed-length clean unitary by deferred measurement and padding. Pointwise failure probability p gives bad amplitude at most sqrt(p); compute-copy-uncompute therefore differs from the ideal xor oracle by at most 2sqrt(p) on each preserved-address block and hence in operator norm on address superpositions. Setting p=O((eta/M)^2) yields O(eta/M) per call and a telescoping O(eta) hybrid over at most M calls. Equation (20a) defines M_i=Q_(i-1)(L,q) for the recursive child and M_i=J(L) for the Johnson child, exactly matching the selection at paper lines 1047–1048; stopped branches use M_i=0 and make no child call. The h<=4U gate, fixed L,K, prefix truncation, and inductive child cap cover bad sampling/counting branches. Amplification costs O(log(M_i/delta))=O_D(log s), a fixed-depth polylogarithmic factor absorbed into N^o(1)<=N^(epsilon/2). |
| I4 — Remark A.8 | **DISCHARGED** | 21R^2-8=1 mod 3. The text correctly separates target 0 for every q>=21R^2-8 from every-target coverage at the exact modulus or at a larger modulus satisfying gcd(3,q)=1. |
| I5 — Proposition 5.2 | **DISCHARGED** | The replacement wording is present and its witnesses are sound. At q=3, the centralizer preserves the fixed-point set, so it cannot realize the indicated transposition between a fixed point and a 2-cycle value. For m>=2, flipping an unused 2-cycle is a nonidentity value symmetry fixing y=(a,a), so uniqueness fails. |
| I6 — DAG/notes synchronization | **DISCHARGED after one TRIVIAL reviewer fix** | A1d’s canonical claim, Mermaid label, and nested outline have the same thresholded statement. The executor made no status-field or Mermaid-class change, but its revised A1d Mermaid label omitted the explicit PROVED status word while retaining the proved class; this reviewer restored “PROVED-BY-REDUCTION” at ksum/notes/KSUM_PROOF_DAG.md (Mermaid A1d label). KSUM_W3_CLOSEOUT.md was extended by a dated erratum; its committed body was not rewritten. KSUM_FINAL_REPORT.md had no corresponding false claim. All mathematical statuses and the OPEN root remain unchanged. |

## Overall ruling

**PASS — all six items DISCHARGED; no substantive or trivial manuscript defect found.** One trivial DAG-label synchronization defect was fixed and disclosed above. The 2026-07-19 statement/proof-repair pass is independently reviewed. Existing node statuses remain as they were because the underlying results were already completion-tier; this review closes only the new revision’s pending-review annotations.

## Validation

- Full build from ksum/paper/: pdflatex, bibtex, pdflatex, pdflatex, all with halt-on-error. All four commands exited 0. Output: **26 pages**, 498,463 bytes.
- Final TeX log scan: **0** errors, undefined references, or undefined citations.
- python tools/proof_dag_check.py --problem ksum: PASS, 34 structurally valid nodes.
- python tools/literature_check.py: PASS, 24 papers, schema v1.
- git diff --check: PASS (no whitespace errors); Git emitted only a user-config permission warning and line-ending conversion warnings.
- Independent finite checks: all 3^7 counterexample inputs; exact-modulus gcd checks over all safely represented pairs 3<=k<=40, 2<=R<=40; and 21R^2-8 mod 3 for 2<=R<=100 all passed.

## Changes made by this reviewer

No manuscript correction was needed. This reviewer restored the explicit PROVED-BY-REDUCTION status word to the A1d Mermaid label (its proved class and actual status were already unchanged), created this report, and updated canonical review records plus synchronized DAG annotations/header to record completion. The rebuild refreshed ksum/paper/ksum_small_alphabet.pdf and ordinary LaTeX outputs. No status or graph edge was changed.

## Not checked

- No external literature refresh or priority search was performed; the review checked only whether the paper’s priority qualification was internally honest and quantifier-safe.
- Unrelated dirty-worktree files, the SE research tree, and other research problems were not audited.
- No independent rerun of the older F1/R3 or B4 numerical scripts was undertaken; this review re-derived the revision mathematics and checked consistency with their already-reviewed stated hypotheses and deterministic caps.
