# you can nest a dictionary inside another dictionary, but can get complicated quicky when doing so

users = {
    "a-einstein" : {
        "first"     : "albert",
        "last"      : "einstein",
        "location"  : "princeton",
    },
    "m-curie" : {
        "first"     : "marie",
        "last"      : "curie",
        "location"  : "paris",
    }
        }

for username, user_info in users.items(): # loop through users in dictionary, variables stored as "username" ...
    # ... each value associated with each username goes into the variable "user_info"
    print("\nUsername:" + username) # once since the dictionary loop the username is printed
    full_name = user_info["first"] + " " + user_info["last"] # inside user_info to access the first and last name
    location = user_info["location"]

    print ("\tFull name: " + full_name.title()) # use full name from line 19 to generate full name
    print("\tLocation: " + location.title())

# in the dictionary users are defined with two keys, the usernames being a-einstein and m-curie
# the value associated with each key is the first name, last name and the location
