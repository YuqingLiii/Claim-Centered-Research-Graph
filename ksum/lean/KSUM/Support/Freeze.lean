/-
`KSUM/Support/Freeze.lean` — support shared by the nodes listed below.

Nodes served: `KSUM.A1a` (its frozen Claim is stated in terms of `frozen`) and `KSUM.A1` (its
composition theorem consumes `Q_frozen_le`).

CONTENT.  `frozen m f c` is `f` with its LAST `m` coordinates fixed to the values `c`, leaving
the first `nlive` coordinates live.  This is the "freeze `k-2` coordinates" operation of
`sec:k3`'s frozen-core construction, item (a).

`Q_frozen_le` is the ONLY place where the interface field `QueryModel.freeze` is used in this
layer.  That field is `sec:prelim` facts **(i) + (iii)** composed at the last position: restrict
to the product subdomain whose last factor is a singleton (fact (i)), then delete that
now-singleton coordinate (fact (iii), *singleton-coordinate deletion*).
**Explicitly recorded after external review.**  It was **finding F1** of the 2026-07-30 T1 audit: the manuscript
then stated no coordinate-freezing principle, and fact (i) as printed did not cover it because
freezing changes the input LENGTH.  Independently, the 2026-07-30 prose composition pass found
the same missing premise for `KSUM.A1` and recorded it in that node's `composition.rel`.  Two
independent routes to the same missing hypothesis — and the reviewed manuscript supplies it: the 2026-07-31
manuscript-repair batch (item M-1) added fact (iii) with the explicit "this is *not* an instance
of (i)" note, so F1 is DISCHARGED.  The dependence is still carried visibly, in the type of every
theorem that uses it, and never hidden.

No `sorry`.
-/
import KSUM.Interface

namespace KSUM.Support

open KsumAudit

/-- `frozen m f c` fixes the last `m` coordinates of `f` to the values `c`.
Defined by iterated `Fin.snoc` so that it matches `QueryModel.freeze` step by step;
`frozen_eq_append` identifies it with the readable `Fin.append` form. -/
def frozen {G : Type} {nlive : ℕ} :
    (m : ℕ) → ((Fin (nlive + m) → G) → Bool) → (Fin m → G) → ((Fin nlive → G) → Bool)
  | 0, f, _ => f
  | m + 1, f, c => frozen m (fun z => f (Fin.snoc z (c (Fin.last m)))) (fun i => c i.castSucc)

/-- Appending an empty tuple changes nothing. -/
theorem append_nil {G : Type} {nlive : ℕ} (z : Fin nlive → G) (c : Fin 0 → G) :
    Fin.append z c = z := by
  funext p
  exact Fin.append_left z c p

/-- `frozen` is "evaluate `f` on the live block followed by the frozen core".
This is the readable characterization; the `Fin.snoc` recursion above is only an implementation
detail chosen to match the shape of `QueryModel.freeze`. -/
theorem frozen_eq_append {G : Type} {nlive : ℕ} :
    ∀ (m : ℕ) (f : (Fin (nlive + m) → G) → Bool) (c : Fin m → G) (z : Fin nlive → G),
      frozen m f c z = f (Fin.append z c)
  | 0, f, c, z => by rw [frozen, append_nil]
  | m + 1, f, c, z => by
      rw [frozen, frozen_eq_append m _ _ z]
      congr 1
      have h := Fin.append_snoc z (Fin.init c) (c (Fin.last m))
      rw [Fin.snoc_init_self] at h
      exact h.symm

/-- **Freezing a core of `m` coordinates does not increase `Q`.**
`m`-fold iteration of the interface field `QueryModel.freeze` (finding F1).
The dependence on that field is visible in the statement through `M : QueryModel`. -/
theorem Q_frozen_le (M : QueryModel) {G : Type} [Fintype G] {nlive : ℕ} :
    ∀ (m : ℕ) (f : (Fin (nlive + m) → G) → Bool) (c : Fin m → G),
      M.Q (frozen m f c) ≤ M.Q f
  | 0, _, _ => le_refl _
  | m + 1, f, c =>
      le_trans (Q_frozen_le M m _ _)
        (M.freeze (Alph := fun _ : Fin (nlive + m + 1) => G) (c (Fin.last m)) f)

end KSUM.Support
