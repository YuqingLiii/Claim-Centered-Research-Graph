# Independent hostile review — W partial k-claw lower bounds

Date: 2026-07-18  
Reviewer role: fresh completing reviewer under `DAG_PROTOCOL.md` rule 6; authored none of the reviewed reductions and was given no wanted verdict.  
Targets: W-LB1 / DAG L2e (2-claw filler lift) and W-LB2 / DAG L2f (random color-coding from k-distinctness).  
Primary work product: `ksum/artifacts/ksum_W_walkopt_landscape.md`.  
Run provenance: `ksum/artifacts/logs_ksum_W_20260718/codex_review_run.log`. The shell launcher failed before executing commands; local sources were read through the Node filesystem interface. No numerical experiment was needed.

## Rulings

| Target | Ruling | Defects | Consequence |
|---|---|---|---|
| R-A / L2e | **PROVED after making the standing hypothesis `R>=2` explicit** | 1 MINOR endpoint omission: at `R=1` every instance is YES, so the displayed positive lower bound would be false. The paper's formal definition already assumes `R>=2`. | For fixed `k>=3`, `n>=2`, and `R>=2`, `Q_k(n,R)=Omega(sqrt(n) min{R,n}^{1/6})`. |
| R-B / L2f | **PROVED** | 1 MINOR exposition gap: repetition must be preceded by constant-error amplification of each claw call. The repair costs only `O_k(1)`. | For fixed `k>=3` and every sufficiently large `R>=C_k n^2`, `Q_k(n,R)=Omega(n^{3/4-1/(4(2^k-1))})`. |

Neither result discharges L2: both are partial floors below the requested walk-optimal donor.

## R-A — 2-claw filler lift

### Imported theorem and endpoint

ABI defines `cl_{n,k}` on two length-`n` lists over `[k]` at `ksum/artifacts/references/abi_2103.16390_src/claw.tex:120-136` and states
`Q(cl_{n,k})=Omega(n^{1/2}k^{1/6})` for `k>=2` at lines 289-295. Write its range size as `s` to avoid collision with the number of lists.

Take `s=min{R,n}`. The repository's formal k-partite collision definition assumes `R>=2` (`ksum/paper/ksum_small_alphabet.tex:369-372`), hence `2<=s<=n`. The landscape's local convention did not repeat this endpoint. Read literally at `R=1`, its display is false because the decision function is constant YES. This is a concrete but MINOR endpoint defect; the reviewed statement and DAG now make `R>=2` explicit.

### Completeness and soundness

Let the hard ABI input be `f_1,f_2:[n]->[s]`. For each `j=3,...,k`, fix a surjection `h_j:[n]->[s]`, possible because `s<=n`.

If `f_1(i_1)=f_2(i_2)=v`, surjectivity supplies `i_j` with `h_j(i_j)=v` in every filler list, so every 2-claw extends to a k-claw.

Conversely, a k-claw has a common value `v` and therefore in particular satisfies `f_1(i_1)=f_2(i_2)=v`. It contains a base 2-claw. Filler-filler collisions cannot bypass equality between the first two lists; neither can a collision between fillers and only one base list. Thus the lifted input is YES iff the ABI input is YES.

### Queries and declared range

A query to either live list forwards one base query. A query to a fixed filler position is answered by an input-independent computation and costs no base query. No input-dependent preprocessing is hidden. This is simpler than the general two-query per-coordinate relabeling fact at `ksum_small_alphabet.tex:120-131`.

For `2<=R<n`, `s=R` and a length-`n` filler enumerates the whole range. For `R>=n`, use only `[n]`. Restriction monotonicity (`ksum_small_alphabet.tex:121-123`) means an algorithm for the declared range must solve the subalphabet restriction; unused labels cannot ease the worst case. Therefore
`Q_k(n,R)>=Q_2(n,s)=Omega(sqrt(n)s^{1/6})`.
This proves corrected R-A.

## R-B — random color-coding from k-distinctness

### Exact imported statement

Belovs's introduction states the exponent for fixed `k=O(1)`, bounded error, and alphabet size at least `Omega(n^2)` at `ksum/artifacts/references/bel2026/new-adversary_v6.tex:93-102`. The final theorem states the search lower bound under `q=Omega(n^2)` at lines 3078-3087, and line 3089 explicitly gives the same lower bound for bounded-error decision via the standard search-to-decision reduction. The donor is worst-case decision hardness, not average-case finding hardness.

### Exact reduction and deterministic soundness

For `x:[n]->[q]`, choose `c:[n]->[k]` uniformly and distinct `d_1,...,d_k` outside `[q]`. Put
`F_j(i)=x_i` when `c(i)=j`, and `F_j(i)=d_j` otherwise.

Because the dummies are pairwise distinct and outside the donor alphabet, no k-claw can contain a dummy. A k-claw exists exactly when some donor value occurs in all k colors. On a donor NO-instance every value occurs at most `k-1` times, so every coloring maps to NO. Soundness is deterministic under all reduction randomness.

On a YES-instance, fix k occurrences of one repeated value. They receive all colors with probability `p_k=k!/k^k`, a positive constant for fixed k. Additional occurrences or witnesses only help.

### Amplification

Let `A` be a `T`-query bounded-error k-claw algorithm. Choose constant `m=m(k)` with `(1-p_k)^m<=1/12`. Amplify each call to error `delta=1/(12m)`, costing `O(log(1/delta))=O_k(1)`, run on m independent colorings, and OR the results.

On a donor NO-instance the union bound gives false acceptance at most `m delta=1/12`. On a YES-instance, failure to expose the fixed witness costs at most `1/12`, and amplified-call failures cost at most another `1/12`; acceptance is at least `5/6`. Total donor-query cost is `O_k(T)`.

A coherent query computes the public coloring predicate and fixed dummies reversibly, forwarding an x-query only on the matching-color branch. Standard controlled-query simulation has constant overhead.

### Range accounting

The target uses `q+k` labels. Belovs requires `q>=C n^2`. Thus for every sufficiently large declared `R>=C_k n^2`, choose a donor alphabet `q<=R-k` meeting that hypothesis and reserve k labels as dummies. Restriction monotonicity covers larger declared ranges. This proves R-B.

## Composition through W3E-2

The exact corollaries in this section are newly formulated in this review. Under rule 6 and the user's explicit tier instruction, they are recorded as CONJECTURED/pending-review rather than self-stamped with a completion status.

The independently reviewed embedding at `ksum/paper/ksum_small_alphabet.tex:365-406` maps a donor `Omega(sqrt(n)R^c)`, with `N=kn`, to
`Q(k-Sum over Z_q at t)=Omega_k(sqrt(N)q^{c/(k-1)})`
for every target t and its constructed moduli `q=Theta_k(R^{k-1})`. The rulings below retain these hypotheses and do not claim an all-moduli interpolation.

### C-A / child L2eC — CONJECTURED pending independent review; dominated in the zone

For `2<=R<=n`, R-A has `c=1/6`. Hence
`Q(k-Sum_{Z_q,t,N})=Omega_k(sqrt(N)q^{1/(6(k-1))})`
on the W3E-2 modulus family.

The zone `q in [Theta_k(N),Theta_k(N^{k-1})]` corresponds to
`R in [Theta_k(N^{1/(k-1)}),Theta_k(N)]`.
At the upper endpoint the bound is `Omega_k(N^{2/3})`; below it is weaker. The already-PROVED W3E-1 floor is `Omega_k(N^{2/3})` throughout `q>=Theta_k(N)` (`ksum_small_alphabet.tex:298-348`). Thus C-A is correct but adds no stronger lower-bound envelope in the requested zone.

### C-B / child L2fC — CONJECTURED pending independent review; no in-zone bound

R-B requires `R=Omega(n^2)`. W3E-2 therefore gives
`q=Theta_k(R^{k-1})=Omega_k(n^{2(k-1)})=Omega_k(N^{2(k-1)})`,
strictly above `Theta_k(N^{k-1})` for fixed `k>=3`.

At `R=Theta(n^2)`, the composed lower bound is only
`Omega_k(N^{3/4-1/(4(2^k-1))})`
at `q=Theta_k(N^{2(k-1)})`. This is not a new useful k-Sum regime: `2(k-1)>=k`, so the moduli already satisfy the Belovs-Špalek large-alphabet hypothesis and its `Omega(N^{k/(k+1)})` bound is stronger. R-B gives no W3E-2 bound in `[Theta(N),Theta(N^{k-1})]`. Treating it as an R-power law down to `R<=n` would violate Belovs's alphabet hypothesis.

## Defect ledger

1. **MINOR, R-A endpoint:** `R>=2` was omitted locally; the formula is false at `R=1`. Repaired in the ruling and DAG.
2. **MINOR, R-B error bookkeeping:** raw repetition is insufficient without lowering each call's false-positive probability. Constant amplification repairs it with `O_k(1)` overhead.
3. **MAJOR overclaim avoided, proposed R-B composition:** the donor hypothesis forces `q=Omega(N^{2(k-1)})`, not the requested zone. This is a defect in the proposed extrapolation to assess, not in R-B.

No completeness, soundness, decision/search, or query-simulation defect remains in either corrected reduction.

## What I did not check

- I did not review L2g, the BKT/MTZ small-alphabet rows, or the surrounding literature reconnaissance.
- I did not re-review W3E-2's encoding algebra or its F1/R3 exhaustive checks; I checked the theorem statement and composition hypotheses.
- I did not independently prove ABI or Belovs; I verified their exact on-disk statements, hypotheses, and decision/search form.
- I did not run brute force: exact iff arguments resolved both reductions. No `ksum/tools/ksum_wr_*.py` scripts are present; the W log directory contains the executor and this review-session logs.
- I did not claim arbitrary cyclic moduli between W3E-2 construction points.

## Status propagation

L2e and L2f move from CONJECTURED/pending-review to PROVED with this archived review cited. Composition children L2eC and L2fC are CONJECTURED/pending-review. They remain dotted partial-outcome/constraint nodes, so L2 stays OPEN/PARKED, B2 stays OPEN, and the root stays OPEN.
