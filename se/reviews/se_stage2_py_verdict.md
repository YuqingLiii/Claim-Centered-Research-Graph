# SE Stage 2 — P_Y verdict: the stay-channel decay bound at q=2n

**Date:** 2026-07-17
**Checker:** fresh assembler (Fable 5), reconciling three independently pre-registered and
adversarially re-verified ingredient audits (A = lem:kappa, B = lem:Wkv, C = matching fraction).
**Source of truth:** `se/artifacts/references/BR_1310.5185v4_collision.tex` (the real LaTeX, 1619 lines).
Commission: `SE_STAGE2_PY_CERTIFICATION_PROMPT.md`; Stage-1 scoping: `se/artifacts/se_stage1_q0_verdict.md`.

---

## VERDICT: **CERTIFIED** — `||Ybar_{se,k}|| <= sqrt(2) * sqrt(k/n)` for all n and all `0 <= k < K = floor(n^{1/3})`, at q=2n (in fact at every q >= 2). Explicit constant **C = sqrt(2)**. [PROVED, conditional on nothing outside this document's chain]

BR prove lem:normEstimations(b) (BR:682-683, `||Ybar_{qp,k}|| = O(sqrt(k/n))`) only under the paper's
standing assumption q = Omega(n^2) (BR:77, BR:120). The finding of this stage: **that assumption is
never consumed anywhere in the (b) proof chain.** All three ingredients are alphabet-free (or need only
q >= 2), the fraction count is exact, and the constant assembles to sqrt(2). The q = Omega(n^2)
requirement lives entirely in the illegal-row/column removal argument (BR:346, BR:714, BR:730,
sec:subIllegal) — a different part of the paper, disjoint from (b). [PROVED — each claim cited below]

---

## 1. Statement certified

Let `Ybar_{se,k} = Y_{se,k} (Pi_0 ⊗ Pibar'_{se,k})` (BR:655-657), with
`Pibar'_{se,k} = sum_{l=0}^{k} Pibar^{(n-1)}_{k-l} ⊗ Pibar^{(n)}_l` (BR:639), acting on
`(C^q)^{⊗ 2n}` with q = 2n, and `Y_{se,k}` the block column over M_se of the stay-channel blocks
`(1/sqrt(|M_se|)) Y^mu_k` (BR:532, BR:549, BR:992). Then

**P_Y:** `||Ybar_{se,k}|| <= sqrt(2) * sqrt(k/n)` for all n >= 2 and all `0 <= k <= K-1`. [PROVED]

(k=0 is trivial: `Y_{se,0} = 0` identically — the `|c|=k-1` sum in BR:549 is empty. [PROVED])

## 2. The chain, link by link

BR's (b) proof is BR:1348-1350, four sentences. Every link, with where it was certified and its
q-dependence:

**Link 1 — existence of a kappa-fixed top singular vector (ingredient A).** [PROVED, Q-FREE]
`Ybar_{se,k}` is symmetric w.r.t. `S'_se = S_{[2..n]} × S_{[n+1..2n]}` (BR:1343/1348), so Schur gives
an irreducible module of principal right-singular vectors, isomorphic to
`Specht^{(n-1-l,lambda)} ⊗ Specht^{(n-k+l,lambda')}` for some sector l (BR:1345). lem:kappa
(BR:759-793) then supplies a nonzero v in the module with `kappa v = v`, kappa = F =
`2^{-k} prod_i (eps - (a_i,b_i))` (BR:752-756), pairs in [2..2n], via a double tensor application
(BR:1345 parenthetical). Ingredient A audited the proof body BR:766-793 line by line: it is pure
`C[S_m]` — tableaux, row/column symmetrizers, a coefficient argument, pigeonhole; the alphabet space
`C^q` appears nowhere between BR:743 and BR:794, and the transfer to embedded copies is a Schur-lemma
transport that references only irrep labels, never multiplicities (where q lives). Adversarially
re-derived by a second checker: AGREES. One implicit hypothesis surfaced: the tableau construction
needs m >= 2k and 2k distinct positions; in SE m ∈ {n-1, n} and `2(floor(n^{1/3})-1) <= n-1` for all
n >= 2, so it is satisfied throughout the witness range. [PROVED]

**Link 2 — the e_0-support step (the "fourth ingredient" ingredient A flagged).** [PROVED, Q-FREE]
BR:1348's "because both these components are e_0 for all basis vectors used in v" is NOT part of
lem:kappa and was flagged by the A-checker as unassigned. It was discharged independently by the
B- and C-audits: `kappa v = v` on the exactly-weight-k space forces every basis vector of v to carry
exactly one non-e_0 label per pair {a_i,b_i} and e_0 everywhere else — this is precisely BR's `w_z`
basis, `z ∈ [1..q-1]^k` (BR:1011-1017); the B-verifier re-derived from first principles that kappa's
image restricted to `H^{(2n)}_k` is exactly `span{w_z}` (weight-k pigeonhole + per-pair
antisymmetrization, q-free). And `v ∈ image(Pi_0 ⊗ Pibar'_{se,k})` (BR:655-657) forces the position-1
component to e_0. Hence if mu(1) is outside the 2k-set, `Y^mu_k v = 0`: `Y^mu_k` applies
`(e_0* ⊗ Pi_1)` to positions (1, mu(1)) (BR:549 with BR:530, mu_{1,1}=1 at BR:317), and
`Pi_1 e_0 = 0`. The flagged gap in the commission's three-ingredient split is thereby CLOSED, not
papered: it was checked, just under B/C's roof. [PROVED]

**Link 3 — the surviving-case bound (ingredient B, lem:Wkv).** [PROVED, needs only q >= 2]
`||Y^mu_k v|| <= ||v||` with constant EXACTLY 1 — not O(1). lem:Wkv's proof (BR:1008-1193) was audited
step by step: the only alphabet use in the entire proof is non-emptiness of the label set [1..q-1]
(q >= 2); everything else is position combinatorics on the graph G' (cycles/paths, BR:1022-1030),
exact 0-1 matrix row/column counts (clm:Lambdav BR:1149-1169 gives `||Xi kappa|| <= 2^{-K'/2}`,
clm:WLambda BR:1173-1188 gives `||W Xi|| <= 2^{K'/2}`, K' = cycle count of G', a DIFFERENT K than
floor(n^{1/3}) — the 2^{K'} factors cancel exactly), and the X/Y restriction (BR:1192) only zeroes
0-1 entries, preserving both counts. clm:odin's perturbative `1/(m-2k+2)` estimate is never imported.
Adversarially re-derived: AGREES; one benign exposition gap in BR:1035 (image inclusion literally
false on all of `H^{⊗2n}`, true restricted to `H^{(2n)}_k`, restriction licit since `W = W Pi^{(2n)}_k`
per BR:531/993) — repaired q-free. At q = 2n >= 4 the q >= 2 requirement is trivially met. [PROVED]

**Link 4 — the fraction (ingredient C).** [PROVED, Q-FREE, and EXACT — this is where C comes from]
Matchings are objects on POSITIONS [2n] (BR:312-319); q never enters the block index set M_se, the
`1/sqrt(|M_se|)` weights (BR:532, BR:992), or the partner distribution. `|M_se| = n!` and mu(1) is
uniform over [n+1..2n] ((n-1)! matchings per partner). The special set has, in sector (l1, j) with
l1 + j = k (BR:1345/BR:639), exactly 2j distinct elements in the second half; the 2·l1 first-half
elements can NEVER partner position 1 (M_se is bipartite). Exact per-sector fraction:

  `P(mu(1) ∈ special set) = 2j/n`, worst sector j = k gives max `2k/n`. [PROVED — exact count, not O(.)]

Brute-force corroboration [NUMERICAL] over ALL n! matchings in exact Fraction arithmetic, n=3..9,
k=1..3, all sectors: fraction == 2j/n in every case; plus a direct operator-norm computation of
`||Ybar_{se,k}||` AT q=2n from the BR definitions (k=1 n=3,4,5; k=2 n=5, dim 3645): all norms within
the certified bound (observed truth j/n — the bound carries a factor-2 slack from Link 3's worst case).
Original: `se_py_taskC_count_and_norm.py` SHA-256
9A40EE2E54DA22F5CFE2C3059B3859DE6F7B1D5113AE30F4FFBD50800B3FB576, log `se_py_taskC_log.txt` SHA-256
C7063938FAFD03568E04B2EF3980D0E81A23D75D4C7AD9EE7A1BA4B048C531E8. Independent re-verification:
`taskC_reverify_fraction.py` SHA-256
11E655BEAC0897F0B0413FFC40B73C061336C554B67396FA56E5D204A0D6458B, log SHA-256
3BC50F562AA656A3428EBC9EAA0EB62D2DB2C340F8AF854A43CC3F5E9F1FE175 (session scratchpad
`<machine-local-path-redacted>\`;
interpreter `<machine-local-path-redacted>`). Note the commission's G8
("numerics unreachable") was half wrong: the WITNESS regime (k>=1 AND K>=2, needing n>=8) is indeed
unreachable, but the P_Y statement itself was computable off-spec and passed.

**Assembly.** [PROVED] Block-column structure gives
`||Ybar_{se,k} v||^2 = (1/n!) sum_mu ||Y^mu_k v||^2` for the principal v of Link 1; Links 2-4 give
`<= (2j/n)·||v||^2 <= (2k/n)·||v||^2`, hence

  **`||Ybar_{se,k}|| <= sqrt(2k/n) = sqrt(2) · sqrt(k/n)`, C = sqrt(2).**

**G5 compliance:** sqrt(2) is derived from the exact positional count 2j/n <= 2k/n plus lem:Wkv's
exact constant 1 — NOT read off BR:683's O(sqrt(k/n)), which carries no extractable constant. (The
previously struck `sqrt(2k/n)` figure is hereby re-established with its own provenance; the F5 strike
was against the attribution, and the correct attribution is now this derivation.)

## 3. q-dependence summary

| Ingredient | Verdict | q needed | Status at q=2n |
|---|---|---|---|
| A: lem:kappa (BR:759-793) | Q_FREE | none (pure C[S_m]) | holds [PROVED] |
| Link 2: e_0-support of v (BR:1348) | Q_FREE | none (w_z structure) | holds [PROVED] |
| B: lem:Wkv (BR:1001-1193) | needs q >= 2 only | q >= 2 (label set nonempty) | 2n >= 4 [PROVED] |
| C: fraction (BR:1348-1350) | Q_FREE, exact 2j/n | none (positions only) | holds [PROVED] |

The proof is q-free in the strongest sense: it holds verbatim at every q >= 2, which per G8 escapes
the small-n spec trap entirely — no numerics are load-bearing.

## 4. Superseded sketches — provenance upgrade

All four on-disk relays of this bound are now labeled **[PROJECT'S BOUND]**, superseded by this
certification as primary source:
- `se_legal_diamond_query_norm_audit.md` (4.4), lines ~394-401 — correct, "deliberately loose".
- `exact_band_descent_analysis.md` (6.3), lines ~424-436 — the most precise (its 2b/n = the per-sector 2j/n).
- `se_legal_br_diamond_descent.md` (1.11), lines ~153-161 — correct.
- withdrawn `se_witness_challenge_response_20260716.md` Q6.1, lines ~326-342 — correct, including its
  remark that BR's large-alphabet assumption is unused here (now verified, no longer a relay).
`SE_CARRIER_SUFFICIENCY_COMMISSION.md` 4.6(b) claim that audit (4.4) was an independent counting
derivation: ACCURATE.

## 5. The two honest counterweights — a certified P_Y does NOT close SE

**(1) One leg of three.** `Gamma ∘ Delta_i` has three channels (BR:668-676): slope X (discharged,
Route 1 — write-up still owed), stay Y (**closed by this document**), and **Phi — OPEN**. Phi is
lem:normEstimations(c) (BR:684, `||W_{qp,k} Phi_{qp,k}|| = O(1/sqrt(n))`), whose proof (BR:1352-1369)
runs through lem:newMain and lem:Wk-1 and has NOT been audited at q=2n. `max_i ||Gamma ∘ Delta_i|| = O(1)`
— the actual open problem (Rosmanis §7, open since 2014) — remains OPEN until Phi is certified. [OPEN]

**(2) Family split (Stage-1 Hole 3(e)).** This bound is on BR's `Ybar_{se,k}`, built on
`Pibar'_{se,k}` over `S_{n-1} × S_n` (BR:639, BR:655). The project's witness `P_k` lives on
`Pibar_{se,k}` over `S_n × S_n` (BR:609). A certified P_Y bounds BR's channel; it is NECESSARY, not
yet provably SUFFICIENT, for the witness channel. [OPEN]

And per the commission's counterweight: P_Y turning out q-free and easy is CONSISTENT with SE being
hard elsewhere — the difficulty concentrated in `c_0 = e^{1.1534n}` (the stay-channel hole of Stage 1
is elsewhere in the chain) and in Phi. SE = Theta(n^{1/3}) is Zhandry's theorem; this program is
certification/write-down work, not a new separation. **"P_Y is certified" must not be read as "SE is
nearly done."**

## 6. Residual caveats (none verdict-affecting)

- Factor-2 slack: small-case truth is j/n vs certified 2j/n (Link 3 worst case is loose). [NUMERICAL]
- Witness-regime numerics (k>=1 with K>=2, i.e. n>=8, q=16) were never computed — the count there is
  proved, not measured. [PROVED by the q-free argument; NUMERICAL coverage stops at n=5 for norms, n=9 for fractions]
- BR:1035 image-inclusion exposition gap: repaired q-free (restriction to `H^{(2n)}_k` via BR:531/993). [PROVED]
- Symbol traps for future readers: kappa renders as the macro `F` in sec:proofs (BR:743); lem:Wkv's
  internal `K` is the G' cycle count, not floor(n^{1/3}); `H^{(m)}_k` is EXACTLY weight k (BR:371-373),
  not at-most.

## 7. Next step

Stage 3: audit the **Phi channel** — lem:normEstimations(c) at q=2n (BR:1352-1369 for the proof;
ingredients lem:newMain, lem:Wk-1, kappa'/eqn:kappaprim), with the same pre-registered
break-criteria discipline. In parallel: resolve Hole 3(e) (transfer from `Pibar'_{se,k}` to the
witness's `Pibar_{se,k}`) so the certified legs provably bound the witness channel.
