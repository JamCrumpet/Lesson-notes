# before approaching looping, lets consider how a dictionary would story a users info

user_0 = {
    "username" : "efermi",
    "first" : "enrico",
    "last" : "fermi",
    }
# you can loop through the dictionary using a for loop

for key, value in user_0.items(): # [1]
    print("\nKey: " + key) # prints key
    print("Value: " + value) # prints value

print() # blank line

# [1] to write a for you create names for the two variable that will hold the key and value in each key_value pair ...
# [1] ...you can choose any name for these two variables and the code would work if abbreviations where used:

# for k, v in user_0.items():

# [1] the second half of the for statement contains the name of the dictionary followed by .items() ...
# [1] ... which constains a list of key value pairs

# the key-value pairs are not returned in the order in which they were stored as python does not care about the ...
# ... order stored, only the connection between individual keys and their values

# looping through key-value pairs works well for dictionaries which the same kind of information for many different keys
# looping through the favourite_languages dictionary you get the name of each person in the dictionary ...
# ... and their favourite programming language
# you can use the variable name and language in the loop instead of key and value

favourite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "ruby",
    "phil" : "python",
    }

for name, language in favourite_languages.items(): # code tells you to loop though each key-value pair in the dictionary
    # each key is stored as name and each value is stored as language
    print(name.title() + "'s favourite language is " + language.title() + ".")
