#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, yaml
ap=argparse.ArgumentParser()
ap.add_argument('--root',type=Path,required=True)
ap.add_argument('--output',type=Path,required=True)
a=ap.parse_args(); files=sorted(set(a.root.rglob('*.yaml'))|set(a.root.rglob('*.yml')))
duplicates=[]; mappings=0
def walk(node,path,file):
 global mappings
 if isinstance(node,yaml.nodes.MappingNode):
  mappings+=1;seen={}
  for k,v in node.value:
   key=yaml.serialize(k).strip()
   if key in seen: duplicates.append({'file':str(file.relative_to(a.root)),'path':path,'key':key,'first_line':seen[key],'duplicate_line':k.start_mark.line+1})
   else: seen[key]=k.start_mark.line+1
   walk(v,path+'/'+key,file)
 elif isinstance(node,yaml.nodes.SequenceNode):
  for i,v in enumerate(node.value):walk(v,path+'/'+str(i),file)
for f in files:
 node=yaml.compose(f.read_text())
 if node is not None:walk(node,'',f)
out={'schema':'round88-duplicate-yaml-scan-v1','status':'PASS' if not duplicates else 'FAIL','files':len(files),'mappings':mappings,'duplicates':duplicates}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
raise SystemExit(0 if not duplicates else 1)
