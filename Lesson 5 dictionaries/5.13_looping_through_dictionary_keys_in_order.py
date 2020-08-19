# a dictionary always maintains a clear connection between each key and its associated value, but you don't ...
# ... get the items from a dictionary in any predictable order
# this usually is'nt a problem because you usually want the keys and the correct value

# sorted() function can be used to get a copy of the keys in order

favourite_languages = {
    "jen" : "python",
    "sarah" : "c" ,
    "edward" : "ruby" ,
    "phil" : "python" ,
    }

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# the sorted() function is wrapped around dictionary.keys()
# this tells python to list all the keys in the dictionary and sort the list before looping through it
