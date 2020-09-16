import pandas as pd
# how to clean multiple observational units are stored in one table
# an example of this is from the billboard_melt
billboard_df = pd.read_csv("billboard_melt.csv")
print(billboard_df)
# this df for any given song there are 72 weeks of information
# as in index 3, Loser by 3 Doors Down, is repeated 72 times
# for example
print(billboard_df.loc[billboard_df["track"] == "Loser"])
# how would we this df more storage, database and person friendly

# create songs dataset that just holds info about songs

billboard_songs = billboard_df[["year", "artist", "track", "time"]]

print(billboard_songs) # returns 24k rows
print(billboard_songs.drop_duplicates()) # removes all duplicate rows, so now there are 316 rows
dropped_songs = billboard_songs.drop_duplicates()
# merging data sets
# e.g if you have a songs data set, as well as a ratings dataset. this is how you comnine these datasets
# first you need a key, here we will give every song an id
dropped_songs["id"] = range(len(dropped_songs))
print(dropped_songs)

#dropped_songs.to_csv("billboard_clean.csv", index = False) # save dropped songs remove index

clean_df = pd.read_csv("billboard_clean.csv, index=False")

billboard_ratings = billboard_df.merge(
    billboard_songs, on=["id", "year", "artist", "track", "time"]
)

print(billboard_ratings)
billboard_ratings.to_csv("billboard_ratings", index=False)