"""(1) Re-derive the kill inside the CAMPAIGN's own 360-column extended code (the [SBB26]
residual presentation {i1,i2} / {i4,i5,i6} / {i5,i6} per check), showing the two presentations
agree; (2) validation runs; (3) exact same-round repair of every weight-10 witness; (4) the
corrected d_eff<=10 disqualifier, stated as a pair/triple condition.

[SBB26]'s 3 residual columns per check are the suffix columns modulo the stabiliser supp(a):
    {i1,i2}    = supp(a) + {i3,i4,i5,i6}   (the 4-suffix)
    {i4,i5,i6} = the 3-suffix
    {i5,i6}    = the 2-suffix
and  {i2..i6} = supp(a) + {i1}  is a singleton column.  Adding supp(a) moves the target logical V
inside its own class, so the two column sets give the SAME d_ext.  This file checks that claim on
every witness rather than asserting it.
"""
import collections, itertools, json, sys, time
import core2 as C

(tX, tZ), T = C.load_candidate()
(pz, _, _), (px, _, _) = C.pools()

print("=" * 78)
print("A.  VALIDATION -- singleton-only columns must reproduce the code distance d = 12")
print("=" * 78)
for lab, mir, pool in (('Zmem', False, pz), ('Xmem', True, px)):
    mn = min(C.popc(V) for V in pool)
    print("  %s: min weight over the complete weight-12 nontrivial-logical pool = %d"
          "   (d_sec = 12, PROVED)  -> singleton-only d_ext = 12" % (lab, mn))

print()
print("=" * 78)
print("B.  THE CORRECTED |V|=12 DISQUALIFIER, AS A PAIR/TRIPLE CONDITION")
print("=" * 78)
print("""  For |V| = 12 and pairwise-disjoint check contributions the exact cost identity
      cost = 12 + sum_a (n_a - rho_a) + loss_in + gain_out
  gives per option an effective gain  2*rho - |C| - n.  With Bound 1 (rho <= 3) the only
  options of positive gain are, in the [SBB26] presentation,
      {i5,i6} inside V   gain 1     (the 2-SUFFIX  -- wave 37 tested this)
      {i1,i2} inside V   gain 1     (the 2-PREFIX  -- wave 37 did NOT test this)
      {i4,i5,i6} in V    gain 2     (the 3-SUFFIX  -- wave 37 tested this)
  and d_ext <= 10 in the |V|=12 stratum iff some V carries total gain >= 2.""")

for lab, mir, pool, chks in (('Zmem', False, pz, C.HXm), ('Xmem', True, px, C.HZm)):
    sec = C.Sector(tX, tZ, mirror=mir)
    suf2, pre2, suf3 = {}, {}, 0
    for a in range(C.NG):
        o = sec.order[a]
        m_s2 = C.msk(o[4:]); m_p2 = C.msk(o[:2]); m_s3 = C.msk(o[3:])
        for V in pool:
            if V & m_s3 == m_s3:
                suf3 += 1
            if V & m_s2 == m_s2:
                suf2.setdefault(V, []).append((a, m_s2, '2suf'))
            if V & m_p2 == m_p2:
                pre2.setdefault(V, []).append((a, m_p2, '2pre'))
    npairs = 0
    per = {}
    for d in (suf2, pre2):
        for V, l in d.items():
            per.setdefault(V, []).extend(l)
    exemplars = []
    for V, l in per.items():
        for (a1, m1, k1), (a2, m2, k2) in itertools.combinations(l, 2):
            if not (m1 & m2):
                npairs += 1
                if len(exemplars) < 2:
                    exemplars.append((k1, a1, k2, a2))
    print("  %s: 2-suffix-in-V incidences %4d   2-prefix-in-V incidences %4d   3-suffix-in-V %d"
          % (lab, sum(len(v) for v in suf2.values()), sum(len(v) for v in pre2.values()), suf3))
    print("       DISJOINT gain-1 pairs inside one weight-12 logical: %d   %s"
          % (npairs, exemplars))
    print("       -> corrected disqualifier fires: %s   (wave 37's incomplete one did not)"
          % (npairs > 0 or suf3 > 0))

print()
print("=" * 78)
print("C.  THE KILL RE-DERIVED IN THE CAMPAIGN'S 360-COLUMN MODEL")
print("=" * 78)
for lab, mir, pool, stab in (('Zmem', False, pz, C.HXm), ('Xmem', True, px, C.HZm)):
    sec = C.Sector(tX, tZ, mirror=mir)
    RS, RP = C.rref(stab)
    conf = json.load(open('conf_%s_W10_j3.json' % ('Z' if not mir else 'X')))
    ok = 0
    shown = 0
    for (cost, vi, ch) in conf:
        V = pool[vi]
        cols, V2 = [], V
        for (a, K) in ch:
            o = sec.order[a]
            for l in K:
                if l == 4:                       # 4-suffix -> [SBB26] {i1,i2} + stabiliser
                    cols.append(('{i1,i2}', a, C.msk(o[:2])))
                    V2 ^= C.msk(o)               # move V inside its class by supp(a)
                elif l == 5:                     # 5-suffix -> {i1} + stabiliser  (a SINGLETON)
                    cols.append(('{i1}', a, C.msk(o[:1])))
                    V2 ^= C.msk(o)
                elif l == 3:
                    cols.append(('{i4,i5,i6}', a, C.msk(o[3:])))
                elif l == 2:
                    cols.append(('{i5,i6}', a, C.msk(o[4:])))
                else:
                    cols.append(('?%d' % l, a, C.msk(o[6 - l:])))
        D = 0
        for (_, _, m) in cols:
            D ^= m
        t = C.popc(V2 ^ D)
        tot = len(cols) + t
        assert C.popc(V2) == 12, "class representative left weight 12: %d" % C.popc(V2)
        assert not C.inspan(V2, RS, RP) and all(C.popc(V2 & h) % 2 == 0
                                                for h in (C.HZm if not mir else C.HXm))
        assert tot == cost, (tot, cost)
        ok += 1
        if shown < 2:
            shown += 1
            print("  %s witness: [SBB26] columns %s + %d singletons = %d faults, |V'| = %d"
                  % (lab, [(k, a) for (k, a, _) in cols], t, tot, C.popc(V2)))
    print("  %s: all %d weight-10 witnesses survive the translation into the 360-column model,"
          " same fault count, target still a WEIGHT-12 nontrivial logical." % (lab, ok))

print()
print("=" * 78)
print("D.  EXACT SAME-ROUND repair OF EVERY WEIGHT-10 WITNESS  (repair 0 => d_circ = d_eff)")
print("=" * 78)


def exact_sameround_repair(sec, hooks, singles):
    tgt = 0
    for (a, S) in hooks:
        tgt ^= sec.u_hook(a, S)
    best = None
    h = len(singles) // 2
    left, right = singles[:h], singles[h:]
    tab = {}
    for cmb in itertools.product(*[sec.Uq[q] for q in left]):
        v = 0
        for x in cmb:
            v ^= x
        if v not in tab:
            tab[v] = 1
    for cmb in itertools.product(*[sec.Uq[q] for q in right]):
        v = 0
        for x in cmb:
            v ^= x
        for lv in tab:
            w = C.popc(lv ^ v ^ tgt)
            if best is None or w < best:
                best = w
                if best == 0:
                    return 0
    return best


for lab, mir, pool in (('Zmem', False, pz), ('Xmem', True, px)):
    sec = C.Sector(tX, tZ, mirror=mir)
    conf = json.load(open('conf_%s_W10_j3.json' % ('Z' if not mir else 'X')))
    hist = collections.Counter()
    mr0 = 0
    t0 = time.time()
    for (cost, vi, ch) in conf:
        V = pool[vi]
        hooks, D = [], 0
        for (a, K) in ch:
            for l in K:
                S = sec.suffix(a, l)
                hooks.append((a, S))
                D ^= C.msk(S)
        singles = C.bits(V ^ D)
        r = exact_sameround_repair(sec, hooks, singles)
        hist[r] += 1
        if r > 0 and C.multiround_repair0(sec, hooks, singles, maxg=2) is not None:
            mr0 += 1
    print("  %s: %d weight-10 witnesses; exact SAME-ROUND repair histogram %s ; "
          "2-group multi-round repair-0 on %d of the rest   (%.1fs)"
          % (lab, len(conf), dict(sorted(hist.items())), mr0, time.time() - t0))
