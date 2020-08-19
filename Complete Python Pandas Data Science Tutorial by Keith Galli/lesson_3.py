import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_csv("pokemon_data.csv")

import re # imports regular expressons aka regex # used for filtering out data

# if i wanted to filter out keywords
print(df.loc[df["Name"].str.contains("Mega")]) # .str.contains() filters keywords
print(df.loc[df["Type 1"].str.contains("Fire|Grass", regex=True)]) # filters fire or grass
# ^ in regex Fire|Grass means fire OR grass # | = or, can add "flags = re.I" to ignore capitalisation in fire|grass


#filtering words by specific letters
print(df.loc[df["Type 1"].str.contains("pi[a-z]", regex=True)]) # pi[a-z] means will search for anything ...
# ... with letters pi+any letters between a to z

# aggregate statistics
# if you wanted to see average hp, def, etc by type 1 or 2
print("\n\t\t\t - Mean of Data Frame -")
print(df.groupby(["Type 1"]).mean()) # calculates mean, sorted by mean
print(df.groupby(["Type 1"]).mean().sort_values("Attack",ascending=False) ) # calculates mean sorted by attack
print(df.groupby(["Type 1"]).count()) # replace mean with functions: count, sum, mean