# author: Wanying Ye
# date: 2021-11-23

"""This script takes multiple file paths. It takes in input path which includes the training data. 
Then, it performs EDA and outputs the summarized tables and figures to corresponding paths.

Usage: eda.py --input_data=<input_data> --output_dir=<output_dir>

Options:
--input_data=<input_data>    The path including filename to the training split
--output_dir=<output_dir>    The directory path containing the outputs
"""

from docopt import docopt
import pandas as pd
import os

opt = docopt(__doc__)

def main(input_data, output_dir):

    # read in train_df.csv
    train_df = pd.read_csv(input_data, index_col=0)

    # count target values
    counts = pd.DataFrame(train_df["quality"].value_counts()).reset_index()
    counts.columns = ["Quality score", "Counts"]
    counts = counts.sort_values(by="Quality score").set_index(counts.columns[0])
    
    # summarize features in training data
    summary = train_df.groupby("quality").agg(["mean", "std"]).round(2).reset_index()

    # export tables and figures
    try:
        counts.to_csv(f"{output_dir}/target_distribution.csv")
    except:
        os.makedirs(os.path.dirname(f"{output_dir}"))
        counts.to_csv(f"{output_dir}/target_distribution.csv")

    try:
        summary.to_csv(f"{output_dir}/feature_summary.csv", index=False)
    except:
        os.makedirs(os.path.dirname(f"{output_dir}"))
        summary.to_csv(f"{output_dir}/feature_summary.csv", index=False)

if __name__ == "__main__":
    main(opt["--input_data"], opt["--output_dir"])
