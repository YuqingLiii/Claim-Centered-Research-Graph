# KSUM W2 — Independent hostile audit of W1's Claw→2-SUM reduction verdict

**Date:** 2026-07-16. **Role:** Opus 4.8 executor/verifier as INDEPENDENT HOSTILE AUDITOR (G1: a self-audit is never a certification; I am the different process). **Target:** `ksum/artifacts/ksum_W1_claw_reduction_verdict.md`. **Mandate:** assume W1 contains an error and find it; confirmation acceptable only after genuine attack. **Provenance rule in force:** every number carries command/log/SHA; every quote carries file:line.

---

## 0. VERDICT (first)

**CONFIRMED.** After attacking **16 distinct surfaces** (§A-summary) — source authenticity, the claw definition/promise, both LB theorem statements and their hidden hypotheses, the base-certificate chain, the three no-collision cases, edge cases, restriction direction, per-position relabel, all-t shift (both directions), the general-G extension on 8 groups, odd-N, the q-range arithmetic, a fresh scoop sweep, and W1's own provenance triplets — **I found no defect that breaks or weakens the reduction.** My from-scratch checker (`ksum/tools/ksum_w2_independent_checker.py`, 484,470 encoding checks + all-t + 8 groups + edge cases) returns **ALL-PASS**, and W1's script reproduces **byte-identically**.

The result is a genuine **conditional theorem**: `Q(2-SUM_{Z_q,t,N}) = Ω(√N·q^{1/6})` for odd `5 ≤ q ≤ N−1` (ABI) or `≤ 2N−1` (Tani), all `t`, resting on the on-disk ABI/Tani claw lower bound. W1's own label **PROVED-BY-REDUCTION-MODULO-CITED-INPUT** is accurate and appropriately hedged.

**Findings against W1 are all LOW severity (none touches the even-N cyclic theorem):**

| # | Finding | Severity | Nature |
|---|---------|----------|--------|
| F1 | W1 calls odd-N "non-immediate" and defers it; in fact odd N **is** covered trivially by freezing one coordinate to `0` (never a used value, so it cannot collide). W1 **under-claimed**. | LOW | missed strengthening, not an error |
| F2 | §0 prose "this is **Θ**(N^{2/3})" at q=Θ(N): only the **Ω** direction is proved in the document. The matching O(N^{2/3}) 2-SUM upper bound (Childs–Eisenberg subset-finding / Ambainis walk, q-independent) is standard and would justify Θ, but W1 cites no UB. Strategist should cite it or write Ω. | LOW | text stronger than in-doc evidence |
| F3 | §6.3 "for any finite abelian G" is implicitly the **t=0** (more precisely t∈2G) case; the all-t equivalence (C4) is odd-q-only. W1 states this correctly in C4 but §6.3 could be read as claiming all-t generally. | LOW | precision |
| F4 | ABI's LB theorem is literally stated "for all k≥2" (claw.tex:294) with the **k<n** hypothesis only in the abstract; W1 correctly re-imposes k<n. Worth surfacing that the bare theorem statement omits it (Tani:391 confirms "M<G" is needed). | INFO | W1 handled it correctly |
| F5 | §6 "Verified" for even-q/non-cyclic refers to **encoding-correctness** (brute-forced), not the asymptotic bound (inherited from claw LB, unverifiable numerically per G11). Consistent with W1's own framing but the word "verified" is load-bearing. | INFO | disclosed elsewhere |

I also **disclose a bug in my own first checker** (§A2c): my initial all-t test compared the wrong target and produced 8,312 spurious "violations"; tracing it showed the *shift identity holds* and W1's script used the correct direction. I fixed my test; it now PASSES. This is reported for honesty and because it independently vindicates W1's C4 script logic.

---

## A1. Source re-verification

### Authenticity of the saved arXiv dumps — GENUINE.

`tar tzf` shows `abi_2103.16390_eprint.tar.gz` = {claw.tex, claw.bbl}; `tani_2410.02243_eprint.tar.gz` = {00README.json, main.bbl, main.tex, STpaperformat.sty, STpapersymbol.sty}. Tani's `00README.json` carries arXiv's standard `{"spec_version":1,"texlive_version":"2025","process":{"compiler":"pdflatex"}}` marker; ABI (2021) predates that format (bare .tex/.bbl) — both internally consistent with their arXiv vintages (file mtimes: ABI src `Mar 30 2021`, Tani src `Oct 8 2025`). SHA-256 (my `sha256sum`, all **match W1 §8**):

```
a3cce85beb4780becfec3d7474f85f4945751ea8df422552b7eaea271904fef9  abi_2103.16390_src/claw.tex
075e5e575fa6ef64c21f484e713273bf361362e4ce96e188b51f9206900b5760  abi_2103.16390_src/claw.bbl
ed3b1cf7a18edf86297af2a18f6198e72b58ca4b24ec53feaffd3462c5d0273f  tani_2410.02243_src/main.tex
273f09ee0a9d05ce68b98f41bf4a4d59f9c932f0b896097c6df2e41b33461c44  tani_2410.02243_src/main.bbl
a6b02a3960931d8756be09019e6b9cfc6bf556f71e2110b90c4a23f8b6f566a2  abi_2103.16390_eprint.tar.gz
4b4b1bd887b49695cbb56fbe2a868a6f2dd56908998d7b36ac16db2b95de4f8e  tani_2410.02243_eprint.tar.gz
```

### (a) Claw DEFINITION — CONFIRMED a single total decision function, no promise.

`claw.tex:125-133` (my Read, verbatim):
> `Let $\cl{n}{k}:\left[k\right]^{2n}\rightarrow\left\{ 0,1\right\}$ be defined as` … `$\cl{n}{k}\left(x_{1},\dots,x_{n},y_{1},\dots,y_{n}\right)=\begin{cases}1, & \text{if }\exists i,j\,x_{i}=y_{j}\\ 0, & \text{otherwise}\end{cases}$`

It is one **total** function on `[k]^{2n}` (a single oracle over 2n positions), no promise, and `∃i,j` allows `i=j`. W1's quote is faithful.

### (b) ABI LOWER-BOUND theorem — CONFIRMED, with a hypothesis note.

`claw.tex:293-294`:
> `\begin{thm} For all $k\geq2$, we have $Q\left(\cl{n}{k}\right)=\Omega\left(n^{1/2}k^{1/6}\right)$. \end{thm}`

Error model: bounded-error quantum query complexity `Q` (claw.tex:121-123). **No** "infinitely many n", **no** log caveats. The theorem statement omits `k<n`, but the abstract (`claw.tex:88-89`, "when `2≤k<n`") and the proof carry it, and **Tani:391 independently states the ABI bound holds "for `M<G`"** (range < domain). **W1 correctly re-imposes k<n in its own Theorem (W1:13).** (F4.) The proof (`claw.tex:296-330`) is a *reduction*, not a single adversary matrix: `f_{n,k}=Claw_{k→k}∘pSearch_{⌊n/k⌋}` padded into `Claw_{n→k+2}`, then `Q(Claw_{n→k}) ≥ Q(Claw_{k-2→k-2}∘pSearch_{⌊n/(k-2)⌋}) = Ω(k^{2/3}√(n/k)) = Ω(n^{1/2}k^{1/6})`. I checked the algebra `k^{2/3}·(n/k)^{1/2}=k^{1/6}n^{1/2}` and that for our regime `k<n` the floor `⌊n/(k-2)⌋≥1` gives the stated bound up to constants; at the ABI edge `k=n−1` it degenerates to `Ω(k^{2/3})=Ω(n^{2/3})` as claimed.

### (c) Tani statement + k-range — CONFIRMED verbatim (W1's combined-form quote is on-page).

`main.tex:356-361` (my Read):
> `\begin{theorem}` `Let $F,G,M\in\Natural$ be such that $F\le G\le F^2$ and $M< F+G$.` `Then, for every $M\in [2,F+G-1]$, the quantum query complexity of detecting the existence of a claw for a given function pair $(f,g)$ in $[M]^{[F]}\times[M]^{[G]}$ is lower-bounded by` `$\Omega\left(\sqrt{G}+F^{1/3}G^{1/6}M^{1/6}\right)$`

The combined form W1 quoted is **literally line 361** (the LHS of an equality to a 2-case bound, lines 364-368) — verbatim, not a paraphrase. Extra hypothesis **`F≤G≤F²`** (line 357): for W1's `F=G=n` this is `n≤n≤n²` ✓. At `F=G` the case split `(G/F)²=1` puts all `M∈[2,2n-1]` in the `Ω(F^{1/3}G^{1/6}M^{1/6})=Ω(n^{1/2}M^{1/6})` branch. `main.tex:374` ("`Setting F=G=N…recovers…Ω(N^{1/2}M^{1/6})` [ABI]") and `main.tex:391` (`M<G`) both match W1. Method `main.tex:335-337` is the **polynomial method / approximate degree** on the multisymmetric claw property — independent of ABI's Zhang+Brassard composition; the ABI citation at line 391 is in a *comparison* passage (showing Tani ≥ the ABI-reduction bound), not in Tani's main proof, so the independence holds.

### (d) ABI base certificate — CONFIRMED real & unconditional; Tani independent.

`claw.tex:322-326`: `Q(Claw_{k→k})=Ω(k^{2/3})` by **Zhang [Zha05]**, and the composition `Q(h∘pSearch_m)=Ω(Q(h)·√m)` by **Brassard et al. [BHK+19, Thm 13]**. Both resolve in `claw.bbl`: `[Zha05]` = Zhang, "Promised and distributed quantum search," COCOON 2005 (claw.bbl:91-95); `[BHK+19]` = Brassard, Høyer, Kalach, Kaplan, Laplante, Salvail, "Key establishment à la Merkle in a quantum world," *J. Cryptology* 32(3) 2019 (claw.bbl:34-38). Both are published, used unconditionally; the chain is claw-LB **builds on** Zhang (base) + Brassard (√m amplifier) with no conditional link. Tani supplies a wholly independent approximate-degree proof, so the claw bound survives even if one distrusts ABI's composition. (I did **not** re-derive Zhang/Brassard/Tani internals — see §What-I-did-not-check; same posture as W1 §9.)

### (e) q-range translations — RECOMPUTED, CONFIRMED.

- **ABI (k<n):** `k=(q−1)/2 < n=N/2 ⟺ q−1<N ⟺ q≤N` (integers); since q odd & N even, `q≠N`, so **`q≤N−1`**. ✓ matches W1.
- **Tani (k≤2n−1):** `(q−1)/2 ≤ 2n−1 = N−1 ⟺ q ≤ 2N−1`. ✓ matches W1.
- **Low end:** `k≥2 ⟺ q≥5`. W1's correction of P-W1-A from `q≥3` to `q≥5` is right (`q=3⇒k=1⇒`claw trivial). ✓
- `k^{1/6}=Ω(q^{1/6})`: `k=(q−1)/2≥q/3` for `q≥3`, so `k^{1/6}≥(q/3)^{1/6}=Ω(q^{1/6})`. ✓

Provenance: `ksum/artifacts/logs_ksum_W2_20260716/independent_checker.log` (SHA in §Provenance); source reads via Read tool at cited lines.

---

## A2. Independent attack on the reduction mathematics

My own checker `ksum/tools/ksum_w2_independent_checker.py` (self-hash `21b1bfba…`, run under `<machine-local-path-redacted>` Python 3.11.9). I wrote and ran it **before** reading W1's script. Log: `independent_checker.log`.

### (a) Three no-collision cases + edge cases — VERIFIED analytically and exhaustively.

For odd `q=2k+1`, encoding `x_i=f(i)∈{1..k}`, `x_{n+j}=(q−g(j))∈{k+1..2k}`:
- **within 1st half**: `f(a)+f(b)∈[2,2k]=[2,q−1]`, never `≡0`.
- **within 2nd half**: `≡−(g(a)+g(b))`, `g·+g·∈[2,2k]`, never `≡0`.
- **cross**: `≡f(i)−g(j)∈[1−k,k−1]`, `|·|<q`, `≡0 ⟺ f(i)=g(j)`.

TEST 1&2 (my log): **484,470** `(f,g)` pairs over `q∈{5,7,9,11}`, `n≤4` → **0 mismatches, 0 within-half zero-hits**. TEST 5 edge cases (my log): boundary `f=g=k` → cross `k+(q−k)=q≡0` = correct claw-1; within-1st `k+k=q−1≢0`; within-2nd `(q−k)+(q−k)≡1≢0`; diagonal `i=j` handled by the legal distinct pair `(i,n+i)`; genuine no-claw → 2sum=0. All **ok**. The encoding uses positions `i` and `n+i` consistently (I verified index alignment `f[i]↔x[i]`, `g[j]↔x[n+j]`). `q=2k+1` is exact for cyclic odd; there is no `q>2k+1` cyclic sub-case to worry about (that only arises in general-G, §f, where I test it).

### (b) Restriction direction — VALID (one-line proof).

`E:[k]^{2n}→Z_q^N` is a fixed per-coordinate injection with `2-SUM(E(z))=Claw(z)` for all `z` (=A2a). Any algorithm correct on all of `Z_q^N` is in particular correct on `E([k]^{2n})`, so `Q(Claw)=Q(2-SUM|_{E(·)}) ≤ Q(2-SUM_full)`. Restricting the input family cannot raise `Q`. Airtight; direction is the safe one (subdomain is *easier*).

### (c) Per-position relabel bijectivity + all-t shift — VERIFIED (after correcting my own test).

Relabel `σ_p:[k]↪Z_q` (identity for `p≤n`; `v↦q−v` for `p>n`) is injective per position → query-complexity-preserving (fixed unitary, 0 queries). **All-t:** for odd `q`, `2` is invertible. TEST 3 verifies **both** directions exhaustively over *all* `Z_q^N` (`q∈{3,5,7}`, N=4): Identity A (task A2e) `x'=x+t·inv2 ⇒ 2sum_t(x')=2sum_0(x)`; Identity B (W1 C4) `x''=x−t·inv2 ⇒ 2sum_0(x'')=2sum_t(x)`; plus each shift is a bijection of `Z_q^N`. Result: **0 violations, 0 non-bijective** over 20,175 instances.

> **Self-disclosure (honesty):** my *first* TEST 3 wrongly compared `2sum_0(x')` to `2sum_t(x)` — a target mismatch of `2t` — and reported 8,312 "violations." I traced it (`q=3,t=1,x=(0,0,0,1)`): the shift `+t·inv2` adds `2t·inv2=t` to every pairwise sum, so target-0 maps to target-**t**, and `2sum_0(x')=2sum_{−t}(x)`. The identity holds; the bug was mine. **W1's C4 script used the correct direction** (`twosum(x,q,t)==twosum(x−t/2,q,0)`, w1 script line 108), so W1 did not make this error. Fixed test PASSES.

### (d) Odd N — COVERED (W1 under-claimed; F1).

W1 (W1:77) calls odd-N padding "non-immediate (a dummy value −w always exists as some used value)" and defers it. But padding with **0** is safe: `0∉{1..k}∪{q−k..q−1}`, so a coordinate frozen to `0` satisfies `x_a+0=x_a≢0` for every real coordinate, and there is only one `0` (no `0+0` pair). Restricting `2-SUM` on `N=2n+1` positions to {position N ≡ 0, positions 1..2n encode a claw} gives `2-SUM = Claw_{n→k}`, hence `Q(2-SUM_{N odd}) ≥ Q(Claw_{(N−1)/2→k}) = Ω(√(N−1)·k^{1/6}) = Ω(√N·q^{1/6})`. Brute-forced (inline run, `q∈{5,7,9}`, N=2n+1 for n∈{2,3}): **5,242 (f,g) pairs, 0 mismatches, 0 dummy-0 collisions.** So odd N follows immediately — W1's caution was unnecessary (W1's fear applies only to *nonzero* dummies). Does not affect the even-N theorem.

### (e) "any t" shift — see (c). VERIFIED both directions + bijectivity, odd q only (correct; even-q needs t∈2G).

### (f) BONUS even-q / general-G extension — re-derived condition, formula, and 8-group brute force.

Correct condition: `S ⊆ G\{0}` with **`S ∩ (−S) = ∅`** (this *already* forces no within-half zero-sum AND no 2-torsion in S — the "no 2-torsion" clause W1 lists is redundant but not wrong). Encode `f↦S`, `g↦−S`; cross `s−s'=0 ⟺ s=s'`. Max `|S| = (|G|−|G[2]|)/2` (one representative per `±`-pair of non-2-torsion elements; always achievable — pick one per pair, no obstruction, so the general-G claim is a genuine theorem, not just small cases). TEST 4 (my log) computes `|G[2]|` generically and brute-forces the encoding:

| G | \|G\| | \|G[2]\| | predicted \|S\|=(q−\|G[2]\|)/2 | actual \|S\| | S∩(−S)=∅ | encoding |
|---|---|---|---|---|---|---|
| Z5 (odd cyclic) | 5 | 1 | 2 | 2 | ✓ | PASS |
| Z6 (even, W1) | 6 | 2 | 2 | 2 | ✓ | PASS |
| Z8 (even, W1) | 8 | 2 | 3 | 3 | ✓ | PASS |
| Z3×Z3 (odd noncyc, W1) | 9 | 1 | 4 | 4 | ✓ | PASS |
| **Z10 (even, NEW)** | 10 | 2 | 4 | 4 | ✓ | PASS |
| **Z2×Z4 (NEW, \|G[2]\|=4)** | 8 | 4 | 2 | 2 | ✓ | PASS |
| **Z2×Z2 (NEW, all 2-torsion)** | 4 | 4 | 0 | 0 | ✓ | (degenerate, correctly no S) |
| **Z15 (odd cyclic, NEW)** | 15 | 1 | 7 | 7 | ✓ | PASS |

The 4 groups W1 did **not** test (Z10, Z2×Z4, Z2×Z2, Z15) all confirm the formula, including `Z2×Z4` (the mandate's target: `|G[2]|=4 ⇒ |S|=2`, `S={(0,1),(1,1)}`) and the large-2-torsion boundary `Z2×Z2 ⇒ |S|=0` (no usable set — matches "small 2-torsion needed"). Explicit witnesses: Z8 `S={1,2,3}`, Z3×Z3 `S={(0,1),(1,0),(1,1),(1,2)}`. **The general-G claim is sound.** Caveat (as W1 disclosed): the *lower bound* at `|S|` still needs the claw LB to bind at range `M=|S|` within Tani's `M∈[2,F+G−1]`; the exact even-q endpoint constants were not re-derived by W1 or by me (the encoding is what's brute-forceable; the bound is inherited). "Verified" in W1 §6 means encoding-verified (F5).

---

## A3. Fresh scoop sweep (G7: negative search ≠ absence)

W1's 4 queries (W1:127) were paraphrases of "k-sum/claw reduction," "3SUM small universe," "2-sum modular Belovs open," "Tani multisymmetric consequence." I used **different** phrasings + the citation graph:

1. WebSearch "quantum query complexity 2-sum modular addition small alphabet lower bound claw reduction" → cluster {ABI 2103.16390, Rosmanis ED-small-range 1401.3826, BS 1206.6528, Tani 2410.02243, cheat-sheets, set-equality}. No claw→2-sum reduction.
2. WebSearch "Belovs Spalek k-sum alphabet size condition relax quantum lower bound 2026" → BS + refinements. A synthesized snippet noted a relaxation to `|q|≥2·C(n,k)` (≈`n²` for k=2 — **still quadratic**, not the q≈N regime; no scoop, no conflict).
3. WebSearch "quantum lower bound subset sum bipartite collision encoding two lists claw finding cryptography" → subset-sum/claw-finding **algorithms** (upper bounds), knapsack-claw, communication LBs. No LB reduction into small-alphabet k-sum.
4. WebSearch "'claw' quantum query lower bound implies k-sum OR 3-sum OR subset-sum small group modular" → engine's own synthesis: "the search results don't directly connect the claw problem to k-sum or subset-sum problems with small group settings."
5. **Semantic Scholar citation graph** (WebFetch, `api.semanticscholar.org/graph/v1/paper/arXiv:…/citations`): **ABI 2103.16390 is cited by exactly 1 paper — Tani 2410.02243 — and Tani has 0 citing papers.** No k-sum/2-sum connection in either.

**Verdict: not scooped, on the evidence searched.** Not searched: paywalled full texts, arXiv full-text/Scholar, non-English venues (S2 citation data is also non-exhaustive).

---

## A4. W1 report-quality audit + provenance spot-checks

**Provenance triplets — 3 spot-checked, all accurate:**
1. W1 script `ksum/tools/ksum_w1_verify_encoding.py` SHA `199a2ce5fab86329e67e718ee3447ccb433225ce6a99a420912c5e9ee42c3cf3` — **matches** W1 §8. Its log `logs_ksum_W1_20260716/verify_encoding.log` SHA `7d42b9ca2a05066b05cc49c7d16dce4282017b831d7ab5926918dda0d27ee074` — **matches** W1 §8. My re-run (`w1_rerun.log`) is **byte-identical** (same SHA `7d42b9ca…`; `diff` clean).
2. Counts **77,598** (C1) and **1,002,762** (C4) — reproduced exactly by re-run.
3. Agent-D anchors: `D_direct_atlas.log:3` `(n=2,q=3)=2.000000`, `:9` `(n=2,q=5)=2.000056`, `:15` `(n=3,q=3)=2.418636` — all present and matching W1 §5's cited values.

**Overclaim / stronger-than-evidence scan:** the only items are F2 (the "Θ(N^{2/3})" prose vs the proved Ω direction) and the F3 precision point on §6.3's "any G." Everything else in W1 is either proved, correctly hedged, or explicitly disclosed. The headline "pushes the Ω(N^{2/3}) threshold from q≥N² to q≈N" is accurate as a **lower-bound** statement (at q=Θ(N), `√N·q^{1/6}=Θ(N^{2/3})` as an expression ⇒ `Q=Ω(N^{2/3})`; the interpolation `√N ≤ √N·q^{1/6} ≤ N^{2/3}` for `5≤q≤~N` is correct). W1's attack-list §4 and witness §5 (no clean single adversary matrix; the object is a relabel/pullback of ABI's composition or Tani's dual polynomial) are honest.

---

## A-summary: surfaces attacked (16), all no-hit

Source SHA/tar/README authenticity · claw single-function/no-promise · ABI LB statement + k<n hypothesis · Tani statement + k-range + F≤G≤F² · base-cert Zhang/Brassard + Tani independence · encoding 3 no-collision cases (484k checks) · within-half never-zero · edge cases (boundary/diagonal/no-claw) · restriction direction · per-position relabel bijectivity · all-t shift both directions + bijectivity · general-G formula on 8 groups (4 new) · odd-N · q-range arithmetic · scoop (4 web + S2 graph) · W1 provenance triplets (3). **No defect found that breaks or weakens the reduction.**

---

## WHAT I DID NOT CHECK (disclosure ≠ certification)

- **Internal proofs of the granted inputs.** I verified the *statements* and *citations* of Zhang [Zha05] Ω(k^{2/3}), Brassard [BHK+19 Thm 13] pSearch composition, and Tani's degree theorem (th:DegreeOfClawForSmallRange / th:ComplexityClawWithSmallerRange), and that ABI and Tani are two independent methods reaching the same bound. I did **not** re-derive any of them line-by-line. The theorem is proved **modulo** these on-disk inputs (same posture as W1 §9).
- **No numerical adversary/dual-object pullback** at (N=6,q=5) or beyond — beyond the exact-SDP ceiling and asymptotically invisible (q^{1/6} needs N≈256; G11). The anchor relation is argued, not computed. (Consistent with W1 §5, §9.)
- **Even-q / non-cyclic endpoint constants** — the encodings are brute-forced correct on 8 groups, but I did not re-derive the exact `M∈[2,F+G−1]` binding constant for `|S|=(q−|G[2]|)/2` (F5; W1 §9 also flags this).
- **The 2-SUM O(N^{2/3}) upper bound** justifying "Θ" (F2) — believed standard (Childs–Eisenberg subset finding / Ambainis walk, q-independent) but not verified or cited here.
- **Scoop:** paywalled full texts, arXiv full-text/Google Scholar, non-English venues; S2 citation data is not exhaustive.
- **k-SUM for k≥3** — out of scope by design (the reduction is intrinsically 2-body/bipartite).

---

## Provenance

Interpreter: `<machine-local-path-redacted>` (Python 3.11.9).

My script: `ksum/tools/ksum_w2_independent_checker.py` SHA-256 `21b1bfbab9502ac789f3d5f5c7b4e91c1151c177fee24e8e68626c1fe6a53b41`.
Command: `python ksum/tools/ksum_w2_independent_checker.py 2>&1 | tee ksum/artifacts/logs_ksum_W2_20260716/independent_checker.log`.
My log: `ksum/artifacts/logs_ksum_W2_20260716/independent_checker.log` SHA-256 `f95a476870be39ccf3c5273d3e5781a7a24745f9349a633f2205971661b764d3` (OVERALL: ALL-PASS, exit 0).

W1 re-run: `python ksum/tools/ksum_w1_verify_encoding.py > ksum/artifacts/logs_ksum_W2_20260716/w1_rerun.log 2>&1` → SHA-256 `7d42b9ca2a05066b05cc49c7d16dce4282017b831d7ab5926918dda0d27ee074` (identical to W1's original log; `diff` clean). W1 script SHA `199a2ce5fab86329e67e718ee3447ccb433225ce6a99a420912c5e9ee42c3cf3` (matches W1 §8).

Sources verified at: `ksum/artifacts/references/abi_2103.16390_src/{claw.tex,claw.bbl}`, `ksum/artifacts/references/tani_2410.02243_src/{main.tex,main.bbl}`, `ksum/artifacts/references/BS_1206.6528v2_ksum.tex` (SHAs in A1). No git commits made.
