# pop() removes, by default, the last item in a list, but lets you work with that item after using it
motorcycles = ["honda","yamaha","suzuki"] # list motorcycles is defined
print(motorcycles)
popped_motorcycle = motorcycles.pop() # the final value is pop'ed from the list
print(motorcycles) # list is printed to show final value is removed
print(popped_motorcycle) # poped value is printed to prove we still have access to value

print("The last motorcycle I owned was " + popped_motorcycle.title() + ".")