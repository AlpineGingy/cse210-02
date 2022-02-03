class display:
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

    def word_display(self):
        for x in self.blanks:
            print(x)
