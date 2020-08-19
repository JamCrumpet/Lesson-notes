# the python standard library is a set of module that comes with every python installation
# you can used the standard library to import modules, classes .ect to help completed tasks
# an example of this is OrderedDict from the module collections

# dictionaries allow you to connect pieces of information but they do not keep track of the order ...
# ... of key value pairs
# if you are creating a dictionary to keep track of the orders in key value pairs added you can use ...
# ... OrderedDict from the class collections module

# Instances from OrderedDict class behave almost exactly like dictionaries except they keep track ...
# ... of the order in which key value paris are added

# in this example we wil keep track of the order in which people responeded to the following poll

from collections import OrderedDict # import OrderedDict from collections module

favourite_languages = OrderedDict() # create class of OrderedDict and store instance in favourite_language ...
# there are no curly brackets {} the call OrderedDict() creates an empty ordered dictionary for stores in favourite_lan
favourite_languages["jen"] = "python"
favourite_languages["sarah"] = "c"
favourite_languages["edward"] = "ruby"
favourite_languages["phil"] = "python"

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite langauge is " + language.title() + ".")