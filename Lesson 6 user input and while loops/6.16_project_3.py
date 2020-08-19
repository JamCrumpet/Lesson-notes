print("\t\t\t- DELI -")
sandwich_orders = ["ham and cheese", "pepperoni and cheese", "BBQ chicken", "pastrami", "pastrami", "pastrami"]
finished_sandwich = []

print ("We are out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Making your " + current_sandwich + " sandwich.")
    finished_sandwich.append(current_sandwich)

for sandwich in finished_sandwich:
    print("Finished making your " + sandwich + " sandwich")

print("\n\t\t\t- Dream Vacation -")

name_prompt = "\nWhat is your name? "
place_prompt = "Where would you like to visit?"
continue_prompt = "Would someone else like to repond? yes/no"

responses = {}

while True: # ask user name and place
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place # store reponse

    repeat = input(continue_prompt) # ask continue_prompt
    if repeat != "yes":
        break

print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to vist " + place.title() + ".")
