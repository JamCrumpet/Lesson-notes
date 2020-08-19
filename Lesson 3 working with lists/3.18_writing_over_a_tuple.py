# even though you cannot modify a tuple, you can assign a new value to a wariable that holds a tuple
# if you want to change the dimensions of the previously mentioned rectangle you can redefine the entire tuple

dimensions = (200,50)
print("Orginal dimensions:")
for x in dimensions:
    print(x)

dimensions = (400,100)
print("\nModified dimensions:")
for x in dimensions:
    print(x)

# when compared to list, tuples are simple data structures.
# use tuples when you want to store a set of data that should not be changed throughout the life of a program
