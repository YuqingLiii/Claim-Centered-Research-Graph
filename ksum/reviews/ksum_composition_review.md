# Independent hostile review — R-A composed through W3E-2

Date: 2026-07-18  
Reviewer role: fresh completing reviewer under `DAG_PROTOCOL.md` rule 6; authored none of the donor, embedding, or proposed composition, and was given no wanted verdict.  
Target: C-A / DAG node L2eC, formulated but left `CONJECTURED · pending-review` in `ksum/artifacts/ksum_W_review.md`.  
Run provenance: `ksum/artifacts/logs_ksum_W_20260718/codex_comp_review_run.log`. The PowerShell launcher failed before executing repository commands because the local sandbox helper was absent; the review then read the on-disk sources through the Node filesystem interface. No network was used and no numerical experiment was needed.

## Ruling

**PASS for the exact composition; L2eC is PROVED.** There is no mathematical defect after retaining the qualifications already present in the on-disk C-A statement: `N=kn`, `2<=R<=n`, and only the explicitly constructed modulus family. The result holds for every target and has no parity restriction.

**The proposed novelty gloss is rejected.** The sentence that this creates a new lower-bound envelope in a zone where “nothing” was known is false relative to this paper: Theorem C / Theorem `thm:kfloor` already proves a bound at least as strong at every covered point. This is a **MAJOR significance/positioning defect**, not a defect in the composed inequality. The original `ksum/artifacts/ksum_W_review.md` correctly called C-A dominated and claimed no new envelope.

## Exact chain check

### 1. Donor hypotheses

The independently reviewed R-A statement is, for fixed `k>=3`,

`Q(Coll_{k,n->R}) = Omega(sqrt(n) min{R,n}^{1/6})`, for `R>=2`.

Restricting to `2<=R<=n` removes the kink and gives `Omega(sqrt(n) R^{1/6})`. Here `Coll_{k,n->R}` is exactly Definition `def:kcoll`: `k` lists, each of length `n`, with one oracle over `kn` positions. No promise or average-case hypothesis is introduced.

### 2. Embedding bookkeeping

Lemma `lem:embed` fixes `k>=3` and `R>=2`. It concatenates the `k` donor lists, so the target k-Sum instance has **exactly**

`N = kn`.

This is not a statement for arbitrary `N`. No padding lemma is used or needed, and there is no parity case: every good k-subset takes one position from each block, while Appendix A excludes every wrong block-multiplicity pattern.

Put

`omega = 2R-1`,

`P_k(R) = k(R-1) ((2R-1)^{k-1}-1)/(2R-2)`,

`M_k = ((2k+1)^{k-1}-1)/2`.

The formal main construction uses the exact integer modulus

`q_k(R) = (P_k(R)+1)(M_k+1)`.

Since `P_k(R)=Theta_k(R^{k-1})`, this is `q_k(R)=Theta_k(R^{k-1})`; the hidden constants depend only on fixed `k`.

### 3. Every target and constants

For target zero the displayed tags in Lemma `lem:embed` give the exact iff reduction. For arbitrary `t`, Lemma `lem:embed-allt` chooses fixed tags summing to `t` and requires

`q > (binom(2k-1,k)-1)(2P+1)`.

The main modulus satisfies this condition. Write `C=binom(2k-1,k)-1`. It is enough that `M_k+1>2C`, because `(2P+1)/(P+1)<2`. For `k=3`, this is `25>18`. For `k>=4`,

`2C < 2(2k-1)^{k-1}/(k-1)! <= (2k-1)^{k-1}/3 < (2k+1)^{k-1}/2 < M_k+1`.

The arbitrary-target tags depend only on `k,R,t`, not on the oracle input. Their existence therefore incurs no query cost. This handles every `t in Z_{q_k(R)}`, including when `gcd(k,q_k(R))>1`; no odd-modulus or parity hypothesis is present.

Each per-block symbol map is injective on the donor alphabet: for `a!=a'`, `0<|u_j(a-a')|<=P/k<q`, so the difference cannot vanish modulo `q`. It is therefore a bijective relabeling onto that coordinate's restricted image.

A query to a k-Sum coordinate is simulated from the corresponding donor coordinate by the paper's standard per-coordinate relabeling: two donor XOR-oracle calls compute and uncompute the donor symbol, and all tag/payload arithmetic is input-independent. Hence

`Q(Coll_{k,n->R}) <= 2 Q(k-Sum_{Z_q,t,N})`.

The absolute factor 2, `sqrt(n)=sqrt(N)/sqrt(k)`, and the constants in `q_k(R)=Theta_k(R^{k-1})` are all absorbed by `Omega_k`.

### 4. Exact licensed statement

For every fixed integer `k>=3`, every integer `n>=2`, every integer `R` with `2<=R<=n`, and every `t in Z_{q_k(R)}`, setting `N=kn` and `q=q_k(R)` gives

`Q(k-Sum_{Z_q,t,N}) = Omega_k(sqrt(N) q^{1/(6(k-1))})`.

Equivalently, this is `Omega_k(sqrt(N) R^{1/6})`.

## Constructed-moduli-only audit

The `Theta_k` notation describes the growth of the exact sequence `q_k(R)`; it is **not** an all-moduli interpolation. For fixed `k` and input length `N=kn`, the licensed set is

`F_{k,n} = { q_k(R) : R=2,3,...,n }`.

The sequence is strictly increasing and has `n-1` points through its endpoint. Its counting function is `Theta_k(X^{1/(k-1)})`, so for `k>=3` it has natural density zero among the integers. More precisely,

`q_k(R+1)-q_k(R)=Theta_k(R^{k-2})`

and

`q_k(R+1)/q_k(R)=1+Theta_k(1/R)`.

Thus the family becomes multiplicatively dense asymptotically while remaining additively sparse; no statement for a modulus between consecutive construction points follows here. The endpoint is

`q_k(n)=Theta_k(n^{k-1})=Theta_k(N^{k-1})`.

Within the zone `q=Omega_k(N)`, only family points with `R=Omega_k(N^{1/(k-1)})` are covered.

For orientation, the main `k=3` family is `q_3(R)=150R(R-1)+25`; `R=2` gives `(N,q)=(6,325)`. The paper also records a smaller specialized zero-target recipe at `q=21R^2-8`; it is not needed for, and is not included in, the licensed main-family statement above.

## Sanity against upper and existing lower bounds

At `R=n`, `q=q_k(n)=Theta_k(N^{k-1})` and the composed lower bound is `Omega_k(N^{2/3})`. For every `2<=R<=n` it is at most this endpoint scale. Tani's range-independent walk upper bound is `O(N^{k/(k+1)})`, and

`2/3 < k/(k+1)` for every `k>=3`.

Therefore the composition never exceeds the known upper bound; there is no fatal contradiction.

Theorem C / Theorem `thm:kfloor` is stronger throughout the same family. Below its plateau it gives `Omega_k(sqrt(N) q^{1/6})`, which dominates the composition's exponent `1/(6(k-1))`; from `q=Theta_k(N)` upward it gives `Omega_k(N^{2/3})`, while the composition is at most that scale and reaches it only at `R=Theta(n)`. Consequently C-A is a valid independent corollary but supplies **no new lower-bound envelope**, including between `Theta_k(N)` and `Theta_k(N^{k-1})`.

There is no overlap with the Belovs--Spalek threshold `q>=N^k` for asymptotically large `N`, because the construction stops at `Theta_k(N^{k-1})`.

## Defect ledger

1. **No mathematical defect in on-disk C-A.** Its `N=kn`, constructed-family, and domination qualifications are correct.
2. **MAJOR significance defect in the intake gloss:** “new” bounds in a zone where “nothing” was known is false relative to Theorem C; the composed bound is dominated everywhere.
3. **Quantifier hazard, excluded from the licensed statement:** arbitrary `N` is not proved; the embedding gives exactly `N=kn`.
4. **Family hazard, excluded from the licensed statement:** `q=Theta_k(R^{k-1})` does not quantify over every comparable modulus. It names the exact sequence `q_k(R)` above.

## What I did not check

- I did not re-prove R-A or re-run its independent review; I imported its PROVED statement from `ksum/artifacts/ksum_W_review.md`.
- I did not re-certify W3E-2's encoding algebra by exhaustive enumeration. I read the integrated Section 4 and Appendix A proofs, checked the all-target size condition and parameter composition, and relied on the already-PROVED F1 audit for the underlying iff encoding.
- I did not prove padding to nonmultiples of `k`, interpolation to unconstructed moduli, or an extension to all `q` above a construction threshold.
- I did not perform a new literature search or make a priority claim outside the repository. The rejected “nothing known” statement is refuted internally by this paper's Theorem C.
- I did not run `ksum/tools/ksum_compr_*.py` or a new tiny-instance enumeration: the exact symbolic chain and prior independent exhaustive W3E-2 audit made numerics non-decisive.
- I did not review C-B/L2fC or any other donor branch.

## Pinned source provenance

- `ksum/artifacts/ksum_W_review.md` SHA-256 `0c2491f616e474071a222b8cdc74f603de38f2c29572baab40c1dda3a3091aab`.
- `ksum/paper/ksum_small_alphabet.tex` SHA-256 `e56ada9eafe7c99bb5e2bf3ac3849a2b261433fe06390da864d472eb4fcd4380`.
- `ksum/tools/ksum_f1_embed.py` SHA-256 `ca5bdbbcbfd1e6886e143903ccd29ff53a8b5f3932bd5aeb1e9870ecad5c2678`.
- `ksum/artifacts/logs_ksum_F1_20260718/embed_audit.log` SHA-256 `e92eee2c4144092bc0a3e02353f37255109189009b58d5ca86f84ad4541b84e4`.

## Status propagation

L2eC moves from `CONJECTURED · pending-review` to `PROVED` with this completed review cited. It is a dotted partial-outcome node, not a walk-optimal donor route, and its proved consequence is dominated by Theorem C. Therefore L2 remains `OPEN · PARKED`, B2 remains `OPEN`, and the root remains `OPEN`.
