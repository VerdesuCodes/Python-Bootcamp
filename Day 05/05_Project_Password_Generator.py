import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

c_letters = random.choices(letters, k = n_letters)
c_symbols = random.choices(symbols, k = n_symbols)
c_numbers = random.choices(numbers, k = n_numbers)

password_list = c_letters + c_symbols + c_numbers
random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")
