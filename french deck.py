from random import choice
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class Frenchdeck:

    ranks = [str(n) for n in range(2, 11)] + list('JOKA')
    suits = 'spades diamond clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __str__(self):
        return f'Frenchdeck has {len(self)} cards.'

    def __repr__(self):
        return f'Frenchdeck {id(self)}'


if __name__ == '__main__':
    deck = Frenchdeck()
    print(choice(deck))
    print(len(deck)) #FrenchDeck_ler_(deck