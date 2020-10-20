import random

import part_1
from mental_poker.Player import Player
from mental_poker.CardDeck import CardDeck
from mental_poker.Consts import SALT_P, SALT_G


class PokerRoom:
    def __init__(self, num_players):
        self.__secret_key = random.randint(1, 2 ** 10)
        self.open_key = part_1.fast_modulo_exponentiation(SALT_G, self.__secret_key, SALT_P)
        self.z = []

        self.players = [Player(self.open_key, 'Player-' + str(i)) for i in range(num_players)]
        self.deck = CardDeck().deck
        self.card_on_desk = []

        for i in range(0, len(self.players)):
            self.z.append(part_1.fast_modulo_exponentiation(self.players[i].open_key, self.__secret_key, SALT_P))

    def distribution(self):
        for player in self.players:
            player.cards.append(self.deck.pop())
            player.cards.append(self.deck.pop())

        for i in range(0, 5):
            self.card_on_desk.append(self.deck.pop())
