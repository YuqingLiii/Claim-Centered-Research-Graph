# B4 upper-bound note v2: a bounded-query ABI port for cyclic 2-Sum

**Status: CONJECTURED pending-review (v2).** This is the executor's repaired proof candidate. It integrates the completed hostile review in `ksum/artifacts/ksum_B4_review.md`, but the new repairs have not received the separate fresh review required by `DAG_PROTOCOL.md` rule 6. Nothing here is a completion-tier claim.

## 1. Candidate theorem and exact quantifiers

**Candidate theorem.** For every real `epsilon>0` there are constants `C_epsilon,N_epsilon` such that, for every integer `N>=N_epsilon`, every integer `q>=2`, every target `t in Z_q`, and every oracle input

    x:[N] -> Z_q,

a bounded-error quantum algorithm decides whether there are **distinct** indices `i,j` with

    x_i+x_j=t (mod q)

using at most

    C_epsilon N^(1/2+epsilon) q^(1/4)

queries. The worst-case query cap holds for every choice of the algorithm's classical randomness and every sequence of quantum measurement outcomes; only correctness is probabilistic. The hidden constant may depend on `epsilon`. Finitely many `N<N_epsilon` are absorbed by increasing that constant.

There is no parity assumption. The algorithm works directly at the supplied target. For odd `q`, `2v=t` has one solution; for even `q` it has none when `t` is odd and two when `t` is even. Thus at most two fixed-point values require special treatment. The on-disk translation lemma gives the equivalent canonical target classes, but the proof does not need to translate the input (`ksum/paper/ksum_small_alphabet.tex:164-170`).

The recursive proof is used exactly when

    2 <= q <= N^(2/3).

When `q>N^(2/3)`, the range-independent Johnson walk costs `O(N^(2/3))`, which is at most `N^(1/2)q^(1/4)`. No hypothesis such as `q<N` or `q=O(N)` is made.

## 2. What comes from ABI and what is reconstructed here

ABI define the two-list claw problem at `ksum/artifacts/references/abi_2103.16390_src/claw.tex:120-132` and state the upper bound `O(n^(1/2+epsilon)k^(1/4))` at lines 135-143. Their upper-bound proof:

- samples `4 n^alpha ln n` positions and Grover-searches the other list (lines 148-160);
- compresses unseen entries by fixed permutations and Grover minimum search (lines 161-175);
- proves the residual and coverage bounds (lines 177-204);
- charges `O-tilde(sqrt(n/b))` per virtual query (lines 206-225); and
- bootstraps the Johnson base with

      T_i(kappa)=((2^i-1)kappa+2^(i+1))/(2^(i+2)-1)

  for `0<=kappa<=2/3` (lines 240-286).

The following are v2 reconstructions rather than claims attributed to ABI: the single-list residual, all cyclic fixed points, an upper residual estimate obtained by bounded approximate counting, fixed truncation of every virtual oracle, coherent nested-oracle amplification, the actual-short-compressed-list fallback, and the global worst-case cap. ABI's line 169 also writes the undefined `X_(A')`; the context at lines 158 and 173 shows that `Y_(A')` is intended. Nothing below relies on that typo.

## 3. Bounded-query primitives used

All computation other than input-oracle calls is free in the query model. Each search routine returns a candidate, and every candidate is checked before acceptance.

1. **Search.** Grover search over `s` positions uses `O(sqrt(s))` queries at constant error. Repetition/coherent majority reduces error to `delta` with `O(log(1/delta))` overhead.
2. **Johnson base.** On a list of length `s`, walk on `r=min{s,ceil(s^(2/3))}` subsets. Setup costs `r`, update costs `O(1)`, the gap is `Theta(1/r)`, and a fixed witness marks `Omega((r/s)^2)` of the states. Hence

       O(r+(s/r)sqrt(r))=O(s^(2/3))

   list-oracle queries. Marking is query-free from stored values and enforces distinct list coordinates. The walk can output and verify a witness.
3. **Capped counting.** After a separate zero search, bounded approximate counting returns a number `c` such that `b/2<=c<=3b/2` when `b>0`, except with error `delta\). Set `h=ceil(2c)`; on the good event,

       b <= h <= 4b.

   The counting procedure is forcibly stopped after `O(sqrt(s)log(1/delta))` queries. Its sharper good-event cost is `O(sqrt(s/b)log(1/delta))`, but the proof uses the fixed `O(sqrt(s))` cap where needed.
4. **Truncated first marked position.** Given a fixed permutation, minimum finding over its first `K` positions returns the earliest residual index using `O(sqrt(K))` queries, or a tagged failure symbol if the prefix has none. The routine is forcibly stopped at that budget.
5. **Nested use.** If a bounded recursive subroutine can make at most `M` virtual calls, amplify each coherent virtual oracle to operator error at most `delta/M`. Compute, copy the answer register, and uncompute. The hybrid bound makes the aggregate nested-oracle error at most `delta`, at `O(log(M/delta))` overhead per virtual call.

These standard primitive guarantees are stated here so the query schedule is explicit. Section 9 records that their literature/circuit proofs were not independently re-audited in this pass.

## 4. The complete depth-i algorithm

For `i>=0`, let `A_i(n,q,t)` be a witness-finding version of the decision algorithm. Define

    T_i(kappa)=a_i+c_i kappa,
    a_i=2^(i+1)/(2^(i+2)-1),
    c_i=(2^i-1)/(2^(i+2)-1).

Fix a final recursion depth `D`. Put

    delta = 1/(200(D+1)),
    Lambda(n,D)=ln(2^16 (D+1) n^4).

Every ordinary search, count, or base walk is amplified to failure at most `delta`. At most four fixed-point searches occur per active level. Each virtual oracle is amplified to `delta/M`, where `M` is the known worst-case virtual-query cap of the selected child algorithm. There are only `O(D)` event families, so a union/hybrid bound leaves total error below `1/3`. The displayed constants are deliberately loose.

### Base and range switch

On a list of length `n`:

- if `i=0`, run the Johnson base;
- if `q>n^(2/3)`, also run the Johnson base;
- otherwise write `q=n^kappa`, so `0<=kappa<=2/3`, and set

      alpha=T_i(kappa).

For this interval, `kappa<=alpha<=2/3` and `alpha>=1/2`.

### F. Fixed-point multiplicity pre-step

Classically list

    F={v in Z_q: 2v=t}.

For each of the at most two values `v in F`, Grover-search for one occurrence. Verify it. If found at position `p`, search `[n] minus {p}` for a second occurrence and verify it. If a second occurrence is found, return those two positions.

On the event that all at most four searches are correct, reaching the next step proves that each fixed-point value occurs at most once. All later residual predicates exclude **every** position whose value lies in `F`. A missed first or second occurrence can cause a false negative, but it is explicitly one of the charged search-error events. This fixes review defect D4.

### S. Sample and search all sample-incident pairs

Let

    ell=min{n, ceil(n^alpha Lambda(n,D))}.

Choose a uniform `ell`-subset `A` of positions, query all of it, and store its values. If `ell=n`, check all pairs classically and stop. Otherwise:

1. check all pairs of distinct positions inside `A` without more queries;
2. let `S` be the sampled values outside `F`;
3. Grover-search `j notin A` for `x_j in t-S`, and verify any returned pair.

If these tests are correctly negative, every surviving witness has both endpoints in

    B={j in [n]: x_j notin F and x_j notin S};    b=|B|.

For a non-fixed value occurring at least `n^(1-alpha)` times, the chance that the uniform sample misses every occurrence is at most

    exp(-ell n^(1-alpha)/n) <= exp(-Lambda).

There are at most `q<=n^(2/3)` values. Therefore, except on a sampling event of probability at most `q exp(-Lambda)<delta`, every unseen non-fixed value has multiplicity below `n^(1-alpha)` and

    b <= q n^(1-alpha).

### C. Count, cap, and compress

Run the capped zero test. If it correctly reports `b=0`, return no witness. Otherwise run capped approximate counting and form the integer upper estimate `h` above. Define the deterministic residual ceiling

    U=ceil(q n^(1-alpha)).

If counting fails to return a legal positive integer or if

    h>4U,

abort this branch and return no witness. This can lose a witness only on the sampling or counting bad event: on their joint good event, `b<=U` and `b<=h<=4b<=4U`.

On every continuing branch—good or bad—we now have the deterministic cap `1<=h<=4U`. Fix

    L=ceil(h Lambda(n,D)),
    K=min{n, ceil(4(n/h)Lambda(n,D))}.

Choose `L` independent uniform permutations `pi_1,...,pi_L` of `[n]` before the recursive computation. For virtual coordinate `s`, search only the first `K` positions of `pi_s` and return the earliest member `r_s in B` and its value `z_s=x_(r_s)`. If the prefix contains no residual index, return a tagged dummy. All work is stopped after the fixed `O(sqrt(K))` query budget.

Run the child algorithm on the length-`L` virtual list:

- use `A_(i-1)(L,q,t)` when `q<=L^(2/3)`;
- use the Johnson base on length `L` when `q>L^(2/3)`.

Unwrap any returned virtual coordinates to original indices and verify the claimed original pair before accepting. This may require reevaluating at most two returned virtual coordinates per active level; those evaluations have the same bounded virtual-oracle cost already charged at that level, and the final two input-value checks are constant-query.

## 5. Correctness

### Sampling loses no within-list witness

After Step F succeeds, no remaining fixed-point witness exists. Step S checks pairs inside the sample and searches every outside position whose value partners a sampled value. Hence a correctly negative Step S leaves every genuine witness wholly inside `B`. No claw bipartition is assumed.

### Coverage

Condition on a fixed nonempty `B` and on good counting. In a full uniform permutation, the first member of `B` is independent uniform on `B`. Since `h>=b`, the chance that some residual index is absent from all `L` full first-member choices is at most

    b exp(-L/b) <= n exp(-Lambda)<delta.

If `K<n`, then `h<=4b` gives

    Pr[first B member is after K]
      <= exp(-bK/n) <= exp(-Lambda).

If `K=n`, that probability is zero. Moreover `alpha>=kappa` implies `U<=n+1`, so on every continuing branch `L=O(n Lambda)`. A union bound over all virtual coordinates makes the probability of any truncated prefix at most `delta` (with the chosen `Lambda`; enlarging the absolute constant handles the finitely many smallest `n`). Thus, on the coverage and prefix good events, every genuine residual pair appears in the actual truncated virtual list.

### Compression creates no false witness

Suppose distinct virtual coordinates form a 2-Sum hit. If their original indices differ, they are a genuine input witness. If both coordinates map to the same original index `r`, then

    2x_r=t,

so `x_r in F`, contradicting the definition of `B`. The same argument persists through every recursion level: two different non-fixed partner values cannot originate at one original position. Returned candidates are unwrapped and verified, so even bad primitive outcomes cannot create an accepted false positive.

Combining the fixed-point, search, sampling, count, coverage, prefix, child, and nested-oracle good events gives success probability at least `2/3`.

## 6. Worst-case query cap (D2 repair)

The high-probability residual inequality is used only for correctness of the abort decision; it is never used to permit an unbounded branch. The query schedule is bounded on every branch because:

- fixed-point and partner searches have predetermined `O(sqrt(n)log(1/delta))` caps;
- zero/counting is stopped after `O(sqrt(n)log(1/delta))` queries;
- a branch continues only with `h<=4U`;
- `L` is then fixed by `h`, and each virtual evaluation searches only a fixed prefix `K<=n`;
- the child is itself a bounded-query algorithm by induction; and
- each virtual oracle receives a predetermined `O(log(M/delta))` amplification count.

Thus a bad sample, a bad count, or a bad permutation can change the answer but cannot exceed the claimed query cap. This is the missing D2 invariant.

The review proposed aborting when an upper estimate is too large. V2 agrees, but strengthens the implementation in one necessary way: all recursive sizes and costs are analyzed in terms of the **capped estimate `h`**, not the unknown actual `b`. On a count-failure event `h` need not approximate `b`; the explicit `h<=4U` gate and prefix truncation still bound the work. This is an implementation-level completion of the reviewer's repair, not a mathematical disagreement.

## 7. Query analysis, including the short-compression subcase (D1)

Suppress factors polynomial in `log n` whose degree depends only on the fixed depth. For an active level, `alpha>=1/2`. The nonrecursive work is therefore `O-tilde(n^alpha)`.

A virtual query costs

    O-tilde(sqrt(K))=O-tilde(sqrt(n/h)),

where the equality includes the harmless cap `K=n` when `h` is very small. The virtual length is `L=O-tilde(h)`.

### Case I: the child remains in ABI's small-range regime

Suppose `q<=L^(2/3)`. By induction,

    Q(A_(i-1);L,q)=O-tilde(L^a_(i-1) q^c_(i-1)).

Consequently the recursive contribution is

    O-tilde(n^(1/2) h^(a_(i-1)-1/2) q^c_(i-1)).

Since `a_(i-1)>=1/2`, this is nondecreasing in `h`. On every continuing branch,

    h<=4U=O(q n^(1-alpha)).

Constants and logarithms do not affect the exponent, so the normalized exponent is

    1/2+(1-alpha)(a_(i-1)-1/2)
       +kappa(a_(i-1)-1/2+c_(i-1)).

With `alpha=T_i(kappa)`, direct substitution gives exactly `T_i(kappa)`, the ABI balance at `claw.tex:263-281`.

### Case II: the actual virtual list is too short

Suppose instead

    q>L^(2/3).

The inductive small-range formula is not applicable. V2 switches to the Johnson base. Its original-query cost is

    O-tilde(sqrt(n/h) L^(2/3))
      =O-tilde(n^(1/2)h^(1/6)).

Because `h<=L<q^(3/2)` in this case,

    O-tilde(n^(1/2)h^(1/6))
      <=O-tilde(n^(1/2)q^(1/4)).

For `0<=kappa<=2/3`, if `d_i=2^(i+2)-1`, then

    T_i(kappa)-(1/2+kappa/4)
      =(2-3kappa)/(4d_i) >= 0.

So the Johnson fallback also costs at most `O-tilde(n^T_i(kappa))`. This is D1's missing branch. The review wrote the same idea using the actual residual size `b`; v2 uses the capped estimate `h` and the actual virtual length `L=Theta(h log n)`, which is required to make D1 and D2 coexist. There is no substantive divergence from the reviewer's inequality.

### Query-accounting table

| Component at length `n` | Worst-case original queries | Charged correctness event | Fits level budget because |
|---|---:|---|---|
| Fixed-point multiplicity, at most four searches | `O(sqrt(n)log(1/delta))` | missed first/second occurrence | `alpha>=1/2` |
| Load sample | `ell<=O(n^alpha Lambda)` | heavy value missed | definition of `ell` |
| Check pairs inside sample | `0` additional | none | stored values |
| Search outside for sample partner | `O(sqrt(n)log(1/delta))` | Grover failure | `alpha>=1/2` |
| Zero test + relative count | capped `O(sqrt(n)log(1/delta))` | zero/count failure | `alpha>=1/2` |
| One virtual value | `O(sqrt(K)log(M/delta))=O-tilde(sqrt(n/h))` | prefix/minimum/oracle failure | fixed `K<=n` |
| In-range child | `O-tilde(n^T_i(kappa))` | child/nested error | ABI balance |
| Short-list Johnson child | `O-tilde(n^(1/2)q^(1/4))` | walk/nested error | D1 inequality |
| Abort on `h>4U` or malformed count | no recursive queries | sample/count bad event | D2 cap |
| Unwrap + final witness verification | at most two extra virtual evaluations per active level, plus two final input queries | nested-oracle event only; final check exact | absorbed by the corresponding level budgets |

## 8. Finish the exponent and spend epsilon once

For fixed depth `D`, induction gives

    Q(A_D;N,q)=O-tilde(N^a_D q^c_D)

throughout `2<=q<=N^(2/3)`, with

    a_D -> 1/2,    c_D<=1/4.

Given the theorem's requested `epsilon>0`, choose the constant depth so that

    a_D<=1/2+epsilon/2.

Then use the remaining `epsilon/2` to absorb the fixed-depth polylogarithmic overhead for all sufficiently large `N`. Hence

    Q(A_D;N,q)
      <= O_epsilon(N^(1/2+epsilon)q^(1/4)).

This fixes review defect D3: v1 spent `epsilon` once in the depth and a second time on logarithms. For `q>N^(2/3)`, the Johnson base gives the same final bound as noted in Section 1. The theorem is a fixed-depth family depending on `epsilon`; no uniform `N^(1/2+o(1))q^(1/4)` claim is made.

## 9. Review-repair ledger, numerical sanity checks, and limitations

### Repairs relative to v1

- **D1 MAJOR:** the child explicitly switches to Johnson when its actual virtual length `L` does not satisfy `q<=L^(2/3)`; Section 7 proves this subcase stays below `T_i`.
- **D2 MAJOR:** capped counting, the `h<=4U` continuation gate, fixed `L,K`, prefix truncation, and bounded child calls give a worst-case query cap even on every bad event.
- **D3 MINOR:** depth consumes `epsilon/2` and logarithms consume `epsilon/2`.
- **D4 MINOR:** all possible first/second fixed-point search failures are named, candidates are verified, and the error union includes all at most four searches.

**Divergence from the reviewer's repairs:** no mathematical defect was found in either proposed repair. V2 replaces the review's informal residual parameter `b` by the algorithmically available capped upper estimate `h`, includes the logarithmic virtual length in the D1 switch, and truncates the first-residual oracle. These are explicit bounded-query completions of the same repairs.

### NUMERICAL sanity evidence — pending-review

These runs do not prove the theorem and do not change B4a's `CONJECTURED` status.

1. Exact rational recurrence/D1 identities.
   - Command: `"<machine-local-path-redacted>" ksum/tools/ksum_b4v2_exponents.py`
   - Raw log: `ksum/artifacts/logs_ksum_B4_20260718/ksum_b4v2_exponents.log`
   - Script SHA-256: `a31f2ebe76e7c9c59d3f9bbd6d47e10dd853ce8f592f3df7ad6b2e8c79ed5364`
2. Finite cyclic fixed-point/same-index check.
   - Command: `"<machine-local-path-redacted>" ksum/tools/ksum_b4v2_fixedpoints.py`
   - Raw log: `ksum/artifacts/logs_ksum_B4_20260718/ksum_b4v2_fixedpoints.log`
   - Script SHA-256: `9bb028882ca48eeb49df3ec3a5ea3b8638e307b5accefaa4610ddf57e0da2ccb`
3. V1 immutability, rule-6 labels, DAG synchronization, and manifest consistency.
   - Command: `"<machine-local-path-redacted>" ksum/tools/ksum_b4v2_artifacts.py`
   - Raw log: `ksum/artifacts/logs_ksum_B4_20260718/ksum_b4v2_artifacts.log`
   - Script SHA-256: `9786156592c1d13575b570743a893e2670bb67ec9e9727687544b7a0a816ea65`

Hash manifest: `ksum/artifacts/logs_ksum_B4_20260718/ksum_b4v2_sha256.txt`. Repair-session provenance: `ksum/artifacts/logs_ksum_B4_20260718/codex_repair_run.log`.

### Remaining known gaps / what this pass did not check

- A second fresh reviewer has not checked v2. Rule 6 therefore leaves the note **CONJECTURED pending-review (v2)**.
- I did not re-prove or independently literature-check Grover search, the Johnson/MNRS walk, approximate counting, minimum finding, or coherent error reduction. Section 3 states the exact standard guarantees used; no on-disk pinned circuit-level composition theorem was located.
- I did not check gate, time, space, or random-bit efficiency. Truly random fixed permutations and classical lookup are free in query complexity.
- I did not audit ABI's lower bound or their unequal two-list residual sizes; the single-list construction has one residual size.
- I did not extend the result to arbitrary abelian groups with a growing set of solutions to `2v=t`; the bound `|F|<=2` is load-bearing.
- Apart from the two logged sanity scripts, I ran no instance simulation. No off-disk source was used.
