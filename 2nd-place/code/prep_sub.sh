./digits_sub_prep.sh cv${1}_preds.txt > tmp.txt
./reorder_submission.sh
mv submission.csv cv${1}_submission.csv

