#!/usr/bin/env python3
"""Exact standard-library GF(2)/Clifford model for the round-54 certificates.

This is a small trusted checker core, not a solver wrapper.  It rebuilds code and
schedule facts, projects the full Pauli alphabet sector by sector, derives every
one-round (residual, record) effect by forward propagation, independently derives
every spacetime signature by backward Clifford propagation, and exhaustively
excludes lighter logical signatures by meet in the middle.  See README.md for the
mathematical completeness argument and trusted-base boundary.
"""
import itertools
import json
import hashlib
from collections import defaultdict

CORNERS=("NW","NE","SW","SE")
OFF={"NW":(0,0),"NE":(0,1),"SW":(1,0),"SE":(1,1)}

def pc(x): return bin(x).count("1")

def rref(rows,n):
    rows=[int(x) for x in rows if x]
    out=[]; piv=[]
    for c in range(n):
        j=next((j for j,x in enumerate(rows) if (x>>c)&1),None)
        if j is None: continue
        p=rows.pop(j)
        rows=[x^p if (x>>c)&1 else x for x in rows]
        out=[x^p if (x>>c)&1 else x for x in out]
        out.append(p); piv.append(c)
    return out,piv

def rank(rows,n): return len(rref(rows,n)[0])

def in_span(v,rows,n):
    bs,piv=rref(rows,n)
    for b,p in zip(bs,piv):
        if (v>>p)&1: v^=b
    return v==0

def kernel_basis(rows,n):
    bs,piv=rref(rows,n); ps=set(piv); out=[]
    for f in range(n):
        if f in ps: continue
        v=1<<f
        for b,p in zip(bs,piv):
            if (b>>f)&1: v|=1<<p
        assert all(pc(v&r)%2==0 for r in rows)
        out.append(v)
    return out

def span_vectors(bs):
    vals=[0]
    for b in bs: vals += [v^b for v in vals]
    return vals

def min_static(kernel,stab,n):
    best=n+1
    for v in span_vectors(kernel):
        if v and not in_span(v,stab,n): best=min(best,pc(v))
    return best

def mask(supp):
    return sum(1<<q for q in supp)

def surface_code(d=5):
    n=d*d; idx=lambda r,c:r*d+c
    xs=[]; zs=[]; xmeta=[]; zmeta=[]
    for i in range(-1,d):
      for j in range(-1,d):
        cs={nm:idx(i+dr,j+dc) for nm,(dr,dc) in OFF.items() if 0<=i+dr<d and 0<=j+dc<d}
        if len(cs) not in (2,4): continue
        typ="X" if (i+j)%2==0 else "Z"
        if len(cs)==2:
            row=(i in (-1,d-1)); col=(j in (-1,d-1))
            if row and col: continue
            if typ=="X" and not row: continue
            if typ=="Z" and not col: continue
        ent=sorted(cs.values())
        (xs if typ=="X" else zs).append(ent)
        (xmeta if typ=="X" else zmeta).append({"center":[i,j],"corners":cs})
    return {"name":"rotated_surface_d5","n":n,"x_checks":xs,"z_checks":zs,
            "x_logicals":[[idx(r,0) for r in range(d)]],
            "z_logicals":[[idx(0,c) for c in range(d)]],
            "geometry":{"d":d,"x_check_meta":xmeta,"z_check_meta":zmeta}}

def bb_code():
    l=m=3; n2=9; idx=lambda i,j:(i%l)*m+(j%m)
    A=[(0,0),(0,1),(1,0)]; B=[(0,0),(0,1),(2,1)]
    xs=[];zs=[]
    for a in range(n2):
        i,j=divmod(a,m)
        xs.append(sorted([idx(i+e,j+f) for e,f in A]+[n2+idx(i+e,j+f) for e,f in B]))
    for b in range(n2):
        i,j=divmod(b,m)
        zs.append(sorted([idx(i-e,j-f) for e,f in B]+[n2+idx(i-e,j-f) for e,f in A]))
    xr=[mask(s) for s in xs]; zr=[mask(s) for s in zs]
    kx=kernel_basis(zr,18); kz=kernel_basis(xr,18)
    def independent_mod(vs,sub,n):
        out=[]; cur=list(sub); rr=rank(cur,n)
        for v in vs:
            nr=rank(cur+[v],n)
            if nr>rr: out.append(v); cur.append(v); rr=nr
        return out
    xl=independent_mod(kx,xr,18); zl=independent_mod(kz,zr,18)
    assert len(xl)==len(zl)==4
    return {"name":"BB_l3_m3","n":18,"x_checks":xs,"z_checks":zs,
            "x_logicals":[bits(v,18) for v in xl],"z_logicals":[bits(v,18) for v in zl],
            "bb":{"l":3,"m":3,"A":[list(x) for x in A],"B":[list(x) for x in B]}}

def bits(v,n): return [q for q in range(n) if (v>>q)&1]

def surface_schedule(code,piX,piZ,name,member):
    tx={x:i for i,x in enumerate(piX)}; tz={x:i for i,x in enumerate(piZ)}; gates=[]
    for typ,meta,times in (("X",code["geometry"]["x_check_meta"],tx),("Z",code["geometry"]["z_check_meta"],tz)):
      for ci,e in enumerate(meta):
        for nm,q in e["corners"].items(): gates.append({"t":times[nm],"kind":typ,"check":ci,"data":q})
    return {"name":name,"depth":4,"gates":sorted(gates,key=lambda x:(x["t"],x["kind"],x["check"],x["data"])),
            "origin":{"family":"uniform_S4xS4","piX":list(piX),"piZ":list(piZ),"member_index":member}}

def bb_schedule(code):
    A=[tuple(x) for x in code["bb"]["A"]]; B=[tuple(x) for x in code["bb"]["B"]]; l=m=3;n2=9
    idx=lambda i,j:(i%l)*m+(j%m); gates=[]
    for a in range(9):
      i,j=divmod(a,m)
      for s,(e,f) in enumerate(A): gates.append({"t":s,"kind":"X","check":a,"data":idx(i+e,j+f)})
      for s,(e,f) in enumerate(B): gates.append({"t":3+s,"kind":"X","check":a,"data":n2+idx(i+e,j+f)})
    for b in range(9):
      i,j=divmod(b,m)
      for s,(e,f) in enumerate(B): gates.append({"t":6+s,"kind":"Z","check":b,"data":idx(i-e,j-f)})
      for s,(e,f) in enumerate(A): gates.append({"t":9+s,"kind":"Z","check":b,"data":n2+idx(i-e,j-f)})
    return {"name":"BB_NI","depth":12,"gates":sorted(gates,key=lambda x:(x["t"],x["kind"],x["check"],x["data"])),
            "origin":{"family":"BB_noninterleaved_NI","X_layers":"A0,A1,A2,B0,B1,B2","Z_layers":"Bt0,Bt1,Bt2,At0,At1,At2"}}

def derive_ids(code):
    n=code["n"]; na=len(code["x_checks"]); nb=len(code["z_checks"])
    return n,na,nb,n+na+nb,lambda a:n+a,lambda b:n+na+b

def gate4(code,g):
    n,na,nb,nq,ax,az=derive_ids(code)
    if g["kind"]=="X": return ax(g["check"]),g["data"]
    return g["data"],az(g["check"])

def validate_schedule(code,sch):
    n,na,nb,nq,ax,az=derive_ids(code); gates=sch["gates"]; T=sch["depth"]
    need={(k,i,q) for k,rows in (("X",code["x_checks"]),("Z",code["z_checks"])) for i,s in enumerate(rows) for q in s}
    got=[(g["kind"],g["check"],g["data"]) for g in gates]
    assert len(got)==len(set(got))==len(need) and set(got)==need
    layers=defaultdict(list)
    for g in gates: layers[g["t"]].append(g)
    for t in range(T):
        used=[]
        for g in layers[t]: used+=list(gate4(code,g))
        assert len(used)==len(set(used))
        assert used
    tx={(g["check"],g["data"]):g["t"] for g in gates if g["kind"]=="X"}
    tz={(g["check"],g["data"]):g["t"] for g in gates if g["kind"]=="Z"}
    bad=[]
    for a,sa in enumerate(code["x_checks"]):
      for b,sb in enumerate(code["z_checks"]):
        c=sum(tz[(b,q)]<tx[(a,q)] for q in set(sa)&set(sb))%2
        if c: bad.append((a,b))
    assert not bad
    return {"gates":len(gates),"per_layer":[len(layers[t]) for t in range(T)],"mc_bad":bad}

def validate_code(code):
    """Return exact CSS parameters and exhaustively compute both static distances."""
    n=code["n"]
    hx=[mask(x) for x in code["x_checks"]]
    hz=[mask(x) for x in code["z_checks"]]
    assert all(pc(a&b)%2==0 for a in hx for b in hz)
    rx,rz=rank(hx,n),rank(hz,n)
    k=n-rx-rz
    assert len(code["x_logicals"])==len(code["z_logicals"])==k
    # Each listed observable family must separate the corresponding logical
    # quotient.  This also checks dependent-generator cases without assuming
    # the given check rows are a basis.
    for checks,stabs,logs in ((hz,hx,code["z_logicals"]),(hx,hz,code["x_logicals"])):
        for v in span_vectors(kernel_basis(checks,n)):
            detected=any(pc(v&mask(L))%2 for L in logs)
            assert detected == (not in_span(v,stabs,n))
    dx=min_static(kernel_basis(hz,n),hx,n)
    dz=min_static(kernel_basis(hx,n),hz,n)
    xdeg=[sum(q in s for s in code["x_checks"]) for q in range(n)]
    zdeg=[sum(q in s for s in code["z_checks"]) for q in range(n)]
    return {"n":n,"rank_x":rx,"rank_z":rz,"k":k,"d_X":dx,"d_Z":dz,
            "d":min(dx,dz),"x_check_weights":[pc(x) for x in hx],
            "z_check_weights":[pc(x) for x in hz],
            "x_qubit_degrees":xdeg,"z_qubit_degrees":zdeg}

def schedule_family_audit(code,sch):
    """Rebuild the exact 576-member uniform surface family and member index."""
    if sch["origin"]["family"]!="uniform_S4xS4":
        return None
    legal=0; survivors=[]
    for px in itertools.permutations(CORNERS):
      for pz in itertools.permutations(CORNERS):
        cand=surface_schedule(code,px,pz,"candidate",-1)
        try:
            validate_schedule(code,cand)
        except AssertionError:
            # validate_schedule combines conflict legality and MC.  Count
            # conflict-legal candidates separately below.
            pass
        # Conflict-only audit.
        layers=defaultdict(list)
        for g in cand["gates"]: layers[g["t"]].append(g)
        conflict_ok=True
        for t in range(cand["depth"]):
            used=[q for g in layers[t] for q in gate4(code,g)]
            conflict_ok &= len(used)==len(set(used))
        if not conflict_ok: continue
        legal+=1
        try:
            validate_schedule(code,cand)
            survivors.append((list(px),list(pz)))
        except AssertionError:
            pass
    target=(sch["origin"]["piX"],sch["origin"]["piZ"])
    assert target in survivors
    return {"candidates":576,"legal":legal,"legal_mc":len(survivors),
            "member_index":survivors.index(target)}

def hook_geometry(code,sch):
    """Count last-two-CNOT weight-two hook orientations on weight-four checks."""
    d=code["geometry"]["d"]
    times={"X":{},"Z":{}}
    for g in sch["gates"]: times[g["kind"]][(g["check"],g["data"])]=g["t"]
    result={}
    for kind,checks in (("X",code["x_checks"]),("Z",code["z_checks"])):
        vert=horiz=other=0
        for i,supp in enumerate(checks):
            if len(supp)!=4: continue
            qs=sorted(supp,key=lambda q:times[kind][(i,q)])[-2:]
            (r1,c1),(r2,c2)=divmod(qs[0],d),divmod(qs[1],d)
            if c1==c2: vert+=1
            elif r1==r2: horiz+=1
            else: other+=1
        result[kind]={"vertical":vert,"horizontal":horiz,"other":other}
    return result

def full_checks_and_logs(code,sector):
    if sector=="Z": return code["z_checks"],code["z_logicals"],"X"
    return code["x_checks"],code["x_logicals"],"Z"

def one_round_faults(code,sch,sector):
    n,na,nb,nq,ax,az=derive_ids(code); T=sch["depth"]
    layers=defaultdict(list)
    for g in sch["gates"]:
        c,t=gate4(code,g); layers[g["t"]].append((c,t,g))
    busy={t:{q for c,tg,g in layers[t] for q in (c,tg)} for t in range(T)}
    full,logs,comp=full_checks_and_logs(code,sector)
    fullfam="Z" if sector=="Z" else "X"
    fullanc=(lambda i:az(i)) if sector=="Z" else (lambda i:ax(i))
    specs=[]
    for t in range(T):
      for c,tg,g in layers[t]:
       for p in (1,2,3): specs.append({"kind":"cnot","t":t,"control":c,"target":tg,"pbits":p})
      for q in range(nq):
       if q not in busy[t]: specs.append({"kind":"idle","t":t,"qubit":q,"pbits":1})
    for q in range(n,nq): specs.append({"kind":"prep","t":-1,"qubit":q,"pbits":1})
    for i in range(len(full)): specs.append({"kind":"record","family":fullfam,"check":i,"pbits":1})
    def locid(f):
      if f["kind"]=="cnot": return ("cnot",f["t"],f["control"],f["target"])
      if f["kind"] in ("idle","prep"): return (f["kind"],f["t"],f["qubit"])
      return ("record",f["family"],f["check"])
    out=[]
    for f in specs:
      v=[0]*nq; rec=0
      if f["kind"]=="prep": v[f["qubit"]]^=1
      for t in range(T):
        for c,tg,g in layers[t]:
          if comp=="X": v[tg]^=v[c]
          else: v[c]^=v[tg]
        if f["kind"]=="cnot" and f["t"]==t:
          if f["pbits"]&1:v[f["control"]]^=1
          if f["pbits"]&2:v[f["target"]]^=1
        elif f["kind"]=="idle" and f["t"]==t: v[f["qubit"]]^=1
      if f["kind"]=="record": rec^=1<<f["check"]
      E=sum((v[q]&1)<<q for q in range(n))
      u=rec
      for i in range(len(full)):
        if v[fullanc(i)]:u^=1<<i
      syn=sum((pc(E&mask(s))%2)<<i for i,s in enumerate(full))
      obs=sum((pc(E&mask(s))%2)<<i for i,s in enumerate(logs))
      x=dict(f); x.update(E=E,u=u,syndrome=syn,logical=obs,hook=pc(E)>=2,measurement=E==0,location=list(locid(f)))
      out.append(x)
    return out

def physical_alphabet_coverage(code,sch,sector):
    """Audit projection of every full physical Pauli assignment.

    Paulis modulo phase use I=0, X=1, Z=2, Y=3.  Z-memory keeps the X
    component; X-memory keeps the Z component.  The returned projected menu is
    exactly the generator menu used by ``one_round_faults``.  Opposite-family
    record flips project to identity.
    """
    n,na,nb,nq,ax,az=derive_ids(code); T=sch["depth"]
    layers=defaultdict(list)
    for g in sch["gates"]: layers[g["t"]].append(gate4(code,g))
    cnot_locations=len(sch["gates"])
    idle_locations=sum(nq-len({q for pair in layers[t] for q in pair}) for t in range(T))
    prep_locations=na+nb
    record_locations=na+nb
    relevant_bit=1 if sector=="Z" else 2
    two_counts=defaultdict(int)
    for pc0 in range(4):
      for pt0 in range(4):
        if pc0==pt0==0: continue
        pb=(1 if pc0&relevant_bit else 0)|(2 if pt0&relevant_bit else 0)
        two_counts[pb]+=1
    one_counts=defaultdict(int)
    for p in range(1,4): one_counts[1 if p&relevant_bit else 0]+=1
    assert dict(two_counts)=={0:3,1:4,2:4,3:4}
    assert dict(one_counts)=={0:1,1:2}
    projected=cnot_locations*3+idle_locations+prep_locations+(nb if sector=="Z" else na)
    full_assignments=cnot_locations*15+(idle_locations+prep_locations)*3+record_locations
    return {"cnot_locations":cnot_locations,"idle_locations":idle_locations,
            "post_preparation_locations":prep_locations,"record_locations":record_locations,
            "full_nonidentity_assignments":full_assignments,
            "projected_generators":projected,
            "two_qubit_projection_multiplicities":{str(k):two_counts[k] for k in range(4)},
            "one_qubit_projection_multiplicities":{str(k):one_counts[k] for k in range(2)}}

def public_fault(f,sector,n,m,k):
    """Lossless JSON representation of one projected one-round fault effect."""
    out={key:f[key] for key in sorted(f) if key not in ("E","u","syndrome","logical")}
    out.update({"component":"X" if sector=="Z" else "Z",
                "residual_bits":format(f["E"],"0%db"%n)[::-1],
                "record_bits":format(f["u"],"0%db"%m)[::-1],
                "syndrome_bits":format(f["syndrome"],"0%db"%m)[::-1],
                "logical_bits":format(f["logical"],"0%db"%k)[::-1]})
    return out

def fault_effect_bits(f,n,m,k):
    """Compact exact effect record used by the full-alphabet projection catalog."""
    return {"residual_bits":format(f["E"],"0%db"%n)[::-1],
            "record_bits":format(f["u"],"0%db"%m)[::-1],
            "syndrome_bits":format(f["syndrome"],"0%db"%m)[::-1],
            "logical_bits":format(f["logical"],"0%db"%k)[::-1]}

def raw_fault_key(f):
    if f["kind"]=="cnot":
        return ("cnot",f["t"],f["control"],f["target"],f["pbits"])
    if f["kind"] in ("idle","prep"):
        return (f["kind"],f["t"],f["qubit"],1)
    return ("record",f["family"],f["check"],1)

def full_fault_projection_catalog(code,sch,sector,faults=None):
    """Enumerate every allowed nonidentity full-Pauli/record assignment.

    Each row names one physical assignment and either points at its retained
    projected generator or records the zero projected effect.  Thus the JSON
    certificate contains the complete physical alphabet, while avoiding a
    misleading multiplication of identical sector effects.  The verifier
    rebuilds this catalog from the four Pauli bit pairs rather than trusting
    the stored pointer.
    """
    if faults is None: faults=one_round_faults(code,sch,sector)
    n=code["n"];full,logs,_=full_checks_and_logs(code,sector);m=len(full);k=len(logs)
    index={raw_fault_key(f):i for i,f in enumerate(faults)}
    assert len(index)==len(faults)
    zero={"residual_bits":"0"*n,"record_bits":"0"*m,
          "syndrome_bits":"0"*m,"logical_bits":"0"*k}
    rows=[]; pnames=("I","X","Z","Y"); relevant=1 if sector=="Z" else 2
    for g in sch["gates"]:
        c,t=gate4(code,g)
        for cp in range(4):
          for tp in range(4):
            if cp==tp==0: continue
            pb=(1 if cp&relevant else 0)|(2 if tp&relevant else 0)
            j=index.get(("cnot",g["t"],c,t,pb)) if pb else None
            rows.append({"kind":"cnot","t":g["t"],"control":c,"target":t,
                         "pauli":pnames[cp]+pnames[tp],"projected_generator_index":j,
                         "effect":fault_effect_bits(faults[j],n,m,k) if j is not None else zero})
    n0,na,nb,nq,ax,az=derive_ids(code);T=sch["depth"]
    layers=defaultdict(list)
    for g in sch["gates"]:layers[g["t"]].append(gate4(code,g))
    for t in range(T):
      busy={q for pair in layers[t] for q in pair}
      for q in range(nq):
       if q in busy: continue
       for p in range(1,4):
        pb=1 if p&relevant else 0;j=index.get(("idle",t,q,1)) if pb else None
        rows.append({"kind":"idle","t":t,"qubit":q,"pauli":pnames[p],
                     "projected_generator_index":j,
                     "effect":fault_effect_bits(faults[j],n,m,k) if j is not None else zero})
    for q in range(n0,nq):
      for p in range(1,4):
        pb=1 if p&relevant else 0;j=index.get(("prep",-1,q,1)) if pb else None
        rows.append({"kind":"prep","t":-1,"qubit":q,"pauli":pnames[p],
                     "projected_generator_index":j,
                     "effect":fault_effect_bits(faults[j],n,m,k) if j is not None else zero})
    fullfam="Z" if sector=="Z" else "X"
    for family,count in (("X",na),("Z",nb)):
      for i in range(count):
        j=index.get(("record",family,i,1)) if family==fullfam else None
        rows.append({"kind":"record","family":family,"check":i,"flip":1,
                     "projected_generator_index":j,
                     "effect":fault_effect_bits(faults[j],n,m,k) if j is not None else zero})
    assert len(rows)==physical_alphabet_coverage(code,sch,sector)["full_nonidentity_assignments"]
    return rows

def fault_from_public(x):
    """Inverse of public_fault for fields used by the checker."""
    def read_le(s): return sum((ch=="1")<<i for i,ch in enumerate(s))
    f={key:x[key] for key in x if key not in ("component","residual_bits","record_bits",
                                               "syndrome_bits","logical_bits")}
    f.update(E=read_le(x["residual_bits"]),u=read_le(x["record_bits"]),
             syndrome=read_le(x["syndrome_bits"]),logical=read_le(x["logical_bits"]))
    return f

def canonical_json_bytes(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")

def sha_obj(obj): return hashlib.sha256(canonical_json_bytes(obj)).hexdigest()

def signature_digest(keys): return sha_obj([str(x) for x in sorted(keys)])

def signature(f,r,R,m,k):
    det=f["u"]<<(r*m)
    det^=(f["u"]^f["syndrome"])<<((r+1)*m)
    return det | (f["logical"]<<((R+1)*m))

def backward_map(code,sch,sector,R):
    n,na,nb,nq,ax,az=derive_ids(code); T=sch["depth"]
    layers=defaultdict(list)
    for g in sch["gates"]:
      c,t=gate4(code,g); layers[g["t"]].append((c,t,g))
    full,logs,comp=full_checks_and_logs(code,sector);m=len(full);nd=(R+1)*m
    fullfam="Z" if sector=="Z" else "X"; fullanc=(lambda i:az(i)) if sector=="Z" else (lambda i:ax(i))
    sig=[0]*nq
    for q in range(n):
      for i,s in enumerate(full):
       if q in s:sig[q]^=1<<(R*m+i)
      for j,L in enumerate(logs):
       if q in L:sig[q]^=1<<(nd+j)
    got={}
    for r in range(R-1,-1,-1):
      for q in range(n,nq):sig[q]=0
      for i in range(m):
       rec=(1<<(r*m+i))^(1<<((r+1)*m+i))
       sig[fullanc(i)]=rec
       got[(r,"record",fullfam,i,1)]=rec
      for t in range(T-1,-1,-1):
       busy=set()
       for c,tg,g in layers[t]:
        busy|={c,tg}
        for p in (1,2,3):got[(r,"cnot",t,c,tg,p)]=(sig[c] if p&1 else 0)^(sig[tg] if p&2 else 0)
       for q in range(nq):
        if q not in busy:got[(r,"idle",t,q,1)]=sig[q]
       for c,tg,g in layers[t]:
        if comp=="X":sig[c]^=sig[tg]
        else:sig[tg]^=sig[c]
      for q in range(n,nq):got[(r,"prep",-1,q,1)]=sig[q]
    return got

def fkey(r,f):
    if f["kind"]=="cnot":return (r,"cnot",f["t"],f["control"],f["target"],f["pbits"])
    if f["kind"] in ("idle","prep"):return (r,f["kind"],f["t"],f["qubit"],1)
    return (r,"record",f["family"],f["check"],1)

def classes(faults,R,m,k,pred=lambda f:True):
    d={}
    for r in range(R):
      for f in faults:
       if not pred(f):continue
       s=signature(f,r,R,m,k)
       if s:d.setdefault(s,(r,f))
    return d

def comb_effects(keys,j):
    if j==0:return [(0,())]
    out=[]
    for co in itertools.combinations(range(len(keys)),j):
      s=0
      for i in co:s^=keys[i]
      out.append((s,co))
    return out

def find_goal(keys,w,nd):
    a=w//2;b=w-a
    A=comb_effects(keys,a); tab=defaultdict(set)
    for s,_ in A:tab[s&((1<<nd)-1)].add(s>>nd)
    for s,_ in comb_effects(keys,b):
      ds=s&((1<<nd)-1);o=s>>nd
      if any(x!=o for x in tab.get(ds,())):return True
    return False

def find_goal_stats(keys,w,nd):
    """Return a deterministic audit record for the complete w-subset test.

    Splitting w=a+b is complete because every w-element subset has such a
    partition.  A zero-detector, nonzero-logical XOR exists exactly when two
    halves have equal detector masks and different logical masks.  We permit a
    class to occur in both halves.  This is a harmless supermodel: an overlap
    cancels and would yield a lighter witness, already excluded in ascending-w
    use.  Therefore ``found=False`` is a rigorous physical exclusion.
    """
    a=w//2;b=w-a; maskd=(1<<nd)-1
    left=comb_effects(keys,a); tab=defaultdict(set)
    for s,_ in left: tab[s&maskd].add(s>>nd)
    found=False
    right=comb_effects(keys,b)
    for s,_ in right:
        if any(x!=(s>>nd) for x in tab.get(s&maskd,())):
            found=True; break
    serial=[[str(d),[str(o) for o in sorted(tab[d])]] for d in sorted(tab)]
    return {"weight":w,"split":[a,b],"left_combinations":len(left),
            "right_combinations":len(right),"left_detector_buckets":len(tab),
            "left_effect_states":sum(len(v) for v in tab.values()),
            "left_catalog_sha256":sha_obj(serial),"logical_found":found}

def exclude_below(keys,bound,nd):
    return [find_goal(keys,w,nd) for w in range(1,bound)]

def find_actual(faults,R,m,k,w,require=None,pred=lambda f:True):
    items=[]
    for r in range(R):
      for f in faults:
       if pred(f):
        s=signature(f,r,R,m,k)
        if s:items.append((s,r,f))
    nd=(R+1)*m; goalobs=range(1,1<<k)
    # exhaustive MITM with physical representative lists; intended only w<=4
    a=w//2;b=w-a;tab=defaultdict(list)
    for co in itertools.combinations(range(len(items)),a):
      s=0;loc=[];flag=False
      for i in co:
       s^=items[i][0];r,f=items[i][1:];loc.append((r,tuple(f["location"])));flag|=bool(require and require(f))
      if len(loc)==len(set(loc)):tab[s].append((co,flag))
    for co2 in itertools.combinations(range(len(items)),b):
      s2=0;loc2=[];flag2=False
      for i in co2:
       s2^=items[i][0];r,f=items[i][1:];loc2.append((r,tuple(f["location"])));flag2|=bool(require and require(f))
      if len(loc2)!=len(set(loc2)):continue
      for o in goalobs:
       target=o<<nd
       for co1,flag1 in tab.get(s2^target,[]):
        idx=list(co1)+list(co2);loc=[(items[i][1],tuple(items[i][2]["location"])) for i in idx]
        if len(loc)!=len(set(loc)):continue
        if require and not(flag1 or flag2):continue
        return [(items[i][1],items[i][2]) for i in idx]
    return None

def reach_min(keys,maxw):
    # exact min weight for each abstract XOR sum up to maxw, via combinations
    d={0:0}
    for w in range(1,maxw+1):
      for s,_ in comb_effects(keys,w):d.setdefault(s,w)
    return d

def has_flagged_goal(allkeys, flagged_sigs, cap,nd):
    # supermodel: choose one flagged elementary effect then <=cap-1 arbitrary signatures.
    # Pair two reachable halves of at most floor/ceil((cap-1)/2), allowing overlap.
    la=(cap-1)//2;lb=(cap-1)-la
    A=reach_min(allkeys,la);B=reach_min(allkeys,lb)
    bydet=defaultdict(dict);maskd=(1<<nd)-1
    for s,w in B.items():
      d=s&maskd;o=s>>nd;bydet[d][o]=min(w,bydet[d].get(o,999))
    for f in sorted(set(flagged_sigs)):
      fd=f&maskd;fo=f>>nd
      for a,wa in A.items():
       needd=fd^(a&maskd); ao=a>>nd
       for bo,wb in bydet.get(needd,{}).items():
        if 1+wa+wb<=cap and (fo^ao^bo)!=0:return True
    return False

def flagged_goal_stats(allkeys,flagged_sigs,cap,nd):
    la=(cap-1)//2;lb=(cap-1)-la
    A=reach_min(allkeys,la);B=reach_min(allkeys,lb)
    bydet=defaultdict(dict);maskd=(1<<nd)-1
    for s,w in B.items():
      d=s&maskd;o=s>>nd;bydet[d][o]=min(w,bydet[d].get(o,999))
    found=False
    for f in sorted(set(flagged_sigs)):
      fd=f&maskd;fo=f>>nd
      for a,wa in A.items():
       for bo,wb in bydet.get(fd^(a&maskd),{}).items():
        if 1+wa+wb<=cap and (fo^(a>>nd)^bo)!=0:
            found=True; break
       if found: break
      if found: break
    serial=[[str(d),[[str(o),w] for o,w in sorted(bydet[d].items())]] for d in sorted(bydet)]
    return {"cap":cap,"flagged_signatures":len(set(flagged_sigs)),
            "arbitrary_effect_classes":len(allkeys),"half_caps":[la,lb],
            "left_reachable_states":len(A),"right_reachable_states":len(B),
            "right_catalog_sha256":sha_obj(serial),"logical_found":found}

def fault_to_assignment(r,f,sector):
    """Choose an allowed full Pauli whose retained component is projected fault f."""
    comp="X" if sector=="Z" else "Z"; kind=f["kind"]
    if kind=="cnot":
        p=(comp if f["pbits"]&1 else "I")+(comp if f["pbits"]&2 else "I")
        return {"round":r,"kind":kind,"t":f["t"],"control":f["control"],
                "target":f["target"],"pauli":p}
    if kind in ("idle","prep"):
        return {"round":r,"kind":kind,"t":f["t"],"qubit":f["qubit"],"pauli":comp}
    return {"round":r,"kind":"record","family":f["family"],"check":f["check"],"flip":1}

def assignment_location(a):
    if a["kind"]=="cnot": return (a["round"],"cnot",a["t"],a["control"],a["target"])
    if a["kind"] in ("idle","prep"): return (a["round"],a["kind"],a["t"],a["qubit"])
    return (a["round"],"record",a["family"],a["check"])

def replay_witness(code,sch,R,sector,assignments):
    """Forward full-symplectic replay against every Definition-2.7 detector.

    This path does not call one_round_faults, signature, or backward_map.  It is
    the trusted upper-bound checker.  Because certificate witnesses are sector
    pure, silence of the full-family differences plus zero opposite records is
    also silence against the Definition-3.5 canonical space decomposition.
    """
    assert sector in ("Z","X") and R>=1
    n,na,nb,nq,ax,az=derive_ids(code);T=sch["depth"]
    layers=defaultdict(list);busy=defaultdict(set)
    for g in sch["gates"]:
        c,t=gate4(code,g);layers[g["t"]].append((c,t));busy[g["t"]]|={c,t}
    locs=[assignment_location(a) for a in assignments]
    assert len(locs)==len(set(locs))
    byslot=defaultdict(list); recflip=defaultdict(int)
    for a in assignments:
        assert 0<=a["round"]<R
        kind=a["kind"]
        if kind=="cnot":
            assert (a["control"],a["target"]) in layers[a["t"]]
            assert len(a["pauli"])==2 and a["pauli"]!="II"
            byslot[(a["round"],a["t"])].append(a)
        elif kind=="idle":
            assert 0<=a["t"]<T and a["qubit"] not in busy[a["t"]]
            assert a["pauli"] in "XYZ"
            byslot[(a["round"],a["t"])].append(a)
        elif kind=="prep":
            assert a["t"]==-1 and n<=a["qubit"]<nq and a["pauli"] in "XYZ"
            byslot[(a["round"],-1)].append(a)
        else:
            lim=na if a["family"]=="X" else nb
            assert kind=="record" and 0<=a["check"]<lim and a["flip"]==1
            recflip[(a["family"],a["check"],a["round"]) ]^=1
    x=[0]*nq;z=[0]*nq;records={}
    def put(q,p):
        if p in ("X","Y"):x[q]^=1
        if p in ("Z","Y"):z[q]^=1
    for r in range(R):
        for q in range(n,nq):x[q]=z[q]=0
        for a in byslot[(r,-1)]:put(a["qubit"],a["pauli"])
        for t in range(T):
            for c,tg in layers[t]:x[tg]^=x[c];z[c]^=z[tg]
            for a in byslot[(r,t)]:
                if a["kind"]=="cnot":put(a["control"],a["pauli"][0]);put(a["target"],a["pauli"][1])
                else:put(a["qubit"],a["pauli"])
        for i in range(na):records[("X",i,r)]=z[ax(i)]^recflip[("X",i,r)]
        for i in range(nb):records[("Z",i,r)]=x[az(i)]^recflip[("Z",i,r)]
    rho=x[:n] if sector=="Z" else z[:n]
    fullfam="Z" if sector=="Z" else "X";partfam="X" if sector=="Z" else "Z"
    full=code["z_checks"] if sector=="Z" else code["x_checks"]
    part=code["x_checks"] if sector=="Z" else code["z_checks"]
    terminal=[sum(rho[q] for q in s)%2 for s in full]
    detectors=[]
    for i in range(len(full)):
      for r in range(R+1):
        cur=records[(fullfam,i,r)] if r<R else terminal[i]
        prev=records[(fullfam,i,r-1)] if r>0 else 0
        detectors.append((fullfam,i,r,cur^prev))
    for i in range(len(part)):
      for r in range(1,R):detectors.append((partfam,i,r,records[(partfam,i,r)]^records[(partfam,i,r-1)]))
    logs=code["z_logicals"] if sector=="Z" else code["x_logicals"]
    obs=[sum(rho[q] for q in L)%2 for L in logs]
    required="X" if sector=="Z" else "Z"
    sector_pure=True
    for a in assignments:
        if a["kind"]=="record": sector_pure &= a["family"]==fullfam
        else: sector_pure &= all(p in ("I",required) for p in a["pauli"])
    opposite_records=[v for (fam,i,r),v in records.items() if fam==partfam and v]
    full_silent=all(v==0 for fam,i,r,v in detectors if fam==fullfam)
    short_silent=all(v==0 for fam,i,r,v in detectors)
    canonical_silent=sector_pure and full_silent and not opposite_records
    return {"weight":len(assignments),"distinct_locations":len(set(locs)),
            "definition_2_7_silent":short_silent,"canonical_silent":canonical_silent,
            "sector_pure":sector_pure,"observable":obs,"logical":any(obs),
            "fired_detectors":[[fam,i,r] for fam,i,r,v in detectors if v],
            "terminal_data_x_bits":x[:n],"terminal_data_z_bits":z[:n]}

def bare_logical_witness(code,sch,sector,r):
    """Insert a spatial logical on data immediately after the final layer."""
    n=code["n"]
    if sector=="Z": checks=[mask(x) for x in code["z_checks"]];stabs=[mask(x) for x in code["x_checks"]]
    else: checks=[mask(x) for x in code["x_checks"]];stabs=[mask(x) for x in code["z_checks"]]
    candidates=(v for v in span_vectors(kernel_basis(checks,n)) if v and not in_span(v,stabs,n))
    logical=bits(min(candidates,key=lambda v:(pc(v),v)),n)
    component="X" if sector=="Z" else "Z";last=sch["depth"]-1
    layer=[]
    for g in sch["gates"]:
        if g["t"]==last: layer.append(gate4(code,g))
    out=[]
    for q in logical:
        pair=next((p for p in layer if q in p),None)
        if pair is None:
            out.append({"round":r,"kind":"idle","t":last,"qubit":q,"pauli":component})
        else:
            c,t=pair;pauli=(component if c==q else "I")+(component if t==q else "I")
            out.append({"round":r,"kind":"cnot","t":last,"control":c,"target":t,"pauli":pauli})
    return out

def translate_witness(assignments,offset):
    return [dict(a,round=a["round"]+offset) for a in assignments]

def make_instances():
    surf=surface_code(5)
    std=surface_schedule(surf,("NW","NE","SW","SE"),("NW","SW","NE","SE"),"surface_standard_member_1",1)
    mis=surface_schedule(surf,("NW","SW","NE","SE"),("NW","NE","SW","SE"),"surface_classD_member_2",2)
    bb=bb_code(); ni=bb_schedule(bb)
    return [("surface_standard_d5",surf,std,5),("surface_classD_d5",surf,mis,5),("BB_18_4_4_NI",bb,ni,4)]
