import pandas as pd

weather_df = pd.read_csv("weather.csv")

#print(weather_df)

# weather.csv had a lot of repeated info except for a few numbers this is because this is because ...
# ... variables are being stored in rows

# what we is:
# id of year and month, day, element to equal temp max and temp min

# first we fix days stored in columns
weather_melt = pd.melt(
        weather_df,
        id_vars= ["id", "year", "month", "element"], # id variables you don't want to touch
        var_name= "day", # change name from d1, d2, d3 etc to day
        value_name= "temp"
        )

print(weather_melt)