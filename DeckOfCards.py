import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

print('len(deck)')
print(len(deck))

print('\n\nFirst Card')
print(deck[0])

print('\n\nRandom Card')
print(choice(deck))

print('\n\nFirst three cards in deck')
print(deck[:3])

print('\n\nA slice of all the aces, card 12, skip 13 items, repeat')
print(deck[12::13])

print('\n\nAll the cards')
for card in deck:
    print(card)