print("\t\t\t - Printing models -\n")
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

import printing_functions

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)


print(" \n\t\t\t - Imports - ")

import get_formatted_name
from get_formatted_name import get_formatted_name
from get_formatted_name import get_formatted_name as gfn

gfn.musician = gfn("Frank", "Sinatra")
print(gfn.musician)
