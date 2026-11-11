#!/usr/bin/env python3
"""Independent iteration-189 exact registry and Z_12 x Z_6 action audit."""
from pathlib import Path
import argparse,gzip,hashlib,json
L,M,G=12,6,72

def canonical_sha(obj):
    h=hashlib.sha256(); enc=json.JSONEncoder(sort_keys=True,separators=(",",":"))
    for s in enc.iterencode(obj): h.update(s.encode())
    return h.hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
def add(x,d):
    i,j=divmod(int(x),M); return ((i+d[0])%L)*M+((j+d[1])%M)
def tq(q,d): q=int(q); return add(q,d) if q<G else G+add(q-G,d)
def te(e,d):
    k,c,q=e.split(':'); return f'{k}:{add(c,d)}:{tq(q,d)}'
def block_key(b): return tuple(sorted((str(a[0]),str(a[1])) for a in b['atoms']))
def tblock(k,d): return tuple(sorted((te(a,d),te(b,d)) for a,b in k))
def selector_key(s):
    return (str(s['sector']),tuple(sorted(map(int,s['data_support']))),tuple(sorted((int(c),tuple(sorted(map(int,ks)))) for c,ks in s['group_kinds'].items())))
def tselector(k,d):
    sec,data,groups=k; return (sec,tuple(sorted(tq(q,d) for q in data)),tuple(sorted((add(c,d),ks) for c,ks in groups)))
def selector_semantics(k):
    sec,data,groups=k; names=[f'D:{q}' for q in data]; gd={str(c):list(ks) for c,ks in groups}
    for c,ks in groups: names += [f'R:{c}:{kind}' for kind in ks]
    return {'sector':sec,'selected_names':names,'data_support':list(data),'group_kinds':gd}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',type=Path,required=True); ap.add_argument('--state',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
    with gzip.open(a.source,'rt') as f: source=json.load(f)
    state=json.loads(a.state.read_text())
    claimed=source.pop('semantic_payload_sha256'); observed=canonical_sha(source); source['semantic_payload_sha256']=claimed; assert observed==claimed
    assert source['schema']=='circdist-gross-iteration189-full-translation-closure-finite-source-v1'
    assert len(source['blocks'])==517140 and len(source['selectors'])==24300
    assert source['expected']['reviewed_blocks']==517140 and source['expected']['selectors']==24300 and source['expected']['assertions']==545838
    assert state['next_iteration']==189 and state['started'] is False and state['stop'] is None
    assert state['block_count']==517140 and state['selector_count']==24300 and state['source_file_sha256']==file_sha(a.source)
    assert state['source_semantic_payload_sha256']==observed
    edges=list(map(str,source['edges'])); edge_set=set(edges); assert len(edges)==len(edge_set)==864
    deltas=[(i,j) for i in range(L) for j in range(M)]; assert len(deltas)==72
    edge_maps={d:{e:te(e,d) for e in edges} for d in deltas}
    assert all(set(m)==edge_set and set(m.values())==edge_set for m in edge_maps.values())
    assert all(edge_maps[(0,0)][e]==e for e in edges)
    composition=0; nonidentity_fixed=0
    for d in deltas:
      if d!=(0,0): nonidentity_fixed += sum(edge_maps[d][e]==e for e in edges)
      for e in deltas:
        s=((d[0]+e[0])%L,(d[1]+e[1])%M)
        for x in edges:
          assert edge_maps[d][edge_maps[e][x]]==edge_maps[s][x]; composition += 1
    assert composition==72*72*864 and nonidentity_fixed==0
    bkeys=[block_key(b) for b in source['blocks']]; bset=set(bkeys); assert len(bkeys)==len(bset)==517140
    skeys=[]; shashes=set()
    for s in source['selectors']:
      k=selector_key(s); semantic=selector_semantics(k); digest=canonical_sha(semantic)
      assert s['selector_semantic_sha256']==digest and s['selected_names']==semantic['selected_names'] and s['data_support']==semantic['data_support'] and s['group_kinds']==semantic['group_kinds']
      assert len(s['selected_names'])==len(set(s['selected_names']))==s['fault_count']<=10
      assert digest not in shashes; shashes.add(digest); skeys.append(k)
    sset=set(skeys); assert len(skeys)==len(sset)==24300
    bg=sg=0
    for d in ((1,0),(0,1)):
      for k in bkeys: assert tblock(k,d) in bset; bg+=1
      for k in skeys: assert tselector(k,d) in sset; sg+=1
    selector_state=canonical_sha([{key:s.get(key) for key in ('mechanism_id','sector','selected_names','data_support','group_kinds','selector_semantic_sha256')} for s in source['selectors']])
    assert selector_state==state['selector_state_sha256']
    families={}
    for b in source['blocks']: families[b['family']]=families.get(b['family'],0)+1
    result={'schema':'circdist-gross-round108-input-registry-invariance-v1','status':'PASS','source_sha256':file_sha(a.source),'semantic_source_sha256':observed,
      'state_sha256':file_sha(a.state),'selector_state_sha256':selector_state,
      'group':{'name':'Z_12 x Z_6','order':72,'elements':72,'edges':864,'edge_bijections':72,'composition_cases':composition,'nonidentity_fixed_edges':nonidentity_fixed,'generators':[[1,0],[0,1]]},
      'blocks':{'count':len(bkeys),'unique_exact_tuples':len(bset),'families':families,'generator_cases':bg},
      'selectors':{'count':len(skeys),'unique_exact_tuples':len(sset),'unique_semantic_hashes':len(shashes),'Xerr':sum(k[0]=='Xerr' for k in skeys),'Zerr':sum(k[0]=='Zerr' for k in skeys),'generator_cases':sg},
      'invariance_theorem':'Closure under generators (1,0) and (0,1) implies closure under all 72 group elements.'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','blocks':len(bkeys),'selectors':len(skeys),'composition_cases':composition,'block_generator_cases':bg,'selector_generator_cases':sg},sort_keys=True))
if __name__=='__main__':main()
