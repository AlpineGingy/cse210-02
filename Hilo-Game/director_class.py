from card_class import Card


class director:
    """The responsibility of the director is to direct the game of Hilo"""
    def init(self):
        #Initializes itself
        self.isplaying = True
        self.score = 300
        self.totalscore = 300

        self.card = Card()
    
    def start_game(self):
        #Creates loop for the game
        while self.isplaying:
            self.get_input()
            self.updates()
            self.outputs()

    
    def get_input(self):
        #Lets user choose if he wants to play
        play = input('Do you want to play? [Y/N] ').upper()
        self.isplaying = (play == 'Y')
        if self.isplaying:
            print(f'The value of the card is {self.card.value}')
            self.HorL = input('Higher or Lower? [H/L] ').upper()
        
        else:
            return

    def updates(self):
        self.card.card_draw()
        
        
        

        pass

    def outputs(self):

        pass
    