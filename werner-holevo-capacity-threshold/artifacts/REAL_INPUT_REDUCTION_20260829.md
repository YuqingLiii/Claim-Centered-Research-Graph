# One-copy real inputs: rank-two theorem and one-curve reduction

Date: 2026-08-29  
Status: proposer-side analytic proof; independent review pending.

## Statement

For the qutrit noisy Werner--Holevo channel and

\[
\frac25\le x\le\frac12,
\]

every real density matrix has nonpositive coherent information. The proof first settles the
rank-two boundary, reduces any possible full-rank violation to the eigenvalue curve
`(t,t,1-2t)`, and then proves the remaining two-variable entropy inequality exactly.

## Classical spectra for a real input

By `O(3)` covariance, a real symmetric input may be diagonalized. Write its eigenvalue vector as
`r=(r_1,r_2,r_3)`, and put

\[
p=1-x,\qquad q=\frac{x}{2},\qquad \alpha=p-q=1-\frac{3x}{2}.
\]

The receiver and padded complementary spectra are

\[
b_i=q+\alpha r_i
\]

and

\[
e=(p,q(1-r_1),q(1-r_2),q(1-r_3)).
\]

Define the entropy excess

\[
F_x(r)=H(e)-H(b)=-I_c(\operatorname{diag}r,\Lambda_x).
\]

We must prove `F_x >= 0`.

## Rank-two boundary theorem

Every rank-two boundary point is, up to permutation,

\[
r=(t,1-t,0),\qquad 0\le t\le1.
\]

The two spectra share a component of mass `q`. Let

\[
m=p+q=1-\frac{x}{2},
\qquad
z=\frac{q}{m}=\frac{x}{2-x}.
\]

After removing the shared component and normalizing the remaining mass `m`, direct entropy
bookkeeping gives

\[
F_x(t,1-t,0)
=m\left[h_2(z)+z h_2(t)-h_2(z*t)\right],
\]

where

\[
z*t=z(1-t)+(1-z)t=z+(1-2z)t
\]

is binary convolution. On the stated `x` interval,

\[
\frac14\le z\le\frac13.
\]

It remains to prove

\[
h_2(z*t)-h_2(z)\le z h_2(t).
\tag{1}
\]

By the symmetries of binary entropy and convolution, restrict to `0 <= t <= 1/2`. Work with
natural logarithms; the base only multiplies all terms by a positive constant. Set

\[
g(t)=h(z)+z h(t)-h(z*t).
\]

Then `g(0)=0` and

\[
g'(t)=zL(t)-(1-2z)L(z*t),
\qquad
L(s)=\log\frac{1-s}{s}.
\]

Write `a=1-2z` and `y=1-2t`. Since

\[
L(t)=2\operatorname{artanh}(y),
\qquad
L(z*t)=2\operatorname{artanh}(ay),
\]

convexity of `artanh` on `[0,1)` and `artanh(0)=0` imply

\[
L(z*t)\le aL(t).
\]

Therefore

\[
g'(t)\ge[z-a^2]L(t)
=(4z-1)(1-z)L(t)\ge0.
\]

So `g(t)>=0`, proving (1), hence

\[
\boxed{I_c(\rho,\Lambda_x)\le0}
\]

for every real rank-two state. Rank-one states give equality because the two Stinespring reductions
have the same nonzero spectrum.

## Why a real full-rank counterexample must have two equal eigenvalues

Apart from the constant `-p log p`, the excess is separable:

\[
F_x(r)=\text{constant}+\sum_{i=1}^3 f_x(r_i),
\]

with

\[
f_x(r)=(q+\alpha r)\log(q+\alpha r)
-q(1-r)\log(q(1-r)).
\]

Its second derivative is

\[
f_x''(r)=\frac{\alpha^2}{q+\alpha r}-\frac{q}{1-r}.
\]

For `2/5 <= x < 1/2`, this changes sign at most once, namely at

\[
r_0=1-\frac{q}{\alpha}
=\frac{2(1-2x)}{2-3x}.
\]

Hence `f_x'` first increases and then decreases; every horizontal line meets its graph in at most
two points. At an interior constrained minimum of `F_x`, the Lagrange equations give

\[
f_x'(r_1)=f_x'(r_2)=f_x'(r_3).
\]

The three coordinates therefore assume at most two distinct values, so at least two are equal.
The endpoint `x=1/2` is simpler because `f_x'` is monotone and obeys the same conclusion.

Since the boundary was proved nonnegative, any negative global minimum, if it exists, is interior
and occurs on

\[
r=(t,t,1-2t),\qquad0<t<1/2.
\]

On that curve the remaining exact inequality is

\[
\begin{aligned}
&H\bigl(p,q(1-t),q(1-t),2qt\bigr)\\
&\quad\ge
H\bigl(q+\alpha t,q+\alpha t,p-2\alpha t\bigr).
\end{aligned}
\tag{2}
\]

Thus (2) is necessary and sufficient to finish the all-real-input one-copy proof.

## Completion of the two-equal curve

For `r=(t,t,1-2t)`, group the two equal outcomes in each spectrum. In bits, (2) is equivalent to

\[
F_x(t)
=h_2(x)+x h_2(t)
-h_2\!\left(x+(2-3x)t\right)
-2(1-x)t
\ge0,
\tag{3}
\]

for `2/5 <= x <= 1/2` and `0 <= t <= 1/2`. Put

\[
y=x+(2-3x)t,
\qquad
L(s)=\log_2\frac{1-s}{s}.
\]

### Monotonicity in `x`

Direct differentiation gives

\[
\partial_xF_x(t)
=L(x)+h_2(t)-(1-3t)L(y)+2t.
\tag{4}
\]

If `0 <= t <= 1/3` and `y >= 1/2`, every term in (4) is nonnegative because `L(x)>=0`,
`L(y)<=0`, and `1-3t>=0`. If instead `y<1/2`, then `y>=x` and `L` is decreasing, so

\[
0<L(y)\le L(x).
\]

Consequently

\[
\partial_xF_x(t)
\ge 3tL(x)+h_2(t)+2t\ge0.
\]

If `1/3 <= t <= 1/2`, then

\[
y\le1-\frac{x}{2}
\]

and hence

\[
L(y)\ge L(1-x/2)=\log_2\frac{x}{2-x}\ge-2,
\]

where the last inequality uses `x>=2/5`. Equation (4) now yields

\[
\partial_xF_x(t)
\ge h_2(t)+2t-2(3t-1)
=h_2(t)+2-4t\ge0;
\]

the final inequality follows, for example, from `h_2(t)>=2t` on `[0,1/2]`.

Therefore

\[
F_x(t)\ge F_{2/5}(t).
\tag{5}
\]

### Exact endpoint analysis

At `x=2/5`, differentiating (3) with respect to `t` and multiplying by `5/2` gives

\[
\frac52F'_{2/5}(t)=L(t)-2L\!\left(\frac25+\frac45t\right)-3.
\]

The derivative vanishes exactly when

\[
\frac{1-t}{t}
\left(\frac{2+4t}{3-4t}\right)^2=8,
\]

or equivalently

\[
1-15t+48t^2-36t^3=0.
\]

Its roots are

\[
\frac13,
\qquad
\frac12-\frac{\sqrt6}{6},
\qquad
\frac12+\frac{\sqrt6}{6}.
\]

Only the first two lie in `[0,1/2]`. The polynomial sign shows that the smaller root is a local
maximum and `t=1/3` is a local minimum. Hence the global minimum on `[0,1/2]` is attained at
`t=0` or `t=1/3`.

At the pure endpoint,

\[
F_{2/5}(0)=0.
\]

At the uniform point,

\[
F_{2/5}(1/3)
=h_2(2/5)-\frac35\log_2 3
=\frac15\log_2\frac{5^5}{4\cdot3^6}>0,
\]

because `5^5=3125>2916=4*3^6`. Together with (5), this proves (3) on the full rectangle.

Combining the curve proof with the boundary theorem and stationary-point reduction gives

\[
\boxed{
I_c(\rho,\Lambda_x)\le0
\quad\text{for every real qutrit state }\rho,
\quad 2/5\le x\le1/2.
}
\]

## Numerical corroboration and scope

A 1001-step triangular grid over the real eigenvalue simplex at each of
`x=0.40,0.41,0.45,0.49,0.50` found the minimum `F_x=0` only at pure vertices. This corroborates the
analytic result but is not used by its proof.

The theorem does not control states with a nonzero imaginary-antisymmetric component, and it does
not tensorize. It is therefore a strict sub-result of the one-copy five-parameter gate, not a
solution of the quantum-capacity strip.
