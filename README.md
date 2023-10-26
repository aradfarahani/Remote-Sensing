[![DOI](https://zenodo.org/badge/683561862.svg)](https://zenodo.org/doi/10.5281/zenodo.10027283) <br>
# Remote Sensing
Remote Sensing is the name of the remote sensing project that is developed with Python inspired by ENVI (software developed by L3Harris Geospatial)<br>
Remote sensing is the acquisition of information about an object or phenomenon without making physical contact with the object, in contrast to in situ or on-site observation. The term is applied especially to acquiring information about Earth and other planets.<br>
Due to my personal interest in applying modern technologies in daily work, I decided to create this repository for the remote sensing applications<br>
In this Repository you will see several folders, and each folder is about specefic topic. <br>
It is better to introduce folders immediately without wasting time, SO....<br>
## No.01 Import
In this folder you only learn about how to import your satellite images and visulize it. there is nothing important about it and just a kickoff on remote sensing by Python :) here is some of the exampel about what you see and what you gonna do with your data<br>
![1692987905704](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/5bf8c7bb-b126-4644-a60a-92792e02eb8b)


## No.02 Image Enhancement
Image enhancement is the process of adjusting digital images so that the results are more suitable for display or further image analysis. For example, you can remove noise, sharpen, or brighten an image, making it easier to identify key features. In this repository I've tried different methods of Image enhancement (e.g. Gamma, Logarithm, Sigmoid function and etc.) that is available in scikit-image module on Python with Landsat 8 Images. The image below by using Gamma method.
![1693949810955](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/1fafe550-52a9-4cc3-94bf-ca77028794be)

## No.03 Mask
Here you can mask your images by considering shape file (.shp):<br>
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/df4fa12f-951b-4367-ad01-ff6b9c0d0056)

## No.04 Mosaic
An orthomosaic is a photogrammetrically orthorectified image product mosaicked from an image collection, where the geometric distortion has been corrected and the imagery has been color balanced to produce a seamless mosaic dataset.

![IMG_9911](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/5463cdc0-c6a4-4fe0-9592-7f145a355122)

## No.05 HSV
![hsvcone](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/997aa9f5-abb3-4da2-bf87-44c2b5934f43)

Herpes simplex virus 1 and 2, also known by their taxonomic names Human alphaherpesvirus 1 and Human alphaherpesvirus 2, are two members of the human Herpesviridae family, a set of viruses that produce viral infections in the majority of humans. Both HSV-1 and HSV-2 are very common and contagious.
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/0e79dad7-ae67-4e57-89eb-bde565428674)

## No.06 Spectral Profile
A spectral profile consists of geometry to define the pixel selection and an image with key metadata from which to sample. To create a chart, right-click the layer you want analyze in the Contents pane, point to Create Chart, and click Spectral Profile to open the Chart Properties pane.
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/c57c2b56-5d5e-4710-b68a-4ff2df6706c1)

## No.07 Principal component analysis
![GaussianScatterPCA svg](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/6a340eec-8aca-4e0b-803a-5e055cea461e)

![images](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/114034a2-70f0-4c10-80f9-0ca050966b48)

Principal component analysis, or PCA, is a statistical procedure that allows you to summarize the information content in large data tables by means of a smaller set of “summary indices” that can be more easily visualized and analyzed. in this image I use PCA on Landsat 8 satellite Images by using scikit-learn on Python.
![PCA](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/8431b007-ff80-4a89-ab77-0668b140ac1b)

## No.08 Spectral Indices
![Spectral-Indices-Equations](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/55672a57-e062-4334-b4d1-9b9e4a5f74a6)

Spectral indices are combinations of spectral reflectance from two or more wavelengths that indicate the relative abundance of features of interest. Vegetation indices are the most popular type, but other indices are available for burned areas, man-made (built-up) features, water, and geologic features.
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/b7d15128-1666-4187-8bb3-27c60d3a9ddc)
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/4f02aa2d-1858-4e98-bd9a-c1ba0bc84d6c)

## No.09 Clustring
![images](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/aa90b2b9-e1b3-4bc9-b466-40d0d7bca855)
![ijH71](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/c5ef50a8-c534-4436-a3c3-3b1a75c17f3c)


k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. In this Image I tried k-means method with 4 clusters on my landsat8 Images.
![1693521262844](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/081c4408-c943-40a4-9e92-0e62da0dbc6c)

## No.10 Filters
Filtering is used to enhance the appearance of an image. Spatial filters are designed to highlight or suppress specific features in an image based on their spatial frequency.
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/c74f9fd4-c85e-4ea5-87ac-214285aeff60)

## No.11 Change Detection
n statistical analysis, change detection or change point detection tries to identify times when the probability distribution of a stochastic process or time series changes. In this section I decide to use to Change Vector Analysis (CVA) methods (Such as Change Direction and Change Magnitude) on my data.<br>
![1693698661388](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/b832b9f4-beda-49f8-8e00-0ed9eee5986a)

## No.12 Gray-Level Co-Occurrence Matrix
![glcm](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/0a167d3f-890f-49e1-b6ed-b84e440b2f97)

Gray-Level Co-Occurrence Matrix, or GLCM is a second-order statistical texture analysis method. It examines the spatial relationship among pixels and defines how frequently a combination of pixels are present in an image in a given direction Θ and distance d.
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/84a7e692-d791-4c43-a7f4-462e37a7b71b)



## No.13 Support Vector Machine
![SVM_margin](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/8e12978b-595e-48f2-8e78-0aa5ce68a32f)

In machine learning, support vector machines (e.g. SVM) are supervised learning models with associated learning algorithms that analyze data for classification and regression analysis.

![1693865889169](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/f9efad77-e97c-4b7a-988f-a5d09fdd8cc1)

## No.14 Time Series
Time Series Analysis is a way of studying the characteristics of the response variable concerning time as the independent variable. In mathematics, a time series is a series of data points indexed in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time. Thus it is a sequence of discrete-time data.
![1695579963833](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/ab1484d2-b6ce-4670-874b-380650ee99e1)

## No.15 Convolutional Neural Network
![Screenshot (3305)](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/3fbb9995-fd2a-40b9-83c6-f0e84cdd570d)
![Roc_curve svg](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/9d19694f-4d11-4712-9a15-ec13edacf820)
![download](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/3d615706-75fd-4102-a50b-0668ad7b75a6)


Convolutional Neural Network (CNN) is a regularized type of feed-forward neural network that learns feature engineering by itself via filters optimization. Vanishing gradients and exploding gradients, seen during backpropagation in earlier neural networks, are prevented by using regularized weights over fewer connections. Hear I used my CNN model for lithology classification on my Sentinel-2 satellite image and my Ground truth data. and for the validation part you can use ROC curve and Confusion Martix. A receiver operating characteristic curve, or ROC curve, is a graphical plot that illustrates the diagnostic ability of a binary classifier system as its discrimination threshold is varied. The ROC curve is the plot of the true positive rate against the false positive rate, at various threshold settings. A Confusion matrix is an N x N matrix used for evaluating the performance of a classification model, where N is the number of target classes. The matrix compares the actual target values with those predicted by the machine learning model.

![1697726601196](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/119d1620-b6a1-401c-ad62-ba6091ac32c9)

![1697726597312](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/3afd885e-9667-4020-a0d8-6e80e94cb468)

![1697726597448](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/b1414a92-9dff-4919-ab80-0292dfaca49b)
![cm](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/91215c38-e801-4e0f-ae9f-8ee20fc79b06)
![r2](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/16b7d92f-c767-41ca-b6d4-5541b58a6b13)
![r1](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/77ccb008-bc76-4333-94ef-16b30afca191)
# License
Remote Sensing is licensed under the [MIT License](https://github.com/aradfarahani/Remote-Sensing/blob/main/LICENSE).

# Contributing
Contributions are welcome! If you'd like to contribute to this project, please send me an E.mail.

# Acknowledgments
I would like to thank the open-source community for the libraries and tools used in this project. Also I like to thank Vcafe (Felestin St.) and Levana Cafe (ASP Towers) for the  coffees; The project would not have been completed without the coffees of these two cafes... 

<br>Enjoy ;)<br> <a
    id="cy-effective-orcid-url"
    class="underline"
     href="https://orcid.org/0009-0008-3800-8688"
     target="orcid.widget"
     rel="me noopener noreferrer"
     style="vertical-align: top">
     <img
        src="https://orcid.org/sites/default/files/images/orcid_16x16.png"
        style="width: 1em; margin-inline-start: 0.5em"
        alt="ORCID iD icon"/>
      https://orcid.org/0009-0008-3800-8688
    </a><br>
    
   <p> And if you have question, don't hesitate and ask :)</p> <br>
   <p>E.mail: mahdifarmahinifarahani@aol.com </p>

