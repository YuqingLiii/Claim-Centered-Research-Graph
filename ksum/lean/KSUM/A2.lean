/-
`KSUM/A2.lean` — linked node module.
**This module's `composition` theorem IS the node's composition proof** (the current composition-linking convention).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A2                          (alias `A2`)
node file      : ksum/proof-dag/nodes/KSUM.A2.yaml
decomposition / role    : AND / proof     children: A2a, A2b
epistemic status (read from the node file on 2026-07-30): **CONJECTURED**
                 (assessment recomputed from the current node record; demoted from
                 PROVED because the prose composition proof is new and unreviewed.  A green build
                 here is EVIDENCE for that pending review, NOT a review — the current evidence-level rules.)
mechanization  : **composition-checked**, relative to
                 rel = [QueryModel.restrict + QueryModel.relabel (= sec:prelim facts (i)/(ii)),
                        which carry the query-freeness;
                        EmbedData (= the data of lem:embed: the payload/tag map `enc`, its
                        per-position injectivity `enc_inj`, and the four recorded arithmetic
                        facts about `P` and `M`)]
claim_hash     : sha256:7f375f3d8172fa71da3e856858fbb835d121d9ab95013db14978af7063da456b
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:3d32188ad689328d14a76d145156109cd422f7821990c111b5e357efc20f9c64

CURRENT CANONICAL CLAIM (verbatim from the node record):

  Lemma W3E-2 (AND): for every k≥3 and R≥2, the displayed construction gives an exact, query-free reduction from k-partite k-collision with range R to k-Sum over Z_q at one constructed modulus q=(P+1)(M+1)=Θ_k(R^{k−1}); the hidden constants depend only on k and are uniform in R.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  Lemma W3E-2 (AND): exact query-free reduction
  k-partite k-collision → k-Sum, q=Θ_k(R^{k−1}) [ENCODING PROVED]

FROZEN COMPOSITION CLAIM (verbatim from the node's `composition.claim`):

  A2a (the explicit payload/tag assignment u_j = omega^{j-1}, u_k = -(omega^{k-1}-1)/(omega-1),
  w_j = V*(2k+1)^{j-1} over the modulus q = (P+1)(M+1) sends every genuine k-partite k-collision
  to a k-subset summing to the target) AND A2b (in the balanced base-omega representation every
  WRONG block-multiset is excluded, so no non-collision produces a hit) together imply A2: the
  map is an exact, query-free reduction from k-partite k-collision with range R to kSum over Z_q
  with q = Theta_k(R^{k-1}).

════════════════════════════════════════════════════════════════════════════════════════════════
  **THE `gcd(k,q) = 1` QUESTION — SETTLED (commission gate G-R5)**
════════════════════════════════════════════════════════════════════════════════════════════════

The node's `composition.rel` records `gcd(k,q)=1` as *"the hypothesis of the 2026-07-19
replacement all-target proof, currently recorded only in this node's Work record and not in any
Claim"*, and its Open obligations ask to *"resolve where `gcd(k,q) = 1` lives: promote it into
the Claim, or show the construction forces it."*

**It is FORCED BY THE CONSTRUCTION, and the manuscript already proves it** — `lem:embed-allt`,
`ksum/paper/ksum_small_alphabet.tex`, appendix `app:embed`:

> First, `k ∣ P` by the definition `P = k(R-1)(ω^{k-1}-1)/(ω-1)`.  Hence `P+1 ≡ 1 (mod p)` for
> every prime `p ∣ k`.  Also `M+1 = ((2k+1)^{k-1}+1)/2`.  If `p` is an odd prime divisor of `k`,
> then `2k+1 ≡ 1 (mod p)`, so the numerator is `≡ 2 (mod p)` and, `2` being invertible mod `p`,
> `M+1 ≡ 1 (mod p)`.  If `2 ∣ k` then `2k+1 ≡ 1 (mod 4)`, so `(2k+1)^{k-1}+1 ≡ 2 (mod 4)` and
> `M+1` is odd.  Thus no prime divisor of `k` divides either `P+1` or `M+1`.

`coprime_k_q` below is that argument, machine-checked, from exactly the two recorded facts
`k ∣ P` and `2(M+1) = (2k+1)^{k-1}+1`.  So `gcd(k,q)=1` is **not** an extra hypothesis of the
composition: it is a theorem about `q = (P+1)(M+1)`, and it therefore belongs in `KSUM.A2`'s
Claim (as the all-targets clause below), not in its `rel`.

════════════════════════════════════════════════════════════════════════════════════════════════
  HYPOTHESES OF `composition` vs the node's `composition` block  (gate G-R3)
════════════════════════════════════════════════════════════════════════════════════════════════

  status-propagating children : A2a, A2b → the two explicit hypotheses `hA2a hA2b`
  declared `composition.rel`  : fact (ii) (query-freeness) → the parameter `M : QueryModel`
                              : `gcd(k,q)=1`               → **REMOVED**: proved, not assumed
  extra data                  : `EmbedData` is universally quantified INSIDE `Claim`, so it is
                                not a hypothesis of `composition`; its fields are the manuscript's
                                own construction data and each cites its display.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF — `Claim` is a CONCLUSION, so weakenings matter
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` has four conjuncts, matching the node's composition steps 3, 4, (the all-target
extension), and 5:

1. **exactness** — the encoded `kSum` predicate is literally equal to `Coll`, i.e. the "iff" that
   the word "exact" means (steps 1–3);
2. **query-freeness** — `Q(Coll) ≤ 2·Q(kSum)`, the absolute-constant simulation of step 4, which
   is `sec:prelim` fact (ii) applied to a fixed per-coordinate encoding;
3. **all targets** — multiplication by `k` is surjective on `Z_q`, which is the usable content of
   `lem:embed-allt` and the reason the target-`0` embedding extends to every `t`;
4. **the modulus count** — `R^{k-1} ≤ q ≤ c_q·R^{k-1}`, the two-sided form of `q = Θ_k(R^{k-1})`.

**Named gap in conjunct 4 (fidelity).**  The prose's `Θ_k` asserts constants depending on `k`
*uniformly in `R`*.  Here `c_q` is built from the instance's own `c_P` and `M`, both of which are
functions of `k` alone in `lem:embed` — but that uniformity is a property of the manuscript's
FORMULAS, and this rendering quantifies over `EmbedData` instances rather than over a family
indexed by `R`.  The two-sided bound is therefore per-instance.  The fidelity review must record
this; it is the one place where `Claim` is weaker than the frozen prose.

No `sorry`.
-/
import KSUM.A2a
import KSUM.A2b

namespace KSUM.A2

open KsumAudit KSUM.Support

/-! ## The coprimality theorem of `lem:embed-allt` (gate G-R5) -/

/-- `k` is coprime to `P+1` whenever `k ∣ P`: a common divisor divides both `P` and `P+1`.
LaTeX: `lem:embed-allt`, first sentence. -/
theorem coprime_k_succ_of_dvd {k P : ℕ} (h : k ∣ P) : Nat.Coprime k (P + 1) := by
  have h1 : Nat.gcd k (P + 1) ∣ P := dvd_trans (Nat.gcd_dvd_left _ _) h
  have h2 : Nat.gcd k (P + 1) ∣ P + 1 := Nat.gcd_dvd_right _ _
  have h3 : Nat.gcd k (P + 1) ∣ 1 := by simpa using Nat.dvd_sub h2 h1
  exact Nat.dvd_one.mp h3

/-- `k` is coprime to `M+1 = ((2k+1)^{k-1}+1)/2`.
LaTeX: `lem:embed-allt`, the two cases "odd prime divisor of `k`" and "`2 ∣ k`", here run
together through the gcd rather than prime by prime. -/
theorem coprime_k_MvSucc {k Mv : ℕ} (hk : 3 ≤ k)
    (hM : 2 * (Mv + 1) = (2 * k + 1) ^ (k - 1) + 1) : Nat.Coprime k (Mv + 1) := by
  set d := Nat.gcd k (Mv + 1) with hd
  have hdk : d ∣ k := Nat.gcd_dvd_left _ _
  have hdM : d ∣ Mv + 1 := Nat.gcd_dvd_right _ _
  -- `d ∣ 2`: modulo `d` we have `2k+1 ≡ 1`, hence `2(M+1) = (2k+1)^{k-1}+1 ≡ 2`, while `d ∣ M+1`
  -- forces `2(M+1) ≡ 0`.
  have hd2 : d ∣ 2 := by
    have hstep : d ∣ (2 * k + 1) ^ (k - 1) - 1 := by
      have hbase : d ∣ 2 * k + 1 - 1 := by simpa using Dvd.dvd.mul_left hdk 2
      have h1 : (2 * k + 1) ≡ 1 [MOD d] := ((Nat.modEq_iff_dvd' (by omega)).mpr hbase).symm
      have h2 : (2 * k + 1) ^ (k - 1) ≡ 1 [MOD d] := by simpa using h1.pow (k - 1)
      exact (Nat.modEq_iff_dvd' (Nat.one_le_pow _ _ (by omega))).mp h2.symm
    have hdvd0 : d ∣ 2 * (Mv + 1) := Dvd.dvd.mul_left hdM 2
    have : d ∣ (2 * k + 1) ^ (k - 1) + 1 := hM ▸ hdvd0
    have hge : 1 ≤ (2 * k + 1) ^ (k - 1) := Nat.one_le_pow _ _ (by omega)
    have := Nat.dvd_sub this hstep
    simpa [Nat.add_sub_sub_cancel hge] using this
  -- `d = 2` is impossible: then `2 ∣ k`, so `2k+1 ≡ 1 (mod 4)` and `2(M+1) ≡ 2 (mod 4)`,
  -- while `2 ∣ M+1` forces `4 ∣ 2(M+1)`.
  have hdne2 : d ≠ 2 := by
    intro h2
    rw [h2] at hdk hdM
    obtain ⟨r, hr⟩ := hdk
    obtain ⟨s, hs⟩ := hdM
    have hbase4 : (2 * k + 1) ≡ 1 [MOD 4] := by
      refine ((Nat.modEq_iff_dvd' (by omega)).mpr ?_).symm
      exact ⟨r, by omega⟩
    have hpow4 : (2 * k + 1) ^ (k - 1) ≡ 1 [MOD 4] := by simpa using hbase4.pow (k - 1)
    have h4dvd : (4 : ℕ) ∣ (2 * k + 1) ^ (k - 1) - 1 :=
      (Nat.modEq_iff_dvd' (Nat.one_le_pow _ _ (by omega))).mp hpow4.symm
    have h4dvd' : (4 : ℕ) ∣ 2 * (Mv + 1) := ⟨s, by omega⟩
    rw [hM] at h4dvd'
    have hge : 1 ≤ (2 * k + 1) ^ (k - 1) := Nat.one_le_pow _ _ (by omega)
    have := Nat.dvd_sub h4dvd' h4dvd
    rw [Nat.add_sub_sub_cancel hge] at this
    omega
  have hdne0 : d ≠ 0 := by
    intro h0
    rw [h0, Nat.zero_dvd] at hdk
    omega
  have hdle : d ≤ 2 := Nat.le_of_dvd (by norm_num) hd2
  show d = 1
  omega

/-- **`gcd(k, q) = 1` is forced by the construction `q = (P+1)(M+1)`** — `lem:embed-allt`,
machine-checked.  This is the answer to the node's Open obligation "promote it into the Claim, or
show the construction forces it": the construction forces it. -/
theorem coprime_k_q (D : EmbedData) : Nat.Coprime D.k D.q :=
  Nat.Coprime.mul_right (coprime_k_succ_of_dvd D.k_dvd_P)
    (coprime_k_MvSucc D.hk D.two_mul_Mv)

/-- Consequence used by the all-targets clause: multiplication by `k` is surjective on `Z_q`, so
the target-`0` embedding translates to every target (`lem:embed-allt`, last paragraph). -/
theorem nsmul_surjective (D : EmbedData) (t : ZMod D.q) : ∃ a : ZMod D.q, D.k • a = t := by
  have hu : IsUnit ((D.k : ℕ) : ZMod D.q) := (ZMod.isUnit_iff_coprime D.k D.q).mpr (coprime_k_q D)
  obtain ⟨u, hu'⟩ := hu
  refine ⟨(↑u⁻¹ : ZMod D.q) * t, ?_⟩
  rw [nsmul_eq_mul, ← hu', ← mul_assoc]
  simp

/-! ## The node's Claim and its composition proof -/

/-- **`KSUM.A2`, formal Claim** — the exact, query-free reduction of `lem:embed`.
Four conjuncts: exactness, query-freeness at absolute constant `2`, the all-targets extension,
and the two-sided modulus count `R^{k-1} ≤ q ≤ c_q·R^{k-1}`. -/
def Claim (M : QueryModel) : Prop :=
  ∀ D : EmbedData,
    (∀ g : Fin (D.k * D.n) → Fin D.R,
        kSum (ZMod D.q) D.k 0 (D.k * D.n) (D.encodeInst g) = Coll D.k D.n D.R g) ∧
      M.Q (Coll D.k D.n D.R) ≤ 2 * M.Q (kSum (ZMod D.q) D.k 0 (D.k * D.n)) ∧
      (∀ t : ZMod D.q, ∃ a : ZMod D.q, D.k • a = t) ∧
      (∃ cq : ℕ, 0 < cq ∧ D.R ^ (D.k - 1) ≤ D.q ∧ D.q ≤ cq * D.R ^ (D.k - 1))

/-- **The composition proof of `KSUM.A2`, mechanized.**

`A2a ∧ A2b ⇒ A2`, relative to the `QueryModel` interface (facts (i) and (ii), which carry the
query-freeness) and the data of `lem:embed`.

A green build of this theorem is a *run* under the current evidence-level rules and therefore evidence at
NUMERICAL tier at best; it does not promote `KSUM.A2`, whose composition proof is awaiting an
independent rule-6/rule-7 review. -/
theorem composition (M : QueryModel) (hA2a : KSUM.A2a.Claim) (hA2b : KSUM.A2b.Claim) :
    Claim M := by
  intro D
  -- 1 + 2 + 3.  Completeness and soundness are the two directions of one `iff`; that iff IS
  -- what "exact reduction" means.
  have hexact : ∀ g : Fin (D.k * D.n) → Fin D.R,
      kSum (ZMod D.q) D.k 0 (D.k * D.n) (D.encodeInst g) = Coll D.k D.n D.R g := by
    intro g
    exact Bool.eq_iff_iff.mpr ⟨hA2b D g, hA2a D g⟩
  refine ⟨hexact, ?_, nsmul_surjective D, ?_⟩
  · -- 4.  Query-freeness: the encoding is a FIXED per-coordinate injection, so `sec:prelim`
    -- facts (i)+(ii) cost the absolute factor 2.
    have hfun : (fun g : Fin (D.k * D.n) → Fin D.R =>
        kSum (ZMod D.q) D.k 0 (D.k * D.n) (fun p => D.enc p (g p))) = Coll D.k D.n D.R := by
      funext g; exact hexact g
    have key := M.relabel_inj (Alph := fun _ : Fin (D.k * D.n) => ZMod D.q)
      (Alph' := fun _ : Fin (D.k * D.n) => Fin D.R) (fun p => D.enc p) D.enc_inj
      (kSum (ZMod D.q) D.k 0 (D.k * D.n))
    rwa [hfun] at key
  · -- 5.  The modulus count `q = (P+1)(M+1) = Θ_k(R^{k-1})`, two-sided.
    refine ⟨(D.cP + 1) * (D.Mv + 1), Nat.succ_mul_pos _ (Nat.succ_pos _), ?_, ?_⟩
    · calc D.R ^ (D.k - 1) ≤ D.P + 1 := by have := D.P_lower; omega
        _ ≤ (D.P + 1) * (D.Mv + 1) := Nat.le_mul_of_pos_right _ (Nat.succ_pos _)
        _ = D.q := rfl
    · have hR1 : 1 ≤ D.R ^ (D.k - 1) := Nat.one_le_pow _ _ (by have := D.hR; omega)
      have hP : D.P + 1 ≤ (D.cP + 1) * D.R ^ (D.k - 1) := by
        have := D.P_upper; nlinarith [D.P_upper, hR1]
      calc D.q = (D.P + 1) * (D.Mv + 1) := rfl
        _ ≤ ((D.cP + 1) * D.R ^ (D.k - 1)) * (D.Mv + 1) :=
            Nat.mul_le_mul_right _ hP
        _ = (D.cP + 1) * (D.Mv + 1) * D.R ^ (D.k - 1) := by ring

end KSUM.A2
