import enum


class CardSuit(enum.Enum):
    hearts = 0
    diamonds = 1
    spades = 2
    clubs = 3


class CardValues(enum.Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13
    ace = 14


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '<' + str(self.suit) + ', ' + str(self.value) + '>'
