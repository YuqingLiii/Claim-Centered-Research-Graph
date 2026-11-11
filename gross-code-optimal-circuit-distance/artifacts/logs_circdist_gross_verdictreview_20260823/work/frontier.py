import json,collections,os,cert4
done=collections.defaultdict(set)
for L in ('logs/full.jsonl','logs/full7.jsonl','logs/full7b.jsonl','logs/t2.jsonl','logs/b6.jsonl','logs/final.jsonl'):
    if not os.path.exists(L): continue
    for l in open(L):
        try: r=json.loads(l)
        except: continue
        if r.get('verdict') in ('SAT','UNSAT') and r.get('orbit',-1)>=0 and tuple(r['triple']) in ((1,2,62),(14,0,2)):
            done[(r['sector'],r['K'],r['Ew'])].add(r['orbit'])
for sec in ('Z','X'):
    op=[]; nj=0
    for (K,Ew) in cert4.cells(10):
        if Ew==12: continue
        m=9-len(done[(sec,K,Ew)])
        if m: op.append(f"({K},{Ew})x{m}"); nj+=m
    print(f"{sec}: {len(op)} cells open, {nj} orbit sub-queries: " + " ".join(op))
