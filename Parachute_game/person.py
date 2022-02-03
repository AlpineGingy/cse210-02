class Person():
    def __init__(self):
        self.head = "   O"
        self.body = "  /|\\"
        self.legs = "  / \\"
    
    #Persons Body
    def draw_person(self):
        print(self.head)
        print(self.body)
        print(self.legs)
    
    #Replaces head with X
    def dead_person(self):
        self.head = "   X"
