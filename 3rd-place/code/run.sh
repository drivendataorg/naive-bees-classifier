echo "creating directories"
for i in `/usr/bin/seq 11 1 26`; do mkdir cv${i}; done

echo "starting training runs - this takes 2 days using 2 GTX 680s..."
./90_10_run.sh

echo "using models to predict the test set - this takes approximately 2.5 hrs..."
for i in `/usr/bin/seq 11 1 26`; do ./pred.sh $i 30000; done

echo "preparing submission files from predictions..."
for i in `/usr/bin/seq 11 1 26`; do ./prep_sub.sh $i; done

echo "I used the top 12 models of 16 (best 75%) - this ranks them by score and lists the cv round number"
./find_top_12.sh

echo "creating avg of top 12 for submission - this was hardcoded from my original submission"
Rscript avg_selective.R
