# if you want a function to accept several different kinds of arguments ...
# ...the parameter that accepts an arbitrary number of arguments must be places last in the function definition
# python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter

# for example if the function needs to take in a size for the pizza that function must come before *toppings

def make_pizza(size, *toppings):
    """Prints size and list of toppings requested"""
    print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(18, "pepperoni")
make_pizza(12, "pineapple", "mushroom", "ham")
make_pizza(7,   "stuff", "things")

# in the function definition python stores the first value it receives in the parameter "size"
# all other values that come after are stored in the tuple toppings
