/-
`KSUM/A1c.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A1c                        (alias `A1c`)
node file      : ksum/proof-dag/nodes/KSUM.A1c.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record)
mechanization  : **proved** (repair batch 2026-07-30) — `Claim` was RESTATED in the
                 coset-covering form prescribed by review finding R-A1-3, and in that form it is
                 proved outright, with the explicit constant `C = 2` (`holds`, from
                 `Q_window_cover_coset`).  The previous ALL-PAIRS rendering survives as the
                 named relic `ClaimAllPairs`; it is underivable, see the box below.  Mechanized
                 here: the translation identity (`kSum_translate`), its query-complexity transfer
                 (`Q_kSum_translate_le`), the covering statement with and without the coset
                 witness (`Q_window_cover_coset` / `Q_window_cover`), `Claim` (`holds`), the
                 all-pairs form under the extra hypothesis `gcd(k,q) = 1` (`Q_le_of_coprime`),
                 and the obstruction `not_reachable_k3_q21`.  The window arithmetic itself is
                 `KsumAudit.KFloor.window_even_length` / `window_odd_length` /
                 `exists_shift_into_window`.
claim_hash     : sha256:ed56ed4dc5ce8212ecc8d858ba12c4c492fa710803cc2586f0090339d99764dd
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:440432db8a151ea3709d715cde9b8e451545a1337424a19e4945fe303184e8e4

CURRENT CANONICAL CLAIM (verbatim from the node record):

  The translation identity k-Sum_t(x)=k-Sum_(t+ka)(x+a*1) implies that, for every target t, there is a window target t' in t+kZ_q with Q(k-Sum_t)>=Q(k-Sum_(t'))/C for an absolute constant C, without parity or coprimality assumptions.

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  target coverage, COSET-COVERING form: window family + translation identity
  k-Sum_t(x)=k-Sum_{t+ka}(x+a·1); for EVERY target t there is a window target t′ ∈ t+kZ_q with
  Q(kSum_t) ≥ Q(kSum_{t′})/C for one absolute constant C — no parity and no coprimality condition
  [PROVED — restated 2026-07-30 per review R-A1-3; the earlier all-pairs-of-targets rendering is
  NOT what lem:transl-cover proves and is kept only as a refuted relic]

  (Previous frozen text, superseded 2026-07-30 — kept so the earlier hash resolves:
   "target coverage: window family + translation identity
    k-Sum_t(x)=k-Sum_{t+ka}(x+a·1), all t via gcd argument, no parity cond. [PROVED]",
   sha256:049957e532d17bfce4e5fdc70e943ced22fa432b5e44cda982d8988ce830fb9c.)

Manuscript: `lem:transl-cover`, `ksum/paper/ksum_small_alphabet.tex`, appendix `app:k3`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF — and the resolution of one quantifier question (rule 7g)
════════════════════════════════════════════════════════════════════════════════════════════════

`Claim` renders what `KSUM.A1`'s composition consumes in its step 3 — *"Steps 1–2 naturally
produce one target.  A1c's window family plus the translation identity … lifts the bound to
arbitrary `t`"* — namely, **since 2026-07-30**: *every target is at least as hard as some window
target of its own coset, up to one absolute constant.*  (Before that date it read "any two
targets have `Q` equal up to one absolute constant", which is strictly stronger and is not what
`lem:transl-cover` proves; see the repair box below.)

**"all t via gcd argument, no parity cond." does NOT hide a coprimality hypothesis.**  This was
checked against the manuscript rather than guessed.  `lem:transl-cover`'s covering argument is:
`gcd(k,q) ≤ k`; the coset `t + kZ_q` is the set of residues `≡ t (mod gcd(k,q))`, spaced
`gcd(k,q)` apart; **any window of at least `gcd(k,q)` consecutive residues meets it**; and the
modulus hypothesis makes the window length `≥ k ≥ gcd(k,q)`.  So coverage comes from the WINDOW
FAMILY, not from `k` being invertible, and `Claim` correctly carries no `Nat.Coprime k q`
hypothesis.  (Contrast `KSUM.A2`, where `gcd(k,q) = 1` genuinely is used — and, as
`KSUM/A2.lean` proves, is forced by the construction of `q`.)

Deliberate differences from the prose:

1. **The absolute constant is existential.**  `lem:transl-cover` states `Θ` "with absolute
   constants" without pinning a value; a single application of `sec:prelim` fact (ii) costs `2`,
   and going through the window may cost two applications.  `Claim` therefore says `∃ C > 0`,
   uniform in `k`, `N`, `q` and both targets.  Pinning `C = 2` would be a strictly stronger
   hypothesis, i.e. the dangerous direction.
2. **The window family is not exhibited.**  `Claim` states the conclusion of the covering
   argument (all targets equivalent) under `KSUM.A1d`'s own window `q₀(k) ≤ q`, rather than
   reproducing `W_even`/`W_odd` and their length bounds.  *(Tier T2, 2026-07-30: the window
   arithmetic IS now mechanized — `KsumAudit.KFloor.window_even_length`, `window_odd_length`,
   `exists_shift_into_window`.  This paragraph's "not attempted" is superseded; what remains
   unmechanized is only `Claim` itself, for the reason in the next box.)*

════════════════════════════════════════════════════════════════════════════════════════════════
  CLAIM DEFECT, AND ITS REPAIR (defect found tier T2 2026-07-30; repaired the same day)
════════════════════════════════════════════════════════════════════════════════════════════════

**Repair applied 2026-07-30** (commissioned after review finding R-A1-3 was applied at the
decision layer): `Claim` is now the coset-covering statement and is PROVED (`holds`), and the
over-strong rendering below is preserved verbatim as `ClaimAllPairs`, which nothing consumes.
The rest of this box is the original diagnosis, kept because it is the reason for the repair.

`ClaimAllPairs` quantifies over **every ordered pair** of targets `(t₀, t)`.  `lem:transl-cover` does not
prove that.  It relates a target only to the other targets **in its own coset** `t + kZ_q`, and
the window family is what guarantees that this coset contains a usable (window) target.  Where
`gcd(k,q) > 1` the cosets are proper subsets of `Z_q` and the manuscript compares nothing across
them.

Three independent derivations of the same defect are now on disk:

* the prose composition pass (`KSUM.A1`'s `composition.rel`, 2026-07-30);
* the concurrent composition-layer review, finding **R-A1-3**
  (`ksum/reviews/ksum_composition_layer_review_20260730.md`), which exhibits `k = 3, q = 3`, where
  `kSum_{Z_3,0,N}` is constant for `N ≥ 7` while `kSum_{Z_3,1,N}` is not, so no constant `C`
  works;
* this tier's own derivation, below.

**Scope caveat on the review's witness, reported rather than resolved (disk is authoritative):**
`q = 3` does **not** satisfy `ClaimAllPairs`'s own range hypothesis `2k²+2k-5 ≤ q`, which at
`k = 3` reads `19 ≤ q`.  So R-A1-3 refutes the *prose* claim ("all `t` via gcd argument") and the
pre-window form, but it does not by itself falsify the all-pairs Lean statement as literally
written.  The Lean-level obstruction proved here is `not_reachable_k3_q21`: at `k = 3, q = 21` —
which **is** inside the range hypothesis — the target `0` lies outside the orbit of the target `1`
under every symmetry this development has (translation by `kZ_q`, and multiplication by a unit,
which is what a per-coordinate affine relabeling does to the target).  Hence `ClaimAllPairs` is
not derivable from the `QueryModel` interface by the manuscript's argument.  Producing a
`QueryModel` that separates the two orbits — which would turn "not derivable" into "false" — was
not attempted, and the repair does not need it: `Claim` no longer asserts the all-pairs form.

**What the repair changed, exactly** (anti-drift, the current formalization synchronization checks): `Claim` gained the coset
membership `s = t + k·a` and the window bounds on `s`, kept the `∃ C > 0` constant in the same
direction (`Q(kSum_s) ≤ C·Q(kSum_t)`, i.e. `Q(kSum_t) ≥ Q(kSum_s)/C`), and exchanged the floor
`q₀(k) = 2k²+2k-5` for the manuscript's own κ-indexed window `(k²-2)κ + 2k-1 ≤ q` — the
hypothesis `lem:transl-cover`(ii) is stated under, and the one `KSUM.A1`'s composition already
establishes for its choice of `κ`.  `2 ≤ κ` plus that window is equivalent to `q ≥ q₀(k)`, so no
modulus in `A1d`'s range is lost.

No `sorry`.
-/
import KSUM.Interface
import KsumAudit.T2KFloor

namespace KSUM.A1c

open KsumAudit

/-- **The translation identity of `lem:transl-cover`, proved.**
`kSum_{G,t,N}(x) = kSum_{G,t+k·a,N}(x + a·1)`: every `k`-subset sum increases by exactly `k·a`
when `a` is added to every coordinate.  Stated for an arbitrary finite abelian group, which
covers `Z_q` at every parity — this is the "no parity cond." of the frozen Claim, and it is the
half of `KSUM.A1c` that this tier does mechanize.

This is the `k ≥ 3` analogue of tier T1's `KsumAudit.twoSum_shift`, and unlike that `k = 2` case
it needs no invertibility of `2`. -/
theorem kSum_translate {G : Type*} [AddCommGroup G] [DecidableEq G] (k N : ℕ) (a t : G)
    (x : Fin N → G) :
    kSum G k (t + k • a) N (fun i => x i + a) = kSum G k t N x := by
  simp only [kSum]
  refine decide_eq_decide.mpr ⟨?_, ?_⟩
  · rintro ⟨S, hcard, hsum⟩
    refine ⟨S, hcard, ?_⟩
    rw [Finset.sum_add_distrib, Finset.sum_const, hcard] at hsum
    exact add_right_cancel hsum
  · rintro ⟨S, hcard, hsum⟩
    refine ⟨S, hcard, ?_⟩
    rw [Finset.sum_add_distrib, Finset.sum_const, hcard, hsum]

/-- **`KSUM.A1c`, formal Claim — the COSET-COVERING form** *(restated 2026-07-30 by the R-A1-3
repair batch; the refuted all-pairs rendering is kept below as `ClaimAllPairs`)*.

There is one absolute constant `C > 0` such that, for every `k ≥ 3`, every length `N`, every claw
alphabet `κ` and modulus `q` inside `lem:transl-cover`(ii)'s window `(k²-2)κ + 2k-1 ≤ q`, and
every target `t`, there are a shift `a` and a **window** target `s ∈ [t₀, t₀+k)` — `t₀`
`= (k-2)(kκ+1)` — such that

* `s` lies in `t`'s own coset: `s = t + k·a` (this is what `lem:transl-cover` proves, and it is
  the clause whose omission produced the refuted all-pairs form), and
* `Q(kSum_{Z_q,s,N}) ≤ C · Q(kSum_{Z_q,t,N})`, i.e. `Q(kSum_t) ≥ Q(kSum_s)/C`.

Read: *the window family plus the translation identity make every target at least as hard as
SOME window target, up to an absolute constant* — which is exactly what lets a bound proved at
the window targets (`KSUM.A1a`, every-window-target form) be lifted to all targets. -/
def Claim (M : QueryModel) : Prop :=
  ∃ C : ℝ, 0 < C ∧
    ∀ (k N q κ : ℕ) [NeZero q], 3 ≤ k → (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q →
      ∀ t : ZMod q, ∃ (a : ZMod q) (s : ℕ),
        KsumAudit.KFloor.baseTarget k κ ≤ s ∧ s < KsumAudit.KFloor.baseTarget k κ + k ∧
          ((s : ℕ) : ZMod q) = t + k • a ∧
          M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) N) ≤ C * M.Q (kSum (ZMod q) k t N)

/-- **The REFUTED rendering, retained under the failure-preservation rule.**  This is the
ALL-PAIRS-of-targets transfer rejected by the linked review.
`lem:transl-cover` does not prove it — the covering argument is coset-local — and it is not
derivable from the `QueryModel` interface, by `not_reachable_k3_q21` below.  It is retained so
that the earlier reading, the reviewer's refutation (R-A1-3) and the machine-checked in-range
obstruction all keep resolving to a statement on disk.  **Nothing in this layer consumes it.** -/
def ClaimAllPairs (M : QueryModel) : Prop :=
  ∃ C : ℝ, 0 < C ∧
    ∀ (k N q : ℕ) [NeZero q], 3 ≤ k → 2 * k ^ 2 + 2 * k - 5 ≤ q →
      ∀ t₀ t : ZMod q, M.Q (kSum (ZMod q) k t₀ N) ≤ C * M.Q (kSum (ZMod q) k t N)

/-! ## The query-complexity half of `lem:transl-cover`, PROVED -/

/-- **`lem:transl-cover`, query half.**  *"`x ↦ x + a·1` is a per-coordinate bijection, so fact
(ii) of `sec:prelim` (applied in both directions) yields the `Θ`."*  Here the single direction
that the manuscript actually uses: shifting the target inside its own coset `t + kZ_q` costs at
most the absolute factor `2`.

This is the whole of the manuscript's target-transfer, with the constant made explicit. -/
theorem Q_kSum_translate_le (M : QueryModel) {q : ℕ} [NeZero q] (k N : ℕ) (t a : ZMod q) :
    M.Q (kSum (ZMod q) k (t + k • a) N) ≤ 2 * M.Q (kSum (ZMod q) k t N) := by
  have h : (kSum (ZMod q) k (t + k • a) N)
      = fun y : (Fin N → ZMod q) =>
          kSum (ZMod q) k t N (fun i => (Equiv.subRight a) (y i)) := by
    funext y
    have hy := kSum_translate k N a t (fun i => y i - a)
    simp only [sub_add_cancel] at hy
    simpa using hy
  rw [h]
  exact M.relabel (Alph := fun _ : Fin N => ZMod q) (Alph' := fun _ : Fin N => ZMod q)
    (fun _ => Equiv.subRight a) (kSum (ZMod q) k t N)

/-- **The faithful covering statement, with the coset witness exposed** — what `lem:transl-cover`
actually delivers, and what the repaired `Claim` says.  Under the manuscript's own modulus
condition `q ≥ (k²-2)K + 2k-1`, every target `t` admits a shift `a` landing it on a window target
`s ∈ [t₀, t₀ + k)` (`t₀ = (k-2)(kK+1)` is `W_odd`'s left endpoint) **inside `t`'s own coset**
`t + kZ_q`, at a cost of the absolute factor `2`.

Note the direction: it produces, for each `t`, SOME window target in `t`'s coset — not a
comparison between two arbitrary targets, which is exactly the strengthening that makes
`ClaimAllPairs` underivable. -/
theorem Q_window_cover_coset (M : QueryModel) {k q : ℕ} [NeZero q] (N κ : ℕ) (hk : 3 ≤ k)
    (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) (t : ZMod q) :
    ∃ (a : ZMod q) (s : ℕ),
      KsumAudit.KFloor.baseTarget k κ ≤ s ∧ s < KsumAudit.KFloor.baseTarget k κ + k ∧
        ((s : ℕ) : ZMod q) = t + k • a ∧
        M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) N) ≤ 2 * M.Q (kSum (ZMod q) k t N) := by
  have hk0 : 0 < k := by omega
  have hlen := KsumAudit.KFloor.window_odd_length (κ := κ) (q := q) hk hwin
  have hfit : KsumAudit.KFloor.baseTarget k κ + k ≤ q := by omega
  have hgcd : Nat.gcd k q ≤ k := Nat.gcd_le_left _ hk0
  obtain ⟨a, s, hs1, hs2, hs3⟩ :=
    KsumAudit.KFloor.exists_shift_into_window (q := q) k (KsumAudit.KFloor.baseTarget k κ) k
      hgcd hfit t
  refine ⟨a, s, hs1, hs2, hs3.symm, ?_⟩
  rw [← hs3]
  exact Q_kSum_translate_le M k N t a

/-- The covering statement in the shape tier T2 stated it (coset witness dropped), kept verbatim
because the T2 report cites this name. -/
theorem Q_window_cover (M : QueryModel) {k q : ℕ} [NeZero q] (N κ : ℕ) (hk : 3 ≤ k)
    (hwin : (k ^ 2 - 2) * κ + 2 * k - 1 ≤ q) (t : ZMod q) :
    ∃ s : ℕ, KsumAudit.KFloor.baseTarget k κ ≤ s ∧ s < KsumAudit.KFloor.baseTarget k κ + k ∧
      M.Q (kSum (ZMod q) k ((s : ℕ) : ZMod q) N) ≤ 2 * M.Q (kSum (ZMod q) k t N) := by
  obtain ⟨_, s, hs1, hs2, _, hQ⟩ := Q_window_cover_coset M N κ hk hwin t
  exact ⟨s, hs1, hs2, hQ⟩

/-- **`KSUM.A1c.Claim` holds, with the explicit constant `C = 2`** — one application of
`sec:prelim` fact (ii), the single direction the manuscript uses.  This is the whole of
`lem:transl-cover`: the translation identity, the window-length computation (ii), and the Bézout
covering step. -/
theorem holds (M : QueryModel) : Claim M := by
  refine ⟨2, by norm_num, ?_⟩
  intro k N q κ _ hk hwin t
  exact Q_window_cover_coset M N κ hk hwin t

/-- **`Claim` under the extra hypothesis `gcd(k,q) = 1`**, with the explicit constant `2`.  When
`k` is invertible mod `q` every pair of targets IS in one coset, so the all-pairs form follows
from the translation identity alone.  `KSUM.A2` is exactly this situation — there `gcd(k,q)=1` is
FORCED by the construction of `q` (`KSUM.A2.coprime_k_q`) — which is why the same over-strong
rendering is harmless on that branch and fatal here. -/
theorem Q_le_of_coprime (M : QueryModel) {q : ℕ} [NeZero q] (k N : ℕ) (h : Nat.Coprime k q)
    (t₀ t : ZMod q) :
    M.Q (kSum (ZMod q) k t₀ N) ≤ 2 * M.Q (kSum (ZMod q) k t N) := by
  obtain ⟨a, ha⟩ : ∃ a : ZMod q, k • a = t₀ - t := by
    refine ⟨((ZMod.unitOfCoprime k h)⁻¹ : (ZMod q)ˣ) * (t₀ - t), ?_⟩
    rw [nsmul_eq_mul, ← mul_assoc]
    have hu : ((k : ℕ) : ZMod q) = ((ZMod.unitOfCoprime k h : (ZMod q)ˣ) : ZMod q) :=
      (ZMod.coe_unitOfCoprime k h).symm
    rw [hu, ← Units.val_mul, mul_inv_cancel, Units.val_one, one_mul]
  have : t + k • a = t₀ := by rw [ha]; ring
  rw [← this]
  exact Q_kSum_translate_le M k N t a

/-! ## The obstruction to `Claim` (see the CLAIM DEFECT box in the header) -/

/-- **The Lean-level obstruction to `Claim`.**  At `k = 3, q = 21` — a modulus *inside* `Claim`'s
own range hypothesis `2k²+2k-5 = 19 ≤ q` — the target `0` is not in the orbit of the target `1`
under the two symmetries the interface supplies: translation by `k·Z_q` and multiplication by a
unit (the effect on the target of a per-coordinate affine relabeling).  Since `3 ∣ 21`, a unit is
never `≡ 0 (mod 3)` while `3a` always is.

So no chain of `lem:transl-cover` steps and `sec:prelim` fact-(ii) relabelings can compare these
two targets, and `Claim`'s all-pairs form is not derivable from the interface. -/
theorem not_reachable_k3_q21 : ∀ u v a : ZMod 21, u * v = 1 → u * 1 + 3 * a ≠ 0 := by decide

/-- Non-vacuity of `not_reachable_k3_q21`'s hypothesis: `q = 21` really does satisfy the range
condition of `Claim` at `k = 3`, so the obstruction is not vacuously about an excluded modulus. -/
theorem k3_q21_in_range : 2 * 3 ^ 2 + 2 * 3 - 5 ≤ 21 := by decide

end KSUM.A1c
