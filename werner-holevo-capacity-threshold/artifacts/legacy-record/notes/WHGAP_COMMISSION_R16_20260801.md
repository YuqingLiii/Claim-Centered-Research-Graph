# WHGAP commission R16 — rule-7 review of the P15-B package (frozen 2026-08-01)

Commissioner: decision layer. Reviewed work: P15-B (death-point localization +
tensorization probe), executed 2026-08-01 under Track P15B of
[WHGAP_COMMISSION_LEAN5_P15B_20260801.md](WHGAP_COMMISSION_LEAN5_P15B_20260801.md).

NODE_ID = `WHGAP.pure-anchor-order`. ROLE = reviewer — fresh instance: you did NOT author
P15-B and you are given NO desired outcome; both LICENSE and FINDINGS are acceptable
results.

Pre-task reload FIRST: `research/PRETASK_RELOAD_PROMPT.md` with
{PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID}, ROLE as above.

Scope: report `artifacts/whgap_r16_review_20260801.md` + `tools/whgap_r16_*.py` + logs
prefixed `r16_` added into `artifacts/logs_whgap_p15b_20260801/` (additive only; never
overwrite executor artifacts). NO node/index/DAG markdown edits (decision layer applies
your verdict). No git commit/push.

## Frozen inputs (read from disk)

- The package: `channel-capacity/werner-holevo-gap/notes/WHGAP_P15B_DEATHPOINT_20260801.md`,
  `artifacts/logs_whgap_p15b_20260801/`, `tools/whgap_p15b_*.py`.
- Baseline definitions: `notes/WHGAP_P15A_STRICTNESS_20260730.md` (P_b2, G(ψ,σ));
  R9's corrected state `artifacts/whgap_r9_review_20260801.md`.

## Review items (rule-7 embedded set is MANDATORY: type audit; c ≥ 2 independent gates on
## every load-bearing identity; anchoring ban; frozen-input scopes; standing failure-mode
## list; value-vs-formula statements)

1. **The quadratic-form reduction (load-bearing for EVERYTHING downstream):** re-derive,
   by your OWN route and WITHOUT reading `tools/whgap_p15b_core.py` first (7c anchoring
   ban), the claim that for pure anchors G(ψ,σ) = ⟨ψ|W(σ)|ψ⟩ with min over all pure ψ =
   λ_min(W(σ)). Type-audit W(σ) (definition, Hermiticity, the pure-input isospectrality
   step it rests on). If this reduction is wrong or scope-limited, everything in Phases
   1–2 inherits the defect — say so precisely.
2. **The stratum formula and the root:** independently derive the orthocomplement-stratum
   value G*(x) = (1−2x)ln x + x ln(2−x) − (1−x)ln(1−x) − (1−x)ln 2 from the definitions
   (symbolic route AND ≥ 50-dps numeric route = the c ≥ 2 gate), and re-solve the root
   x_d with your own code. Verify the note claims x_d as EXACT only on-stratum and as
   CANDIDATE globally (5-point numerical global-optimality check — audit that wording).
3. **Bracket endpoints:** with your OWN optimizer, (a) re-find a violation at
   x = 687/1600 and sharpen to ≥ 40 dps; (b) rerun the null at x = 43/100 with your own
   restart protocol and state your power reasoning. Audit the executor's detection-power
   argument (hit rates → N = 200 → P(miss)); flag any spot where the claimed power
   outruns the instrument.
4. **Certificates hygiene:** spot-check ≥ 3 of the 7 violation certificates (recompute G
   at the recorded pairs, 40+ dps); check the support/rank status of each checked
   certificate (interior full-rank claims at 41/100 and 17/40 — verify; the standing
   exact-zero-mode trap applies near boundaries).
5. **Tensorization structure:** verify W₂(σ₁⊗σ₂) = W(σ₁)⊗1 + 1⊗W(σ₂) symbolically by
   your own route, and its stated consequence (product-σ 2-copy P_b2 ⟺ 1-copy). Verify
   the 2-copy calibration at x = 41/100 and the superadditivity claim
   (min G₂ = −0.13639… < 2·min G₁ = −0.13606…) with your own 2-copy code at that point.
6. **Null-scope honesty:** the 2-copy bounded null (80/32 restarts, 162 real dims) must
   be presented as exactly that; the note's own flag that the rank-2-boundary search (F2)
   was not run must survive into any summary sentence. Over-claim and under-claim both
   reportable.
7. **No-Q-consequence audit (R8 MAJOR-3):** confirm no sentence in the note or logs
   derives a Q-statement from P_b2 data.
8. **Value-vs-formula:** for every headline number (x_d, bracket endpoints, certificate
   G values, superadditive gap) state whether it is a computed VALUE or an evaluated
   FORMULA, and that the two agree where both exist.

## Licensing menu

- **(A)** "P15-B is licensed as recorded: the bracket, the exact-form candidate (as
  candidate), and the tensorization bounded null stand at NUMERICAL with accurate
  scope wording." (You may add itemized upgrades, e.g. the stratum formula as a
  reviewer-verified identity.)
- **(B)** FINDINGS — itemized MAJORs (wrong/unsupported claims) and minors.

Budget ≤ 90 min. Closeout: your own SHA entries for r16_ logs appended to a separate
`SHA256SUMS_r16.txt` (LF convention header); `proof_dag_check` + `literature_check` exit 0
(you touch no node files). Return `{verdict, summary, majors, minors, report_path}`.

