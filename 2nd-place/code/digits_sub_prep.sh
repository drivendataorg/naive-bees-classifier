awk 'BEGIN{print "id,genus";}/Prediction/{split($4,a,"/"); getline; if($3=="\"bombus\""){split(a[3],p,".");print p[1]","$1}else{split(a[3],p,"."); print p[1]","1-$1}}' $1 
