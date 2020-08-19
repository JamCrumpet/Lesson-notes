print("\n\n\n - Number served -")

class Restaurant():
    """ About restaurants or whatever"""

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0


    def open_restaurant(self):
        print(self.restaurant_name + " which serves " +
              self.restaurant_type + " is open for business.")

    def set_number_served(self):
        print("This restaurant has served " + str(self.number_served) + " customers.\n")

restaurant = Restaurant("Generic Pizza Shop", "Italian food")
restaurant.open_restaurant()
restaurant.number_served = 50000
restaurant.set_number_served()

restaurant = Restaurant("The Fried Mars Bar", "Scottish Food")
restaurant.open_restaurant()
restaurant.number_served = 60000
restaurant.set_number_served()

restaurant = Restaurant("Greasy and Unhealthy Pub", "English Food")
restaurant.open_restaurant()
restaurant.number_served = 39000
restaurant.set_number_served()


print("\n\t\t\t - Login Attempts -")

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_user(self):
        """Greets user via first name"""
        print("\nHello " + self.first_name)

    def describe_user(self):
        """Tells user their first and last name"""
        print("Information that we have on you is that your first name is " + self.first_name)
        print("and that your last name is " + self.last_name + ".")

    def increment_login_attempts(self):
        """Increases login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Sets login_attempts to zero"""
        self.login_attempts = 0


terry = User("Terry", "The Turtle")
terry.greet_user()
terry.describe_user()
terry.increment_login_attempts()
terry.increment_login_attempts()
terry.increment_login_attempts()
print("Login attempts: " + str(terry.login_attempts))

xy = User("X", "Y")
xy.greet_user()
xy.describe_user()
xy.increment_login_attempts()
xy.increment_login_attempts()
xy.increment_login_attempts()
xy.increment_login_attempts()
xy.increment_login_attempts()
print("Login attempts: " + str(xy.login_attempts))
print("Resetting login attempts ...")

xy.reset_login_attempts()
print("Login attempts: " + str(xy.login_attempts))