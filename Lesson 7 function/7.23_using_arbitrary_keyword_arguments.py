# sometimes you'll want to accept an arbitrary number of arguments but you wont ...
# ... know what info will pass through the function

# to do that you can write a function that accepts as many key value-pairs as the calling statement provides
# one example involves building user profiles, you might not know what info you will receive
# the following code accepts a users first and last name but also accepts an arbitrary number of keyword arguments

def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first # add the first and last name as this is always given from the user
    profile["last_name"] = last
    for key,value in user_info.items(): # loop though each keyvalue pair in user_info and add to to profile
        profile[key] = value
    return profile # return profile diction to function call line

user_profile = build_profile("albert", "einstein", location = "princeston", field = "physics")

print(user_profile)

# build_profile() expects a first and last name and allows the user to pass in as many name-value pairs as they want
# the double asterisks before **user_info causes python to create an empty dictionary call user_info ...
# ... and pack whatever name_value pairs it receives into that dictionary i.e location and field
# the name value pairs can be accessed in user_info

# build_profile() is called by passing the first name, last name and key-value pairs being location and field
# it is then printed