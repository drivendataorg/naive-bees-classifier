#!/bin/bash
for d in model*
do
  cd $d
  cd TEST
  bash ./run.sh
  cd ../..
done

