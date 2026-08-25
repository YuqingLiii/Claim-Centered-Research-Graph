/-
`KSUM/A1d.lean` — linked node module.

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : KSUM.A1d                        (alias `A1d`)
node file      : ksum/proof-dag/nodes/KSUM.A1d.yaml
decomposition / role    : none / proof
epistemic status (read from the node file on 2026-07-30): **PROVED**
                 (assessment source: current node record; statement correction independently reviewed
                 2026-07-19)
mechanization  : **stated** — `Claim` is the CONCLUSION of `KSUM.A1`'s composition theorem, and
                 is proved there RELATIVE to `KSUM.A1a`, `KSUM.A1b`, `KSUM.A1c` and the
                 `QueryModel` interface.  No unconditional `holds` exists and none is claimed.
claim_hash     : sha256:5306ca606f3668dab95889262983b0af1443926ca67009b7c82d5509d2d27606
                 (byte convention: see `KSUM/A1a.lean`)

current_claim_hash: sha256:d9f22fb14b5783c6250635c63c8b446222ec69911d051d3f55ed6e8e0b382af1

CURRENT CANONICAL CLAIM (verbatim from the node record):

  For every fixed k>=3 there are constants C_k,c_k>0 such that, for all sufficiently large N, every target t, and q0(k)=2k^2+2k-5<=q<=C_k N, Q(k-Sum,Z_q,t,N)=Omega_k(sqrt(N)q^(1/6)); for q>=c_k N the same reduction gives Omega_k(N^(2/3)).

END CURRENT CANONICAL CLAIM

FROZEN CLAIM (verbatim from `claim.statement` in the node file):

  For every fixed k≥3 there are constants C_k,c_k>0 such that, for all sufficiently large N,
  every target t, and q0(k):=2k²+2k−5≤q≤C_kN,
  Q(k-Sum,Z_q,t,N)=Ω_k(√N·q^{1/6}); for q≥c_kN the same reduction gives
  Ω_k(N^{2/3}).
  [Statement correction independently reviewed 2026-07-19; PROVED-BY-REDUCTION status unchanged]

Manuscript: `thm:kfloor`, `ksum/paper/ksum_small_alphabet.tex`, `sec:k3`.

════════════════════════════════════════════════════════════════════════════════════════════════
  PROSE ↔ `Claim` DIFF — this is the CONCLUSION, so every difference must be checked in the
  strengthening direction, not the weakening one
════════════════════════════════════════════════════════════════════════════════════════════════

* The two `Ω_k` are rendered in **explicit-constant form** (T1 house rule 3): `∃ A > 0` and
  `∃ B > 0`, existentially quantified per `k` exactly where the prose writes `Ω_k`, with `A`, `B`
  independent of `N`, `q` and `t`.  This is stronger than the asymptotic form and removes the
  two-parameter (`N`, `q`) ambiguity.
* "for all sufficiently large `N`" is `∃ N₀, ∀ N ≥ N₀`, with `N₀` allowed to depend on `k` only.
* The window is `q₀(k) ≤ q ≤ C_k·N` with `q₀(k) = 2k²+2k-5` **as an inequality over `ℕ` for the
  floor and over `ℝ` for the ceiling**, matching the prose (`C_k` is a positive real).
* The plateau clause "for `q ≥ c_k N` the same reduction gives `Ω_k(N^{2/3})`" is rendered as a
  SECOND conclusion under the SAME quantifiers, guarded by `c_k·N ≤ q`; "the same reduction"
  is honoured by `KSUM.A1`'s composition, which derives both from one chain.
* No `Θ_c`-style hidden constant: `A` and `B` are the only constants and both are exhibited by
  the composition proof.

No `sorry`.
-/
import KSUM.Interface
import KSUM.A1

namespace KSUM.A1d

open KsumAudit

/-- **`KSUM.A1d`, formal Claim** — the `k ≥ 3` floor of `thm:kfloor`, in explicit-constant form.

For every fixed `k ≥ 3` there are `C_k, c_k > 0` and constants `A, B > 0` and a threshold `N₀`
such that for all `N ≥ N₀`, every modulus `q` with `2k²+2k-5 ≤ q` and `q ≤ C_k·N`, and every
target `t`:

* `A · √N · q^{1/6} ≤ Q(kSum_{Z_q,t,N})`, and
* if moreover `c_k·N ≤ q`, then `B · N^{2/3} ≤ Q(kSum_{Z_q,t,N})`. -/
def Claim (M : QueryModel) : Prop :=
  ∀ k : ℕ, 3 ≤ k →
    ∃ Ck ck A B : ℝ, 0 < Ck ∧ 0 < ck ∧ 0 < A ∧ 0 < B ∧ ∃ N₀ : ℕ,
      ∀ (N q : ℕ) [NeZero q], N₀ ≤ N → 2 * k ^ 2 + 2 * k - 5 ≤ q → (q : ℝ) ≤ Ck * N →
        ∀ t : ZMod q,
          A * Real.sqrt N * (q : ℝ) ^ (1 / 6 : ℝ) ≤ M.Q (kSum (ZMod q) k t N) ∧
            (ck * N ≤ (q : ℝ) → B * (N : ℝ) ^ (2 / 3 : ℝ) ≤ M.Q (kSum (ZMod q) k t N))

end KSUM.A1d
