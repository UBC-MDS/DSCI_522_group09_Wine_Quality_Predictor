# Wine_Quality_Predictor

- authors: Gabriel Fairbrother, Paniz Fazlali, Luming Yang, Wanying Ye.

A data analysis (machine learning) project for MDS DSCI522 (Data Science Workflows) from Group 09.

## About
 Can we use a machine learning model to predict the human perceived quality of a wine using its physical and chemical attributes? Moreover which of these attribute contributes most to that percieved quality? We compared results from 3 different machine learning models (SVC with Linear Kernel, Logistic Regression, and Random Forest) and selected the best performer (Random Forest). With Random Forest we achieved an ROC/AUC score of 0.86. Further, we found that Alcohol, Density and Volatile Acidity were the top contributors to higher quality scores.


The data sets were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009). The data sets were sourced from the UC Irvine Machine Learning Repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine. 

## Report

[The final report can be found here](https://htmlpreview.github.io/?https://github.com/UBC-MDS/DSCI_522_group09_Wine_Quality_Predictor/blob/main/reports/wine_quality_predictor_report/_build/html/report_summary.html).

## Usage
To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands at the command line/terminal from the root directory of this project:
```python
python -m ipykernel install --user --name wine_quality_predictor --display-name "Wine Quality Predictor"

# creating conda environment
conda env create --file src/environment.yml
conda activate wine_quality_predictor
**For Windows Users:
npm install -g vega vega-cli vega-lite canvas

# downloading data
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" --out_file="data/raw/winequality-red.csv" --delimiter=";"
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv" --out_file="data/raw/winequality-white.csv" --delimiter=";"  

# preprocessing data
python src/preprocess_data.py --input_path_white="data/raw/winequality-white.csv" --input_path_red="data/raw/winequality-red.csv" --output_dir="data/processed"  

# eda
python src/eda.py --input_data="data/processed/train_df.csv" --output_dir="results"

# machine learning analysis
python src/machine_learning.py --input_path_train="data/processed/train_df.csv" --input_path_test="data/processed/test_df.csv" --output_dir="results"

# final report
jupyter-book build reports/wine_quality_predictor_report
```
We are aware that there is an issue with the eda.py script on windows and are working on a resolution. We appear to be missing something in our environment.
    
## Dependencies
From the root of this project, please check src/environment.yml

## References

[References can be found here](https://htmlpreview.github.io/?https://github.com/UBC-MDS/DSCI_522_group09_Wine_Quality_Predictor/blob/main/reports/wine_quality_predictor_report/_build/html/bibliography.html).
