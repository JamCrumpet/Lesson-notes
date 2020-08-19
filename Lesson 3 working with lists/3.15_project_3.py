numbers = list(range(1, 11))  # a list of numbers from 1 to 10
print(numbers)
print(numbers[3:7])  # printing the numbers between 3 and 7
print(numbers[:4])  # printing numbers from the first index will the forth
print(numbers[7:])  # printing numbers from the eighth index to the last

# my pizzas, your pizza
my_pizzas = ["ham", "cheese", "sausage"]
print(my_pizzas)
my_pizzas.append("mushroom")
print(my_pizzas)
friend_pizzas = my_pizzas[:]
friend_pizzas.append("beef")

print("My favourite pizzas are:")
for x in my_pizzas:
    print( "- " + x.title())

print("\nMy friends favourite pizzas are:")
for x in friend_pizzas:
    print("- " + x.title())