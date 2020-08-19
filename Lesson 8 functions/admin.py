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