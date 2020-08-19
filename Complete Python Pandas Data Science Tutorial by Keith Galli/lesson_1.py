import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_csv("pokemon_data.csv")

print(df)
print(df.head(3)) # prints top 3 row
print((df.tail(3))) # prints bottom 3 rows

# df_xlsl = pd.read_excel("pokemon_data.xlsx")

txt_df = pd.read_csv("pokemon_data.txt", delimiter = "\t") # w/o delimiter data wont separate properly
print(txt_df)

print(df.columns) # prints headers
print(df["Name"]) # prints each column
print(df["Name"][0:4]) # prints column's 0:4
print(df[["Name", "Type 1", "HP"]]) # prints multiple columns
print("Specific row: ", df.iloc[45]) # iloc = interger location # prints information in the following row
print("Specific row: ", df.iloc[4:6])
print("Really specific item: ", df.iloc[2,1]) # reads specific location, iloc[row,column]
print(df.loc[df["Type 1"] == "Fire"]) # prints non interger based info, based off context
print(df.describe()) # gives high level stats i.e mean, min and other metrics
print(df.sort_values("Name")) # .sort_values() sorts by selected value .i.e column
print(df.sort_values("Name", ascending = False)) # ascending = False reverses
print(df.sort_values("Type 1", "HP", ascending = [1,0])) # sets Type 1 to ascending and hp to descending