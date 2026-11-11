from pathlib import Path
import sys,json,itertools,hashlib,collections
ROOT=Path('<repo>/circdist/artifacts/circdist_gross_direct360_proof_round68_20260829')
DATA=Path('/tmp/circdist_round69_work_20260829_a')
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import model as M,round68_build as B
px,pz,lx,lz=B.load_context();ALL=(1<<720)-1;perms=list(itertools.permutations(range(6)))
def mk(qs):return M.mask(qs)
def iterbits(z):
 while z:
  b=z&-z;yield b.bit_length()-1;z^=b
def atom_holds(atom,pos):
 a,op,b=atom;assert op=='<';return pos[int(a.split(':')[2])]<pos[int(b.split(':')[2])]
def parity(v,duals):return [M.popcount(v&z)&1 for z in duals]
def syndrome(v,rows):return sum(((M.popcount(v&h)&1)<<i) for i,h in enumerate(rows))
catobj=json.loads((DATA/'local_order_catalog.json').read_text());pobj=json.loads((DATA/'pair_classification.json').read_text())
cats={};catalog_order_cases=0;unary_mechanisms=0
for e in catobj['entries']:
 lab=e['sector'];a=e['check'];rows=M.Xchecks if lab=='Xerr' else M.Zchecks;pool=px if lab=='Xerr' else pz;duals=lz if lab=='Xerr' else lx;det=M.HZ if lab=='Xerr' else M.HX;stabs=M.HX if lab=='Xerr' else M.HZ;row=rows[a]
 assert e['row']==row and len(e['orders'])==720
 seen=set();unary=0;good=0;records=[]
 for rec,pidx in zip(e['orders'],perms):
  order=tuple(rec['qubits']);assert order==tuple(row[i] for i in pidx) and order not in seen;seen.add(order);pos={q:i for i,q in enumerate(order)}
  opts=[]
  for k,(rp,pp) in enumerate(zip(M.RES_POS,M.PHYS_POS)):
   s=mk(order[i] for i in rp);phys=mk(order[i] for i in pp);z=rec['options'][k]
   assert z['kind']==k and z['canonical_support']==M.bits(s) and z['physical_support']==M.bits(phys)
   assert z['opposite_syndrome']==M.bits(syndrome(s,det)) and z['logical_quotient']==parity(s,duals)
   assert syndrome(s,det)==syndrome(phys,det) and parity(s,duals)==parity(phys,duals)
   opts.append((k,s,phys))
  sm=opts[1][1];V=next((V for V in pool if V&sm==sm),None);isbad=V is not None
  assert rec['unary_bad']==isbad
  if isbad:
   w=rec['unary_witness'];assert mk(w['logical_support'])==V and w['selected_residual']==f'R:{a}:1'
   D=mk(int(x.split(':')[1]) for x in w['singleton_columns']);assert sm^D==V and w['fault_weight']==1+M.popcount(D)==10
   assert syndrome(V,det)==0 and not M.inspan(V,stabs) and any(parity(V,duals));unary+=1;unary_mechanisms+=1
  else:good+=1
  records.append({'order':order,'pos':pos,'opts':opts,'bad':isbad})
 assert (unary,good)==(360,360) and e['unary_bad_order_count']==360 and e['unary_good_order_count']==360
 cats[(lab,a)]=records;catalog_order_cases+=720
pair_order_cases=0;positive_configs=0;physical_replays=0;terms=0;deletion_controls=0;new_cells=0;source_hist=collections.Counter();atom_hist=collections.Counter()
for pe in pobj['pairs']:
 lab,a,b=pe['sector'],pe['a'],pe['b'];A=cats[(lab,a)];B=cats[(lab,b)];duals=lz if lab=='Xerr' else lx;det=M.HZ if lab=='Xerr' else M.HX;stabs=M.HX if lab=='Xerr' else M.HZ;rows=M.Xchecks if lab=='Xerr' else M.Zchecks
 cmap={}
 for c in pe['positive_residual_configurations']:
  s1=mk(c['a_support']);s2=mk(c['b_support']);V=mk(c['logical_support']);D=mk(int(x.split(':')[1]) for x in c['singleton_columns']);key=(c['a_kind'],s1,c['b_kind'],s2);assert key not in cmap;cmap[key]=c
  assert s1^s2^D==V and c['fault_weight']==2+M.popcount(D)<=10 and M.popcount(V)==c['logical_weight'] in (12,14)
  assert syndrome(V,det)==0 and not M.inspan(V,stabs) and c['logical_parities']==parity(V,duals) and any(c['logical_parities'])
  # Exact option predicates reconstruct fixed physical suffixes. Kind 0 differs by its check stabilizer.
  p1=(M.mask(rows[a])^s1) if c['a_kind']==0 else s1;p2=(M.mask(rows[b])^s2) if c['b_kind']==0 else s2;PV=p1^p2^D
  assert syndrome(PV,det)==0 and not M.inspan(PV,stabs) and parity(PV,duals)==parity(V,duals)
  assert c['source'] in ('weight12_pool','weight14_direct');source_hist[c['source']]+=1;positive_configs+=1;physical_replays+=1
 assert len(cmap)==pe['positive_config_count']
 truth=[];new=[];witnessed=0
 for ia,ra in enumerate(A):
  rowmask=0;newmask=0
  for ib,rb in enumerate(B):
   ok=False
   if ra['bad'] or rb['bad']:ok=True
   else:
    for k1,s1,_ in ra['opts']:
     for k2,s2,_ in rb['opts']:
      if (k1,s1,k2,s2) in cmap:ok=True;break
     if ok:break
   if ok:rowmask|=1<<ib
   if ok and not ra['bad'] and not rb['bad']:newmask|=1<<ib;witnessed+=1
  truth.append(rowmask);new.append(newmask)
 assert [hex(z) for z in truth]==pe['truth_rows_hex'] and [hex(z) for z in new]==pe['new_good_good_rows_hex']
 assert sum(len(list(iterbits(z))) for z in truth)==pe['full_bad_order_pairs'] and witnessed==pe['new_good_good_bad_order_pairs'];new_cells+=witnessed;pair_order_cases+=720*720
 union=[0]*720
 for t in pe['deletion_minimal_terms']:
  atoms=[tuple(x) for x in t['atoms']];am=ALL;bm=ALL
  for i,r in enumerate(A):
   if not all(atom_holds(x,r['pos']) for x in atoms if x[0].startswith(('X:'+str(a)+':','Z:'+str(a)+':'))):am&=~(1<<i)
  for i,r in enumerate(B):
   if not all(atom_holds(x,r['pos']) for x in atoms if x[0].startswith(('X:'+str(b)+':','Z:'+str(b)+':'))):bm&=~(1<<i)
  for i in iterbits(am):assert bm & (ALL^truth[i])==0
  for i in iterbits(am):
   if not A[i]['bad']:union[i]|=bm & sum((1<<j) for j,r in enumerate(B) if not r['bad'])
  assert t['atom_count']==len(atoms);terms+=1;atom_hist[len(atoms)]+=1
  assert len(t['deletion_controls'])==len(atoms)
  for ctrl in t['deletion_controls']:
   rem=tuple(ctrl['removed_atom']);trial=[x for x in atoms if x!=rem];ia=ctrl['exposed_a_order_id'];jb=ctrl['exposed_b_order_id']
   assert ctrl['exposed_a_order']==list(A[ia]['order']) and ctrl['exposed_b_order']==list(B[jb]['order'])
   assert all(atom_holds(x,A[ia]['pos'] if x[0].startswith(('X:'+str(a)+':','Z:'+str(a)+':')) else B[jb]['pos']) for x in trial)
   assert ((truth[ia]>>jb)&1)==0;deletion_controls+=1
 assert union==new
 assert len(pe['deletion_minimal_terms'])==pe['term_count']
print(json.dumps({'status':'PASS','catalog_entries':len(cats),'catalog_order_cases':catalog_order_cases,'unary_mechanism_order_replays':unary_mechanisms,'pair_relations':len(pobj['pairs']),'pair_order_cases':pair_order_cases,'positive_residual_configurations':positive_configs,'physical_mechanism_replays':physical_replays,'source_histogram':dict(source_hist),'new_good_good_cells':new_cells,'deletion_minimal_terms':terms,'term_atom_histogram':dict(atom_hist),'deletion_controls':deletion_controls},indent=2,sort_keys=True))
