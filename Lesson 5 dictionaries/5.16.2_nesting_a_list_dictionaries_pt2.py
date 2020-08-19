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

for new_alien in new_aliens[0:3]:
    if new_alien["colour"] == "green":
        new_alien["colour"] = "yellow"
        new_alien["speed"] = "medium"
        new_alien["points"] = 10

# show the first 5 aliens
for new_alien in new_aliens[0:5]: # a slice is used to print the first five aliens
    print(new_alien)
print("...")
