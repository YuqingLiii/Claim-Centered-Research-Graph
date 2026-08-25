/-
`SE/goal.lean` — linked node module.
The root: an explicit optimal negative-weight adversary witness for Set Equality at `q = 2n`.
The route theorem here is the Lean mirror of the paper's **Theorem B** (`thm:main`, eq:main).

────────────────────────────────────────────────────────────────────────────────────────────────
node id        : SE.goal      (alias `GOAL`)
node file      : se/proof-dag/nodes/SE.goal.yaml
decomposition / role    : OR / proof
children       : br, ros, mdh, sdp, jz (five)
epistemic status (read from the node file on 2026-07-30): **OPEN / UNSUPPORTED**
route status on the node: `SE.br` route **PROVED** (relative to the cited adversary interface);
                 `ros` REFUTED/DEAD; `mdh`/`sdp`/`jz` OPEN with `proof: null`
mechanization  : composition-checked (br route only), relative to Cited + br.Claim
claim_hash     : sha256:9ac39ac1e9de6e5ab45b32375be0dcf7f559271b16266c3318949d9aaec1a0b5
                 (SHA-256 of the frozen Claim text quoted below, UTF-8, LF, stripped)

FROZEN CLAIM (verbatim from `claim` in the node record):

  SE.goal — explicit optimal neg-weight adversary witness for SE at q=2n
  Adv± >= ||Gamma_n||/max_i||Gamma_n o Delta_i|| = Omega(n^1/3); Theta(n^1/3) known (Zhandry), witness missing

  (Indentation added only to nest the quote inside this comment; the hash above is of the
  UNINDENTED node text.)

────────────────────────────────────────────────────────────────────────────────────────────────
WHAT `Claim` BELOW RENDERS.  The frozen `Ω(n^{1/3})` is rendered quantitatively as the paper's
Theorem B (eq:main): an explicit `ε_n → 0` with

  `Adv(SE(n,2n)) ≥ (C − ε_n)·n^{1/3}`   for every `n ≥ 27`,

`C = 9/(18+4√6+3√10) = 0.2413852814754581733…` (19 digits certified, `SE.Cconst_digits`).
The "explicit witness" part of the frozen Claim — that the bound is achieved by the CONSTRUCTED
matrix `Γ_n` — is carried by the abstract carrier (`F.gammaNorm`/`F.maskNorm` stand for the
constructed witness of `SE.br.def`) and cannot be strengthened at tier 1.

────────────────────────────────────────────────────────────────────────────────────────────────
ROUTE DECLARATION (coordinator ruling R5, 2026-07-30).  §7.4 asks for one `composition_via_*`
per status-propagating child; only ONE exists here, and the omission of the other four is
deliberate and visible:

  * `composition_via_br` — RENDERED below, mirroring the node's prose route proof:
    step 1 (admissibility) is by construction in the carrier; step 2 is the cited
    Høyer–Lee–Špalek interface `Cited.adv_ge`.  "Every status obtained through this route is
    exactly as strong as that citation and not one notch stronger."
  * `composition_via_ros` — NOT rendered: `SE.ros` is REFUTED/DEAD (`proof: null` on the node);
    a refuted child kills its route, not the decomposed claim.  There is no prose route proof to mirror.
  * `composition_via_mdh` — NOT rendered: `SE.mdh` is OPEN with `proof: null` — no prose route
    proof exists on disk; rendering one would invent content.
  * `composition_via_sdp` — NOT rendered: `SE.sdp` is OPEN with `proof: null` — same reason.
  * `composition_via_jz`  — NOT rendered: `SE.jz` is OPEN with `proof: null`, and the node
    records the UNPROVED multiplicative → `Adv±` transfer; as registered the route would resolve
    a VARIANT of the goal, not the goal.

The four unrendered routes carry NO stub theorem.  Since 2026-08-17 each is declared route by
route, with the reason above, in the node's `formalization.lean.rel`
(`route-not-formalized: SE.ros/SE.mdh/SE.sdp/SE.jz`), together with the five premises of those
routes (`premise-not-imported:`); none of those premise nodes carries a `formalization` block, so
no module exists for this one to import.  The deviation from §7.6 check 5 is declared here, in
`SE/Trust.lean` §D6/§D8, and in that `lean.rel` field, which `tools/lean_dag_check.py` now reads:
declared -> INFO, UNDECLARED -> still FAIL.

No `sorry`.  A green build says the ROUTE is machine-checked; the node file itself warns: "the
route is PROVED while `SE.br` itself is OPEN — a green route proves nothing about the goal until
its input closes."
-/
import SE.br

open Filter Topology

namespace SE.goal

section
variable (F : SE.SEFrame)

/-- The node's Lean claim — **Theorem B** (paper `thm:main`, eq:main), quantitative form:
there is an explicit `ε_n → 0` (namely `SE.epsB`) with
`Adv(SE(n,2n)) ≥ (C − ε_n)·n^{1/3}` for every `n ≥ 27`, `C = 9/(18+4√6+3√10)`. -/
def Claim : Prop :=
  Tendsto (SE.epsB SE.rhoConst) atTop (𝓝 0) ∧
    ∀ n : ℕ, 27 ≤ n →
      (SE.Cconst - SE.epsB SE.rhoConst n) * (n : ℝ) ^ ((1 : ℝ) / 3) ≤ F.adv n

end

section
variable {F : SE.SEFrame}

/-- **`Adv ≥ K/(2·envBound)`** — the quantitative core of the route: the `br` ratio bound
composed with the cited adversary interface `Cited.adv_ge` (Høyer–Lee–Špalek; only the `≥` half
is used) and the cited positive denominator. -/
theorem adv_quantitative (hC : F.Cited) (hbr : br.Claim F) {n : ℕ} (hn : 27 ≤ n) :
    (SE.K n : ℝ) / (2 * SE.envBound SE.rhoConst n) ≤ F.adv n := by
  have hmpos : 0 < F.maskNorm n := hC.maskNorm_pos n (by omega)
  exact le_trans (hbr n hn) (hC.adv_ge n hmpos)

/-- **The `br` route theorem** (§7.4, GOAL node: one `composition_via_*` per rendered route):
Cited ∧ br ⟹ `Claim` — i.e. **Theorem B, conditionally**.

**What this does NOT say.**  Through its `hbr` input this theorem is conditional on Conjecture H:
H1 (`SE.denom.Phi.legal.trace.t6`) and H4 (`SE.denom.Phi.legal.sect`) are **OPEN**, and H2/H3
(`SE.denom.Phi.legal.gram.interface`, `SE.denom.Phi.legal.omega.interface`) are **CONJECTURED**
on disk as of 2026-07-30, and they enter only in their tier-1 norm shadows (see the four
hypothesis node modules).  `hC` is a bundle of cited results, not of results proved here.
A green build says the DERIVATION is machine-checked; it says nothing about the hypotheses. -/
theorem composition_via_br (hC : F.Cited) (hbr : br.Claim F) : Claim F := by
  constructor
  · -- `ε_n → 0`
    have hden : Tendsto (fun n : ℕ => 2 * SE.envBound SE.rhoConst n) atTop
        (𝓝 (2 * (1 + Mconst))) :=
      (tendsto_envBound SE.rhoConst).const_mul 2
    have hnum : Tendsto (fun n : ℕ => 1 - 1 / (n : ℝ) ^ ((1 : ℝ) / 3)) atTop (𝓝 (1 - 0)) :=
      tendsto_const_nhds.sub (tendsto_one_div_rpow (by norm_num))
    have hMpos : (0 : ℝ) < Mconst := Mconst_pos
    have hne : (2 * (1 + Mconst)) ≠ 0 := ne_of_gt (by linarith)
    have hq : Tendsto (fun n : ℕ => (1 - 1 / (n : ℝ) ^ ((1 : ℝ) / 3))
        / (2 * SE.envBound SE.rhoConst n)) atTop (𝓝 ((1 - 0) / (2 * (1 + Mconst)))) :=
      hnum.div hden hne
    have hval : Cconst - (1 - (0 : ℝ)) / (2 * (1 + Mconst)) = 0 := by
      rw [sub_zero, ← inv_two_one_add_Mconst]
      norm_num
    have h0 : Tendsto (fun n : ℕ => Cconst - (1 - 1 / (n : ℝ) ^ ((1 : ℝ) / 3))
        / (2 * SE.envBound SE.rhoConst n))
        atTop (𝓝 (Cconst - (1 - 0) / (2 * (1 + Mconst)))) := tendsto_const_nhds.sub hq
    rw [hval] at h0
    exact h0.congr fun n => rfl
  · intro n hn
    have hE : 0 < SE.envBound SE.rhoConst n := envBound_pos SE.rhoConst_nonneg hn
    have hE2 : (0 : ℝ) < 2 * SE.envBound SE.rhoConst n := by linarith
    have hnpos : (0 : ℝ) < (n : ℝ) := by
      have : 0 < n := by omega
      exact_mod_cast this
    have hx : (0 : ℝ) < (n : ℝ) ^ ((1 : ℝ) / 3) := by positivity
    have hsimp : (Cconst - epsB SE.rhoConst n) * (n : ℝ) ^ ((1 : ℝ) / 3)
        = ((n : ℝ) ^ ((1 : ℝ) / 3) - 1) / (2 * SE.envBound SE.rhoConst n) := by
      unfold epsB
      field_simp
      ring
    rw [hsimp]
    refine le_trans ?_ (adv_quantitative hC hbr hn)
    rw [div_le_div_iff₀ hE2 hE2]
    nlinarith [rpow_sub_one_le_K n, hE2]

end

end SE.goal
