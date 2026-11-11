#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil
ap=argparse.ArgumentParser(); ap.add_argument('--source',type=Path,required=True); ap.add_argument('--destination',type=Path,required=True); a=ap.parse_args()
assert a.source.is_dir() and not a.destination.exists()
a.destination.parent.mkdir(parents=True,exist_ok=True)
shutil.copytree(a.source,a.destination,symlinks=False)
files=sum(p.is_file() for p in a.destination.rglob('*'))
links=sum(p.is_symlink() for p in a.destination.rglob('*'))
assert links==0
print({'status':'PASS','files':files,'symlinks':links,'destination':str(a.destination)})
