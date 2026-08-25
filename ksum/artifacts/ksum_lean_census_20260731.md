# k-Sum Lean audit — itemized coverage census (LaTeX label → tier → module → state)

**Purpose.** This table is the discharge object of `KSUM.LEAN`'s restated composition claim
(frozen 2026-07-31): *"the conjunction is definitional and the ONLY mathematical content is the
scope identity `targets(T1) ∪ targets(T2) ∪ targets(T3) = ⟨the declared target lists⟩`, to be
discharged by an itemized census table."* Authored by the lead 2026-07-31 (post gap-closure
batches 1–2, build `3017 jobs / exit 0 / 283 declarations axiom-clean`); **UNREVIEWED at creation**
— verification is item DF-9 of the delta-fidelity commission, and the composition may not rise
above CONJECTURED until that review confirms this table against disk.

State vocabulary: **proved-uncond** (kernel-proved, no `QueryModel`); **proved-rel** (kernel-proved
relative to the `QueryModel` interface = ABI21 + Tani24 + facts (i)–(iv)); **cert-json**
(exact rational certificates on disk, subset kernel-checked); **partial** (some clauses proved,
named residual); **stated** (Lean `Prop` declared, consumed as hypothesis, not proved);
**unformalized** (no Lean rendering; named).

## Tier T1 — k=2 lower-bound main line (module `KsumAudit.MainLine` + `Defs` + `QueryModel`)

| LaTeX label | State | Note |
|---|---|---|
| `lem:encode` | proved-rel | G-L2 gate; explicit constants |
| `lem:shift` | proved-rel | one-sided `Θ` rendering (declared) |
| `lem:oddN` | proved-rel | uses fact (iii) (F1; now stated in paper v5.2) |
| `thm:main-odd` | proved-rel | Tani genuinely needed for `2n−1 < q ≤ 4n−1` |
| `thm:main-general` | proved-rel | representative-set construction |
| `cor:threshold` | proved-rel | lower side; ABI-only per F6 (paper v5.2 aligned); `5 ≤ cN` threshold explicit |
| `thm:oabarrier` | proved-rel | (i)+(ii); constancy form + fact (iv) (F2; now stated in paper) |
| `thm:k2-upper` | out of scope | algorithm; declared exclusion from day one |

## Tier T2 — k-floor cores + Rosmanis barrier (modules `KsumAudit.T2KFloor`, `KsumAudit.RosmanisBarrier`, `KSUM/A1a,A1b,A1c`)

| LaTeX label | State | Note |
|---|---|---|
| `thm:kfloor` | proved-rel | **ADDED per delta-review C-4** (was silently absent): the floor itself = `KSUM.A1d.Claim`, delivered end-to-end by `KSUM.A1.holds` (composition machine-checked rel interface) |
| `lem:core` | partial | whole-core-sum clause at every window target; subset-range clause base-target-only (declared) |
| `prop:core-even` | proved-uncond | `core_reduction_at`, every window target, witnesses incl. tight `r = k−1` |
| `lem:core-odd` | proved-uncond | parked coordinate in the same theorem |
| `lem:transl-cover` | proved-rel | windows (i)/(ii) + Bézout coset covering + query half (`Q_window_cover`, `C = 2`) |
| `prop:embed` | partial | **CORRECTED per delta-review C-1**: `genEmbed` (batch 2 H-5) proves `lem:embed`'s **DATA** for all `k ≥ 3, n ≥ 1, R ≥ 2` (`c_P = k(k−1)2^{k−2}`, injectivity, `k∣P`, `2(M+1)=(2k+1)^{k−1}+1`, bounds); the encoding IDENTITY itself is `A2a`/`A2b` — stated `Prop`s consumed as hypotheses, prose-PROVED with archived reviews, not kernel-proved |
| `lem:embed` (data) | proved-uncond | `EmbedData` + `demoEmbed` + `coprime_k_q` (`gcd(k,q)=1` forced) |
| `lem:embed-allt` | partial | **ADDED per delta-review C-2** (was silently absent): the coprimality theorem is kernel-proved (`coprime_k_q`, both parity branches); the all-targets encoding clause enters `KSUM.A2.Claim` as a stated conjunct, not separately kernel-proved |
| `prop:rosmanis`(1) | partial | count `≥ 2` proved orbit-proper both branches; `(f,λ)` bijection + `Σ_f p_{≤m}(N−f)` formula **unformalized** (C(σ) wreath infra) |
| `prop:rosmanis`(2) | partial | both finite witnesses proved; representation sentence **unformalized** |
| `prop:rosmanis`(3) | proved-uncond | fixed-point-free ⇒ empty positive blocks |
| `C(σ) ≅ (C₂≀S_m)×S_τ` | unformalized | declared T2 caveat; prerequisite for the rosmanis bijection |

## Tier T3 — obstruction / negative-result group (modules `KsumAudit.Obstructions*`, `FactorialFiltration`, `JointLP`)

| LaTeX label | State | Note |
|---|---|---|
| `lem:factorial-filtration` | proved-uncond | **batch 1 L-1**: both directions, any alphabet/invariant measure/degree; `(N)_m` proved |
| `prop:joint-lp` | cert-json | **batch 2 H-6, scope corrected per delta-review C-3**: 24/24 exact primal+dual certificates, gap 0; 6 kernel-checked — covering rows 1+3 of display (39) EXCEPT the `(5,4,1)`-single degree-2 optimum (JSON-certified only), and with `d`-monotonicity a docstring argument, not a theorem; optima independently recomputed three ways by the delta review, identical to manuscript in all 24 |
| `thm:pair-tensor` | partial | occupancy-level annihilation proved; `Z_q` pair-orientation lift to query polynomials **residual** (named) |
| `thm:tilted-log-band` | partial | **batch 2 H-1**: construction (42), divided differences, (44), `C_h ≤ 25/19`, `ΣA_j ≤ 29/23`, `corr ≥ 437/581` all hypothesis-free; inner-pair-tensor-as-measure identification **residual** |
| `lem:band-multiplication` | partial | (a)(b)(c)(d) proved ((a)/(d) = batch 1 L-2); convolution reduction's `S_N`-average operator **residual** |
| `thm:product-obstruction` | proved-uncond | + mixture value `2^{1−r}` |
| `thm:block-obstruction` | partial | (49) + (ii) proved; (iii) `ρ_j ≤ 4/5` **derived** (batch 2 H-3); (i) linearity half proved, `m`-fold Vandermonde **residual** |
| `thm:orientation-obstruction` | partial | (a) exact factor + counting identity; (b) **batch 2 H-2**: (51) produced end-to-end, `corr ≤ 1/8` (even) / `≤ 1/2` (odd) outright; named-construction genPoly identification **residual** |
| `prop:transfer-facts` | proved-uncond | G1, G3; G2 at the manuscript's satellite hypothesis (batch 1 L-4 Maschke dictionary) |
| β1 identities C1/C2/C4 | out of tier | PROVED-scoped by the 2026-07-23 rule-7 review (prose); C3 NUMERICAL by design |

## Composition layer (modules `KSUM/*`)

| Node | State | Note |
|---|---|---|
| `KSUM.A1` | proved-rel | `composition` + `holds` end-to-end; children A1a/A1b/A1c all proved |
| `KSUM.A2` | proved-rel | `composition` + `coprime_k_q`; `EmbedData` inhabited (`demoEmbed`, `genEmbed`) |
| `KSUM.B1` | proved-rel | **batch 1 L-7**: `holds` with absolute `C = 4`, donor-unconditional; route = `composition_via_A1_inputs` |
| `KSUM.B2` | proved-rel | transport with `k`-dependent donor typing (batch 1 L-6); novelty side-condition NOT mechanized (declared) |
| `KSUM.B4` | proved-rel | sandwich scoped `q` odd, `5 ≤ q ≤ N`; joint witness `sandwichModel` |
| `KSUM.B4a` | stated | interface hypothesis, faithful incl. `q ≥ 2` (closeout C-5) |
| `KSUM.goal` | claim-free | deliberate §7.4 record (research-target, not a proposition) |
| leaves `A1a/A1b/A1c/A1d/A2a/A2b` | mirrored | A1a/A1b/A1c proved; A1d/A2a/A2b stated (prose-PROVED with archived reviews) |
| `KSUM.B3`, `KSUM.B4b`, `KSUM.k3.donor` | no module | declared §7.3 deviations (B3 REFUTED·PARKED; B4b OR-routes unwritten; k3.donor hypothesis-shaped) |

## Explicitly open extension (named in `KSUM.LEAN`'s narrowed Claim; NOT covered, by design)

`rem:k3embed` (tighter k=3 recipe), `prop:kclaw-fillers`, `prop:kclaw-coloring`, `rem:torsion` —
never in any tier's declared target list; plus the residuals named above (rosmanis bijection/formula/
rep-sentence + C(σ) structure; pair-tensor lift; block (i) Vandermonde; band-mult S_N-average op;
tilted inner identification; orientation genPoly identification; 18 JOINTLP LPs JSON-certified but
not kernel-checked).

## Scope-identity verdict (the composition claim's content)

Every label in T1/T2/T3's **declared target lists** appears above with a Lean artifact at
`partial` or better; every absence is either the day-one exclusion (`thm:k2-upper`), the
explicitly-open extension, or a named residual inside a `partial` row. That is the identity the
restated composition claim asserts.

**Verification history (DF-9):** the 2026-08-01 delta-fidelity review checked this table row by row
against disk and returned **CORRECTIONS** — four errors (C-1 `prop:embed` over-stated as
proved-uncond; C-2 `lem:embed-allt` and C-4 `thm:kfloor` silently absent, falsifying the original
"no declared target is silently absent" sentence; C-3 the JointLP "decide rows 1+3" over-statement).
All four corrections are applied above, verbatim to the reviewer's prescriptions, by the lead on
2026-08-01. Every OTHER row was verified accurate by that review.
