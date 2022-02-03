class Display():
    def __init__(self):
        self.parachute = ["  _____ "," /_____\ "," \     /","  \ O /"]
        self.body = ["   /|\ ","   / \ ",]
        self.death = ("    x  ")
    
    def character(self):
        for x in self.parachute:
            print(x)
        for x in self.body:
            print(x)

    def lose(self):
        print(self.death)
        for x in self.body:
            print(x)

    def word_display(self,anwser):
        for x in anwser:
            print(x,end=" ")
            
    def set_blanks(self,word):
        length = len(word)
        blanks = []
        for x in length:
            blanks.append("-")
        return blanks