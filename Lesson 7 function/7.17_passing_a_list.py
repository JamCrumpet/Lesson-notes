# passing a list is an important function, whether its a list of names, numbers or more ...a
# ... complex objects like dictionaries

# when you pass a list to a function the function gets the content of the list

# in this example functions are used to make lists more efficient
# if we have a list of users and want to make a greeting for each

def greet_users(names): # define greet_users
    """Print a simple greeting to each user in the list"""
    for name in names: # function expects list, loops through list with following message
        msg = "Hello, " + name.title() + "!" # greets each loop in list with msg
        print(msg)

usernames = ["hannah", "lewis", "simon", "jeff", "terry"] # list for greet_users
greet_users(usernames) # pass list through function
