# Wine_Quality_Predictor


- authors: Gabriel Fairbrother, Paniz Fazlali, Luming Yang, Wanying Ye.


A data analysis (machine learning) project for MDS DSCI522 (Data Science Workflows) from Group 09.

## About

In this project, we are trying to answer the question what are the top contributing physicochemical features to a high-quality wine? This question is of marketing significance in the way that if we can decide which physicochemical features are important in determining the quality score of a wine, the wine manufacturers can refine certain wine-making procedures that may yield wines with "promising" properties. Noteworthy, the quality score is a human taste output (_i.e._ each quality score is a median taken over a minimum of 3 sensory assessors) instead of following an objective and rigid standard, which makes wine certification a complicated task. Therefore, attempting to unravel the relationship between physicochemical properties and human taste sensations may also be a direction in the wine certification field (Cortez, Cerdeira, Almeida, Matos and Reis, 2009).


The data sets were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009). The data sets were sourced from the UC Irvine Machine Learning Repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine. 


In order to answer the research question stated above, we plan to construct multiple classification machine learning models to predict on the quality of wines, and report the best model with highest metric score of interest. Before building any model, we plan to partition the data into a training split and a test split (70% for training and 30% for test). The next step will be performing analysis on the results to explore accuracy of our model as well as correlation between features and the resultant quality rating. 

ML Model candidates include: kNN, SVM, logistic regression, decision tree. These candidates may vary but the intention is to evaluate 4.

We plan to merge the red and white datasets. The preprocessing of the data includes scaling all numeric features into the same scales, and One Hot Encoding on the type of wines (_i.e._ white or red) as an added feature.
  
After building a pipeline with the preprocessor and an estimator, we are going to carry out hyperparameter optimization through cross validation. We expect to have one graph showing the metric score (_e.g. accuracy_) vs. hyperparameter values for each estimator we will attempt. We also plan as a stretch goal to evaluate which features contribute most to quality by using feature coefficients which we will present as a visualization.

Finally, we will rank models by their performance and select the best model with highest metric score as the final model. We will re-fit the model on the entire training set. The prediction performance will be summarized in the final report as a table.

Thus far the EDA performed can be found [here](https://github.com/UBC-MDS/DSCI_522_group09_Wine_Quality_Predictor/tree/main/src/EDA.ipynb) 

## Usage
To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands at the command line/terminal from the root directory of this project:
```
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" --out_file="data/raw/winequality-red.csv" --delimiter='";"
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv" --out_file="data/raw/winequality-white.csv" --delimiter=";"
jupyter lab EDA.ipynb
  
```  
## Dependencies
  We will collect a list of dependencies as we move through the project to publish here.

## References
Wine Quality 
Paulo Cortez, A. Cerdeira, F. Almeida, T. Matos, J. Reis
http://www3.dsi.uminho.pt/pcortez/wine5.pdf
“UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences.
https://archive-beta.ics.uci.edu/ml/datasets/wine+quality
