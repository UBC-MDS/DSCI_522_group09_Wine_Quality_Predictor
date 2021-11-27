# Wine_Quality_Predictor

- authors: Gabriel Fairbrother, Paniz Fazlali, Luming Yang, Wanying Ye.

A data analysis (machine learning) project for MDS DSCI522 (Data Science Workflows) from Group 09.

## About

Wine is a product that is both an extremely popular and highly consumed product, and one that can be very expensive to buy and lucrative to sell. It is also sold at much higher variety levels than almost any other consumer product - in some supermarkets well over 1000 different wines are stocked.{cite}

At the same time, it is also one of the hardest to identify quality ahead of purchase, since you must consume it to decide. The level of quality a consumer might require can even vary wildly depending on the consumption occasion ([2 https://psycnet.apa.org/record/2001-11394-001]).

The quality of wine however is difficult to evaluate objectively and is reliant on some very subjective sensory elements. However we believe that this question can be answered by evaluating which physicochemical features are important in determining the quality score of a wine, the wine manufacturers can refine certain wine-making procedures that may yield wines with "promising" properties.

We also believe that by using a quality score that is a human taste output (i.e. each quality score is a median taken over a minimum of 3 sensory assessors) instead of following an objective and rigid standard, which makes wine certification a complicated task, we can better capture the inherent subjectivity of the task. Therefore, attempting to unravel the relationship between physicochemical properties and human taste sensations may also be a direction in the wine certification field [3(Cortez, Cerdeira, Almeida, Matos and Reis, 2009).]


The data sets were sampled from the red and white _vinho verde_ wines from the North of Portugal, created by P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis (2009). The data sets were sourced from the UC Irvine Machine Learning Repository and can be found [here](https://archive-beta.ics.uci.edu/ml/datasets/wine+quality). One data set is for the red wine, and the other is for the white wine, and both data sets have the same features and target columns. Each row represents a wine sample with its physicochemical properties such as fixed acidity, volatile acidity, etc. The target is a score (integer) ranging from 0 (very bad) to 10 (excellent) that represents the quality of the wine. 

## Report

[The final report can be found here](https://github.com/UBC-MDS/DSCI_522_group09_Wine_Quality_Predictor/reports/wine_quality_predictor_report/_build/html/index.html).

## Usage
To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands at the command line/terminal from the root directory of this project:
```python
python -m ipykernel install --user --name wine_quality_predictor --display-name "Wine Quality Predictor"
conda env create --file src/environment.yml
conda activate wine_quality_predictor
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" --out_file="data/raw/winequality-red.csv" --delimiter=";"
python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv" --out_file="data/raw/winequality-white.csv" --delimiter=";"  
python src/preprocess_data.py --input_path_white="data/raw/winequality-white.csv" --input_path_red="data/raw/winequality-red.csv" --output_dir="data/processed"  
python src/eda.py --input_data="data/processed/train_df.csv" --output_dir="results"
python src/machine_learning.py --input_path_train="data/processed/train_df.csv" --input_path_test="data/processed/test_df.csv" --output_dir="results"
jupyter-book build reports/wine_quality_predictor_report
```
We are aware that there is an issue with the eda.py script on windows and are working on a resolution. We appear to be missing something in our environment.
  
```  
## Dependencies
From the root of this project, please run  `conda env create -f src/environment.yml`

## References

[References can be found here](https://github.com/UBC-MDS/DSCI_522_group09_Wine_Quality_Predictor/reports/wine_quality_predictor_report/_build/html/references.html).