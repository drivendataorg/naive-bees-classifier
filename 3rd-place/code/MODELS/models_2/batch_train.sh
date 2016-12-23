#!/bin/bash
for d in model*
do
  cd $d
  bash ./train.sh
  cd ..
done

