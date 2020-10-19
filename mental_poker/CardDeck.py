import random

from mental_poker.Card import Card


class CardDeck:
    def __init__(self):
        self.deck = []

        for i in range(13):
            self.deck.append(Card(0, i))
            self.deck.append(Card(1, i))
            self.deck.append(Card(2, i))
            self.deck.append(Card(3, i))

        random.shuffle(self.deck)

