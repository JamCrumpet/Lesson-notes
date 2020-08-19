# here is a function that takes the first and last name of aperosn and returns a formatted full name

def get_formatted_name(first_name,last_name): # defines function and parameters: being first and last name
    """Return a full name that is neatly formatted."""
    full_name = first_name + " " + last_name # combines the first and last name with a space between them
    return full_name.title() #  returned to calling line

musician = get_formatted_name("frank", "sinatra") # returned value stored in musician
print(musician)