#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1]);f=root/'formulas/iter136';r=root/'reconstruction'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert (f/'outer.cnf').read_bytes()==(r/'outer.recompiled.cnf').read_bytes()
assert (f/'assertion_map.jsonl').read_bytes()==(r/'assertion_map.recompiled.jsonl').read_bytes()
assert (f/'circuit_trace.json.gz').read_bytes()==(r/'circuit_trace.recompiled.json.gz').read_bytes()
a=json.loads((f/'metadata.json').read_text());b=json.loads((r/'metadata.recompiled.json').read_text());ca=a.pop('compile_seconds');cb=b.pop('compile_seconds');assert a==b
x=json.loads((f/'encoding_check.json').read_text());y=json.loads((r/'encoding_check.recompiled.json').read_text());sx=x.pop('seconds');sy=y.pop('seconds');assert x==y
out={'schema':'circdist-round94-iter136-correspondence-v1','status':'PASS','stored_decompressed_cnf_sha256':sha(f/'outer.cnf'),'recompiled_cnf_sha256':sha(r/'outer.recompiled.cnf'),'cnf_byte_identical':True,'assertion_map_byte_identical':True,'circuit_trace_byte_identical':True,'metadata_equal_excluding_compile_seconds':True,'encoding_check_equal_excluding_seconds':True,'stored_compile_seconds':ca,'fresh_compile_seconds':cb,'stored_encoding_check_seconds':sx,'fresh_encoding_check_seconds':sy,'assertions':a['assertions'],'variables':a['variables'],'clauses':a['clauses'],'source_to_cnf_correspondence':'exact deterministic compilation plus independent complete clause/definition/root reconstruction'}
(r/'correspondence.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
