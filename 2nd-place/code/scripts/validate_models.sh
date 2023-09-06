#!/bin/bash

for i in {0..2}
do
  cd ../MODELS/models_$i
  bash ./batch_val.sh
  cd ../../scripts
done
