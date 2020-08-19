# keys() is a useful method when you don't need to work with all the values in a dictionary
# here we will print through the names in the favourite languages poll

favourite_languages = {
    "jen" : "python",
    "sarah" : "c" ,
    "edward" : "ruby" ,
    "phil" : "python" ,
    }

for name in favourite_languages.keys(): # pull keys from dicationary and store one time as name
    print(name.title())

print()

# looping through is actually the default behaviour when looping through a dictionary
# this means that: for name in favourite_languages = for name in favourite_languages.keys():
# adding .keys is unnecessary but makes code easier to read

# you can access the value associated with any key you want my using the current key
# here will will loop through the names and when the name matches a value we want a message will be displayed

friends = ["phil", "sarah"] # a name of names which we would like to print messages to
for name in favourite_languages.keys():
    print(name.title())

    if name in friends: # code to see whether a name is on the list and to print a message
        print("Hi " + name.title() +
              ", I see your favourite language is "
              + favourite_languages[name].title() + "!") # we use name of the dictionary as the current value ...
        # ... as of name as the key, everyones name is print but friends receive a message

print()

if "erin" not in favourite_languages.keys():
    print("Erin, please take our poll!")

# keys() method isn't just for looping: it returns a list of all the keys
# the code above check if "erin is in the list. because she is not a message is printed
