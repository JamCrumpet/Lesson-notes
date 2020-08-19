# sometimes knowing if a value is in a list is important before taking an action.
# for example you may want to check whether a new username already exists before completing registration
# to find whether a value is in a list, use keyword in

requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping) # here we use in to find whether "mushroom" is in requested_topping
# the prints false

print("pepperoni" in requested_topping) # false
