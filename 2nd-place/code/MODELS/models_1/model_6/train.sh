#!/usr/bin/env sh
d=$(date +%Y%m%d_%H%M%S)

../../../caffe/build/tools/caffe.bin train \
    --solver=./quick_solver.prototxt --gpu=0 \
    --weights=../../bvlc_googlenet.caffemodel \
    2>&1 | tee logs/train_$d.txt

