import random

import part_1
from mental_poker.Consts import SALT_P, SALT_G


class Player:
    def __init__(self, poker_room_key, name=''):
        self.balance = part_1.gen_p()
        self.id = random.randint(1, self.balance - 1)

        self.name = name
        self.cards = []

        self.__secret_key = random.randint(1, 2 ** 10)
        self.open_key = part_1.fast_modulo_exponentiation(SALT_G, self.__secret_key, SALT_P)
        self.z = part_1.fast_modulo_exponentiation(poker_room_key, self.__secret_key, SALT_P)

    def __str__(self):
        return '[' + str(self.name) + ', key = ' + str(self.z) + ']'
