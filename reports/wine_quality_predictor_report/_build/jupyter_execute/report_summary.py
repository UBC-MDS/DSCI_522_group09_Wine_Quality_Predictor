#!/usr/bin/env python
# coding: utf-8

# # Summary

# This project is an attempt to build a classification model for predicting wine quality. Our target is multi-class, and since some classes were under-populated, we decided to combine some of them. The final classes are $\leq4$, $5$, $6$, $7$ and $\geq8$. We evaluated three models for effectiveness in predicting quality scores in red and white wines. Our best classifier was Random Forest Classifier with the test score of 0.685 using Roc_Auc One vs Rest metric. The model has some confusion among the quality scores of $5$, $6$ and $7$ mainly because these classes are of ordinary quality and there are many ordinary quality wines rather than low or high quality wines, and the features do not have well-separated distributions for these features. The test score is not very well but we are confident to share the results since the classification does not include sensitive information. However, it is worth working on feature engineering to extract better features and increase the test score.
