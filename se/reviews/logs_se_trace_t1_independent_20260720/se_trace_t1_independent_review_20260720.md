# Independent Rule-7 Review — `SE.denom.Phi.legal.trace.t1`

**Date:** 2026-07-20  
**Role:** independent reviewer; no DAG edits  
**Claim reviewed:** On every admissible tame sector, for every removable tail `z`,

\[
\frac{m f^{\tau_z}(\delta_{\min}+1)}{(\delta_z+1)\binom{q-1}{j}}
\le f^\alpha f^\beta,
\]

and therefore the tail-Hölder route proves (T-b).

## 0. Verdict

**REFUTED as stated.**

The printed branchwise scalar inequality has an exact admissible tame `c=1` counterexample at

\[
(n,q,j,\theta;a,\alpha;b,\beta)=(12,24,4,(4);2,(2);2,(2)),
\]

where its sole tail gives the ratio `36/35 > 1`.

The actually sufficient full-tail Hölder condition is

\[
\boxed{
\frac{\delta_{\min}+1}{\binom{q-1}{j}}
\sum_{z\in\operatorname{Rem}(\theta)}
\frac{f^{\tau_z}}{\delta_z+1}
\le f^\alpha f^\beta.}
\]

It contains **no factor `m`**. The fold factor `m`, the physical-fiber count, and both powers of `B_θ(q)` cancel against the target normalization.

The corrected summed condition is also false uniformly. Its first failure in the exact scan occurs at

\[
(18,36,6,(4,2);2,(2);4,(4)),
\qquad \text{ratio}=\frac{903}{620}>1.
\]

Therefore the plain tail-Hölder route does not prove (T-b) on all admissible tame sectors. This does **not** refute (T-b); it refutes this sufficient route. The actual (T-b) trace still passes the supplied large permutation-module gate at the `(9,18,3,(2,1);2,(2);1,(1))` sector by a wide certified margin.

`c>=2` identity-level carrier testing remains **UNTESTED**. The independent scalar scan includes exact LR multiplicities `c>=2`, but that is not an identity-level matrix residual.

**Rule-7 recommendation:** record `SE.denom.Phi.legal.trace.t1` as **REFUTED/DEAD as stated**, using the normal independent status process. Leave (T-b), the trace frontier, and DAG ancestors unchanged except by normal recomputation. This review makes no DAG edit.

## 1. Anchoring and notation

I use

\[
N_{\rm phys}:=\binom{n-1}{j},\qquad
N_{\rm qry}:=\binom{q-1}{j},\qquad
m:=\binom ja.
\]

This separates a source-level notation collision: `se_mphys2_20260719.md` uses `N` for `binom(n-1,j)`, while `se_eta_20260719.md` uses `N` for `binom(q-1,j)`.

The executable `se_trace_t1_independent_audit_20260720.py` imports none of the supplied eta or bigate programs. It independently implements partitions, hook dimensions, LR coefficients, admissibility checks, removable tails, and both scalar conditions. Supplied values were compared only after this construction was fixed. This documents constructional independence; a static artifact cannot cryptographically prove reading chronology.

## 2. Sector definitions and predicates

Let

\[
q=2n,\quad |\theta|=j,\quad a+b=j,\quad |\alpha|=a,\quad |\beta|=b,
\]

\[
\lambda=(q-j,\theta),\qquad
\kappa=(n-1-a,\alpha),\qquad
\nu=(n-b,\beta),
\]

\[
c=c_{\alpha,\beta}^{\theta}>0,\qquad d=f^\kappa f^\nu.
\]

The explicit attached audit code resolves “admissible” by requiring: `λ,κ,ν` are partitions; `q-j-1 >= θ_1`; `n-1-a >= θ_1`; `n-b >= θ_1`; positive LR coefficient; and the size/split identities above. “Tame” is `n >= 3j`.

For a removable corner in row `r`, of width `t=θ_r`,

\[
\tau_z=(q-j,\theta-z),\qquad
\delta_z=q-j-t+r,
\qquad
\delta_{\min}=\min_z\delta_z.
\]

The attached prose does not reproduce the full original definition of “strict.” The review therefore binds the claim to the explicit supplied admissibility/tame predicates. The counterexample satisfies them. Under the stronger interpretation `n>3j`, the printed claim still fails first at

\[
(13,26,4,(3,1);1,(1);3,(3)),
\]

with ratio `14/11`.

## 3. Rule-7(a): type, dimension, and normalization audit

Let

\[
\mathcal C=P_\xi V_\lambda,\qquad \dim\mathcal C=dc.
\]

For each physical colored choice `s`, `Π_{D_{h,s}}` is an orthogonal projector of rank `f^θ`. The number of physical colored choices is

\[
|\mathcal D_{a,b}|=
\binom{n-1}{a}\binom{n-1-a}{b}
=\binom ja\binom{n-1}{j}
=mN_{\rm phys}.
\]

Hence

\[
\mathscr X_h=\bigoplus_{s\in\mathcal D_{a,b}}\operatorname{Ran}\Pi_{D_{h,s}},
\qquad
\dim\mathscr X_h=mN_{\rm phys}f^\theta.
\]

Let `O=Ran(P_comp)` and `R=dim O`. The maps in scope are:

| Object | Type | Matrix dimensions |
|---|---|---:|
| `L_h` | `C -> X_h` | `m N_phys f^θ × dc` |
| `S_{h,z}` | `X_h -> O` | `R × m N_phys f^θ` |
| `B_{h,z}=S_{h,z}L_h` | `C -> O` | `R × dc` |
| `A_z=S_{h,z}*S_{h,z}` | `X_h -> X_h` | `m N_phys f^θ × m N_phys f^θ` |
| `D_h=L_hL_h*` | `X_h -> X_h` | same |
| `L_h*A_zL_h` | `C -> C` | `dc × dc` |

Thus every displayed composition is well-defined for arbitrary LR multiplicity `c`. The multiplicity occurs in the domain dimension of `L_h`; it does not occur explicitly in `X_h`, `S_{h,z}`, or the one-fiber scalar `η_z`.

The literal factorization and trace identities are

\[
B_{h,z}=S_{h,z}L_h:\mathcal C\to\mathcal O,
\]

\[
\|B_{h,z}\|_{\rm HS}^2
=\operatorname{Tr}_{\mathcal C}(L_h^*A_zL_h)
=\operatorname{Tr}_{\mathscr X_h}(A_zD_h),
\]

\[
\operatorname{Tr}(A_zD_h)
\le \|D_h\|\operatorname{Tr}(A_z)
=\|L_h\|^2\|S_{h,z}\|_{\rm HS}^2.
\]

The last line is finite-dimensional positive-matrix `S_∞–S_1` Hölder. No subgroup-normalizer conjugator is introduced in this route.

The inherited inputs are

\[
\|L_h\|^2\le B_\theta(q),
\]

\[
\|S_{h,z}\|_{\rm HS}^2=mN_{\rm phys}\eta_z,
\]

\[
\eta_z=
\frac{B_\theta(q)f^{\tau_z}}
{N_{\rm qry}(\delta_z+1)},
\qquad
B_\theta(q)=\frac{\binom qj f^\theta}{f^\lambda}.
\]

Therefore

\[
\|B_{h,z}\|_{\rm HS}^2
\le
\frac{B_\theta(q)^2mN_{\rm phys}f^{\tau_z}}
{N_{\rm qry}(\delta_z+1)}.
\]

The target is

\[
\sum_z\|B_{h,z}\|_{\rm HS}^2
\le
\frac{B_\theta(q)^2T}{\delta_{\min}+1},
\qquad
T=mN_{\rm phys}f^\alpha f^\beta.
\]

This audits the roles of all requested quantities: `m` is the color-fold multiplicity; `N_phys` counts uncolored physical sets; `N_qry` counts query-avoiding `j`-sets; `B_θ` occurs once in the input bound and once in `η_z`; `η_z` is the one-fiber branch trace; `τ_z` is the query-stabilizer tail shape; `δ_z+1` is the hook/frame divisor; and `δ_min+1` is the target tail weight.

## 4. Correct full-tail condition and the missing `m`

Summing the branch estimates gives

\[
\sum_z\|B_{h,z}\|_{\rm HS}^2
\le
\frac{B_\theta(q)^2mN_{\rm phys}}{N_{\rm qry}}
\sum_z\frac{f^{\tau_z}}{\delta_z+1}.
\]

Comparing with the target and cancelling the positive common factor `B_θ(q)^2 m N_phys` yields exactly

\[
\boxed{
\frac{\delta_{\min}+1}{N_{\rm qry}}
\sum_z\frac{f^{\tau_z}}{\delta_z+1}
\le f^\alpha f^\beta.}
\]

There is **no factor `m`**. The printed per-tail condition is not the direct scalar consequence of the Hölder chain. In addition, a “for every tail, therefore sum” argument needs an explicit allocation of the total tail budget; no such tail-count factor appears in the printed statement.

## 5. Exact nine `c=1` gates

The independently reconstructed tuples and printed tail ratios are:

| `n,j,θ` | split `(a,b)` | ratio |
|---|---:|---:|
| `3,1,(1)` | `(1,0)` | `1/5` |
| `3,1,(1)` | `(0,1)` | `1/5` |
| `4,1,(1)` | `(1,0)` | `1/7` |
| `4,1,(1)` | `(0,1)` | `1/7` |
| `4,2,(2)` | `(0,2)` | `2/7` |
| `4,2,(2)` | `(1,1)` | `4/7` |
| `4,2,(1,1)` | `(0,2)` | `2/7` |
| `4,2,(1,1)` | `(1,1)` | `4/7` |
| `4,2,(1,1)` | `(2,0)` | `2/7` |

All nine pass exactly. However, the five `n=4,j=2` rows have `n<3j`, so they are not tame under the supplied predicate. They are algebraic controls, not active-range tests. The independent hook/LR outputs agree with the supplied literal-matrix/formula values, corroborating the scalar formula but not testing a `c>=2` carrier identity.

## 6. Killer and larger-sector gates

### 6.1 Killer sector

For

\[
(9,18,3,(2,1);2,(2);1,(1)),
\]

`m=3`, `N_qry=680`, `f^αf^β=1`, and `δ_min=14`. The tails are

| `τ_z` | `δ_z` | `f^{τ_z}` | printed ratio |
|---|---:|---:|---:|
| `(15,1,1)` | 14 | 120 | `9/17` |
| `(15,2)` | 16 | 119 | `63/136` |

Both printed inequalities pass. The corrected summed ratio is `45/136 < 1`.

The supplied permutation-module executable was rerun. This is a reproducibility rerun of the proposer’s matrix construction, not a separately implemented matrix construction. It returned

\[
(T\text{-b})\in[0.3078630633,0.3102937233]
<\frac{578}{35}.
\]

Thus the actual trace passes here by a wide margin.

### 6.2 Minimal tame counterexample to the printed condition

Take

\[
(12,24,4,(4);2,(2);2,(2)).
\]

Then

\[
\lambda=(20,4),\quad \kappa=(9,2),\quad \nu=(10,2),
\]

\[
24-4-1=19\ge4,\quad 12-1-2=9\ge4,\quad 12-2=10\ge4,
\]

and `c_{(2),(2)}^{(4)}=1`; also `n=3j`, so the sector is tame. Its sole tail is

\[
\tau=(20,3),\qquad \delta=\delta_{\min}=17,
\qquad f^\tau=1518.
\]

With `m=6`, `N_qry=binom(23,4)=8855`, and `f^αf^β=1`, the printed ratio is

\[
\frac{6\cdot1518\cdot18}{18\cdot8855}
=\frac{36}{35}>1.
\]

This is the first failure under the executable’s natural ordering by `n`, then `j`, partitions, and splits. The corrected summed condition passes this sector with ratio `6/35`; hence this counterexample isolates the extra printed factor `m`.

### 6.3 Counterexample to the corrected summed condition

Take

\[
(18,36,6,(4,2);2,(2);4,(4)).
\]

Then

\[
\lambda=(30,4,2),\quad \kappa=(15,2),\quad \nu=(14,4),
\]

\[
36-6-1=29\ge4,\quad 18-1-2=15\ge4,\quad 18-4=14\ge4,
\]

`c_{(2),(4)}^{(4,2)}=1`, and `n=3j`. Here

\[
N_{\rm qry}=\binom{35}{6}=1623160,\qquad \delta_{\min}=27.
\]

The two tails are

\[
(\tau_1,\delta_1,f^{\tau_1})=((30,3,2),27,1374450),
\]

\[
(\tau_2,\delta_2,f^{\tau_2})=((30,4,1),30,1095633).
\]

Thus the corrected summed ratio is

\[
\frac{28}{\binom{35}{6}}
\left(\frac{1374450}{28}+\frac{1095633}{31}\right)
=\frac{105}{124}+\frac{189}{310}
=\frac{903}{620}>1.
\]

So even after removing the erroneous `m`, the full-tail scalar premise is false uniformly.

## 7. Materially larger exact scan

The independent exact scan covered all supplied-predicate admissible tame sectors with `3 <= n <= 36`, all `1 <= j <= floor(n/3)`, all partitions `θ,α,β`, and exact LR multiplicities.

- admissible tame sectors: **84,937**;
- scalar sectors with `c>=2`: **4,377**;
- failing printed tail branches: **198,325**;
- sectors failing the corrected summed condition: **50,594**.

The first strict-tame (`n>3j`) printed failure occurs at `(13,26,4,(3,1);1,(1);3,(3))`, ratio `14/11`. The first strict-tame corrected-sum failure occurs at `(19,38,6,(4,2);2,(2);4,(4))`, ratio `1035/748`.

These are exact integer/rational computations, not floating-point searches.

## 8. Failure-of-route versus failure of (T-b)

The counterexamples establish only:

1. the printed branchwise scalar inequality is false;
2. its claimed implication to a summed tail budget is not normalized correctly;
3. the correctly normalized plain-Hölder summed condition is also false uniformly.

They do **not** establish failure of

\[
\operatorname{Tr}\!\left(L_h^*\sum_zS_{h,z}^*S_{h,z}L_h\right)
\le \frac{B_\theta(q)^2T}{\delta_{\min}+1}.
\]

The Hölder estimate discards the spectral alignment/cancellation supplied by the physical `L_h` sandwich. The killer-sector permutation-module gate directly demonstrates this distinction.

## 9. Rule-7 checklist disposition

- **7a — Type audit:** every operator identity in scope is typed above, with dimensions including LR multiplicity `c`; no undefined normalizer/conjugator is used.
- **7b — Regime-complete identity gates:** all nine `c=1` scalar gates were reconstructed exactly; the killer and two larger active-range sectors were tested. Exact scalar LR scans include `c>=2`, but **`c>=2` identity-level carrier residual remains UNTESTED** and is not relabeled as tested.
- **7c — Anchoring ban:** the review uses its own `N_phys/N_qry` notation and an independent hook/LR implementation importing no proposer audit code. Coincidence with standard hook/LR formulas is unavoidable and explicitly declared.
- **7d — No frozen-input immunity:** the inherited all-`c` input norm/fold/eta package retains its existing `CERTIFIED*` caveat. The refutation itself is already complete at `c=1` and does not require extending that package to `c>=2` identity level.
- **7e — Failure-mode diversity:** the audit checks the extra `m`, the two incompatible meanings of `N`, all dimensions, full tail sums rather than maxima, `δ_z` versus `δ_z+1`, active-range predicates, and value-versus-formula separation.
- **7f — Value/formula decoupling:** the scalar counterexamples come from an independent exact construction. The large matrix result is only a rerun of the supplied proposer executable and is labeled as such.
- **7g — Quantifier hygiene:** admissible and tame are resolved to the explicit supplied predicates. “Strict” is not fully defined in the attached foundations, so both boundary-tame and `n>3j` counterexamples are reported.

## 10. Final status recommendation

**Reviewed claim:** REFUTED.  
**Recommended node disposition:** `SE.denom.Phi.legal.trace.t1` -> **REFUTED/DEAD as stated**, after the project’s normal archival/status procedure.  
**(T-b):** not refuted; remains a separate conjectured trace target.  
**`c>=2` identity-level:** **UNTESTED**.  
**DAG edits:** none performed or claimed.

## 11. Reproduction

Independent exact scan:

```text
python se_trace_t1_independent_audit_20260720.py \
  --json se_trace_t1_independent_audit_20260720.json \
  --log se_trace_t1_independent_audit_20260720.log \
  --n-max 36
```

Supplied large-gate rerun:

```text
python bigate_permutation_module(1).py \
  --controls --secondary \
  --out reviewer_bigate_results.json \
  --log reviewer_bigate.log
```
