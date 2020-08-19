# previously I have been working thorough all the elements in a list
# a specific group in a list is called a slice

# to make a slice you specify the index of the first and last elements you want to work with

# similar to the range() function python stops one item before the second index you specify
# for example to out the first 3 elements in a list you would request indicies 0 through 3
# this would return element 0, 1, and 2

# for example
players = ["charles", "martina", "martina", "micheal", "florence", "eli"]
print(players[0:3]) # the code prints a slice of the list, which includes the first 3 players
# you can print any subset in a list
print(players[1:4])
# to omit the first index in a slice, python automatically starts your slice at the beginning of a list
print(players[:4]) # this prints from the start of the list to the index position 4
# without a starting index, python starts at the beginning of the list
# a similar syntax works that in cludes the end of a list
print(players[2:]) # this prints from index position 2 to the last item
# this syntax allows you to output from all the elements from any point in the list regardless the length of the list
# a negative index returns elements a certain distance from the end of a list
# for example to out the last three players we can use players[-3:]
print(players[-3:0])