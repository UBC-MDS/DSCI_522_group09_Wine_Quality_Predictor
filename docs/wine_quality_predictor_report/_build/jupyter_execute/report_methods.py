#!/usr/bin/env python
# coding: utf-8

# # Methods

# ## Data
# 
# The data sets used in this project were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis {cite:p}`cortez2009modeling`. They were sourced from the UC Irvine Machine Learning Repository {cite:ps}`Dua:2019` and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. We combined these columns and created a new feature to indicate colour. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer but we treat as a classification task) ranging from 3 (very bad) to 9 (excellent) that represents the quality of the wine.

# ## Analysis
# 
# Three classification models were attempted and assessed to predict the quality score of a wine: [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), [Support Vector Machine with linear kernel (SVC linear)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) and [Random Forest Classification](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html). These candidates were selected based on their common intriguing attributes such as high interpretability and giving handy measurements on feature importance. All numeric features in the original datasets were included and scaled, with the type of wine (_i.e._ white or red) as an added binary feature. 
# 
# During the EDA stage, we discovered the data set has severe class-imbalance issue. Our target is multi-class in terms of quality scores ranging from "3" to "9". However, the classes "3" and "9" were extremely under-populated. Therefore, we decided to combine the lowest two classes ("3" and "4") and the highest two classes ("8" and "9") to mitigate the severe class imbalance problem. By doing so, the number of examples in each class is distributed more evenly. The final quality score classes are "<=4", "5", "6", "7" and ">=8". The best wines will be classified as ">=8", and the poorest wines will be classified as "<=4".
# 
# We also chose the scoring metrics to be f-1 macro score, Receiver Operating Characteristic (One vs. Rest) Area Under the Curve, and Receiver Operating Characteristic (One vs. One) Area Under the Curve. 
# 
# For each algorithm, the default hyperparameters were used first to train the model, and then the 5-fold cross-validation scores were compared across the models. Hyperparameter optimization was carried out on the algorithm with the best cross-validation score. The resulting model with the optimized hyperparameters was the solution to this prediction task. We then assess its performance on test data (_i.e._ unseen examples).
# 
# The computing language used in this project is Python {cite:p}`perez2011python`. Packages used in EDA and machine learning analysis include: altair {cite:p}`vanderplas2018altair`, docopt {cite:p}`docopt`, scikit-learn {cite:p}`scikit-learn`, matplotlib {cite:p}`Hunter:2007`, numpy {cite:p}`harris2020array`, pandas {cite:p}`mckinney2010data`, pickle {cite:p}`van1995python`.

# In[ ]:




