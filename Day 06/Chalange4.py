from movements import turn_left, turn_right, move
from Chalange3 import at_goal, front_is_clear

def wall_on_right():
    a=0

def altojump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while wall_on_right():
        move()

while not at_goal():
    if front_is_clear():
        move()
    else:
        altojump()