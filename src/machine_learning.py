# author: Luming Yang, Paniz Fazlali
# date: 2021-11-25

"""This script takes two file paths. It takes in the input path which includes the clean train and test data
and the output directory to store the results in. It performs machine learning analysis. 
This script will have 4 outputs: 3 tables and 1 figure.

Usage: src/machine_learning.py --input_path_train=<input_path_train> --input_path_test=<input_path_test> --output_dir=<output_dir>

Options:
--input_path_train=<input_path_train>     The path including filename to the raw data of white wine (csv file)
--input_path_test=<input_path_test>       The path including filename to the raw data of red wine (csv file)
--output_dir=<output_dir>                 The directory to the tables and figures
"""

from docopt import docopt
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV, cross_validate
from sklearn.metrics import ConfusionMatrixDisplay

opt = docopt(__doc__)


def main(input_path_train, input_path_test, output_dir):
    # input_path_train = "data/processed/train_df.csv"
    # input_path_test = "data/processed/test_df.csv"
    # output_dir = "results"

    # read in data
    train_df = pd.read_csv(input_path_train)
    test_df = pd.read_csv(input_path_test)

    # combine classes to deal with the issue of under-populated classes
    train_df.loc[train_df["quality"] == 3, "quality"] = 4
    train_df.loc[train_df["quality"] == 9, "quality"] = 8
    train_df["quality"] = train_df["quality"].map(str)

    test_df.loc[test_df["quality"] == 3, "quality"] = 4
    test_df.loc[test_df["quality"] == 9, "quality"] = 8
    test_df["quality"] = test_df["quality"].map(str)

    # X_train and y_trian
    X_train, y_train = train_df.drop(columns=["quality"]), train_df["quality"]
    X_test, y_test = test_df.drop(columns=["quality"]), test_df["quality"]

    # define the transformer
    numeric_features = list(X_train.select_dtypes(include="number").columns)
    categorical_features = ["type"]
    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        (OneHotEncoder(handle_unknown="ignore", sparse=False), categorical_features),
    )

    # models
    dummy = make_pipeline(
        preprocessor, DummyClassifier(strategy="stratified", random_state=123)
    )
    svc = make_pipeline(
        preprocessor, SVC(kernel="linear", probability=True, random_state=123)
    )
    lr = make_pipeline(
        preprocessor, LogisticRegression(max_iter=5000, random_state=123)
    )
    rf = make_pipeline(preprocessor, RandomForestClassifier(random_state=123))

    models = {}
    models["Dummy"] = dummy
    models["SVC"] = svc
    models["Logistic Regression"] = lr
    models["Random Forest"] = rf

    # scoring metrics
    scoring = ["accuracy", "f1_macro", "roc_auc_ovr", "roc_auc_ovo"]

    # perform cross_validation
    results = {}
    for key, value in models.items():
        results[key] = mean_std_cross_val_scores(
            value,
            X_train,
            y_train,
            return_train_score=True,
            scoring=scoring,
            error_score="raise",
        )
    cross_val_results = (
        pd.DataFrame(results).rename(index={"test_score": "cross_validation_score"}).T
    )

    # hyperparameter optimization for the best model (random forest classifier)
    param_grid_rf = {
        "randomforestclassifier__n_estimators": np.logspace(1, 4, 10, dtype=int),
        "randomforestclassifier__max_depth": np.linspace(1, 30, 10, dtype=int),
    }

    search_rf = RandomizedSearchCV(
        rf,
        param_distributions=param_grid_rf,
        return_train_score=True,
        n_jobs=-1,
        n_iter=30,
        cv=5,
        random_state=123,
        scoring="roc_auc_ovr",
        error_score="raise",
    )
    search_rf.fit(X_train, y_train)

    # results of random forest
    rf_results = {
        "Random Forest Best n_estimators": search_rf.best_params_[
            "randomforestclassifier__n_estimators"
        ],
        "Random Forest Best max_depth": search_rf.best_params_[
            "randomforestclassifier__max_depth"
        ],
        "Random Forest Best Validation Score": search_rf.best_score_,
        "Random Forest Roc_Auc Test Score": search_rf.best_estimator_.score(
            X_test, y_test
        ),
    }
    rf_results = pd.DataFrame(rf_results, index=[0])

    # confusion matrix
    test_cm = ConfusionMatrixDisplay.from_estimator(
        search_rf.best_estimator_, X_test, y_test, display_labels=['<=4', '5', '6', '7', '>=8']
    )

    # feature importances
    categorical_columns = list(
        search_rf.best_estimator_.named_steps["columntransformer"]
        .named_transformers_["onehotencoder"]
        .get_feature_names_out()
    )
    all_columns = numeric_features + categorical_columns
    feature_importances = pd.DataFrame(
        search_rf.best_estimator_.named_steps[
            "randomforestclassifier"
        ].feature_importances_,
        index=all_columns,
        columns=["Feature Importances"],
    ).sort_values(by="Feature Importances", ascending=False).drop(index='Unnamed: 0')

    # export tables, figures and model
    try:
        cross_val_results.to_csv(f"{output_dir}/cross_val_results.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/cross_val_results.csv"))
        cross_val_results.to_csv(f"{output_dir}/cross_val_results.csv")
    try:
        rf_results.to_csv(f"{output_dir}/random_forest_results.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/random_forest_results.csv"))
        rf_results.to_csv(f"{output_dir}/random_forest_results.csv")
    try:
        feature_importances.to_csv(f"{output_dir}/feature_importances.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/feature_importances.csv"))
        feature_importances.to_csv(f"{output_dir}/feature_importances.csv")
    try:
        plt.savefig(f"{output_dir}/test_cm.png")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/test_cm_png"))
        plt.savefig(f"{output_dir}/test_cm.png")
    try:
        pickle.dump(search_rf.best_estimator_, open(f"{output_dir}/random_forest.rds", "wb"))
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/random_forest.rds"))
        pickle.dump(search_rf.best_estimator_, open(f"{output_dir}/random_forest.rds", "wb"))



# helper function, adapted from 573 lecture 4
# https://pages.github.ubc.ca/mds-2021-22/DSCI_573_feat-model-select_students/lectures/04_feat-importances-selection.html
def mean_std_cross_val_scores(model, X_train, y_train, **kwargs):
    """
    Returns mean and std of cross validation

    Parameters
    ----------
    model :
        scikit-learn model
    X_train : numpy array or pandas DataFrame
        X in the training data
    y_train :
        y in the training data

    Returns
    ----------
        pandas Series with mean scores from cross_validation
    """

    scores = cross_validate(model, X_train, y_train, **kwargs)

    mean_scores = pd.DataFrame(scores).mean()
    std_scores = pd.DataFrame(scores).std()
    out_col = []

    for i in range(len(mean_scores)):
        out_col.append((f"%0.3f (+/- %0.3f)" % (mean_scores[i], std_scores[i])))

    return pd.Series(data=out_col, index=mean_scores.index)


if __name__ == "__main__":
    main(opt["--input_path_train"], opt["--input_path_test"], opt["--output_dir"])
