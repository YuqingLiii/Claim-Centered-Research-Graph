# k-Sum GAP repair verification and rule-6 closeout

Date: 2026-07-18

Reviewer: fresh Codex completing reviewer. I did not author the audited mathematics, the hostile audit, or the prescribed repairs.

Inputs read in full:

- `DAG_PROTOCOL.md`
- `ksum/artifacts/ksum_final_gap_audit.md`
- `ksum/artifacts/ksum_gap_fixes_applied.md`

Live work products checked:

- `ksum/paper/ksum_small_alphabet.tex`
- `ksum/artifacts/ksum_F0_obstruction_note.md`
- `ksum/tools/ksum_f0_captable.py`
- `ksum/notes/KSUM_PROOF_DAG.md`

## Verdict

Ten of the eleven repair groups were present and correct exactly as prescribed. Repair group 11 had the correct MTZ scope in the live L2a outline, but one older ledger parenthetical still said `k≥4` despite the repair report saying the nearby occurrence had also been changed. I classified that as LOW documentary scope drift and corrected it during the authorized Task-3 DAG finalization. All eleven groups are correct in the final live state.

No HIGH or MODERATE defect remains in the checked repairs. The repaired paper conclusions survive.

## Task 1 — per-defect verification

| # | Audit defect | Repaired correctly? | Independent derivation / correctness check |
|---:|---|---|---|
| 1 | Abstract omitted `σ≠id` from the single-orbit claim | **YES** | The abstract now says the negative set is never a single orbit for `q≥3` **when `σ≠id`**, matching Proposition `prop:rosmanis`. This excludes the real `σ=id` one-orbit cases and introduces no broader claim. |
| 2 | Threshold constant incorrectly used untruncated `c^{1/6}` | **YES** | In the large-`q` branch `q≥N−1`, choose `κ=n−1`; this gives an absolute `Ω(√n(n−1)^{1/6})=Ω(N^{2/3})` constant. In `cN≤q<N−1`, `κ=floor((q−1)/2)≥q/3≥cN/3` for `q≥5), giving an absolute multiple of `c^{1/6}N^{2/3}`. Combining the exhaustive branches gives an absolute multiple of `min{1,c^{1/6}}`, exactly as the repaired corollary states. |
| 3 | Threshold prose could be read for all finite abelian groups/targets | **YES** | Both the abstract and informal theorem now restrict the plateau claim to cyclic `Z_q`, with every target for odd `q` and only `t=0` for even `q`. This avoids the elementary-abelian pigeonhole counterexample from the audit. |
| 4 | Large-`q` case omitted odd-`q`, arbitrary-target translation | **YES** | For odd `q`, multiplication by 2 is invertible. Given target `t`, choose a translation `c` with `2c=-t` (equivalently apply Lemma `lem:shift` between `t` and 0). Translating every input value changes each pair sum by `2c`, so target `t` is reduced to 0. Lemma `lem:shift` gives both query-complexity directions with factor at most 2, hence the lower bound loses only another absolute factor 2 before the target-zero encoding. |
| 5 | False claim that only XOR-by-a-constant has a one-query conjugation | **YES** | Let `U_A|b>=|Ab>` for invertible binary-linear `A`. Then `U_A O_y U_A^{-1}|b>=U_A O_y|A^{-1}b>=U_A|A^{-1}b⊕y>=|b⊕Ay>=O_{Ay}|b>`. Thus `U_A O_y U_A^{-1}=O_{Ay}`. The repaired sentence says this and retains the valid two-query construction for a general per-position bijection. |
| 6 | Ill-typed direct non-isomorphism across two representation categories | **YES** | For any finite group action on `X`, the invariant subspace of `C[X]` consists of functions constant on orbits, so its dimension—and the trivial-representation multiplicity—is the orbit count. Here that is at least 2. In `⊕_λ(λ boxtimes λ)` as an `S_N×S_N` module, the product-group trivial occurs only for `λ=triv`, hence exactly once. The repaired prose compares this category-independent numerical invariant and concludes only that the ED regular-representation identification does not apply; it no longer asserts a cross-category isomorphism. |
| 7 | Orbit count said to “grow” strictly with every `N` | **YES** | For fixed `m≥2`, `p_{≤m}(r)` is nondecreasing (add 1 to a largest part) and unbounded (already `p_{≤2}(r)=floor(r/2)+1`). Summing over the allowed fixed-point count preserves nondecreasingness and unboundedness. The repaired “nondecreasing and unbounded” wording is exact. |
| 8 | `R=√n` table displayed only the walk cap | **YES** | At `θ=1/2`, the walk arm is `(k−1)/(k+1)`; the combined cap is `min{1/2,(k−1)/(k+1)}`. For `k=2..8` this is `1/3, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2`. The note's displayed rows are correct, and the checker prints and asserts the full `k=2..8` sequence. |
| 9 | Uniform-donor wording overstated an endpoint iff | **YES** | With `c_*=(k−1)/(2(k+1))` and `R=Θ(n)`, `√n R^{c_*}=Θ(n^{1/2+c_*})=Θ(n^{k/(k+1)})`. Tani supplies the matching endpoint upper bound, so the endpoint lower bound holds iff the walk is optimal there. An endpoint lower bound alone says nothing about one bound holding uniformly for every smaller `R`; the note now states that converse is unproved at the heading, iff, reframing, status table, and closeout. |
| 10 | Blocked zone called a “half” | **YES** | The blocked interval in `E=log_N q` is `1≤E<(k−1)^2/(k+1)`; the full interval is `1≤E≤k−1`. Its relative length is `[((k−1)^2/(k+1))−1]/[(k−1)−1] = [(k−1)^2−(k+1)]/[(k+1)(k−2)] = k(k−3)/((k+1)(k−2))`. This is `2/5` for `k=4` and `5/9` for `k=5`. “Low-`q` sub-zone” and the examples are correct. |
| 11 | DAG said MTZ required `k≥4` | **NO in the executor's complete claimed scope; corrected here** | The principal L2a outline repair was correct: MTZ's theorem is for every fixed `k≥2`; `3/4−1/(4k)=2/3` at `k=3`, is below at `k=2`, and is strictly above exactly for integer `k≥4`. However, an older ledger parenthetical still read “TQC'20, `k≥4`,” contrary to repair-report edit 19. Task 3 changed it to “theorem for fixed `k≥2`.” The final Mermaid, outline, and ledger now agree. |

### Repair-scope spot-check

I read the live repaired passages with their surrounding proofs and read the F0 note and checker in full. The changes align with the repair report's before/after descriptions and with each file's role. I found no unlisted mathematical-content change attributable to the repair pass.

This checkout's k-Sum research tree is untracked and the worktree is heavily dirty, so `git diff` cannot supply a true pre-repair baseline for these files. Scope evidence therefore consists of the exact-location hostile audit, the repair executor transcript `ksum/artifacts/logs_ksum_GAP_20260718_fix_stdout.log`, the before/after repair report, the preserved paper integration fragment used as a role/context check, and the current full-file/context reads. This is a spot-check, not a cryptographic proof that no other byte changed.

A pre-existing LOW documentation issue remains outside the prescribed repairs: `ksum/artifacts/ksum_F0_obstruction_note.md` §6 still says W3E-2 is single-author / independent-audit-owed, while the later F1 audit recorded in the DAG says that audit completed. This is stale provenance, not a mathematical error in L2d or its endpoint qualification; I did not alter the historical F0 note beyond verifying the prescribed repairs.

## Task 2 — independent runs

### Fixed cap-table checker

Command:

```text
"<machine-local-path-redacted>" ksum/tools/ksum_f0_captable.py
```

Results:

- Exit status: 0
- Stderr: empty
- Current checker SHA-256: `75c5cebf3f9931de70ea4a1169016bce9d6e096c4901fd30eaaf03d7543c4408`
- Source inspection: `ok4` is initialized, updated against an exact `Fraction` table for every `k=2..8`, asserted by `assert ok4`, and included in the final `ok1 and ok2 and ok4` PASS gate.
- Printed combined `R=√n` caps: `1/3, 1/2, 1/2, 1/2, 1/2, 1/2, 1/2`.
- Final line: `ALL EXACT-ARITHMETIC ASSERTIONS PASSED.`
- Run log: `ksum/artifacts/logs_ksum_GAP_20260718/captable_verify.log`
- Run-log SHA-256: `0abdfe831fadd6f133fe51540c1617030e3df300d219520eb163b464edfef628`

The current checker hash correctly differs from the audit's pre-repair `130a06fd...` hash because block [4] now contains the repaired display and assertion.

### Paper rebuild

Working directory: `ksum/paper/`

Commands:

```text
<machine-local-path-redacted> -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
<machine-local-path-redacted> ksum_small_alphabet
<machine-local-path-redacted> -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
<machine-local-path-redacted> -interaction=nonstopmode -halt-on-error ksum_small_alphabet.tex
```

Results:

- All four exit statuses: 0
- Fatal TeX errors: 0
- Undefined-reference messages: 0
- Undefined-citation messages: 0
- Final rerun warnings: 0
- BibTeX warnings: 0
- Page count: 18, independently read with `pdfinfo`
- PDF SHA-256: `6a396072d0de77b844412b21b7af4d3c69aeb8882817e585e362707adb6f1c90`
- Full run/scan log: `ksum/artifacts/logs_ksum_GAP_20260718/paper_build_verify.log`
- Build-log SHA-256: `b6eddfbf58444ccd7cc5d6f109fbe500b56d54983baae2b4f4cb64c757977d1d`

## Task 3 — rule-6 DAG finalization

Updated `ksum/notes/KSUM_PROOF_DAG.md`:

- L2d's Mermaid label is now `PROVED · INDEPENDENTLY REVIEWED 2026-07-18`; the single-author star and owed-review caveat are removed.
- The label and outline explicitly cover the reviewed value-search bound, the combined cap
  `c≤min{1/2,(k−1)/(2θ(k+1))}`, the endpoint-only iff, and the corrected blocked-zone length.
- Tani's range-independent walk input is retained honestly as `PROVED-IN-LIT`, pinned by the hostile audit to primary-source Corollary 11.
- The uniform-in-`R` converse remains `UNPROVED`; the conjectural tighter `k≥3` small-range envelope remains `CONJECTURED`.
- L2b now says “dream endpoint bound” and qualifies the equivalence at `R=Θ(n)` in both Mermaid and outline; older header/ledger summaries were synchronized.
- L2a's MTZ theorem scope is `k≥2`; the improvement crossover remains `k≥4`.
- L2d moved from the special constraint class to the defined `proved` status class; the dotted edge still records its pruning-constraint role.
- Added the requested ledger line: “GAP verify pass ... L2d review cycle closed.”
- Updated “Most recent change.”
- Ancestors recomputed: L2 is still OPEN/PARKED; B2 is still OPEN because its donor child is open; no top-level route reaches the tight goal; root remains **OPEN**.
- Mermaid validation: no undefined classes, every defined node is classed exactly once, and no stale L2d star/unqualified iff/“low-q half” wording remains.

Review chain cited on L2d:

`ksum/artifacts/ksum_final_gap_audit.md` → `ksum/artifacts/ksum_gap_fixes_applied.md` → this report, plus `ksum/artifacts/logs_ksum_GAP_20260718/captable_verify.log`.

## Anything found wrong

- **LOW, corrected:** one old DAG ledger parenthetical still represented MTZ as `k≥4`, although the main outline was fixed and repair-report edit 19 claimed both occurrences were changed.
- **LOW, not changed (outside prescribed scope):** the F0 note's historical “WHAT I DID NOT CHECK” still describes W3E-2 as awaiting independent audit; the DAG records the later F1 completion.
- No HIGH or MODERATE defect remains in the verified repair set.

## WHAT I DID NOT CHECK

- I did not re-audit paper Section 4 or Appendix A except their interfaces with the reviewed claims.
- I did not independently re-prove ABI, Tani 2024, Rosmanis, Belovs–Špalek, MTZ, or W3E-2. For Tani 2009's walk I verified the audit's recorded primary-source pin and the downstream algebra, as requested.
- I did not perform a new literature search.
- I did not visually inspect all 18 rendered pages; I verified the full build, logs, references/citations, BibTeX status, PDF metadata, and page count.
- I did not run unrelated repository test suites.
- I could not establish an ordinary tracked pre-repair diff because the relevant research files are untracked in this checkout; the scope conclusion is the documented spot-check described above.
- I made no git commit.

## DAG_PROTOCOL §6 session-close checklist

- [x] Root status recomputed and matches the header: **OPEN**.
- [x] L2d has disk citations; no REFUTED node was added or changed.
- [x] Nothing self-audited was given a completion status. L2d's PROVED status is written by this fresh independent completing reviewer after the archived audit/repair/reverification chain.
- [x] Mermaid and text outline agree; every class is defined; every node is classed once.
- [x] “Most recent change” was updated; no dead node was deleted.
- [x] No new route was proposed.
- [x] Every completion-tier status written in this pass cites a completed independent review and run provenance (rule 6); unproved uniform/conjectural claims remain below completion tier.

