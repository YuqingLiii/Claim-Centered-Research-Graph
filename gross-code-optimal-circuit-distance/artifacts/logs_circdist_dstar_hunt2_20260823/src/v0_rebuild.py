"""Stage-2 step 0: independent rebuild + reproduction of every stage-1 audit number."""
import collections, itertools, json, sys
import core2 as C

print("== gross code ==")
print("commutation failures:", sum(1 for a in C.HXm for b in C.HZm if C.popc(a & b) % 2))
ov = collections.Counter(len(o[2]) for o in C.OV)
print("overlap sizes over the %d overlapping (X,Z) pairs: %s ; non-overlapping %d"
      % (len(C.OV), dict(ov), 72 * 72 - len(C.OV)))
lr = set((sum(1 for q in sh if q < C.NG), sum(1 for q in sh if q >= C.NG)) for _, _, sh in C.OV)
print("(left,right) split of every overlap:", lr)
rx = len(C.rref(C.HXm)[0]); rz = len(C.rref(C.HZm)[0])
print("rank H_X = %d  rank H_Z = %d  k = %d" % (rx, rz, C.N - rx - rz))

# all-ones in both row spaces => every logical has EVEN weight (stage-1 section 2)
ones = (1 << C.N) - 1
for nm, rows in (('H_X', C.HXm), ('H_Z', C.HZm)):
    R, piv = C.rref(rows)
    print("all-ones in rowspace(%s): %s" % (nm, C.inspan(ones, R, piv)))

# X-check / X-check support overlaps (needed for the stratum search bookkeeping)
xx = collections.Counter(C.popc(C.HXm[i] & C.HXm[j])
                         for i in range(C.NG) for j in range(i + 1, C.NG))
zz = collections.Counter(C.popc(C.HZm[i] & C.HZm[j])
                         for i in range(C.NG) for j in range(i + 1, C.NG))
print("X-check pair support overlaps:", dict(xx))
print("Z-check pair support overlaps:", dict(zz))

print("\n== weight-12 logical pools ==")
(pz, nz, bz), (px, nx, bx) = C.pools()
print("Z-memory sector pool (X-type logicals): %d wt-12 kernel vectors, %d nontrivial, %d invalid"
      % (nz, len(pz), bz))
print("X-memory sector pool (Z-type logicals): %d wt-12 kernel vectors, %d nontrivial, %d invalid"
      % (nx, len(px), bx))

# BOUND 1 (proved):  |V cap supp(a)| <= (|V|-6)/2  for every nontrivial logical V and check a,
# because V + supp(a) lies in the same nontrivial class and d = 12.  Verify for |V| = 12 -> <= 3.
for nm, pool, chks in (('Zmem', pz, C.HXm), ('Xmem', px, C.HZm)):
    mx = max(C.popc(v & h) for v in pool for h in chks)
    print("%s: max |V cap supp(check)| over the wt-12 pool = %d   (Bound 1 predicts <= 3)"
          % (nm, mx))

print("\n== candidate schedule ==")
(tX, tZ), T = C.load_candidate()
print("T =", T)
print("legal =", C.legal(tX, tZ), " (MC) violations =", len(C.mc_violations(tX, tZ)))
pi, si, gi_ = C.interleave_stats(tX, tZ)
print("pairs interleaved on the overlap = %d / %d ; whole-check interleaved = %d ; globally interleaved = %s"
      % (pi, len(C.OV), si, gi_))

for lab, mir, pool in (('Zmem', False, pz), ('Xmem', True, px)):
    sec = C.Sector(tX, tZ, mirror=mir)
    k2 = collections.Counter(sec.classify(a, sec.suffix(a, 2)) for a in range(C.NG))
    print("%s hook(2-suffix) classification: %s" % (lab, dict(k2)))
    # stage-1 disqualifier: 3-suffix inside a wt-12 logical, or two DISJOINT 2-suffixes in one
    t3 = sum(1 for a in range(C.NG)
             for V in pool if (C.opt_mask(sec, a, (1, 2, 3)) & V) == C.opt_mask(sec, a, (1, 2, 3)))
    per = {}
    for a in range(C.NG):
        s2 = C.opt_mask(sec, a, (1, 2))
        for V in pool:
            if (V & s2) == s2:
                per.setdefault(V, []).append((a, s2))
    npair = sum(1 for V, lst in per.items() for (a1, m1), (a2, m2) in itertools.combinations(lst, 2)
                if not (m1 & m2))
    ncan = sum(len(l) for l in per.values())
    print("   3-suffix-inside-wt12 hits = %d ; disjoint-2-suffix-pairs = %d ; canonical gammas = %d"
          % (t3, npair, ncan))
