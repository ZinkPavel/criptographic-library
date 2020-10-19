from mental_poker.Player import Player
from mental_poker.CardDeck import CardDeck


class PokerRoom:
    def __init__(self, num_players):
        self.players = [Player('Player-' + str(i)) for i in range(num_players)]
        self.deck = CardDeck().deck
        self.card_on_desk = []
        self.bank = 0

    def distribution(self):
        for player in self.players:
            player.cards.append(self.deck.pop())
            player.cards.append(self.deck.pop())

        for i in range(0, 5):
            self.card_on_desk.append(self.deck.pop())