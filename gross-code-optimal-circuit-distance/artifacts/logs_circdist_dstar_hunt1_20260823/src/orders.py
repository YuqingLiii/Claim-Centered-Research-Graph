"""STEP 1 of the directed hunt: find within-check CNOT orders whose residual set has
d_ext = 11 (no weight-<=10 gamma from the weight-12 logical pool).  Only the 3-suffix
T_a and its 2-sub-suffix S_a matter (|V cap supp(check)| <= 3).
Cost function = #(3-suffixes inside a logical) + #(logicals containing two disjoint 2-suffixes).
Sectors decouple: X-check orders <-> Z-memory, Z-check orders <-> X-memory."""
import itertools, random, sys, json, time, collections
import gross as G, hunt as H
NG=G.NG; CSSG=G.CSSG
rng=random.Random(int(sys.argv[2]) if len(sys.argv)>2 else 1)
PX,PZ=H.pools()

def build(pool, checks):
    pidx=H.pair_index(pool); tidx=H.triple_index(pool)
    # per check: the 60 (T,S) options -> (is T in some V?, list of V containing S)
    opts=[]
    for a in range(len(checks)):
        sup=sorted(checks[a]); o=[]
        for T in itertools.combinations(sup,3):
            tbad = 1 if tidx.get(tuple(sorted(T))) else 0
            for S in itertools.combinations(T,2):
                o.append((T,S,tbad,tuple(pidx.get(tuple(sorted(S)),()))))
        opts.append(o)
    return opts

def cost(state, opts):
    """state[a] = index into opts[a]"""
    c=0; perV=collections.defaultdict(list)
    for a,k in enumerate(state):
        T,S,tbad,Vs=opts[a][k]
        c+=tbad*10
        for V in Vs: perV[V].append((a,frozenset(S)))
    for V,lst in perV.items():
        for (a1,s1),(a2,s2) in itertools.combinations(lst,2):
            if not (s1&s2): c+=1
    return c

def anneal(opts, iters=200000, restarts=6):
    n=len(opts); bestall=None
    for r in range(restarts):
        state=[rng.randrange(len(opts[a])) for a in range(n)]
        c=cost(state,opts)
        for it in range(iters):
            if c==0: break
            a=rng.randrange(n); old=state[a]; new=rng.randrange(len(opts[a]))
            if new==old: continue
            state[a]=new; c2=cost(state,opts)
            if c2<=c: c=c2
            else: state[a]=old
        if bestall is None or c<bestall[0]: bestall=(c,list(state))
        if c==0: break
    return bestall

for tag,pool,checks in (('Z-memory (X-check orders)',PX,CSSG.Xchecks),
                        ('X-memory (Z-check orders)',PZ,CSSG.Zchecks)):
    t0=time.time(); opts=build(pool,checks)
    c,state=anneal(opts, iters=int(sys.argv[1]) if len(sys.argv)>1 else 4000, restarts=4)
    print("%-28s best cost = %d   (%.0fs)" % (tag,c,time.time()-t0))
    if c==0:
        json.dump([opts[a][k][:2] for a,k in enumerate(state)],
                  open('orders_%s.json'%tag[0],'w'))
        print("   -> WROTE a d_ext=11-compatible order assignment")
