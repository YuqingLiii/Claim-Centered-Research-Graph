# External cross-vendor hostile-referee review (ChatGPT Pro, via lead) — 2026-07-28

Provenance: the decision layer prepared the self-contained review prompt
(`channel-capacity/werner-holevo-gap/notes/WHGAP_EXTERNAL_REVIEW_PROMPT_CHATGPT_20260728.md`);
the LEAD submitted it to ChatGPT Pro on the web and pasted the full reply back verbatim
(archived below the marker). Fourth verification layer: vendor-independent of both the codex
executor/reviewers and the Fable decision-layer audit.

## Verdict summary (as returned)

- Claims 1, 2, 3, 5: **PASS** (Claim 3 with a convention note; Claim 5 with an endpoint remark).
- Claim 4: **PASS within the explicitly stated five-real-parameter ansatz** — heading should be
  softened; complex cross-coefficient Im(r) direction not yet classified.
- **Overall: "PASS — no fatal flaw found."** Establishes Q = P = 0 on [1/2, 1); with the
  reviewer's minimal-environment observation, on the CLOSED interval [1/2, 1].

## Substantive contributions beyond confirmation

1. **Closed-form Choi spectrum:** spec C_x = {0 (×19), 4(1-x)(2x-1)/x (×5),
   16(1-x)(3x-1)/(9x) (×3)} (unnormalized Choi convention). Reproduces our witness
   -102/1225 at x = 49/100 (multiplicity 5) and gives 3/7, 20/21 at x = 4/7.
2. **x = 1 endpoint is a representation artifact:** at x = 1, K_0 = 0; dropping the zero Kraus
   direction gives the minimal 3-dim environment complement Λ_{1,min}^c = (1/2)(Tr X · I - X^T)
   = Λ_1 itself (self-complementary); J = id satisfies the theorem trivially (defect 0). Hence
   Q(Λ_1) = P(Λ_1) = 0 via the SAME mechanism — the theorem extends to [1/2, 1] without RK24.
3. **Claim-4 scope caveat:** adjoint preservation permits a complex cross coefficient r with
   blocks (r a(Y)^T, -conj(r) a(Y)); intertwining sees only Re(r), so the fully general
   covariant adjoint-preserving family has one more real parameter (Im r) than the frozen real
   ansatz. PSD plausibly forces Im r = 0, but that needs an argument. Uniqueness statements must
   stay scoped to the five-real-parameter ansatz (as our R2/R3 licensing already does).
4. Presentation requirements for publication: state the unnormalized Choi convention; soften
   the Claim-4 heading; present x = 1 via the minimal complement; frame the novelty as closing
   the ZERO-CAPACITY gap (the antidegradability threshold is a separate, numerical, statement).

## Decision-layer verification of the reviewer's new mathematics (2026-07-28)

- x = 1 self-complementarity: hand-verified — (Λ_{1,min}^c(X))_{μν} = (1/2)Tr(A_μ X A_ν†)
  = (1/2)(δ_{μν} Tr X - (X^T)_{μν}) = Λ_1(X)_{μν}; J = id adjoint-preserving, intertwining
  exact, defect ≡ 0 CP; Λ_1(1) = 1 ≻ 0 faithful. CONFIRMED.
- Closed-form spectrum + the two forcing vectors (v_p on the A=|0> maximally-entangled BB'
  direction; v_d mixed): machine-verified in
  [fable_audit_ext.log](logs_whgap_fable_audit_20260728/fable_audit_ext.log). CONFIRMED.

Status impact: none applied here (external review is not a rule-6 gate by itself); the findings
flow into the paper draft and the P4 note revision. The [1/2,1] closed-interval strengthening
enters the paper as a theorem with the minimal-complement proof.

---

## Verbatim archived reply (ChatGPT Pro)

[The lead pasted the full hostile-referee report in the session transcript of 2026-07-28; the
mathematical content is summarized above. Key boxed conclusions: characteristic polynomial
det(zI - C_x) = z^19 (z - 4(1-x)(2x-1)/x)^5 (z - 16(1-x)(3x-1)/(9x))^3; forcing quadratic
forms <v_p, C v_p> = -((1-x)/x)(3p-1)^2 and <v_d, C v_d> = -(1/x)(3d-2(1-x))^2 with
d = 2βq; final verdict "PASS — no fatal flaw found."]

