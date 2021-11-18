import pandas as pd
# reading csv files
data =  pd.read_csv('../data/student/winequality-red.csv', sep=";")


#data.columns = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9","A10", "A11", "A12", "A13", "A14", "A15", "A16"]


data


import altair as alt
alt.Chart(data).mark_bar().encode(
    x = "A3",
    y = "count()"
)



