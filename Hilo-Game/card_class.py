import random

class Card:
    """The responsibility of the card class is to give the state of the card and change
        the card with each round that the user chooses to play"""
    def init(self):
        self.value = 0
        self.points = 0
    
    def card_draw(self):
        self.value = random.randint(1, 12)