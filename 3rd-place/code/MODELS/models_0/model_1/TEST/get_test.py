import argparse


CAFFE_ROOT = '../../../../caffe/'
DATA_FILE = '../../../../DATA/SubmissionFormat.csv'
IMAGES_PREFIX = '../../../../DATA/images/test/'


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

images = map(lambda x: IMAGES_PREFIX + x.split(',')[0] + '.jpg',
             open(DATA_FILE, 'r').readlines()[1:])
print len(images)



NPY_FILENAME = 'pred_test_{}.npy'.format(SCALE)



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
