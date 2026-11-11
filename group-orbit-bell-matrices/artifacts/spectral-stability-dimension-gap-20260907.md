# Spectral stability and a quantitative vector-dimension gap

Author: primary Codex research agent, 2026-09-07. Initially author-level;
independent findings are stored separately under reviews/. Novelty is not asserted.

## ST1: normalized setup

Let A be nonzero real m by n, sigma=||A||op, and U,V paired orthonormal
top singular bases with r columns. Let tau be the norm of A restricted to
the orthogonal complement of im(V), with tau=0 for a zero complement.
Thus tau<sigma. Unit-row strategies X,Y satisfy ||X||F=sqrt(m),
||Y||F=sqrt(n). Put x=X/sqrt(m), y=Y/sqrt(n), B=A/sigma, so
||x||F=||y||F=1. Write q=<x,By>F. The spectral upper bound says q<=1.

## ST2: concentration and alignment

Suppose q>=1-epsilon with 0<=epsilon<=1. Put P=VV^T and t=tau/sigma.
Orthogonality of singular spaces gives

    ||By||F^2 <= ||Py||F^2+t^2||(I-P)y||F^2
               =1-(1-t^2)||(I-P)y||F^2.

Cauchy--Schwarz gives ||By||F>=q>=1-epsilon. Squaring is justified by
the nonnegative right side. Hence

    ||(I-P)y||F^2 <= (2epsilon-epsilon^2)/(1-t^2).

Also

    ||x-By||F^2=1+||By||F^2-2q <=2epsilon.

No equivariance or attainability assumption is used. These estimates assert
concentration and alignment, not proximity to a feasible exact optimum.

## ST3: the paired dilation

For the quantitative dimension result assume r>=2, A is transitive
equivariant, and the linear map

    L:Sym_r -> R^(m+n), K -> (diag(UKU^T),diag(VKV^T))

is injective. Norms on its domain and target are Frobenius and Euclidean.
Let s=min_{||K||F=1}||L(K)||2>0 and delta=1-tau/sigma>0.
Define

    C = [[0,B],[B^T,0]],
    W = (1/sqrt(2))*[U;V],
    Z = (1/sqrt(2))*[x;y].

Then ||Z||F=1, W has orthonormal columns, CW=W, and <Z,CZ>F=q.
All eigenvalues of C outside im(W) are <=tau/sigma: the others are
the remaining positive singular values divided by sigma, their negatives,
possible zeros, and the eigenvalue -1. This remains true when tau=0.
Put Z0=WW^TZ=W T, T=W^TZ, E=Z-Z0, eta=||E||F. Orthogonal spectral
decomposition yields

    q <= ||Z0||F^2+(1-delta)||E||F^2=1-delta*eta^2,
    eta^2 <= (1-q)/delta.

This inequality is valid even when q is negative.

## ST4: diagonal balance residual

Write M=[x;y]=sqrt(2)Z and M0=[UT;VT]=sqrt(2)Z0, and H=T T^T.
The rows of M have squared norms 1/m on the first side and 1/n on the
second. Transitivity of the top singular projectors gives

    L(I_r/r)=((1/m)1_m,(1/n)1_n).

For arbitrary real row matrices F,G of equal shape,

    ||diag(FF^T-GG^T)||2
      <= ||diag(FF^T-GG^T)||1
      <= ||F-G||F (||F||F+||G||F).

Indeed each absolute row-norm-square difference is at most
||f_i-g_i||(||f_i||+||g_i||); sum and apply Cauchy--Schwarz and the
triangle inequality in Euclidean space. Here ||M||F=sqrt(2),
||M0||F<=sqrt(2), and ||M-M0||F=sqrt(2)eta. Therefore

    ||L(H-I_r/r)||2 <=4eta,
    ||H-I_r/r||F <=4eta/s.

The constant is intentionally conservative. The H here is normalized by
Tr(H)<=1; the earlier balance classification uses a weight n times larger.

## ST5: robust dimension exclusion

If X,Y have d<r columns, H=T T^T has rank at most d and has a unit null
vector v. Thus

    ||H-I_r/r||F >= ||(H-I_r/r)v||2=1/r.

Combining ST3 and ST4 proves

    1/r <= (4/s)*sqrt((1-q)/delta),
    q <= 1-delta*s^2/(16r^2).

Multiplying by sigma sqrt(mn) gives the claim of
GROTHORB.robust-dimension-gap. A larger observed value therefore rules out
real-vector dimension d<r in this correlation model.

This proof uses only top-space balance, so it applies beyond group orbits
whenever those projector diagonals are constant. Group transitivity is one
explicit sufficient hypothesis. We retain the narrower registered statement.

## ST6: scope and remaining work

The gap is a certificate expressed through computable spectral quantities and
the least singular value of a finite linear map; it is not an optimal gap.
Exact certification of concrete nonrational s or tau needs further evidence.
Finite checks corroborate the calculations and do not prove the all-matrix
theorems. Injectivity and a gap do not by themselves establish an optimal
complex Hilbert-space dimension, robust physical self-testing, or a sharp
classical value. Those claims are outside this result.
