import argparse
import os


CAFFE_ROOT = '../../../../caffe/'
curr_dir = os.path.dirname(os.path.abspath(__file__))
LMDB_IDX = curr_dir.split('/')[-2][-1]
DATA_FILE = '../../../../DATA/LMDBs/val_{}.txt'.format(LMDB_IDX)
IMAGES_PREFIX = '../../../../DATA/'


parser = argparse.ArgumentParser()
parser.add_argument('--model', help='deploy file for a model',
                    type=str, required=True)
parser.add_argument('--weights', help='caffemodel snapshot file',
                    type=str, required=True)
parser.add_argument('--scale', help='image scale (in pixels)',
                    type=int, default=256)
args = parser.parse_args()


SCALE = args.scale
MODEL_FILENAME = args.model
PRETRAINED = args.weights
BATCH_SIZE = 10




import numpy as np
import sys
sys.path.append(CAFFE_ROOT + '/python/')
import caffe
import pyprind

images = map(lambda x: IMAGES_PREFIX + x.split(' ')[0],
                   open(DATA_FILE, 'r').readlines())
labels_truth = map(lambda x: int(x.split(' ')[-1]),
                   open(DATA_FILE, 'r').readlines())
print len(images)



NPY_FILENAME = 'pred_val_{}.npy'.format(SCALE)



caffe.set_mode_gpu()
net = caffe.Classifier(model_file=MODEL_FILENAME,
                       pretrained_file=PRETRAINED,
                       image_dims=[SCALE, SCALE],
                       raw_scale=255,
                       mean=np.array([104, 117, 123]),
                       channel_swap=(2,1,0))

preds = np.empty((len(images), 2))

for i in pyprind.prog_percent(range(0, preds.shape[0], BATCH_SIZE)):
    i2 = min(i+BATCH_SIZE, preds.shape[0])
    imgs = [caffe.io.load_image(img) for img in images[i:i2]]
    preds[i:i2, ...] = net.predict(imgs, oversample=True, interp_order=3)
np.save(NPY_FILENAME, preds)


def accuracy(scores, labels):
    N = scores.shape[0]
    acc = 0
    for i in xrange(N):
        if labels[i] == np.argmax(scores[i,:]):
            acc = acc + 1
    return acc*1.0/N



r = np.load(NPY_FILENAME)
print accuracy(r, labels_truth)


