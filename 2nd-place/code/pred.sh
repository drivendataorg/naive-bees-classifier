for i in `ls ./test/*.jpg`; do ~/caffe/build/examples/cpp_classification/classification.bin ./deploy.prototxt cv${1}/snapshots/_iter_${2}.caffemodel ./imagenet_mean.binaryproto ./labels.txt $i >> cv${1}_preds.txt; done

