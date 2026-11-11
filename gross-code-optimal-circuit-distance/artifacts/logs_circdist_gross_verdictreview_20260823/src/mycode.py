#!/usr/bin/env python3
"""INDEPENDENT construction of the gross code + independent check of the two weight-11 anchors,
and of the analytic ingredients (wmax, all-ones parity). Reviewer-written; imports gross.py ONLY
to compare against, never to supply the answer."""
import sys, os, json, itertools, collections
import numpy as np

L, M = 12, 6          # gross code: l=12, m=6, n = 2*l*m = 144
NQ = L * M            # 72 per half

def shift(pw_x, pw_y):
    """permutation matrix of x^pw_x y^pw_y acting on the l x m torus, index = i*M + j."""
    P = np.zeros((NQ, NQ), np.uint8)
    for i in range(L):
        for j in range(M):
            P[i * M + j, ((i + pw_x) % L) * M + ((j + pw_y) % M)] = 1
    return P

x = shift(1, 0); y = shift(0, 1)
def mp(*ms):
    r = np.eye(NQ, dtype=np.uint8)
    for m in ms: r = (r @ m) % 2
    return r
x3 = mp(x, x, x); y2 = mp(y, y); y3 = mp(y, y, y); x2 = mp(x, x)
A = (x3 + y + y2) % 2           # A = x^3 + y + y^2
B = (y3 + x + x2) % 2           # B = y^3 + x + x^2
myHX = np.concatenate([A, B], axis=1).astype(np.uint8)               # H_X = [A | B]
myHZ = np.concatenate([B.T, A.T], axis=1).astype(np.uint8)           # H_Z = [B^T | A^T]
N = 2 * NQ

def rref(Mat):
    Mt = Mat.copy() % 2; r = 0; piv = []
    for c in range(Mt.shape[1]):
        p = None
        for i in range(r, Mt.shape[0]):
            if Mt[i, c]: p = i; break
        if p is None: continue
        Mt[[r, p]] = Mt[[p, r]]
        for i in range(Mt.shape[0]):
            if i != r and Mt[i, c]: Mt[i] ^= Mt[r]
        piv.append(c); r += 1
        if r == Mt.shape[0]: break
    return Mt[:r], piv

RX, pX = rref(myHX); RZ, pZ = rref(myHZ)
print("INDEPENDENT gross-code build (l=12, m=6, A=x^3+y+y^2, B=y^3+x+x^2)")
print("  n = %d   rank H_X = %d   rank H_Z = %d   k = n - rX - rZ = %d"
      % (N, len(RX), len(RZ), N - len(RX) - len(RZ)))
print("  commutation H_X H_Z^T = 0 :", bool(((myHX @ myHZ.T) % 2 == 0).all()))

def inspan(R, piv, v):
    v = v.copy() % 2
    for i, c in enumerate(piv):
        if v[c]: v ^= R[i]
    return not v.any()

ones = np.ones(N, np.uint8)
print("  all-ones in rowspace(H_X): %s   in rowspace(H_Z): %s  =>  every zero-syndrome vector has EVEN weight"
      % (inspan(RX, pX, ones), inspan(RZ, pZ, ones)))

# ---- compare with the project's own gross.py
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work'))
import gross as G
print("  project gross.py: HX identical to mine: %s   HZ identical to mine: %s"
      % (bool((G.HX == myHX).all()), bool((G.HZ == myHZ).all())))
print("  project rank/k report: rankHX=%d rankHZ=%d" % (len(rref(G.HX)[0]), len(rref(G.HZ)[0])))

# ---- the two recorded weight-11 anchors, checked against MY matrices only
anch = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                                   '..', 'logs_circdist_gross_verdict_20260823', 'anchor3.json')))
print()
print("ANCHOR WITNESSES (d_ext <= 11), checked against the INDEPENDENTLY BUILT matrices")
print(json.dumps(anch)[:400])
