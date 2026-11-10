def turn_left():
    a=0
def turn_right():
    a=0
def move():
    a=0

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

for i in range(6):
    move()
    jump()
