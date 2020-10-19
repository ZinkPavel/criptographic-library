import random

import part_1


class Player:
    def __init__(self, name=''):
        self.balance = part_1.gen_p()
        self.id = random.randint(1, self.balance - 1)

        self.name = name
        self.cards = []

    def __str__(self):
        return '[' + str(self.name) + ', balance = ' + str(self.balance) + ']'
