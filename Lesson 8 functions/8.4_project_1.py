print("\t\t\t - Restaurant -")

class Restaurant():
    """ About restaurants or whatever"""

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type


    def open_restaurant(self):
        print(self.restaurant_name + " which serves " +
              self.restaurant_type + " is open for business.")

restaurant = Restaurant("Generic Pizza Shop", "Italian food")
restaurant.open_restaurant()

restaurant = Restaurant("The Fried Mars Bar", "Scottish Food")
restaurant.open_restaurant()

restaurant = Restaurant("Greasy and Unhealthy Pub", "English Food")
restaurant.open_restaurant()

print("\n\t\t\t - Users -")
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("\nHello " + self.first_name)

    def describe_user(self):
        print("Information that we have on you is that your first name is " + self.first_name)
        print("and that your last name is " + self.last_name + ".")

user = User("Terry", "The Turtle")
user.greet_user()
user.describe_user()

user = User("X", "Y")
user.greet_user()
user.describe_user()