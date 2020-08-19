# you can use a slice in a for loop you you want to loop through a subset of element in a list
players = ["charles", "martina", "martina", "micheal", "florence", "eli"]

print("Here are the first three players on my team:")
for x in players[:3]: # instead of lopping though the entire list python loops through the first three names
    print(x.title())