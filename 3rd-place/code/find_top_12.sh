echo "cv_round score"
for i in `/usr/bin/seq 11 1 26`; do echo $i"       "`grep 'utput #7' run_cv${i}.log | tail -n1 | awk '{print $11}'`; done | sort -rnk2 | head -n12
