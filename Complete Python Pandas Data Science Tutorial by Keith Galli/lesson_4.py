import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# df = pd.read_csv("modified.csv.csv") # how you would normally read data

# when working with large data sets (20GB) you can read chunks of data
df = pd.read_csv("modified.csv", chunksize=5) # chucksize paramater = 5 means 5 rows are being passed in a time

# for example
# for df in pd.read_csv("modified.csv", chunksize=5):
    # df would be equal to 5 rows in modified.csv
for df in pd.read_csv("modified.csv", chunksize=5):
    print("\t\t\t - - - Example Spacing - - -")
    print(df)