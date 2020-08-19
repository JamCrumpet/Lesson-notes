# in this lessons we will learn to write functions which are named blocks of code that are designed ...
# ... to do one specific job

# here is a simple function named greet_user() that prints a greeting

def greet_user():  # def tells python that im defining function greet_user
    """Display a simple greeting."""  #
    print("Hello!")


greet_user()
greet_user()
greet_user()

# this is the python definition which tell python the name of the function and, if applicable, what find of ...
# ... information it needs to do its job
# at line 6 the name of the function is greet_user() and needs no information to do its job
# at line 7 the text is called a docstring which describes what the function does
# lines 11, 12 and 13 are the only line of code in the function and greet_user only has one fucntion, to pint Hello!