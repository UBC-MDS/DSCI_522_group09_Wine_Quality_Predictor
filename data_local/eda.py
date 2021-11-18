# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python [conda env:573]
#     language: python
#     name: conda-env-573-py
# ---

# https://archive-beta.ics.uci.edu/ml/datasets/credit+approval
#
#
#
#
# https://archive-beta.ics.uci.edu/ml/datasets/divorce+predictors+data+set
# https://archive-beta.ics.uci.edu/ml/datasets/university
# https://archive-beta.ics.uci.edu/ml/datasets/climate+model+simulation+crashes
#
# https://archive-beta.ics.uci.edu/ml/datasets/wine+quality
#
#
# https://archive-beta.ics.uci.edu/ml/datasets/student+performance
# https://archive-beta.ics.uci.edu/ml/datasets/student+academics+performance

# # Dataset selection
#
# 1. Predict Student performance https://archive-beta.ics.uci.edu/ml/datasets/student+performance
# 2. Classify origin of wines https://archive-beta.ics.uci.edu/ml/datasets/wine
#
# Reasons: I have looked at both datasets. Both of them are relatively clean. They are easy to understand and work with. The description pages linked above are worth reading (very clear and straight to the point). 

import pandas as pd
# reading csv files
data =  pd.read_csv('../data/student/winequality-red.csv', sep=";")

# +
#data.columns = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9","A10", "A11", "A12", "A13", "A14", "A15", "A16"]
# -

data

import altair as alt
alt.Chart(data).mark_bar().encode(
    x = "A3",
    y = "count()"
)


