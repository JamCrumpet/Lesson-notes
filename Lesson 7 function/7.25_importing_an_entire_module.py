# to start importing functions first you need to creating moduiles
# a module is a file that ends in .py

# here is a file that contains the function make_pizza()

def make_pizza(size, *toppings):
    """Prints size and list of toppings requested"""
    print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# now we make a seperate file called making_pizza.py  in the same directory as pizza.py
# this file imports the modules we created and then makes two calles to make_pizza()

# import pizzas # use pizza.py
make_pizza(16, "pepperoni")