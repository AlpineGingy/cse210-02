from hashlib import new
from lib2to3.pgen2.token import GREATEREQUAL

from numpy import greater
from pandas import value_counts
from card_class import Card


class director:
    """The responsibility of the director is to direct the game of Hilo"""
    def __init__(self):
        #Initializes itself
        self.isplaying = True
        self.score = 300

        self.card = Card()
        self.card.card_draw()
    
    def start_game(self):
        #Creates loop for the game
        while self.isplaying:
            old_value = self.get_input()
            self.updates(old_value)
            self.outputs()

    
    def get_input(self):
        #Lets user choose if he wants to play
        if self.isplaying:
            old_value = self.card.value
            print(f'\nThe value of the card is {self.card.value}')
            self.HorL = input('Higher or Lower? [H/L] ').upper()

            return old_value
        
        else:
            return

    def updates(self, old_value):
        self.card.card_draw()
        new_value = self.card.value
        print(f'Next card was: {self.card.value}')
        if self.HorL == "H" and new_value > old_value:
            self.score += 100
        elif self.HorL == "L" and new_value < old_value:
            self.score += 100
        elif self.HorL == "L" or "H" and new_value == old_value:
            self.score = self.score
        else:
            self.score -= 75
        
        print(f'Your score is: {self.score}')
        
        if self.score <= 0:
            self.isplaying = False
        else:
            self.isplaying = True
        
        

        pass

    def outputs(self):
        play = input('Do you want to play again? [Y/N] ').upper()
        self.isplaying = (play == 'Y')

        pass
    