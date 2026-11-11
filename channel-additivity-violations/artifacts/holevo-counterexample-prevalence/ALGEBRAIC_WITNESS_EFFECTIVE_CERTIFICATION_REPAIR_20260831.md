# Effective certification repair for algebraic p=1 MOE pair witnesses

Date: 2026-08-31

Status: proposer-side canonical repair after the BLOCK findings in
`ALGEBRAIC_WITNESS_EXISTENCE_INDEPENDENT_REVIEW_20260831.md`. This document is not an independent
review and does not license promotion.

## 1. Exact target

All logarithms and entropies in this document are base two. For finite-dimensional CPTP maps
\(\mathcal N,\mathcal M\), define the pair minimum-output-entropy defect

\[
\Delta_S(\mathcal N,\mathcal M)
 :=S_{\min}(\mathcal N)+S_{\min}(\mathcal M)
   -S_{\min}(\mathcal N\otimes\mathcal M).
\]

The repaired target is: for every rational \(G>0\), an exhaustive Turing procedure eventually
prints finite-dimensional CPTP maps \(\mathcal N,\mathcal M\) with algebraic Kraus entries and a
finite certificate proving \(\Delta_S(\mathcal N,\mathcal M)>G\). The target is pair MOE only.
It makes no Holevo, same-channel, dimension-bound, denominator-bound, certificate-size, or runtime
claim.

## 2. Exact existence input

The only random/existence premise used is `HCPREV.product-haar-moe-unbounded`. Its exact theorem is
in bits and states that for every target gap there is a fixed finite product depth and, at some
finite per-leg dimension, a channel/conjugate-channel pair with MOE defect strictly greater than
the target. The strict inequality leaves a positive residual margin.

The broader `HCPREV.product-haar-unbounded` contains deterministic Holevo pushforwards and is not a
premise of the repaired route. `HCPREV.open-set-stability` remains a useful qualitative theorem,
but the effective construction below records the actual modulus it needs and does not treat bare
openness as an effectivity oracle.

## 3. Effective algebraic Cayley enumeration

Let \(A^*=-A\) have entries in \(\mathbb Q(i)\) and set

\[
C(A)=(I-A)(I+A)^{-1}.
\]

### 3.1 Exactness and enumerability

`I+A` is always invertible. If \((I+A)v=0\), then \(Av=-v\); however
\(\langle v,Av\rangle\) is purely imaginary whereas \(-\lVert v\rVert^2\) is negative real.
Inversion over \(\mathbb Q(i)\) remains in \(\mathbb Q(i)\), and direct multiplication proves
\(C(A)^*C(A)=I\). Gaussian-rational skew-Hermitian matrices can be enumerated by dimension,
common denominator, numerator height, and exact skew-Hermitian constraints. Thus their Cayley
unitaries are exactly and effectively enumerable.

For a fixed number \(m\) of terms, define

\[
\Phi_{\mathbf U}(\rho)=\frac1m\sum_{i=1}^mU_i\rho U_i^*.
\]

The Kraus matrices \(m^{-1/2}U_i\) have algebraic entries. Trace preservation is exact and is
verified by \(\sum_i m^{-1}U_i^*U_i=I\).

### 3.2 Density, including the minus-one chart boundary

If a unitary \(U\) has no eigenvalue \(-1\), then
\(A=(I-U)(I+U)^{-1}\) is skew-Hermitian. Approximate \(A\) entrywise by Gaussian-rational
skew-Hermitian matrices and use continuity of \(C\). If \(U\) has eigenvalue \(-1\), multiply it
by an arbitrarily small scalar phase avoiding the finite forbidden set of phases; then use the
preceding chart. Hence the enumerated Cayley unitaries are dense in every finite \(U(d)\).

### 3.3 Entrywise distance to diamond distance

For two \(d\)-dimensional unitaries,

\[
\lVert\operatorname{Ad}_U-\operatorname{Ad}_V\rVert_\diamond
 \leq 2\lVert U-V\rVert_{\rm op}.
\]

This follows after adjoining an arbitrary reference system by expanding
\((U\otimes I)X(U^*\otimes I)-(V\otimes I)X(V^*\otimes I)\) into two terms and applying the
trace-norm ideal inequality. If every entry differs by at most \(\eta\), then
\(\lVert U-V\rVert_{\rm op}\leq\lVert U-V\rVert_F\leq d\eta\). Consequently

\[
\lVert\Phi_{\mathbf U}-\Phi_{\mathbf V}\rVert_\diamond
 \leq \frac2m\sum_i\lVert U_i-V_i\rVert_{\rm op}
 \leq 2d\eta.
\]

Entrywise conjugation preserves the same bound. For CPTP pairs,

\[
\lVert\mathcal N\otimes\mathcal M-
          \mathcal N'\otimes\mathcal M'\rVert_\diamond
\leq
\lVert\mathcal N-\mathcal N'\rVert_\diamond+
\lVert\mathcal M-\mathcal M'\rVert_\diamond,
\]

because every CPTP map has diamond norm one. These estimates convert the algebraic entrywise
enumeration into a certified diamond-dense enumeration.

## 4. Pure-state reduction and a certified rational sphere net

### 4.1 Pure-state reduction

For a CPTP map \(\Phi\) and any decomposition
\(\rho=\sum_jp_j|\psi_j\rangle\langle\psi_j|\), entropy concavity gives

\[
S(\Phi(\rho))\geq\sum_jp_jS(\Phi(|\psi_j\rangle\langle\psi_j|))
\geq\min_jS(\Phi(|\psi_j\rangle\langle\psi_j|)).
\]

Thus \(S_{\min}(\Phi)\) is the minimum over pure inputs. For a product channel, the pure-state
sphere is the full joint input sphere, so entangled pure inputs are included.

### 4.2 Explicit finite rational net and its radius certificate

Identify the unit sphere of \(\mathbb C^a\) with \(S^q\subset\mathbb R^{q+1}\), where
\(q=2a-1\). For \(t\in\mathbb Q^q\), use the rational stereographic point

\[
\sigma(t)=\left(\frac{2t}{1+\lVert t\rVert^2},
                  \frac{\lVert t\rVert^2-1}{1+\lVert t\rVert^2}\right),
\]

and also include the north pole \(e_{q+1}\). The derivative operator norm of \(\sigma\) is at
most two.

Given rational \(0<\delta<1\), choose an integer \(R\) satisfying the rationally checkable
inequality

\[
4\leq\delta^2(1+R^2).
\]

Then every stereographic point with \(\lVert t\rVert\geq R\) lies within \(\delta\) of the north
pole. Choose a rational grid step \(h\) on \([-R,R]^q\) satisfying the rationally checkable
condition \(q h^2\leq\delta^2\), with endpoints included. Coordinate rounding moves \(t\) by at
most \(\sqrt qh/2\), hence moves \(\sigma(t)\) by at most \(\sqrt qh\leq\delta\). The finite grid
images plus the north pole are therefore a finite rational \(\delta\)-net with a certificate
consisting only of \(q,R,h\) and the two displayed rational inequalities.

### 4.3 Exact entropy modulus and global minimum bounds

For unit vectors \(\psi,\phi\),

\[
T(|\psi\rangle\langle\psi|,|\phi\rangle\langle\phi|)
 =\sqrt{1-|\langle\psi,\phi\rangle|^2}
 \leq\lVert\psi-\phi\rVert_2.
\]

Trace distance contracts under CPTP maps. For output dimension \(b\geq2\), rational
\(0<\delta\leq1-1/b\), and

\[
\omega_b(\delta)=\delta\log_2(b-1)+h_2(\delta),
\]

Audenaert's theorem gives entropy variation at most \(\omega_b(\delta)\). For \(b=1\), set
\(\omega_1=0\).

At requested precision `q`, the directed-logarithm routine from Section 5.3 also returns a
rational upper enclosure

\[
\widehat\omega_{b,q}(\delta)\in\mathbb Q,
\qquad
\omega_b(\delta)\leq\widehat\omega_{b,q}(\delta)
\leq\omega_b(\delta)+2^{-q}.
\]

This enclosure, rather than an unevaluated transcendental value, is stored in the finite
certificate.

Suppose a pointwise entropy verifier returns directed rational intervals
\([\ell_{\Phi,\phi},u_{\Phi,\phi}]\) on a finite net \(E_\delta\). Define

\[
L_{\Phi,q}=\min_{\phi\in E_\delta}\ell_{\Phi,\phi}
             -\widehat\omega_{b,q}(\delta),
\qquad
U_\Phi=\min_{\phi\in E_\delta}u_{\Phi,\phi}.
\]

Then

\[
L_{\Phi,q}\leq S_{\min}(\Phi)\leq U_\Phi.
\]

The same construction is run separately for \(\mathcal N\), \(\mathcal M\), and the full joint
input sphere for \(\mathcal N\otimes\mathcal M\).

## 5. Finite entropy intervals for algebraic output states

### 5.1 Exact input representation

Represent a real algebraic number by a square-free integer polynomial and a rational isolating
interval; represent a complex algebraic number by its real and imaginary algebraic parts. Exact
sign tests, equality, field arithmetic, resultants, Sturm chains, and isolating-interval refinement
are terminating algorithms. A rational net vector and algebraic Kraus matrices therefore give an
exact algebraic Hermitian PSD trace-one output matrix.

### 5.2 Spectral isolation

Compute the characteristic polynomial over the generated real algebraic number field. Exact
Hermitian eigenvalue isolation produces disjoint rational intervals in \([0,1]\), with
multiplicities, each containing exactly the certified number of roots. Refinement makes every
interval arbitrarily narrow. Positivity and unit trace are checked by exact algebraic sign/equality
tests and by the certified root counts.

### 5.3 Directed logarithm intervals, including zero

For a positive rational interval \([a,b]\) with \(a>0\), range reduction and a convergent rational
series for \(\log\) give finite rational lower and upper bounds on
\(f(x)=-x\log_2x\) over \([a,b]\); split at the unique critical point \(1/e\) when necessary.
The resulting proof object contains the range-reduction exponent, truncation order, rational
remainder bound, and directed arithmetic operations.

If an eigenvalue interval touches zero, exact algebraic equality decides whether the eigenvalue is
zero. For an exact zero use \(f(0)=0\). Otherwise refinement eventually produces a positive lower
endpoint. Before separation, a valid temporary interval is obtained from nonnegativity and a safe
upper bound. Once \(b<1/4<1/e\), monotonicity on \([0,b]\) gives
\(0\leq f(x)\leq f(b)\), and the directed log routine bounds \(f(b)\); this upper bound tends to
zero with \(b\). Thus zero eigenvalues and eigenvalues arbitrarily close to zero cause no
termination obstruction.

Summing the multiplicity-weighted scalar intervals gives rationals

\[
\ell_q(\rho)\leq S_{\rm bits}(\rho)\leq u_q(\rho),
\qquad u_q(\rho)-\ell_q(\rho)\leq2^{-q},
\]

after finite refinement, where
\(S_{\rm bits}(\rho)=-\operatorname{Tr}(\rho\log_2\rho)\) is von Neumann entropy in bits,
not Renyi-2 entropy.

### 5.4 Finite verifier

A certificate contains:

1. exact algebraic matrix representations and exact CPTP identities;
2. the characteristic polynomial and disjoint rational eigenvalue isolators with root counts;
3. PSD and trace-one sign/equality checks;
4. directed scalar \(-x\log_2x\) proof objects, including the explicit zero branch; and
5. the rational entropy sum interval.

A Turing verifier repeats only exact polynomial arithmetic, rational comparisons, Sturm/root-count
checks, and rational remainder inequalities. Hence acceptance of each interval is decidable and
finite.

## 6. Effective preservation of the strict gap

Let the output dimensions of \(\mathcal N,\mathcal M\) be \(b,c\), and define
\(\varepsilon_{\mathcal N}=\tfrac12\lVert\mathcal N-\mathcal N'\rVert_\diamond\) and similarly
for \(\mathcal M\). For sufficiently small errors, the bounds above give

\[
|\Delta_S(\mathcal N,\mathcal M)-\Delta_S(\mathcal N',\mathcal M')|
\leq
F_b(\varepsilon_{\mathcal N})+
F_c(\varepsilon_{\mathcal M})+
F_{bc}(\varepsilon_{\mathcal N}+\varepsilon_{\mathcal M}),
\]

where \(F_d(x)=\omega_d(\min\{x,1-1/d\})\). The right side tends effectively to zero. At every
finite stage the verifier computes a directed rational upper enclosure for each displayed
\(F_d\), using the same range reduction and rational remainder bounds as Section 5.3. Therefore a
successful finite product-Haar sample with gap \(G+\eta\) has a sufficiently close algebraic
Cayley approximation with gap still greater than \(G\). The search need not know \(\eta\) or the
needed entrywise radius.

## 7. Certified lower gap and dovetail termination

At mesh/precision stage \(s\), compute

\[
C_s=L_{\mathcal N,s}+L_{\mathcal M,s}-U_{\mathcal N\otimes\mathcal M,s}.
\]

The sign is forced by the definition of \(\Delta_S\): both positive single-channel terms require
lower bounds, while the subtracted joint term requires an upper bound. Thus

\[
C_s\leq\Delta_S(\mathcal N,\mathcal M).
\]

Here every \(L_{\Phi,s}\) uses a directed rational upper enclosure
\(\widehat\omega_{b,q_s}(\delta_s)\), so \(C_s\) is rational and its final comparison with the
rational target \(G\) is exact. As meshes, entropy intervals, and modulus enclosures refine,
\(C_s\) converges to the true defect from a certified lower side; monotonicity in \(s\) is
unnecessary.

The Turing procedure dovetails:

1. dimensions and equal-weight tuple lengths;
2. pairs of finite Gaussian-rational Cayley-unitary tuples;
3. the three independently certified sphere nets; and
4. every entropy-isolation/logarithm precision.

Whenever the rational comparison \(C_s>G\) holds, it prints the two algebraic Kraus lists, the
three mesh certificates, every accepted entropy interval proof object, and the final inequality.
The successful algebraic approximation from Section 6 has a strict residual margin, so some stage
on its branch satisfies \(C_s>G\). Dovetailing therefore halts for every rational \(G>0\).

## 8. Scope exclusions

- The procedure is proved to terminate but has no known usable resource bound.
- No successful tuple is claimed to have been printed in the repository.
- No compact or low-dimensional explicit witness is obtained.
- Holevo/Weyl/flagged/same-channel reductions in older proposer notes are non-load-bearing history
  for this repaired MOE-pair claim.
- This theorem does not close `HCPREV.explicit-witness-frontier` or `HCPREV.goal`.

## 9. Repair and review map

The repaired main route has four load-bearing premises:

1. `HCPREV.product-haar-moe-unbounded`;
2. `HCPREV.cayley-algebraic-channel-density`;
3. `HCPREV.effective-pure-state-net-moe-bounds`; and
4. `HCPREV.algebraic-entropy-interval-verifier`.

All three new effective atoms and the repaired route remain `CONJECTURED`. A different reviewer
must inspect their exact hashes, the Audenaert source interface, this proof, the certificate signs,
and the termination quantifiers before any promotion.
