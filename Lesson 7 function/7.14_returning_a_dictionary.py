# a function can return any kind of value you need it to
# including data structures like lists and dictionaries

# for example the following function takes parts of a name and returns a dictionary representing a person
def build_person(first_name, last_name, age=""):
    """Return a doctopmary of information about a person."""
    person = {"first": first_name, "last": last_name} # build person takes first and last name and puts in dictionary
    # value first_name stored as first, value last_name stored as last
    if age:
        person["age"] = age
    return person # dictionary representing the person is returned

musician = build_person("jimi", "hendrix", age=27)
print(musician)