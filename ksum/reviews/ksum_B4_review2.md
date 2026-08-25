# Independent hostile review, round 2: B4 cyclic 2-Sum upper bound

Review target: ksum/artifacts/ksum_B4_upper_note_v2.md
Reviewed SHA-256: 17eb214acf015ad3dd3b25db655527ead7b986e0baebb40e4c252de278e979b6

Required history checked:

- v1, ksum/artifacts/ksum_B4_upper_note.md, SHA-256 c99c681233b5795b089338532ca58f57d6c64a781ac35d7719be37b90ba91e84.
- round-1 review, ksum/artifacts/ksum_B4_review.md, SHA-256 bbad9575c6b746962b4df5565268c896a72cd7ad440ab88f75bc85037e7eb419.
- ABI source, ksum/artifacts/references/abi_2103.16390_src/claw.tex, SHA-256 a3cce85beb4780becfec3d7474f85f4945751ea8df422552b7eaea271904fef9.

Reviewer provenance: fresh Codex rule-6 completing reviewer, 2026-07-18. I did not author v1, v2, or the round-1 review, and was given no wanted verdict. No network was used. The review was analytic; no numerical script or finite-instance result was used as evidence. Run record: ksum/artifacts/logs_ksum_B4_20260718/codex_review2_run.log.

## Ruling

**PROVED.** V2 is a complete bounded-query proof of

    Q(2-Sum over Z_q, target t, N inputs)
      = O_epsilon(N^(1/2+epsilon) q^(1/4))

for every epsilon>0, all sufficiently large N, every integer q>=2, and every t in Z_q, with a single input list and a hit requiring distinct indices. Both round-1 MAJOR defects are discharged without breaking the recurrence or final parameter balance. Both MINOR defects are fixed. I found **0 new FATAL, 0 new MAJOR, and 0 new MINOR defects**.

This proves the upper side only. It does not close the middle-regime exponent gap: the proved lower bound has q^(1/6), while this upper bound has q^(1/4) and an arbitrarily small N^epsilon loss. There is no contradiction because 1/6<1/4.

## Defect-discharge table

| Round-1 item | V2 location | Verdict | Independent check |
|---|---|---|---|
| D1 MAJOR: child called below the inductive small-range hypothesis | lines 145-149, 227-248 | **DISCHARGED** | The child uses the inductive formula only when q<=L^(2/3) and otherwise uses Johnson. The fallback costs O-tilde(n^(1/2)h^(1/6)) <= O-tilde(n^(1/2)q^(1/4)) <= O-tilde(n^T_i(kappa)). |
| D2 MAJOR: no worst-case cap on bad sampling/counting branches | lines 126-150, 181-194 | **DISCHARGED** | Capped counting, the h<=4U gate, fixed L, fixed K<=n, capped virtual evaluation, and a bounded child give a deterministic cap for every randomness/outcome branch. The high-probability residual bound is used only for correctness of the abort. |
| D3 MINOR: epsilon spent twice | lines 265-284 | **DISCHARGED** | Depth uses epsilon/2; fixed-depth logarithms use the other epsilon/2. |
| D4 MINOR: fixed-point search error hidden by deterministic wording | lines 73-78, 92-100, 179 | **DISCHARGED** | All at most four searches are amplified and included in the error union; candidates are verified; missed multiplicity is explicitly a false-negative error event. |

## Independent re-derivation of D1

At an active level write q=n^kappa, alpha=T_i(kappa), and let the continuing count estimate be h. V2 fixes

    L=ceil(h Lambda),
    K=min{n,ceil(4(n/h)Lambda)}.

One virtual query costs O-tilde(sqrt(n/h)); when K=n, the discrepancy is only polylogarithmic because that case forces h=O(Lambda). Also L=O-tilde(h).

If q<=L^(2/3), put a=a_(i-1), c=c_(i-1). The recursive term is

    O-tilde(n^(1/2) h^(a-1/2) q^c).

Since a>=1/2, it is nondecreasing in h. The deterministic continuation gate gives h<=4U=O(q n^(1-alpha)), so the normalized n exponent is

    1/2 +(1-alpha)(a-1/2)
        +kappa(a-1/2+c).

Substituting a=2^i/(2^(i+1)-1), c=(2^(i-1)-1)/(2^(i+1)-1), and alpha=T_i(kappa) gives exactly T_i(kappa), matching ABI's balance.

If q>L^(2/3), the inductive formula is not used. Johnson on the virtual list costs

    O-tilde(sqrt(n/h) L^(2/3))
      = O-tilde(n^(1/2)h^(1/6)).

Here h<=L<q^(3/2), hence this is at most O-tilde(n^(1/2)q^(1/4)). Finally, with d_i=2^(i+2)-1,

    T_i(kappa)-(1/2+kappa/4)
      =(2-3kappa)/(4d_i) >= 0

for 0<=kappa<=2/3. Thus the fallback remains within the same level budget. This re-derivation uses v2's algorithmically available h, not the unknown b; that is the correct divergence from the round-1 sketch.

## Independent re-derivation of D2

On the sampling good event, every unseen non-fixed value has multiplicity below n^(1-alpha), so

    b<=q n^(1-alpha)<=U=ceil(q n^(1-alpha)).

On the counting good event, b<=h<=4b; therefore a good execution never aborts at h>4U. On an arbitrary bad event, a continuing execution still has the deterministic invariant 1<=h<=4U.

Consequently L=ceil(h Lambda) is fixed and bounded, K<=n, every minimum search is forcibly capped at O(sqrt(K)) queries, and the selected child is bounded by induction. The child has a known maximum M of virtual calls, so each virtual oracle can be coherently amplified to error O(delta/M) with fixed logarithmic overhead. No cost inequality relies on b<=U after the gate. Bad sampling, counting, or permutations may enter the correctness union but cannot create an over-budget path.

The deterministic gate preserves the good-event exponent balance because h<=4U=O(q n^(1-alpha)). D2's repair therefore does not damage D1 or the ABI recurrence.

## Standalone proof audit

### Algorithm, correctness, and soundness

- The top-level range switch is correct: recursion is used for 2<=q<=N^(2/3); above that, Johnson costs O(N^(2/3)) <= O(N^(1/2)q^(1/4)).
- At depth zero, the Johnson walk with r=Theta(s^(2/3)) has setup r, gap Theta(1/r), and marked fraction Omega((r/s)^2) for a fixed witness, giving O(s^(2/3)) list queries. Stored values make marking query-free and distinct virtual coordinates are enforced.
- For Z_q, 2v=t has at most two solutions. Searching for a first and second occurrence of each costs O(sqrt n) up to amplification. On the joint good event, excluding all fixed-point-valued indices removes no genuine remaining witness.
- The uniform sample has the stated size and all sample-internal pairs are checked. The single outside Grover predicate x_j in t-S catches every pair incident to a sampled non-fixed value, so no two-list bipartition is assumed.
- Compression covers every residual index except with probability at most b exp(-L/b). Good counting has h>=b, making this at most b exp(-Lambda). Also h<=4b makes the probability that one permutation's first residual lies after K at most exp(-Lambda); union over L=O(n Lambda) coordinates is below the allocation for sufficiently large n.
- A repeated virtual copy of one original index can form a virtual hit only if 2x_r=t. Such indices are excluded. All returned witnesses are unwrapped and checked at the original list, so bad internal events cannot create an accepted false positive. The tagged failure value at line 143 is a recognizable non-value, occurs only on the charged prefix event, and is never accepted without original-index verification.

### Query and error accounting

At an active level alpha>=1/2, so the fixed-point searches, partner search, zero test, capped relative count, and verification calls fit under the O-tilde(n^alpha) nonrecursive budget. Loading the sample costs O(n^alpha Lambda). The recursive contribution is covered by the two D1 cases. At most two additional virtual evaluations per returned witness per level are a constant additive multiple of the already bounded virtual-oracle cost.

All quantum primitives have explicit forced query caps. Ordinary search, counting, base-walk, sampling, coverage, prefix, the at most four fixed-point failures, and nested-oracle hybrid error form only O(D) event families. With delta=1/(200(D+1)) and the stated Lambda, their union is below 1/3; constant slack also absorbs the witness-unwrapping calls. The recursive depth is fixed before the input size is seen.

### Recursion closure and quantifiers

Induction yields

    Q(A_D;N,q)=O-tilde(N^a_D q^c_D),
    a_D=2^(D+1)/(2^(D+2)-1),
    c_D=(2^D-1)/(2^(D+2)-1)

for 2<=q<=N^(2/3). Here a_D decreases to 1/2 and c_D<1/4. Given epsilon>0, choose constant D with a_D<=1/2+epsilon/2, then absorb fixed-depth polylogarithms into N^(epsilon/2) for sufficiently large N. Enlarging the constant handles the finite remainder. This gives the claimed O_epsilon form, not a uniform little-o claim.

The proof uses the supplied target directly and handles odd and even q. It requires no parity assumption, no q<N assumption, and no claw bipartition.

## New defects

None. Defect count for v2: **0 FATAL, 0 MAJOR, 0 MINOR**.

The unmatched Markdown escape in v2 line 55 is typographical only. The explicit tagged-dummy convention at line 143 totalizes a failed virtual evaluation: predicates regard the tag as a non-value, and original witness verification prevents acceptance. Neither affects the mathematical algorithm.

## What I did not check

- I did not re-prove the literature-standard Grover, Johnson/MNRS, approximate-counting, quantum-minimum-finding, or coherent-amplification primitives. I checked that the exact guarantees v2 states suffice and that their query/error composition here is consistent.
- I did not audit ABI's lower-bound proof or its unequal two-list residual-size ambiguity; neither is used by this single-list upper-bound proof.
- I did not check time, gate, space, or random-bit complexity. The claim is only quantum query complexity.
- I did not extend the proof to arbitrary abelian groups. The cyclic bound on the number of fixed points is load-bearing.
- I did not run optional numerics or instance simulations because no remaining issue was numerically decisive.

## Status action

Under DAG_PROTOCOL.md rule 6, this completed fresh independent review licenses B4a as **PROVED**. B4 remains **OPEN** because its other AND-child is the unresolved exponent-matching obligation (q^(1/6) lower versus q^(1/4) upper), and the root remains **OPEN**.
