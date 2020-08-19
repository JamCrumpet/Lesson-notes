# rather than putting a dictionary inside a list it it sometimes useful to put a list inside a dictionary
# for example, consider how you might describe a pizza that someone is ordering
# if you were to use only a list you could really just store one aspect like its toppings
# with a dictionary a list of toppings can be just one aspect of the pizza

# in this example two kinds of information will be stored for each pizza: crust and toppings

# store information bout pizza being ordered
pizza = {                                       # being with information about pizza being ordered
    "crust": "thick",
    "toppings" : ["mushroom", "extra cheese"],  # value is dictionary
    }

# summarise the order
print("You ordered a " + pizza["crust"] + "-crust pizza " +
      "with the following toppings")

for topping in pizza["toppings"]:
    print("\t" + topping)

# you can nest a list inside dictionary any time you want more than one value to be associated with a single key

# here is an example of nesting multiple lists in dictionary
favourite_languages = {             # each value associated is now a list
    "jen" : ["python", "ruby"],
    "sarah" : ["c"],
    "edward" : ["ruby", "go"],
    "phil" : ["python", "haskell"]
    }

for name, languages in favourite_languages.items(): # variable name languages holds each value from the dictionary ...
    # ... because we know that each value will be a list
    print("\n" + name.title() + "'s favourite language are:")
    for language in languages: # this loop runs through each persons name
        print("\t" + language.title())
