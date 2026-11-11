#!/bin/bash
cd "$(dirname "$0")"
for i in bb surf_5_std surf_5_misboth surf_7_misboth surf_7_std; do
  python3 -u exp_attrib.py $i > attrib_$i.log 2>&1 &
done
wait
echo ATTRIB_DONE
