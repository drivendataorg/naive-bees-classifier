#!/bin/bash
for d in model*
do
  cd $d
  rm ./snapshots/*.*
  rm ./TEST/*.npy
  rm ./logs/*.*
  cd ..
done
rm submission.csv
