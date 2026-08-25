# β1 — concrete occupancy-profile-lattice ansatz + exact q=5 shadow check

**Target node (rule 8a):** `KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core`
(`ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core.yaml`).
Kill criteria K1–K4 pre-registered on that node (lines 40–49) govern this commission.

**STATUS OF EVERYTHING BELOW: NUMERICAL / CONJECTURED — pending-review.**
No completion-tier language is used. Every number is an exact finite falsification
diagnostic (SymPy/`Fraction` rational arithmetic); per **G11** no asymptotic exponent
is inferred from any of it. This artifact edits no existing file.

**Outcome class (see §7): B** — first concrete ansatz written; **K2 = CONTAINS**
(consistent, not inconsistent); **K1 = the ansatz does not deliver a q-gain** — its
constant-correlation degree is *exactly q-independent* on bounded-pair support and
scalar-capped at `Θ(√N)`, and the only instantiated route to a growing-with-q degree
(activating `Θ(q)` pairs by a product) decays **exactly** as M2's `2^(1-(q-1)/2)`.
The genuinely-non-product multi-pair law that could escape both is uninstantiated
(the node's "no coefficient law yet"); a real but finite-unresolved ceiling signal
keeps the node **OPEN, not refuted**.

---

## 0. Scope and frozen inputs (file:line)

Frozen — read, not re-derived (each within the scope of its cited reviewed record):

- **Kill criteria K1–K4, target claim** — `KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core.yaml:27`
  (`Ω(√N·q^(1/6+δ))` at `q=Θ(N^(2/3))`), `:40–49`.
- **The PROVED q=5 germ** — `KSUM.B4b.L2.ALT.two-orientation-shared-no-cascade.yaml:32`
  (PROVED, scoped q=5,K=2, odd N≥513), `:34` (`D=floor(sqrt(N/512))+2`), `:50–56`
  (Decision A: opposite weights at `s`,`N-s` cancel the shared NO atom; barycentric kernel +
  `h=64` quadratic bridge; unit `l1`, `F_<D W=0`, tail `1/4`, correlation `>4536/6565>2/3`).
- **Germ machinery (conventions copied exactly)** — `ksum/tools/ksum_l2p27_shared_no_rule7_independent.py`
  (five-colour `central_row` = `Σ_{g∈G} Π falling`, `two_sum` sign predicate `is_yes`,
  `collision_count`=C_t, `bridge_coeffs`, `shared_coeffs`); `ksum/tools/ksum_l2p27_shared_no_check.py`.
- **General-q exact orbit-moment LP** — `ksum/tools/ksum_l2p1_exact_moment_lp.py:39` (`centralizer_of_sigma`),
  `:63` (`two_sum_sign`), `:100–120` (`class_data`: falling-factorial occupancy moment rows,
  "exact S_N symmetrizations of query-indicator monomials", degree `<d`), `:126–175` (unit-`l1`
  signed-orbit-measure LP, `+1`/`-1` YES/NO encoding).
- **Degree/query convention** — `ksum/tools/ksum_l2p14_target_scale_sweep.py:1–8`
  ("D is a polynomial cutoff; moment degree is `<D`; query scale is `D/2`"); the LP never
  identifies D with a query count.
- **Product-class obstructions (K1 ancestors)** — M2 `KSUM.B4b.L2.M2.yaml:21`
  (sign-separated product / positive mixture, correlation **exactly** `2^(1-(q-1)/2)`, odd q≥5);
  ORIENT `KSUM.B4b.L2.ORIENT.yaml:21` (`2^(-r(m-1))`).
- **K4 pre-filter** — `KSUM.B4b.compcap.yaml:17,21–33` (block-factorized constructions cap at
  `O(√N·q^(1/6))`; the witness must *not* factorize across disjoint position blocks).
- **Problem conventions / odd-q scope / q=5 endpoint** — `ksum/notes/KSUM_PROVER_PROMPT.md`;
  `ksum/notes/KSUM_HANDOFF_20260720.md` phases 12–27 (finite machinery, Hahn-law
  failure, shared-NO construction).

Deliverable scripts (this artifact), SHA-256 recorded in §6:
`ksum_beta1_profile_lattice_ansatz_q5_20260723_{core,k2_germ,k1_trend,k1_qgain,k1_ceiling}.py`.

**Convention note / fixed choice.** WLOG target `t=0` (relabel by `a↦a-t·2^{-1}`; odd q makes
`2` invertible). Then `σ(a)=(-a) mod q`, the unique fixed point is colour `0`, and the
`P=(q-1)/2` involution pairs are `{i, q-i}`. `C(σ)=C_2≀S_P`, order `2^P·P!` (verified:
q=5→8, q=7→48, q=9→384 — matches `centralizer_of_sigma`). This is a documented choice;
`central_row` and the LP are invariant under it.

---

## 1. Formulation — the occupancy-profile lattice of 2-Sum at odd q

**Profiles.** A profile (occupancy histogram) is `n = (n_0,…,n_{q-1}) ∈ N^q`, `Σ n_a = N`,
where `n_a` = number of the `N` input columns carrying alphabet value `a`. `n_0` is the
fixed-point multiplicity `f`; each pair `i` carries an ordered split `(n_i, n_{q-i})`.

**Profile lattice / classes.** The instance symmetry is `S_N` (columns) `× C(σ)` (alphabet).
A **profile class** is a `C(σ)`-orbit of profiles: `C_2≀S_P` flips the two colours inside a
pair and permutes the `P` pairs, fixing colour 0. A class is therefore
`(f, multiset of unordered pair-splits {n_i, n_{q-i}})` — per-pair **total** `t_i=n_i+n_{q-i}`
and **imbalance** `|n_i-n_{q-i}|`, plus `f`. Constraint `f + Σ_i t_i = N`.

**Predicate (two_sum sign).** `YES` iff `f≥2` (fixed point twice) **or** some pair is
**two-sided** (`n_i>0` and `n_{q-i}>0`); `NO` otherwise (`f≤1` **and** every pair one-sided).
This is exactly the sigma-pair predicate; `NO` profiles = `(f∈{0,1},` all pairs one-sided`)`,
i.e. the complete **one-sided/two-sided boundary** is the codim-1 face `{min_i n_i·n_{q-i}=0,
f≤1}`. Collision count `C_t = C(f,2) + Σ_i n_i n_{q-i}` (`=0` on NO, `>0` on YES).

**Position-symmetrization map and "degree".** A degree-`d` multilinear query dual on inputs
`Z_q^N`, after `S_N` averaging, descends to a function on profile classes. The image basis is
the **falling-factorial occupancy moments**: for `α∈N^q`, `total(α)=Σ_a α_a`,
`R_α(n) = Σ_{g∈C(σ)} Π_a (g·n)_a^{underline{α_a}}` (integer central row;
`underline{k}` = falling factorial), the exact `S_N`-symmetrization of the degree-`total(α)`
query-indicator monomial (`ksum_l2p1_exact_moment_lp.py:100–120`). "Degree" therefore means:
input side = number of queried columns; profile side = `total(α)`. A unit-`l1` signed profile
measure `W` with `⟨W,R_α⟩=0` for every `total(α)<D` and sign-correlation `⟨W,sgn⟩=c` certifies
polynomial degree `D`, hence 2-Sum query lower bound scale `D/2` (`p14:1–8`). At q=5 the target
scale is `D=Θ(√N)`; the node's bet is `D=Ω(√N·q^(1/6+δ))` at `q=Θ(N^(2/3))`.

No convention was ambiguous on disk; the only free choice (`t=0`) is fixed above.

---

## 2. The ansatz — a global boundary-pairing dual on the profile lattice

**Atoms (boundary pairing / discrete derivative in the two-sidedness coordinate).**
For a NO backbone `ν = (f∈{0,1}, one-sided totals m_1≥…≥m_P)` and a pair `k` with `m_k≥2`,
the **single-flip** moves one column from the majority to the minority side of pair `k`:

    Δ_{ν,k} = δ[ Y_k(ν) ] − δ[ ν ],   Y_k(ν): split of pair k goes (m_k,0) → (m_k−1, 1).

`Y_k(ν)` is YES (pair `k` two-sided, minority `1`); `ν` is NO. `Δ_{ν,k}` is the exact discrete
derivative `∂_{u_k}` at the one-sided/two-sided boundary `u_k: 0→1`, holding `t_k=m_k` and all
other pairs fixed. This is (ii): the NO/YES contrast is a boundary pairing in the per-pair
two-sidedness coordinate, not a product over pairs or orientations.

**Witness.** `W = Σ_{ν,k} c_{ν,k} · Δ_{ν,k}`, free real parameters `c_{ν,k}` (weights over
profile shells) — (iii). Induced signed orbit-measure `w(class) = Σ c_{ν,k}(1[·=Y_k(ν)] −
1[·=ν])`, with **exact cancellation** when distinct `(ν,k)` share a canonical NO class
(the germ's *shared-NO* reflection: `ν` with totals `{s, N−s}` and its swap coincide, so
opposite `c` annihilate the duplicated NO atom). Because `w` is a single global sum over
profile classes (not `Π_i`), the witness is (i) globally supported, non-product.

For the LP we optimise over the **whole profile-lattice support** — the tightest well-defined
carrier of these atoms — which upper-bounds any specific coefficient law:
`supp = {all NO backbones} ∪ {single-flip minimal-YES}`. This is exactly the germ's carrier
(§3). Enriched variants tested: `deep_yes` (one pair two-sided, minority `1..D`); full-orbit
(all classes, the true ceiling).

**Annihilation / correlation as finite linear algebra at fixed (N,q).**

    maximise   c := Σ_class w(class)·sgn(class)          (sign correlation)
    subject to Σ_class w(class)·R_α(class) = 0   ∀ α, total(α) < D    (annihilation)
               Σ_class |w(class)| = 1                    (unit l1; w = p − n, p,n ≥ 0)

**Per-display type audit.**

| object | space | dimension (functions of N,q,D) |
|---|---|---|
| profile | `{n∈N^q : Σn=N}` | `C(N+q-1, q-1)` |
| `C(σ)` | `C_2≀S_P ⊂ S_q`, P=(q-1)/2 | `|G| = 2^P·P!` |
| profile class | `C(σ)`-orbit | ≤ `C(N+q-1,q-1)/? ` (generically `/|G|`) |
| NO backbones | `(f∈{0,1},` partition of `N−f` into ≤P parts`)` | `≈ 2·p_{≤P}(N)` |
| single-flip YES | one pair two-sided, minority 1 | `≈` #backbones with a part ≥2 |
| exponent `α` | `{α∈N^q : total(α)<D}`, deduped by `C(σ)` | ≤ `Σ_{t<D} C(t+q-1,q-1)` |
| moment row `R_α` | `Z`-valued on classes; integer `= Σ_{g∈G} Π falling` | one per distinct row |
| witness `w` | signed measure `class→Q`; `w=p−n` | `2·#classes` LP vars |
| correlation `c` | `Q`, `= ⟨w,sgn⟩` at `‖w‖_1=1` | scalar |

Every `R_α` is well typed: `g·n` is a genuine `C(σ)`-relabelling of a profile (colour
permutation fixing 0), and `falling(n_a,α_a)` is `0` unless `n_a≥α_a`, so empty colours
contribute the identity factor `falling(0,0)=1` and kill any `α` with mass on them. `sgn`
and `C_t` are `C(σ)`-invariant (checked in code).

---

## 3. K2 — q=5 shadow: the germ is CONTAINED in the ansatz

**Verdict: CONTAINS.** The PROVED germ (bridge `3/4` + shared-NO `1/4`,
`two-orientation-shared-no-cascade.md:50–56`) is an **exactly feasible point** of the ansatz
LP. Rebuilt in this study's *independent* canonical-orbit / integer-`central_row` basis
(no import of the germ's own row generator), on the germ's schedule `D=floor(sqrt(N/512))+2`,
odd `N≥513`:

| N | D | support ⊆ profile lattice | max moment residual (deg<D) | l1 | net mass | correlation | tail (C_t≥N/4) | feasible LP point |
|---|---|---|---|---|---|---|---|---|
| 513 | 3 | yes (off-lattice 0) | **0** | 1 | 0 | 8/11 = 0.7273 | 1/4 | **yes** |
| 2049 | 4 | yes | **0** | 1 | 0 | 0.7199 | 1/4 | **yes** |
| 4609 | 5 | yes | **0** | 1 | 0 | 0.7160 | 1/4 | **yes** |
| 8193 | 6 | yes | **0** | 1 | 0 | 0.7135 | 1/4 | **yes** |
| 20003 | 8 | yes | **0** | 1 | 0 | 0.7104 | 1/4 | **yes** |

The germ's support is entirely `{NO backbones} ∪ {single-flip minimal-YES}` (minority always 1;
freedom is in the pair total `s`), its shared-NO reflection is the atom cancellation of §2,
and its bridge is a Chebyshev-type combination over `s`. Because residual `=0` under the
independent moments, `W_germ` satisfies the ansatz LP's equality constraints, so the LP optimum
`≥` germ correlation `>2/3`. **K2 passes: same mechanism class, no contradiction with the
reviewed q=5 scope.** (Command/SHA in §6; JSON `k2_germ.json`.)

---

## 4. K1 — finite trend (exact, q=5 then q=7,9). G11: no asymptotic claim.

### A. Matched profile-lattice-support LP correlation at fixed (N,D). (`*` = `>2/3`.)

| N | D | q=5 | q=7 | q=9 |
|---|---|---|---|---|
| 8 | 3 | 0.8571\* | 0.8571\* | 0.8571\* |
| 8 | 4 | 0.5625 | 0.5625 | 0.5625 |
| 8 | 5 | 0.2387 | 0.2857 | 0.2857 |
| 10 | 4 | 0.6400 | 0.6400 | 0.6400 |
| 10 | 5 | 0.2954 | 0.3936 | 0.3951 |
| 12 | 4 | 0.6944\* | 0.6944\* | 0.6944\* |
| 12 | 5 | 0.3524 | 0.4545 | 0.4545 |
| 14 | 5 | 0.4147 | 0.5192 | — |
| 16 | 4 | 0.7656\* | 0.7656\* | — |
| 16 | 5 | 0.4659 | 0.5600 | — |

**Reading.** At `D≤4` the correlation is **bit-identical across q** — the critical degree
`D_crit` (largest D with corr`>2/3`: `=3` for N≤10, `=4` for N≥12) is q-independent in range.
At the super-critical `D=5` (all q below `2/3`), extra alphabet gives a real gain **q5<q7**,
but it **saturates**: `q9≈q7` (equal at N=8,12; `0.3951` vs `0.3936` at N=10) — inconsistent
with a `q^(1/6)` growth (`(9/5)^(1/6)=1.10` would demand `q9` visibly above `q7`).

### B. The `≤2-active-pair` sub-support is EXACTLY q-independent (all cells).

One active pair + one spectator, all other pairs empty — identical rational correlation for
q=5,7,9 at **every** tested (N,D):

| N | D | q=5 = q=7 = q=9 |
|---|---|---|
| 8 | 3/4/5 | 6/7 · 9/16 · 18/83 |
| 12 | 3/4/5 | 10/11 · 25/36 · 20/57 |
| 16 | 3/4/5 | 14/15 · 49/64 · 147/316 |
| 20 | 3/4/5 | 18/19 · 81/100 · 1296/2375 |

**Exact obstruction identity (B).** For a support touching `≤2` pairs, empty spectator pairs
contribute only the identity factor to every `R_α` and only fixed positive `|G|`-scaling under
the larger group, so the annihilation kernel and the correlation ratio are **independent of q**.
Corollary: any bounded-pair boundary family — including the germ — gains nothing from larger q.
(`deep_yes` on ≤2 pairs is likewise identical: 13/16 at (10,4), 69/80 at (12,4).)

### C. Product-over-pairs boundary witness — decays exactly as M2.

Per-pair zero-total factor `φ(one-sided)=−1`, `φ(two-sided,minority 1)=+1`; global weight
`Π_i φ(u_i)`. Closed evaluation (and code): `‖·‖_1 = 2^P`, correlation numerator `= 2`, so

    correlation = 2^(1-P) = 2^(1-(q-1)/2)   —   exactly M2 (M2.md:21).

Confirmed: q=5→**1/2**, q=7→**1/4**, q=9→**1/8**, q=11→**1/16**, q=13→**1/32** (`matches_M2=true`).
Activating all `P=Θ(q)` pairs *by a product* pays exponential-in-q NO-side correlation — the
K1 ancestors' graveyard (M2 `2^(1-(q-1)/2)`, ORIENT `2^(-r(m-1))`).

### D. Scalar single-active-pair family (q=5): the `Θ(√N)` cap.

`D_crit` (largest D with corr`>2/3`) vs `√N`:

| N | 16 | 24 | 36 | 48 | 64 |
|---|---|---|---|---|---|
| D_crit | 4 | 4 | 5 | 6 | 6 |
| D_crit/√N | 1.00 | 0.82 | 0.83 | 0.87 | 0.75 |

A clean `D_crit = Θ(√N)` scalar-Chebyshev threshold (e.g. N=64: D=6→0.782\*, D=7→0.623), the
same scale as the germ's `floor(sqrt(N/512))+2`, on a family Part B proves q-independent.

### E. Full-orbit ceiling (the true optimum, not just the ansatz) — the honest caveat.

`solve_band` "joint" (`ksum_l2p1`), q=5 vs q=7 vs q=9:

| N | D | q=5 | q=7 | q=9 |
|---|---|---|---|---|
| 8 | 4 | 0.8355\* | **0.8355\*** (identical) | — |
| 8 | 5 | 0.5327 | 0.5865 | **0.6175** |
| 10 | 4 | 0.8851\* | **0.8851\*** (identical) | — |
| 10 | 5 | 0.6438 | **0.6894\*** | (N=10,D=5,q=9 not reached in budget) |

**In the constant-correlation regime (`D≤4`, corr`>2/3`) even the best-possible witness is
q-identical** (`0.8355`, `0.8851` for q5=q7). A genuine gain appears at the super-critical
`D=5`, and — unlike the single-flip ansatz support (§4A, which **saturates** `q9≈q7`) — the
full-orbit ceiling **grows monotonically** with q on the fully-computed triple:
`0.5327<0.5865<0.6175` (N=8, D=5), increments *decelerating* `+0.054, +0.031`. At `(N=10,D=5)`
the q=7 ceiling already crosses `2/3` (`0.6894`) where q=5 does not (`0.6438`) — a real finite
lift of `D_crit` from `≥3`-pair (genuinely multi-pair, non-product; the product realization is
capped by §4C) backbones with **deeper-than-single-flip** YES structure. (The `(N=10,D=5,q=9)`
exact LP did not finish in budget — INTERRUPTED; N=8 D=5 already gives the full q=5/7/9 triple.)
So the profile-lattice *direction* has a live finite gain — but it lives in the deeper
multi-pair non-product region the first single-flip ansatz does **not** reach, and the data
cannot resolve whether the (decelerating) growth tracks `q^(1/6)` or converges to a bounded
constant near `2/3` (G11: separating `1/6` from a bounded ceiling needs `N≈256`).

---

## 5. K3, K4

**K3 (cap-sweep).** No positive lower-bound claim is registered here, so the pre-registration
sweep is not triggered. For reference the finite scales sit far below both caps: the certified
query scale `D/2` at these `N` is `O(1)`, versus walk `O(N^(2/3))` and B4a `O_ε(N^(1/2+ε)q^(1/4))`.

**K4 (non-factorization).** The boundary-pairing witness is a globally `S_N`-symmetric signed
measure on whole-`N` profiles with a global `s↔N−s` reflection coupling (shared-NO). It is a
symmetric function of the entire profile and **does not factorize across disjoint position
blocks** — it is not the block-factorized construction `compcap` (`compcap.md:21`) caps at
`O(√N·q^(1/6))`. **So the ansatz PASSES K4** (it is not disqualified by the position-block
pre-filter). This does not rescue it: the operative product obstruction here is on the
**alphabet-pair** axis (M2, §4C), a different factorization than compcap's position-block axis.
K4 passes; the alphabet-pair cap bites when the ansatz tries to use `q`.

---

## 6. Reproduction — commands, logs, SHA-256

Interpreter `<machine-local-path-redacted>` (Python 3.11.9,
SymPy 1.13.1); run from `ksum/artifacts/`. Every number above is exact rational.

Scripts (SHA-256, prefix `ksum_beta1_profile_lattice_ansatz_q5_20260723_`):

    2faa252fe12d4b9f3a5e2e88c677c70558a7c205daecf09398314611d8056b18  _core.py
    e1f31d3652a21ba7c6f53fc3326f45be17adbec126431422583a0f3eb7cede32  _k2_germ.py
    14bd7979ca07205bd4c3f65ad32ddc41ba4d94aabc237bc506c85a2cc970725b  _k1_trend.py
    28ec7113c08b04aa3badab74b720c491c342e87d9788040c2de9e3b664d1613a  _k1_qgain.py
    c566d0afcef6b26f81e8a2e67b8ab1d6483d725831498e9751882cd40438b55e  _k1_ceiling.py

Logs (SHA-256, dir `logs_ksum_beta1_20260723/`):

    49d6064b61b91632d1bae4b184d1b8cf6ab90b87a533e03a05783e0cf6efda24  k2_germ.json
    5d3104a41856c3ad8c01801d0487b7edb54d77162a5a4c5c778a574e79e4eb9f  k1_trend.json
    b6dfab61ca88294bce3ce13b3b510fa605f6c87cbdcea795a5c55645b5bddfee  qgain_check.log
    50e0f784c93f2763cb1285ea541331c0737fe6d74390650cfa2dabf55606482a  qceiling9.log  (INTERRUPTED)
    66de4bdcf0ac07e78aff63faeb1d1803de1fcf7d3bf31979fa32f138a07430bd  calibration.log

Commands (run from `ksum/artifacts/`):

    python ..._k2_germ.py   --output logs_ksum_beta1_20260723/k2_germ.json
    python ..._k1_trend.py  --output logs_ksum_beta1_20260723/k1_trend.json
    python ..._k1_qgain.py    > logs_ksum_beta1_20260723/qgain_check.log
    python ..._k1_ceiling.py  > logs_ksum_beta1_20260723/qceiling9.log   # INTERRUPTED at (N=10,D=5,q=9)

Cross-checks against disk: germ reproduced independently via
`ksum/tools/ksum_l2p27_shared_no_rule7_independent.py` (residual 0; corr 3/4, 8/11, … at N=511…51201);
full-orbit ceiling via `ksum/tools/ksum_l2p1_exact_moment_lp.py` `solve_band` "joint".
`calibration.log` records single-flip vs deep-YES vs full-orbit at q=5 (N=8/10/12).

**INTERRUPTED marker.** `qceiling9.log` completed `(N=8,D=5)` for q=5/7/9 (the full triple used
in §4E) and `(N=10,D=5)` for q=5/7; the `(N=10,D=5,q=9)` exact LP (~600 classes) was stopped
before completion in budget. No conclusion leans on that one uncomputed cell.

---

## 7. Outcome and "what would change this"

**Outcome class B** (ansatz written; K2 pass; K1 does not deliver a q-gain — with exact
obstruction identities). Precisely:

1. The first concrete boundary-pairing profile-lattice ansatz is defined (§2) and **contains
   the PROVED q=5 germ as an exactly feasible point** (§3, K2 = CONTAINS).
2. Its constant-correlation degree is **exactly q-independent** on bounded-pair support
   (§4B, exact identity) and scalar-capped at `Θ(√N)` (§4D) — no `q^(1/6)` gain from the
   boundary mechanism as instantiated.
3. The only instantiated way to make the degree grow with q — activating `Θ(q)` pairs by a
   **product** — has correlation **exactly `2^(1-(q-1)/2)`** (§4C = M2), the ancestor decay K1
   forbids.
4. The genuinely-non-product `Θ(q)`-pair law that would escape both (2) and (3) is
   **uninstantiated** — the node's "no coefficient law yet." Consistent with **OPEN**: the
   full-orbit ceiling shows a *real, monotone (decelerating)* multi-pair q-gain
   (§4E: `0.5327<0.5865<0.6175` for q=5/7/9 at N=8,D=5; q≥7 crosses 2/3 at N=10,D=5 where q=5
   does not), so the profile-lattice bet is **not refuted** — the direction is live and located
   in the deeper multi-pair non-product region, bottlenecked on the missing coefficient law.

**What would change this (raise toward Outcome A / kill the node):**

- **Toward A:** a formula-defined `Θ(q)`-active-pair, non-product coefficient law that realizes
  the §4E ceiling gain — an explicit `w` on `≥3`-pair backbones with **deeper-than-single-flip**
  YES structure, constant correlation, and `D_crit/√N` rising in q. The §4E ceiling already
  **grows** `q5<q7<q9` (N=8,D=5), so the target is not empty; the missing object is the
  coefficient law that attains it while staying non-product (else §4C's `2^(1-(q-1)/2)` cap). The
  decisive next finite discriminator: push the q=9 (and q=11) ceiling to `N≈16–20` at `D≈√N` and
  measure whether `D_crit/√N` rises with q or the decelerating increments converge below `2/3`.
- **Toward killing:** a proof that every `S_N`-symmetric annihilating profile measure with
  constant correlation has its NO/YES separation carried by `O(1)` pairs (generalizing §4B's
  exact ≤2-pair q-invariance to all bounded-pair supports), forcing either the §4C product
  decay or the §4D scalar cap — which would upgrade `compcap`/M2 into a full profile-lattice
  no-go. Neither is established here; both are finite-consistent with the data.

**Boundary-cancellation well-definedness (directive v).** The boundary-cancellation idea is
**not** ill-defined and **not** forced to zero by invariance — §3 exhibits it live (the germ,
residual 0, correlation `>2/3`). What the data shows is narrower and exact: it delivers constant
correlation only while the YES/NO boundary is carried by `O(1)` alphabet pairs; spreading it over
`Θ(q)` pairs to grow the degree re-enters the M2 product cap. That precise scoping — not a
refutation — is the β1 result.
