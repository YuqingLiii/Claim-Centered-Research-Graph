/-
`KSUM/SelfTest.lean` — decidable checks that the definitions reproduce independently known exact
values.

WHY THIS FILE EXISTS, and what it guards that nothing else does.

Every theorem in this layer is a statement ABOUT `kSum`, `twoSum`, `Claw`, `encode`, `Coll`,
`frozen`.  If one of those definitions were the wrong object — an off-by-one in `blockPos`, a
`Claw` that compared the wrong halves, a `frozen` that froze the first coordinates instead of the
last — then every theorem would still typecheck, every witness `example` would still elaborate,
and every gate would still pass, while the whole development would be about a different problem.
Witness examples cannot catch this: they are existence proofs, and a wrong definition has
witnesses too.

The checks below are `decide`d, i.e. the kernel evaluates the definitions on concrete inputs and
compares against values computed by hand from the manuscript's own descriptions.  **Every
definition gets at least one POSITIVE and one NEGATIVE case**, because a definition that is
constantly `true` passes any number of positive checks.

No `sorry`, no `native_decide` (a `native_decide` would move these checks outside the kernel and
defeat their purpose).
-/
import KSUM.A2
import KSUM.Support.Freeze

namespace KSUM.SelfTest

open KsumAudit KSUM.Support

/-! ## `twoSum` — a hit is a pair of DISTINCT positions summing to the target -/

/-- Positive: `1 + 4 = 0` in `Z_5`. -/
example : twoSum (ZMod 5) 0 4 ![1, 4, 2, 2] = true := by decide

/-- Negative: the pair sums of `(1,1,2,2)` are `2, 3, 4` — never `0`. -/
example : twoSum (ZMod 5) 0 4 ![1, 1, 2, 2] = false := by decide

/-- Negative, the failure mode "a single coordinate is allowed to be used twice":
`x = (3, 1, 1, 1)` has `3 + 3 = 1` but no two DISTINCT positions summing to `1`
(`3+1 = 4`, `1+1 = 2`). -/
example : twoSum (ZMod 5) 1 4 ![3, 1, 1, 1] = false := by decide

/-! ## `kSum` — the `k`-subset version -/

/-- Positive: `1 + 2 + 4 = 7 ≡ 0` in `Z_7`. -/
example : kSum (ZMod 7) 3 0 4 ![1, 2, 4, 3] = true := by decide

/-- Negative: `1 + 1 + 1 = 3 ≠ 0` in `Z_7`, and there is no other `3`-subset. -/
example : kSum (ZMod 7) 3 0 3 ![1, 1, 1] = false := by decide

/-- Negative, the failure mode "subsets of the wrong size count": at `k = 3` the pair
`3 + 4 = 0` must NOT make `x = (3,4,1,1)` a hit at target `0`
(`3+4+1 = 1`, `3+1+1 = 5`, `4+1+1 = 6`). -/
example : kSum (ZMod 7) 3 0 4 ![3, 4, 1, 1] = false := by decide

/-! ## `Claw` — `f(i) = g(j)` ACROSS the two halves, not within one half -/

/-- Positive: `f = (0,1)`, `g = (2,0)` share the value `0`. -/
example : Claw 2 3 ![0, 1, 2, 0] = true := by decide

/-- Negative: `f = (0,1)`, `g = (2,2)` share nothing. -/
example : Claw 2 3 ![0, 1, 2, 2] = false := by decide

/-- Negative, the failure mode "a repeat INSIDE one half counts": `f = (2,2)`, `g = (0,1)` has a
repeat in the first half and none across, so it must be `false`. -/
example : Claw 2 3 ![2, 2, 0, 1] = false := by decide

/-! ## `cyc` and `encode` — first half `s`, second half `-s` -/

/-- The value set of `lem:encode` at `q = 5`, `κ = 2` is `{1,2}` on the first half. -/
example : (cyc 5 2 0 = (1 : ZMod 5)) ∧ (cyc 5 2 1 = (2 : ZMod 5)) := by decide

/-- The second half carries `-s`, i.e. `{q-κ,…,q-1} = {3,4}` at `q = 5`, `κ = 2`.
Here `y = (0,1)`: position `0` is in the first half and carries `s 0 = 1`; position `1` is in the
second half and carries `-(s 1) = -2 = 3`. -/
example : encode 1 (cyc 5 2) ![0, 1] 0 = (1 : ZMod 5) := by decide

example : encode 1 (cyc 5 2) ![0, 1] 1 = (3 : ZMod 5) := by decide

/-- Negative: the encoding is NOT `s` on both halves — `encode` at position `1` is `-s 1 = 3`,
not `s 1 = 2`. -/
example : ¬ (encode 1 (cyc 5 2) ![0, 1] 1 = (2 : ZMod 5)) := by decide

/-! ## `lem:encode` itself, exhaustively at `(n, κ, q) = (1, 2, 5)`

This is the load-bearing identity of the whole development, checked by the kernel on ALL `2^2`
live words rather than on a witness. -/
example : ∀ y : Fin (2 * 1) → Fin 2,
    twoSum (ZMod 5) 0 (2 * 1) (encode 1 (cyc 5 2) y) = Claw 1 2 y := by decide

/-- Negative control for the same identity: at `q = 4 < 2κ+1 = 5` it FAILS, so the hypothesis
`2κ+1 ≤ q` of `KSUM.A1b.Claim` is load-bearing and not decoration.  The failure needs `n ≥ 2`,
because it is a WITHIN-half pair that goes wrong: at `q = 4`, `f = (1,1)` encodes to `(2,2)` and
`2 + 2 = 0`, a spurious hit with no claw.  (At `n = 1` there is only the cross pair, and the
identity survives — which is itself worth recording, since it shows the hypothesis is about the
within-half cases exactly as `lem:encode`'s case analysis says.) -/
example : ¬ (∀ y : Fin (2 * 2) → Fin 2,
    twoSum (ZMod 4) 0 (2 * 2) (encode 2 (cyc 4 2) y) = Claw 2 2 y) := by decide

/-- The `n = 1` remark above, checked. -/
example : ∀ y : Fin (2 * 1) → Fin 2,
    twoSum (ZMod 4) 0 (2 * 1) (encode 1 (cyc 4 2) y) = Claw 1 2 y := by decide

/-! ## `blockPos` and `Coll` — one position per block, all values equal -/

/-- Block `0` occupies positions `0,1` and block `1` occupies positions `2,3` when `k = n = 2`. -/
example : (blockPos 2 2 0 0 = (0 : Fin 4)) ∧ (blockPos 2 2 0 1 = (1 : Fin 4)) ∧
    (blockPos 2 2 1 0 = (2 : Fin 4)) ∧ (blockPos 2 2 1 1 = (3 : Fin 4)) := by decide

/-- Positive: value `1` occurs in block `0` (at offset `1`) and in block `1` (at offset `0`). -/
example : Coll 2 2 3 ![0, 1, 1, 2] = true := by decide

/-- Negative: block `0` carries only `0`, block `1` only `1`. -/
example : Coll 2 2 3 ![0, 0, 1, 1] = false := by decide

/-- Negative, the failure mode "a repeat INSIDE one block counts": `(1,1,0,2)` repeats `1` in
block `0` but shares nothing with block `1`. -/
example : Coll 2 2 3 ![1, 1, 0, 2] = false := by decide

/-! ## `frozen` — the LAST `m` coordinates are the frozen core -/

/-- Positive: freezing the last coordinate to `4`, the live word `(1,2)` gives the assembled
string `(1,2,4)` with `1+2+4 = 7 ≡ 0` in `Z_7`. -/
example : frozen 1 (kSum (ZMod 7) 3 0 (2 + 1)) ![4] ![1, 2] = true := by decide

/-- Negative: the live word `(1,1)` gives `(1,1,4)` with `1+1+4 = 6 ≠ 0`. -/
example : frozen 1 (kSum (ZMod 7) 3 0 (2 + 1)) ![4] ![1, 1] = false := by decide

/-- Negative: with core `(3)` the assembled string is `(1,2,3)`, summing to `6 ≠ 0`. -/
example : frozen 1 (kSum (ZMod 7) 3 0 (2 + 1)) ![3] ![1, 2] = false := by decide

/-! The failure mode "the core was PREPENDED instead of appended" cannot be caught by any
`kSum`-valued test, because `kSum` is invariant under permuting positions.  These three checks
use a position-sensitive function instead, and pin the order exactly: live block first, core
last. -/

example : frozen 1 (fun x : Fin (2 + 1) → ZMod 7 => decide (x 0 = 1)) ![4] ![1, 2] = true := by
  decide

example : frozen 1 (fun x : Fin (2 + 1) → ZMod 7 => decide (x 2 = 4)) ![4] ![1, 2] = true := by
  decide

/-- Negative: position `0` carries the live value `1`, NOT the core value `4`. -/
example : frozen 1 (fun x : Fin (2 + 1) → ZMod 7 => decide (x 0 = 4)) ![4] ![1, 2] = false := by
  decide

/-- `frozen` really is "evaluate on live-block-followed-by-core" (`frozen_eq_append`), checked by
the kernel on a concrete instance so the recursion is not merely believed. -/
example : frozen 1 (kSum (ZMod 7) 3 0 (2 + 1)) ![4] ![1, 2]
    = kSum (ZMod 7) 3 0 (2 + 1) (Fin.append ![1, 2] ![4]) := by decide

/-- And the assembled string is in the expected order: live first, core last. -/
example : (Fin.append ![1, 2] ![4] : Fin (2 + 1) → ZMod 7) = ![1, 2, 4] := by decide

/-! ## The `lem:embed-allt` arithmetic of `KSUM.A2.coprime_k_q`

The theorem is proved from `k ∣ P` and `2(M+1) = (2k+1)^{k-1}+1`.  These checks confirm that
those two facts hold for the manuscript's own values, and that the conclusion is the expected
one — i.e. that the theorem is about the right numbers. -/

/-- `k = 3`: `M+1 = (7² + 1)/2 = 25`, so `M = 24`; with `P = 24` (a multiple of `3`) the modulus
is `q = 25 · 25 = 625`, and `gcd(3, 625) = 1`. -/
example : 2 * (24 + 1) = (2 * 3 + 1) ^ (3 - 1) + 1 := by decide

example : Nat.gcd 3 ((24 + 1) * (24 + 1)) = 1 := by decide

/-- `k = 4`: `M+1 = (9³ + 1)/2 = 365`, so `M = 364`; with `P = 8` (a multiple of `4`) the modulus
is `q = 9 · 365 = 3285`, and `gcd(4, 3285) = 1`.  Note `2 ∣ k` here, which is the case the
manuscript handles separately (`2k+1 ≡ 1 mod 4`). -/
example : 2 * (364 + 1) = (2 * 4 + 1) ^ (4 - 1) + 1 := by decide

example : Nat.gcd 4 ((8 + 1) * (364 + 1)) = 1 := by decide

/-- Negative control for the coprimality theorem's hypotheses: **dropping `k ∣ P` breaks it.**
With `k = 3` and `P = 25` (not a multiple of `3`), `P + 1 = 26`… still coprime to 3; the sharp
failure is at `P = 2`, where `P+1 = 3` and `gcd(3, 3·25) = 3 ≠ 1`.  So `k ∣ P` is load-bearing
and not decoration. -/
example : Nat.gcd 3 ((2 + 1) * (24 + 1)) = 3 := by decide

end KSUM.SelfTest
