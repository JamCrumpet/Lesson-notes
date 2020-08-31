# tidying messy data sets
# 5 most common problems with messy datasets, along with their remedies:
# column headers are values not variable names
# multiple variable are stored in one column
# variable are stored in both rows and columns
# multiple types of observational units are stored in the same table
# a single observational unit is stored in multiple tables


import pandas as pd

pew_df = pd.read_csv("pew.csv")

print(pew_df.head()) # data comes in income brackets which should be in one bracket e.g. income

# id_vars turns multiple columns into single columns and tells ...
pew_long= pd.melt(pew_df, id_vars="religion",# ... which columns not to touch...
                  var_name="income", # var_name= changes variable name to income
                  value_name = "count") # changes value name to count


print(pew_long)

billboard_df = pd.read_csv("billboard.csv")

print(billboard_df.head())
billboard_melt = pd.melt(
    billboard_df, # select dataset I want to melt is billboard_df
    id_vars=["year", "artist", "track", "time", "date.entered"], # id_vars is that data you don'jt want melted,
    var_name = "week",
    value_name = "rating",
                        )

print(billboard_melt)

# billboard_df was originally 317 x 81, billboard_melt is 24092 x 7