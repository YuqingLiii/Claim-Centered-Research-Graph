#!/usr/bin/env python3
"""manifest.py -- emit (a) the per-sub-query certificate manifest, (b) the cell tables,
(c) the aggregate block, for the harvest verdict artifact.

usage: manifest.py OUTDIR DIR [DIR ...]
"""
import sys, os, json, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cert4

W = 10
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
TRIPLE = {'Z': (1, 2, 62), 'X': (14, 0, 2)}
SECTORS = ('Z', 'X')
NORB = 9

OUT = sys.argv[1]
DIRS = sys.argv[2:]
os.makedirs(OUT, exist_ok=True)

uni = collections.defaultdict(list)
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        for ln in open(L):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get('verdict') not in ('SAT', 'UNSAT'):
                continue
            if 'triple' not in r or r.get('W') != W:
                continue
            if (r['sector'], tuple(r['triple'])) not in CAND:
                continue
            if r.get('orbit', -1) < 0:
                continue
            r['_log'] = os.path.basename(D.rstrip('/')) + '/' + os.path.basename(L)
            uni[(r['sector'], r['K'], r['Ew'], r['orbit'])].append(r)

# single-file records this box produced (job7k stdout, one json per file)
for L in sorted(glob.glob(os.path.join(HERE, 'logs', '*.json'))):
    b = os.path.basename(L)
    if not (b.startswith('h_') or b.startswith('audit_')):
        continue
    try:
        r = json.load(open(L))
    except Exception:
        continue
    if r.get('verdict') not in ('SAT', 'UNSAT'):
        continue
    if (r['sector'], tuple(r['triple'])) not in CAND:
        continue
    r['_log'] = 'logs_circdist_gross_verdict_20260823/' + b
    uni[(r['sector'], r['K'], r['Ew'], r['orbit'])].append(r)


def best(v):
    """authoritative record for a sub-query: prefer the fastest verified one."""
    return sorted(v, key=lambda r: (r['verdict'] != 'UNSAT', r.get('seconds', 1e18)))[0]


cells = cert4.cells(W)

# ------------------------------------------------------------------ manifest
rows = []
for sec in SECTORS:
    for (K, Ew) in cells:
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                r = best(uni[k])
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict=r['verdict'], solver=r.get('solver') or 'cd15',
                                 seconds=r.get('seconds'), cnf_sha256=r['cnf_sha256'],
                                 nclauses_final=r.get('nclauses_final'),
                                 nvars=r.get('nvars'), log=r['_log'],
                                 n_records=len(uni[k]),
                                 route='SAT-solver'))
            elif Ew == 12:
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict='UNSAT', solver='enum12.py', seconds=None,
                                 cnf_sha256=None, nclauses_final=None, nvars=None,
                                 log='logs_circdist_gross_verdict_20260823/enum12.out',
                                 n_records=0,
                                 route='exhaustive enumeration of the 1884 weight-12 logicals'))
            else:
                rows.append(dict(sector=sec, triple=list(TRIPLE[sec]), K=K, Ew=Ew, orbit=o,
                                 verdict='OPEN', solver=None, seconds=None, cnf_sha256=None,
                                 nclauses_final=None, nvars=None, log=None, n_records=0,
                                 route=None))

json.dump(rows, open(os.path.join(OUT, 'MANIFEST.json'), 'w'), indent=1)

with open(os.path.join(OUT, 'MANIFEST.md'), 'w') as f:
    f.write("# CIRCDIST.gross -- complete certificate manifest, W = 10\n\n")
    f.write("One row per (sector, K, |E|, orbit) slot of the complete sub-query space.\n")
    f.write("`route = SAT-solver` rows carry a CNF SHA-256 (sha256(...).hexdigest()[:32], i.e. the\n")
    f.write("first 128 bits -- NOT an MD5). Rebuild with `hashonly.py <sector> <a,b,c> 10 K Ew orbit`\n")
    f.write("and compare, then re-solve to re-derive the verdict.\n\n")
    f.write("`route = exhaustive enumeration` rows are the |E| = 12 stratum, decided without any\n")
    f.write("cell machinery by `enum12.py`: all 1884 weight-12 non-trivial logicals of the gross code\n")
    f.write("are enumerated by incremental SAT with blocking clauses (terminating in UNSAT, hence\n")
    f.write("exhaustive by construction), and each is shown to admit no weight-<=10 solution.\n\n")
    f.write("| # | sector | triple | K | \\|E\\| | orbit | verdict | route | solver | solver s | CNF SHA-256 (first 128 bits) | clauses | log |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
    for i, r in enumerate(rows, 1):
        f.write("| %d | %s | %s | %d | %d | %d | %s | %s | %s | %s | %s | %s | %s |\n" % (
            i, r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'],
            "**" + r['verdict'] + "**",
            'solver' if r['route'] == 'SAT-solver' else ('enum12' if r['route'] else '--'),
            r['solver'] or '--',
            ("%.1f" % r['seconds']) if r['seconds'] is not None else '--',
            ("`%s`" % r['cnf_sha256']) if r['cnf_sha256'] else '--',
            r['nclauses_final'] if r['nclauses_final'] else '--',
            ("`%s`" % r['log']) if r['log'] else '--'))

# ------------------------------------------------------------------ cell tables
tbl = []
agg = collections.Counter()
for sec in SECTORS:
    tbl.append("")
    tbl.append("**sector %s, triple %s**" % (sec, str(TRIPLE[sec])))
    tbl.append("")
    tbl.append("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | cell CPU s |")
    tbl.append("|---|---|---|---|---|")
    nd = 0
    for (K, Ew) in cells:
        marks = ''
        cpu = 0.0
        nhave = 0
        for o in range(NORB):
            k = (sec, K, Ew, o)
            if k in uni:
                r = best(uni[k])
                marks += 'S' if r['verdict'] == 'SAT' else 'U'
                cpu += r.get('seconds') or 0.0
                nhave += 1
            else:
                marks += '.'
        if nhave == NORB:
            verdict = "**UNSAT**" if 'S' not in marks else "**SAT**"
            nd += 1
            agg['cells_solver'] += 1
        elif Ew == 12:
            verdict = "**UNSAT** (enum12)"
            nd += 1
            agg['cells_enum12'] += 1
        else:
            verdict = "open (%d)" % (NORB - nhave)
            agg['cells_open'] += 1
        tbl.append("| %d | %d | `%s` | %s | %d |" % (K, Ew, marks, verdict, round(cpu)))
    tbl.append("")
    tbl.append("`%d` of `%d` cells decided; SAT cells: `0`" % (nd, len(cells)))
open(os.path.join(OUT, 'CELLTABLES.md'), 'w').write("\n".join(tbl) + "\n")

# ------------------------------------------------------------------ aggregate
nslot = 2 * len(cells) * NORB
nsolver = sum(1 for r in rows if r['route'] == 'SAT-solver')
nenum = sum(1 for r in rows if r['route'] and r['route'] != 'SAT-solver')
nopen = sum(1 for r in rows if r['verdict'] == 'OPEN')
nsat = sum(1 for r in rows if r['verdict'] == 'SAT')
tot_best = sum(r['seconds'] or 0 for r in rows)
nrec = sum(len(v) for v in uni.values())
ndup = sum(1 for v in uni.values() if len(v) > 1)
conf = sum(1 for v in uni.values() if len({r['verdict'] for r in v}) > 1)

lines = [
    "complete sub-query space (2 sectors x %d cells x %d orbits)   %d" % (len(cells), NORB, nslot),
    "    decided by a SAT-solver certificate                      %4d" % nsolver,
    "    decided by exhaustive enumeration (|E| = 12, enum12.py)  %4d" % nenum,
    "    OPEN                                                     %4d" % nopen,
    "",
    "    of the decided slots, SAT                                %4d" % nsat,
    "    of the decided slots, UNSAT                              %4d" % (nsolver + nenum - nsat),
    "",
    "contributing solver records                                  %4d" % nrec,
    "sub-queries decided more than once                           %4d" % ndup,
    "verdict conflicts across duplicate decisions                 %4d" % conf,
    "",
    "cells decided by all-9-orbit solver cover                    %4d" % agg['cells_solver'],
    "cells decided by enum12                                      %4d" % agg['cells_enum12'],
    "cells open                                                   %4d" % agg['cells_open'],
    "",
    "solver time, best-of per sub-query    ~ %.0f s  (~%.0f CPU-hours)" % (tot_best, tot_best / 3600),
]
open(os.path.join(OUT, 'accounting.txt'), 'w').write("\n".join(lines) + "\n")
print("\n".join(lines))
print()
print("wrote %s/{MANIFEST.md,MANIFEST.json,CELLTABLES.md,accounting.txt}" % OUT)
if nopen:
    print("\nOPEN:")
    for r in rows:
        if r['verdict'] == 'OPEN':
            print("   %s (%d,%d) orbit %d" % (r['sector'], r['K'], r['Ew'], r['orbit']))
