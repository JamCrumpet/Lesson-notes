import pandas as pd
import numpy

ebola_df = pd.read_csv("country_timeseries.csv")
print(ebola_df.head())

ebola_melt = pd.melt(ebola_df,
                     id_vars=["Date", "Day"])

print(ebola_melt)

print("Cases_Guinea".split("_")) # split() will split within a space, inputting "_" will split by delimiter _

variable_split = ebola_melt["variable"].str.split("_") #.str allows you to treat column like a string
print(variable_split)
print(type(variable_split)) # shows variable is a list

