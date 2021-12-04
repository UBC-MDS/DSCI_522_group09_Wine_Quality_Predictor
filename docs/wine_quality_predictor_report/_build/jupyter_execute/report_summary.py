#!/usr/bin/env python
# coding: utf-8

# # Summary

# This project is an attempt to build a classification model for predicting wine quality. We have two main questions. First, can we use a machine learning model to predict the human perceived quality of a wine using its physical and chemical attributes? Second, which of these attributes contribute most to that perceived quality? 
# 
# We evaluated three models including Logistic Regression, Support Vector Machine with linear keranl (SVC linear) and Random Forest Classification. Our best classifier was Random Forest Classifier, with the best validation ROC AUC (One vs Rest) score of 0.867 through hyperparameter optimization. The test ROC AUC (One vs Rest) score for Random Forest Classifier was 0.685. The confusion matrix implies that the model did a fairly good job - most of the false predictions fall into adjacent classes, which makes sense because our targets classes are indeed ordinal. The feature importances given by this optimized model suggested that `alcohol`, `density` and `volatile acidity` are the top 3 contributing features in this prediction task. In general, we are confident to use and share this model as a preliminary tool to classify the quality scores of red and white wines. We recommend further improvement on feature engineering to extract better features and increase the model performance.
