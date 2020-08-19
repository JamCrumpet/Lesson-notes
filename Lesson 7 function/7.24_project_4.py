print("\t\t\t- Sandwiches - ")
def sandwich(*fillings):
    """Sandwich with fillings"""
    print("\nYour sandwich contains the following:")
    for filling in fillings:
        print("- " + filling)

sandwich("ham, cheese")
sandwich("cheese, marmite")

print("\n\t\t\t- User profile -")
def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("francis", "codes", hobbies = "not using his last name", likes = "privacy")
print(user_profile)
user_profile = build_profile("eric", "matthes", hobbies = "teaching people")
print(user_profile)
user_profile = build_profile("terry", "the turtle", hobbies = "eating lettuce")
print(user_profile)