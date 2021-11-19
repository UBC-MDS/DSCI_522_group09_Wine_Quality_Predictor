# Wine_Quality_Predictor

- authors: Gabriel Fairbrother, Paniz Fazlali Luming Yang, Wanying Ye

A data analysis (machine learning) project for MDS DSCI522 (Data Science Workflows) from Group 09.

## About

In this project, we are trying to answer the question what are the top contributing physicochemical features to a high-quality wine? This question is of marketing significance in the way that if we can decide which physicochemical features are important in determining the quality score of a wine, the wine manufacturers can refine certain wine-making procedures that may yield wines with "promising" properties. Noteworthy, the quality score is a human taste output (_i.e._ each quality score is a median taken over a minimum of 3 sensory assessors) instead of following an objective and rigid standard, which makes wine certification a complicated task. Therefore, attempting to unravel the relationship between physicochemical properties and human taste sensations may also be a direction in the wine certification field.


The data sets were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009). The data sets were sourced from the UC Irvine Machine Learning Repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine. 


In order to answer the research question stated above, we plan to construct multiple <font color=red> regressive/classification </font> machine learning models to predict on the quality of wines, and report the best model with highest metric score of interest. 