#!/usr/bin/env python3
from pathlib import Path
import gzip,json,hashlib,argparse

def load(p):
 p=Path(p); b=p.read_bytes(); return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dump(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def sha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); a=ap.parse_args(); r=a.root
old=load(r/'classification/base/round69_pair_classification.json.gz'); r72=load(r/'classification/base/round72_retained_terms.json.gz')
terms=[]
for p in old['pairs']:
 for j,t in enumerate(p['deletion_minimal_terms']):
  terms.append({'term_id':f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",'sector':p['sector'],'atoms':t['atoms'],
                'relation_kind':'reviewed_round69_positive_pair_rectangle','source_round':69,
                'source_pair':[p['a'],p['b']],'source_term_sha256':sha(t)})
for t in r72['terms']:
 z={'term_id':t['term_id'],'sector':t['sector'],'atoms':t['atoms'],'relation_kind':t['relation_kind'],
    'source_round':72,'source_term_sha256':sha(t)}
 if 'mechanism_id' in t:z['mechanism_id']=t['mechanism_id']
 if 'a' in t:z['source_pair']=[t['a'],t['b']]
 terms.append(z)
assert len(terms)==5306 and len({t['term_id'] for t in terms})==5306
obj={'schema':'round74-installed-generalized-state-v1','reviewed_round69_terms':4740,'reviewed_round72_terms':566,
     'round74_retained_terms':0,'term_count':5306,'terms':terms}
dump(r/'classification/installed_generalized_terms.json',obj)
print(json.dumps({'term_count':len(terms),'sha256':sha(terms)},sort_keys=True))
