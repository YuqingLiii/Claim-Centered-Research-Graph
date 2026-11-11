#!/usr/bin/env python3
"""
acct11.py -- AUTHORITATIVE union accounting for CIRCDIST.gross W=10.

Written from scratch for the harvest box.  Does NOT reuse acct.py or frontier.py.

Enumerates the COMPLETE sub-query space
     (sector, K, Ew, orbit)  over  sector in {Z, X},  (K,Ew) in cert4.cells(10),  orbit in 0..8
and classifies every slot as
     SATDEC   decided by a recorded SAT-solver verdict on the candidate triple
     ENUM12   in the |E| = 12 stratum, closed en bloc by enum12.py (0 of 1884 weight-12
              logicals per sector admits a weight <= 10 solution)
     OPEN     neither

Also: dedup, per-key hash consistency, verdict-conflict detection, SAT-record audit.

usage:  python3 acct11.py DIR [DIR ...]
"""
import json, os, sys, glob, collections, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cert4

W = 10
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
SECTORS = ('Z', 'X')
NORB = 9

DIRS = sys.argv[1:]
if not DIRS:
    sys.exit("usage: acct11.py DIR [DIR ...]")

# ---------------------------------------------------------------- ingest
records = []            # every parsed record, with provenance
nlines = nbad = 0
files = []
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        files.append(L)
        for i, ln in enumerate(open(L)):
            ln = ln.strip()
            if not ln:
                continue
            nlines += 1
            try:
                r = json.loads(ln)
            except Exception:
                nbad += 1
                continue
            r['_file'] = L
            r['_line'] = i + 1
            r['_tag'] = os.path.basename(os.path.dirname(L.rstrip('/'))) \
                if os.path.basename(os.path.dirname(L)) == 'logs' else os.path.basename(D)
            r['_short'] = os.path.basename(D) + '/' + os.path.basename(L)
            records.append(r)

print("=" * 78)
print("ACCT11 -- authoritative union accounting, CIRCDIST.gross W=10")
print("=" * 78)
print("log directories scanned : %d" % len(DIRS))
for D in DIRS:
    print("     %s" % D)
print("jsonl files             : %d" % len(files))
print("lines parsed            : %d   unparseable: %d" % (nlines, nbad))
print("records                 : %d" % len(records))
print()

# ---------------------------------------------------------------- global histograms
print("--- verdict histogram over ALL records ---")
print("   ", dict(collections.Counter(r.get('verdict') for r in records)))
print()
print("--- (sector, triple) histogram over ALL records ---")
tri = collections.Counter((r.get('sector'), tuple(r['triple']))
                          for r in records if 'triple' in r)
for k, v in tri.most_common():
    mark = "   <== CANDIDATE" if (k[0], k[1]) in CAND else ""
    print("    %-4s %-14s %5d%s" % (k[0], str(k[1]), v, mark))
print()

# ---------------------------------------------------------------- SAT audit
print("--- SAT-record audit (every SAT record in the corpus) ---")
sats = [r for r in records if r.get('verdict') == 'SAT']
oncand = 0
seen = set()
for r in sats:
    key = (r.get('sector'), tuple(r.get('triple', ())), r.get('K'), r.get('Ew'), r.get('orbit'))
    on = (r.get('sector'), tuple(r.get('triple', ()))) in CAND
    oncand += on
    flags = (r.get('decomposition_ok'), r.get('zero_syndrome'), r.get('nontrivial_logical'))
    print("    %-28s %-4s %-12s K=%-2s |E|=%-3s orbit=%-3s  oncand=%-5s  flags=%s"
          % (r['_short'], r.get('sector'), str(r.get('triple')), r.get('K'),
             r.get('Ew'), r.get('orbit'), on, flags))
    seen.add(key)
print("    SAT records: %d   distinct (sector,triple,K,|E|,orbit): %d   ON CANDIDATE: %d"
      % (len(sats), len(seen), oncand))
print()

# ---------------------------------------------------------------- candidate sub-query union
uni = collections.defaultdict(list)
for r in records:
    if r.get('verdict') not in ('SAT', 'UNSAT'):
        continue
    if 'triple' not in r or r.get('W') != W:
        continue
    if (r['sector'], tuple(r['triple'])) not in CAND:
        continue
    o = r.get('orbit', -1)
    if o is None or o < 0:
        continue
    uni[(r['sector'], r['K'], r['Ew'], o)].append(r)

print("--- dedup on the candidate ---")
mult = collections.Counter(len(v) for v in uni.values())
print("    distinct decided sub-queries       : %d" % len(uni))
print("    contributing records               : %d" % sum(len(v) for v in uni.values()))
print("    multiplicity histogram             : %s" % dict(sorted(mult.items())))
print("    sub-queries with >1 record         : %d   max multiplicity %d"
      % (sum(1 for v in uni.values() if len(v) > 1), max(mult)))

vconf = []
hgroups = collections.Counter()
hconf = []
for k, v in sorted(uni.items()):
    verds = {r['verdict'] for r in v}
    if len(verds) > 1:
        vconf.append((k, [(r['_short'], r['verdict']) for r in v]))
    # hash consistency: records that agree on cnf_sha256 must agree on verdict.
    byh = collections.defaultdict(set)
    for r in v:
        byh[r.get('cnf_sha256')].add(r['verdict'])
    hgroups[len(byh)] += 1
    for h, vs in byh.items():
        if len(vs) > 1:
            hconf.append((k, h, vs))
print("    VERDICT CONFLICTS across duplicates : %d" % len(vconf))
for k, d in vconf:
    print("        !! %s %s" % (str(k), d))
print("    distinct-CNF-hash count per sub-query: %s   (>1 = same sub-query under >1 encoding)"
      % dict(sorted(hgroups.items())))
print("    SAME-HASH verdict disagreements     : %d" % len(hconf))
for k, h, vs in hconf:
    print("        !! %s hash=%s verdicts=%s" % (str(k), h, vs))
print("    union verdicts                      : %s"
      % dict(collections.Counter(v[0]['verdict'] for v in uni.values())))
uv = collections.Counter()
for v in uni.values():
    uv[sorted({r['verdict'] for r in v})[0]] += 1
print()

# ---------------------------------------------------------------- complete space
cells = cert4.cells(W)
print("--- the COMPLETE sub-query space ---")
print("    cert4.cells(%d) : %d cells per sector, %d over both sectors"
      % (W, len(cells), 2 * len(cells)))
Ks = sorted({K for K, _ in cells})
print("    K values present : %s        K=0 cells: %s   (K>=1 everywhere: %s)"
      % (Ks, [c for c in cells if c[0] == 0], all(K >= 1 for K, _ in cells)))
print("    |E| values       : %s" % sorted({E for _, E in cells}))
print("    cells per K      : %s"
      % dict(sorted(collections.Counter(K for K, _ in cells).items())))
e12 = [c for c in cells if c[1] == 12]
print("    |E|=12 cells     : %d per sector (%d slots/sector) -- closed en bloc by enum12.py"
      % (len(e12), len(e12) * NORB))
TOTAL = 2 * len(cells) * NORB
print("    TOTAL SLOTS      : 2 x %d x %d = %d" % (len(cells), NORB, TOTAL))
print()

satdec = []
enum12only = []
openl = []
for sec in SECTORS:
    for (K, Ew) in cells:
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                satdec.append(k)
            elif Ew == 12:
                enum12only.append(k)
            else:
                openl.append(k)

print("--- classification of all %d slots ---" % TOTAL)
print("    SATDEC  (recorded solver verdict)   : %d" % len(satdec))
print("    ENUM12  (|E|=12, closed by enum12)  : %d" % len(enum12only))
print("    OPEN                                 : %d" % len(openl))
print("    ---------------------------------------------")
print("    accounted                            : %d / %d"
      % (len(satdec) + len(enum12only) + len(openl), TOTAL))
print()
print("    denominator used by the wave-6 tables (SATDEC + OPEN, i.e. excluding the")
print("    %d |E|=12 slots that carry no individual solver record) : %d"
      % (len(enum12only), len(satdec) + len(openl)))
print()

# ---------------------------------------------------------------- cells
print("--- cell verdicts ---")
opencells = []
for sec in SECTORS:
    nd = nsat = 0
    for (K, Ew) in cells:
        have = {o for o in range(NORB) if (sec, K, Ew, o) in uni}
        anysat = any(r['verdict'] == 'SAT' for o in have for r in uni[(sec, K, Ew, o)])
        if anysat:
            nsat += 1
        if len(have) == NORB or (Ew == 12 and len(have) < NORB):
            nd += 1
        else:
            opencells.append((sec, K, Ew, sorted(set(range(NORB)) - have)))
    print("    sector %s : %d/%d cells decided;  cells containing a SAT sub-query: %d"
          % (sec, nd, len(cells), nsat))
print("    open cells (both sectors) : %d" % len(opencells))
print()

print("--- THE EXACT OPEN LIST ---")
if not openl:
    print("    *** EMPTY -- the complete W=10 sub-query space is decided ***")
else:
    for sec in SECTORS:
        rows = [(K, Ew, o) for (s, K, Ew, o) in openl if s == sec]
        bycell = collections.defaultdict(list)
        for K, Ew, o in rows:
            bycell[(K, Ew)].append(o)
        print("    %s sector: %d cells, %d sub-queries" % (sec, len(bycell), len(rows)))
        for (K, Ew) in sorted(bycell):
            print("        (%d,%d): %s" % (K, Ew, sorted(bycell[(K, Ew)])))
    print("    by orbit index: %s" % dict(sorted(collections.Counter(o for _, _, _, o in openl).items())))
print()

# ---------------------------------------------------------------- cost
tot_all = sum(r['seconds'] for v in uni.values() for r in v if isinstance(r.get('seconds'), (int, float)))
tot_best = sum(min(r['seconds'] for r in v) for v in uni.values())
print("--- solver time ---")
print("    all distinct records : %.0f s  (%.1f CPU-hours)" % (tot_all, tot_all / 3600))
print("    best-of per sub-query: %.0f s  (%.1f CPU-hours)" % (tot_best, tot_best / 3600))
print()

json.dump({
    'open': openl,
    'decided': len(satdec),
    'enum12': len(enum12only),
    'total': TOTAL,
    'verdict_conflicts': len(vconf),
    'hash_conflicts': len(hconf),
}, open(os.path.join(HERE, 'acct11.json'), 'w'), indent=1)
print("wrote acct11.json")
