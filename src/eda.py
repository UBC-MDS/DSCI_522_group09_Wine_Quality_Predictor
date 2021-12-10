# author: Wanying Ye
# date: 2021-11-24

"""This script takes multiple file paths. It takes in input path of the cleaned training data. 
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
    train_df["quality"] = train_df["quality"].map(str)

    # make tables
    ## count target values
    counts = pd.DataFrame(train_df["quality"].value_counts()).reset_index()
    counts.columns = ["Quality score", "Counts"]
    counts = counts.sort_values(by="Quality score").set_index(counts.columns[0])
    
    ## summarize features in training data
    summary = train_df.groupby("quality").agg(["mean", "std"]).round(2).reset_index()

    # export tables
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_tables_lst = [train_df.head(), counts, summary]
    output_tables_name = [
        "table_1_combined_dataset.csv",
        "table_2_observations_count.csv",
        "table_3_summary.csv",
    ]
    for i in range(len(output_tables_lst)):
        if not os.path.exists(f"{output_dir}/" + output_tables_name[i]):
            output_tables_lst[i].to_csv(f"{output_dir}/" + output_tables_name[i])


    # make figures
    ## target distribution bar plot
    figure_1 = alt.Chart(train_df, title="Class Imbalance of Wine Quality").mark_bar().encode(
        alt.X("quality", title="Quality", axis=alt.Axis(labelAngle=0)),
        alt.Y("count()", title="Counts"),
        alt.Color("quality", title="Quality"),
    ).properties(width=350, height=350)

    ## target distribution bar plot for red and white wines 
    figure_2 = alt.Chart(train_df, title="Red and White Wine Quantities").mark_bar(opacity=0.5).encode(
    alt.X("quality", title="Quality", axis=alt.Axis(labelAngle=0)),
    alt.Y("count()", title="Counts", stack=False),
    alt.Color("type", title="Wine type"),
    ).properties(width=350, height=350)

    ## distribution of features
    figure_3 = alt.Chart(train_df).mark_line(interpolate="step").encode(
    alt.X(alt.repeat(), type="quantitative", bin=alt.Bin(maxbins=40)),
    alt.Y("count()", title="Counts"),
    alt.Color("quality", title="Quality"),
    ).properties(width=300, height=450).repeat(
    [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
    ],
    columns=3,
    )
    
    ## correlation plot including all numeric features and the target
    train_df_int = train_df.copy()
    train_df_int["quality"] = train_df_int["quality"].map(int)
    corr_df = train_df_int.select_dtypes('number').corr('spearman').stack().reset_index(name='corr')
    corr_df.loc[corr_df['corr'] == 1, 'corr'] = 0  # Remove diagonal
    corr_df['abs'] = corr_df['corr'].abs()
    ### make the target appear at last in correlation plot
    variable_order = train_df.select_dtypes('number').columns.to_list()
    figure_4 = alt.Chart(corr_df, title="Correlation plot").mark_circle().encode(
    x=alt.X('level_0', title="", sort=variable_order),
    y=alt.Y('level_1', title="", sort=variable_order),
    size=alt.Size('abs', title="Magnitude of correlation"),
    color=alt.Color('corr', 
                    scale=alt.Scale(scheme='blueorange', domain=(-1, 1)),
                    title="Correlation",
                   ))

    # export figures
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_figures_lst = [figure_1, figure_2, figure_3, figure_4]
    output_figures_name = [
        "figure_1_class_imbalance.png",
        "figure_2_red_and_white_quantities.png",
        "figure_3_distribution_of_features.png",
        "figure_4_correlation_plot.png",
    ]
    for i in range(len(output_figures_lst)):
        if not os.path.exists(f"{output_dir}/" + output_figures_name[i]):
            output_figures_lst[i].save(
                f"{output_dir}/" + output_figures_name[i], scale_factor=3
            )


if __name__ == "__main__":
    main(opt["--input_data"], opt["--output_dir"])
