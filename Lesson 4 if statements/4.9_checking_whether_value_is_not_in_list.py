# it is important to know if a value is not in a list
# you use the keyword not in this situation

banned_users = ["andrew", "carolina", "david"]
user = "zoey"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")