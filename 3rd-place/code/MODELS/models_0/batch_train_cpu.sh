#!/bin/bash
for d in model*
do
  cd $d
  bash ./train_cpu.sh
  cd ..
done

