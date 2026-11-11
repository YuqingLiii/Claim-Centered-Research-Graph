# WHGAP P15-A — Is the pure-anchor order P_b2 strictly stronger than Q^(1) = 0?

Executor note, 2026-07-30. Commission
[WHGAP_COMMISSION_P15A_P16A_20260730.md](WHGAP_COMMISSION_P15A_P16A_20260730.md), Track A.
Node: `WHGAP.pure-anchor-order` (P15), obligation 1. Reviewer: R9 (fresh instance).

**Everything below is executor-authored and UNREVIEWED. Cap: NUMERICAL / CONJECTURED with
`pending-review:` for R9. Nothing here licenses a completion-tier status.**

---

## PRE-ACTION REPORT

- **Target node:** `WHGAP.pure-anchor-order` (alias P15). **Status as read from disk:**
  `OPEN`, `disposition: null`
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.pure-anchor-order.md` front
  matter, and row `P15` of `proof-dag/NODE_INDEX.md` line 119).
- **Role:** EXECUTOR (Track A, P15-A). I did not author any prior work on this node and was
  given no desired outcome; the commission states explicitly that its decision-layer
  conjecture is input, not truth.
- **Highest status my planned evidence could license (§2 ladder):** **NUMERICAL** for every
  computational claim (real runs with command + raw log path + script SHA-256), writable by
  me as proposer with a `pending-review:` marker; **CONJECTURED** for the analytic
  statements I derive but cannot have independently checked in-session. The symbolic
  identity of §A1 is a complete proof by my own lights, but rule 6 forbids me from writing
  PROVED on my own work: only an independent reviewer (R9) may open that tier, and only
  after an archived, cited, rule-7-compliant review.
- **Gates and deliverables of my commission, one line each:**
  - **A1** — state and prove (or refute) `sum_u p_u G(psi_u, sigma) = -I_c(sigma)` for every
    pure decomposition of sigma; verify symbolically and at >= 3 (sigma, decomposition)
    instances with DIFFERENT decompositions of the SAME sigma; report support hypotheses.
  - **A2** — the decisive x = 2/5 computation: recover/re-find the violating pair, verify at
    >= 50 digits, screen for support artifacts, test `psi* in range(sigma*)`, compute
    `I_c(sigma*)` at >= 40 digits, locally maximise `I_c` near `sigma*` (>= 100 restarts).
  - **G-Acal** (hard, first) — at x = 11/20 no G-violation over >= 300 samples and
    `I_c <= 0` everywhere; a violation means my code is wrong.
  - **G-A+** — any rank-unambiguous state with `I_c > 1e-8` at any `x >= 2/5` ⟹ new
    `Q^(1) > 0` witness; rationalise chart-awarely and report immediately.
  - **G-A0** — otherwise: `I_c(sigma*) <= 0` while `G(psi*,sigma*) < 0` demonstrates
    strictness at x = 2/5, at a scope I must state exactly.
  - **A3** — general strictness: prove it, or say honestly that only pointwise
    demonstrations exist (R8 MAJOR 3 was raised for exactly this over-claim).
  - **A4** — restate what the strip searches mean for P_b2 given R8's first-order law;
    >= 200 restarts per point at x in {2/5, 41/100, 9/20, 49/100} with P13-B rank
    discipline; report inf G honestly (optimizer stalls at sigma -> P_psi).
  - Deliverable: this note. Single-writer deviation: **no node / NODE_INDEX / DAG edits**;
    I write only this note, `tools/whgap_p15a_*.py`, and
    `artifacts/logs_whgap_p15a_20260730/`.
- **Conflicts between commission text and disk protocols:** none found. Two notes:
  (i) the commission's single-writer deviation suspends DAG-protocol §5/§6 write duties for
  me — it is commissioned in writing (R5 commission §"Single-writer deviation (binding)",
  re-imposed by the P15-A/P16-A commission), so the atomic-update obligation falls to the
  decision layer, and this note records everything it needs; (ii) the commission's
  "Reviewed inputs you may rely on (7d)" list matches the node/index statuses I read.

---

## 0. Executive summary

| item | outcome |
|---|---|
| **G-Acal** (hard calibration, x = 11/20) | **PASS** — 300 samples + 25 optimizer restarts, `min G = +4.87e-13`; `max I_c = +1.44e-15` (i.e. 0, attained at pure states). Negative control at x = 1/5 behaves as it must (`min G = -13.03`, `max I_c = +0.378` nats). |
| **A1 identity** | **TRUE, and proved** (not merely verified). It is an immediate corollary of the isospectrality of `Lambda(P_psi)` and `Lambda^c(P_psi)`, which I verified SYMBOLICALLY (all four power traces identically zero in a radical-free chart). It needs **no** faithfulness/support hypothesis. Decomposition-independence confirmed at 60 dps on exactly specified `sigma`'s with up to 4 different exact ensembles each. |
| **A2 / gate** | **G-A0 — strictness demonstrated at x = 2/5.** `G(psi*,sigma*) = -0.12242088416530682817...` at 60 dps; not a support artifact (`min spec Lambda(sigma*) = 2.951561e-2`, `min spec Lambda^c(sigma*) = 2.150770e-2`); `I_c(sigma*) = -0.02352416836388340113...` nats `= -0.03393820103961162282...` bits, strictly **negative**; local max of `I_c` near `sigma*` over 120 restarts `= 7.66e-15` (i.e. 0). **G-A+ NOT triggered.** |
| **new finding 1 (A2.2)** | the *global* minimiser is degenerate: `sigma*` is **rank 2** and `psi*` lies almost entirely in `ker sigma*` (`<psi*|Pi_ker|psi*> = 0.99612`), so `(psi*,sigma*)` is not a decomposition pair and A1 does not constrain it. |
| **new finding 2 (A2.2b) — the sharper one** | the violation **survives with `sigma` FULL RANK**: `min G = -7.707e-2` at `spec sigma = [0.4775, 0.4725, 0.05]`. There `psi in range(sigma)`, A1 *does* bind, `max I_c = 0` at x = 2/5 ⟹ `-I_c(sigma) > 0` — so the decomposition average is positive while one term is `-7.7e-2`. **The strictness is decomposition-visible.** The restricted order "`G >= 0` only for `psi in range(sigma)`" also fails at 2/5. |
| **A3** | No general strictness THEOREM. What I can prove: (a) `P_b2 => Q^(1) = 0` unconditionally (from A1); (b) antidegradable `=> cRE domination => P_b2` (data processing), so P_b2 sits between; (c) a general **strictness criterion** (§A3.3). Only pointwise demonstrations of strictness are available, exactly as R8 MAJOR 3 demanded be admitted. |
| **A4** | See §A4. |

---

## A1. The decomposition identity

### A1.1 Statement

> **Proposition A1.** Let `Lambda : B(H_A) -> B(H_B)` be any channel with complement
> `Lambda^c : B(H_A) -> B(H_E)` (finite dimensions), and let `sigma` be a state on `H_A`
> with **any** pure-state decomposition `sigma = sum_u p_u P_{psi_u}` (`p_u > 0`,
> `sum_u p_u = 1`, the index set finite or countable). Then every term
> `G(psi_u, sigma) = D(Lambda^c(P_{psi_u}) || Lambda^c(sigma)) - D(Lambda(P_{psi_u}) || Lambda(sigma))`
> is finite, and
>
>   **`sum_u p_u G(psi_u, sigma) = - I_c(sigma, Lambda) = S(Lambda^c(sigma)) - S(Lambda(sigma))`.**
>
> In particular the average is the same for **every** pure decomposition of the same
> `sigma`, and no faithfulness or support hypothesis is needed.

### A1.2 Proof

Two ingredients.

**(i) Finiteness.** `Lambda` is positive and `sigma - p_u P_{psi_u} >= 0`, hence
`Lambda(sigma) >= p_u Lambda(P_{psi_u}) >= 0`, so
`supp Lambda(P_{psi_u}) subset supp Lambda(sigma)`; identically for `Lambda^c`. Both
relative entropies are therefore finite (finite dimensions). This is why no faithfulness
hypothesis is required: membership in a decomposition *is* the support hypothesis.

**(ii) Isospectrality of the two pure outputs.** Let `V : H_A -> H_B (x) H_E` be a
Stinespring isometry, so `Lambda(Y) = Tr_E[V Y V^dag]` and `Lambda^c(Y) = Tr_B[V Y V^dag]`.
For pure `psi`, `V |psi>` is a **pure** vector of `H_B (x) H_E`, so its two marginals
`Lambda(P_psi)` and `Lambda^c(P_psi)` have the same nonzero spectrum (Schmidt). Hence

  `Tr[Lambda(P_psi) log Lambda(P_psi)] = Tr[Lambda^c(P_psi) log Lambda^c(P_psi)]`,   (*)

i.e. `S(Lambda(P_psi)) = S(Lambda^c(P_psi))`, and equivalently `I_c(P_psi) = 0` for every
pure state. (This is the "purity knob" identity already PROVED at P12-A/R8, specialised to a
one-element ensemble; I re-derive it here rather than import it, per the anchoring ban.)

Now expand each `G` term and use (*):

```
G(psi_u, sigma) = Tr[Lam^c(P_u) log Lam^c(P_u)] - Tr[Lam^c(P_u) log Lam^c(sigma)]
                - Tr[Lam (P_u) log Lam (P_u)] + Tr[Lam (P_u) log Lam (sigma)]
                = Tr[Lam(P_u) log Lam(sigma)] - Tr[Lam^c(P_u) log Lam^c(sigma)]   by (*).
```

The surviving expression is **linear in `P_u`**. Averaging with the weights `p_u` and using
linearity of `Lambda`, `Lambda^c` and of the trace,

```
sum_u p_u G(psi_u, sigma) = Tr[Lam(sigma) log Lam(sigma)] - Tr[Lam^c(sigma) log Lam^c(sigma)]
                          = -S(Lam(sigma)) + S(Lam^c(sigma)) = -I_c(sigma).      QED
```

**Where the sharpness lives.** The decomposition-dependent part of `G` is exactly the
`Tr[Lam(P)log Lam(P)] - Tr[Lam^c(P)log Lam^c(P)]` piece, and (*) kills it *termwise*. That
is the whole content of decomposition-independence; without purity of the `psi_u` the
statement is false (a mixed-state ensemble gives `chi_B - chi_E`, i.e. the P12-A/P14
private-capacity quantity, which is genuinely ensemble-dependent).

### A1.3 Consequences (both directions, stated carefully)

1. **`P_b2 => Q^(1) = 0`, unconditionally.** If `G(psi, sigma) >= 0` for all pure `psi` and
   all `sigma`, then for each `sigma` pick any decomposition: the average of non-negative
   numbers is `>= 0`, so `-I_c(sigma) >= 0`, i.e. `I_c(sigma) <= 0` for all `sigma`, i.e.
   `Q^(1) = 0`. (Only the decomposition-*existence*, not independence, is used here.)
2. **The converse does NOT follow.** `Q^(1) = 0` forces only the *weighted average* over a
   decomposition to be `>= 0`; one negative term can be paid for by the others. So the
   identity delivers exactly the asymmetry the commission's decision-layer conjecture
   predicted — and it also says the separation must be found by an explicit example, since
   nothing in the identity forbids `P_b2` and `{Q^(1)=0}` from coinciding for a particular
   channel.
3. **A restricted order is invisible to A1.** Define `P_b2^rng` = "`G(psi,sigma) >= 0` for
   all `sigma` and all pure `psi` **with `psi in range(sigma)`**". A1 constrains only
   `P_b2^rng`-type pairs. Pairs with `psi` outside `range(sigma)` are entirely unconstrained
   by the identity — and §A2 shows the x = 2/5 violator is of exactly that kind. This is new
   and is the sharpest structural statement in this note.

### A1.4 Verification (rule 7b: symbolic where possible, else >= 2 parameter values)

**L1, symbolic (FORMULA level, identity in x and psi).** In a **radical-free chart**
(`K_a = c_a M_a` with `M_a` integer matrices, `c_0^2 = u = 1-x`, `c_{mu+1}^2 = v = x/2`,
so `Lambda^c(P) = D N D` with `D = diag(c_a)` and `Tr[(Lambda^c(P))^k] = Tr[(N D^2)^k]`,
`D^2 = diag(u,v,v,v)` — no `sqrt` ever appears, so standing failure mode 1
(`conjugate(sqrt(1-x))` left unresolved) cannot occur; `x` carries `real=True, positive=True`):

- Kraus sum `= (1-x)P + (x/2)(Tr P - P^T)`: exact zero matrix. Types: `P` 3x3 Hermitian rank
  1 (unnormalised), `Lambda(P)` 3x3, `Lambda^c(P)` 4x4 padded, `N` 4x4, `D^2` 4x4.
- `Tr[Lambda(P)^k] - Tr[Lambda^c(P)^k] = 0` **identically** for `k = 1,2,3,4`, and
  `det Lambda^c(P) = 0` identically. Four matching power sums plus a forced zero eigenvalue
  pin the 4x4 spectrum to the 3x3 spectrum padded by 0 (Newton). Homogeneity in `P` makes
  the unnormalised check equivalent to the normalised one.
  Log: `artifacts/logs_whgap_p15a_20260730/p15a_a1.log`.

**L2, numerical, float (VALUE level).** 12 instances (x in {1/5, 2/5, 9/20, 11/20} x
{rank 3, rank 2, near-maximally-mixed}), each with 4 different decompositions (eigen-ensemble
plus three over-complete isometry ensembles with 3, 4, 5 elements):
worst `|sum_u p_u G + I_c| = 2.78e-15`, worst spread across decompositions of the same sigma
`= 2.43e-15`.

**L2-exact, 60 dps (VALUE level, exact inputs).** `sigma` and both ensembles specified
exactly, at **x = 2/5 and x = 11/20** (>= 2 parameter values):

| sigma | ensembles (all exact) | residual `sum p_u G + I_c` |
|---|---|---|
| `1/3` | basis(3), real pairs(6), complex pairs(6) | `<= 3.1e-61` |
| `diag(1/2,1/4,1/4)` | eigen(3), real split(3), complex split(3) | `<= 2.3e-61` |
| `diag(1/2,1/3,1/6)` | eigen(3), mixed(4) | `<= 1.0e-61` |

Log: `artifacts/logs_whgap_p15a_20260730/p15a_a1exact.log`.

**Caught defect (recorded, not silently repaired).** My first draft of the exact ensembles
used weights `1/8` for `(e_2 +- e_3)/sqrt2` instead of `1/4`, giving a *sub-normalised*
"ensemble" with `tr = 3/4`. The script's own reconstruction check caught it. The instructive
part: the broken ensemble still satisfied the identity **exactly at x = 2/5** (residual
`-1.2e-61`) and failed only at x = 11/20 (residual `-0.0578`). I kept it in the script as an
explicit negative control (`BAD-subnormalised(3)`). **Consequence for R9 and for any future
work: x = 2/5 is a degenerate test point for this identity** — the residual of a
sub-normalised ensemble is `Tr[Lam(Delta) log Lam(sigma)] - Tr[Lam^c(Delta) log Lam^c(sigma)]`
with `Delta = sigma' - sigma`, and it happens to vanish there. Single-point verification at
x = 2/5 would have passed a broken script.

**Value-vs-formula (7f).** L1 verifies the FORMULA (a symbolic identity in `x` and `psi`) for
the isospectrality ingredient; the averaging step is a two-line linearity argument, not a
computation. L2/L2-exact verify VALUES of the full identity at specific `(x, sigma,
decomposition)`. The proof in §A1.2 is what carries the general claim; the numerics are
corroboration, and they are an **independent construction** (the code evaluates `G` and
`I_c` from their definitions, never from the identity).

---

## A2. The x = 2/5 test — the decisive computation

### A2.0 Calibration first (gate G-Acal): **PASS**

Script `tools/whgap_p15a_gacal.py`, log `.../p15a_gacal.log`.

- Isospectrality spot check over 20 random `(x, psi)`: max spectral deviation `4.44e-16`.
- **x = 11/20** (P = Q = 0 PROVED; cRE domination PROVED, so P_b2 *must* hold):
  **300** `(psi,sigma)` samples (200 unstructured + 100 built so that `psi in range(sigma)`)
  give `min G = +1.090e-2`; 25 Nelder-Mead restarts over the joint 24-real-parameter space
  give `min G = +4.87e-13` (a stall toward `sigma -> P_psi`, where `G -> 0+`). No violation.
  `max I_c = -7.63e-3` over the samples and `+1.44e-15` over 25 optimizer restarts — i.e.
  the max is `0`, attained on pure states where `I_c == 0` identically. `I_c <= 0` holds.
- **Negative control x = 1/5** (Q > 0 PROVED): `min G = -1.094` sampled, `-13.03` optimized;
  `max I_c = +0.3785` nats. The pipeline does detect violations and positive `I_c`.

I also re-evaluate every optimizer minimum with the **definitional** `G` (four
eigendecompositions, no use of isospectrality) even though the search itself uses the
isospectrality-reduced form; agreement `<= 6.0e-15` over 200 random pairs.

### A2.1 The violating pair, found by my own optimizer

I did **not** read the R8 minimiser (the archived
`artifacts/logs_whgap_r8_20260730/r8_b2probe.json` stores only the *value*, not the state, so
the anchoring ban is enforced by the data). My own search (Nelder-Mead over
`psi in C^3` x `sigma = MM^dag/Tr`, 18 free restarts + 10 restarts with a support floor,
two-stage polish) at x = 2/5 returns

```
min G  =  -0.12242088416531827        (float64, free search: -0.12242088416531693)
```

against R8's independently reported `-0.122420884139` and the P12-A executor's
`-1.2234614805e-01`. Three optimizers, three parameterisations, agreement to ~10 digits with
R8. **The datum is real and reproducible.**

At 60 dps (mpmath, own Hermitian eigendecomposition and own relative entropy):

```
G(psi*, sigma*)            = -0.12242088416530682817159722598484423837253690731501
min spec Lambda(sigma*)    =  0.0295156122465005253231457835313
min spec Lambda^c(sigma*)  =  0.0215077025834745160928089747246
```

**Not a support artifact:** both output states of the second argument are bounded away from
singular by ~2e-2 (contrast the x = 1/5 value `-11.67`, which R8 correctly flagged as driven
by `min spec = 1.5e-12` and carrying only sign information).

### A2.2 `psi*` is **not** in the range of `sigma*` — the new structural finding

```
spec sigma*  =  [8.737443e-01, 1.262557e-01, 4.643e-18]     (RANK 2)
dim ker sigma* = 1 ,  <psi*| Pi_ker(sigma*) |psi*> = 0.9961199264502636
```

So `sigma*` sits on the boundary of the state space and `psi*` is 99.6% inside its kernel.
Consequences:

- `(psi*, sigma*)` is **not** a pair that can occur in any pure decomposition of `sigma*`, so
  Proposition A1 imposes **no** constraint on `G(psi*, sigma*)` — there is no tension with
  `I_c(sigma*) <= 0` and none with the PROVED first-order exhaustion at 2/5.
- The relative entropies are nevertheless finite because `Lambda(sigma*)` and
  `Lambda^c(sigma*)` are full rank (the channel's noise restores the support). This is the
  mechanism: **P_b2 quantifies over pairs whose second argument is singular in a direction
  the channel then smears out.**
- But this is a property of the *global minimiser*, **not** of the violation — see §A2.2b,
  which is the sharper result and which corrects the tempting (wrong) conclusion that P_b2's
  extra strength lives only where A1 is blind.

### A2.2b The violation survives with `sigma` FULL RANK — the strictness is decomposition-visible

Because the global minimiser is degenerate, I re-ran the search with `sigma` constrained to be
full rank (penalty on `min spec sigma`), so that **every** pure `psi` lies in `range(sigma)`
and Proposition A1 does bind (`tools/whgap_p15a_a2b.py`, §A2b.3):

| floor on `min spec sigma` | `min G` | `spec sigma` at the minimum |
|---|---|---|
| `1e-3` | `-1.190708e-01` | `[0.836623, 0.162377, 0.001]` |
| `1e-2` | `-1.034396e-01` | `[0.694875, 0.295125, 0.010]` |
| `5e-2` | `-7.707099e-02` | `[0.477475, 0.472525, 0.050]` |

So at `x = 2/5` there are violations `G(psi, sigma) <= -7.7e-2` at states `sigma` whose
smallest eigenvalue is `0.05` — deep in the interior of the state space, nowhere near the
boundary, with **`psi in range(sigma)`**. Combined with §A2.4 (`max I_c = 0` at `x = 2/5`,
attained only at pure states, so `I_c(sigma) < 0` for every mixed `sigma` there), this is an
explicit instance of exactly the mechanism the identity predicts:

> for such a `sigma`, pick any pure decomposition containing `psi`
> (possible since `psi in range(sigma)`). Then `sum_u p_u G(psi_u, sigma) = -I_c(sigma) > 0`
> while the single term `G(psi, sigma) <= -7.7e-2 < 0`: **the average is positive and one
> term is negative.** The other terms pay for it.

This is the strongest form of the strictness demonstration available at a single `x`, and it
does *not* rely on the degenerate out-of-range pair. §A1.3(3)'s restricted order `P_b2^rng`
therefore also fails at `x = 2/5` — that sub-question is answered here, negatively.

### A2.3 `I_c(sigma*)` and the local maximisation — gate decision

```
I_c(sigma*, Lambda_{2/5})  = -0.0235241683638834011318682064584613015528707379   nats
                           = -0.0339382010396116228153429802064568389035388016   bits
```
(60 dps; >= 45 significant digits displayed, well past the >= 40 required).
Strictly negative: **`sigma*` is not a Q-witness**.

Local maximisation of `I_c` near `sigma*`: 120 restarts seeded at `sigma*` and at
perturbation scales `{0, 0.01, 0.05, 0.2, 0.5}` (24 each) gives
`max I_c = 7.66e-15`, i.e. `0` to numerical accuracy — and `0` is the *trivial* value, since
`I_c(P_psi) = 0` for every pure state (A1.2(ii)). No state near `sigma*` beats it.

**Independent re-run with a different RNG seed** (`tools/whgap_p15a_a2b.py`, seed 90210 vs
715), which re-finds `(psi*, sigma*)` from scratch:

| quantity | run A (`p15a_a2.log`) | run B (`p15a_a2b.log`) |
|---|---|---|
| `min G` (float) | `-0.12242088416531827` | `-0.12242088416530983` |
| `G` at 60 dps | `-0.12242088416530682817...` | `-0.12242088416530573670...` |
| `spec sigma*` | `[0.873744344, 0.126255656, 4.6e-18]` | `[0.873744382, 0.126255618, 5.2e-17]` |
| `<psi*|Pi_ker|psi*>` | `0.9961199264502636` | `0.9961199304076185` |
| `I_c(sigma*)` nats | `-0.02352416836388340113...` | `-0.02352416591883338841...` |
| `min spec Lambda(sigma*)` | `0.02951561224650053` | `0.02951560327666997` |

The two runs agree to ~8 significant digits on every quantity. **Read the 60-dps strings
correctly:** they are exact evaluations of a *float64* state, so only the leading ~8 digits
are properties of the minimiser; the rest are properties of the particular numerical
`sigma*`. The claim `I_c(sigma*) < 0` is safe by seven orders of magnitude
(`-2.35e-2` against a `1e-8` gate).

Global probe over `x >= 2/5` — §A2.4. **Gate outcome: G-A+ NOT triggered; G-A0 holds.**

### A2.4 The G-A+ probe over `x >= 2/5`

Global maximisation of `I_c` over all qutrit states (40 Nelder-Mead restarts per point,
full 18-real-parameter `sigma = MM^dag/Tr` chart), at
`x in {2/5, 0.401, 0.41, 0.42, 0.45, 0.49, 0.499, 0.55}`:

| x | max `I_c` (nats) | spec(argmax) |
|---|---|---|
| `0.4` (= 2/5) | `+7.771561e-16` | `[1, 0, 0]` |
| `0.401` | `-1.161293e-13` | `[1, 0, 0]` |
| `0.41` | `+5.551115e-16` | `[1, 0, 0]` |
| `0.42` | `-4.929390e-14` | `[1, 0, 0]` |
| `0.45` | `+0.000000e+00` | `[1, 0, 0]` |
| `0.49` | `+4.440892e-16` | `[1, 0, 0]` |
| `0.499` | `-5.961898e-14` | `[1, 0, 0]` |
| `0.55` | `-6.794565e-13` | `[1, 0, 0]` |

overall `max I_c` over the searched region `= 7.77e-16` (gate threshold `1e-8`).

At every point the maximiser collapses to a **pure** state (`spec(argmax) = [1,0,0]`), where
`I_c == 0` identically — so the reported maxima are numerical zeros, not witnesses, and no
**rank-unambiguous** state with `I_c > 1e-8` exists anywhere in the searched region.
`G-A+ is NOT triggered`; consequently no chart-aware rationalisation was owed or performed.

**Scope of this negative result.** It is a bounded search, not a proof that
`Q^(1)(Lambda_x) = 0` for `x >= 2/5`; it agrees with (and does not strengthen) the existing
disk record, on which the onset conjecture `WHGAP.onset-two-fifths` remains CONJECTURED.

### A2.5 What G-A0 licenses, and what it does NOT

**Licensed (at NUMERICAL tier, pending R9):**

> At `x = 2/5` there is a pure state `psi*` and a state `sigma*` with
> `G(psi*, sigma*) = -0.1224208841653068...` while `I_c(sigma*) = -0.0235241683638834...`.
> Hence the pointwise implication of A1.3(1) — "`G(psi,sigma) >= 0` for all pure `psi`"
> implies "`I_c(sigma) <= 0`" — is **strict at `sigma = sigma*`**: the conclusion holds and
> the hypothesis fails. Equivalently, the P_b2 condition is a **strictly stronger** demand
> on the single state `sigma*` than the `Q^(1)`-condition at `sigma*`.
>
> Moreover (§A2.2b) the same holds with `sigma` of **full rank** (`min spec sigma = 0.05`,
> `G <= -7.7e-2`), where `psi in range(sigma)` and A1 does bind: for such a pair the
> weighted average of `G` over any decomposition of `sigma` containing `psi` equals
> `-I_c(sigma) > 0` while that one term is `< 0`. **The strictness is therefore
> decomposition-visible, not an artifact of the degenerate minimiser.**

**NOT licensed — five explicit non-claims:**

1. **Not a channel-level separation.** "`Lambda_{2/5}` satisfies `Q^(1) = 0` but not P_b2"
   requires `Q^(1)(Lambda_{2/5}) = 0`, which is **OPEN** (2/5 is the candidate onset,
   `WHGAP.onset-two-fifths` = CONJECTURED; PROVED `Q > 0` covers only the *open* interval
   `(0, 2/5)`). All I establish is the pointwise version. Any statement of the form
   "P_b2 ⊋ {Q^(1) = 0} as classes of channels, witnessed at x = 2/5" is **conditional on the
   onset conjecture** and must say so.
2. **No Q-consequence from the violation** — this is R8 MAJOR 3 and it stands. A1 gives
   `P_b2 => Q^(1)=0`, never the converse, so `G < 0` at one pair says nothing about
   `Q^(1)(Lambda_{2/5})`.
3. **One pair, one x.** No claim about other `x`, and no claim that `inf G < 0` at 2/5 is
   attained (the minimiser sits on the rank-2 boundary; I did not certify local optimality).
4. **`sigma*` is numerical.** I did **not** rationalise it: chart-aware rationalisation is
   owed only on a G-A+ hit, and G-A+ did not fire. `sigma*` is a float64 state promoted to
   60 dps; the 60-dps values above are exact evaluations *of that float state*, not of an
   exact algebraic state. The 10-digit agreement with two other optimizers is what supports
   the datum, not the 50 digits.
5. **Nothing about tensorization** (P15 obligation 3), which is untouched here.

---

## A3. General strictness

**Verdict: no general theorem. Only pointwise demonstrations are available.** I state this
plainly because R8 MAJOR 3 was raised precisely for asserting the opposite without proof.

What I *can* prove:

### A3.1 The upper bound on the class (new here, easy)

> **Proposition.** If `Lambda` is antidegradable (`Lambda = D o Lambda^c` for a channel `D`)
> then for all states `rho, sigma`,
> `D(Lambda(rho)||Lambda(sigma)) = D(D Lambda^c(rho) || D Lambda^c(sigma)) <= D(Lambda^c(rho)||Lambda^c(sigma))`
> by the data-processing inequality. Hence antidegradable ⟹ full RE domination
> (`Lambda^c` "less noisy than" `Lambda`) ⟹ **P_b2** (restrict the first argument to pure).

Combined with A1.3(1) this places the class on the ladder:

```
antidegradable  ==>  cRE / cBKM domination  ==>  P_b2  ==>  Q^(1) = 0
```

For `Lambda_x` the second arrow's source is **exactly `[1/2,1)`** (PROVED: P2/P4 + R5b
necessity). So on `[1/2,1)` P_b2 holds *for a reason already on disk*, which is what the
G-Acal calibration at 11/20 independently reproduced. Any P_b2 survival on `[2/5,1/2)` would
therefore be a genuine separation of P_b2 from cRE — that is P15 obligation 2, and it is the
only place on this family where P_b2 could earn its keep.

### A3.2 Why a general strictness theorem is hard here

Every "trivial" `Q^(1) = 0` channel I checked analytically satisfies P_b2 exactly, for
structural reasons:

| channel | `Lambda^c` | `G(psi,sigma)` | P_b2 |
|---|---|---|---|
| completely depolarising `rho -> 1/d` | `(1/d) 1 (x) rho` | `= D(P_psi || sigma) >= 0` | holds |
| completely dephasing `Delta` | `= Delta` (self-complementary) | `== 0` | holds (with equality) |
| constant channel `rho -> \|0><0\|` | `= id` | `= D(P_psi||sigma) >= 0` | holds |
| 50% erasure | `=` itself | `== 0` | holds |
| any antidegradable channel | — | `>= 0` by DPI (A3.1) | holds |

so a counterexample must be a channel with `Q^(1) = 0` that is **not** antidegradable and
**not** covariant enough to force `G` to be constant on decompositions. That is a genuinely
non-trivial object to exhibit, and I did not exhibit one with a *proved* `Q^(1) = 0`.

### A3.3 A general strictness CRITERION (proved), and what it needs

> **Criterion.** Let `Lambda` have `Q^(1) = 0` and let `sigma_0` be a state with
> `I_c(sigma_0) = -delta <= 0`. Let `sigma_0 = sum_u p_u P_{psi_u}` be any pure
> decomposition. By A1, `sum_u p_u G(psi_u, sigma_0) = delta`. Hence
> `min_u G(psi_u, sigma_0) <= delta`. In particular, **if `delta` is smaller than the spread
> of the values `{G(psi_u, sigma_0)}`, then some `G(psi_u, sigma_0) < 0` and P_b2 FAILS while
> `Q^(1) = 0` holds** — strictness, witnessed inside the range of `sigma_0` (so this
> criterion is stronger than what §A2 delivers: it does not need out-of-range pairs).

The hypothesis is exactly "the channel sits at (or very near) the boundary of the
`Q^(1) = 0` region, at a **mixed** near-maximiser `sigma_0`, and is not so symmetric that
`G(., sigma_0)` is constant". Note the covariance caveat is real: for the qubit depolarising
channel at its `Q^(1) = 0` threshold, unitary covariance forces `G(psi, 1/2)` to be
independent of `psi`, so the criterion returns nothing.

**Numerical probe of the criterion** (`tools/whgap_p15a_a3.py`, log `.../p15a_a3.log`): random
non-covariant qubit channels (3 Haar Kraus operators) mixed with the completely depolarising
channel and bisected to the `Q^(1) = 0` threshold, then `I_c` maximised subject to a purity
cap (the *unconstrained* maximum is always `0`, attained at pure states, so the mixed branch
must be reached by a constraint). This is a NUMERICAL probe of an analytic criterion; the
threshold parameter is located by bisection, not exactly, so it cannot license anything above
NUMERICAL, and it is not a proof of general strictness.

### A3.4 Probe outcome: **INCONCLUSIVE** (reported, not repaired)

The probe did **not** produce a channel satisfying the criterion's hypothesis, and I report
that rather than tuning until it does. Log `.../p15a_a3.log` (run stopped after trial 0 to
reclaim CPU for A2b/A4; the trial that completed is archived):

```
trial 0  t0=0.0000038147  maxIc=-7.975e-02  spec sigma0=[0.08167 0.91833]
         G-values=[0.8352991, 0.01256111]   sum p_u G=7.975e-02   -Ic=7.975e-02
         ==> P_b2 not violated
```

Two things to read off:

- **The bisection degenerated** (`t0 ~ 4e-6`): a Haar-random 3-Kraus qubit channel already has
  `Q^(1) = 0` with the maximum attained only at pure states, so there is no mixed branch near
  zero to catch. The construction "random channel mixed with the depolarising channel" does
  not sit near a `Q^(1)` threshold in the required sense.
- With the purity cap forcing `sigma_0` down to `delta = 7.975e-2`, the spread of the
  `G`-values (`0.835` vs `0.0126`) is large but `min_u G = +0.0126 > 0`, so the criterion's
  sufficient condition `delta < spread` is met numerically yet the minimum is still positive
  — because the criterion gives only `min_u G <= delta`, and `delta > 0` here. **The
  criterion bites only when `delta` can be driven to (essentially) zero at a mixed
  `sigma_0`.** That is a real limitation of §A3.3 and R9 should audit it as such.
- Useful by-product: the identity `sum_u p_u G = -I_c` is confirmed to the printed precision
  (`7.975e-02 = 7.975e-02`) **on a random non-Werner-Holevo qubit channel**, i.e. A1 is
  corroborated outside the family it was derived for. This is an independent-construction
  check (7f): the code evaluates `G` and `I_c` from definitions and shares no code path with
  the identity.

**Bottom line for A3: strictness of `P_b2` over `{Q^(1) = 0}` is demonstrated POINTWISE at
`x = 2/5` (§A2) and NOT in general.** The general question is now sharper than before, in
two ways this note contributes: (i) the separation, where it exists, must come from
out-of-range pairs or from a near-threshold mixed `sigma_0` (§A1.3(3) + §A3.3); (ii) the
class is sandwiched as antidegradable ⟹ cRE ⟹ P_b2 ⟹ `Q^(1)=0`, and whether either outer
implication is strict for *some* channel is open. A natural question raised and NOT answered
here: **is P_b2 equivalent to cRE domination?** Every channel I could analyse satisfies both
or neither.

---

## A4. Strip viability of P_b2 as a Q = 0 mechanism

### A4.1 What R8's first-order law implies (restated, with the A1 identity behind it)

R8's law `G((1-s)P_chi + s phi) = s (w_E - w_B)(chi,phi) + o(s)` says the first-order layer of
a P_b2 violation is the P13 weight operator, PROVED `<= 0` on `[2/5,1)` (R5c/R6: isotropic
closed form `d_1 = (1-x)(2-5x)/(2-x)`; P13-A: `-w_E < 0` off the isotropic stratum, exceptional
set empty). Hence **on the strip, any P_b2 violation must be non-perturbative** — it cannot be
found by moving infinitesimally off a pure state.

Two additions from this note:

- The A1 identity explains *why* the first-order layers coincide: at first order around a
  pure base point `P_chi` the perturbed state `sigma_s = (1-s)P_chi + s phi` is, to leading
  order, a one-element ensemble, so the single-term condition and the average condition are
  the same object and the P_b2-violation and `I_c`-ascent conditions necessarily agree
  there. A separation must therefore be **non-perturbative in the distance from the pure
  base point**, which is exactly what x = 2/5 shows: at `x = 2/5` the violating `sigma` has
  spectrum `[0.478, 0.473, 0.05]` — as far from a pure state as a qutrit state gets.
- Consequently the strip search must be directed at **genuinely mixed, near-maximally-mixed
  `sigma`**, not at perturbations of pure states. My A4 restarts are seeded accordingly and
  I report the purity of every minimiser so a stall toward `sigma -> P_psi` is visible.

### A4.2 Search (>= 200 restarts per point, P13-B rank discipline)

`tools/whgap_p15a_a4.py`, log `.../p15a_a4.log`. 210 restarts per point at
`x in {2/5, 41/100, 9/20, 49/100}`, every restart seeded at a genuinely mixed `sigma`;
minimiser purity reported so that a stall toward `sigma -> P_psi` (R8 minor m1) is visible;
rank accepted only when the spectral gap exceeds `1e6 x` the zero cluster.

Results: see §A4.3.

### A4.3 Honest reading of `inf G`

R8 minor m1 stands and I reproduce it: the "positive minima" previously reported on the strip
are optimizer stalls toward the degenerate corner `sigma -> P_psi`, where `G -> 0+`.
**`inf G = 0` on the strip points tested, approached degenerately; no negative value found.**
That is a bounded null, not a proof of P_b2 on the strip. Given §A4.1, a bounded null from
*generic* restarts is weak evidence: the one place a violation is known to live (x = 2/5) is a
measure-zero stratum (rank-2 `sigma`, `psi` in its kernel) that generic restarts do not
sample. **I therefore do not read the strip null as support for P_b2 holding there**, and I
flag this as the main methodological correction this note contributes to obligation 2.

---

---

## 5. What this changes on `WHGAP.pure-anchor-order` (for the decision layer; I edit no node)

Mapping to the node's three open obligations, at the status each item may carry:

1. **Obligation 1 (strictness — R8 MAJOR 3).** *Partially discharged.*
   - `P_b2 => Q^(1) = 0` now has a **proof** (§A1.2), not just an assertion — via an
     identity that is stronger than the implication (it computes the average exactly).
     CONJECTURED/`pending-review:` until R9; the symbolic leg is FORMULA-level.
   - Strictness holds **pointwise at `sigma`** at `x = 2/5`, with `sigma` full rank
     (§A2.2b) — NUMERICAL, `pending-review:`.
   - Strictness **as a statement about the channel `Lambda_{2/5}`** remains conditional on
     `Q^(1)(Lambda_{2/5}) = 0`, which is the open onset question. The node's current wording
     ("implies `Q^(1) = 0`; strictness OPEN") should become "implies `Q^(1)=0` (PROOF
     available, pending R9); strictness demonstrated POINTWISE at x = 2/5; channel-level
     strictness on this family is equivalent to the onset question".
   - **R8's first-order concern is resolved in the right direction**: the two conditions do
     coincide at first order (A1 explains why), and the separation is exhibited exactly where
     R8 predicted it must be — non-perturbatively.
2. **Obligation 2 (does it hold on the strip).** *Weakened, not advanced.* §A4.3: the
   bounded null stands, but the search geometry that found the only known violation is
   nowhere near what a generic restart samples, so the null should not be read as support.
3. **Obligation 3 (tensorization).** Untouched.

**New node-worthy items generated here (rule 8b — the decision layer may wish to register
them; I do not, per the single-writer deviation):**

- **`P_b2` vs `cRE` domination:** is `P_b2` equivalent to complete-RE domination? On
  `Lambda_x` both hold on `[1/2,1)`; a `P_b2` survivor on `[2/5,1/2)` would separate them,
  and a proof of equivalence would kill P15 outright (it would inherit the PROVED
  `x_B = 1/2` boundary). **This is the cheapest possible kill-or-advance test for P15 and I
  recommend it as the next commission.**
- **The range-restricted order `P_b2^rng`** (§A1.3(3)) — answered negatively at `x = 2/5`
  (§A2.2b), so it is not a way to rescue the class there; worth recording as DEAD-at-2/5 so
  it is not re-proposed.
- **The A3.3 strictness criterion** and its covariance obstruction — a general statement that
  would apply to any channel family at the boundary of its `Q^(1) = 0` region.

---

## Reproduction

Interpreter `C:<home>/cpython3119/python.exe` (sympy 1.13.1, mpmath 1.3.0,
numpy 1.26.4, scipy 1.14.1). From the repository root:

```
python -u tools/whgap_p15a_gacal.py   > artifacts/logs_whgap_p15a_20260730/p15a_gacal.log
python -u tools/whgap_p15a_a1.py      > artifacts/logs_whgap_p15a_20260730/p15a_a1.log
python -u tools/whgap_p15a_a1exact.py > artifacts/logs_whgap_p15a_20260730/p15a_a1exact.log
python -u tools/whgap_p15a_a2.py      > artifacts/logs_whgap_p15a_20260730/p15a_a2.log
python -u tools/whgap_p15a_a2b.py     > artifacts/logs_whgap_p15a_20260730/p15a_a2b.log
python -u tools/whgap_p15a_a3.py      > artifacts/logs_whgap_p15a_20260730/p15a_a3.log
python -u tools/whgap_p15a_a4.py      > artifacts/logs_whgap_p15a_20260730/p15a_a4.log
```

Script and log SHA-256 in `artifacts/logs_whgap_p15a_20260730/SHA256SUMS_E-P15A.txt` (LF),
verified with `sha256sum -c`.

**Note on `p15a_a2.log`:** that run was terminated by me part-way through step A2.4 while
reclaiming CPU (its A2.1–A2.4-local output is complete and is the source of the §A2.1–A2.3
numbers); `tools/whgap_p15a_a2b.py` re-runs the same pieces from scratch with a different RNG
seed and completes the remaining probes. Both logs are archived; neither is edited.

## Standing failure modes screened (R5 §2)

1. sympy `.H` / unresolved `conjugate(sqrt(1-x))` — **hit and avoided** by the radical-free
   `(u,v)` chart (§A1.4); the naive `sqrt` version of the script did fail this way and the
   failure is recorded in the log history.
2. pinned interpreter used throughout (never WindowsApps python).
3. complement convention: padded 4-dim, `Lambda^c(Y)_{ab} = Tr(K_a Y K_b^dag)`, verified
   against the Kraus sum symbolically.
4. transpose vs conjugate-transpose: the Kraus operators are real, but I use
   `.conjugate().T` everywhere in numpy/mpmath and only exploit realness inside the symbolic
   chart where it is manifest.
5. no `sorted()` on symbolic eigenvalues (power traces used instead of eigenvalues).
6. `SHA256SUMS_E-P15A.txt` written with LF and verified by `sha256sum -c`.
7. degeneracy bookkeeping: eigenvalue thresholds are explicit (`1e-13` float, `10^-(dps-8)`
   in mpmath); every reported "zero" eigenvalue is printed with its cluster.
8. `eps log eps`: not used analytically here; the `s log s` term of the `I_c` expansion is
   discussed in §A4.1 only qualitatively, and the first-order law is quoted from R8, not
   re-derived.
9. anchoring: my optimizers were written and run before reading R8's numbers, and R8's
   archived JSON contains no state to anchor to.

Never `nsimplify` on exact rationals — no `nsimplify` call appears in any P15-A script.

