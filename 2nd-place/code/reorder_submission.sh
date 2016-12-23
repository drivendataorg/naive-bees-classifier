echo "reordering submission..."
Rscript reorder.R
sed 's/\"//g' -i submission.csv
echo "done..."
