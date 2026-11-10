from movements import turn_left, turn_right, move
from Chalange4 import wall_on_right, at_goal, front_is_clear

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_right()