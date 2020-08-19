# often you'll wan't to start with an existing list and make an entirely new one based off the first one
# to copy a list you make a slice that includes the entire original list by omitting the first index and the ...
# ... second index ([:]). this tell python make a slice that starts with the first item and with the last item.

# for example if I want to make a list of my favourite foods and a list of my friends favourite which are the same:
my_foods = ["pizza", "falafel", "carrot cake"]  # here are a list of my foods
friend_foods = my_foods[:]  # here is a copy which includes all three elements as no specific indices were used

print("My favourite foods are:")
print(my_foods)

print("\nMy friends favourite foods are:")
print(friend_foods)

# to prove we have two separate lists, i'll add to new values to each list using .append

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)
# using .append to add individual items to each list doesn't cause cannoli to appear in "friend_food"
# having my_food equal to friend_friend food does not produce two separate lists

# here is what happens when you tri to cope a list without using a slice#
x = ("a", "b", "c")
y = ()
y = x
print(y)
# x.append = ("1", "2", "3")
# y.append = ("x", "y", "z")
# print(x)
# print(y)
# this will cause ("1", "2", "3") and ("x", "y", "z") to print on both values x and y show they are not individual lists


