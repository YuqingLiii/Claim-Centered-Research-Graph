"""Render the per-cell result table for the artifact, from all sweep logs."""
import json, collections, sys, os
import cert4

LOGS = [('logs/full.jsonl', 'cert4'), ('logs/t2.jsonl', 'cert4'), ('logs/b6.jsonl', 'cert6'),
        ('logs/full7.jsonl', 'cert7'), ('logs/full7b.jsonl', 'cert7'), ('logs/final.jsonl', 'cert7')]
rs = []
for L, e in LOGS:
    if not os.path.exists(L):
        continue
    for l in open(L):
        r = json.loads(l)
        if (r.get('verdict') in ('SAT', 'UNSAT') and r.get('orbit', -1) >= 0
                and tuple(r['triple']) in ((1, 2, 62), (14, 0, 2))):
            r['enc'] = e
            rs.append(r)
cells = cert4.cells(10)
by = collections.defaultdict(dict)
for r in rs:
    k = (r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'])
    if k in by[(r['sector'], tuple(r['triple']))]:
        old = by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])]
        if old['seconds'] <= r['seconds']:
            continue
    by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])] = r

summary = {}
for key in [('Z', (1, 2, 62)), ('X', (14, 0, 2))]:
    sec, tr = key
    tab = by.get(key, {})
    print(f"\n**sector {sec}, triple {tr}** — `U` = UNSAT, `S` = SAT, `.` = not decided\n")
    print("| `K` | `\\|E\\|` | orbit 0..8 | cell verdict | encoding | cell CPU s | slowest orbit s |")
    print("|---|---|---|---|---|---|---|")
    tot = 0.0; ndone = 0; nsat = 0
    for (K, Ew) in cells:
        row = []; sats = []; times = []; encs = set()
        for j in range(9):
            r = tab.get((K, Ew, j))
            if r is None:
                row.append('.')
            else:
                row.append('U' if r['verdict'] == 'UNSAT' else 'S')
                times.append(r['seconds']); encs.add(r['enc'])
                if r['verdict'] == 'SAT':
                    sats.append(j)
        done = all(x != '.' for x in row)
        if Ew == 12:
            v = 'SAT' if sats else '**UNSAT** (enum12)'
            done = True
        else:
            v = 'SAT' if sats else ('**UNSAT**' if done else 'incomplete')
        ndone += int(done); nsat += int(bool(sats))
        tot += sum(times)
        print(f"| {K} | {Ew} | `{''.join(row)}` | {v} | {'+'.join(sorted(encs)) or '-'} | "
              f"{sum(times):.0f} | {max(times) if times else 0:.0f} |")
    print(f"\n`{ndone}` of `{len(cells)}` cells decided; SAT cells: `{nsat}`; "
          f"CPU for this sector: `{tot:.0f}` s")
    summary[sec] = (ndone, nsat, tot)
print("\nTOTAL:", summary, " grand CPU", round(sum(v[2] for v in summary.values())))
