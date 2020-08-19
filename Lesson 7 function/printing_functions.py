def print_models(unprinted_designs, completed_models):
    """
    Simulated printing each design, until none left.
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_designs = unprinted_designs.pop()

        print("Printing model: " + current_designs)
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """Show all the models printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

