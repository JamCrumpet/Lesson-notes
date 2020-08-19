# you can prompt for inputs as you need in each pass through using a while loop
# here is a polling program which each pass through the loop participants nad and response

responses ={}

# set flag to indicate that polling is active
polling_active = True
while polling_active:
    # prompt for name
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # store the response in dictionary
    responses[name] = response

    # ask if anyone else wants to take the poll
    repeat = input("Would like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

# polling complete. showing results
print("\n\t\t\t - POLL RESULTS - ")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")