import glob, re, collections, pathlib

rows = collections.defaultdict(dict)
for f in glob.glob("out/*.txt"):
    for line in open(f):
        m = re.match(r"([ZX]) \((\d+), (\d+), (\d+)\) W=(\d+) orbit (\d+) rep=(.+?): (SAT|UNSAT)\s+([\d.]+)s(.*)", line.strip())
        if not m:
            continue
        sec, a, b, c, W, oi, rep, verdict, el, rest = m.groups()
        key = (sec, (int(a), int(b), int(c)), int(W))
        rows[key][int(oi)] = (verdict, float(el), rest.strip())

out = []
out.append("| sector | tiled assignment | `W` | verdict | time | witness |")
out.append("|---|---|---|---|---|---|")
for key in sorted(rows):
    sec, tr, W = key
    d = rows[key]
    sats = [(oi, v) for oi, v in sorted(d.items()) if v[0] == "SAT"]
    if sats:
        oi, (v, el, rest) = sats[0]
        wt = re.search(r"'weight': (\d+).*?'n_data': (\d+), 'n_res': (\d+), 'Ewt': (\d+)", rest)
        w = (f"weight {wt.group(1)} = {wt.group(2)} data + {wt.group(3)} hooks, "
             f"\\|E\\| = {wt.group(4)}"
             if wt else rest[:60])
        out.append(f"| {sec} | {tr} | {W} | **SAT** (orbit {oi}) | {el:.0f} s | {w} |")
    else:
        n = len(d)
        tot = sum(v[1] for v in d.values())
        out.append(f"| {sec} | {tr} | {W} | UNSAT on {n} orbit reps | {tot:.0f} s | — |")
print("\n".join(out))
