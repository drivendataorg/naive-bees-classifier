[<img src='https://community.drivendata.org/uploads/default/optimized/1X/e055d38472b1ae95f54110375180ceb4449c026b_1_690x111.png'>](https://www.drivendata.org/)
<br><br>

![Banner Image](https://s3.amazonaws.com/drivendata/comp_images/bombus_metis_tile.jpeg)

# Naive Bees Classifier
## Goal of the Competition
Metis wants to know: using images from BeeSpotter can you identify a bee as a honey bee or a bumble bee? These bees have different behaviors and appearances, but given the variety of backgrounds, positions, and image resolutions it can be a challenge for machines to tell them apart.

Wild bees are important pollinators and the spread of colony collapse disorder has only made their role more critical. Right now it takes a lot of time and effort for researchers to gather data on wild bees. Using data submitted by citizen scientists, Bee Spotter is making this process easier. However, they still require that experts examine and identify the bee in each image. You're goal is to build an algorithm to help. The starting point is to determine the genus—Apis (honey bee) or Bombus (bumble bee)—based on photographs of the insects.

## What's in this Repository
This repository contains code volunteered from leading competitors in the [Naive Bees Classifier](https://www.drivendata.org/competitions/8/) on DrivenData.

## Winning Submissions

Place |Team or User | Public Score | Private Score | Summary of Model
--- | --- | --- | --- | --- | ---
1 | E.A. | 0.9951 | .9956 | We fine-tuned a GoogleNet model using caffe and achieved great results. Fine-tuning using caffe is an easy task.  For each of the inception outputs in GoogleNet, we extracted the features and passed it through logistic regression model.
2 | loweew | 0.9946 | 0.9949 | I used the pre-trained googlenet model provided by caffe as a starting point and fine-tuned on the data sets.  Using the last recorded accuracy for each training run, I took the top 75% of models (12 of 16) by accuracy on the validation set.  These models were used to predict on the test set and predictions were averaged with equal weighting.
3 | L.V.S. | 0.9935 | 0.9934 | To get higher accuracy, I decided to fine-tune a model pre-trained on ImageNet data.


#### Winner's Interview: ["Building the best naïve bees classifier!"](http://blog.drivendata.org/2016/04/19/bees-winners/)

#### Benchmark Blog Post: ["Bumble bee or honey bee?"](http://blog.drivendata.org/2015/09/24/bees-benchmark/)
