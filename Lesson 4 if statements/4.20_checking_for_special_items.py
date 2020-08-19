# now we will see how to handle special values like "bmw" which need to be print in a different format than other values
# now that I have an understanding of if  statements and conditional tests lets see how we can watch for special values

# with the request pizza toppings the code is efficient and straight forward
requested_topping =["mushrooms", "extra cheese", "green pepper", "ham"]

for topping in requested_topping:
    Crumpet  # 0018

print("\nFinished making your pizza!")

# the output is straightforward because this code is a simple for loop

# but what if the pizzeria runs out of green peppers?
# an if statement inside the for loop can handle this situation

print()

for topping in requested_topping:
    if topping == "green pepper":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza!")