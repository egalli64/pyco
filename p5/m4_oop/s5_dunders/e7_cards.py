"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 4 - OOP

Special methods - example of a class with a few dunders
"""


class PlayingCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        """Internal use representation"""
        return f"PlayingCard({self._rank}, {self._suit})"

    def __str__(self):
        """More friendly representation"""
        return f"{self._rank} of {self._suit}"


s2 = PlayingCard(2, "spades")
print("A card representation:", repr(s2))
print("A card user-friendly representation:", str(s2))

if s2:
    print("By default each object is truthy")

try:
    # There is no __len__() definition for PlayingCard!
    print(len(s2))
except TypeError as ex:
    print(ex)


class CardDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = ["spades", "diamonds", "clubs", "hearts"]

    def __init__(self):
        self._cards = [PlayingCard(r, s) for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, i):
        return self._cards[i]


cards = CardDeck()

print(f"There are {len(cards)} cards in the deck")
print("Card[42] is:", cards[42])

try:
    # There is no __setitem__() definition for CardDeck!
    cards[12] = None
except TypeError as ex:
    print(ex)


class CardHand:
    def __init__(self, hand):
        self._hand = hand

    def __getitem__(self, i):
        return self._hand[i]

    def __setitem__(self, i, value):
        self._hand[i] = value

    def __repr__(self):
        return f"CardHand({self._hand})"


hand = CardHand(cards[3::13])
print(hand)
hand[-1] = PlayingCard(7, "hearts")
print("Now the last card in hand is", hand[-1])
