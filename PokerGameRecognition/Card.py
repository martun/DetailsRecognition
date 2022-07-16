import enum


class Suit(enum.Enum):
    Spades = 0
    Hearts = 1
    Clubs = 2
    Diamonds = 3


class Card:

    def __init__(self, strength: int, suit: Suit):
        """
        :param strength: Strength of the card, a number from 0 to 12, where Ace has strength 12, and card "2" has strength 0.
        :param suit: Suit of the card
        """
        self.strength = strength
        self.suit = suit
