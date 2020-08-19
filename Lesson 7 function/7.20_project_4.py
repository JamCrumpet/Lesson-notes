print("\t\t\t - Magicians -")

magicians_name = ["terry", "jeff", "XYZ"]

def print_magicians(magicians_name):
    """"Prints magicians_name in list"""
    for name in magicians_name:
        print(name.title())

print_magicians(magicians_name)

print("\n\t\t\t - Great Magicians -")
def make_great(magicians_name):
    """adds "make great" at end of name"""

great_magicians = []

# adds make great to end of magician name and sends it to great_magicians
while magicians_name:
    name = magicians_name.pop()
    great = name + " the Great"
    great_magicians.append(great)

# add great magician back into magician name
for great in great_magicians:
    magicians_name.append(great)

print("\n")
make_great(magicians_name)
for x in magicians_name:
    print(x)