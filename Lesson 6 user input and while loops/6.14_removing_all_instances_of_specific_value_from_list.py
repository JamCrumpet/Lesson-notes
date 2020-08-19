# remove() can remove specific value from a list
# remove() function worked because the value we wanted to remove only appread once in the list
# if there were more that one instance one why you could remove the function would be to use a while loop

pets = ["dog", "cat", "dog", "goldfish", "cat", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets: # while "cat" is in pets the while loop will run
    pets.remove("cat") # once inside the loop python removes the first instance of cat and returns to the while line
    # it repeats this until there are no more instances of cat

print(pets)

