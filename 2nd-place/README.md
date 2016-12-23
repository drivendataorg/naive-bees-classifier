![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/bombus_metis_tile.jpeg)
# Naive Bees Classifier - 2nd Place
<br> <br>
# Entrant Background and Submission Overview

### Mini-bio
As a chemistry graduate student in 2007, I was drawn to GPU computing by the release of CUDA and its utility in popular molecular dynamics packages.  After finishing my Ph.D. in 2008, I did a 2 year postdoctoral fellowship where I implemented the first GPU-accelerated machine learning framework specifically optimized for computer-aided drug design which included deep learning.  I was awarded a prestigious NSF CyberInfrastructure Fellowship for Transformative Computational Science (CI-TraCS) in 2011 and continued as a Research Assistant Professor.  I now direct Data Science and Predictive Modeling efforts.  Prior to this competition, I had no experience in anything image related.  This was a very fruitful experience for me.

### High Level Summary of Submission
Because of the variable positioning of the bees and quality of the photos, I oversampled the training sets using random perturbations of the images.  I used ~90/10 split training/validation sets and only oversampled the training sets.  The splits were randomly generated.  This was performed 16 times (originally intended to do 20-30, but ran out of time).  I used the pre-trained googlenet model provided by caffe as a starting point and fine-tuned on the data sets.  Using the last recorded accuracy for each training run, I took the top 75% of models (12 of 16) by accuracy on the validation set.  These models were used to predict on the test set and predictions were averaged with equal weighting.

### Omitted Work
Since this was my first experience with image recognition, a lot of time was spent just getting things to work and learning about image handling in python.  Oversampling the images with random perturbations helped significantly.

### Model Evaluation
I did try optimizing log loss and not worrying about accuracy.  But that ended up hurting my submission performance.

### Future Steps
I would like to train inceptionv3 and ResNet models on this set to create a more diverse ensemble.  I would also like to try some stacking methods which I just didn't have the time to try.  Additionally, I think much better results could be achieved by first creating a bee detector to localize, crop, and align the thorax of all bees in the images and then training a classifier on that.

<br><br>
# Replicating the Submission

### Install Requirements
* CUDA (if GPU training with caffe is desired)
* caffe (I used the NVIDIA fork - branch 0.14 with CUDNN v3, but any recent caffe should work)
* python 2 (there is a python script for image perturbation that requires PIL - I used anaconda for python management)

### Run run.sh
A script is included (run.sh) which will run all steps required to reproduce the submission within some small error. The oversampling of the training images using the python script (morph.py) creates random perturbations of image rotation, scale, flips, color, contrast, brightness, and sharpness. So there might be very slight differences in the resulting submission file. However, I did keep all intermediate files generated for the original submission, so I can provide the exact training sets for each set if required. I can also provide the actual winning models if desired.

The entire run time on my dated GPUs (2 GTX 680s) is about 50 hrs. I suspect using a Maxwell architecture GPU with CUDNN v4 should significantly reduce run time.
