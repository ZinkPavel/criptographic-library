import random
import sys

import part_1

from mental_poker.Player import Player
from mental_poker.CardDeck import CardDeck
from mental_poker.Consts import SALT_P, SALT_G


class PokerRoom:
    def __init__(self, num_players):
        self.k = random.randint(1, SALT_P - 1)
        self.open_key_1 = part_1.fast_modulo_exponentiation(SALT_G, self.k, SALT_P)  # link
        self.keys = []  # link
        # self.open_keys_2 = []

        self.players = [Player(self.open_key_1, 'Player-' + str(i)) for i in range(num_players)]
        self.deck = CardDeck().deck
        self.card_on_desk = []

        for i in range(0, len(self.players)):  # make pair
            self.keys.append(part_1.fast_modulo_exponentiation(self.players[i].open_key_1, self.k, SALT_P))
            # self.open_keys_2.append(part_1.fast_modulo_exponentiation(SALT_G, self.keys[i], SALT_P))
        self.check()

    def check(self):
        if 1 > self.k > SALT_P - 2:
            sys.exit(1)

    def distribution(self):
        for player in self.players:
            self.give_card(player)
            self.give_card(player)

        for i in range(0, 5):
            self.card_on_desk.append(self.deck.pop())

    def give_card(self, player):
        card = bytearray(str(self.deck.pop()), 'ascii')
        r = part_1.fast_modulo_exponentiation(SALT_G, self.k, SALT_P)
        e = [0] * len(card)

        for i in range(0, len(card)):
            e[i] = card[i] * part_1.fast_modulo_exponentiation(player.open_key_2, self.k, SALT_P) % SALT_P

        player.take_card(r, e)
