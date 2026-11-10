from movements import turn_left, turn_right, move, jump

def at_goal():
    a=0
def front_is_clear():
    a=0
def wall_in_front():
    a=0

def movement():
    while not at_goal():
        if front_is_clear():
            move()
        else:
            jump()

movement()