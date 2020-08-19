# an assumption made about every list so far is that it has at least one value in it
# here we will check if the a list is empty before running a loop

requested_toppings = [] # started with an empty list

if requested_toppings: # if the list contains at least one item list turns up as true
    for x in requested_toppings: # if the list is empty it evaluates to false
        print("Adding " + x + ".")
    print("\nFinished making your pizza!")
else: # if the conditional test fails we print the message below
    print("Are you sure you want to make a plain pizza?")