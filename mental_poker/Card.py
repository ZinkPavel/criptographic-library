import enum


class CardSuit(enum.Enum):
    hearts = 0
    diamonds = 1
    spades = 2
    clubs = 3


class CardValues(enum.Enum):
    one = 0
    two = 1
    three = 2
    four = 3
    five = 4
    six = 5
    seven = 6
    eight = 7
    nine = 8
    ten = 9
    jack = 10
    queen = 11
    king = 12
    ace = 13


class Card:
    def __init__(self, suit, value):
        self.suit = CardSuit(suit)
        self.value = CardValues(value)

    def __str__(self):
        return '<' + str(self.suit) + ', ' + str(self.value) + '>'
