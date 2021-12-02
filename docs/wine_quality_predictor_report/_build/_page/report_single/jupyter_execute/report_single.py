#!/usr/bin/env python
# coding: utf-8

# # Summary

# This project is an attempt to build a classification model for predicting wine quality. Our target is multi-class, and since some classes were under-populated, we decided to combine some of them. The final classes are <=4 , 5, 6, 7 and >=8. We evaluated three models for effectiveness in predicting quality scores in red and white wines. Our best classifier was Random Forest Classifier with the test score of 0.685 using Roc_Auc One vs Rest metric. The model has some confusion among the quality scores of 5, 6 and 7 mainly because these classes are of ordinary quality and there are many ordinary quality wines rather than low or high quality wines, and the features do not have well-separated distributions for these features. The test score is not very well but we are confident to share the results since the classification does not include sensitive information. However, it is worth working on feature engineering to extract better features and increase the test score.

# # Introduction

# Wine is a product that is both an extremely popular and highly consumed product, and one that can be very expensive to buy and lucrative to sell. It is also sold at much higher variety levels than almost any other consumer product - in some supermarkets well over 1000 different wines are stocked.{cite:ps}`lockshin2003wine`
# 
# At the same time, it is also one of the hardest to identify quality ahead of purchase, since you must consume it to decide.  The level of quality a consumer might require can even vary wildly depending on the consumption occasion {cite:ps}`quester1998wine`
# 
# The quality of wine however is difficult to evaluate objectively and is reliant on some very subjective sensory elements. However we believe that this question can be answered by evaluating which physicochemical features are important in determining the quality score of a wine, the wine manufacturers can refine certain wine-making procedures that may yield wines with "promising" properties. 
# 
# We also believe that by using  a quality score that is a human taste output (i.e. each quality score is a median taken over a minimum of 3 sensory assessors) instead of following an objective and rigid standard, which makes wine certification a complicated task, we can better capture the inherent subjectivity of the task. Therefore, attempting to unravel the relationship between physicochemical properties and human taste sensations may also be a direction in the wine certification field {cite:ps}`cortez2009modeling`

# # Methods

# ## Data
# 
# The data sets used in this project were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis {cite:p}`cortez2009modeling`. They were sourced from the UC Irvine Machine Learning Repository{cite:ps}`Dua:2019` and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine.

# ## Analysis
# 
# Three classification models were attempted and assessed to predict the quality score of a wine: the logistic regression model, the support machine vector with linear kernel (SVM RBF) and the random forest classification model. These candidates were selected based on their common intriguing attributes such as high interpretability and giving handy measurements on feature importance. All numeric features in the original datasets were included and scaled, with the type of wine (_i.e._ white or red) as an added binary feature. 
# 
# To address the problem of class imbalance, we re-categorized the targets classes into <=4, 5, 6, 7 and >=8 so that there are enough training examples in each class. We also chose the scoring metrics to be f-1 macro score, Receiver Operating Characteristic (One vs. Rest) Area under the curve, and Receiver Operating Characteristic (One vs. One) Area under the curve. 
# 
# For each algorithm, the default hyperparameters were used first to train the model, and then the 5-fold cross-validation scores were compared across 3 models. Hyperparameter optimization was carried out on the algorithm with the best cross-validation score. The resulting model with the optimized hyperparameters was the solution to this prediction task. We then assess its performance on test data (_i.e._ unseen examples).
# 
# The computing language used in this project is Python {cite:p}`perez2011python`. Packages used in EDA and machine learning analysis include: altair {cite:p}`vanderplas2018altair`, docopt {cite:p}`docopt`, scikit-learn {cite:p}`scikit-learn`, matplotlib {cite:p}`Hunter:2007`, numpy {cite:p}`harris2020array`, pandas {cite:p}`mckinney2010data`, pickle {cite:p}`van1995python`.

# # Results & Discussion

# In order to classify the wine qualities, we chose to use three different models, including support vector machine with linear kernal, logistic regression, and random forest. We carried out 5-fold cross validation on all three models to find the best performing model based on the cross validation scores. During the EDA stage of the project, we observed class imbalance in our data set (**_Fig. 1_**). Therefore, we decided to use several scoring metrics such as f1 score, Receiver Operating Characteristic - One versus Rest - Area under the curve (ROC-AUC-OVR), and Receiver Operating Characteristic - One versus One - Area under the curve (ROC-AUC-OVO). 

# ```{figure} ../../results/figure_1_class_imbalance.png
# 
# 
# Class imbalance in original data.
# ```

# Based on the cross validation results shown in **_Table. 1_**, the random forest model performed the best across three models. Therefore, the random forest model was selected for downstream hyperparamater tuning.

# **_Table. 1_** Summary on f1 macro scores, ROC AUC (OVR) and ROC AUC (OVO) of dummy classifier, SVC, logistic regression, and random forest with default hyperparameters.

# In[1]:


import pandas as pd
pd.read_csv("../../results/cross_val_results.csv", index_col = 0)


# To find the best parameters of the random forest model, we perform hyperparameter optimization on `n_estimators` and `max_depth` in the random forest model. The optimal hyperparameter results are shown in the **_Table. 2_**. We observed that the optimal `n_estimators` was 4641 and the max_depth was 26. During the hyperparameter optimization, we used `roc_auc_ovr` as our scoring metrics. The validation score for the optimized model is 0.867. Our model performs acceptable, and the test score for the optimized model is 0.685.

# **_Table. 2_** The best ROC-AUC-OVR cross-validation score together with the hyperparameter combination yielding the it, and the test score of this tuned random forest model on test examples.

# In[2]:


pd.read_csv("../../results/random_forest_results.csv", index_col = 0).round(3)


# In addition, we plotted the confusion matrix of model performance on test data to get insights of how our model performed. As seen in **_Fig. 2_**, our model was mostly confused among the quality classes of 5, 6 and 7. This is probably because the features do not have well separated distributions with respect to these classes. This is in line with what we observed in the preliminary exploratory data analysis. Although the model did not perform great on this classification task, our main task does not include any sensitive prediction. Therefore, we are relatively confident to share the results of our model.

# ```{figure} ../../results/test_cm.png
# 
# 
# Confusion matrix on test data.
# ```

# Among all the features that our data set had, alcohol, density and volatile acidity were the top 3 important features (see **_Table. 3_**). On the other hand, fixed acidity, type-white and type-red were the least important features. This result is also consistent with our initial exploratory data analysis. The features alcohol, density and volatile acidity were among the most important features that we observed during exploratory data analysis.

# **_Table. 3_** The feature importances of the optimized random forest model.

# In[3]:


pd.read_csv("../../results/feature_importances.csv", index_col = 0).round(3)


# Furthermore, to improve this model in future, we suggest to gather more wine samples from lower quality class and higher quality class to fix the severe class imbalance issue in the dataset so that it could be used to classify the wine qualities properly in the real world. Also, we could carry out feature engineering like adding polynomial features to our dataset or finding new features, and perform feature elimination to remove unimportant features.
# 
# In conclusion, we used the random forest model which has feature interaction and gives better cross validation scores than the other two models we tried. However, due to the presence of a almost $20\%$ gap between the cross-validation score and the test score, whether this model will generalize well to real-world unseen data remains a doubt.

# # Bibliography
# 
# ```{bibliography}
# ```
