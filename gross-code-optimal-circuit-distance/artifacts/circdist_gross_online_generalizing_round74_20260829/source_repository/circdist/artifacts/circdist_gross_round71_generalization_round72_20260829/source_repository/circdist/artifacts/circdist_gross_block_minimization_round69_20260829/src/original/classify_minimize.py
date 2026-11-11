from pathlib import Path
import sys,json,itertools,hashlib,time,collections
ROOT=Path('<repo>/circdist/artifacts/circdist_gross_direct360_proof_round68_20260829')
OUT=Path('/tmp/circdist_round69_work_20260829_a')
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import model as M,round68_build as B
px,pz,lx,lz=B.load_context();v=json.loads((ROOT/'verification.json').read_text());c=json.loads((ROOT/'cegar_continuation5.json').read_text())
blocks=[]
for lab in ('Xerr','Zerr'):blocks.append(('primary-'+lab,lab,v['sectors'][lab]['mechanism']))
for row in c['ledger']:
 for lab in ('Xerr','Zerr'):blocks.append((f"continuation-{row['iteration']}-{lab}",lab,row['sectors'][lab]['mechanism']))
w14={lab:json.loads((OUT/f'{lab}_w14_individual.json').read_text())['weight14_completions'] for lab in ('Xerr','Zerr')}
PERMS=list(itertools.permutations(range(6)));ALL720=(1<<720)-1

def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def iterbits(z):
 while z:
  b=z&-z;yield b.bit_length()-1;z^=b

def atoms_for(lab,a,row,k,s):
 S=set(M.bits(s));O=set(row)-S;kind='X' if lab=='Xerr' else 'Z';out=[]
 if k==0:
  for q in sorted(S):
   for r in sorted(O):out.append((M.edge_key(kind,a,q),'<',M.edge_key(kind,a,r)))
 else:
  for q in sorted(O):
   for r in sorted(S):out.append((M.edge_key(kind,a,q),'<',M.edge_key(kind,a,r)))
 return tuple(sorted(out))

cats={};used={(lab,a) for _,lab,m in blocks for a in {f['check'] for f in m['faults'] if f['elementary_fault']=='ancilla_hook_suffix'}}
for lab,a in sorted(used):
 rows=M.Xchecks if lab=='Xerr' else M.Zchecks;pool=px if lab=='Xerr' else pz;duals=lz if lab=='Xerr' else lx;det=M.HZ if lab=='Xerr' else M.HX;row=rows[a]
 omasks=collections.defaultdict(int);orders=[];cmpm={}
 for oi,p in enumerate(PERMS):
  order=tuple(row[i] for i in p);pos={q:i for i,q in enumerate(order)}
  opts=[]
  for k,poss in enumerate(M.RES_POS):
   s=M.mask(order[j] for j in poss);phys=M.mask(order[j] for j in M.PHYS_POS[k]);omasks[(k,s)]|=1<<oi
   opts.append({'kind':k,'canonical_support':M.bits(s),'canonical_mask_hex':hex(s),'physical_support':M.bits(phys),'opposite_syndrome':M.bits(sum(((M.popcount(s&h)&1)<<b) for b,h in enumerate(det))),'logical_quotient':[M.popcount(s&z)&1 for z in duals]})
  sm=M.mask(order[3:]);V=next((V for V in pool if V&sm==sm),None);unary=V is not None
  orders.append({'order_id':oi,'qubits':list(order),'options':opts,'unary_bad':unary,'unary_witness':None if V is None else {'logical_support':M.bits(V),'selected_residual':f'R:{a}:1','singleton_columns':[f'D:{q}' for q in M.bits(V^sm)],'fault_weight':10}})
 for q in row:
  for r in row:
   if q==r:continue
   z=0
   for oi,p in enumerate(PERMS):
    order=tuple(row[i] for i in p)
    if order.index(q)<order.index(r):z|=1<<oi
   cmpm[(M.edge_key('X' if lab=='Xerr' else 'Z',a,q),'<',M.edge_key('X' if lab=='Xerr' else 'Z',a,r))]=z
 unarymask=sum((1<<o['order_id']) for o in orders if o['unary_bad']);assert unarymask.bit_count() if hasattr(int,'bit_count') else True
 cats[(lab,a)]={'row':row,'orders':orders,'option_masks':dict(omasks),'comparison_masks':cmpm,'unary_mask':unarymask,'good_mask':ALL720^unarymask}
 print('CAT',lab,a,'unary',len(list(iterbits(unarymask))),flush=True)

def poolbest(lab,rr):
 pool=px if lab=='Xerr' else pz;best=None
 for i,V in enumerate(pool):
  gain=2*M.popcount(V&rr)-M.popcount(rr)
  if best is None or gain>best[0]:best=(gain,i,V)
 return best

def mask_atoms(cat,atoms):
 z=ALL720
 for x in atoms:z &= cat['comparison_masks'][x]
 return z

def rect_sound(A,B,badrows):
 for i in iterbits(A):
  if B & (ALL720^badrows[i]):return False
 return True

pair_results={};pair_keys=set()
for bid,lab,m in blocks:
 checks=sorted({f['check'] for f in m['faults'] if f['elementary_fault']=='ancilla_hook_suffix'})
 for a,b in itertools.combinations(checks,2):pair_keys.add((lab,a,b))
for pi,(lab,a,b) in enumerate(sorted(pair_keys)):
 ca,cb=cats[(lab,a)],cats[(lab,b)];configs=[];newrows=[0]*720
 optsA=sorted(ca['option_masks']);optsB=sorted(cb['option_masks'])
 cache={}
 for oa in optsA:
  k1,s1=oa;Ag=ca['option_masks'][oa]&ca['good_mask']
  if not Ag:continue
  for ob in optsB:
   k2,s2=ob;Bg=cb['option_masks'][ob]&cb['good_mask']
   if not Bg:continue
   rr=s1^s2;gain,vi,V=poolbest(lab,rr);source=None
   if gain>=4:source='weight12_pool'
   elif k1==k2==1 and not(s1&s2) and str(rr) in w14[lab]:
    source='weight14_direct';V=sum(1<<q for q in w14[lab][str(rr)]['support']);vi=None
   if source is None:continue
   singles=M.bits(V^rr);cost=2+len(singles);assert cost<=10
   conf={'a':a,'b':b,'a_kind':k1,'b_kind':k2,'a_support':M.bits(s1),'b_support':M.bits(s2),'logical_support':M.bits(V),'logical_weight':M.popcount(V),'logical_parities':w14[lab].get(str(rr),{}).get('logical_parities') if source=='weight14_direct' else [M.popcount(V&z)&1 for z in (lz if lab=='Xerr' else lx)],'singleton_columns':[f'D:{q}' for q in singles],'fault_weight':cost,'source':source,'a_atoms':atoms_for(lab,a,ca['row'],k1,s1),'b_atoms':atoms_for(lab,b,cb['row'],k2,s2)}
   configs.append(conf)
   for i in iterbits(Ag):newrows[i]|=Bg
 # full bad relation = unary A or unary B or new pair region
 badrows=[]
 for i in range(720):badrows.append(ALL720 if ((ca['unary_mask']>>i)&1) else (cb['unary_mask']|newrows[i]))
 # exact configs -> deletion-minimal implicants. One forward and one reverse deletion order.
 terms={}
 for conf in configs:
  base=list(conf['a_atoms']+conf['b_atoms'])
  for reverse in (False,True):
   cur=list(base);seq=list(reversed(base)) if reverse else list(base)
   for atom in seq:
    if atom not in cur:continue
    trial=cur.copy();trial.remove(atom)
    aa=[x for x in trial if x[0].split(':')[1]==str(a)];bb=[x for x in trial if x[0].split(':')[1]==str(b)]
    A=mask_atoms(ca,aa);B=mask_atoms(cb,bb)
    if rect_sound(A,B,badrows):cur=trial
   aa=tuple(sorted(x for x in cur if x[0].split(':')[1]==str(a)));bb=tuple(sorted(x for x in cur if x[0].split(':')[1]==str(b)));A=mask_atoms(ca,aa);B=mask_atoms(cb,bb)
   key=aa+bb
   if key not in terms:terms[key]={'atoms':key,'a_atoms':aa,'b_atoms':bb,'a_mask':A,'b_mask':B,'source_config':conf}
 # retain terms that cover a new good-good cell, and find deletion witnesses
 final=[]
 for t in terms.values():
  A=t['a_mask']&ca['good_mask'];B=t['b_mask']&cb['good_mask'];covers=False
  for i in iterbits(A):
   if B&newrows[i]:covers=True;break
  if not covers:continue
  controls=[]
  for atom in t['atoms']:
   trial=[x for x in t['atoms'] if x!=atom];aa=[x for x in trial if x[0].split(':')[1]==str(a)];bb=[x for x in trial if x[0].split(':')[1]==str(b)];A2=mask_atoms(ca,aa);B2=mask_atoms(cb,bb);wit=None
   for i in iterbits(A2):
    good=B2&(ALL720^badrows[i])
    if good:wit=(i,next(iterbits(good)));break
   assert wit is not None
   controls.append({'removed_atom':atom,'exposed_a_order_id':wit[0],'exposed_b_order_id':wit[1],'exposed_a_order':ca['orders'][wit[0]]['qubits'],'exposed_b_order':cb['orders'][wit[1]]['qubits']})
  final.append({'atoms':[list(x) for x in t['atoms']],'atom_count':len(t['atoms']),'a_order_count':len(list(iterbits(t['a_mask']))),'b_order_count':len(list(iterbits(t['b_mask']))),'source_config':t['source_config'],'deletion_controls':controls})
 # verify term union covers exactly newrows on good-good
 union=[0]*720
 for t in final:
  A=mask_atoms(ca,[tuple(x) for x in t['atoms'] if x[0].split(':')[1]==str(a)])&ca['good_mask'];B=mask_atoms(cb,[tuple(x) for x in t['atoms'] if x[0].split(':')[1]==str(b)])&cb['good_mask']
  for i in iterbits(A):union[i]|=B
 assert union==newrows
 full_count=sum(len(list(iterbits(z))) for z in badrows);new_count=sum(len(list(iterbits(z))) for z in newrows)
 pair_results[(lab,a,b)]={'sector':lab,'a':a,'b':b,'positive_residual_configurations':configs,'positive_config_count':len(configs),'truth_rows_hex':[hex(z) for z in badrows],'new_good_good_rows_hex':[hex(z) for z in newrows],'full_bad_order_pairs':full_count,'new_good_good_bad_order_pairs':new_count,'deletion_minimal_terms':final,'term_count':len(final),'term_atom_histogram':dict(collections.Counter(t['atom_count'] for t in final))}
 print('PAIR',pi+1,'/',len(pair_keys),lab,a,b,'configs',len(configs),'newcells',new_count,'terms',len(final),'atoms',dict(collections.Counter(t['atom_count'] for t in final)),flush=True)
# serialize categories without integer masks/maps
catout=[]
for (lab,a),z in sorted(cats.items()):catout.append({'sector':lab,'check':a,'row':z['row'],'orders':z['orders'],'unary_bad_order_count':len(list(iterbits(z['unary_mask']))),'unary_good_order_count':len(list(iterbits(z['good_mask']))),'unary_mask_hex':hex(z['unary_mask']),'good_mask_hex':hex(z['good_mask'])})
pairout=[pair_results[k] for k in sorted(pair_results)]
blockout=[]
for bid,lab,m in blocks:
 checks=sorted({f['check'] for f in m['faults'] if f['elementary_fault']=='ancilla_hook_suffix'});refs=[]
 for a,b in itertools.combinations(checks,2):
  p=pair_results[(lab,a,b)];refs.append({'a':a,'b':b,'truth_sha256':sha(p['truth_rows_hex']),'new_bad_order_pairs':p['new_good_good_bad_order_pairs'],'term_count':p['term_count']})
 # factorized exact count via complement product DP over explicit tuples only for <=2; for main use BDD-like row DP count avoiding cartesian enumeration
 # Count good tuples with no bad pair by incremental assignments over 360 good orders/check using recursive DP; potentially huge, so only record factor form here.
 blockout.append({'block_id':bid,'sector':lab,'participating_checks':checks,'factorization':'OR of inherited unary relations and listed exact binary relations','pair_relations':refs,'source_round68_atom_count':m['sound_outer_block']['atom_count']})
(OUT/'local_order_catalog.json').write_text(json.dumps({'schema':'round69-local-order-catalog-v1','entries':catout},indent=2,sort_keys=True)+'\n')
(OUT/'pair_classification.json').write_text(json.dumps({'schema':'round69-one-two-residual-pair-classification-v1','pairs':pairout},indent=2,sort_keys=True,default=list)+'\n')
(OUT/'block_factorization.json').write_text(json.dumps({'schema':'round69-twelve-block-factorization-v1','blocks':blockout},indent=2,sort_keys=True)+'\n')
print('DONE',len(catout),'cats',len(pairout),'pairs','terms',sum(p['term_count'] for p in pairout),flush=True)
