#!/usr/bin/env python
# coding: utf-8

# # Results & Discussion

# To see whether there is some relation between different features and also to have an idea on whether some features are more important in prediction, we explored the correlation plot for all numeric features and the wine quality score. As shown in **_Fig. 1_**, several features have strong correlation. For example, `total sulfur dioxide` and `free sulfur dioxide` are strongly positively correlated, and `alcohol` and `density` are strongly negatively correlated. Additionally, the high correlation between the target `quality` and some features (_i.e._ `alcohol`, `density`, `chlorides`, `volatile acidity`) imply that these features might be important for prediction.

# ```{figure} ../../results/figure_4_correlation_plot.png
# 
# 
# Correlation plot for all numeric features (excluding wine type) and quality score.
# ```

# In order to classify the wine qualities, we chose to use three different models, including support vector machine with linear kernel, logistic regression, and random forest. We carried out 5-fold cross validation on all three models to find the best performing model based on the cross validation scores. During the EDA stage of the project, we observed class imbalance in our data set (**_Fig. 2_**). Therefore, we decided to use several scoring metrics such as f1 score, Receiver Operating Characteristic - One versus Rest - Area under the curve (ROC-AUC-OVR), and Receiver Operating Characteristic - One versus One - Area under the curve (ROC-AUC-OVO). 

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


# In addition, we plotted the confusion matrix of model performance on test data to get insights of how our model performed. As seen in **_Fig. 3_**, our model was mostly confused among the quality classes of 5, 6 and 7. This is probably because the features do not have well separated distributions with respect to these classes. This is in line with what we observed in the preliminary exploratory data analysis. Although the model did not perform great on this classification task, our main task does not include any sensitive prediction. Therefore, we are relatively confident to share the results of our model.

# ```{figure} ../../results/test_cm.png
# 
# 
# Confusion matrix on test data.
# ```

# Among all the features that our data set had, alcohol, density and volatile acidity were the top 3 important features (see **_Table. 3_**). On the other hand, fixed acidity, type-white and type-red were the least important features. This result is also consistent with our initial exploratory data analysis. The features alcohol, density and volatile acidity were among the most important features that we observed during exploratory data analysis.

# **_Table. 3_** The feature importances of the optimized random forest model.

# In[3]:


pd.read_csv("../../results/feature_importances.csv", index_col = 0).round(3)


# ## Conclusions
# 
# In conclusion, we used the random forest model which has feature interaction and gives better cross validation scores than the other two models we tried. However, due to the presence of a almost 20% gap between the cross-validation score and the test score, whether this model will generalize well to real-world unseen data remains a doubt.
# 
# ## Limitations
# Furthermore, to improve this model in future, we suggest to gather more wine samples from lower quality class and higher quality class to fix the severe class imbalance issue in the dataset so that it could be used to classify the wine qualities properly in the real world. Also, we could carry out feature engineering like adding polynomial features to our dataset or finding new features, and perform feature elimination to remove unimportant features.

# In[ ]:




