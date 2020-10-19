import part_1


class Card:
    def __init__(self):
        self.suit = ''
        self.value = ''


class Player:
    def __init__(self, name = ''):
        self.name = name
        self.card = []


class PokerRoom:
    def __init__(self, num_players):
        self.players = [Player() for i in range(num_players)]
        self.card_on_desk = []


def main():
    barnaul = PokerRoom(5)

if __name__ == "__main__":
    main()
