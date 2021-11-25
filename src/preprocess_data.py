# author: Paniz Fazlali, Wanying Ye
# date: 2021-11-24

"""This script takes two file paths. It takes in the input path which includes the raw data and
the output directory to store the output data in. It performs data cleaning, transformating and 
partitioning. This script should have 4 outputs: cleaned but unpreprocessed train dataframe, 
cleaned but and unpreprocessed test dataframe, cleaned and preprocessed train dataframe and 
cleaned and preprocessed test dataframe.

Usage: preprocess_data.py --input_path_white=<input_path_white> --input_path_red=<input_path_red> --output_dir=<output_dir>

Options:
--input_path_white=<input_path_white>     The path including filename to the raw data of white wine (csv file)
--input_path_red=<input_path_red>         The path including filename to the raw data of red wine (csv file)
--output_dir=<output_dir>                 The directory to store wrangled data 
"""

from docopt import docopt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

opt = docopt(__doc__)

def main(input_path_white, input_path_red, output_dir):
    # input_path_white = "data/raw/winequality-white.csv"
    # input_path_red = "data/raw/winequality-red.csv"
    # output_dir = "data/processed"
    
    # read in white wine data
    white = pd.read_csv(input_path_white)
    white['type'] = 'white'
    white['quality'] = white['quality'].map(str)
    
    # read in red wine data
    red = pd.read_csv(input_path_red)
    red['type'] = 'red'
    red['quality'] = red['quality'].map(str)

    # gather both wine data in one dataframe
    data = pd.concat((white, red))

    # split data
    train_df, test_df = train_test_split(data, train_size=0.7, random_state=123)

    X_train, y_train = train_df.drop(columns=['quality']), train_df['quality']
    X_test, y_test = test_df.drop(columns=['quality']), test_df['quality']
    
    # transform data
    numeric_features = list(X_train.select_dtypes(include='number').columns)
    binary_features = ['type']
    preprocessor = make_column_transformer(
        (StandardScaler(), numeric_features),
        (OneHotEncoder(drop='if_binary'), binary_features)
    )
    columns = numeric_features + binary_features
    X_train_preprocessed = pd.DataFrame(preprocessor.fit_transform(X_train), index=X_train.index, columns=columns)
    X_test_preprocessed = pd.DataFrame(preprocessor.transform(X_test), index=X_test.index, columns=columns)
    
    # gathering X_train and y_train in one dataset
    train_df_preprocessed = X_train_preprocessed.copy()
    train_df_preprocessed['quality'] = y_train

    # gathering X_test and y_test in one dataset
    test_df_preprocessed = X_test_preprocessed.copy()
    test_df_preprocessed['quality'] = y_test
    
    
    # export cleaned unpreprocessed data
    try:
        train_df.to_csv(f"{output_dir}/train_df.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/train_df.csv"))
        train_df.to_csv(f"{output_dir}/train_df.csv")
    try:
        test_df.to_csv(f"{output_dir}/test_df.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}/test_df.csv"))
        test_df.to_csv(f"{output_dir}/test_df.csv")

    # export cleaned preprocessed data
    try:
        train_df_preprocessed.to_csv(f"{output_dir}/train_df_preprocessed.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}"))
        train_df_preprocessed.to_csv(f"{output_dir}/train_df_preprocessed.csv")
    try:
        test_df_preprocessed.to_csv(f"{output_dir}/test_df_preprocessed.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}"))
        test_df_preprocessed.to_csv(f"{output_dir}/test_df_preprocessed.csv")

if __name__ == "__main__":
    main(opt["--input_path_white"], opt["--input_path_red"], opt["--output_dir"])
