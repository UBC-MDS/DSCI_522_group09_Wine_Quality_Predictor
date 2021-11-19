# author: Luming Yang
# date: 2021-11-18

"""This script automatically downloads both of the wine quality data csvs from the UCI database to a local filepath as a csv.
Usage: src/download_data.py
"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)  # parse these into dict opt; alphabetically

def main():
    urls = ("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv")
    files = ("../data/raw/winequality-red.csv", "../data/raw/winequality-white.csv")
    i = 0
    for url in urls:
        data = pd.read_csv(url, header=None)
        try:
            data.to_csv(files[i], index=False)
        except:
            os.makedirs(os.path.dirname(out_file))
            data.to_csv(out_file, index=False)
        i+=1


if __name__ == "__main__":
    main()
