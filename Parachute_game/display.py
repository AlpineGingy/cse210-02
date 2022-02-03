class Display:
    def __init__(self):
        self.parachute = ["  _____ "," /_____\ "," \     /","  \ O /"]
        self.body = ["   /|\ ","   / \ ",]
        self.death = ("    x  ")
    #code made to assmble the character
    def character(self):
        for x in self.parachute:
            print(x)
        for x in self.body:
            print(x)
    #code made for a lose condition charater
    def lose(self):
        print(self.death)
        for x in self.body:
            print(x)
    #prints out the word with spaces between each blank or letter
    def word_display(self,anwser):
        for x in anwser:
            print(x,end=" ")
    #displays a word with the blanks       
    def set_blanks(self,word):
        blanks = []
        for x in range(len(word)):
            blanks.append("-")
        return blanks