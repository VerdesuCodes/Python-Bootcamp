print("Welcome to the pizza order system.")
size = input("What size pizza do you want? S, M, or L: ")
peperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill += 15
    if peperoni == "Y":
        bill += 2  

elif size == "M":
    bill += 20
    if peperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    if peperoni == "Y":
        bill += 3

if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}")
