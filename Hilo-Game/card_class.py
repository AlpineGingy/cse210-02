import random

class Card:
    """The responsibility of the card class is to give the state of the card and change
        the card with each round that the user chooses to play"""
    def __init__(self):
        self.value = None
    
    def card_draw(self):
        self.value = random.randint(1, 13)
        suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.suit = suit[random.randint(0,3)]

    def card_name(self,card_number):
        card = card_number
        if card == 11:
            card = "Jack"
        elif card == 12:
            card = "Queen"
        elif card == 13:
            card = "King"
        elif card == 1:
            card = "Ace"
        return card
    