# SE Actions 1+2 — q-dependence audit of the Φ channel and X̄ transfer (PROPOSER READING)

**Date:** 2026-07-17
**Author:** lead (Fable 5), reading `se/artifacts/references/BR_1310.5185v4_collision.tex` (the real LaTeX,
1619 lines) directly, line by line. **STATUS: PROPOSER-SIDE READING. Not certified.** An independent
checker (separate model, not told these conclusions) was launched BEFORE this file was written; its
verdict will be appended as §6. Numerical corroboration (fresh small-n operator norms, also blind) is
being computed in parallel and lands in `se_action0_py_reverify_20260717.md`.

**Timestamp discipline:** this file is written while both the checker and the numerics are still
running. Nothing below has been adjusted to agree with them.

---

## 0. Verdict being proposed

**The ambient norm bounds of `lem:normEstimations` (BR:678-686) — all three of (a), (b), (c) — are
q-free: every proof goes through verbatim for every q ≥ 2, in particular at q = 2n.** The handoff's
prediction that the Φ channel "likely genuinely needs large alphabet" is WRONG in the ambient sense:
`lem:newMain` and `lem:Wk-1` never consume a large alphabet. Explicit constants (no O(·) readings, G5):

- (a) `‖X̄_{se,k}‖ ≤ 1` at every q ≥ 2. [discharges §6.4 of the handoff = Action 2]
- (b) `‖Ȳ_{se,k}‖ ≤ √(2k/n)` at every q ≥ 2. [Stage 2's P_Y; re-verified separately today]
- (c) `‖W_{se,k}Φ_{se,k}‖ ≤ √6/√(n−2k+1)` at every q ≥ 2. [NEW today = Action 1]
- `lem:newMain`: `‖Φ^(m)_k‖ ≤ √2/√(m−2k+1)` for k < m/3, at every q ≥ 2.
- `lem:Wk-1`: constant exactly √3 (max of `√((|P|+2)/2)·2^(−max(0,|P|−4)/4)` at |P|=4), q ≥ 2.

The `q = Ω(n²)` standing assumption is consumed ONLY in `sec:subIllegal` (BR:714, BR:730; announced
BR:120, BR:346) — the legality/illegal-removal layer, disjoint from all of `sec:normEstimationsProof`.
Grep sweep over the tex for `\Omega(n^2)`: exactly those four sites.

## 1. lem:newMain (BR:625-629; proof BR:831-986) — where q could enter, and doesn't

Setup: `Φ^(m)_k = Π̄^(m)_k − Π_0⊗Π̄^(m−1)_k − Π_1⊗Π̄^(m−1)_{k−1}` (BR:833-836).

1. **Branching step (BR:838):** image of Φ uses only S_{m−1}-irreps with λ₁ ∈ {m−k, m−k−1}. Pure
   branching rule; the three terms' images sit in shapes (m−k,λ)↓, (m−k−1,λ), (m−k,λ) respectively.
   q-free.
2. **λ₁ = m−k−1 part is killed exactly (BR:840-853):** Schur + lem:kappa (q-free, see §3) + the
   pigeonhole "weight k with a nonzero in each of k pairs ⊂ [2..m] ⟹ first component e₀" (BR:848).
   Φv = v − v − 0 = 0 (BR:850). q-free.
3. **clm:odin (BR:865-917), the H₁⊗H̄^(m−1)_{k−1} part:** basis `w_z` of image(κ′) indexed by
   `z ∈ [1..q−1]^k` — q enters ONLY as this index set (non-empty ⟺ q ≥ 2). The split `w_z = w′_z + w″_z`
   (BR:896-901): I verified the algebra — the `c = b_k` terms of w″ cancel the negative halves of w′,
   and the coefficient counts `|[m]∖{a₁,b₁,…,a_{k−1},b_{k−1}}| = m−2k+2` positions. `w′_z ∈ H̄^(m)_k`
   by lem:kappa; `‖w″_z‖ = 1/√(m−2k+2)`, mutually orthogonal (distinct z ⟹ distinct labels) ⟹
   `‖Φv‖ ≤ ‖v‖/√(m−2k+2)` (BR:911-916). Exact, q-free.
4. **clm:dva (BR:919-986), the H₀⊗H̿^(m−1)_k part:** v = E_t-image vector; d₁..d_ℓ = height-1 column
   entries, `ℓ ≥ m−2k+1` (λ₁ = m−k minus ≤ k−1 taller columns). v's normal form (BR:938-942) has
   coordinates `u_0,…,u_{q−1}` indexed by the alphabet — a DECOMPOSITION, never a count; no step uses
   how many there are. `‖v‖² ≥ ℓ·Σ_z‖u_z‖² = ℓ‖v″‖²` (BR:952-954; the ℓ terms per z are orthogonal).
   The claim v′ ∈ image(E_{t′}) (BR:955, proof BR:966-985) is pure tableau/position combinatorics
   (the new S-sets with `S∩{d₁..d_{ℓ+1}} = {d_{ℓ+1}}` are (d_ℓ,d_{ℓ+1})-swaps of old ones). NOTE the
   claim needed is membership in the SUBSPACE image(E_{t′}) — linear in v — so the per-basis-vector
   argument sums with no uniform-constant issue. Then `‖Φv‖ = ‖Π̄^(m)_k v″‖ ≤ ‖v″‖ ≤ ‖v‖/√ℓ`
   (BR:958-964). Exact, q-free.
5. **Combination (BR:857-861, implicit in the text):** coimage = V₀ ⊕ V₁ (orthogonal), so
   `‖Φ‖ ≤ √(1/(m−2k+1) + 1/(m−2k+2)) ≤ √2/√(m−2k+1)`. The text says only O(1/√m); the √2 assembly is
   ours (Cauchy–Schwarz on orthogonal components), flagged as such.

**Minimal q for the entire proof: q ≥ 2.** No step needs q growing with n.

## 2. lem:Wk-1 (BR:1197-1201; proof BR:1203-1338) — q-audit

- Basis of image(κ′) on weight k: types `w_{a_i,z}` (a doubly-occupied pair, z_i < z_k) and `w_{c,z}`
  (free nonzero at c), BR:1204-1216. q enters only as label ranges; at q = 2 the first type is empty,
  harmlessly (fewer basis vectors). Completeness on H^(2n)_k: k−1 antisym pairs force one nonzero each
  (pigeonhole), the k-th nonzero is free or doubles a pair — matches the two types.
- Special-path structure (BR:1219-1286), projectors Ξ^P, κ^P: position combinatorics, q-free.
- clm (BR:1292-1309): `‖Ξ^P κ^P‖ ≤ 2^(−(K′ + max(0,|P|−4)/2)/2)`, K′ = #cycles: coefficients
  `2^(−(|P|−2)/4)`, ≤ 2 survivors on the special path, 1/√2 per cycle. q-free.
- clm (BR:1311-1325): `‖WΞ^P‖ ≤ √(2^(K′−1)(|P|+2))`: 0-1 matrix column/row counts (cycles ×2, special
  path ≤ (|P|+2)/2). q-free.
- Assembly (BR:1327-1338): `‖WF′‖ = max_P ‖WΞ^P F^P‖ ≤ √((|P|+2)/2)·2^(−max(0,|P|−4)/4)`; values at
  |P| = 2,4,6,8: √2, √3, √2, √5/2 ⟹ **exactly √3**, attained at |P| = 4. q-free.

**Minimal q: q ≥ 2.** (Statement covers only W^μ_k, not X/Y — the (c) proof needs only W. ✓)

## 3. Inputs re-verified today for Action 0 (cross-referenced here)

- **lem:kappa (BR:759-794): pure C[S_m]** — tableaux, E_t = C_t⁻R_t⁺, coefficient/pigeonhole. The
  alphabet appears nowhere between BR:743 and BR:794. Implicit hypothesis: 2k distinct elements of [m]
  (m ≥ 2k); in-spec always satisfied, and infeasible sectors have H̄ = 0 anyway.
- **lem:Wkv (BR:1001-1193): needs only q ≥ 2, constant exactly 1** — `‖Ξκ‖ ≤ 2^(−K′/2)` (clm:Lambdav,
  BR:1149-1169) × `‖WΞ‖ ≤ 2^(K′/2)` (clm:WLambda, BR:1173-1188) cancel exactly; covers W, X, Y
  (BR:1004, BR:1192). w_z-basis/e₀-support step re-derived: weight-k κ-fixed ⟹ one nonzero per pair,
  e₀ elsewhere (antisymmetry kills weight-0 pairs; pigeonhole forces the rest).

## 4. The (c) assembly at q = 2n (BR:1352-1372), se case

Schur ⟹ principal module `S^λ ⊗ S^λ′`, λ ⊢ n−1 with k−ℓ−1 boxes, λ′ ⊢ n with ℓ boxes, some
ℓ ∈ [0..k−1] (BR:1361-1364, using lem:newMain's second statement). Double lem:kappa ⟹ κ′-fixed
principal v (BR:1365). `W_{se,k}Φ_{se,k}v = W_{se,k}(Φ^(n)_{k−ℓ}⊗Π̄^(n)_ℓ)v` (BR:1366-1370, sector
selection). `‖(Φ^(n)_{k−ℓ}⊗Π̄^(n)_ℓ)v‖ ≤ √2/√(n−2(k−ℓ)+1)·‖v‖ ≤ √2/√(n−2k+1)·‖v‖` (§1). κ′ commutes
with `Φ⊗Π̄` (group-algebra element vs S′-equivariant maps, BR:1371) ⟹ lem:Wk-1 applies per block:
`‖W^μ_k(·)v‖ ≤ √3‖(·)v‖`; the block column preserves it. Hence

**`‖W_{se,k}Φ_{se,k}‖ ≤ √6/√(n−2k+1)` at every q ≥ 2.**

lem:newMain's hypothesis k−ℓ < n/3: for k < K = ⌊n^{1/3}⌋ this holds for all n ≥ 8 (and for n < 8,
K = 1 forces k = 0, where Φ_{se,0} = 0 identically — the empty sum, BR:640).

Same skeleton for (a) (BR:1342-1346): Schur + double lem:kappa + lem:Wkv(X). All inputs q-free ⟹
**`‖X̄_{se,k}‖ ≤ 1` at every q ≥ 2** — the §6.4/Action-2 transfer is discharged analytically, not
just numerically.

## 5. What this does and does NOT close

**Closes (pending checker):** the AMBIENT half of all three channels at q = 2n, i.e. the entire
`lem:normEstimations` transfers. With cross-k orthogonality (BR:689; proved for the S_n×S_n family at
all n, `exact_band_descent_analysis.md:410-421`) and the α_k arithmetic (BR:692-698), this gives
`‖Δ₁⋄Γ̃‖ = 1 + O(n^{−1/6})` AMBIENTLY at q = 2n.

**Does NOT close SE.** The witness is the LEGAL restriction with its own normalization (1/q!; the
k = 0 legal block has norm 1, a factor c₀ above BR's ambient scale). The submatrix bound
`‖Γ^leg∘Δ_i‖ ≤ ‖Γ̃∘Δ_i‖` is then off by c₀ = e^(1.1534n) against the numerator: worthless. Each
channel needs a LEGAL bound of the form (legality factor) × (ambient), as in
`exact_band_descent_analysis.md` (6.2): `‖X_k^leg‖ ≤ R_{n,k}·‖X̄_k‖`. **The open problem is now
EXACTLY the legality layer:**
1. stay and Φ analogues of (6.2) — the handoff table marks stay "covered"; verify, and produce the Φ
   analogue (nothing exists for it);
2. the Route-1 write-up debts: the LR first-row inequality (stated as a formula nowhere), the
   commutation `Π^alph_j P_N* = P_N* Π^{alph,L}_j`, the `J_Y = 1_M ⊗ R_n` factorization;
3. the legal Δ₁-assignment (6.4) hygiene (Δ⋄ requirements of BR sec:adv at q = 2n).

**Family split (Hole 3(e)) — proposed resolution:** BR's OWN `W̄_{se,k} = W_{se,k}Π̄_{se,k}` is built
on the S_n×S_n family (BR:605-609) — the SAME family as the witness's P_k. The Π̄′ (S_{n−1}×S_n)
objects are internal to the channel split via the exact identities BR:650 and BR:662. So DECLARE
`P_k := Π̄_{se,k}` (BR:609) as the witness's projector (commission Stage-0 deliverable, `:666-669`,
`:1486-1488`): the witness is then the legal restriction of BR's Γ̃, and the channel decomposition is
BR's own algebra, not a new transfer. IDENT-1 (BR:650) and IDENT-2 (BR:662) are being verified
numerically at n = 3,4,5 today as part of the Action-0 fresh computation.

## 6. Checker verdict — received after §§0-5 were on disk

**Checker:** fresh independent instance (Sonnet-class, per session protocol: execution/checking on the
cheaper model, blind — given only the BR file, specified line ranges, and neutral questions; NOT told
this document's conclusions, which it had no access to).

**Outcome: AGREES on every substantive conclusion, independently.**
- lem:newMain: q enters at exactly two places (BR:881, BR:940 — label index sets); minimal q for the
  whole proof = 2; "no step requires q growing with n or m."
- clm:odin `≤ 1/√(m−2k+2)` (BR:916), clm:dva `≤ 1/√(m−2k+1)` (BR:964); the direct-sum combination is
  implicit at BR:861 and costs √2 (checker supplied the same Cauchy–Schwarz argument as §1.5):
  `‖Φ^(m)_k‖ ≤ √(2/(m−2k+1))`.
- lem:Wk-1: no new q in BR:1197-1338; q inherited from lem:Wkv (BR:1011, q ≥ 2); constant √3 verified
  TIGHT for the method (max at |P| = 4, where the expression equals exactly 3).
- (a) and (c): no q beyond the black boxes; both go through at q = 2. Chained explicit constant
  independently derived: **`‖W_{se,k}Φ_{se,k}‖ ≤ √(6/(n−2k+1))`** — identical to §4.
- The BR:896-901 prefactor question (w′+w″ reconstruction) checked term-by-term by the checker and
  found NOT an error — same algebra as §1.3.

**Checker flags, reconciled:**
1. *"BR:848 invokes cor:kappa, outside my assigned ranges — unverifiable from the given text."* —
   Range-assignment artifact (the checker was not given BR:810-817). `cor:kappa` is at **BR:810-817**:
   "If v ∈ H^(m)_k and κv = v then v ∈ H̄^(m)_k", proved in two lines from lem:kappa + cor:Hm
   (BR:796-808), both q-free (lead's direct reading). RESOLVED — no q enters.
2. *"w_{a_i,z} type (BR:1211, z_i < z_k) silently needs q ≥ 3 to be non-empty."* — Correct; at q = 2
   that basis type is empty and the claims cover it vacuously (checker's own observation, matching
   §2). At q = 2n ≥ 4: irrelevant.
3. *"The k < m/3 hypothesis of lem:newMain is never used in BR:831-986; the proof needs only
   ~k ≤ (m−1)/2 (positive denominators, disjoint pairs in [2..m])."* — Agreed; bonus slack. Our
   application has k < n^(1/3), far inside either threshold.

**Upgraded status of §0:** PROPOSER-READING + INDEPENDENT BLIND CHECKER AGREEMENT (different model,
different process, checker launched before this file existed). Numerical corroboration (fresh small-n
norms of X̄, W_kΦ_k, Φ at q = 2n) pending in `se_action0_py_reverify_20260717.md`; a Fable-fresh
checker pass per the strict §8 ROLES protocol remains available as further hardening if the lead
wants belt-and-suspenders before external use.
