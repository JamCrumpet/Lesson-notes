import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_csv("pokemon_data.csv")

# making changes to data
print(df.head(5))
df["Total"] = df["HP"] + df["Attack"] + df["Defense"] +df["Sp. Atk"] + df["Sp. Def"] + df["Speed"] # creates new ...
# ... column consisting of following values
print(df.head(5))
df["Total"]


# saving data
df.to_csv("modified.csv") # creates new csv save file named modified.csv
# df.to_csv("modified.csv", index = False) # removes indexs

# df.to_excel("excel_modified.xlsx") # creates new excel save file named excel_modified.xlsl

# filtering data
new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Posion") & (df["HP"] > 70)] # only shows data for ...
#  ... multiple types and meeting certain condition
# ^ also creates new dataframe set as new_df

# when filtering data and shrinking data size, when printing it can effect indexes
# to resent index: new_df_new.df.reset_index()