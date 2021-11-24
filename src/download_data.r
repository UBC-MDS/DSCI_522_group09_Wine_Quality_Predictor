# author: Wanying Ye
# date: 2021-11-23

"Downloads delimited data from the web to a local filepath as a csv.

Usage: download_data.r --url=<url> --out_file=<out_file> [--delimiter=delimiter]

Options: 
--url=<url>               URL from where to download the data (must standard csv format)
--out_file=<out_file>     Path (including the filename) of where to write the csv file locally
[--delimiter=<delimiter>] Optional nonstandard delimiter if file has a delimiter other than ','
" -> doc

library(tidyverse)
library(readr)
library(docopt)

opt <- docopt(doc)

main <- function(url, out_file, delimiter = ',') {
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    # out_file = "data/winequality-red.csv"
    # out_file = "data/winequality-white.csv"

    # read in data
    data <- read_delim(url, delim = ',')

    # write the csv file to a local path (but the output file is colon-seperated, not sure why)
    write_csv(data, out_file)
}

main(opt$url, opt$out_file, opt$delimiter)