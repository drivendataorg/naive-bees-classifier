import caffe
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics

import skimage.transform

MEAN_IMAGE = np.array([103.939, 116.779, 123.68])[:,np.newaxis,np.newaxis]

def prep_image(fn):
    im = plt.imread(fn)
    # Resize so smallest dim = 256, preserving aspect ratio
    h, w, _ = im.shape
    if h < w:
        im = skimage.transform.resize(im, (256, w*256/h), preserve_range=True)
    else:
        im = skimage.transform.resize(im, (h*256/w, 256), preserve_range=True)

    # Central crop to 224x224
    h, w, _ = im.shape
    im = im[h//2-114:h//2+113, w//2-114:w//2+113]
    
    rawim = np.copy(im).astype('uint8')
    
    # Shuffle axes to c01
    im = np.swapaxes(np.swapaxes(im, 1, 2), 0, 1)
    
    # Convert to BGR
    im = im[::-1, :, :]

    im = im - MEAN_IMAGE
    return rawim, im[np.newaxis]


iters = [8000, 15000, 20000]
for iter_no in iters:
	model = 'deploy.prototxt'
	weights = './snapshots/bees_googlenet_iter_' + str(iter_no) + '.caffemodel'
	caffe.set_mode_gpu()
	net = caffe.Classifier(model, weights)
	sub = pd.read_csv('../data/SubmissionFormat.csv')
	ys = []
	ps = []
	for id, label in sub.values.astype('int'):
	    fn = '../data/images/test/{}.jpg'.format(id)
	    rawim, im = prep_image(fn)
	    p = net.predict(np.swapaxes(np.swapaxes(im, 1, 2), 2, 3))
	    
	    ys.append(label)
	    ps.append(p)
	    
	ys = np.array(ys)
	ps = np.array(ps)

	sub.ix[:,1] = (1 - ps[:,0,1]).round(10)
	sub.to_csv('submission_'+ str(iter_no) +'.csv', index=False)