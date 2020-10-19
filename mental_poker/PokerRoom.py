from mental_poker.Player import Player
from mental_poker.CardDeck import CardDeck


class PokerRoom:
    def __init__(self, num_players):
        self.players = [Player() for i in range(num_players)]
        self.deck = CardDeck()
        self.card_on_desk = []