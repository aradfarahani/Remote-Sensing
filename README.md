# Remote Sensing  
[![CodeFactor](https://www.codefactor.io/repository/github/aradfarahani/remote-sensing/badge)](https://www.codefactor.io/repository/github/aradfarahani/remote-sensing)  
[![DOI](https://zenodo.org/badge/683561862.svg)](https://zenodo.org/doi/10.5281/zenodo.10027283)  

"Remote Sensing" is a Python-based project inspired by ENVI (developed by L3Harris Geospatial) but designed to push the boundaries a bit further. Remote sensing involves gathering data about objects or phenomena without physical contact, typically applied to Earth and planetary observation. This repository is my personal exploration of modern remote sensing techniques using Python, fueled by a passion for integrating cutting-edge tech into everyday workflows.

This project is organized into topical folders, each focusing on a specific aspect of remote sensing. Let’s dive into what you’ll find inside!

---

## Folder Overview

### 01. Import  
Kick off your remote sensing journey here. Learn how to import satellite imagery and visualize it using Python. This folder provides a simple starting point with examples like this:  
![Import Example](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/5bf8c7bb-b126-4644-a60a-92792e02eb8b)

### 02. Image Enhancement  
Enhance your images to make them more suitable for analysis or display. Techniques like Gamma, Logarithm, and Sigmoid functions (via scikit-image) are applied to Landsat-8 imagery. Example using the Gamma method:  
![Gamma Enhancement](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/1fafe550-52a9-4cc3-94bf-ca77028794be)

### 03. Mask  
Mask satellite images using shapefiles (.shp) to focus on specific regions:  
![Masked Image](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/df4fa12f-951b-4367-ad01-ff6b9c0d0056)

### 04. Mosaic  
Create seamless orthomosaics from image collections, corrected for geometric distortion and color-balanced:  
![Orthomosaic](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/5463cdc0-c6a4-4fe0-9592-7f145a355122)

### 05. HSV  
Explore the HSV (Hue, Saturation, Value) color space to analyze image properties numerically:  
![HSV Cone](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/997aa9f5-abb3-4da2-bf87-44c2b5934f43)  
![HSV Example](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/0e79dad7-ae67-4e57-89eb-bde565428674)

### 06. Spectral Profile  
Generate spectral profiles to analyze pixel data across an image:  
![Spectral Profile](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/c57c2b56-5d5e-4710-b68a-4ff2df6706c1)

### 07. Principal Component Analysis (PCA)  
Reduce data complexity with PCA, visualized and analyzed using scikit-learn on Landsat-8 imagery:  
![PCA Scatter](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/6a340eec-8aca-4e0b-803a-5e055cea461e)  
![PCA Result](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/8431b007-ff80-4a89-ab77-0668b140ac1b)

### 08. Spectral Indices  
Calculate indices (e.g., vegetation, water) using spectral reflectance combinations:  
![Indices Equations](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/55672a57-e062-4334-b4d1-9b9e4a5f74a6)  
![Indices Example](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/b7d15128-1666-4187-8bb3-27c60d3a9ddc)

### 09. Clustering  
Apply k-means clustering (e.g., 4 clusters) to group similar pixels in Landsat-8 images:  
![Clustering Result](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/081c4408-c943-40a4-9e92-0e62da0dbc6c)

### 10. Filters  
Enhance or suppress image features using spatial filters:  
![Filtered Image](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/c74f9fd4-c85e-4ea5-87ac-214285aeff60)

### 11. Change Detection  
Detect changes over time using Change Vector Analysis (CVA) methods like direction and magnitude:  
![Change Detection](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/b832b9f4-beda-49f8-8e00-0ed9eee5986a)

### 12. Gray-Level Co-Occurrence Matrix (GLCM)  
Analyze texture with GLCM, examining pixel relationships:  
![GLCM Example](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/84a7e692-d791-4c43-a7f4-462e37a7b71b)

### 13. Support Vector Machine (SVM)  
Classify data using SVM for supervised learning:  
![SVM Margin](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/8e12978b-595e-48f2-8e78-0aa5ce68a32f)  
![SVM Result](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/f9efad77-e97c-4b7a-988f-a5d09fdd8cc1)

### 14. Time Series  
Study temporal patterns in satellite data:  
![Time Series Plot](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/ab1484d2-b6ce-4670-874b-380650ee99e1)

### 15. Convolutional Neural Network (CNN)  
Use CNNs for lithology classification on Sentinel-2 data, validated with ROC curves and confusion matrices:  
![CNN Workflow](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/3fbb9995-fd2a-40b9-83c6-f0e84cdd570d)  
![ROC Curve](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/9d19694f-4d11-4712-9a15-ec13edacf820)  
![CNN Result](https://github.com/aradfarahani/Remote-Sensing/assets/90475349/3d615706-75fd-4102-a50b-0668ad7b75a6)

---

## License  
This project is licensed under the [MIT License](https://github.com/aradfarahani/Remote-Sensing/blob/main/LICENSE).

## Contributing  
Contributions are welcome! If you’d like to collaborate or improve this project, please email me at:  
**mahdifarmahinifarahani@aol.com**

## Acknowledgments  
- Thanks to the open-source community for the incredible libraries and tools that made this project possible.  
- A special shoutout to Vcafe (Felestin St.) and Levana Cafe (ASP Towers) for the coffee that fueled countless coding sessions.

---

**Enjoy exploring the repo!**  
Questions? Feel free to reach out:  
📧 **mahdifarmahinifarahani@aol.com**  
ORCID: <a href="https://orcid.org/0009-0008-3800-8688" target="_blank"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" alt="ORCID iD icon"/> 0009-0008-3800-8688</a>
