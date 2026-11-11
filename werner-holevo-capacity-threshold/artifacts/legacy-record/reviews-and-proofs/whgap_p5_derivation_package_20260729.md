# WHGAP P5 paper-grade derivation package (2026-07-29)

Purpose: exposition data for the R2-PROVED certificate core at node
`WHGAP.signed-lift-extension`. This package makes no new mathematical claim and
changes no proof-DAG status. All algebra below was generated and verified with exact
SymPy arithmetic under the frozen P2 conventions.

## Conventions and residual chart

We use row-major \(E_{ij}\leftrightarrow |i\rangle|j\rangle\), the
unnormalized input-leg-first Choi matrix, and \(k^2=x(1-x)/2\). Our direct
residual chart is

\[
q=\frac{d}{2k},\qquad s_1=\frac{(1-x)(1-p)}{x},\qquad
s_2=\frac{2-x-4d}{x}.
\]

Thus \(p=1/3,\ d=2(1-x)/3\) is exactly
\(s_1=2(1-x)/(3x),\ s_2=(5x-2)/(3x)\).

## P5.1 — entrywise closed form

For row index `(i,b,b')` and column index `(j,r,s)`, the exact fit gives

\[
\begin{aligned}
C_{(i,b,b'),(j,r,s)}={}&
\left(\frac{- d p - 4 d x + 3 d + 2 p x^{2} - 4 p x + 2 p - 2 x^{2} + 4 x - 2}{2 x}\right)\delta_{ib} \delta_{b'j} \delta_{rs} \\
&\quad + \left(- \frac{d \left(9 d x - 8 d + 2 x^{2} - 6 x + 4\right)}{4 x \left(x - 1\right)}\right)\delta_{ib} \delta_{b'r} \delta_{js} \\
&\quad + \left(- \frac{- 9 d^{2} x + 8 d^{2} - 8 d x^{2} + 16 d x - 8 d + 4 x^{3} - 8 x^{2} + 4 x}{4 x \left(x - 1\right)}\right)\delta_{ib} \delta_{b's} \delta_{jr} \\
&\quad + \left(\frac{d p + 4 d x - 3 d + p x^{2} - p x - x^{2} + x}{2 x}\right)\delta_{ib'} \delta_{bj} \delta_{rs} \\
&\quad + \left(- \frac{d \left(- 9 d x + 8 d + 4 x^{2} - 4 x\right)}{4 x \left(x - 1\right)}\right)\delta_{ib'} \delta_{br} \delta_{js} \\
&\quad + \left(- \frac{d \left(9 d x - 8 d + 2 x^{2} - 6 x + 4\right)}{4 x \left(x - 1\right)}\right)\delta_{ib'} \delta_{bs} \delta_{jr} \\
&\quad + \left(- \frac{\left(x - 1\right) \left(- p^{2} + p x - 2 x + 1\right)}{x}\right)\delta_{ij} \delta_{bb'} \delta_{rs} \\
&\quad + \left(- \frac{9 d^{2} + 4 d x - 8 d + 4 x^{2} - 8 x + 4}{2 x}\right)\delta_{ij} \delta_{br} \delta_{b's} \\
&\quad + \left(- \frac{- 9 d^{2} - 4 d x + 8 d + 4 x^{2} - 4 x}{2 x}\right)\delta_{ij} \delta_{bs} \delta_{b'r} \\
&\quad + \left(\frac{d p + 4 d x - 3 d + p x^{2} - p x - x^{2} + x}{2 x}\right)\delta_{ir} \delta_{bb'} \delta_{js} \\
&\quad + \left(- \frac{2 d \left(2 x - 1\right)}{x}\right)\delta_{ir} \delta_{bj} \delta_{b's} \\
&\quad + \left(\frac{- d x + 2 d + 2 x^{2} - 2 x}{2 x}\right)\delta_{ir} \delta_{bs} \delta_{b'j} \\
&\quad + \left(\frac{- d p - 4 d x + 3 d + 2 p x^{2} - 4 p x + 2 p - 2 x^{2} + 4 x - 2}{2 x}\right)\delta_{is} \delta_{bb'} \delta_{jr} \\
&\quad + \left(\frac{- d x + 2 d + 2 x^{2} - 2 x}{2 x}\right)\delta_{is} \delta_{bj} \delta_{b'r} \\
&\quad + \left(\frac{5 d x - 4 d + 2 x^{2} - 4 x + 2}{x}\right)\delta_{is} \delta_{br} \delta_{b'j}
.
\end{aligned}
\]

The coefficient table, including the forced-point specialization, is:

| pattern | delta product | `c_k(x;p,d)` | forced coefficient |
|---|---|---|---|
| P1 | $\delta_{ib} \delta_{b'j} \delta_{rs}$ | $\frac{- d p - 4 d x + 3 d + 2 p x^{2} - 4 p x + 2 p - 2 x^{2} + 4 x - 2}{2 x}$ | $\frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}$ |
| P2 | $\delta_{ib} \delta_{b'r} \delta_{js}$ | $- \frac{d \left(9 d x - 8 d + 2 x^{2} - 6 x + 4\right)}{4 x \left(x - 1\right)}$ | $- \frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}$ |
| P3 | $\delta_{ib} \delta_{b's} \delta_{jr}$ | $- \frac{- 9 d^{2} x + 8 d^{2} - 8 d x^{2} + 16 d x - 8 d + 4 x^{3} - 8 x^{2} + 4 x}{4 x \left(x - 1\right)}$ | $- \frac{4 \left(x - 1\right) \left(3 x - 1\right)}{9 x}$ |
| P4 | $\delta_{ib'} \delta_{bj} \delta_{rs}$ | $\frac{d p + 4 d x - 3 d + p x^{2} - p x - x^{2} + x}{2 x}$ | $- \frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}$ |
| P5 | $\delta_{ib'} \delta_{br} \delta_{js}$ | $- \frac{d \left(- 9 d x + 8 d + 4 x^{2} - 4 x\right)}{4 x \left(x - 1\right)}$ | $\frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}$ |
| P6 | $\delta_{ib'} \delta_{bs} \delta_{jr}$ | $- \frac{d \left(9 d x - 8 d + 2 x^{2} - 6 x + 4\right)}{4 x \left(x - 1\right)}$ | $- \frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}$ |
| P7 | $\delta_{ij} \delta_{bb'} \delta_{rs}$ | $- \frac{\left(x - 1\right) \left(- p^{2} + p x - 2 x + 1\right)}{x}$ | $\frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}$ |
| P8 | $\delta_{ij} \delta_{br} \delta_{b's}$ | $- \frac{9 d^{2} + 4 d x - 8 d + 4 x^{2} - 8 x + 4}{2 x}$ | $- \frac{4 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |
| P9 | $\delta_{ij} \delta_{bs} \delta_{b'r}$ | $- \frac{- 9 d^{2} - 4 d x + 8 d + 4 x^{2} - 4 x}{2 x}$ | $- \frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |
| P10 | $\delta_{ir} \delta_{bb'} \delta_{js}$ | $\frac{d p + 4 d x - 3 d + p x^{2} - p x - x^{2} + x}{2 x}$ | $- \frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}$ |
| P11 | $\delta_{ir} \delta_{bj} \delta_{b's}$ | $- \frac{2 d \left(2 x - 1\right)}{x}$ | $\frac{4 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |
| P12 | $\delta_{ir} \delta_{bs} \delta_{b'j}$ | $\frac{- d x + 2 d + 2 x^{2} - 2 x}{2 x}$ | $\frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |
| P13 | $\delta_{is} \delta_{bb'} \delta_{jr}$ | $\frac{- d p - 4 d x + 3 d + 2 p x^{2} - 4 p x + 2 p - 2 x^{2} + 4 x - 2}{2 x}$ | $\frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}$ |
| P14 | $\delta_{is} \delta_{bj} \delta_{b'r}$ | $\frac{- d x + 2 d + 2 x^{2} - 2 x}{2 x}$ | $\frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |
| P15 | $\delta_{is} \delta_{br} \delta_{b'j}$ | $\frac{5 d x - 4 d + 2 x^{2} - 4 x + 2}{x}$ | $- \frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}$ |

At the forced point the same formula specializes to

\[
\begin{aligned}
C^\star_{(i,b,b'),(j,r,s)}={}&
\left(\frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\right)\delta_{ib} \delta_{b'j} \delta_{rs} \\
&\quad + \left(- \frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\right)\delta_{ib} \delta_{b'r} \delta_{js} \\
&\quad + \left(- \frac{4 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\right)\delta_{ib} \delta_{b's} \delta_{jr} \\
&\quad + \left(- \frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}\right)\delta_{ib'} \delta_{bj} \delta_{rs} \\
&\quad + \left(\frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}\right)\delta_{ib'} \delta_{br} \delta_{js} \\
&\quad + \left(- \frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\right)\delta_{ib'} \delta_{bs} \delta_{jr} \\
&\quad + \left(\frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}\right)\delta_{ij} \delta_{bb'} \delta_{rs} \\
&\quad + \left(- \frac{4 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{ij} \delta_{br} \delta_{b's} \\
&\quad + \left(- \frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{ij} \delta_{bs} \delta_{b'r} \\
&\quad + \left(- \frac{\left(x - 1\right) \left(15 x - 8\right)}{9 x}\right)\delta_{ir} \delta_{bb'} \delta_{js} \\
&\quad + \left(\frac{4 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{ir} \delta_{bj} \delta_{b's} \\
&\quad + \left(\frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{ir} \delta_{bs} \delta_{b'j} \\
&\quad + \left(\frac{2 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\right)\delta_{is} \delta_{bb'} \delta_{jr} \\
&\quad + \left(\frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{is} \delta_{bj} \delta_{b'r} \\
&\quad + \left(- \frac{2 \left(x - 1\right) \left(2 x - 1\right)}{3 x}\right)\delta_{is} \delta_{br} \delta_{b'j}
.
\end{aligned}
\]

**GATE V1: PASS.** The 15-pattern matrix has rank 15; the formula
reproduces all 729 entries symbolically both in the general residual family and
at the forced point. Runtime: 4.192447 s.

## P5.2 — displayed forcing identities

For \(v_p=|0\rangle_A\sum_{a=0}^2|a,a\rangle\), the contributing ordered pairs are:

| left | right | Choi entry | active patterns |
|---|---|---|---|
| (0, 0, 0) | (0, 0, 0) | $\frac{\left(p - 1\right) \left(x - 1\right) \left(p + 2 x - 1\right)}{x}$ | P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15 |
| (0, 0, 0) | (0, 1, 1) | $\frac{\left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{2 x}$ | P1, P4, P7 |
| (0, 0, 0) | (0, 2, 2) | $\frac{\left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{2 x}$ | P1, P4, P7 |
| (0, 1, 1) | (0, 0, 0) | $\frac{\left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{2 x}$ | P7, P10, P13 |
| (0, 1, 1) | (0, 1, 1) | $- \frac{\left(x - 1\right) \left(- p^{2} + p x + 2 x - 1\right)}{x}$ | P7, P8, P9 |
| (0, 1, 1) | (0, 2, 2) | $- \frac{\left(x - 1\right) \left(- p^{2} + p x - 2 x + 1\right)}{x}$ | P7 |
| (0, 2, 2) | (0, 0, 0) | $\frac{\left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{2 x}$ | P7, P10, P13 |
| (0, 2, 2) | (0, 1, 1) | $- \frac{\left(x - 1\right) \left(- p^{2} + p x - 2 x + 1\right)}{x}$ | P7 |
| (0, 2, 2) | (0, 2, 2) | $- \frac{\left(x - 1\right) \left(- p^{2} + p x + 2 x - 1\right)}{x}$ | P7, P8, P9 |

Grouping equal entries and summing gives

\[
\begin{aligned}
\langle v_p,Cv_p\rangle
&=1\left(\frac{\left(p - 1\right) \left(x - 1\right) \left(p + 2 x - 1\right)}{x}\right) + 4\left(\frac{\left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{2 x}\right) + 2\left(\frac{\left(1 - x\right) \left(- p^{2} + p x + 2 x - 1\right)}{x}\right) + 2\left(\frac{\left(1 - x\right) \left(- p^{2} + p x - 2 x + 1\right)}{x}\right)\\
&=\frac{\left(3 p - 1\right)^{2} \left(x - 1\right)}{x}.
\end{aligned}
\]

For \(v_d=|0,1,2\rangle+|1,0,2\rangle\), the contributing ordered pairs are:

| left | right | Choi entry | active patterns |
|---|---|---|---|
| (0, 1, 2) | (0, 1, 2) | $- \frac{9 d^{2} + 4 d x - 8 d + 4 x^{2} - 8 x + 4}{2 x}$ | P8 |
| (0, 1, 2) | (1, 0, 2) | $- \frac{2 d \left(2 x - 1\right)}{x}$ | P11 |
| (1, 0, 2) | (0, 1, 2) | $- \frac{2 d \left(2 x - 1\right)}{x}$ | P11 |
| (1, 0, 2) | (1, 0, 2) | $- \frac{9 d^{2} + 4 d x - 8 d + 4 x^{2} - 8 x + 4}{2 x}$ | P8 |

Grouping equal entries and summing gives

\[
\begin{aligned}
\langle v_d,Cv_d\rangle
&=2\left(\frac{- 9 d^{2} - 4 d x + 8 d - 4 x^{2} + 8 x - 4}{2 x}\right) + 2\left(- \frac{2 d \left(2 x - 1\right)}{x}\right)\\
&=- \frac{\left(3 d + 2 x - 2\right)^{2}}{x}.
\end{aligned}
\]

**GATE V2: PASS.** Every listed entry was independently evaluated from the
15-pattern formula and the direct 27-by-27 Choi matrix; each displayed sum
simplifies symbolically to the commissioned square.

## P5.3 — integer spin bases, Gram matrices, and reduced blocks

The multiplicity dimensions are \(m_0,m_1,m_2,m_3=(1,3,2,1)\), so
\(\sum_jm_j(2j+1)=1+9+10+7=27\). The integer columns are:

### Spin \(j=0\)

\[u_{0,1}=|0,1,2\rangle - |0,2,1\rangle - |1,0,2\rangle + |1,2,0\rangle + |2,0,1\rangle - |2,1,0\rangle.\]

\[G_0=U_0^{\mathsf T}U_0=\left[\begin{matrix}6\end{matrix}\right].\]

\[B_0(x,p,d)=U_0^{\mathsf T}CU_0=\left[\begin{matrix}- \frac{6 \left(3 d - 2\right) \left(3 d + 2 x - 2\right)}{x}\end{matrix}\right].\]

\[B_0^\star(x)=\left[\begin{matrix}0\end{matrix}\right].\]

### Spin \(j=1\)

\[u_{1,1}=3|0,0,0\rangle + |0,1,1\rangle + |0,2,2\rangle + |1,0,1\rangle + |1,1,0\rangle + |2,0,2\rangle + |2,2,0\rangle.\]
\[u_{1,2}=2|0,0,0\rangle + 4|0,1,1\rangle + 4|0,2,2\rangle - |1,0,1\rangle - |1,1,0\rangle - |2,0,2\rangle - |2,2,0\rangle.\]
\[u_{1,3}=2|0,0,0\rangle - |0,1,1\rangle - |0,2,2\rangle + 4|1,0,1\rangle - |1,1,0\rangle + 4|2,0,2\rangle - |2,2,0\rangle.\]

\[G_1=U_1^{\mathsf T}U_1=\left[\begin{matrix}15 & 10 & 10\\10 & 40 & -10\\10 & -10 & 40\end{matrix}\right].\]

\[B_1(x,p,d)=U_1^{\mathsf T}CU_1=\left[\begin{matrix}\frac{25 \left(p - 1\right) \left(x - 1\right) \left(p + 2 x - 1\right)}{x} & \frac{25 \left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{x} & \frac{25 \left(d p + d x - d + p x^{2} - p x - x^{2} + x\right)}{x}\\\frac{25 \left(x - 1\right) \left(2 p^{2} + p x - 2 p + x\right)}{x} & - \frac{100 p \left(- p + x\right) \left(x - 1\right)}{x} & \frac{25 \left(2 d p - d x + 2 p x^{2} - 2 p x\right)}{x}\\\frac{25 \left(d p + d x - d + p x^{2} - p x - x^{2} + x\right)}{x} & \frac{25 \left(2 d p - d x + 2 p x^{2} - 2 p x\right)}{x} & \frac{25 d \left(d + 2 x^{2} - 2 x\right)}{x \left(x - 1\right)}\end{matrix}\right].\]

\[B_1^\star(x)=\left[\begin{matrix}- \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & - \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\\\frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & - \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\\- \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x} & - \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\end{matrix}\right].\]

### Spin \(j=2\)

\[u_{2,1}=2|0,1,2\rangle - 2|0,2,1\rangle + |1,0,2\rangle - |1,2,0\rangle - |2,0,1\rangle + |2,1,0\rangle.\]
\[u_{2,2}=|0,1,2\rangle - |0,2,1\rangle + 2|1,0,2\rangle + |1,2,0\rangle - 2|2,0,1\rangle - |2,1,0\rangle.\]

\[G_2=U_2^{\mathsf T}U_2=\left[\begin{matrix}12 & 6\\6 & 12\end{matrix}\right].\]

\[B_2(x,p,d)=U_2^{\mathsf T}CU_2=\left[\begin{matrix}- \frac{12 \left(3 d - 1\right) \left(3 d + x - 1\right)}{x} & - \frac{3 \left(18 d^{2} + 33 d x - 30 d + 6 x^{2} - 14 x + 8\right)}{x}\\- \frac{3 \left(18 d^{2} + 33 d x - 30 d + 6 x^{2} - 14 x + 8\right)}{x} & - \frac{3 \left(3 d + 4 x - 4\right) \left(3 d + 6 x - 4\right)}{x}\end{matrix}\right].\]

\[B_2^\star(x)=\left[\begin{matrix}- \frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x} & \frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x}\\\frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x} & - \frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x}\end{matrix}\right].\]

### Spin \(j=3\)

\[u_{3,1}=2|0,0,0\rangle - |0,1,1\rangle - |0,2,2\rangle - |1,0,1\rangle - |1,1,0\rangle - |2,0,2\rangle - |2,2,0\rangle.\]

\[G_3=U_3^{\mathsf T}U_3=\left[\begin{matrix}10\end{matrix}\right].\]

\[B_3(x,p,d)=U_3^{\mathsf T}CU_3=\left[\begin{matrix}0\end{matrix}\right].\]

\[B_3^\star(x)=\left[\begin{matrix}0\end{matrix}\right].\]

For each column, the exact Casimir check is
\(\mathcal L^2U_j=j(j+1)U_j\); every generator commutes with \(C\).
With the nonorthonormal integer bases, the exact normalized pencil identity is

\[
\det(zI_{27}-C)
=\prod_{j=0}^3
\left(\frac{\det(zG_j-B_j)}{\det G_j}\right)^{2j+1}.
\]

Here \(U_j\) is exactly the full zero-weight multiplicity space: the script
also checks \(L_0U_j=0\). Since \(C\) commutes with all three generators,
Schur's lemma replicates the displayed multiplicity-space action over all
\(2j+1\) weights. This proves the pencil identity symbolically.

The generic direct SymPy 27-by-27 `charpoly` call was stopped at the mandated
15-minute single-step limit. Under the commissioned fallback rule, the same
identity was also checked by direct exact 27-by-27 characteristic polynomials
at these five general residual-chart points:

| x | p | d | direct check |
|---|---|---|---|
| 1/2 | 1/3 | 1/3 | PASS |
| 2/3 | 2/5 | 1/7 | PASS |
| 3/4 | -1/5 | 2/9 | PASS |
| 2/5 | 4/7 | -1/6 | PASS |
| 5/6 | 7/11 | 3/10 | PASS |

**GATE V3: PASS (documented fallback).** The dimension sum, zero-weight and
Casimir equations, all generator commutators, the exact isotypic pencil proof,
and five direct exact 27-by-27 characteristic comparisons all pass.
Fallback runtime: 22.290423 s.

## P5.4 — forced-point spectrum closure

\[B_1^\star=d_1(x)\ell_1\ell_1^{\mathsf T},\qquad d_1(x)=- \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x},\qquad\ell_1=\begin{pmatrix}1\\-1\\1\end{pmatrix}.\]

For a rank-one generalized pencil, the sole nonzero root is

\[
z=d_1(x)\ell_1^{\mathsf T}G_1^{-1}\ell_1=- \frac{100 \left(x - 1\right) \left(3 x - 1\right)}{9 x}\left(\frac{4}{25}\right)=- \frac{16 \left(x - 1\right) \left(3 x - 1\right)}{9 x}=\lambda_3.
\]

\[B_2^\star=d_2(x)\ell_2\ell_2^{\mathsf T},\qquad d_2(x)=- \frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x},\qquad\ell_2=\begin{pmatrix}1\\-1\end{pmatrix}.\]

For a rank-one generalized pencil, the sole nonzero root is

\[
z=d_2(x)\ell_2^{\mathsf T}G_2^{-1}\ell_2=- \frac{12 \left(x - 1\right) \left(2 x - 1\right)}{x}\left(\frac{1}{3}\right)=- \frac{4 \left(x - 1\right) \left(2 x - 1\right)}{x}=\lambda_5.
\]

The spin dimensions give multiplicities \(2(2)+1=5\) and \(2(1)+1=3\);
the remaining 19 dimensions are zero. Directly on the 27-by-27 matrix:

\[C(C-\lambda_5I)(C-\lambda_3I)=0,\]

\[
\operatorname{Tr}C=- \frac{4 \left(x - 1\right) \left(42 x - 19\right)}{3 x}=5\lambda_5+3\lambda_3,
\qquad
\operatorname{Tr}C^2=\frac{16 \left(x - 1\right)^{2} \left(684 x^{2} - 636 x + 151\right)}{27 x^{2}}=5\lambda_5^2+3\lambda_3^2.
\]

**GATE V4: PASS.** Both rank-one factorizations, the Gram-pencilled
eigenvalues, the annihilating polynomial, and both trace identities were
verified symbolically. Runtime: 21.301970 s.

## P5.5 — exact certificate congruence data

| x | (s1,s2) | (p,q,d) | `lambda_5` (mult. 5) | `lambda_3` (mult. 3) |
|---|---|---|---|---|
| $26/51$ | $(25/39,14/39)$ | $(1/3,\frac{5 \sqrt{13}}{39},50/153)$ | $50/663$ | $200/221$ |
| $4/7$ | $(1/2,1/2)$ | $(1/3,\frac{\sqrt{6}}{6},2/7)$ | $3/7$ | $20/21$ |
| $3/4$ | $(2/9,7/9)$ | $(1/3,\frac{\sqrt{6}}{9},1/6)$ | $2/3$ | $20/27$ |

### Certificate \(x=26/51\)

\[G_0=\left[\begin{matrix}6\end{matrix}\right],\qquadB_0=\left[\begin{matrix}0\end{matrix}\right].\]

\[G_1=\left[\begin{matrix}15 & 10 & 10\\10 & 40 & -10\\10 & -10 & 40\end{matrix}\right],\qquadB_1=\left[\begin{matrix}\frac{1250}{221} & - \frac{1250}{221} & \frac{1250}{221}\\- \frac{1250}{221} & \frac{1250}{221} & - \frac{1250}{221}\\\frac{1250}{221} & - \frac{1250}{221} & \frac{1250}{221}\end{matrix}\right].\]

\[G_2=\left[\begin{matrix}12 & 6\\6 & 12\end{matrix}\right],\qquadB_2=\left[\begin{matrix}\frac{50}{221} & - \frac{50}{221}\\- \frac{50}{221} & \frac{50}{221}\end{matrix}\right].\]

\[G_3=\left[\begin{matrix}10\end{matrix}\right],\qquadB_3=\left[\begin{matrix}0\end{matrix}\right].\]

\[B_1=(\frac{1250}{221})\begin{pmatrix}1\\-1\\1\end{pmatrix}\begin{pmatrix}1\\-1\\1\end{pmatrix}^{\mathsf T},\qquad\ell_1^{\mathsf T}G_1^{-1}\ell_1=4/25.\]

\[B_2=(\frac{50}{221})\begin{pmatrix}1\\-1\end{pmatrix}\begin{pmatrix}1\\-1\end{pmatrix}^{\mathsf T},\qquad\ell_2^{\mathsf T}G_2^{-1}\ell_2=1/3.\]

\[\det(zI-C)=\frac{z^{19} \left(221 z - 200\right)^{3} \left(663 z - 50\right)^{5}}{1382752534188934925523}.\]

Direct and normalized-pencil spectra: exact identity PASS.

### Certificate \(x=4/7\)

\[G_0=\left[\begin{matrix}6\end{matrix}\right],\qquadB_0=\left[\begin{matrix}0\end{matrix}\right].\]

\[G_1=\left[\begin{matrix}15 & 10 & 10\\10 & 40 & -10\\10 & -10 & 40\end{matrix}\right],\qquadB_1=\left[\begin{matrix}\frac{125}{21} & - \frac{125}{21} & \frac{125}{21}\\- \frac{125}{21} & \frac{125}{21} & - \frac{125}{21}\\\frac{125}{21} & - \frac{125}{21} & \frac{125}{21}\end{matrix}\right].\]

\[G_2=\left[\begin{matrix}12 & 6\\6 & 12\end{matrix}\right],\qquadB_2=\left[\begin{matrix}\frac{9}{7} & - \frac{9}{7}\\- \frac{9}{7} & \frac{9}{7}\end{matrix}\right].\]

\[G_3=\left[\begin{matrix}10\end{matrix}\right],\qquadB_3=\left[\begin{matrix}0\end{matrix}\right].\]

\[B_1=(\frac{125}{21})\begin{pmatrix}1\\-1\\1\end{pmatrix}\begin{pmatrix}1\\-1\\1\end{pmatrix}^{\mathsf T},\qquad\ell_1^{\mathsf T}G_1^{-1}\ell_1=4/25.\]

\[B_2=(\frac{9}{7})\begin{pmatrix}1\\-1\end{pmatrix}\begin{pmatrix}1\\-1\end{pmatrix}^{\mathsf T},\qquad\ell_2^{\mathsf T}G_2^{-1}\ell_2=1/3.\]

\[\det(zI-C)=\frac{z^{19} \left(7 z - 3\right)^{5} \left(21 z - 20\right)^{3}}{155649627}.\]

Direct and normalized-pencil spectra: exact identity PASS.

### Certificate \(x=3/4\)

\[G_0=\left[\begin{matrix}6\end{matrix}\right],\qquadB_0=\left[\begin{matrix}0\end{matrix}\right].\]

\[G_1=\left[\begin{matrix}15 & 10 & 10\\10 & 40 & -10\\10 & -10 & 40\end{matrix}\right],\qquadB_1=\left[\begin{matrix}\frac{125}{27} & - \frac{125}{27} & \frac{125}{27}\\- \frac{125}{27} & \frac{125}{27} & - \frac{125}{27}\\\frac{125}{27} & - \frac{125}{27} & \frac{125}{27}\end{matrix}\right].\]

\[G_2=\left[\begin{matrix}12 & 6\\6 & 12\end{matrix}\right],\qquadB_2=\left[\begin{matrix}2 & -2\\-2 & 2\end{matrix}\right].\]

\[G_3=\left[\begin{matrix}10\end{matrix}\right],\qquadB_3=\left[\begin{matrix}0\end{matrix}\right].\]

\[B_1=(\frac{125}{27})\begin{pmatrix}1\\-1\\1\end{pmatrix}\begin{pmatrix}1\\-1\\1\end{pmatrix}^{\mathsf T},\qquad\ell_1^{\mathsf T}G_1^{-1}\ell_1=4/25.\]

\[B_2=(2)\begin{pmatrix}1\\-1\end{pmatrix}\begin{pmatrix}1\\-1\end{pmatrix}^{\mathsf T},\qquad\ell_2^{\mathsf T}G_2^{-1}\ell_2=1/3.\]

\[\det(zI-C)=\frac{z^{19} \left(3 z - 2\right)^{5} \left(27 z - 20\right)^{3}}{4782969}.\]

Direct and normalized-pencil spectra: exact identity PASS.

**GATE V5: PASS.** All three direct 27-by-27 characteristic polynomials equal
their normalized Gram-pencil products and their stated 19/5/3 spectra.
Runtime: 0.687801 s.

## P5.6 — verification-statement metadata

<!-- P5_METADATA_START -->
| Script | SHA-256 |
|---|---|
| `tools/whgap_p5_derivation.py` | `d9e2774ce5d64a7fed1cc1755930636d8fd582b22ae1be020f10e5e9ea6ba4cc` |
| `tools/whgap_p5_metadata.py` | `d7cb6ccb753f05f6dc0650203093b5dd10df88a14a2f5647907a5fc52c6abd71` |
| `tools/whgap_p2_exact.py` | `1429d64222422765d008381304ca788d3c89fa70af10465e4f17ad117f559f53` |
| `tools/whgap_p2_feasibility.py` | `86247afba3a88660a00d4a1262997b63b149e5502e6d35ffc40098662f24722b` |
| `tools/whgap_fable_audit.py` | `cc10e0cd2a5b7338ab9927ba7f6f16476641276d6c8077029b078e93d903dd05` |
| `tools/whgap_fable_audit_ext.py` | `4f42e8fffeb692a382028917c41ec4e8ecf1d807ff9eb62acaa7aca88d253b8d` |

| Runtime component | Version/value |
|---|---|
| Executable | `C:<home>/cpython3119/python.exe` |
| Python | `3.11.9` (CPython) |
| sympy | `1.13.1` |
| numpy | `1.26.4` |
| scipy | `1.14.1` |
| mpmath | `1.3.0` |

The hashes above are computed from the exact source files used by this package.
<!-- P5_METADATA_END -->

## Gate summary

| Gate | Result | Scope |
|---|---|---|
| V1 | PASS | 15-pattern expansion, all 729 entries general and forced |
| V2 | PASS | both entry-list forcing computations |
| V3 | PASS | integer bases, Casimir, blocks, direct/pencil characteristic identity |
| V4 | PASS | rank-one pencils, eigenvalues, annihilator, trace checks |
| V5 | PASS | all three exact certificate spectra |

Total derivation runtime: 54.493270 s.

