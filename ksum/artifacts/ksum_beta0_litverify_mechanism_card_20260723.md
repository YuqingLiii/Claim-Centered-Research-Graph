# β0 — Verify-before-cite + mechanism card (collision-dual / mass-correction inputs)

**Commission:** β0 of the β batch for node `KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core`
(open obligation: "Verify-before-cite pass on the collision-dual / mass-correction literature inputs").
**Executor:** fresh Opus 4.8 instance. **Date:** 2026-07-23.
**Evidence tier:** literature verification only. Nothing here is a proof; no completion-tier status is
asserted about any mathematical claim of this project. Verdicts are reported neutrally.

**Copyright discipline:** all mathematics restated in this file's own notation; at most one short
quotation (<15 words, attributed) per paper.

---

## 0. What was checked, and how

For each arXiv ID: (i) fetched the live abstract page and read title / authors / submission date /
abstract; (ii) for the two mechanism-bearing papers, downloaded the arXiv LaTeX e-print and read the
relevant sections directly, so that every section/lemma/equation cite below is against the **actual
source**, not a summarizer's paraphrase. This mattered: a fast-model summary of the paper body
mislabeled the central cancellation identity as "Lemma 15 / Equation 3"; the real label is
`eq:pleasethishastoenddiediedie` inside Theorem `thm:collision_main`. Every label below was read from
the primary source.

Fetch/download provenance:

| Resource | URL | Retrieved | What it gave |
|---|---|---|---|
| Abstract 1503.07261 | https://arxiv.org/abs/1503.07261 | 2026-07-23 | title/authors/date/abstract |
| Abstract 1302.6191 | https://arxiv.org/abs/1302.6191 | 2026-07-23 | title/authors/date/abstract |
| Abstract 1710.09079 | https://arxiv.org/abs/1710.09079 | 2026-07-23 | title/authors/date/abstract |
| Abstract 2002.08389 | https://arxiv.org/abs/2002.08389 | 2026-07-23 | title/authors/date/abstract |
| E-print 1503.07261 | https://arxiv.org/e-print/1503.07261 | 2026-07-23 | `collision_ed.tex` (read in full) |
| E-print 1710.09079 | https://arxiv.org/e-print/1710.09079 | 2026-07-23 | `arXiv_v3.tex` (k-distinctness + dual-block sections read) |

---

## 1. Per-ID verification table

| arXiv ID | Recon claim (title / authors / result) | Live check (2026-07-23) | Verdict |
|---|---|---|---|
| **1503.07261** | Bun–Thaler, "Dual Polynomials for Collision and Element Distinctness"; nonproduct collision dual, globally supported on multiplicity/type classes, correlation from **exact cancellation on the common bad orbit rather than a tensor product** | Title, authors (Mark Bun, Justin Thaler), submitted 25 Mar 2015 — all match. Abstract confirms explicit dual polynomials reproving Aaronson–Shi Ω̃(n^{1/3}) / Ω̃(n^{2/3}). Body confirms the mechanism claim at formula level (see §2): dual supported on `S_N × S_R`-orbits `R_{m,a,b}`; final witness is a **sum** `ψ = aψ₁+bψ₂` (not a product) that **exactly cancels on the bad orbit `R_{N/2,2,1}`** (`eq:pleasethishastoenddiediedie`, `thm:collision_main`). | **VERIFIED-MATCH** (bibliographic + mechanism) |
| **1302.6191** | Bun–Thaler, tight duals for symmetric Boolean functions on Hamming-weight orbits; the 1-D orbit template used later | Title "Dual Lower Bounds for Approximate Degree and Markov-Bernstein Inequalities", authors (Mark Bun, Justin Thaler), submitted 25 Feb 2013 — all match. Abstract confirms an explicit dual for the approximate degree of **any symmetric Boolean function** (answering a question of Špalek). Its template role is corroborated inside 1503.07261: the collision OR-dual `ω` is stated as a refinement of `[bt13, Prop 14]`, and `bt13` resolves in the 1503 bibliography to exactly this 1302.6191. | **VERIFIED-MATCH** (bibliographic + template role); see provenance note P2 |
| **1710.09079** | Bun–Kothari–Thaler, "The Polynomial Method Strikes Back"; orbit-supported k-distinctness with a **mass-correction** move (build high pure degree, then remove/correct out-of-domain mass, preserving correlation) | Title/authors/date (25 Oct 2017) match abstract **and** the existing verified library record (`ksum/literature/bun-kothari-thaler-2018-dual-polynomials`). Body confirms mass-correction at formula level (see §2f): Step 3 zeroes the Hamming-weight-`>N` tail via `prop:btzeroing` (`prop:prelim-mass` = tail exponentially small; `prop:correction` = correction object ν with no pure-high-degree loss). | **VERIFIED-MATCH** (bibliographic + mechanism; library-consistent) |
| **2002.08389** | Mande–Thaler–Zhu, "Improved Approximate Degree Bounds for k-distinctness"; nonproduct compose-and-correct over global multiplicity profiles | Title/authors/date (19 Feb 2020) match abstract **and** the existing verified library record (`ksum/literature/mande-thaler-zhu-2020-k-distinctness`). Abstract confirms the improved lower bound Ω(N^{3/4−1/(4k)}) for constant k≥4, applying to approximate degree. | **VERIFIED-MATCH** on ID/title/authors/main-claim (library-consistent); the *detailed* "compose-and-correct over multiplicity profiles" mechanism was **not** re-traced at formula level in this pass (see provenance note P4) |

**None unreachable; none mismatched.** All four IDs resolve; all four titles/authors match the recon.
The recon's stated cross-validation signal is also confirmed: 1710.09079, 2002.08389, and 2103.16390
are all present in `research/literature/` with the same arXiv IDs (ABI record shows arXiv 2103.16390v1).

---

## 2. Mechanism card — the collision/ED exact-cancellation dual + mass-correction

Template for a later construction commission. All cites are to `collision_ed.tex` (arXiv:1503.07261)
unless prefixed **[BKT]** (= `arXiv_v3.tex`, arXiv:1710.09079). Notation is this card's own.

### Setup / notation (this card)
- Inputs `x ∈ {−1,1}^n` are read as functions `g_x : [N] → [R]`, `R ≥ N` (§2.3, def. Collision).
- `T_k := { x : g_x is globally k-to-1 }` (each range value hit exactly `k` times) (def. Collision, line ~419).
- For a "split profile" triple `(m,a,b)`: `R_{m,a,b} :=` inputs where `m` domain elements are mapped
  `a`-to-1 and the other `N−m` are mapped `b`-to-1. **Definition is orbit-theoretic**: `R_{m,a,b}` is
  the orbit of a canonical representative `g_{m,a,b}` under the automorphism group **`S_N × S_R`**
  (`lem:symmetrization` preamble, line ~619). A triple is **valid** iff `a|m` and `b|(N−m)`.
- Collision as a promise LP dual: `φ` is an `(ε,d)`-dual for `COL_{N,R}` iff
  - (**correlation**) `Σ_{T₁} φ − Σ_{T₂} φ − Σ_{B} |φ| > ε·‖φ‖₁`, where `B` = inputs that are neither
    1-to-1 nor 2-to-1 (the "bad"/NO-adjacent mass), and
  - (**pure high degree ≥ d**) `Σ_x φ(x) χ_S(x) = 0` for every `|S| ≤ d` (`eq:prelim2`).
  Here YES `= T₁` (1-to-1), NO `= T₂` (2-to-1).

### (a) Support of the dual witness — which input classes carry mass
- The witness is supported **only on valid profile orbits**: `φ(x)=0` for all invalid `x`
  (Eq. `whoop`, line 520). So mass lives on the `S_N×S_R`-orbit lattice `{ R_{m,a,b} }`, i.e. on
  **global multiplicity/type classes**, never on individual inputs in isolation. This is the sense in
  which the construction is "globally supported on type classes."
- Warm-up Stage-1 witness `φ` (§3, `sec:firstlb`): mass only on `T_k` for divisors `k|N` that are (up
  to scaling) perfect squares — the exact analogue of the OR-dual living on Hamming shells `H_k`
  (`lem:or-dual`; discussion line 724–726). Gives only Ω(√(log N/log log N)).
- Optimal Stage-2 witness `ψ` (§4, `sec:mainlb`): mass on `R_{m,k,1}` and `R_{m,k,2}` for **many**
  valid triples, parameterized by a single bivariate weight function `Ψ(m,k)` (below).

### (b) Sign structure + the exact cancellation identity producing constant NO-side correlation
This is the antidote to product-correlation collapse. Two facts combine:

1. **Additive (non-product) assembly.** `ψ = a·ψ₁ + b·ψ₂` with `a = Σ_{T₁} ψ₁ = ω(1)` and
   `b = −Σ_{T₂} ψ₂ = −ω(2)` (proof of `thm:collision_main`, line 862). `ψ₁` puts ≈½ of its `L₁` mass
   on `T₁` (YES); `ψ₂` puts ≈½ on `T₂` (NO). Each `ψ_i` is itself a **sum**, not a product
   (`ψ₁ = ψ' + Σ_{invalid (N/2,a,1)} ψ''_{N/2,a,1}`, line 558). At no point is a tensor product over
   blocks/pairs taken — hence no per-factor correlation penalty.

2. **Exact cancellation on the single common bad orbit `R_{N/2,2,1}`.** `R_{N/2,2,1}` (half the domain
   2-to-1, half 1-to-1) sits in the bad set `B` and is the orbit both `ψ₁` and `ψ₂` load. `ψ₁,ψ₂` are
   built (`lem:intermediate`, Properties 6–8, line 842–844) so that, on this orbit,
   `a·ψ₁(x) + b·ψ₂(x) = 0` pointwise. The identity (`eq:pleasethishastoenddiediedie`, line 870):
   `Σ_{x∈R_{N/2,2,1}} |a·ψ₁(x)+b·ψ₂(x)| = 0`. The derivation (lines 873–878) uses:
   - Property 6: `Σ_{T₁} ψ₁ = Σ_{R_{N/2,2,1}} ψ₂`; Property 7: `Σ_{R_{N/2,2,1}} ψ₁ = Σ_{T₂} ψ₂`
     (the two witnesses' aggregate weights are cross-matched);
   - Property 8: `ψ₁, ψ₂` are **constant on each valid orbit** `R_{m,a,b}`, so on `R_{N/2,2,1}` each
     `ψ_i(x)` equals its orbit-average `(1/|R_{N/2,2,1}|)·Σ ψ_i`. Substituting collapses
     `aψ₁(x)+bψ₂(x)` to `(Σψ₂)(avg ψ₁) − (Σψ₁)(avg ψ₂) = 0`.
   Bun–Thaler design the two pieces "designed so that their values exactly cancel out" on this orbit
   (Bun–Thaler, §2 overview, paraphrased around the one quoted fragment). Net effect: the NO-adjacent
   `B`-mass that would kill correlation is annihilated by cancellation, giving
   `Σ_{T₁}ψ − Σ_{T₂}ψ − Σ_B|ψ| ≥ a²+b² − (a+b)δ ≥ ½ − 2δ` (constant), independent of how many orbits
   carry mass (`thm:collision_main`, line 884). **The constant correlation comes from one exact
   cancellation on one shared orbit, not from a product of small correlations.**

### (c) How pure high degree is bookkept (what forces high degree)
- "Pure high degree ≥ d" = no Fourier mass on characters of degree `≤ d` (`eq:prelim2`).
- **Additivity** (`lem:phd-sum`, line 890): if `ψ₁,ψ₂` each have pure high degree ≥ d, so does
  `ψ₁+ψ₂`. This is what licenses the additive assembly in (b) without degree loss.
- **Symmetrization bridge** (`lem:symmetrization`, line 623): for any degree-`d` `p` on `{−1,1}^n`
  there is a **trivariate degree-`d`** `P` with `P(m,a,b)=E_{x∈R_{m,a,b}}[p]` on valid triples. Proof
  route: multilinearize to `N·R` indicator variables `T_{ij}=1[g_x(i)=j]` (`lem:representation`,
  from bt14) then apply Kutin's symmetrization over the `S_N×S_R` orbit (`lem:kutin`). Because the
  witness is orbit-constant and supported only on valid orbits (Eq. `whoop`),
  `Σ_x ψ(x)χ_S(x) = Σ_{m,k} Ψ(m,k)·Q(m,k)` where `Q(m,k)=E_{R_{m,k,1}}[χ_S]` is a bivariate polynomial
  of degree ≤ d−1 in each variable (`eq:nomoreseriously`, line 964).
- **High degree is forced by using many orbits, killed by two 1-D symmetric-function duals.** Splitting
  `Ψ` (see (d)) makes `Σ_{m,k}Ψ(m,k)Q(m,k)` factor into (i) `Σ_k ω(k)Q(N/2,k)`, killed by the OR-dual's
  pure-high-degree property because `Q(N/2,·)` is a low-degree polynomial in `k`; and (ii) for each
  `k`, `Σ_r η_k(r)Q(r,k)`, killed by the MAJ-dual's pure-high-degree property because `Q(·,k)` is a
  low-degree polynomial in `r` (`eq:soveryveryclose`, lines 971–976). Degree budget: `K ≈ N^{2/3}`
  distinct `k`-shells and MAJ-dual threshold `ρ√δ·N/k` combine to `d = Ω(δ^{1/3}N^{1/3})`
  (`lem:intermediate`, `thm:collision_main`). **Pure degree scales with the number of orbit-shells used**
  (as in the OR/Hamming-shell template), which is why the construction must spread over many orbits.

### (d) The bivariate weight `Ψ` and the mass-correction step *(present already in 1503.07261)*
- Both `ψ₁,ψ₂` are generated by ONE bivariate weight (`Ψ`, line 906):
  `Ψ(m,k) = ω(k)·1[m=N/2] − (ω(k)/η_k(N/2))·1[k≥3]·η_k(m)`, where
  - `ω` = OR-dual on the multiplicity variable `k` (`lem:or-dual`): supported on `{1}∪{ci²}`,
    `ω(1)≈½`, `−ω(2)≈½`, `‖ω‖₁=1`, kills polynomials of degree `≤ ζ√(δL)` — a refinement of
    `[bt13 = 1302.6191, Prop 14]`;
  - `η_k` = MAJ-dual on the split variable `m` (`lem:maj-dual`): supported on `{2k,4k,…}∪{N/2}`,
    `η_k(N/2)≈½`, `‖η_k‖₁=1`, kills polynomials of degree `≤ ρ√δ·N/k` — a refinement of
    `[bt14, Prop 10]` (a *different* Bun–Thaler paper; see P2).
- `ψ₁` places weight `Ψ(m,k)` on `R_{m,k,1}` (spread uniformly over the orbit); `ψ₂` places `Ψ(m,k)`
  on `R_{m,k,2}` (definitions lines 924–929, 979–985).
- **What is corrected and why.** The raw first term `ω(k)·1[m=N/2]` would put weight on the point
  `(m,k)=(N/2,k)` even when `k ∤ N/2` — i.e. on **empty/invalid orbits** `R_{N/2,k,1}=∅`, which a real
  polynomial cannot do. The subtracted `−(ω(k)/η_k(N/2))·η_k(m)` term is the **mass-correction**: the
  MAJ-dual `η_k` redistributes that spurious weight from the invalid point `m=N/2` onto the **valid**
  points `m∈{2k,4k,…}` (where `k|m`), engineered so that `Ψ(N/2,k)=ω(k)−(ω(k)/η_k(N/2))·η_k(N/2)=0`
  for `k≥3` (line 954). **Cost:** the correction dumps extra `L₁` mass on the corrected orbits, bounded
  by `Σ_k |ω(k)/η_k(N/2)|·Σ_i|η_k(2ki)| ≤ 4Σ_k|ω(k)| ≤ δ/2` (lines 940–945) — a constant-fraction, not
  exponential, loss. This is exactly the "build a pure-high-degree object, then correct the mass it
  places on the wrong (here: empty) part of the profile lattice" move.

### (e) BKT mass-correction variant *(1710.09079 — the second correction template)*
1503.07261 corrects **empty/invalid** orbits; [BKT] corrects a **Hamming-weight overflow**, a cleaner
template for "high pure degree first, prune out-of-promise mass second":
- Target reduces to `ϕ_comp = OR_R ∘ THR^k_N` restricted to Hamming weight `≤ N` (`thm:dist-promise`,
  [BKT] line 2119).
- **Step 1** (`prop:thr-sym-dual`/`prop:thr-dual`, [BKT] 2152–2262): a `THR^k` dual `ψ` on the single
  weight variable `t`, supported on `{1,…,k}∪{ci²}`, sign-alternating, with a crucial
  **exponential Hamming-weight decay** `|ω(t)| ≤ (2k)^k e^{−c₂ t/√(kTN^{1/k})}/t²`
  (`eqn:thr-sym-decay`, line 2159).
- **Step 2** (`sec:k-dist-step2`): dual-block-compose `Φ ⧫ ψ` (`Φ` = OR_R dual, itself `ρ⧫φ` with `φ`
  an "error amplifier" and `ρ` a "degree amplifier", line 2271). Yields approximate degree
  `Ω(√R·√T) = Ω(R^{3/4−1/(2k)})` — but places mass on Hamming weight `> N`.
- **Step 3 — the mass-correction** (`prop:btzeroing`, [BKT] §2.7, line 1197): "zeroing out" the mass on
  Hamming weight `> N`. Two parts: `prop:prelim-mass` (the overflow mass is exponentially small,
  `≤ (2NR)^{−2Δ}`, thanks to Step-1 decay) and `prop:correction` (build a correction object `ν` that
  cancels the overflow **without lowering pure high degree**); `ζ = ξ + ν` is the final dual. Cost is
  negligible **because** the inner dual decays exponentially in Hamming weight. Refinement over the
  earlier Bun–Thaler surjectivity technique: works at `N=Θ(R)` rather than `N=Ω(R log²R)` (line 1212).

### (f) σ-twist dependency flags — where the collision promise (σ=id, r-to-1) is load-bearing
For the target node, NO = every involution pair `{a, t−a}` one-sided (fixed point ≤ once), YES = some
pair two-sided. Each item below is a place the collision mechanism **assumes σ=id / global r-to-1** and
would need rework. **Count: 8 (7 core + 1 conditional).**

1. **Symmetry group / symmetrization lemma (`lem:symmetrization`, S_N×S_R).** Collision's orbits and
   the "degree-d poly → low-degree poly in the profile parameters" bridge use the **full** `S_N × S_R`
   (range values freely permutable). The σ-twist symmetry is `S_N × C(σ)` where `C(σ)` must **preserve
   the pairing** `a ↔ t−a` — the hyperoctahedral-type group `S_2 ≀ S_{t/2}`, not `S_R`. **REWORK:**
   re-derive the symmetrization/degree bridge over the `S_N×C(σ)`-orbit lattice. This is the node's core
   "occupancy-profile lattice" task and gates everything in (c).

2. **Support classes: r-to-1 shells → per-pair occupancy profiles.** `T_k`/`R_{m,a,b}` are indexed by a
   single multiplicity `k`. The σ-twist analogue must record, per pair `{a,t−a}`, how many domain
   elements land on each side (an occupancy vector in `N^q`), a genuinely richer lattice. **REWORK:**
   define these classes and confirm they are the `S_N×C(σ)`-orbits (node's central definitional step).

3. **YES/NO dichotomy is global-uniform for collision, existential for 2-Sum.** Collision YES/NO are
   both *single-multiplicity global* profiles (`T₁` vs `T₂`), giving the clean two-piece
   `ψ = aψ₁+bψ₂`. 2-Sum YES = **∃** a two-sided pair (a disjunction/OR over Θ(q) pairs); NO = all pairs
   one-sided. **REWORK:** the `ψ₁`(YES)/`ψ₂`(NO) split does not port; a multi-orbit existential
   structure is needed. This is the structural root of kill-criterion **K1** (does NO-side correlation
   survive as the number of pairs grows?).

4. **The single shared bad orbit `R_{N/2,2,1}`.** Cancellation happens on exactly **one** orbit. The
   σ-twist analogue is "the one-sided/two-sided boundary" profile. **REWORK:** identify whether that
   boundary is a *single* orbit (cancellation exact and cheap, as in collision) or a family growing
   with `q` (cancellation must be arranged to avoid a per-pair factor). Directly stresses **K1**; must
   reproduce analogues of Properties 6–8 (cross-matched aggregates + orbit-constancy).

5. **1-D building-block duals (`ω` OR-dual, `η_k` MAJ-dual).** Collision's pieces are 1-D
   symmetric-function duals on a single count (`k`, or split `m`). The σ-twist count structure is
   plausibly intrinsically ≥2-D (per-pair occupancy); a 1-D template applied **per pair and multiplied**
   would reintroduce the very product/exponential-decay collapse the node exists to avoid. **REWORK:**
   decide whether 1-D templates suffice or a new genuinely 2-D non-product orbit template is required
   (this is the node's central bet, and the K4 non-factorization filter must be applied).

6. **Degree/parameter budget.** Collision: `K≈N^{2/3}` shells at the `m=N/2` pivot → degree `N^{1/3}`;
   ED lift `N≈M²` → `M^{2/3}`. Target here is `Ω(√N·q^{1/6+δ})` at `q=Θ(N^{2/3})` — a **√N-side** budget
   far above `N^{1/3}`. **REWORK:** recompute shell-count-vs-degree and the pivot for the pair lattice,
   and re-derive the MAJ-dual-style threshold. This is where kill-criterion **K3** (cap-sweep vs walk
   `O(N^{2/3})` and B4a `O_ε(N^{1/2+ε}q^{1/4})`) must be checked at both `q=5` and `q=Θ(N)` endpoints.

7. **Rigid modular pairing & range geometry (`R≥N`, free collisions).** Collision assumes `R≥N` and
   collisions can form between **any** domain pair. 2-Sum's `σ: a↔t−a` is **rigid** — every value
   belongs to exactly one pair, and "sums to `t`" restricts admissible configurations. **REWORK:** the
   orbit sizes `|R_{m,a,b}|` and the promise geometry must be recomputed for the rigid pairing; this
   rigidity is the essence of the σ-twist and the reason the target profile lattice is non-product.

8. **(Conditional) ED extension-lift (`thm:ed-reduction`).** The Collision→ED lift averages `ψ` over
   `S_N` subset-extensions `ext(x)`, preserving pure high degree exactly. If the 2-Sum route needs a
   promise→total (ED-like) lift, the extension operator must be made **σ-compatible** (respect the
   pairing). Only needed if a lift step is used; flagged for completeness.

**Reusable design principle (from §6 complementary slackness, lines 1100–1184):** Bun–Thaler support
the dual on `k`-to-1 inputs because those are the (near) maximum-error points of the optimal
BHT-collision-algorithm polynomial `p(x)=E_{|S|=r}[I_{ED,S}(x)·A_d(cross_S(x)/r)]` (Chebyshev extrema
of `cross_S`). **Analogue for 2-Sum:** locate the max-error orbits of the best 2-Sum algorithm
(walk / BHT-style) and support the profile-lattice dual there — a heuristic for *where* mass should sit,
not a hard dependency.

---

## 3. Provenance audit — recon claims NOT confirmed (or only partially) in the actual papers

The recon file (`ksum/artifacts/ksum_L2_litrecon_20260720.md`) is itself explicit that its IDs are
ChatGPT-reported and provenance-suspect. Findings of this pass:

- **P1 — "first decisive nonproduct example for function properties" (recon, on 1503.07261).** This
  exact editorial phrasing was **not** located as a verbatim claim in the paper. The *substance* it
  encodes (additive combination `ψ=aψ₁+bψ₂` with cancellation, not a tensor product) **is** confirmed
  (`thm:collision_main`, `lem:phd-sum`, `lem:intermediate`). Treat "first decisive nonproduct example"
  as the summarizer's framing, not a paper quote.

- **P2 — 1302.6191 as the source of the collision building blocks (recon).** Partially precise. Inside
  1503.07261, the OR-dual `ω` **does** refine `[bt13, Prop 14]`, and `bt13` resolves in the 1503
  bibliography to 1302.6191 — so 1302.6191 is genuinely the OR-dual/symmetric-function template, as
  claimed. **But** the MAJ-dual `η_k` (the mass-corrector) refines `[bt14, Prop 10]`, which is a
  *different* Bun–Thaler paper ("Hardness Amplification and the Approximate Degree of Constant-Depth
  Circuits", ECCC), **not** 1302.6191 — although MAJ is itself symmetric and 1302.6191's symmetric-
  function result covers it in principle. The recon's phrasings "Hamming-weight orbits" and
  "one-dimensional orbit-template" are corroborated by usage but are the recon's characterization, not
  verbatim from 1302.6191 (whose body was not read at formula level this pass — abstract only).

- **P3 — "mass-correction … outside the valid low-Hamming-weight/profile domain" (recon, on
  1710.09079).** Confirmed, with a precision fix: BKT's Step-3 correction (`prop:btzeroing`) zeroes mass
  on **Hamming weight `> N`** — a one-dimensional weight threshold, **not** a general multiplicity-
  profile correction. The "profile domain" wording overstates the object BKT actually corrects; the
  multiplicity-profile framing belongs to the recon's own synthesis (and, plausibly, to MTZ — see P4),
  not to the confirmed BKT mechanism.

- **P4 — 2002.08389 "nonproduct compose-and-correct over global multiplicity profiles" (recon).** The
  ID, title, authors, and headline exponent (Ω(N^{3/4−1/(4k)}), k≥4) are confirmed via the abstract and
  the existing library record. The **detailed mechanism claim** ("compose-and-correct over global
  multiplicity profiles") was **not** re-traced at formula level in the MTZ body in this pass; the
  library record verifies MTZ's *claim card* (the exponent), not its full construction. Anyone leaning
  on MTZ's mechanism as a template should commission a dedicated body-level trace before citing it that
  way. (It is *not* the primary mechanism source; 1503.07261 is.)

- **P5 — cross-validation signal (recon).** Confirmed true: 1710.09079, 2002.08389, and 2103.16390 are
  all present in `research/literature/` with matching arXiv IDs (ABI record: arXiv 2103.16390v1). As the
  recon itself notes, this raises but does not replace confidence.

- **P6 — everything in the recon's Q1 (gauge-fixing) and Q4 (small-range claw / Tani) buckets** is
  **out of scope** for β0 and was not checked here. Only the collision-dual / mass-correction inputs
  (Q2/Q3) were in scope. Those IDs (math/0604108, 1102.2047, 1812.03698, 1807.00481, 2201.02289, and the
  Tani update) remain ChatGPT-reported and unverified.

**No claim in scope was found false.** The two in-scope substantive claims (1503.07261 = exact-
cancellation-on-common-bad-orbit nonproduct dual; 1710.09079 = high-pure-degree-then-mass-correction)
are both verified at formula level. The corrections above are scope/attribution precisions, not
refutations.

---

## 4. Frozen-inputs list (disk files relied on)

Read-only inputs this pass depended on (no existing file was edited):

- `DAG_PROTOCOL.md` — the eight rules (evidence-tier discipline, rule 7/8).
- `ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core.yaml` — target node,
  claim, kill criteria K1–K4, σ-pair NO/YES definitions.
- `ksum/artifacts/ksum_L2_litrecon_20260720.md` — the recon under audit (ChatGPT-reported IDs/claims).
- `ksum/literature/bun-kothari-thaler-2018-dual-polynomials/README.md` — verified library
  record for 1710.09079 (title/authors/version/DOI/claim card); cross-referenced, not duplicated.
- `ksum/literature/mande-thaler-zhu-2020-k-distinctness/README.md` — verified library record
  for 2002.08389; cross-referenced, not duplicated.
- `ksum/literature/ambainis-balodis-iraids-2021-small-range-claw/README.md` — confirms
  2103.16390v1 is in the library (recon cross-validation check only).

External sources fetched (2026-07-23), used as primary evidence, cached to scratchpad (session-local,
not committed): arXiv abstracts for 1503.07261, 1302.6191, 1710.09079, 2002.08389; arXiv e-prints
`collision_ed.tex` (1503.07261) and `arXiv_v3.tex` (1710.09079).

**Scripts:** none written (only `curl`/`tar`/`grep`/read were used); no `.py` artifact, so no SHA-256
to record. E-print retrieval, for reproducibility:
`curl -sL https://arxiv.org/e-print/1503.07261 -o bt1503.tar.gz` and
`curl -sL https://arxiv.org/e-print/1710.09079 -o bkt1710.tar.gz`.

---

*Evidence tier: literature verification. This file makes no proof claim about k-Sum and opens no
completion gate on any node. Verdicts (VERIFIED-MATCH / PARTIAL) are bibliographic/mechanism-tracing
outcomes only.*
