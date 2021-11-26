# author: Paniz Fazlali, Wanying Ye
# date: 2021-11-24

"""This script takes two file paths. It takes in the input path which includes the raw data and
the output directory to store the output data in. It performs data cleaning and partitioning. 
This script will have 2 outputs: cleaned train dataframe and cleaned test dataframe.

Usage: src/preprocess_data.py --input_path_white=<input_path_white> --input_path_red=<input_path_red> --output_dir=<output_dir>

Options:
--input_path_white=<input_path_white>     The path including filename to the raw data of white wine (csv file)
--input_path_red=<input_path_red>         The path including filename to the raw data of red wine (csv file)
--output_dir=<output_dir>                 The directory to store wrangled data 
"""

from docopt import docopt
import pandas as pd
import os
from sklearn.model_selection import train_test_split

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
    
    # export clean data
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

if __name__ == "__main__":
    main(opt["--input_path_white"], opt["--input_path_red"], opt["--output_dir"])
