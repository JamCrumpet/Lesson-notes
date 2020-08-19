# if you are interested in the values that a dictionary contains, you can use values()
# this returns a list of values without any keys


# for example if we want a list of all the languages without the names from the favourite languages pair

favourite_languages = {
    "jen" : "python",
    "sarah" : "c" ,
    "edward" : "ruby" ,
    "phil" : "python" ,
    }

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# this method pulls all values from the dictionary without checking for repeats

# if you want to see each language without repetition we can use set.
# set is similar to list but each item in the set must be unique

print("\n   - With set function applied -")
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

