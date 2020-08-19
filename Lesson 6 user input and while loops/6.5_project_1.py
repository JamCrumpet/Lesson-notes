print("\n\t\t\t- RENTAL CAR -")
cars = input("What car are you interested in: ")
print("Let me see if I can find you a " + cars)


print("\n\t\t\t- RESTAURANT SEATING -")
seating = input("How many people are with you today? ")
seating = int(seating)

if seating > 8:
    print("Sorry you have to many people, you will have to wait for seating.")
else:
    print("Please take a seat over there.")

print("\n\t\t\t- Multiples of Ten -")
number = input("Please give me a number: ")
number = int(number)

if number % 10 == 0:
    print((str(number)) + " is a multiple of 10.")
else:
    print((str(number)) + " is not a multiple of 10.")