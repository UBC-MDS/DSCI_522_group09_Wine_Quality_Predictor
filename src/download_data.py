# author: Gabe Fairbrother, Luming Yang
# date: 2021-11-19

"""Downloads separated value data from the web to a local filepath as a csv.

Usage: download_data.py --url=<url> --out_file=<out_file> [--delimiter=delimiter]

Options: 
--url=<url>               URL from where to download the data (must standard csv format)
--out_file=<out_file>     Path (including the filename) of where to write the file locally
[--delimiter=<delimiter>] Optional nonstandard delimiter if file has a delimiter other than ','

"""

import os
import pandas as pd
from docopt import docopt

opt = docopt(__doc__)  # parse these into dict opt; alphabetically

def main(url, out_file, delimiter=','):
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    # out_file = "data/winequality-red.csv"
    # out_file = "data/winequality-white.csv"

  data = pd.read_csv(url, delimiter=delimiter )
  try:
      data.to_csv(out_file, index=False)
  except:
      os.makedirs(os.path.dirname(out_file))
      data.to_csv(out_file, index=False)


if __name__ == "__main__":
    main(opt['--url'], opt['--out_file'], opt['--delimiter'])