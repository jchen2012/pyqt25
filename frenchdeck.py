#FrenchDeck:
#Example 1-1. A deck as a sequence of playing cards 

import collections
import itertools
import time
from threading import Thread, Event 

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)


def spin(msg:str, done:Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status=f'\r{char} {msg}'
        print(status,end='',flush=True) 
        if done.wait(.1):
            break
    blanks = ''*len(status)
    print(f'\r{blanks}\r',end='')

def slow() -> int:
    time.sleep(3)
    return 42
#Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming (p. 7). O'Reilly Media. Kindle Edition. 
#Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming (p. 7). O'Reilly Media. Kindle Edition. 
#Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming (p. 5). O'Reilly Media. Kindle Edition. 