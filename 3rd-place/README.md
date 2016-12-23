![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/bombus_metis_tile.jpeg)
# Naive Bees Classifier - 3rd Place
<br> <br>
# Entrant Background and Submission Overview

### Mini-bio
I am a researcher with 9 years of experience both in industry and academia. Currently, I am dealing with machine learning developing intelligent data processing
algorithms. My previous experience was in the field of digital signal processing and fuzzy logic
systems.

### High Level Summary of Submission
I employed convolutional neural networks, since nowadays they are the best tool for computer
vision tasks [1].  Provided dataset contains only two classes and it is relatively small. So to get higher accuracy, I
decided to fine-tune a model pre-trained on ImageNet data. Fine-tuning almost always produces
better results [2].

There are many publicly available pre-trained models. But some of them have license restricted
to non-commercial academic research only (e.g., models by Oxford VGG group). It is incompatible
with the challenge rules. That is why I decided to take open GoogleNet model pre-trained by
Sergio Guadarrama from BVLC [3].

One can fine-tune a whole model as is but I tried to modify pre-trained model in such a way, that
could improve its performance. Specifically, I considered parametric rectified linear units (PReLUs)
proposed by Kaiming He et al. [4]. That is, I replaced all regular ReLUs in the pre-trained model
with PReLUs. After fine-tuning the model showed higher accuracy and AUC in comparison with
the original ReLUs-based model.

In order to evaluate my solution and tune hyperparameters I employed 10-fold cross-validation.
Then I checked on the leaderboard which model is better: the one trained on the whole train data
with hyperparameters set from cross-validation models or the averaged ensemble of crossvalidation
models. It turned out the ensemble yields higher AUC.

To improve the solution further, I evaluated different sets of hyperparameters and various preprocessing
techniques (including multiple image scales and resizing methods).

I ended up with three groups of 10-fold cross-validation models.

Model Group Name | Training Image Scale | Testing Image Scale | Initial Learning Rate | Cross-validation AUC
--- | --- | --- | --- | --- | ---
models_0 | 256 | 224, 228, 256, 284, 320 | 0.001 | 0.9926
models_1 | 256 | 224, 228, 256 | 0.005 | 0.9938
models_2 | 300 | 224, 228, 256 | 0.005 | 0.9941

To get the final ensemble, I multiplied all three averaged cross-validation models. The product
(multiplication) yielded slightly better AUC in comparison with the sum (addition).

### Omitted Work
Weighed loss function to tackle class imbalance, exponential linear units (ELUs) [5] instead of PReLUs, training randomly initialized models (without fine-tuning) didn't help to improve my solution.

### Model Evaluation
10-fold cross-validation helped me to evaluate my models and build an ensemble. Regarding metrics, I checked negative log likelihood loss, accuracy and AUC.

### Potentially Helpful Features
It would be great to have images of higher resolution. I am not an expert in bees but probably GPS coordinates and time stamps could help to distinguish between species more precisely in some cases.

### Notes About the Model
It is preferable to run my solution using cuDNN v.3 library on NVIDIA GPU with 4GB RAM. Amazon EC2 g2.2xlarge instance should be OK. GPU and cuDNN are not necessary, though highly recommended, please see README.md for the details.

### Future Steps
I would check the recent ImageNet challenge solutions and fine-tune the best available model. It could be the latest GoogLeNet or deep ResNet. Also I would experiment with various data augmentation methods.

<br><br>
# Replicating the Submission

### 1. Directory structure

```
solution -+-> DATA -> LMDBs
          |-> MODELS -+-> models_0
          |           |-> models_1
          |           |-> models_2
          |-> caffe
          |-> scripts
```

**DATA** is a directory containing the original challenge data and preprocessed LMDBs (databases storing images for Caffe).

**DATA/LMDBs** is a directory storing cross-validation splits (text files describing images and labels per a split and databases).

**MODELS** directory has three subdirectories with corresponding models' groups and baseline pre-trained BVLC GoogLeNet model.

Each **MODELS/models_x** (x = 0, 1, 2) directory includes 10 cross-validation models of the group and scripts for group operations (train, validation, test):

```
models_x -+-> model_0
          |-> model_1
          .
          |-> model_9
```

Each **MODELS/models_x/model_y** (y = 0, 1, ..., 9) directory contains model's definition (train_val.prototxt and deploy.prototxt), solver's parameters (quick_solver.prototxt) and additional scripts.

The solution requires modified version of Caffe. It is stored in **caffe** directory. The only difference with the standard Caffe at GitHub is in **caffe/python/caffe/classifier.py** module. I added **interp_order** parameter to the method *predict* in order to allow calling bicubic interpolation instead of the default bilinear.

All necessary scripts for training, testing and ensembling were placed in **scripts** directory.

### 2. Software installation

The solution could be reproduced on many software/hardware configurations, the most important requirement is a proper installation of Caffe deep learning framework.  Please follow the instructions below to setup all necessary dependencies.

1. Setup Ubuntu 14.04.3 LTS operating system.
2. If NVIDIA GPU isn't available, please skip to step 12.
3. Download the latest NVIDIA driver (now, it is 352.63) from http://www.nvidia.com/Download/driverResults.aspx/95159/en-us
4. If Ubuntu is in desktop mode, switch to the console by pressing `Ctrl-Alt-F1`, log in and stop desktop manager.
```
sudo service lightdm stop
```
5. Remove all previously installed NVIDIA drivers
```
sudo apt-get remove nvidia*
```
6. Install the driver
```
sudo bash NVIDIA-Linux-x86_64-352.63.run --no-opengl-files
```
7. If you need to return to the desktop, type
```
sudo service lightdm start
```
8. Download CUDA 7.5 (or 7.0 especially if you are using Amazon) from NVIDIA https://developer.nvidia.com/cuda-downloads
9. Install CUDA (skip driver installation)
```
sudo bash cuda_7.5.18_linux.run
```
10. Download cuDNN v.3 at https://developer.nvidia.com/cudnn
11. Install it
```
sudo tar -xvf ./cudnn-7.0-linux-x64-v3.0-prod.tgz -C /usr/local/
```
12. Get Anaconda 2.4.1 (for Python 2) at https://repo.continuum.io/archive/Anaconda2-2.4.1-Linux-x86_64.sh
13. Install it
```
bash Anaconda2-2.4.1-Linux-x86_64.sh
```
14. Remove *xz* package
```
conda remove xz
```
15. Install via pip some packages:
```
pip install pyprind
pip install protobuf
```
16. Install all Caffe dependencies as recommended at http://caffe.berkeleyvision.org/install_apt.html
17. Add Anaconda and CUDA libraries to LD_LIBRARY_PATH
```
export LD_LIBRARY_PATH=$HOME/anaconda2/lib:/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```
Please note that this step should be done every time when new terminal session is opened.
18. If you are using CPU only, then edit Makefile.config
```
vim caffe/Makefile.config
```
19. Build Caffe
```
cd caffe
make -j4
make pycaffe
cd ..
```

### 3. Data preparation

1. Get the challenge dataset at https://drivendata.s3.amazonaws.com/data/8/public/2f9cb1e7-d1ab-43aa-b04c-1264eea88a2f.zip and extract it to **DATA**
```
unzip 2f9cb1e7-d1ab-43aa-b04c-1264eea88a2f.zip -d ./DATA/
```
2. Get BVLC GoogLeNet pre-trained model
```
cd MODELS
wget http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel
cd ..
```
3. Create cross-validation splits as text files in **DATA/LMDBs**
```
cd scripts
python make_CV_splits.py
```
4. Create LMDB databases with images and labels for each cross-validation split in two scales (default, scale=256 and additional, scale=300)
```
bash create_LMDBs.sh
```

### 4. Training procedure

Start training of all 30 models by executing the following script in **scripts** directory:
```
bash train_models.sh
```
Please note that you can train models for each group **models_x** separately
```
cd MODELS/models_x
bash batch_train.sh
```
If you'd like to train using CPU only, type
```
cd MODELS/models_x
bash batch_train_cpu.sh
```

### 5. Prediction

1. Generate predictions for each model on test data
```
cd scripts
bash test_models.sh
```
You can find these predictions at **MODELS/models_x/model_y/TEST/pred_test_*.npy**. They are regular NumPy arrays.
Please note that you can generate predictions on validation data with *validate_models.sh* script.

2. Aggregate predictions for each models' group (by averaging) and make group's submission
```
bash generate_submissions.sh
```
The submission for each cross-validation group is available at **MODELS/models_x/submission.csv**
3. Ensemble groups' submissions (by product)
```
python ensemble_submissions.py
```
This script generates file **scripts/ensemble.csv**.


### References
1. Ali Sharif Razavian et al. CNN Features off-the-shelf: an Astounding Baseline for Recognition, 2014: http://arxiv.org/abs/1403.6382
2. Jason Yosinski et al. How transferable are features in deep neural networks, 2014: http://arxiv.org/abs/1411.1792
3. GoogLeNet model by BVLC: https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet
4. Kaiming He et al. Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification, 2015: http://arxiv.org/abs/1502.01852
5. Djork-Arne Clevert et al. Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs), 2015: http://arxiv.org/abs/1511.07289
