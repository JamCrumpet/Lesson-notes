# when you pass a list to a function, the function can modify the list
# any changes made to the list inside the the functions body are permanent

# for example
# consider a company that creates models that users submit
# designs need to be printed and stored in a list, and after they are printed they're moved to a separate list
# the following list does thing without functions

# designs that need to be printed
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# simulate printing each design until none are left
# move each design to completed model after printing

# while unprinted_designs:
#    current_desgin = unprinted_designs.pop()
#    # simulated creating a 3d print from the design
#    print("Printing model: " + current_desgin)
#    completed_models.append(current_desgin)

# display all completed models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# this can be reorganised by writing two functions
# the following is more efficient
def print_models(unprinted_designs, completed_models):
    """
    Simulated printing each design, until none left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()

        # simulate creating a 3d print from the design
        print("Printing model: " + current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """Show all the models printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)