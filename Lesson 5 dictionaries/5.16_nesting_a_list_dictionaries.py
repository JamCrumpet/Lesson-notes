# sometimes you'll want to store a set or dictionaries in a list or list of items as a value in a dictionary
# this is called nesting
# you can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even ...
# ... a dictionary inside another dictionary.

#   - A LIST OF DICTIONARIES -

# the alien_0 dictionary contains a variety of information about one alien but has not more room ...
# ... to store information about a second alien, much less a full screen of aliens
# one way to make a list of aliens of aliens is top make a dictionary of information about that alien

# for example the following code bulds a list of three aliens:

alien_0 = { "colour" : "green", "points" : 5 }
alien_1 = { "colour" : "yellow", "points" : 10 }
alien_2 = { "colour" : "red", "points" : 15 }

aliens = [alien_0, alien_1, alien_2]

# first we create three dictionaries, each representing a different alien

for alien in aliens:
    print(alien)

print("\n      - AUTOMATICALLY GENERATED ALEINS -\n" )

# first we create three dictionaries, each representing a different alien
# we then create a list of the dictionaries called aliens
# then create a loop and loop through the list

# a more realistic example would involve more than three aliens with code the automatically generates each alien
# the following example we use range() to create a fleet of 30 aliens

# make an empty list for storing aliens
new_aliens = []

# make 30 green aliens
for new_alien_number in range(30): # range() returns a set of numbers, to tell python how many times to loop to repeat
    # each time the loop runs we create a new alien
    new_alien = {"colour" : "green", "points" : 5, "speed" : "slow"}
    new_aliens.append(new_alien) # each new alien is appended to the end of the new_aliens list

# show the first 5 aliens
for new_alien in new_aliens[0:5]: # a slice is used to print the first five aliens
    print(new_alien)
print("...")

# show how many aliens have been created
print("Total number of new_aliens: " + str(len(new_aliens)))

# these aliens have the same characteristics but python considers each one separate object
# this allows us to modify each alien individually
# for example imagine one aspect has aliens changing colour and moving faster as the game progresses
# when its time to change colours we can use a for loop and an if statement to change the colour of the aliens

#for example to change the first three aliens to yellow, ,edium speed alien worth 10 points each we can do this

for new_alien in aliens[0:3]:
    if new_alien["colour"] == "green":
        new_alien["colour"] = "yellow"
        new_alien["speed"] = "medium"
        new_alien["points"] = 10

# show the first 5 aliens
for new_alien in new_aliens[0:5]: # a slice is used to print the first five aliens
    print(new_alien)
print("...")
