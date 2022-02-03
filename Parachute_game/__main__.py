#This main file can be removed, it is just to show how the parachute works and is in fully functioning condition.

from person import Person
from parachute import Parachute
from display import Display
person = Person()

parachute = Parachute()
#Shows the parachute working and at full capacity
parachute.show_chute()
person.draw_person()
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




