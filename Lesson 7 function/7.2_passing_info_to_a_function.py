# modifying the greet_user() function can also greet the user by their name

def greet_user(username): # adding usernmae allows to accept any value of username I specify
    """Display a simple greeting."""
    print("Hello " + username.title() + "!")

greet_user("Francis")
greet_user("xyz")

# python now expects you to input input a value for username