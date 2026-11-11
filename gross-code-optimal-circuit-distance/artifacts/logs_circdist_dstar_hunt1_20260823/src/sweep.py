"""Stage-1 sweep: repair-0 RATE over the canonical minimum-weight family, per structured
family.  Reports the minimum rate seen (a rate of 0 would be a GAP CANDIDATE)."""
import itertools, random, sys, json, time, collections
from lift import Schedule, Sector, popc
import gross as G
import hunt as H

NG, N = G.NG, G.N
CSSG = G.CSSG
rng = random.Random(int(sys.argv[4]) if len(sys.argv) > 4 else 20260823)
t0 = time.time()
PX, PZ = H.pools()
pidxX = H.pair_index(PX)
pidxZ = H.pair_index(PZ)

NTI = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
NCOS = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
NSER = int(sys.argv[3]) if len(sys.argv) > 3 else 60

best = {}
log = []


def record(fam, tag, sched, checksZ=None, checksX=None):
    if not sched.legal():
        return None
    if sched.mc_violations():
        return None
    row = {'fam': fam, 'tag': tag,
           'pair_int': sched.interleaved_pairs(),
           'strict_pair_int': sched.strict_interleaved_pairs(),
           'glob_int': sched.globally_interleaved()}
    for lab, mir, pidx, chk in (('Z', False, pidxX, checksZ), ('X', True, pidxZ, checksX)):
        sec = Sector(CSSG, sched, mirror=mir)
        n0, nt, kinds = H.decide_rate(sec, pidx, chk)
        row[lab] = (n0, nt, {k: v for k, v in kinds.items() if v})
        r = n0 / nt if nt else -1
        key = (fam, lab)
        if key not in best or r < best[key][0]:
            best[key] = (r, tag, n0, nt)
    log.append(row)
    return row


# ------------------------------------------------- family A: non-interleaved
print("=== A: non-interleaved TI (candidate class) ===")
for name, p in [('A1 X-first', ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))),
                ('A2 Z-first', ((6, 7, 8), (9, 10, 11), (0, 1, 2), (3, 4, 5))),
                ('A3 perm', ((2, 0, 1), (5, 3, 4), (8, 6, 7), (11, 9, 10))),
                ('A4 mixLR', ((0, 2, 4), (1, 3, 5), (6, 8, 10), (7, 9, 11)))]:
    r = record('A-nonint', name, H.sched_TI(*p), [0], [0])
    print("  %-12s Z %s  X %s" % (name, r['Z'], r['X']))

# ------------------------------------------------- family C: TI legal+MC
print("=== C: TI legal+(MC), a=0 only (translation invariance) ===")
seen = set()
nti = 0
draws = 0
while nti < NTI and draws < NTI * 200:
    draws += 1
    perm = list(range(12))
    rng.shuffle(perm)
    key = (tuple(perm[0:3]), tuple(perm[3:6]), tuple(perm[6:9]), tuple(perm[9:12]))
    if key in seen or not H.ti_ok(*key):
        continue
    seen.add(key)
    nti += 1
    r = record('C-TI', str(key), H.sched_TI(*key), [0], [0])
print("  sampled %d TI legal+(MC) schedules from %d draws (%.2f%% acceptance)"
      % (nti, draws, 100.0 * nti / max(draws, 1)))
print("  min repair-0 rate  Z: %s   X: %s" % (best.get(('C-TI', 'Z')), best.get(('C-TI', 'X'))))
print("  %.0fs" % (time.time() - t0))

# ------------------------------------------------- family D: coset-TI (non-TI, m=2,3)
print("=== D: coset-TI legal+(MC) (m=2,3) -- genuinely non-translation-invariant ===")
ncos = 0
draws = 0
CH = list(range(0, NG, 6))[:6]      # one check per class-orbit sample
while ncos < NCOS and draws < NCOS * 400:
    draws += 1
    m = rng.choice([2, 3])
    XL = [tuple(rng.sample(range(24), 3)) for _ in range(m)]
    XR = [tuple(rng.sample(range(24), 3)) for _ in range(m)]
    ZL = [tuple(rng.sample(range(24), 3)) for _ in range(m)]
    ZR = [tuple(rng.sample(range(24), 3)) for _ in range(m)]
    s = H.sched_coset(m, XL, XR, ZL, ZR)
    if not s.legal() or s.mc_violations():
        continue
    ncos += 1
    record('D-coset', 'm=%d %s' % (m, XL), s, CH, CH)
print("  sampled %d coset legal+(MC) schedules from %d draws" % (ncos, draws))
print("  min repair-0 rate  Z: %s   X: %s" % (best.get(('D-coset', 'Z')), best.get(('D-coset', 'X'))))
print("  %.0fs" % (time.time() - t0))

# ------------------------------------------------- family B: check-serial
print("=== B: check-serial (random global check order; always (MC)) ===")
for i in range(NSER):
    s = H.sched_check_serial(rng)
    record('B-serial', 'ser%d' % i, s, list(range(0, NG, 8)), list(range(0, NG, 8)))
print("  min repair-0 rate  Z: %s   X: %s"
      % (best.get(('B-serial', 'Z')), best.get(('B-serial', 'X'))))
print("  %.0fs" % (time.time() - t0))

print("\n=== SUMMARY (stage 1) ===")
for k in sorted(best):
    r, tag, n0, nt = best[k]
    print("  %-10s %s   MIN repair-0 rate = %d/%d = %.4f   at %s" % (k[0], k[1], n0, nt, r, tag[:60]))
gaps = [row for row in log if row['Z'][0] == 0 or row['X'][0] == 0]
print("GAP CANDIDATES (rate exactly 0 in some sector):", len(gaps))
for g in gaps[:10]:
    print("   ", g['fam'], g['tag'][:70], g['Z'], g['X'])
json.dump(log, open('sweep_log.json', 'w'))
print("schedules decided:", len(log), " elapsed %.0fs" % (time.time() - t0))
