import itertools, random, sys, json, time, collections
from lift import Schedule, Sector, popc, sameround_repair0
import gross as G
import hunt as H

NG, N = G.NG, G.N
CSSG = G.CSSG
rng = random.Random(20260823)

t0 = time.time()
PX, PZ = H.pools()          # PX: X-logicals (Z-memory sector), PZ: Z-logicals (X-memory)
print("pool sizes", len(PX), len(PZ), "  %.1fs" % (time.time() - t0))

# ---------------- structural checks ---------------------------------------
hist = collections.Counter()
for w in PX[:400]:
    for b in CSSG.Zmask:
        hist[popc(w & b)] += 1
print("STRUCT |V cap supp(b)| over 400 X-logicals x 72 Z-checks:", dict(hist))
histx = collections.Counter()
for w in PX[:400]:
    for a in CSSG.Xmask:
        histx[popc(w & a)] += 1
print("STRUCT |V cap supp(a)| (own sector's X-checks):", dict(histx))

pidxX = H.pair_index(PX)
pidxZ = H.pair_index(PZ)
cov = 0
tot = 0
for a in range(NG):
    for x, y in itertools.combinations(sorted(CSSG.Xchecks[a]), 2):
        tot += 1
        if (x, y) in pidxX:
            cov += 1
print("STRUCT dext-cap pair coverage (X-checks / X-logicals): %d/%d" % (cov, tot))
nV = [len(pidxX[(x, y)]) for a in range(NG)
      for x, y in itertools.combinations(sorted(CSSG.Xchecks[a]), 2) if (x, y) in pidxX]
print("        #weight-12 logicals per in-check pair: min %d max %d mean %.1f"
      % (min(nV), max(nV), sum(nV) / len(nV)))
print("  %.1fs" % (time.time() - t0))

rows = []


def go(sched, tag):
    r = H.run(sched, tag, pidxX, pidxZ, verbose=False)
    rows.append(r)
    if r['status'] != 'OK':
        print("%-28s %s" % (tag, r['status']))
    else:
        print("%-28s glob-int=%-5s pair-int=%3d strict-pair-int=%3d | "
              "Zmem %s hooks2=%s mis=%d/%d | Xmem %s hooks2=%s mis=%d/%d"
              % (tag, r['globally_interleaved'], r['pair_interleaved'],
                 r['strict_pair_interleaved'],
                 r['Zmem']['verdict'],
                 {k: v for k, v in r['Zmem']['hooks2'].items() if v},
                 r['Zmem']['misalign_checks'], NG,
                 r['Xmem']['verdict'],
                 {k: v for k, v in r['Xmem']['hooks2'].items() if v},
                 r['Xmem']['misalign_checks'], NG))
    sys.stdout.flush()
    return r


# ---------------- family A : non-interleaved (the candidate's class) -------
print("\n=== FAMILY A: non-interleaved TI schedules (candidate class) ===")
for name, (XL, XR, ZL, ZR) in [
        ('A1 X-first', ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))),
        ('A2 Z-first', ((6, 7, 8), (9, 10, 11), (0, 1, 2), (3, 4, 5))),
        ('A3 X-first perm', ((2, 0, 1), (5, 3, 4), (8, 6, 7), (11, 9, 10))),
        ('A4 X-first mixLR', ((0, 2, 4), (1, 3, 5), (6, 8, 10), (7, 9, 11)))]:
    print("   ti_ok=%s" % H.ti_ok(XL, XR, ZL, ZR), end=' ')
    go(H.sched_TI(XL, XR, ZL, ZR), name)

# ---------------- family B : check-serial (always (MC), globally interleaved)
print("\n=== FAMILY B: check-serial schedules (random global check order) ===")
NB = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for i in range(NB):
    go(H.sched_check_serial(rng), 'B%d serial' % i)

# ---------------- family C : translation-invariant legal (MC) --------------
print("\n=== FAMILY C: TI legal+(MC) schedules (random search over 12 slot times) ===")
NC = int(sys.argv[2]) if len(sys.argv) > 2 else 200000
found = []
seen = set()
for it in range(NC):
    perm = list(range(12))
    rng.shuffle(perm)
    XL, XR, ZL, ZR = tuple(perm[0:3]), tuple(perm[3:6]), tuple(perm[6:9]), tuple(perm[9:12])
    if not H.ti_ok(XL, XR, ZL, ZR):
        continue
    key = (XL, XR, ZL, ZR)
    if key in seen:
        continue
    seen.add(key)
    found.append(key)
print("   TI legal+(MC) schedules found: %d out of %d random slot-orderings" % (len(found), NC))
rng.shuffle(found)
for i, (XL, XR, ZL, ZR) in enumerate(found[:int(sys.argv[3]) if len(sys.argv) > 3 else 30]):
    go(H.sched_TI(XL, XR, ZL, ZR), 'C%d TI %s|%s|%s|%s' % (i, XL, XR, ZL, ZR))

print("\n=== SUMMARY ===")
ok = [r for r in rows if r['status'] == 'OK']
for lab in ('Zmem', 'Xmem'):
    c = collections.Counter(r[lab]['verdict'] for r in ok)
    print("%s verdicts over %d legal+MC schedules: %s" % (lab, len(ok), dict(c)))
gap = [r for r in ok if r['Zmem']['verdict'] == 'GAPCAND' or r['Xmem']['verdict'] == 'GAPCAND']
print("GAP CANDIDATES:", len(gap))
for r in gap:
    print("   ", r['tag'], r['Zmem']['verdict'], r['Xmem']['verdict'])
json.dump(rows, open('rows.json', 'w'), indent=0)
print("elapsed %.1fs" % (time.time() - t0))
