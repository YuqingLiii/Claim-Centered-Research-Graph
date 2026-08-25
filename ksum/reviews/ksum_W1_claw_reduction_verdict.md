# KSUM W1 — Claw → 2-SUM reduction: adversarial verdict

**Date:** 2026-07-16. **Role:** Opus 4.8 executor/verifier, adversarial mandate (assume the reduction is WRONG; confirm only after genuinely trying to break it). **Strategist:** Fable 5 (registered predictions P-W1-A/B/C below). **Provenance rule in force:** every quote carries file+line; every number carries command/log/SHA.

---

## 0. VERDICT (first)

**The reduction SURVIVES at full strength. Registered prediction P-W1-A is CONFIRMED**, with one immaterial boundary tightening: the new content begins at **q ≥ 5**, not q ≥ 3 (q = 3 ⇒ range k = 1 ⇒ the claw is trivially always-1, so the bound there is only the base √N with no q^{1/6} gain). Both predicted failure modes **P-W1-C(a) search-vs-decision and P-W1-C(b) oracle-model DID NOT fire.**

**Theorem W1** *(label: **PROVED-BY-REDUCTION-MODULO-CITED-INPUT**; the cited input is the ABI claw lower bound `abi_2103.16390_src/claw.tex:293-294`, independently reproved by Tani `tani_2410.02243_src/main.tex:356-374`, both now on disk).*

> Let q be **odd**, q ≥ 5, write k = (q−1)/2 ≥ 2. Let N = 2n be even with the claw domain n satisfying **k < n** (i.e. N ≥ q+1; via Tani's wider range k ≤ 2n−1 it suffices that N ≥ (q+1)/2, i.e. 5 ≤ q ≤ 2N−1). Then for **every** target t ∈ Z_q, the bounded-error quantum query complexity of 2-SUM over Z_q on N inputs is
>
>   Q(2-SUM_{Z_q, t, N}) = Ω( √N · ((q−1)/2)^{1/6} ) = Ω( √N · q^{1/6} ).

At the top of the range (q = Θ(N)) this is Θ(N^{2/3}); it **pushes the Ω(N^{2/3}) threshold for 2-SUM down from q ≥ N² (Belovs–Špalek) to q ≈ N**, and gives a nontrivial interpolation √N ≤ Ω(√N q^{1/6}) ≤ N^{2/3} across 5 ≤ q ≤ ~N for all odd q — precisely the open region the commission isolated (`KSUM_STAGE0_VERDICT.md:13`: "all odd-order cyclic G in particular … stands").

**Why this is not the hoped-for-answer talking:** the tasking embedded the hope (P-W1-A). I attacked the reduction on ~10 fronts (§4) — decision-vs-search, oracle model, promise, k-range, direction of the reduction, alphabet-embedding, base-certificate validity, all-t, even-q, scoop — and it holds on all of them. The only material discovery *against* the registered prediction is the q ≥ 5 (not q ≥ 3) start, which is a triviality (k = 1 degeneracy), not a weakening. I also found the "odd" hypothesis is **not necessary** (small-2-torsion even q and non-cyclic odd G also work — §6, my extension, verified but labelled separately).

---

## 1. Verbatim source quotes (with file+line in the saved sources)

**Source acquisition (G2 satisfied — worked from the LaTeX sources, not summaries).** Files saved to `ksum/artifacts/references/`, SHA-256 in §8.

### ABI — arXiv:2103.16390, "A Note About Claw Function With a Small Range" (Ambainis, Balodis, Iraids)

Definition (`claw.tex:125-133`), one **single** function on `[k]^{2n}` (this is the whole ballgame for the oracle-model attack):
> `\cl{n}{k}:[k]^{2n}\to\{0,1\}` … `= 1 if ∃ i,j  x_i = y_j, else 0.`

Lower-bound theorem (`claw.tex:293-294`), a **decision** problem:
> "For all `k≥2`, we have `Q(\cl{n}{k}) = Ω(n^{1/2}k^{1/6})`."

Abstract range (`claw.tex:88-89`): "between `Ω(n^{1/2}k^{1/6})` and `O(n^{1/2+ε}k^{1/4})` when `2≤k<n`."

Proof method (`claw.tex:296-330`): a **reduction**, NOT a single adversary matrix — `f_{n,k}=\cl{k}{k}∘pSearch_{⌊n/k⌋}` padded (`*`→k+1 on the x-side, →k+2 on the y-side) into `\cl{n}{k+2}`; then `Q(\cl{k}{k})=Ω(k^{2/3})` by Zhang [Zha05] composed with the pSearch theorem `Q(h∘pSearch_m)=Ω(Q(h)√m)` [BHK+19, Thm 13] ⇒ `Q(\cl{n}{k}) ≥ Ω(k^{2/3}√(n/k)) = Ω(n^{1/2}k^{1/6})`.

### Tani — arXiv:2410.02243, "Approximate Degrees of Multisymmetric Properties…" (independent corroboration, different method)

Main small-range theorem (`main.tex:356-366`), **decision**, no promise:
> "for every `M∈[2,F+G-1]`, the quantum query complexity of detecting the existence of a claw for a given function pair `(f,g)` in `[M]^{[F]}×[M]^{[G]}` is lower-bounded by `Ω(√G + F^{1/3}G^{1/6}M^{1/6})`."

Recovers ABI (`main.tex:374`): "Setting `F=G=N` in the theorem recovers the lower bound `Ω(N^{1/2}M^{1/6})` [ABI]."
Explicit equal-domain citation of ABI (`main.tex:391`): "the quantum query complexity of `claw_{(G,G)→M}` for `M<G` is `Ω(G^{1/2}M^{1/6})` [ABI]."
Method (`main.tex:335-343`): "By the polynomial method, [the degree theorem] implies the optimal lower bound on the bounded-error quantum query complexity of both claw detection and claw finding" — an **approximate-degree / multisymmetric-polynomial** proof, wholly independent of ABI's Zhang+Brassard composition.

### BS — arXiv:1206.6528, "Adversary Lower Bound for the k-sum Problem" (target problem's definition + the open problem)

k-SUM definition (`BS_1206.6528v2_ksum.tex:100`):
> "the `k-sum problem` consists in deciding whether the input string `x_1,…,x_n∈group` contains a **subset of k elements** that sums up to `t`." (distinct indices; k=2 ⇒ ∃ a<b: x_a+x_b=t — matches the encoding.)

The open problem this reduction addresses (`BS_..._ksum.tex:388`):
> "Our technique relies crucially on the `n^k` lower bound on the alphabet size. Can one relax this bound…? element distinctness is nontrivial when `q≥n`, but our lower bound only holds for `q≥n²`."

---

## 2. Notation reconciliation (a real trap — flagged)

ABI's claw domain is `n`; its input string has length `2n`. The strategist's / commission's 2-SUM position count is **N = 2n**. Agent D's exact-Adv± logs use "n" for the **2-SUM position count** (`D_direct_atlas.log:1` "n=2 q=3" has `|D|=q^n`, PSDdim=2·q^n). So **Agent-D-"n" = my N = 2·(ABI-claw-domain)**. All statements below are in the (N = positions, q = |Z_q|) convention.

---

## 3. The chain C1–C5 (verify or break, every step)

### C1 — encoding correctness: 2-SUM(encode(f,g)) = claw(f,g) EXACTLY. **VERIFIED (analytic + exhaustive).**
Encoding (strategist's): N=2n, q=2k+1, t=0; x_i=f(i)∈{1..k} (i∈[1..n]); x_{n+j}=(q−g(j)) mod q ∈{k+1..2k} (j∈[1..n]).
- Within first half: f(a)+f(b)∈[2,2k]; q=2k+1>2k ⇒ never ≡0. ✔
- Within second half: −(g(a)+g(b)), g(·)+g(·)∈[2,2k] ⇒ never ≡0. ✔
- Across halves: f(i)−g(j), |·|≤k−1<q ⇒ ≡0 iff f(i)=g(j). ✔ (diagonal claw case i=j uses the legal distinct pair (i, n+i).)
Hence 2-SUM = claw. **Brute-force (`ksum/tools/ksum_w1_verify_encoding.py`, log `verify_encoding.log`): 77,598 (f,g) pairs over n≤4, k≤4 — 0 mismatches, 0 within-half zero-hits. PASS.**

### C2 — simulation / oracle direction. **VERIFIED.**
ABI's claw IS a single function on `[k]^{2n}` (`claw.tex:125`) — the "two functions" is conceptual; formally one oracle over 2n positions. The 2-SUM oracle is one oracle over N=2n positions. **They are the same oracle model up to a fixed per-position injective relabel** σ_p: [k]↪Z_q (identity for p≤n; v↦q−v for p>n). Query complexity is invariant under fixed per-position injective value relabeling and under oracle-encoding conventions (Buhrman–de Wolf). Therefore Q(2-SUM restricted to the encoded subdomain) = Q(Claw_{n→k}) **exactly**; the naive read-into-ancilla simulation costs ≤2 claw-queries per 2-SUM query, an irrelevant constant. Direction: a total-input 2-SUM algorithm is correct on the encoded subdomain, hence solves claw ⇒ **Q(2-SUM_full) ≥ Q(2-SUM_subdomain) = Q(Claw) = Ω(√N k^{1/6})**. Airtight.

### C3 — chained statement, exact range. **VERIFIED (see §0 theorem).**
k=(q−1)/2; for q≥5, k≥2 and k=(q−1)/2 ≥ q/3 ⇒ k^{1/6} = Ω(q^{1/6}); √n = √(N/2) = Ω(√N). Literal bound Ω(√N·((q−1)/2)^{1/6}); constant not read off O(·) (G5). Range: ABI needs k<n ⇒ N>q−1 ⇒ q≤N−1; Tani widens to k≤2n−1 ⇒ q≤2N−1. **q odd, but "not of the form 2k+1" is vacuous — every odd q IS 2k+1.** N odd: N=2n is always even; odd-N padding is non-immediate (a dummy value −w always exists as some used value) but irrelevant to the even-N statement. No promise/log caveats in ABI's or Tani's theorem statements.

### C4 — extension to all t (odd q). **VERIFIED (elementary + exhaustive), no C7 needed.**
For odd q, 2 is invertible; the per-position shift x_p ↦ x_p − t/2 is a fixed bijection carrying 2-SUM_{Z_q,t} to 2-SUM_{Z_q,0} (x_a+x_b=t ⟺ (x_a−t/2)+(x_b−t/2)=0). Query-complexity-preserving ⇒ Q(2-SUM_{Z_q,t}) = Q(2-SUM_{Z_q,0}) for all t. **Brute force: 1,002,762 strings over q∈{3,5,7,9}, all t, 0 mismatches. PASS.** (This is a cleaner, self-contained proof of the τ=1/all-t equivalence than the C7 machinery cited in `KSUM_STAGE0_VERDICT.md:65-67`; it agrees with it.)

### C5 — what it does NOT give / scope. **VERIFIED, and partly RELAXED (see §6).**
- k-SUM for k≥3: **out of scope** — the reduction is intrinsically 2-body/bipartite (claw compares two lists; the negation trick works only because the two lists are distinct positions). Correct.
- Large 2-torsion groups (|G[2]|=Θ(q), e.g. Z_2^m): the claw route degenerates (usable value set S has size (q−|G[2]|)/2 → small/zero), but these are covered by the ED-restriction theorem when |G[2]|≥n (`KSUM_STAGE0_VERDICT.md:13`, Ω(n^{2/3})). Complementary, not overlapping. Correct.
- Odd non-cyclic G: the strategist routed this through C7; I find it holds **directly** (§6), no C7 dependence.

---

## 4. Attack list (STEP 2) — outcomes

| # | Attack | Outcome |
|---|--------|---------|
| (a) | decision vs search in the LB | **Does not fire.** ABI `\cl{n}{k}:[k]^{2n}→{0,1}` is decision (`claw.tex:125,294`); Tani states detection (`main.tex:358`). 2-SUM is decision. Match. |
| (b) | oracle model (two vs one; superposition across f,g) | **Does not fire.** ABI's claw is literally one function on `[k]^{2n}`; the "two oracles" never exists formally. Same single-oracle model as 2-SUM up to fixed per-position relabel (C2). |
| (c) | k-range translated to q-range | **Survives, tightened.** ABI 2≤k<n ⇒ 5≤q≤N−1; Tani 2≤k≤2n−1 ⇒ 5≤q≤2N−1. Lower end q≥5 (not 3). |
| (d) | claw "∃i,j" vs bipartite-only; do hard instances map INTO our subdomain? | **Survives.** ABI's claw is exactly bipartite cross-list (x_i vs y_j), never within-list — matches encoding (within-half never hits 0). The encoding covers ALL of [k]^{2n}, so **every** ABI/Tani hard instance (incl. the pSearch-padded ones, values in [k]) maps in. |
| (e) | bounded-error / promise | **Survives.** No promise in either theorem statement. Even if there were, promise-claw ⊂ our subdomain ⇒ still Q(2-SUM_full) ≥ Q(promise). |
| (f) | hidden logs / "infinitely many n" | **None.** ABI/Tani bounds are clean Ω with no log factors, all-k / all-M∈[2,F+G−1]. |
| (g) | scoop (claw→k-sum / collision→k-sum encoding) | **No scoop found** (§7); G7: negative search ≠ absence. |

Additional self-generated attacks that also fail to break it: **direction** (subdomain is easier than full ⇒ bound direction correct); **alphabet embedding** (larger Z_q alphabet only makes 2-SUM harder; encoded inputs use all nonzero values, 0 unused); **multiset vs subset 2-SUM** (a=b needs 2x_a=0 ⇒ x_a=0, never used ⇒ same answer); **base-certificate validity** (ABI rests on Zhang [Zha05] + Brassard [BHK+19 Thm 13], both real published — `claw.bbl:80-95,34-38`; Tani gives a fully independent approx-degree proof, so the claw bound survives even if one distrusts ABI's composition step).

---

## 5. Witness-object analysis (STEP 3 ii–iii)

**Certificate underlying the cited LB.** ABI's is a *composition*, not a single matrix: [Aaronson–Shi collision polynomial Ω((·)^{1/3}) → Zhang Ω(k^{2/3}) for Claw_{k→k}] ⊗ [Brassard et al. pSearch composition, √m factor], glued by `*`-padding. Tani's is a *dual polynomial* certifying approximate degree Ω(√G+(FG)^{1/3}) of the multisymmetric claw property, pulled to smaller range via multisymmetric-polynomial symmetrization; both ultimately root in Aaronson–Shi.

**Pull-back through the encoding.** The encoding E is a fixed injective relabel per position, so a dual polynomial (or adversary matrix Γ) for Claw_{n→k} pulls back verbatim to one for 2-SUM restricted to E([k]^{2n}) with the **same value**, extended by 0 to full 2-SUM ⇒ Adv±(2-SUM_{Z_q,N}) ≥ Adv±(Claw_{n→k}) = Ω(√N q^{1/6}). It is a *composition/relabel of a dual object*, not a fresh single matrix — there is no "one clean 2-SUM adversary matrix" to exhibit; the honest statement is the query reduction.

**Smallest checkable (N,q) and the anchor relation.** Smallest nontrivial claw is k=2 (q=5) with k<n ⇒ n≥3 ⇒ **N=6, q=5**. Agent D's exact anchors sit at (N=2,q=3/4/5/7), (N=3,q=3)=2.418636, (N=4,q=3)=2.712711 (`D_direct_atlas.log:3,6,9,12,15`; (4,3) per `KSUM_STAGE0_VERDICT.md:121`). **None tests the reduction:** q=3 is k=1 (trivial claw), q=4 is even, and the sole q=5 anchor (N=2, =2.000056, `:9`) is claw-domain-1. The first witness point (N=6,q=5) has PSD dim ≈2·5^6≈3.1e4, at/above the ~10³ DNF ceiling (`KSUM_STAGE0_VERDICT.md:75`), so no fresh exact solve is readily available. And per the project's own permanent blocker (`:59-61`, `:100`) the q^{1/6} factor is numerically invisible at any reachable N (n^{1/6} separation needs N≈256). A pulled-back certified value would be ≤ Adv± by construction; this is a consistency guard, **not** an asymptotic confirmation (none is possible numerically — G11).

---

## 6. Extensions beyond the registered claim (MY additions — clearly separated, each verified)

These STRENGTHEN the result; they are not part of P-W1-A and carry my own verification, not the strategist's.

1. **The "odd" hypothesis is not needed for cyclic Z_q.** Replace {1..k} by any **sum-free-from-zero** set S⊂G\{0} with S∩(−S)=∅ and no 2-torsion (s+s≠0). Encode f(i)↦S, g(j)↦−S. Then within-halves never sum to 0 and cross sums to 0 iff labels match — 2-SUM(encoded)=claw. Max |S| = (q−|G[2]|)/2. For even **cyclic** q, |G[2]|=2 ⇒ |S|=(q−2)/2=Θ(q) ⇒ **Ω(√N q^{1/6}) for even q too** (q≥6). Verified: Z₆ (|S|=2), Z₈ (|S|=3), 0 mismatches (`verify_encoding.log`).
2. **Odd non-cyclic G (direct, no C7).** |G[2]|=1 ⇒ |S|=(q−1)/2=k ⇒ Ω(√N q^{1/6}) directly. Verified: Z₃×Z₃ (q=9, |S|=4), 0 mismatches. So `KSUM_STAGE0_VERDICT.md`'s "odd non-cyclic covered via C7" holds by the **same reduction**, more robustly than the C7 route.
3. **Unified scope statement.** The claw reduction gives Ω(√N·((q−|G[2]|)/2)^{1/6}) for any finite abelian G, useful when 2-torsion is small (|G[2]|=o(q)); the ED-restriction theorem covers large 2-torsion (|G[2]|≥n). Together they leave a gap only at intermediate 2-torsion. **Caveat (unverified at endpoints):** the claw LB needs the label count |S| within Tani's M∈[2,F+G−1]; for |S| near the top this is fine, but I did not re-derive the exact even-q endpoint constants.

---

## 7. Scoop-search log (STEP 2g; G7 — negative search ≠ proof of absence)

Queries run (WebSearch, 2026-07-16): (1) "quantum query complexity k-sum … claw function reduction lower bound"; (2) "quantum 3SUM small universe modular lower bound"; (3) "quantum lower bound 2-sum modular addition small group … Belovs open"; (4) "Tani multisymmetric claw detection approximate degree k-sum consequence". Plus disk: all **47** citing papers of BS 1206.6528 (`ksum/artifacts/bs_cites.json`) title-scanned.

Findings: every query returns the same cluster — BS k-SUM (large q), ABI claw small-range, Rosmanis/Ambainis ED-small-range, Belovs-2026 k-distinctness, Naya-Plasencia/Schrottenloher k-XOR **algorithms**. **No source states a claw→k-SUM (or collision→k-SUM) small-alphabet lower-bound reduction.** Zero of the 47 BS-citers has "claw" in title; the k-XOR/k-SUM citers (entries 12/18/40) are upper-bound/algorithm papers. The open problem is repeatedly **restated as still open** ("reduce the required group size in the Ω(N^{k/(k+1)}) k-SUM bound; k-SUM is O(√N) for constant-size groups") — consistent with `KSUM_STAGE0_VERDICT.md:9` (Belovs Apr-2026 "still assumes q=Ω(n²) and restates the open problem"). One search engine's *synthesized* prose speculated a claw→k-sum link, but it is the LLM's inference over juxtaposed abstracts, not a quoted result. **Verdict: not scooped, on the evidence searched.** Not searched: paywalled full texts, Google Scholar proper, arXiv full-text search, non-English venues.

---

## 8. Provenance

Interpreter: `<machine-local-path-redacted>` (Python 3.11.9).
Script: `ksum/tools/ksum_w1_verify_encoding.py` SHA-256 `199a2ce5fab86329e67e718ee3447ccb433225ce6a99a420912c5e9ee42c3cf3`.
Command: `python ksum/tools/ksum_w1_verify_encoding.py 2>&1 | tee ksum/artifacts/logs_ksum_W1_20260716/verify_encoding.log`.
Log: `ksum/artifacts/logs_ksum_W1_20260716/verify_encoding.log` SHA-256 `7d42b9ca2a05066b05cc49c7d16dce4282017b831d7ab5926918dda0d27ee074`.

Saved sources (`ksum/artifacts/references/`), SHA-256:
```
a6b02a3960931d8756be09019e6b9cfc6bf556f71e2110b90c4a23f8b6f566a2  abi_2103.16390_eprint.tar.gz
d373202c8ca65e006d20c4631687336116a19428514746814b90e6439fb2087b  abi_2103.16390_claw_smallrange.pdf
a3cce85beb4780becfec3d7474f85f4945751ea8df422552b7eaea271904fef9  abi_2103.16390_src/claw.tex
075e5e575fa6ef64c21f484e713273bf361362e4ce96e188b51f9206900b5760  abi_2103.16390_src/claw.bbl
4b4b1bd887b49695cbb56fbe2a868a6f2dd56908998d7b36ac16db2b95de4f8e  tani_2410.02243_eprint.tar.gz
a0740237235e1a8513abe1630bce10d988b9e63a133911a2bb57c155d2c7d225  tani_2410.02243_multisym_claw.pdf
ed3b1cf7a18edf86297af2a18f6198e72b58ca4b24ec53feaffd3462c5d0273f  tani_2410.02243_src/main.tex
273f09ee0a9d05ce68b98f41bf4a4d59f9c932f0b896097c6df2e41b33461c44  tani_2410.02243_src/main.bbl
```
Anchors reused (Agent D): `ksum/artifacts/logs_ksum_stage0_20260716/D_direct_atlas.log:3,9,15`. No git commits made.

---

## 9. WHAT I DID NOT CHECK (disclosure ≠ certification)

- **Deep correctness of the cited claw LB.** I verified ABI's and Tani's *theorem statements* verbatim and that their citations exist, and confirmed they agree (two independent methods). I did NOT re-verify Zhang [Zha05]'s Ω(k^{2/3}), the Brassard et al. [BHK+19 Thm 13] pSearch composition, or Tani's dual-polynomial construction line by line. The W1 theorem is PROVED-BY-REDUCTION **modulo** these on-disk inputs.
- **The pulled-back adversary matrix numerically.** Not built/solved at (N=6,q=5) — beyond the exact-SDP ceiling and asymptotically invisible anyway (G11). The anchor relation (pulled-back ≤ Adv±) is argued, not computed.
- **Even-q / non-cyclic endpoint constants** (§6): the encodings are exhaustively verified as *correct*, but I did not re-derive the exact k-range/constant at which Tani's M∈[2,F+G−1] binds for |S|=(q−|G[2]|)/2.
- **Odd-N padding**, k-SUM k≥3 (both out of scope by design).
- **Scoop:** paywalled full texts, arXiv full-text/Scholar, non-English venues (§7).

---

## 10. Registered-prediction scorecard

| Prediction | Outcome |
|---|---|
| **P-W1-A** survives full strength: Q(2-SUM,Z_q odd,any t)=Ω(√N q^{1/6}), 3≤q≤c·N | **CONFIRMED**, corrected to **5≤q≤c·N** (q=3 is the k=1 triviality). All-t ✔ (C4). c=1 via ABI, c=2 via Tani. |
| P-W1-B survives weakened | superseded — no weakening needed |
| P-W1-C dies at (a) search-vs-decision or (b) oracle-model | **Did NOT occur.** Both (a) and (b) fail to bite: ABI's claw is a decision function on a single `[k]^{2n}` oracle. |

**Route status: ALIVE. Result: a new odd-q (in fact small-2-torsion, incl. even cyclic and odd non-cyclic) lower bound Q(2-SUM_{G,t})=Ω(√N·((q−|G[2]|)/2)^{1/6}) for 5≤q≤~2N, all t, resting on the on-disk ABI/Tani claw theorem.**
