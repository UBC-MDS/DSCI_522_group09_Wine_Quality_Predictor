#!/usr/bin/env python
# coding: utf-8

# # Summary

# This project is an attempt to build a classification model for predicting wine quality. We have two main questions. First, can we use a machine learning model to predict the human perceived quality of a wine using its physical and chemical attributes? Second, which of these attributes or features contributes most to that perceived quality? 
# 
# During the EDA stage, we discovered the data set has severe class-imbalance issue. Our target is multi-class in terms of quality scores ranging from "3" to "9". However, the classes "3" and "9" were extremely under-populated. Therefore, we decided to combine the lowest two classes ("3" and "4") and the highest two classes ("8" and "9") to mitigate the severe class imbalance problem. By doing so, the number of examples in each class is distributed more evenly. The final quality score classes are "<=4", "5", "6", "7" and ">=8". The best wines will be classified as ">=8", and the poorest wines will be classified as "<=4".
# 
# We evaluated the effectiveness in predicting quality scores in red and white wines with three models including [Support Vector Machine with linear keranl (SVC linear)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html), [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), and [Random Forest Classification](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).  Our best classifier was Random Forest Classifier, with the best validation score of 0.867 using the [ROC AUC (One vs Rest)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html) scoring metric.
# 
# The final test score for Random Forest Classifer was 0.685 with ROC AUC. Although the score itself is not high, the confusion matrix implies that the model did a fairly good job in predicting the wine quality classes. From the confusion matrix plot, we could observe that most of the false predictions fall into adjacent classes, which makes sense because our targets classes are indeed ordinal. For example, that means even if we did not prediction a true class "7" perfectly, we did predicted it as adjacent class "6". In conclusion, we are confident to use and share this model as a preliminary tool to classify the quality scores of red and white wines. Furthermore, it is worth working on feature engineering to extract better features and increase the test score.

# In[ ]:




