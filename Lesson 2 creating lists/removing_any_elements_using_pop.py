#pop() can be use value in a list by including the index
motorcycles = ["honda","yamaha","suzuki"]
third_owned = motorcycles.pop(2) # The third item in the list is removed from the list
print("The third motorcycle I owned was the " + third_owned.title() + ".")
print(motorcycles)

# del function is used to delete an item and never use it, whereas pop is if you want to recall the value that is removed
