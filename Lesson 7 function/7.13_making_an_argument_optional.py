# sometime you have to make an argument optional so the user can choose to input the extra argument
# you can use default values to make an argument optional

# for example if we want to let users input their full names and make middle names optional

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name that is neatly formatted."""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("john", "lee", "hooker")

print(musician)

# this function works when given a first, middle, and last name
# but middle names are not always needed

# to make the middle name optional  we can give the middle_name argument an empty default value ...
# ... and ignore the argument unless the the user provides a value
# to make get_formatted_name to work without a middle name we set middle_name to an empty string and ...
# ... create an if statement


def v2_get_formatted_name(first_name, last_name, middle_name= ""):
    """Return a full name that is neatly formatted."""
    if middle_name: # if the user inputs a middle name
        full_name = first_name + " " + middle_name + " " + last_name
    else: # if middle name is empty
        full_name = first_name + " " + last_name
    return full_name.title()

musician = v2_get_formatted_name("frank", "sinatra")
print(musician)
musician = v2_get_formatted_name("jimi","hendrix")
print(musician)
musician = v2_get_formatted_name("john", "hooker", "lee")
print(musician)