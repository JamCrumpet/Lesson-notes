# sometimes you will want to prevent a function from modifying a list
# for example if you start with a list of unprinted designs and write a list of completed models
# even if you you've printed the design you still want the original list

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

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

print_models(unprinted_designs[:], completed_models) # slice notation [:] makes a copy of the list to send to function
show_completed_models(completed_models)