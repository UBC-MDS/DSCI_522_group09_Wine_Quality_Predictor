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
import altair as alt
alt.data_transformers.enable('data_server')
alt.renderers.enable('mimetype')

opt = docopt(__doc__)

def main(input_data, output_dir):

    # read in train_df.csv
    train_df = pd.read_csv(input_data, index_col=0)
    train_df["quality"] = train_df['quality'].map(str)

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

    # target counts distribution (bar plot)
    figure_1 = alt.Chart(train_df, title="Class Imbalance of Wine Quality").mark_bar().encode(
        alt.X("quality", title="Quality", axis=alt.Axis(labelAngle=0)),
        alt.Y("count()", title="Counts"),
        alt.Color("quality", title="Quality"),
    ).properties(width=350, height=350)

    try:
        figure_1.save(f"{output_dir}/target_distribution.png", scale_factor=3)
    except:
        os.makedirs(os.path.dirname(f"{output_dir}"))
        figure_1.save(f"{output_dir}/target_distribution.png", scale_factor=3)


if __name__ == "__main__":
    main(opt["--input_data"], opt["--output_dir"])
