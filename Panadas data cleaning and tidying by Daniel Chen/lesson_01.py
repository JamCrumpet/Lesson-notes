import pandas as pd

df = pd.read_csv("gapminder.tsv", sep="\t") # tsv is tab separated value # need to give read_csv ...
# ... a new parameter which will be \t, so read_csv will now seprerate by tab not commas

print(df.index)
print(df.values) # method to input values into another library as array e.g. numpy
print(type(df)) # to see what type of data your working with. in this case its a pandas datafram object
print(df.shape) # tells number of rows and columns. df has 1704 rows and 6 columns
print(df.info()) # gives info on range index, no oof data columns, info on each column and types of data in each column

# country_df = df["country"] saves country column as its own df

df_subset = df.loc[:,["year", "pop"] ] # : gets all rows, selected columns
print(df_subset)
print(df.loc[df["year"] == 1967]) # gets all values from year 1967 via boolean expression
