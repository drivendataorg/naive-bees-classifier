
for i in `ls -d cv*/`
do 
echo $i
#mkdir -p $i/train/apis
#mkdir -p $i/train/bombus
#mkdir -p $i/val/apis
#mkdir -p $i/val/bombus
find data/apis/ -name '*.jpg' | sort --random-sort > a.txt
find data/bombus/ -name '*.jpg' | sort --random-sort > b.txt
sed 's/$/ 0/g' -i a.txt
sed 's/$/ 1/g' -i b.txt
#mkdir train val
head -n80 a.txt > a_val.txt
tail -n747 a.txt > a_train.txt
head -n310 b.txt > b_val.txt
tail -n2832 b.txt > b_train.txt

mkdir a_train b_train

awk '{system("cp "$1" a_train/.");}' a_train.txt
awk '{system("cp "$1" b_train/.");}' b_train.txt

cd a_train

python ../morph.py

cd ../b_train

python ../morph.py

cd ..

find `pwd`/a_train/ -name '*jpg' > a_train.txt
find `pwd`/b_train/ -name '*jpg' > b_train.txt

sed 's/$/ 0/g' -i a_train.txt
sed 's/$/ 1/g' -i b_train.txt

cat a_train.txt b_train.txt | sort --random-sort > train.txt
cat a_val.txt b_val.txt | sort --random-sort > val.txt

cp val.txt train.txt $i/.

cp *prototxt $i/.

mkdir snapshots

name=`basename $i`

~/caffe/build/tools/caffe train -solver solver.prototxt -weights ~/caffe/models/bvlc_googlenet/bvlc_googlenet.caffemodel -gpu 0,1 &> run_${name}.log

mv snapshots $i/.
mv a_train b_train $i/.

done
