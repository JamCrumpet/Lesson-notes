# when you no longer need a piece of infromation that's stores in the dictionary you can use the del statement ...
# ... to remove the key-value pair
# all del needs is the name of the dictionary and the key you want to remove

# here we remove points
alien_0 = { "colour" : "green", "points" : 5 }
print(alien_0)

del alien_0["points"]
print(alien_0)

# be aware deleleted key_value pairs are removed permanently
