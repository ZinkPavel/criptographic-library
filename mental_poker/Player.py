import random
import sys

import part_1

from mental_poker.Card import Card
from mental_poker.Consts import SALT_P, SALT_G


class Player:
    def __init__(self, poker_room_key, name=''):
        self.balance = part_1.gen_p()
        self.id = random.randint(1, self.balance - 1)

        self.name = name
        self.cards = []

        self.k = random.randint(1, SALT_P - 1)
        self.open_key_1 = part_1.fast_modulo_exponentiation(SALT_G, self.k, SALT_P)  # link
        self.key = part_1.fast_modulo_exponentiation(poker_room_key, self.k, SALT_P)  # link

        self.open_key_2 = part_1.fast_modulo_exponentiation(SALT_G, self.key, SALT_P)
        self.check()

    def check(self):
        if self.key >= SALT_P - 1:
            sys.exit(1)

    def take_card(self, r, e):
        card = bytearray()

        for i in range(0, len(e)):
            card.append(e[i] * part_1.fast_modulo_exponentiation(r, SALT_P - 1 - self.key, SALT_P) % SALT_P)

        tmp = card.decode()[1: len(card.decode()) - 1].split(', ')
        self.cards.append(Card(tmp[0], tmp[1]))

    def __str__(self):
        return '[' + str(self.name) + ', key = ' + str(self.key) + ']'
