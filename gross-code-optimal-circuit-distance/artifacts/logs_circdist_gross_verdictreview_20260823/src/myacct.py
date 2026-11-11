#!/usr/bin/env python3
"""INDEPENDENT re-accounting of the CIRCDIST.gross W=10 sub-query space.
Written from scratch by the 2026-08-23 verdict reviewer. Does not import cert4 or acct11:
the slot space is built from the ANALYTIC bound re-derived in the review, not from cells()."""
import json, glob, os, sys, collections

W = 10
WMAX = 3                      # asserted; checked separately in mywmax.py
DMIN = 12                     # gross code distance
NORB = 9
CAND = {'Z': (1, 2, 62), 'X': (14, 0, 2)}

# ---- my own cells(): {(K,|E|) : 12 <= |E| <= (W-K)+K*wmax, |E| even, K>=1}
def mycells(W, wmax=WMAX, dmin=DMIN):
    out = []
    for K in range(0, W + 1):
        hi = (W - K) + K * wmax
        E = dmin
        while E <= hi:
            out.append((K, E)); E += 2
    return sorted(out)

cells = mycells(W)
print("MY analytic cells(%d): %d per sector" % (W, len(cells)))
print("  cells per K:", dict(sorted(collections.Counter(K for K, _ in cells).items())))
print("  |E| values:", sorted({E for _, E in cells}))
print("  K=0 cells:", [c for c in cells if c[0] == 0])
e12 = [c for c in cells if c[1] == 12]
print("  |E|=12 cells: %d per sector -> %d slots/sector, %d over both sectors"
      % (len(e12), len(e12) * NORB, 2 * len(e12) * NORB))
TOTAL = 2 * len(cells) * NORB
print("  TOTAL SLOTS = 2 x %d x %d = %d" % (len(cells), NORB, TOTAL))

# ---- scan every jsonl in every repository circdist gross log dir
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
DIRS = sorted(glob.glob(os.path.join(ROOT, 'artifacts', 'logs_circdist_gross_*')))
DIRS = [d for d in DIRS if 'verdictreview' not in d]
recs = []
bad = 0
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        for line in open(L):
            line = line.strip()
            if not line: continue
            try: r = json.loads(line)
            except Exception: bad += 1; continue
            r['_src'] = os.path.join(os.path.basename(D), os.path.basename(L))
            recs.append(r)
print()
print("dirs scanned:", [os.path.basename(d) for d in DIRS])
print("records: %d   unparseable: %d" % (len(recs), bad))
print("verdicts:", dict(collections.Counter(r.get('verdict') for r in recs)))

# ---- keep only decisions on the candidate triples at W=10 with a real orbit
def key(r):
    return (r['sector'], r['K'], r['Ew'], r['orbit'])
dec = collections.defaultdict(list)
for r in recs:
    if r.get('verdict') not in ('SAT', 'UNSAT'): continue
    if r.get('W') != W: continue
    if 'orbit' not in r or r['orbit'] is None or r['orbit'] < 0: continue
    if tuple(r.get('triple', ())) != CAND.get(r.get('sector')): continue
    dec[key(r)].append(r)

print()
print("distinct decided sub-queries (candidate, W=10, orbit>=0): %d" % len(dec))
print("contributing records: %d" % sum(len(v) for v in dec.values()))
multi = {k: v for k, v in dec.items() if len(v) > 1}
print("decided more than once: %d" % len(multi))
conf = [k for k, v in dec.items() if len({r['verdict'] for r in v}) > 1]
print("VERDICT CONFLICTS across duplicates: %d %s" % (len(conf), conf[:5]))
hashconf = []
for k, v in dec.items():
    byh = collections.defaultdict(set)
    for r in v:
        if r.get('cnf_sha256'): byh[r['cnf_sha256']].add(r['verdict'])
    for h, vs in byh.items():
        if len(vs) > 1: hashconf.append((k, h, vs))
print("SAME-HASH verdict disagreements: %d" % len(hashconf))
print("distinct CNF hashes per sub-query:",
      dict(sorted(collections.Counter(len({r['cnf_sha256'] for r in v if r.get('cnf_sha256')})
                                      for v in dec.values()).items())))
print("multiplicity histogram:",
      dict(sorted(collections.Counter(len(v) for v in dec.values()).items())))
print("union verdicts:", dict(collections.Counter(
    ('SAT' if any(r['verdict'] == 'SAT' for r in v) else 'UNSAT') for v in dec.values())))

# ---- classify all TOTAL slots
satdec, enum12only, openl = [], [], []
for sec in ('Z', 'X'):
    for (K, Ew) in cells:
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in dec: satdec.append(k)
            elif Ew == 12: enum12only.append(k)
            else: openl.append(k)
print()
print("--- classification of all %d slots ---" % TOTAL)
print("    SATDEC : %d" % len(satdec))
print("    ENUM12 : %d" % len(enum12only))
print("    OPEN   : %d" % len(openl))
print("    accounted: %d / %d" % (len(satdec) + len(enum12only) + len(openl), TOTAL))
sats = [k for k in satdec if any(r['verdict'] == 'SAT' for r in dec[k])]
print("    of the decided slots, SAT: %d  %s" % (len(sats), sats[:10]))
print("    OPEN LIST:", (openl[:40] if openl else "*** EMPTY ***"), "... total %d" % len(openl))

# ---- how many |E|=12 slots carry a solver record too
e12slots = [(sec, K, 12, o) for sec in ('Z','X') for (K,E) in cells if E==12 for o in range(NORB)]
print()
print("|E|=12 slots total: %d ; of these SATDEC: %d ; ENUM12-only: %d"
      % (len(e12slots), sum(1 for k in e12slots if k in dec),
         sum(1 for k in e12slots if k not in dec)))

# ---- SAT records anywhere in the corpus, on or off candidate
print()
allsat = collections.defaultdict(list)
for r in recs:
    if r.get('verdict') == 'SAT':
        allsat[(r.get('sector'), tuple(r.get('triple', ())), r.get('K'), r.get('Ew'), r.get('orbit'))].append(r)
print("DISTINCT SAT CELLS IN CORPUS: %d" % len(allsat))
for k, v in sorted(allsat.items(), key=lambda kv: str(kv[0])):
    oncand = (CAND.get(k[0]) == k[1])
    print("   %s %s K=%s |E|=%s orbit=%s  ON CANDIDATE: %s  %d records"
          % (k[0], k[1], k[2], k[3], k[4], oncand, len(v)))
print("SAT cells ON THE CANDIDATE: %d"
      % sum(1 for k in allsat if CAND.get(k[0]) == k[1]))
