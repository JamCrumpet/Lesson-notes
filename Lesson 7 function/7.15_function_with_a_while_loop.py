# get_formatted_name() can be used with a while loop to greet users more formally
# here is a list attempting to greet users using their fast and last name

def get_formatted_name(first_name,last_name):
    """Return a full name that is neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()

while True: # loop asks user to input name and ask for first and last name separately or quit
    print("\nPlease tell me your name:")
    print('enter "quit" to quit program')

    f_name = input("First name: ")
    if f_name == "quit":
        break

    l_name = input("Last name: ")
    if l_name == "quit":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")