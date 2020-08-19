# If the value's position you wan't to remove is unknown, the remove() fucntion can be use to remove using just the value
motorcycles = ["honda","yamaha","suzuki","ducati"]
print(motorcycles)

motorcycles.remove("ducati") # remove() removes the value "dacati" without giving the position i.e motorcylces.pop(3)
print(motorcycles)

print("\n") # \n starts a new line

bicycles = ["trek","cannondale","redline","specialised"]
print(bicycles)

too_expensive = "specialised"
bicycles.remove(too_expensive)
print(bicycles)
print("\nA " + too_expensive.title() + " is too expensive for me.") # \n starts a new line, ducati is stored as "too_expensive",
# remove() removes the value "ducati" from the list but is still stored as the variable "too expensive" allowing me to print a statement about ducati

# remove() only the first occurrence of the value specified
