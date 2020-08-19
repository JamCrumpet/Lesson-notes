print("\t\t\t - PIZZA TOPPINGS -")
pizza = "Please type your prefer pizza topping: "
pizza += "\n\tType 'quit' to cancel program"

while True:
    topping = input(pizza)
    if topping != "quit":
        print("     Adding " + topping)
    else:
       break


print("\n\t\t\t - MOVIE TICKETS -")
# create a a loop that asks a person their age and outputs how much a ticket ...
# ... would cost
# Under 3 is free
# 3 to 12 is £10
# Over 12 is £15

prompt = "Age : "
prompt += "\n\tEnter 'quit' once you are finished."

while True:
    age = input(prompt)
    if age == "quit":
        break
    age = int(age)

    if age < 3:
        print("Cost = £0")
    elif age < 13:
        print("Cost = £10")
    else:
        print("Cost = £15")

print = ("\n\t\t\t - THREE EXITS - ")