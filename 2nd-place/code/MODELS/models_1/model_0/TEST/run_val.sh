#!/bin/bash

for scale in 224 228 256
do
  python get_val.py --model=../deploy.prototxt --weights=../snapshots/gn_iter_1000.caffemodel --scale=$scale
done
