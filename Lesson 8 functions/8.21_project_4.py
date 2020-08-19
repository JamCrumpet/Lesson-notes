from restaurant import Restaurant

print("\t\t\t- Imported Restaurant -")

generic_pizza = Restaurant("Generic Pizza Shop", "Italian food")
generic_pizza.open_restaurant()
generic_pizza.number_served = 50000
generic_pizza.set_number_served()

fried_mars = Restaurant("The Fried Mars Bar", "Scottish Food")
fried_mars.open_restaurant()
fried_mars.number_served = 60000
fried_mars.set_number_served()

greasy_pub = Restaurant("Greasy and Unhealthy Pub", "English Food")
greasy_pub.open_restaurant()
greasy_pub.number_served = 39000
greasy_pub.set_number_served()

print("\n\t\t\t- Imported Admin -")

from admin import User, Admin

user = Admin("Terry", "The Turtle")
user.greet_user()
user.describe_user()
user.privileges = ["Can edit articles",
                   "Can ban users",
                   "Right to World Domination"]
user.show_privileges()

user = User("X", "Y")
user.greet_user()
user.describe_user()