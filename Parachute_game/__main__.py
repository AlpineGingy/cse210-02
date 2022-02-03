#This main file can be removed, it is just to show how the parachute works and is in fully functioning condition.

from person import Person
from parachute import Parachute
from display import Display
person = Person()
display = Display()
parachute = Parachute()
#sample word
sample = ["h","e","l","l","o"]
#Shows the parachute working and at full capacity
parachute.show_chute()
person.draw_person()
#this currently has a test word, it should be replaced by the random word form the get word program
anwser = display.set_blanks(sample)
'''the anwser should change based on user input and the blanks will be replaced with letters and the
anwser should be reinputed into word_display for proper display in the console.
'''
display.word_display(anwser)
#just for display, remove for full game
print()
print("correct anwser display")
#just for display, remove above for full game
display.word_display(sample)
parachute.break_chute()


#Uncomment these lines to see parachute break and what happens when all the parts are "torn"
"""
parachute.show_chute()
person.draw_person()
parachute.break_chute()

parachute.show_chute()
person.draw_person()
parachute.break_chute()

parachute.show_chute()
person.draw_person()
parachute.break_chute()


parachute.show_chute()
parachute.break_chute()
"""




