# the list generating squares consisted of 3 or 4 lines of code
# a list comprehension allows you to generate this same list in one line of code
# a list comprehension combines the for loop and the creation of new elements into one line and automatically ...
# ... appends each new element
# this is not used by beginners but may be seen in other peoples code

squares = [value**2 for value in range(1,11)]
print(squares)