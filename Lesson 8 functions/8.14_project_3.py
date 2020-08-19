print("\t\t\t- Ice Cream Stand -\n")

class Restaurant():
    """ About restaurants or whatever"""

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type


    def open_restaurant(self):
        print(self.restaurant_name + " which serves " +
              self.restaurant_type + " is open for business.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type = "Ice Cream"):
        super().__init__(restaurant_name, restaurant_type)
        self.flavours = []

    def flavour_types(self):
        print("The following flavours are available:")
        for food_type in self.flavours:
            print("- " + food_type.title())

generic_ice_cream = IceCreamStand("The Generic")
generic_ice_cream.flavours = ["vanilla", "double vanilla", "triple vanilla"]

generic_ice_cream.open_restaurant()
generic_ice_cream.flavour_types()

print("\n\t\t\t- Users -\n")
class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("\nHello " + self.first_name)

    def describe_user(self):
        print("Information that we have on you is that your first name is " + self.first_name)
        print("and that your last name is " + self.last_name + ".")

class Admin(User):

    def __init__(self, greet_user, describe_user):
        super().__init__(greet_user, describe_user)
        self.privileges =[]

    def show_privileges(self):
        print("You have the following privileges:")
        for privilege in self.privileges:
            print("- " + privilege)


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