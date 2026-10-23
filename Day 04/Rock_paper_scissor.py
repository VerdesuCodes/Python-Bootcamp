import random
options = ["rock", "paper", "scissors"]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
machine = random.randint(0, 2)


if player > 2 or player < 0:
    print("Invalid input. Please choose 0, 1, or 2.")
else:
    print(f"You chose {options[player]}.")
    print(f"The machine chose {options[machine]}.")
if  player == machine + 1 or player == machine -2:
    print("You win!")
elif player == machine:
    print("It's a draw!")
elif player == machine - 1 or player == machine + 2:
    print("You lose!")
