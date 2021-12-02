# Makefile
# Paniz Fazlali
# 2021-12-01
# 
# Driver script/analysis pipeline for milestone 3
# 
# Usage:
# make all

all : report

# downloading data
data/raw/winequality-red.csv : src/download_data.py
	python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" --out_file="data/raw/winequality-red.csv" --delimiter=";"


data/raw/winequality-white.csv : src/download_data.py
	python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv" --out_file="data/raw/winequality-white.csv" --delimiter=";"  

# preprocessing data
data/processed: src/preprocess_data.py data/raw/winequality-red.csv data/raw/winequality-white.csv 
	python src/preprocess_data.py --input_path_white="data/raw/winequality-white.csv" --input_path_red="data/raw/winequality-red.csv" --output_dir="data/processed"  

# eda
results_eda: src/eda.py data/processed/train_df.csv
	python src/eda.py --input_data="data/processed/train_df.csv" --output_dir="results"

# machine learning analysis
results_ml: src/machine_learning.py data/processed
	python src/machine_learning.py --input_path_train="data/processed/train_df.csv" --input_path_test="data/processed/test_df.csv" --output_dir="results"

# final report
report: results_ml results_eda
	jupyter-book build docs/wine_quality_predictor_report

clean :
	rm -rf data/raw//winequality-red.csv data/raw//winequality-white.csv
	rm -rf data/processed/train_df.csv data/processed/test_df.csv
	rm -rf results/cross_val_results.csv results/feature_importances.csv results/figure_1_class_imbalance.png results/figure_2_red_and_white_quantities.png results/figure_3_distribution_of_features.png results/random_forest_results.csv results/table_1_combined_dataset.csv results/table_2_observations_count.csv results/table_3_summary.csv results/test_cm.png resuls/random_forest.rds 
	# Not sure which file I should delete! rm -rf docs/wine_quality_predictor_report
