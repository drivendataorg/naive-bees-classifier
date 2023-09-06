#!/bin/bash

for i in {0..2}
do
  cd ../MODELS/models_$i
  python ./generate_submission.py
  cd ../../scripts
done
