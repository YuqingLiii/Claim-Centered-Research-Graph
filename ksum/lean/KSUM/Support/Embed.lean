/-
`KSUM/Support/Embed.lean` — shared support module.

Nodes served: `KSUM.A2a`, `KSUM.A2b`, `KSUM.A2` (and, through `KSUM.A2`, `KSUM.B2`).

CONTENT.

* `Coll k n R` — `k`-partite `k`-collision on `k` blocks of `n` positions with range `R`
  (`sec:prelim`; the paper indexes the `kn` positions by block and offset, which is what
  `blockPos` does).
* `EmbedData` — the DATA of `lem:embed`: the payload/tag assignment of `KSUM.A2a` and the modulus
  `q = (P+1)(M+1)` it forces.  The manuscript's symbols are kept.  Only the properties actually
  consumed downstream are recorded as fields, and each field says which manuscript display it
  comes from.  Nothing here is proved about the encoding: `EmbedData` is data plus the two
  arithmetic facts about `P` and `M` that `lem:embed-allt` uses, exactly as printed.

No `sorry`.
-/
import KSUM.Interface

namespace KSUM.Support

open KsumAudit

/-- Position `i` of block `j`, among the `k·n` positions.  LaTeX: `lem:embed`, "a `k`-subset of
the `kn` positions has a block multiset". -/
def blockPos (k n : ℕ) (j : Fin k) (i : Fin n) : Fin (k * n) :=
  ⟨(j : ℕ) * n + (i : ℕ), by
    have hj : (j : ℕ) + 1 ≤ k := j.isLt
    have hi : (i : ℕ) < n := i.isLt
    have h1 : ((j : ℕ) + 1) * n ≤ k * n := Nat.mul_le_mul_right n hj
    have h2 : ((j : ℕ) + 1) * n = (j : ℕ) * n + n := by ring
    omega⟩

/-- `Coll_{k,n→R}(g) = 1` iff one can pick one position in each of the `k` blocks so that all `k`
chosen values coincide — `k`-partite `k`-collision.  LaTeX: `sec:prelim`, `Coll_{k,n→R}`. -/
def Coll (k n R : ℕ) : (Fin (k * n) → Fin R) → Bool :=
  fun g => decide (∃ v : Fin R, ∀ j : Fin k, ∃ i : Fin n, g (blockPos k n j i) = v)

/-- **The data of `lem:embed`.**

`k` parts of `n` elements with range `R`; the payload budget `P`, the tag budget `M` (`Mv` here,
`M` being taken by the query model), and the induced modulus `q = (P+1)(M+1)`.  The per-position
value map `enc p a` is the manuscript's `u_j·a + w_j` at position `p = (j,i)`.

Only two arithmetic properties of `P` and `Mv` are recorded, and they are exactly the two the
manuscript's own proof of `lem:embed-allt` uses:

* `k_dvd_P`   : from `P = k(R-1)(ω^{k-1}-1)/(ω-1)`, so `k ∣ P` by construction;
* `two_mul_Mv`: from `M+1 = ((2k+1)^{k-1}+1)/2`, written multiplicatively to avoid `ℕ` division.

`enc_inj` is the per-position injectivity of the value map (`|u_j|(R-1) ≤ P < q`, so the map
`a ↦ u_j a + w_j` does not wrap around).  It is what makes the reduction QUERY-FREE through
`sec:prelim` fact (ii); it is declared here as data rather than proved, and is listed as a
relative hypothesis on `KSUM.A2`. -/
structure EmbedData where
  /-- number of parts -/
  k : ℕ
  /-- elements per part -/
  n : ℕ
  /-- range of the collision instance -/
  R : ℕ
  /-- payload budget `P = k(R-1)(ω^{k-1}-1)/(ω-1)` -/
  P : ℕ
  /-- tag budget `M = ((2k+1)^{k-1}-1)/2` -/
  Mv : ℕ
  hk : 3 ≤ k
  hn : 1 ≤ n
  hR : 2 ≤ R
  /-- `k ∣ P`, by the definition `P = k(R-1)(ω^{k-1}-1)/(ω-1)`. -/
  k_dvd_P : k ∣ P
  /-- `M+1 = ((2k+1)^{k-1}+1)/2`, i.e. `2(M+1) = (2k+1)^{k-1}+1`. -/
  two_mul_Mv : 2 * (Mv + 1) = (2 * k + 1) ^ (k - 1) + 1
  /-- The `k`-only constant of `lem:embed`'s payload count. -/
  cP : ℕ
  cP_pos : 0 < cP
  /-- `R^{k-1} ≤ P`: from `P = k(R-1)(ω^{k-1}-1)/(ω-1)` with `ω = 2R-1`. -/
  P_lower : R ^ (k - 1) ≤ P
  /-- `P ≤ c_P · R^{k-1}` with `c_P` depending only on `k`: same formula. -/
  P_upper : P ≤ cP * R ^ (k - 1)
  /-- the per-position value map `(j,i) ↦ u_j·a + w_j` of `lem:embed`. -/
  enc : Fin (k * n) → Fin R → ZMod ((P + 1) * (Mv + 1))
  /-- the value map is injective at every position (no wraparound: `|u_j|(R-1) ≤ P < q`). -/
  enc_inj : ∀ p, Function.Injective (enc p)

namespace EmbedData

variable (D : EmbedData)

/-- The induced modulus `q = (P+1)(M+1)`. -/
def q : ℕ := (D.P + 1) * (D.Mv + 1)

theorem q_pos : 0 < D.q := Nat.succ_mul_pos _ (Nat.succ_pos _)

instance : NeZero D.q := ⟨D.q_pos.ne'⟩

/-- The encoded `kSum` instance attached to a collision instance `g`. -/
def encodeInst (g : Fin (D.k * D.n) → Fin D.R) : Fin (D.k * D.n) → ZMod D.q :=
  fun p => D.enc p (g p)

end EmbedData

/-! ## Non-vacuity: `EmbedData` is inhabited

**Closeout item C-4(a), 2026-07-31.**  Statement-fidelity review
`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §7.2 (and, before it, finding
**R-A2-3** of `ksum/reviews/ksum_composition_layer_review_20260730.md`, left OPTIONAL and undone by
tier T2) recorded the gap this closes: `KSUM.A2a.Claim`, `KSUM.A2b.Claim`, `KSUM.A2.Claim` and
`KSUM.B2.Claim` all open with `∀ D : EmbedData, …`, and **no instance existed anywhere in the
development**.  Had `EmbedData` been uninhabited, all four Claims would have been vacuously true
and `KSUM.A2.composition` / `KSUM.B2.composition` would have carried no content whatsoever.

The instance below is the one the reviewer arithmetically verified in §7.2 — `k = 3`, `n = 1`,
`R = 2`, `P = 12`, `Mv = 24`, `cP = 3`, hence `q = (P+1)(Mv+1) = 13 · 25 = 325` — with the
per-position value map `a ↦ (a : ZMod 325)`, injective because `R = 2 < 325`.  Every field is
discharged, none by `decide` on a hypothesis-free restatement:

    3 ∣ 12                              `k_dvd_P`
    2 · 25 = 50 = 7² + 1 = (2k+1)^{k-1}+1   `two_mul_Mv`
    R^{k-1} = 4 ≤ 12 = P                `P_lower`
    P = 12 ≤ 12 = 3 · 4 = cP · R^{k-1}  `P_upper`   (tight — `cP` is not slack here)

**What this does and does not settle.**  It settles that the four `∀ D : EmbedData` Claims are
*about something*, so the A2/B2 branch of the composition layer is not vacuously true.  It does
**not** claim that these particular parameters are the manuscript's `lem:embed` recipe evaluated
at `k = 3, R = 2`: `EmbedData` records only the properties `lem:embed-allt` consumes, and this
witness meets them.  It is a consistency witness, exactly as `KsumAudit.demoModel` is for
`QueryModel`, and it is no evidence at all that the manuscript's formulas satisfy the fields. -/

/-- **`EmbedData` is inhabited** (review §7.2 / R-A2-3): the `k = 3, n = 1, R = 2` instance with
`P = 12`, `Mv = 24`, `cP = 3`, modulus `q = 13 · 25 = 325`. -/
def demoEmbed : EmbedData where
  k := 3
  n := 1
  R := 2
  P := 12
  Mv := 24
  hk := le_refl 3
  hn := le_refl 1
  hR := le_refl 2
  k_dvd_P := ⟨4, rfl⟩
  two_mul_Mv := rfl
  cP := 3
  cP_pos := Nat.succ_pos 2
  P_lower := by norm_num
  P_upper := by norm_num
  enc := fun _ a => ((a : ℕ) : ZMod ((12 + 1) * (24 + 1)))
  enc_inj := by
    intro p a b hab
    have hval : ∀ c : Fin 2, (((c : ℕ) : ZMod ((12 + 1) * (24 + 1))).val) = (c : ℕ) := by
      intro c
      exact ZMod.val_natCast_of_lt (by have := c.isLt; omega)
    have h := congrArg ZMod.val hab
    rw [hval a, hval b] at h
    exact Fin.ext h

@[simp] theorem demoEmbed_q : demoEmbed.q = 325 := rfl

/-! ## The GENERAL construction of `lem:embed` / `prop:embed`  (gap-closure batch 2, item H-5)

`demoEmbed` above settles only that `EmbedData` is inhabited; the statement-fidelity review
(`ksum/reviews/ksum_lean_statement_fidelity_review_20260731.md` §10, KSUM-layer caveat (3)) recorded
that `KSUM.A2.Claim`'s `Θ_k(R^{k-1})` is therefore **per-`EmbedData`-instance rather than uniform
in `R`**, and §5 listed `prop:embed` among the labels *"not formalized"*.

This section removes that caveat by building `EmbedData` from the manuscript's own parameter
display, for **every** `k ≥ 3`, `n ≥ 1`, `R ≥ 2`:

    ω = 2R-1,   u_j = ω^{j}  (j < k-1),   u_{k-1} = -(ω^{k-1}-1)/(ω-1),
    P = k(R-1)(ω^{k-1}-1)/(ω-1),
    M = ((2k+1)^{k-1}-1)/2,  V = P+1,  w_j = V(2k+1)^{j} (j < k-1),  w_{k-1} = -∑_{j<k-1} w_j,
    q = (P+1)(M+1).

The two ℕ-divisions of the display are written as the geometric sums they abbreviate, so no
truncated subtraction ever enters a claim: `(ω^{k-1}-1)/(ω-1) = ∑_{i<k-1} ω^i` and
`((2k+1)^{k-1}-1)/2 = k ∑_{i<k-1}(2k+1)^i`.

**Scope.**  What is proved is that the manuscript's parameters satisfy every field of
`EmbedData` — including `k ∣ P`, `2(M+1) = (2k+1)^{k-1}+1`, the two-sided
`R^{k-1} ≤ P ≤ c_P R^{k-1}` with `c_P = k(k-1)2^{k-2}` depending only on `k`, and per-position
injectivity of the value map.  What is NOT proved here is the *encoding identity*
`kSum_{Z_q,0,kn}(encoded) = Coll_{k,n→R}(g)` itself (the balanced base-`ω` / base-`(2k+1)`
uniqueness argument of `prop:embed`'s proof): `KSUM.A2a`/`KSUM.A2b` carry that as their Claims and
`EmbedData` deliberately records only the properties `lem:embed-allt` consumes. -/

section GeneralEmbed

open Finset

/-- `ω = 2R - 1`. -/
def embedOmega (R : ℕ) : ℕ := 2 * R - 1

/-- `(ω^{k-1}-1)/(ω-1) = ∑_{i<k-1} ω^i` — the largest payload coefficient `|u_k|`. -/
def embedU (k R : ℕ) : ℕ := ∑ i ∈ range (k - 1), embedOmega R ^ i

/-- `P = k(R-1)(ω^{k-1}-1)/(ω-1)`. -/
def embedP (k R : ℕ) : ℕ := k * ((R - 1) * embedU k R)

/-- `M = ((2k+1)^{k-1}-1)/2 = k ∑_{i<k-1}(2k+1)^i`. -/
def embedM (k : ℕ) : ℕ := k * ∑ i ∈ range (k - 1), (2 * k + 1) ^ i

/-- The geometric-sum identity behind both ℕ-divisions: `d·∑_{i<m}(d+1)^i + 1 = (d+1)^m`. -/
theorem geom_mul_add_one (d : ℕ) : ∀ m : ℕ, d * (∑ i ∈ range m, (d + 1) ^ i) + 1 = (d + 1) ^ m := by
  intro m
  induction m with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_range_succ, Nat.mul_add]
      calc d * (∑ i ∈ range m, (d + 1) ^ i) + d * (d + 1) ^ m + 1
          = (d * (∑ i ∈ range m, (d + 1) ^ i) + 1) + d * (d + 1) ^ m := by ring
        _ = (d + 1) ^ m + d * (d + 1) ^ m := by rw [ih]
        _ = (d + 1) ^ (m + 1) := by rw [pow_succ]; ring

/-- **`2(M+1) = (2k+1)^{k-1}+1`** — the field `lem:embed-allt` uses to get `M+1 ≡ 1 (mod p)`. -/
theorem embed_two_mul_M (k : ℕ) : 2 * (embedM k + 1) = (2 * k + 1) ^ (k - 1) + 1 := by
  have h := geom_mul_add_one (2 * k) (k - 1)
  have hmul : 2 * embedM k = 2 * k * ∑ i ∈ range (k - 1), (2 * k + 1) ^ i := by
    rw [embedM]; ring
  omega

/-- `ω ≥ 3` for `R ≥ 2`. -/
theorem embed_three_le_omega {R : ℕ} (hR : 2 ≤ R) : 3 ≤ embedOmega R := by
  rw [embedOmega]; omega

/-- `R ≤ ω`. -/
theorem embed_R_le_omega {R : ℕ} (hR : 2 ≤ R) : R ≤ embedOmega R := by
  rw [embedOmega]; omega

/-- `ω ≤ 2R`. -/
theorem embed_omega_le {R : ℕ} : embedOmega R ≤ 2 * R := by
  rw [embedOmega]; omega

/-- `1 ≤ U`: the `i = 0` term of the sum is `1`, and `k - 1 ≥ 1`. -/
theorem embed_one_le_U {k R : ℕ} (hk : 3 ≤ k) : 1 ≤ embedU k R := by
  rw [embedU]
  have h0 : (0:ℕ) ∈ range (k - 1) := Finset.mem_range.mpr (by omega)
  calc 1 = embedOmega R ^ 0 := by simp
    _ ≤ ∑ i ∈ range (k - 1), embedOmega R ^ i :=
        Finset.single_le_sum (f := fun i => embedOmega R ^ i) (fun i _ => Nat.zero_le _) h0

/-- **`R^{k-1} ≤ P`.** -/
theorem embed_P_lower {k R : ℕ} (hk : 3 ≤ k) (hR : 2 ≤ R) : R ^ (k - 1) ≤ embedP k R := by
  have hmem : (k - 2) ∈ range (k - 1) := Finset.mem_range.mpr (by omega)
  have hU : embedOmega R ^ (k - 2) ≤ embedU k R :=
    Finset.single_le_sum (f := fun i => embedOmega R ^ i) (fun i _ => Nat.zero_le _) hmem
  have hpow : R ^ (k - 2) ≤ embedOmega R ^ (k - 2) :=
    Nat.pow_le_pow_left (embed_R_le_omega hR) _
  have hkR : R ≤ k * (R - 1) := by
    obtain ⟨R', rfl⟩ : ∃ R', R = R' + 2 := ⟨R - 2, by omega⟩
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 3 := ⟨k - 3, by omega⟩
    have hs : R' + 2 - 1 = R' + 1 := by omega
    rw [hs]
    nlinarith
  have hsplit : embedP k R = (k * (R - 1)) * embedU k R := by rw [embedP]; ring
  have hexp : R ^ (k - 1) = R * R ^ (k - 2) := by
    rw [← pow_succ']
    congr 1
    omega
  rw [hsplit, hexp]
  exact Nat.mul_le_mul hkR (le_trans hpow hU)

/-- **`P ≤ c_P·R^{k-1}` with `c_P = k(k-1)2^{k-2}` depending only on `k`.** -/
theorem embed_P_upper {k R : ℕ} (hk : 3 ≤ k) (hR : 2 ≤ R) :
    embedP k R ≤ (k * (k - 1) * 2 ^ (k - 2)) * R ^ (k - 1) := by
  have h3 : 3 ≤ embedOmega R := embed_three_le_omega hR
  have hterm : ∀ i ∈ range (k - 1), embedOmega R ^ i ≤ 2 ^ (k - 2) * R ^ (k - 2) := by
    intro i hi
    have hik : i < k - 1 := Finset.mem_range.mp hi
    have hi' : i ≤ k - 2 := by omega
    calc embedOmega R ^ i ≤ embedOmega R ^ (k - 2) := Nat.pow_le_pow_right (by omega) hi'
      _ ≤ (2 * R) ^ (k - 2) := Nat.pow_le_pow_left embed_omega_le _
      _ = 2 ^ (k - 2) * R ^ (k - 2) := by rw [Nat.mul_pow]
  have hU : embedU k R ≤ (k - 1) * (2 ^ (k - 2) * R ^ (k - 2)) := by
    rw [embedU]
    calc ∑ i ∈ range (k - 1), embedOmega R ^ i
        ≤ ∑ _i ∈ range (k - 1), 2 ^ (k - 2) * R ^ (k - 2) := Finset.sum_le_sum hterm
      _ = (k - 1) * (2 ^ (k - 2) * R ^ (k - 2)) := by
          rw [Finset.sum_const, Finset.card_range, smul_eq_mul]
  have hRm : R - 1 ≤ R := Nat.sub_le _ _
  have hexp : R ^ (k - 1) = R * R ^ (k - 2) := by
    rw [← pow_succ']
    congr 1
    omega
  calc embedP k R = k * ((R - 1) * embedU k R) := rfl
    _ ≤ k * (R * ((k - 1) * (2 ^ (k - 2) * R ^ (k - 2)))) :=
        Nat.mul_le_mul_left _ (Nat.mul_le_mul hRm hU)
    _ = (k * (k - 1) * 2 ^ (k - 2)) * (R * R ^ (k - 2)) := by ring
    _ = (k * (k - 1) * 2 ^ (k - 2)) * R ^ (k - 1) := by rw [hexp]

/-- The payload coefficients `u_j` (0-indexed): `u_j = ω^j` for `j < k-1` and `u_{k-1} = -U`. -/
def embedu (k R : ℕ) (j : ℕ) : ℤ :=
  if j < k - 1 then (embedOmega R : ℤ) ^ j else -(embedU k R : ℤ)

/-- The tag coefficients `w_j = V(2k+1)^j` for `j < k-1`, `w_{k-1} = -∑_{j<k-1} w_j`,
`V = P+1`. -/
def embedw (k R : ℕ) (j : ℕ) : ℤ :=
  if j < k - 1 then ((embedP k R + 1 : ℕ) : ℤ) * ((2 * k + 1 : ℕ) : ℤ) ^ j
  else -(((embedP k R + 1 : ℕ) : ℤ) * ∑ i ∈ range (k - 1), ((2 * k + 1 : ℕ) : ℤ) ^ i)

/-- Every payload coefficient is nonzero — the reason the per-position value map is injective. -/
theorem embedu_ne_zero {k R : ℕ} (hk : 3 ≤ k) (hR : 2 ≤ R) (j : ℕ) : embedu k R j ≠ 0 := by
  have homega : (0:ℤ) < (embedOmega R : ℤ) := by
    have h3 := embed_three_le_omega hR
    exact_mod_cast (by omega : 0 < embedOmega R)
  have hU : (0:ℤ) < (embedU k R : ℤ) := by
    have h1 := embed_one_le_U (k := k) (R := R) hk
    exact_mod_cast (by omega : 0 < embedU k R)
  rw [embedu]
  split
  · exact ne_of_gt (pow_pos homega j)
  · omega

/-- Every payload coefficient is bounded by `U` in absolute value: `|u_j| ≤ (ω^{k-1}-1)/(ω-1)`. -/
theorem embedu_abs_le (k R j : ℕ) : |embedu k R j| ≤ (embedU k R : ℤ) := by
  rw [embedu]
  split
  · rename_i hj
    have hmem : j ∈ range (k - 1) := Finset.mem_range.mpr hj
    have hle : embedOmega R ^ j ≤ embedU k R :=
      Finset.single_le_sum (f := fun i => embedOmega R ^ i) (fun i _ => Nat.zero_le _) hmem
    have hnn : (0:ℤ) ≤ (embedOmega R : ℤ) ^ j := by positivity
    rw [abs_of_nonneg hnn]
    have hcast : ((embedOmega R ^ j : ℕ) : ℤ) ≤ ((embedU k R : ℕ) : ℤ) := by exact_mod_cast hle
    simpa using hcast
  · rw [abs_neg, Nat.abs_cast]

/-- `U·(R-1) ≤ P`: the payload budget dominates the largest possible payload, which is exactly
what stops the encoding from wrapping around the modulus. -/
theorem embed_U_mul_le_P {k R : ℕ} (hk : 3 ≤ k) (hR : 2 ≤ R) :
    (embedU k R : ℤ) * ((R : ℤ) - 1) ≤ (embedP k R : ℤ) := by
  have hUpos : (0:ℤ) < (embedU k R : ℤ) := by
    have h1 := embed_one_le_U (k := k) (R := R) hk
    exact_mod_cast (by omega : 0 < embedU k R)
  have hk3 : (3:ℤ) ≤ (k : ℤ) := by exact_mod_cast hk
  have hR2 : (2:ℤ) ≤ (R : ℤ) := by exact_mod_cast hR
  have hcast : (embedP k R : ℤ) = (k : ℤ) * (((R : ℤ) - 1) * (embedU k R : ℤ)) := by
    rw [embedP]
    push_cast [Nat.cast_sub (by omega : 1 ≤ R)]
    ring
  rw [hcast]
  nlinarith

/-- `P < q = (P+1)(M+1)`. -/
theorem embed_P_lt_q (k R : ℕ) : embedP k R < (embedP k R + 1) * (embedM k + 1) := by
  have h1 : embedP k R + 1 ≤ (embedP k R + 1) * (embedM k + 1) :=
    Nat.le_mul_of_pos_right _ (Nat.succ_pos _)
  omega

/-- **Per-position injectivity of the value map `a ↦ w_j + u_j·a`.**  `|u_j·(a-b)| ≤ U(R-1) ≤ P
< q`, so the map does not wrap around; and every `u_j` is nonzero. -/
theorem embed_enc_inj {k R : ℕ} (hk : 3 ≤ k) (hR : 2 ≤ R) (j : ℕ) :
    Function.Injective (fun a : Fin R =>
      ((embedw k R j + embedu k R j * ((a : ℕ) : ℤ) : ℤ) :
        ZMod ((embedP k R + 1) * (embedM k + 1)))) := by
  haveI : NeZero ((embedP k R + 1) * (embedM k + 1)) :=
    ⟨Nat.mul_ne_zero (Nat.succ_ne_zero _) (Nat.succ_ne_zero _)⟩
  intro a b hab
  simp only at hab
  have heq : embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ))
      = (embedw k R j + embedu k R j * ((a : ℕ) : ℤ))
        - (embedw k R j + embedu k R j * ((b : ℕ) : ℤ)) := by ring
  have hzero : ((embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)) : ℤ) :
      ZMod ((embedP k R + 1) * (embedM k + 1))) = 0 := by
    rw [heq, Int.cast_sub, hab, sub_self]
  have hdvd : (((embedP k R + 1) * (embedM k + 1) : ℕ) : ℤ)
      ∣ embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)) :=
    (ZMod.intCast_zmod_eq_zero_iff_dvd _ _).mp hzero
  have hR2 : (2:ℤ) ≤ (R : ℤ) := by exact_mod_cast hR
  have h2 : |((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)| ≤ (R : ℤ) - 1 := by
    have ha : ((a : ℕ) : ℤ) < (R : ℤ) := by exact_mod_cast a.isLt
    have hb : ((b : ℕ) : ℤ) < (R : ℤ) := by exact_mod_cast b.isLt
    have ha0 : (0:ℤ) ≤ ((a : ℕ) : ℤ) := Int.natCast_nonneg _
    have hb0 : (0:ℤ) ≤ ((b : ℕ) : ℤ) := Int.natCast_nonneg _
    rw [abs_le]
    omega
  have hUpos : (0:ℤ) < (embedU k R : ℤ) := by
    have h1 := embed_one_le_U (k := k) (R := R) hk
    exact_mod_cast (by omega : 0 < embedU k R)
  have habs : |embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ))|
      < (((embedP k R + 1) * (embedM k + 1) : ℕ) : ℤ) := by
    have hPq : (embedP k R : ℤ) < (((embedP k R + 1) * (embedM k + 1) : ℕ) : ℤ) := by
      exact_mod_cast embed_P_lt_q k R
    calc |embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ))|
        = |embedu k R j| * |((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)| := abs_mul _ _
      _ ≤ (embedU k R : ℤ) * ((R : ℤ) - 1) :=
          mul_le_mul (embedu_abs_le k R j) h2 (abs_nonneg _) (by linarith)
      _ ≤ (embedP k R : ℤ) := embed_U_mul_le_P hk hR
      _ < _ := hPq
  have heq0 : embedu k R j * (((a : ℕ) : ℤ) - ((b : ℕ) : ℤ)) = 0 :=
    Int.eq_zero_of_abs_lt_dvd hdvd habs
  rcases mul_eq_zero.mp heq0 with h | h
  · exact absurd h (embedu_ne_zero hk hR j)
  · exact Fin.ext (by omega)

end GeneralEmbed

/-- **`EmbedData` for EVERY `k ≥ 3`, `n ≥ 1`, `R ≥ 2`**, built from the manuscript's own parameter
display (gap-closure batch 2, item H-5).  This is what makes `KSUM.A2.Claim`'s `Θ_k(R^{k-1})`
uniform in `R` rather than per-instance: for fixed `k`, the family `R ↦ genEmbed k n R _ _ _`
realizes every range `R ≥ 2` with one and the same `c_P = k(k-1)2^{k-2}`. -/
def genEmbed (k n R : ℕ) (hk : 3 ≤ k) (hn : 1 ≤ n) (hR : 2 ≤ R) : EmbedData where
  k := k
  n := n
  R := R
  P := embedP k R
  Mv := embedM k
  hk := hk
  hn := hn
  hR := hR
  k_dvd_P := ⟨(R - 1) * embedU k R, rfl⟩
  two_mul_Mv := embed_two_mul_M k
  cP := k * (k - 1) * 2 ^ (k - 2)
  cP_pos := by
    have h : 0 < k * (k - 1) := Nat.mul_pos (by omega) (by omega)
    positivity
  P_lower := embed_P_lower hk hR
  P_upper := embed_P_upper hk hR
  enc := fun p a =>
    ((embedw k R ((p : ℕ) / n) + embedu k R ((p : ℕ) / n) * ((a : ℕ) : ℤ) : ℤ) :
      ZMod ((embedP k R + 1) * (embedM k + 1)))
  enc_inj := fun p => embed_enc_inj hk hR ((p : ℕ) / n)

@[simp] theorem genEmbed_q (k n R : ℕ) (hk : 3 ≤ k) (hn : 1 ≤ n) (hR : 2 ≤ R) :
    (genEmbed k n R hk hn hR).q = (embedP k R + 1) * (embedM k + 1) := rfl

/-! ### Non-vacuity / sanity anchors for the general construction

`demoEmbed` (`k = 3`, `R = 2`, `q = 325`) is the anchor: the general construction at those
parameters gives `ω = 3`, `U = 1 + 3 = 4`, `P = 3·1·4 = 12`, `M = 3·(1 + 7) = 24`, hence
`q = 13·25 = 325` — the SAME modulus, arrived at from the formulas rather than by hand. -/

example : embedOmega 2 = 3 := rfl
example : embedU 3 2 = 4 := rfl
example : embedP 3 2 = 12 := rfl
example : embedM 3 = 24 := rfl

/-- The general construction reproduces `demoEmbed`'s modulus at `k = 3, R = 2`. -/
example : (genEmbed 3 1 2 (by norm_num) (by norm_num) (by norm_num)).q = 325 := rfl

/-- The two-sided bound at `k = 3, R = 2`: `R^{k-1} = 4 ≤ 12 = P ≤ 48 = c_P·R^{k-1}`. -/
example : 2 ^ (3 - 1) ≤ embedP 3 2 ∧ embedP 3 2 ≤ (3 * (3 - 1) * 2 ^ (3 - 2)) * 2 ^ (3 - 1) :=
  ⟨embed_P_lower (by norm_num) (by norm_num), embed_P_upper (by norm_num) (by norm_num)⟩

/-- A second, larger anchor: `k = 4`, `R = 3` gives `ω = 5`, `U = 1 + 5 + 25 = 31`,
`P = 4·2·31 = 248`, `M = 4·(1 + 9 + 81) = 364`, `q = 249·365 = 90885`. -/
example : (genEmbed 4 1 3 (by norm_num) (by norm_num) (by norm_num)).q = 90885 := rfl

#print axioms geom_mul_add_one
#print axioms embed_two_mul_M
#print axioms embed_P_lower
#print axioms embed_P_upper
#print axioms embed_enc_inj
#print axioms genEmbed

end KSUM.Support
