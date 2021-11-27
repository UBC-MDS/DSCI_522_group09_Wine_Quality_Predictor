#!/usr/bin/env python
# coding: utf-8

# # Methods

# ## Data
# 
# The data sets used in this project were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos, and José Reis {cite:p}`cortez2009modeling`. They were sourced from the UC Irvine Machine Learning Repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine.

# ## Analysis
# 
# Three classification models were attempted and assessed to predict the quality score of a wine: the logistic regression model, the support machine vector with linear kernel (SVM RBF) and the random forest regression model. These candidates were selected based on their common intriguing attributes such as high interpretability and giving handy measurements on feature importance. All numeric features in the original datasets were included and scaled, with the type of wine (_i.e._ white or red) as an added binary feature. 
# 
# To address the problem of class imbalance, we re-categorized the targets classes into $\leq4$, $5$, $6$, $7$ and $\geq8$ so that there are enough training examples in each class. We also chose the scoring metrics to be f-1 macro score, Receiver Operating Characteristic (One vs. Rest) Area under the curve, and Receiver Operating Characteristic (One vs. One) Area under the curve. 
# 
# For each algorithm, the default hyperparameters were used first to train the model, and then the 5-fold cross-validation scores were compared across 3 models. Hyperparameter optimization was carried out on the algorithm with the best cross-validation score. The resulting model with the optimized hyperparameters was the solution to this prediction task. We then assess its performance on test data (_i.e._ unseen examples).
# 
# The computing language used in this project is Python {cite:p}`perez2011python`. Packages used in EDA and machine learning analysis include: altair {cite:p}`vanderplas2018altair`, docopt {cite:p}`docopt`, scikit-learn {cite:p}`scikit-learn`, matplotlib {cite:p}`Hunter:2007`, numpy {cite:p}`harris2020array`, pandas {cite:p}`mckinney2010data`, pickle {cite:p}`van1995python`.

# ## Bibliography
# 
# ```{bibliography} references.bib
# :filter: docname in docnames
# ```

# In[ ]:




