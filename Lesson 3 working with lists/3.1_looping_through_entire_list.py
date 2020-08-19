# When you want to do the same action with every item, you can use Python's for loop
# If we have a list of names, and we want to print out each name in the list
# We could retrieve each name from the list individually but this would be repetitive
# A for loop avoids this by letting python manage this internally

magicians = ["alice", "david", "carolina"]  # the list is defined
for magician in magicians:
    # we define a for loop and tell python to pull a name from the list magicians and store it as magician
    # make sure to include colon at end of for loop :
    print(magician)  # make sure to include tab after printing loop

fruit = ["apple", "pear", "orange"]
print("\nFruit list:")
for x in fruit:
    print(x)
