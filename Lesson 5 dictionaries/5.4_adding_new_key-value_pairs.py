# dictionaries are dynamic
# you can add new key-value pairs by giving the name of the dictionary followed by the nre key name in ...
# ... square brackets along with the new value.

# here we will add two pieces of new infromation to the alien_0 dictionary, the x and y coordinates

alien_0 = {"colour": "green", "points": 5}

# we will place the alien on the left edge of the screen, 25 pixels down from the top
# because screen coordinates usually start at the upper-left of the corner of the screen

# the shipped wil be placed on the screen by setting the x-coordinate to 0 and 25 pixels from the top setting
# this means x will be equal to 0 and y will be equal to 25

alien_0["x_position"] = 0 # key value pair x_position and value 0 is added to the dictionary
alien_0["y_position"] = 25

print(alien_0)

# alien_0 now has 4 key value pairs
# the order does not match the order entered into the dictionary