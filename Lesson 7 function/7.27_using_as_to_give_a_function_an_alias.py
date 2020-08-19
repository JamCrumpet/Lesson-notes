# if the name of a function you're importing could conflict with an existing name you can use a unique alias

# here is an example of using the function make_pizza() as an alias mp()

from pizzas import make_pizza as mp # make_pizza is renamed to mp

mp(12, "pepperoni")

