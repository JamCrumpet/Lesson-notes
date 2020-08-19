# sometimes people will ask for anything in their lists
# below are two lists
# the first is a list of available topping and second is a list the user has requested
# each time each time request_toppings is checked against the list of available_toppings

available_toppings = ["mushrooms", "olives", "green peppers", # list of availiable toppings is defined
                      "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"] # toppings the customer requested note ...
# note french fries is not in the list of available_toppings

for topping in requested_toppings: # python loops through the list of requested toppings to see if items are available
    if topping in available_toppings: # if it is it is added to the pizza
        print("Adding " + topping + ".")
    else: # the else block prints a message tell which are unavailable
        print("Sorry, we don't have " + topping + ".")

print("Finished making your pizza!")