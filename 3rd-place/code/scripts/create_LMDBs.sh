#!/bin/bash

# remove LMDBs in target directory
rm -rf ../DATA/LMDBs/*-lmdb

# create LMDBs for scale = 256 (models_0, models_1)
for split_file in $(ls ../DATA/LMDBs/*.txt)
do
    ../caffe/build/tools/convert_imageset.bin \
        --resize_height=256 \
        --resize_width=256 \
        ../DATA/ \
        $split_file \
        ${split_file%\.txt}-lmdb
done

# create LMDBs for scale = 300 (models_2)
for split_file in $(ls ../DATA/LMDBs/*.txt)
do
    ../caffe/build/tools/convert_imageset.bin \
        --resize_height=300 \
        --resize_width=300 \
        ../DATA/ \
        $split_file \
        ${split_file%\.txt}-s300-lmdb
done
