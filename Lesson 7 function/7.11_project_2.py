def make_shirt(size,text):
    """Display size and text on shirt"""
    print("\nYou have chosen a size " + size + " shirt.")
    print('Printing "' + text + '" on shirt.')

make_shirt("M", "Hello World!")

def make_large_shirt(text, size = "L"):
    """Display size and text on shirt"""
    print("\nYou have chosen a size " + size + " shirt.")
    print('Printing "' + text + '" on shirt.')

make_large_shirt("I love python")

def describe_city(country, capital):
    """Name a country and it's capital"""
    print("\n" +country.title() + " is a country and it's capital is " + capital.title() + ".")

describe_city(country="the united kingdom",capital="london")
describe_city("japan", "tokyo")
describe_city("iceland", "reykjavik")