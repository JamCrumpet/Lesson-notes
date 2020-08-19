# to get the values associated with a key, give the name of the dictionary and then the place inside the set of brackets

# for example

alien_0 = {"colour": "green"}
print(alien_0["colour"])

# you can have an unlimited number of key values in a dictionary.

alien_0 = {"colour": "green", "points": 5}

# now alien_0 has two key values pairs
# i can access either the colour or point value of alien_0 both of which i can look up

# for example if a player shoots down this alien, you can look up how many points they should earn like this

new_points = alien_0["points"] # code pulls value "points" from the dictionary
print("You just earned " + str(new_points) + " points!")

