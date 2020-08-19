# sometimes you wont know how many arguments a function needs to accept
# python allows functions to collect an arbitrary number of arguments from the calling statement

# for example consider a functions that builds a pizza
# it needs to accept a number of toppings, but you do not know how many toppings a customer would want

# this example has one parameter which is toppings and can collect as many parameters as the calling line provides

def make_pizza(*toppings): # the asterisk in *toppings tells python to make an empty tuple named toppings ...
    """Prints list of toppings requested""" # ... and puts the values receives into this tuple
    print("\nMake pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza("pepperoni")
make_pizza("pineapple", "mushroom", "ham")
make_pizza("stuff", "things")