/-
`KSUM/A1.lean` — linked node module.
**This module's `composition` theorem IS the node's composition proof** (the current composition-linking convention).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A1                          (alias `A1`)
node file      : ksum/proof-dag/nodes/KSUM.A1.yaml
decomposition / role    : AND / proof     children: A1a, A1b, A1c, A1d
epistemic status (read from the node file on 2026-07-30): **CONJECTURED**
                 (assessment recomputed from the current node record; demoted from
                 PROVED because the prose composition proof is new and unreviewed.  A green build
                 here is EVIDENCE for that pending review, NOT a review — the current evidence-level rules.)
mechanization  : **composition-checked** — and, since the 2026-07-30 R-A1-1/R-A1-3 repair batch,
                 with all three child Claims themselves PROVED, so `KSUM.A1.holds` closes
                 `Claim` outright — relative to
                 rel = [QueryModel.abi/tani (= ABI21 + Tani24, cited);
                        QueryModel.restrict (= sec:prelim fact (i));
                        QueryModel.relabel  (= sec:prelim fact (ii));
                        QueryModel.freeze   (= sec:prelim facts (i)+(iii) composed at the last
                                               position — coordinate freezing; STATED in the
                                               manuscript in the reviewed manuscript, explicitly recorded after external review
                                               as audit finding F1)]
claim_hash     : sha256:c9f8aa1f93e19a5ced2cbad5829906c0be6fc8d783bc47d580807f73e92fc2dc
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:ee8ff595289aacafbaa83b36b68426d91decaad2d2b3ac745a389978115c99ef

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For every fixed k>=3, the frozen core (A1a), the live two-list encoding (A1b), and target-coset coverage (A1c) compose to establish the small-alphabet k-Sum reduction and the lower bounds stated in A1d.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  Lemma W3E-1 = Theorem C (AND) — the REPAIRED reduction
  [PROVED-BY-REDUCTION mod donor · INDEPENDENTLY AUDITED F1 2026-07-18]

That text is a label, not a proposition.  The node file resolves this explicitly: *"`A1d`
restates the target conclusion rather than supplying an input, so the composition claim is
literally `A1a ∧ A1b ∧ A1c ⇒ A1d` and `A1`'s own claim is `A1d`'s.  The current graph retains
both claims until an independent review adjudicates their boundary."*  This module follows that
registered dependency structure:
`KSUM.A1.Claim := KSUM.A1d.Claim`.

FROZEN COMPOSITION CLAIM (verbatim from the node's `composition.claim`):

  A1a (a positive frozen core of k-2 coordinates exists that no unintended k-subset can sum to
  the target) AND A1b (the live 2n coordinates admit the even k=2 claw encoding with no unpaired
  live coordinate) AND A1c (the window family plus the translation identity reach every target t)
  together imply A1d: for every fixed k>=3 there are constants C_k, c_k > 0 such that for all
  sufficiently large N, every target t, and every q with 2k^2+2k-5 <= q <= C_k*N,
  Q(kSum_{Z_q,t,N}) = Omega_k(sqrt(N) q^{1/6}); and Omega_k(N^{2/3}) for q >= c_k*N.

════════════════════════════════════════════════════════════════════════════════════════════════
  HYPOTHESES OF `composition` vs the node's `composition` block  (gate G-R3)
════════════════════════════════════════════════════════════════════════════════════════════════

  status-propagating children : A1a, A1b, A1c  → the three explicit hypotheses `hA1a hA1b hA1c`
                                A1d            → the CONCLUSION (`Claim = A1d.Claim`)
  declared `composition.rel`  : ABI21/Tani24, fact (i), fact (ii), and coordinate freezing
                                (facts (i)+(iii); originally the unstated principle F1, stated
                                in the manuscript in the reviewed manuscript) → all four are fields of the
                                single parameter `M : QueryModel`, and none is used outside it
  extra hypotheses            : NONE.  In particular `gcd(k,q) = 1` does NOT appear — see the
                                quantifier note in `KSUM/A1c.lean`: `lem:transl-cover`'s covering
                                argument runs off the window length `≥ k ≥ gcd(k,q)`, not off
                                coprimality.

The four fields of `M` used are exactly: `tani` (ABI21/Tani24), `restrict` + `relabel` (facts (i)
and (ii), through `QueryModel.relabel_inj`), and `freeze` (facts (i)+(iii); originally F1,
through `KSUM.Support.Q_frozen_le`).  `cABI`/`cABI_pos` are the bookkeeping constant of `tani`.

════════════════════════════════════════════════════════════════════════════════════════════════
  THE COMPOSITION, STEP BY STEP — the same four steps as the node's prose proof
════════════════════════════════════════════════════════════════════════════════════════════════

0. **Cover the target (A1c), FIRST — this is the 2026-07-30 R-A1-3 repair.**  For the given `t`,
   the coset-covering Claim produces a shift `a` and a WINDOW target `s ∈ [t₀, t₀+k)` with
   `s = t + k·a` (same coset) and `Q(kSum_s) ≤ C·Q(kSum_t)`.  The window target is chosen by the
   covering argument, not by `A1a`; the old proof consumed the reverse (an all-pairs transfer
   from a target of `A1a`'s choosing), which is the premise the review refuted.
1. **Freeze (A1a) at that window target.**  A core `c` of `m ∈ {k-2, k-1}` coordinates for which
   the residual problem on the encoded live block is `2Sum` at `0`.  (`m = k-1` is the parked
   coordinate of `lem:core-odd`, which is what lets the composition hit EVERY length `N`, both
   parities, rather than only `N ≡ k-2 (mod 2)`.)
2. **Encode (A1b).**  On the `2n` live coordinates, `2Sum` at `0` read through `E` is `Claw`.
   Composing 1 and 2: `Claw_{n→κ} = (frozen kSum) ∘ E`.
3. **Transfer.**  `E` is a per-coordinate injection, so facts (i)+(ii) cost the absolute factor
   `2` (`QueryModel.relabel_inj`); freezing `m` coordinates costs nothing (`Q_frozen_le`, i.e.
   `m` applications of the F1 field).  Hence `Q(Claw) ≤ 2·Q(kSum_s)`.
4. **Exponent arithmetic.**  `QueryModel.tani` bounds `Q(Claw_{n→κ})` below by
   `c_ABI·√n·κ^{1/6}`; chaining through steps 0–3 gives `c_ABI·√n·κ^{1/6} ≤ 2C·Q(kSum_t)`; and
   `KsumAudit.combine_bound` converts `(n, κ)` into `(N, q)` through `N ≤ 3n` and `q ≤ 2k²κ`.
   The plateau clause follows by substituting `q ≥ N/2` and `√N·N^{1/6} = N^{2/3}`.

**The claw alphabet is `thm:kfloor`'s, not the `k = 2` one.**  Step 4 must take
`κ = ⌊(q-2k+1)/(k²-2)⌋`, the largest `κ` inside `lem:core-odd`'s window `(k²-2)κ + 2k-1 ≤ q` —
NOT the `κ = ⌊(q-1)/2⌋` that tier T1 uses at `k = 2`, which lies outside that window for every
`k ≥ 3` (see the note in `KSUM/A1a.lean`).  `2 ≤ κ` for this choice is *equivalent* to
`q ≥ 2k²+2k-5 = q₀(k)`, which is why `A1d`'s window floor is what it is; the two-sided estimate
`q ≤ 2k²·κ` that `combine_bound` needs is proved inline below.

Constants actually delivered (all exhibited, none asymptotic):
`C_k = 1`, `c_k = 1/2`, `A = c_ABI / (2·C·√3·(2k²)^{1/6})`, `B = A·(1/2)^{1/6}`, `N₀ = 40k+40`,
with `C` the absolute constant of `A1c`.  The `k`-dependence of `A` sits entirely in the
`(2k²)^{1/6}` coming from `κ = Θ_k(q)`, which is exactly where `thm:kfloor`'s `Ω_k` puts it.

════════════════════════════════════════════════════════════════════════════════════════════════
  NON-VACUITY — DISCHARGED 2026-07-30 (it was the named gap of this module)
════════════════════════════════════════════════════════════════════════════════════════════════

* `KSUM.A1b.Claim` is PROVED for every `M` (`KSUM.A1b.holds`).
* `KSUM.A1a.Claim` is PROVED unconditionally, now at EVERY window target
  (`KSUM.A1a.holds` ← `KsumAudit.KFloor.core_reduction_at` = `prop:core-even` + `lem:core-odd`).
* `KSUM.A1c.Claim` is PROVED for every `M` in its repaired coset-covering form
  (`KSUM.A1c.holds` ← `Q_window_cover_coset` = `lem:transl-cover`), with `C = 2`.
* `KsumAudit.demoModel` inhabits `QueryModel`, so the interface itself is not empty.

Consequently the three hypotheses of `composition` are **jointly satisfiable for every `M`** —
`KSUM.A1.holds` below composes them — and finding **F-R8** (joint satisfiability not
machine-checked) is closed rather than narrowed.  The earlier record of this gap is preserved in
the node file's work log and in tier T2's report; the `k=3, q=3` observation that used to block a
cheap witness is now irrelevant, because the repaired `A1c.Claim` no longer asserts anything
about pairs of targets in different cosets.

No `sorry`.
-/
import KSUM.A1a
import KSUM.A1b
import KSUM.A1c

namespace KSUM.A1

open KsumAudit KSUM.Support

/-- **`KSUM.A1`, formal Claim.**  The explicit-constant version of the lower-bound conclusion.

The proposition is written here rather than imported through the duplicate `KSUM.A1d` record, so
the module's imports agree with this node's actual premises `A1a`, `A1b`, and `A1c`. -/
def Claim (M : QueryModel) : Prop :=
  ∀ k : ℕ, 3 ≤ k →
    ∃ Ck ck A B : ℝ, 0 < Ck ∧ 0 < ck ∧ 0 < A ∧ 0 < B ∧ ∃ N₀ : ℕ,
      ∀ (N q : ℕ) [NeZero q], N₀ ≤ N → 2 * k ^ 2 + 2 * k - 5 ≤ q → (q : ℝ) ≤ Ck * N →
        ∀ t : ZMod q,
          A * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (kSum (ZMod q) k t N) ∧
            (ck * N ≤ (q : ℝ) → B * (N : ℝ) ^ (2 / 3 : ℝ) ≤ M.Q (kSum (ZMod q) k t N))

/-- **The composition proof of `KSUM.A1`, mechanized.**

`A1a ∧ A1b ∧ A1c ⇒ A1d`, relative to the `QueryModel` interface (ABI21/Tani24 as citations, and
`sec:prelim` facts (i), (ii) and (iii) — the last through coordinate freezing, originally the
unstated principle F1 and stated in the manuscript in the reviewed manuscript).

A green build of this theorem is run evidence and does not by itself promote `KSUM.A1`.  The
canonical node is now `PROVED` because this composition also passed the independent review linked
from that node. -/
theorem composition (M : QueryModel)
    (hA1a : KSUM.A1a.Claim) (hA1b : KSUM.A1b.Claim) (hA1c : KSUM.A1c.Claim M) :
    Claim M := by
  obtain ⟨C, hCpos, hcover⟩ := hA1c
  intro k hk
  have hkposℕ : 0 < k := by omega
  have hkpos : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hkposℕ
  have hd2R : (0 : ℝ) < 2 * (k : ℝ) ^ 2 := mul_pos two_pos (pow_pos hkpos 2)
  have hs3 : (0 : ℝ) < Real.sqrt 3 * (2 * (k : ℝ) ^ 2) ^ (1 / 6 : ℝ) :=
    mul_pos (Real.sqrt_pos.mpr (by norm_num)) (Real.rpow_pos_of_pos hd2R _)
  have hden : (0 : ℝ) < 2 * C * (Real.sqrt 3 * (2 * (k : ℝ) ^ 2) ^ (1 / 6 : ℝ)) :=
    mul_pos (mul_pos two_pos hCpos) hs3
  set A : ℝ := M.cABI / (2 * C * (Real.sqrt 3 * (2 * (k : ℝ) ^ 2) ^ (1 / 6 : ℝ))) with hAdef
  have hApos : 0 < A := div_pos M.cABI_pos hden
  set B : ℝ := A * (1 / 2 : ℝ) ^ (1 / 6 : ℝ) with hBdef
  have hBpos : 0 < B := mul_pos hApos (Real.rpow_pos_of_pos (by norm_num) _)
  refine ⟨1, 1 / 2, A, B, one_pos, by norm_num, hApos, hBpos, 40 * k + 40, ?_⟩
  intro N q _inst hN hq0 hqN t
  -- ℕ-level form of the window ceiling `q ≤ C_k·N` with `C_k = 1`
  have hqN' : q ≤ N := by
    have h : (q : ℝ) ≤ (N : ℝ) := by simpa using hqN
    exact_mod_cast h
  -- split `N = 2n + m` with `k-2 ≤ m ≤ k-1`: `m = k-2` (even live block) or `m = k-1` (parked)
  obtain ⟨n, m, hm1, hm2, rfl⟩ :
      ∃ n m : ℕ, k - 2 ≤ m ∧ m ≤ k - 1 ∧ N = 2 * n + m :=
    ⟨(N - (k - 2)) / 2, (k - 2) + (N - (k - 2)) % 2, by omega, by omega, by omega⟩
  -- `thm:kfloor`'s claw alphabet: `κ = ⌊(q - 2k + 1)/(k² - 2)⌋`, the largest `κ` inside
  -- `lem:core-odd`'s window.  `2 ≤ κ` is equivalent to `q ≥ q₀(k) = 2k²+2k-5`.
  have hk2 : 9 ≤ k ^ 2 := by
    have h := Nat.pow_le_pow_left hk 2
    simpa using h
  have h2k : 2 * k ≤ k ^ 2 := by nlinarith
  have hq19 : 19 ≤ q := by omega
  obtain ⟨κ, hκ2, hwin, hq2k2⟩ :
      ∃ κ : ℕ, 2 ≤ κ ∧ (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q ∧ q ≤ 2 * k ^ 2 * κ := by
    have hD0 : 0 < k ^ 2 - 2 := by omega
    have hDplus : k ^ 2 - 2 + 2 = k ^ 2 := by omega
    set D := k ^ 2 - 2 with hDdef
    set a := q - (2 * k - 1) with hadef
    have hκ2' : 2 ≤ a / D := (Nat.le_div_iff_mul_le hD0).mpr (by omega)
    refine ⟨a / D, hκ2', ?_, ?_⟩
    · have hlb : a / D * D ≤ a := Nat.div_mul_le_self a D
      have hcomm : D * (a / D) = a / D * D := Nat.mul_comm _ _
      omega
    · have hub : a < (a / D + 1) * D := (Nat.div_lt_iff_lt_mul hD0).mp (Nat.lt_succ_self _)
      have hcomm : (a / D + 1) * D = D * (a / D) + D := by ring
      have hDk : D * 2 ≤ D * (a / D) := Nat.mul_le_mul (le_refl D) hκ2'
      have hexp : 2 * k ^ 2 * (a / D) = 2 * (D * (a / D)) + 4 * (a / D) := by
        rw [← hDplus]; ring
      omega
  have hwinlin : 7 * κ ≤ (k ^ 2 - 2) * κ := Nat.mul_le_mul (by omega) (le_refl κ)
  have hqκ : 2 * κ + 1 ≤ q := by omega
  have hκ2n : κ < 2 * n := by omega
  have hd1 : 2 * n + m ≤ 3 * n := by omega
  have hd2pos : 0 < 2 * k ^ 2 := by omega
  -- 0. cover the target (A1c, coset-covering form): a WINDOW target `s` inside `t`'s own coset
  --    `t + kZ_q`, with `Q(kSum_s) ≤ C·Q(kSum_t)`.  The window target is chosen by the covering
  --    argument, not by `A1a` — which is why `A1a` must hold at every window target.
  obtain ⟨_a, s, hs1, hs2, _hcoset, hliftq⟩ := hcover k (2 * n + m) q κ hk hwin t
  -- 1. freeze the core AT THAT WINDOW TARGET (A1a)
  obtain ⟨c, hcore⟩ :=
    KSUM.A1a.frozen_form hA1a k q n m κ s hk hm1 hm2 hκ2 hwin (by omega) hs1 hs2
  -- 1 + 2: `Claw = (frozen kSum) ∘ E`  (A1a and A1b)
  have hclaw_eq : (fun y : Fin (2 * n) → Fin κ =>
      frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
        (fun p => encMap n (cyc q κ) p (y p)))
      = Claw n κ := by
    funext y
    change frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
      (encode n (cyc q κ) y) = Claw n κ y
    rw [hcore y, hA1b n κ q hqκ y]
  -- 3. transfer: facts (i) + (ii) cost the factor 2, freezing costs nothing
  have htrans : M.Q (Claw n κ)
      ≤ 2 * M.Q (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c) := by
    have key := M.relabel_inj (Alph := fun _ : Fin (2 * n) => ZMod q)
      (Alph' := fun _ : Fin (2 * n) => Fin κ) (fun p => encMap n (cyc q κ) p)
      (encMap_injective n (cyc q κ) (cyc_injective hqκ))
      (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c)
    rwa [hclaw_eq] at key
  have hfrz : M.Q (frozen m (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c)
      ≤ M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) :=
    Q_frozen_le M (G := ZMod q) (nlive := 2 * n) m
      (kSum (ZMod q) k ((s : ℕ) : ZMod q) (2 * n + m)) c
  -- 4. import the claw bound
  have htani := M.tani n κ hκ2 hκ2n
  have hchain : M.cABI * Real.sqrt n * (κ : ℝ) ^ (1 / 6 : ℝ)
      ≤ 2 * (C * M.Q (kSum (ZMod q) k t (2 * n + m))) := by linarith
  have hfin := combine_bound M.cABI M.cABI_pos (2 * n + m) n q κ 3 (2 * k ^ 2) (by norm_num)
    hd2pos hd1 hq2k2 (2 * (C * M.Q (kSum (ZMod q) k t (2 * n + m)))) hchain
  push_cast at hfin
  -- first conclusion: `A · √N · q^{1/6} ≤ Q`
  have hmain : A * Real.sqrt ((2 * n + m : ℕ) : ℝ) * (q : ℝ) ^ (1 / 6 : ℝ)
      ≤ M.Q (kSum (ZMod q) k t (2 * n + m)) := by
    have hEq : A * Real.sqrt ((2 * n + m : ℕ) : ℝ) * (q : ℝ) ^ (1 / 6 : ℝ)
        = (M.cABI / (Real.sqrt 3 * (2 * (k : ℝ) ^ 2) ^ (1 / 6 : ℝ))
            * Real.sqrt ((2 * n + m : ℕ) : ℝ) * (q : ℝ) ^ (1 / 6 : ℝ)) / (2 * C) := by
      rw [hAdef]; field_simp
    rw [hEq, div_le_iff₀ (mul_pos two_pos hCpos)]
    push_cast
    linarith [hfin]
  refine ⟨hmain, ?_⟩
  -- second conclusion: the plateau `B · N^{2/3} ≤ Q` once `q ≥ N/2`
  intro hpl
  have hNpos : 0 < 2 * n + m := by omega
  have hrq : (1 / 2 : ℝ) ^ (1 / 6 : ℝ) * ((2 * n + m : ℕ) : ℝ) ^ (1 / 6 : ℝ)
      ≤ (q : ℝ) ^ (1 / 6 : ℝ) := by
    rw [← Real.mul_rpow (by norm_num) (Nat.cast_nonneg _)]
    exact Real.rpow_le_rpow (by positivity) hpl (by norm_num)
  have hmulnn : (0 : ℝ) ≤ A * Real.sqrt ((2 * n + m : ℕ) : ℝ) :=
    mul_nonneg hApos.le (Real.sqrt_nonneg _)
  have hsq := sqrt_mul_rpow_eq (2 * n + m) hNpos
  calc B * ((2 * n + m : ℕ) : ℝ) ^ (2 / 3 : ℝ)
      = A * Real.sqrt ((2 * n + m : ℕ) : ℝ)
          * ((1 / 2 : ℝ) ^ (1 / 6 : ℝ) * ((2 * n + m : ℕ) : ℝ) ^ (1 / 6 : ℝ)) := by
        rw [← hsq, hBdef]; ring
    _ ≤ A * Real.sqrt ((2 * n + m : ℕ) : ℝ) * (q : ℝ) ^ (1 / 6 : ℝ) :=
        mul_le_mul_of_nonneg_left hrq hmulnn
    _ ≤ M.Q (kSum (ZMod q) k t (2 * n + m)) := hmain

/-- **`KSUM.A1.Claim` holds relative to the interface** (the current composition-linking convention: "once all necessary
children have closed proofs, an optional `holds : Claim` composes them").

Available only since the 2026-07-30 repair batch, and it is the point of that batch: all three
child Claims are now theorems — `KSUM.A1a.holds` (every window target), `KSUM.A1b.holds`,
`KSUM.A1c.holds` (coset covering) — so `composition` no longer rests on any unproved leaf, and
its hypotheses are **jointly satisfiable for every `M`**, which discharges the named non-vacuity
gap (finding F-R8) completely rather than narrowing it.

What remains relative is exactly the interface: `M.tani` is ABI21/Tani24 on trust, `M.restrict`
and `M.relabel` are `sec:prelim` facts (i)/(ii), and `M.freeze` is coordinate freezing = facts
(i)+(iii) composed (originally the unstated principle F1; stated in the manuscript in the reviewed manuscript).
A theorem proved against an abstract interface is exactly as strong as the results that
interface cites, and not one notch stronger. -/
theorem holds (M : QueryModel) : Claim M :=
  composition M KSUM.A1a.holds KSUM.A1b.holds (KSUM.A1c.holds M)

end KSUM.A1
