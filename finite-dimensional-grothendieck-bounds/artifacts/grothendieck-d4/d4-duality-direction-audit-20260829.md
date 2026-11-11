# Degree-four duality-direction audit

## D4-DIR1. Target polynomial

Let

\[
 f(x,y)=C-x^TAy,
 \qquad C=2081044153087351400,
\]

in the Boolean quotient `x_i^2=y_j^2=1`.  An exact identity

\[
 f=\sum_k q_k^2,\qquad \deg q_k\le2,
\]

implies `f>=0` on every Boolean assignment and therefore proves the desired
classical upper bound.

## D4-DIR2. Equality-face restriction

The archived sign witness makes `f=0`.  If the above SOS identity exists, then
every summand `q_k` vanishes at every symmetry image of an equality witness.
Thus each `q_k` lies in the equality-vanishing degree-at-most-two module `K`.
Consequently it is lossless for this particular SOS search to restrict Gram
matrices to `K`.

## D4-DIR3. Meaning of the 746825-coordinate system

The constructor `h4_full_invariant_dual_spec.py` explicitly defines an
H4-invariant functional `L` on Boolean moments through degree four.  Its block
conditions are

\[
 L(q^2)\ge0\quad\hbox{for every }q\in K,
\]

and its normalization is

\[
 L(f)=-1.
\]

Therefore a feasible point of that system separates `f` from the cone of
degree-four SOS expressions supported on `K`.  Feasibility proves that the
degree-four SOS route fails.  It does **not** prove `f>=0` on Boolean points.

## D4-DIR4. Correct implication directions

The correct logic is:

1. an exact PSD Gram/SOS certificate for `f` implies the classical upper bound;
2. a feasible separating functional `L` with `L(f)<0` refutes that SOS route;
3. failure of a restricted family of candidate `L` proves neither (1) nor the
   infeasibility of the unrestricted separating system;
4. neither outcome alone decides whether a different combinatorial or higher-
   degree proof of the classical upper bound exists.

The previous local DAG had used item 2 in the direction of item 1.  This audit
repairs that dependency before further computation is interpreted.

