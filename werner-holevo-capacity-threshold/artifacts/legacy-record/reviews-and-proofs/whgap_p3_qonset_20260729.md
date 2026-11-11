# WHGAP P3 q-positive onset execution artifact (2026-07-29)

Target node: `WHGAP.qpositive-onset`

Role: executor/proposer
Status ceiling: `NUMERICAL`; `pending-review:` applies to every result below.

## Outcome

Gate G0 passed. The maximally mixed coherent information has a unique zero

\[
x_1=0.3909102320761813234827218531342\ldots,
\]

with a directed-rounding rational bracket of width \(10^{-31}\). The full-input S1 scan found
an input with positive coherent information at \(x=0.3915>x_1\). A nearby rational rank-two
input was then checked using exact spectra and mpmath interval arithmetic:

\[
I_c(\rho,783/2000)>
\frac{1449965437710479183}{5000000000000000000000000}
>0\quad\text{bits}.
\]

Thus the pre-registered interpretation is **G2(b)**: the certified \(Q>0\) region extends beyond
the maximally mixed crossing. This is proposer-authored exact-arithmetic-grade evidence awaiting
independent rule-7 review; it is not a completion-tier claim.

S2 independently found that the maximally mixed input remains a local maximum beyond \(x_1\) and
loses local maximality only at

\[
x_H=0.4162325706014828112675191458355\ldots>x_1.
\]

S3 completed its bounded two-letter search in 757.297 seconds, below the 20-minute hard cap, and
found no value above the pre-registered \(10^{-7}\)-bit MAJOR threshold.

## G0: exact calibration

All entropies below are in bits. Expressions first written using natural logarithms are divided by
\(\ln 2\).

### D1: identity input

For \(\pi=I_3/3\), exact SymPy evaluation with the frozen Kraus convention gives

\[
\Lambda_x(\pi)=\pi,\qquad
\Lambda_x^c(\pi)=\operatorname{diag}(1-x,x/3,x/3,x/3).
\]

Consequently,

\[
I_c(\pi,x)
=\log_2 3+(1-x)\log_2(1-x)+x\log_2(x/3).
\]

### D2: monotonicity and uniqueness

Exact differentiation gives

\[
\frac{d}{dx}I_c(\pi,x)=
\log_2\!\left(\frac{x}{3(1-x)}\right).
\]

It is strictly negative for \(0<x<3/4\). Since
\(I_c(\pi,0)=\log_2 3>0\) and \(I_c(\pi,3/4)=-1/4<0\), there is exactly one root
\(x_1\in(0,3/4)\).

### D3: directed-rounding root certificate

At mpmath.iv precision 60 decimal digits:

\[
\begin{aligned}
a&=\frac{3909102320761813234827218531341}{10^{31}},\\
b&=\frac{1954551160380906617413609265671}{5\cdot10^{30}},\\
b-a&=10^{-31}.
\end{aligned}
\]

The computed enclosures were

\[
I_c(\pi,a)\in
[2.2053778267312532193824580768964{\times}10^{-31},
 2.2053778267312532193824580769044{\times}10^{-31}]
\]

and

\[
I_c(\pi,b)\in
[-1.940219516785425435438747068650{\times}10^{-33},
 -1.940219516785425435438747067751{\times}10^{-33}].
\]

Therefore \(a<x_1<b\) with directed-rounding certified signs.

### D4: interval positivity certificates

| \(x\) | interval lower endpoint for \(I_c(\pi,x)\) (bits) | positive rational lower bound |
|---:|---:|---:|
| \(1/4\) | 0.3774437510817342721806084159217247631 | \(2359023444260839201128802599510779769623260072117/6250000000000000000000000000000000000000000000000\) |
| \(1/3\) | 0.1383458330929479395154203520173944971 | \(55338333237179175806168140806957798832024745641/400000000000000000000000000000000000000000000000\) |
| \(39/100\) | 0.002027576934818056915900376150140742919 | \(25344711685225711448754701876759286492324431277/12500000000000000000000000000000000000000000000000\) |

By the frozen Lloyd–Shor–Devetak lower-bound principle
\(Q(\Lambda_x)\geq Q_1(\Lambda_x)\geq I_c(\pi,x)\), each row certifies
\(Q(\Lambda_x)>0\) at that rational point.

The first calibration attempt is retained in `calibration.log`: D1 passed, but SymPy declined to
simplify the D2 logarithm identity under default branch rules. The rerun used exact forced log
expansion for positive real \(x\) and passed; no numerical claim was changed.

## S1: full-input single-letter ceiling scan

The scan used the full parameterization
\(\rho=LL^\dagger/\operatorname{Tr}(LL^\dagger)\), with \(L\) a complex \(3\times3\)
lower-triangular matrix (nine real coordinates, full coverage of qutrit density matrices).
Every grid point used exactly 200 restarts: \(\pi\); 40 starts sweeping the RK24 family
\(\operatorname{diag}(s,1-2s,s)\); 80 random full-rank starts; and 79 random near-pure starts.
L-BFGS-B used at most 300 iterations. Values within \(10^{-9}\) of zero are classified as the
exact pure-state floor, since pure inputs have isospectral channel and environment outputs.

| \(x\) | best \(I_c\) (bits) | \(I_c(\pi)\) (bits) | best spectrum | character | successful exits |
|---:|---:|---:|---|---|---:|
| \(2/5\) | \(1.1102{\times}10^{-14}\) | -0.0199730940 | \((7.46{\times}10^{-17},4.01{\times}10^{-15},1-4.2{\times}10^{-15})\) | pure floor | 200/200 |
| \(21/50\) | \(1.1657{\times}10^{-14}\) | -0.0621756446 | \((4.16{\times}10^{-16},3.61{\times}10^{-15},1-3.8{\times}10^{-15})\) | pure floor | 198/200 |
| \(11/25\) | \(8.4377{\times}10^{-15}\) | -0.1020085208 | \((7.52{\times}10^{-16},3.38{\times}10^{-15},1-4.0{\times}10^{-15})\) | pure floor | 200/200 |
| \(23/50\) | \(4.6629{\times}10^{-15}\) | -0.1394986884 | \((2.35{\times}10^{-17},2.06{\times}10^{-15},1-2.4{\times}10^{-15})\) | pure floor | 200/200 |
| \(12/25\) | \(4.2188{\times}10^{-15}\) | -0.1746650356 | \((0,3.54{\times}10^{-15},1-3.6{\times}10^{-15})\) | pure floor | 197/200 |
| \(49/100\) | \(5.3291{\times}10^{-15}\) | -0.1913805664 | \((5.07{\times}10^{-16},2.50{\times}10^{-15},1-2.4{\times}10^{-15})\) | pure floor | 200/200 |
| \(499/1000\) | \(4.2188{\times}10^{-15}\) | -0.2059309017 | \((0,3.43{\times}10^{-15},1-3.8{\times}10^{-15})\) | pure floor | 200/200 |
| \(77/200\) | 0.01325498712 | 0.01325498712 | \((0.3333333304,0.3333333334,0.3333333362)\) | maximally mixed | 199/200 |
| \(783/2000\) | \(2.9798322{\times}10^{-7}\) | -0.00131105031 | \((9.45{\times}10^{-17},1.286675{\times}10^{-5},0.9999871332)\) | rank-two candidate | 200/200 |
| \(79/200\) | \(8.8404{\times}10^{-11}\) | -0.00904822276 | \((3.83{\times}10^{-15},6.06{\times}10^{-9},0.9999999939)\) | pure floor | 200/200 |

The \(x=783/2000\) numerical candidate was rationalized with
\(\epsilon=1/100000\):

\[
\rho_\epsilon=
\begin{pmatrix}
0&0&0\\
0&1/2&-i(1/2-\epsilon)\\
0&i(1/2-\epsilon)&1/2
\end{pmatrix},
\qquad
\operatorname{spec}\rho_\epsilon=(0,\epsilon,1-\epsilon).
\]

Exact SymPy spectra are

\[
\operatorname{spec}\Lambda_x(\rho_\epsilon)=
\left(
\frac{783}{4000},
\frac{321696783}{400000000},
\frac{3217}{400000000}
\right)
\]

and

\[
\operatorname{spec}\Lambda_x^c(\rho_\epsilon)=
\left(
\frac{3217}{8000}\mathbin{-}\frac{\sqrt{6467990044705822}}{200000000},
\frac{3217}{8000}\mathbin{+}\frac{\sqrt{6467990044705822}}{200000000},
\frac{78299217}{400000000},
\frac{783}{400000000}
\right).
\]

All entries are positive and sum to one. Interval evaluation at 80 decimal digits gives

\[
I_c(\rho_\epsilon,783/2000)
\in[0.00000028999308754209583665821303434210409412835388031921374063357196791052759253524926,
\ 0.00000028999308754209583665821303434210409412835388031921374063357196791052759258479759],
\]

and the positive rational lower bound stated in the Outcome. This is an independent evaluation
of the rationalized candidate, not an interval wrapping of the optimizer’s floating-point value.
The first certificate-formatting log is retained: interval evaluation used 80 digits, but endpoint
conversion inherited mpmath’s 15-digit scalar default. The rerun set scalar precision to 120 digits
before extracting the 80-digit directed endpoints; only the rerun bound is cited.

S1 also tests pre-registered G2(c): below \(x_1\), the \(x=77/200\) optimum agrees with
\(I_c(\pi)\) to displayed precision, so this scan found no contradiction of RK24 on that side.

## S2: Hessian at the maximally mixed input

For a traceless Hermitian perturbation \(\Delta\), \(O(3)\) covariance decomposes the tangent
space into real-symmetric traceless perturbations (dimension five) and imaginary-antisymmetric
perturbations (dimension three). With

\[
\left.\frac{d^2}{dt^2}I_c(\pi+t\Delta)\right|_{t=0}
=C_{\rm sector}(x)\operatorname{Tr}(\Delta^2),
\]

exact entropy differentials give

\[
C_{\rm sym}(x)=
-\frac{3(x-1)(9x-4)}{4\ln2},
\]

whose first sign change is \(x=4/9\), and

\[
C_{\rm asym}(x)=
-\frac{3(x-1)
\left(4x^2+8x\ln x-8x\ln(3-3x)-19x+12\right)}
{4(4x-3)\ln2}.
\]

The first local-maximality loss is therefore the antisymmetric-sector zero. Its certified bracket is

\[
\frac{832465141202965622535038291671}{2\cdot10^{30}}
<x_H<
\frac{1040581426503707028168797864589}{25\cdot10^{29}},
\]

again of width \(10^{-31}\), with the numerator of \(C_{\rm asym}\) strictly negative at the
left endpoint and strictly positive at the right endpoint.

For uniqueness, put \(r=3(1-x)/x\). On \(0<x<4/9\), \(r>15/4\), and the sign is the sign of

\[
F(r)=8(r+3)\ln r-(4r+9)(r-1).
\]

Here

\[
F''(r)=-8(r^2-r+3)/r^2<0
\]

and
\(F'(15/4)=8\ln(15/4)-103/5<16-103/5<0\), using
\(\ln(15/4)<\ln4<2\). Thus \(F\) is strictly decreasing in \(r\), while \(r\) is strictly
decreasing in \(x\); the certified sign bracket supplies the unique zero. The mismatch
\(x_H-x_1\approx0.02532233852530149\) is a finding: crossing zero coherent information and losing
local maximality are different events.

## S3: two-letter probe

At each of \(x\in\{21/50,23/50,49/100\}\), the probe searched:

- the full nine-dimensional computational-basis diagonal simplex from 40 starts;
- 50 correlated directions away from \(\pi\otimes\pi\), including maximally correlated and
  antisymmetric directions;
- 50 random full-parameter \(9\times9\) density-matrix restarts using an 81-real-coordinate
  Cholesky parameterization (25 Wishart and 25 near-pure starts).

| \(x\) | diagonal best | correlated best | full-parameter best | \(2\times\) S1 floor | MAJOR \(>10^{-7}\)? |
|---:|---:|---:|---:|---:|---|
| \(21/50\) | \(7.2831{\times}10^{-14}\) | \(8.8818{\times}10^{-16}\) | \(2.0783{\times}10^{-13}\) | \(2.3315{\times}10^{-14}\) | no |
| \(23/50\) | \(8.9262{\times}10^{-14}\) | \(8.8818{\times}10^{-16}\) | \(1.6964{\times}10^{-13}\) | \(9.3259{\times}10^{-15}\) | no |
| \(49/100\) | \(1.1902{\times}10^{-13}\) | \(1.3323{\times}10^{-15}\) | \(1.3678{\times}10^{-13}\) | \(1.0658{\times}10^{-14}\) | no |

These values are numerical pure-state-scale residuals, not positive findings. The bounded-null
statement is limited to the listed families, restart counts, blocklength two, and 757.297-second
run; it is not a proof that two-letter coherent information is nonpositive.

## Pre-registered G2 interpretation

**G2(b) applies.** A certified single-letter value \(I_c>0\) was obtained at
\(x=783/2000>x_1\), so the certified \(Q>0\) region extends beyond the maximally mixed crossing.
This execution certifies a point (and, by continuity, some neighborhood), not the exact onset
boundary. The S3 probe is null within its pre-registered budget and families. The strip between
the new certified neighborhood and \(1/2\) remains open.

## Reproduction and provenance

Pinned interpreter used for every Python invocation:
`C:<home>/cpython3119/python.exe` (CPython 3.11.9).

Commands:

```powershell
& 'C:<home>/cpython3119/python.exe' tools/whgap_p3_calibration.py
& 'C:<home>/cpython3119/python.exe' tools/whgap_p3_hessian.py
& 'C:<home>/cpython3119/python.exe' tools/whgap_p3_single_letter.py
& 'C:<home>/cpython3119/python.exe' tools/whgap_p3_interval_candidate.py
& 'C:<home>/cpython3119/python.exe' tools/whgap_p3_two_letter.py
```

Scripts:

- `tools/whgap_p3_calibration.py`
- `tools/whgap_p3_hessian.py`
- `tools/whgap_p3_single_letter.py`
- `tools/whgap_p3_interval_candidate.py`
- `tools/whgap_p3_two_letter.py`

Raw logs and generated JSON certificates are under
`artifacts/logs_whgap_p3_20260729/`. The authoritative script/log digests are in that directory’s
`SHA256SUMS.txt`.

## Review boundary

`pending-review:` Exact symbolic identities, rational input/output/environment spectra, interval
signs, and rational lower bounds are exact-arithmetic-grade proposer evidence but await a fresh
rule-7 review. S1 and S3 optimizer maxima/null statements are numerical-only. No
`CERTIFIED*`, `PROVED`, or `REFUTED` status is claimed here.

