#!/usr/bin/env python3
from pathlib import Path
import argparse, json
ap=argparse.ArgumentParser()
ap.add_argument('expected',type=Path)
ap.add_argument('actual',type=Path)
ap.add_argument('--ignore',action='append',default=[])
a=ap.parse_args()
e=json.loads(a.expected.read_text());g=json.loads(a.actual.read_text())
for k in a.ignore:
 e.pop(k,None);g.pop(k,None)
assert e==g,(a.expected,a.actual)
print('JSON_MATCH',a.expected,a.actual)
