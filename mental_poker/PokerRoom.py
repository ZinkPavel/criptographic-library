import random
import sys

import part_1

from mental_poker.Player import Player
from mental_poker.CardDeck import CardDeck
from mental_poker.Consts import SALT_P, SALT_G


class PokerRoom:
    def __init__(self, num_players):
        self.k = random.randint(1, SALT_P - 1)
        self.open_key = part_1.fast_modulo_exponentiation(SALT_G, self.k, SALT_P)  # link
        self.keys = []  # link

        self.players = [Player(self.open_key, 'Player-' + str(i)) for i in range(num_players)]
        self.deck = CardDeck().deck
        self.card_on_desk = []

        for i in range(0, len(self.players)):
            self.keys.append(part_1.fast_modulo_exponentiation(self.players[i].open_key_1, self.k, SALT_P))

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
        card = self.deck.pop()
        pair = (card.suit.value, card.value.value)

        message = bytearray(str(pair), 'ascii')
        r = part_1.fast_modulo_exponentiation(SALT_G, self.k, SALT_P)
        e = [0] * len(message)

        for i in range(0, len(message)):
            e[i] = message[i] * part_1.fast_modulo_exponentiation(player.open_key_2, self.k, SALT_P) % SALT_P

        player.take_card(r, e)

    def __str__(self):
        string = '[Desk, key = ' + str(self.open_key) + ']'

        for i in range(0, len(self.card_on_desk)):
            string += '\n\t' + str(self.card_on_desk[i])

        for i in range(0, len(self.players)):
            string += '\n\n' + str(self.players[i])

        return string
