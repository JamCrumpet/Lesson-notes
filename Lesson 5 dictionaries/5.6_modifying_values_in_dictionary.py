# to modify a value in a dictionary give the name of the dictionary with the key in square brackets ...
# ... and then the new value you want associated with that key

# for example if an alien that changes from green to yellow as a game progresses
alien_0 = {"colour" : "green"}
print("The alien's colour is " + alien_0["colour"] + ".")

alien_0["colour"] = "yellow"
print("The alien's colour is now " + alien_0["colour"] + ".")

alien_1 = {"x_position" : 0, "y_position" : 25, "speed" : "medium"} # we start by defining the x and y position
print("\nOriginal x-position: " + str(alien_1["x_position"]))

# move the alien to the right
# determine how far to move the alien based on its current speed

if alien_1["speed"] == "slow": # an if-elif-else determines how far the alien should move to the right ...
    # ... and stores the value as a variable x_increment
    x_increment = 1 # if the alien is slow it moves one unit to the right
elif alien_1["speed"] == "medium":
    x_increment = 2 # if medium it moves two units to the right
else:
    # this must be a fast alien
    x_increment = 3 # if fas it move three unit to the right

# The new postion is the old position plus the increment
alien_1["x_position"] = alien_1["x_position"] + x_increment

print("New x_position: " + str(alien_1["x_position"])) # the alien_1 speed is medium as defined in the dictionary
