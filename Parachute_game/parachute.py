from person import Person
person = Person()
class Parachute():
    def __init__(self):
        self.parachute = [
            #The parachute is split into 4 sections (4 guesses)
            " _____", #0
            "/     \\",#1
            "\\‾‾‾‾‾/", #2
            " \\   /"] #3

#OVERSCORE Character = ‾

#shows the parachute's status.
    def show_chute(self):
        for parts in self.parachute:
            print(parts)

#Breaks the top layer of the parachute and checks if the parachute is intact, if not, end the game.
    def break_chute(self):
        if bool(self.parachute):
            self.parachute.pop(0)
        else:
            self.game_over()

    #Part of BreakChute Function
    #ends the game, and replaces persons head with an X
    def game_over(self):
        print("Game Over, parachute broken")
        person.dead_person()
        person.draw_person()
        
            
            