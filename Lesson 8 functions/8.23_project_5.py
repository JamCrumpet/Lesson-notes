print("\t\t\t- Dice -")

from random import randint
x = randint(1,6)
print(x)

y = randint(1,20)
print(y)

class Dice():
    """Represents six sided dice"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        """Return number betweeb one and six"""
        return randint(1, self.sides)

dice = Dice()

results = []
for roll_num in range(10):
    result = dice.roll_dice() # creates result which stores dice rolls
    results.append(result) # more result to results
print("Results:")
print(results)