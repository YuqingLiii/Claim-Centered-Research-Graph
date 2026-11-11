"""Aggregate the cell x orbit sweep into the per-cell verdict table and check the cover."""
import json, collections, sys
import cert4

LOGS = sys.argv[1:] or ['logs/full.jsonl', 'logs/full7.jsonl']
rs = [json.loads(l) for L in LOGS for l in open(L)]
rs = [r for r in rs if r.get('verdict') in ('SAT', 'UNSAT')]
cells = cert4.cells(10)
by = collections.defaultdict(dict)
for r in rs:
    by[(r['sector'], tuple(r['triple']))][(r['K'], r['Ew'], r['orbit'])] = r

for key in sorted(by):
    sec, tr = key
    tab = by[key]
    print(f"\n=== sector {sec}  triple {tr}")
    tot = 0.0
    ncomplete = 0
    hdr = "  K  |E|   " + " ".join(f"o{j}" for j in range(9)) + "   cell verdict   cell CPU s"
    print(hdr)
    for (K, Ew) in cells:
        row = []
        sats = []
        for j in range(9):
            r = tab.get((K, Ew, j))
            row.append('.' if r is None else ('U' if r['verdict'] == 'UNSAT'
                                              else ('S' if r['verdict'] == 'SAT' else '?')))
            if r is not None:
                tot += r['seconds']
                if r['verdict'] == 'SAT':
                    sats.append(j)
        done = all(x != '.' for x in row)
        cellcpu = sum(tab[(K, Ew, j)]['seconds'] for j in range(9) if (K, Ew, j) in tab)
        verdict = ('SAT' if sats else ('UNSAT' if done else 'incomplete'))
        if done:
            ncomplete += 1
        print(f" {K:2d}  {Ew:3d}   " + "  ".join(row) + f"    {verdict:10s}  {cellcpu:8.1f}")
    print(f"  cells complete: {ncomplete}/{len(cells)};  total CPU {tot:.0f} s")
