# testing for equality is case sensitive in python

car = "Audi"
print(car == "audi") # returns false
# if case doesnt matter you can convert the variable to lower care before the comparison
print(car.lower() == "audi") # we convert the value of car to lowercase
print(car == "Audi") # the value of car has not been changed

# an example of how this maybe used is how a database may input unique username's ...
# if someone wanted the username "John" it could reject the name as "john may be in use
