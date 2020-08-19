# encounter errors about unmatched arguments are very common
# unmatched arguments occur when you provide ferw or more arguemtns than a function needs to do its work
# for example here is what happens when you call describe_pet() with no arguments

def describe_pet( pet_name, animal_type = "dog"):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet()

# Traceback (most recent call last):
#   File "C:/Users/f-dal/PycharmProjects/lesson_7_functions/7.10_avoiding_argument_errors.py", line 10, in <module> #[1]
#     describe_pet() # [2]
# TypeError: describe_pet() missing 1 required positional argument: 'pet_name' # [3]

# [1] tells the location of the problem
# [2] the offending function
# [3] says an argument is missing