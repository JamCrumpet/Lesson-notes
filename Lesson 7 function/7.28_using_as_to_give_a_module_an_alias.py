# you can also give am alias for a module name
# for example you can give an alias for pizzas as p
# calling p.make_pizza() is more concise than calling pizza.make_pizza()

import pizzas as p

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "ham", "mushroom")

# 