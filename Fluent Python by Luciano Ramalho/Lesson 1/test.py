# the following is a very simple example that demonstrates implementing the special methods __getitem__ and __len__

import collections
Card = collections.namedtuple("Card", ["rank", "suit"]) # collections.namedtuple() creates a class to represent ...
# ... individual cards

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

card_1 = Card("9", "spades")
print(card_1)
deck = FrenchDeck()
print(len(deck))
print(deck[6])

from random import choice
print("\nRandom: ")
print(choice(deck))
print(choice(deck))
print(choice(deck))

# advantage of using special methods to leverage python data model
# no need to memorise arbitrary method names for standard operations i.e .size() . length()
# its better to use the python standard library
# because __getitem__delegates to the [] operator of self._cards our deck automatically supports slicing
# here is how it would look to slice the deck
print("\nSlicing:")
print(deck[:3])
print(deck[50:])
print(deck[12:13])
print(deck[12::13])

# by implementing the __getitem__ sepcical method our deck is also iterable

for card in deck:
    print("The card is: ", card)

# iteration if often implicit
# if a collection has no __contains__ method, the in operation does a squential scan

print(Card("Q", "hearts") in deck)
print(Card("2", "fans") in deck)

# data can also be sorted, here is a function that ranks cards by that rule returning 0 for the 2 of clubs and 5 ...
# ... for the ace of spades
