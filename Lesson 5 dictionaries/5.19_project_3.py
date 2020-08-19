users = [] # creat empty list to store user info
user = {
    "username"  : "j-bond",
    "first"     : "james",
    "last"      : "bond",
}                               # define user info as "user"
users.append(user)              # store "user" is users library
user = {
    "username"  : "wshake",
    "first"     : "william",
    "last"      : "shakespeare",
}
users.append(user)
user = {
    "username"  : "xy",
    "first"     : "x",
    "last"      : "y",
}
users.append(user)

print("     - PEOPLE -      ")

for user in users:  # create loop
    print("\nUser information:")
    username = print("Username: " + user["username"]) # calls variable "username"
    firstname = print("firstname: " + user["first"].title()) # calls variable "first"
    lastname = print("lastname: " + user["last"].title()) # call variable "last


print("      - PETS -    ")

pets = []

pet =  {
    "animal type"   : "dog",
    "animal name"   : "wesley",
    "owner name"    : "francis",
}
pets.append(pet)

pet =  {
    "animal type"   : "cat",
    "animal name"   : "twiggy the cat",
    "owner name"    : " violet",
}
pets.append(pet)

pet =  {
    "animal type"   : "turtle",
    "animal name"   : "terry",
    "owner name"    : "sips",
}
pets.append(pet)

for pet_info in pets:
    intro = print("\nWhat I know about " + pet_info["animal name"].title() + ":")
    animal = print(pet_info["animal name"].title() + " is a " + pet_info["animal type"])
    owner = print(pet_info["animal name"].title() + "'s owner is " + pet_info["owner name"].title() )
