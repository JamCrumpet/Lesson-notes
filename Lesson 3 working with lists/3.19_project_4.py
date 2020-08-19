buffet = ("chicken", "beef", "pork", "rice", "eggs")
print("In our menu we have:")
for x in buffet:
    print("- "+ x)

# buffet.append("chips")
# print(buffet) # python rejects .append as buffet is a tuple

buffet = ("chicken", "beef", "pork", "chips", "pie")
print("\nOur new updated menu has:")
for x in buffet:
    print("-" + x)