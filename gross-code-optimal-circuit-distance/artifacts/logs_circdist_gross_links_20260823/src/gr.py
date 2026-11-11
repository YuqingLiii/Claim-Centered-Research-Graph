"""Independent gross-code build (reviewer's own; no artifact code reused).
Group G = Z_12 x Z_6, element (i,j) -> index i*6+j.  A = x^3+y+y^2, B = y^3+x+x^2.
H_X = [A|B], H_Z = [B^T|A^T].  Vectors are Python ints (bit p = qubit p);
left half = qubits 0..71, right half = 72..143."""
L, M = 12, 6
NG = L*M            # 72
N  = 2*NG           # 144

def gi(i,j): return (i%L)*M + (j%M)
def gadd(g,d):
    i,j = divmod(g,M); return gi(i+d[0], j+d[1])

Amon = [(3,0),(0,1),(0,2)]      # x^3, y, y^2
Bmon = [(0,3),(1,0),(2,0)]      # y^3, x, x^2

def circ(mons):
    """rows indexed by g; row g has 1 at column g+mon."""
    return [ [gadd(g,mo) for mo in mons] for g in range(NG) ]

Arows = circ(Amon); Brows = circ(Bmon)

# H_X row g: left cols Arows[g], right cols 72+Brows[g]
HX = []
for g in range(NG):
    v = 0
    for c in Arows[g]: v |= 1 << c
    for c in Brows[g]: v |= 1 << (NG + c)
    HX.append(v)
# H_Z = [B^T | A^T]: row g, left col h iff B[h][g]=1 iff g in Brows[h] iff h = g - bmon
HZ = []
for g in range(NG):
    v = 0
    for mo in Bmon: v |= 1 << gadd(g,(-mo[0],-mo[1]))
    for mo in Amon: v |= 1 << (NG + gadd(g,(-mo[0],-mo[1])))
    HZ.append(v)

def popc(x): return bin(x).count('1')

# --- GF(2) linear algebra on int-vectors -------------------------------------
def rref(rows):
    rows = list(rows); piv = []; r = 0
    for c in range(N-1, -1, -1):      # arbitrary column order; use high->low
        p = None
        for k in range(r, len(rows)):
            if rows[k] >> c & 1: p = k; break
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        for k in range(len(rows)):
            if k != r and (rows[k] >> c & 1): rows[k] ^= rows[r]
        piv.append(c); r += 1
        if r == len(rows): break
    return [x for x in rows[:r] if x], piv

def rank(rows):
    return len(rref(rows)[0])

def nullspace(rows, n=N):
    """basis of {v : rows . v = 0}  (rows are int masks, dot = parity of AND)"""
    R, piv = rref(rows)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = 1 << f
        for r, c in zip(R, piv):
            # r has leading 1 at c; solve for bit c
            if (r >> f) & 1: v |= 1 << c
        basis.append(v)
    return basis

def inspan(v, R, piv):
    for r,c in zip(R,piv):
        if (v >> c) & 1: v ^= r
    return v == 0

if __name__ == "__main__":
    assert all(popc(h)==6 for h in HX) and all(popc(h)==6 for h in HZ)
    # CSS commutation
    bad = sum(1 for a in HX for b in HZ if popc(a & b) % 2)
    print("commutation failures:", bad)
    rx, rz = rank(HX), rank(HZ)
    print("rank HX =", rx, " rank HZ =", rz, " k =", N - rx - rz)
    kerX = nullspace(HX)
    print("dim ker HX =", len(kerX))
